---
title: 시퀀스 패킹 (Sequence Packing)
category: training
page_type: concept
tags: [sequence-packing, padding, attention-mask, training-efficiency, throughput]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# 시퀀스 패킹 (Sequence Packing)

## 개요

시퀀스 패킹(Sequence Packing)은 서로 다른 길이의 훈련 시퀀스 여러 개를 하나의 고정 길이 버퍼에 이어 붙여(concatenate) 패딩(padding) 낭비를 제거하는 기법이다. 언어 모델 사전학습에서 배치 내 빈 패딩 토큰은 연산은 소비하되 학습 신호를 제공하지 않는다. 데이터 길이 분포가 고르지 않을수록 패딩 비율이 높아지고 GPU 활용도가 떨어진다.

## 패딩 낭비 문제

[[causal-language-modeling]] 사전학습에서 일반적인 미니배치 구성:

```
배치 내 예시 (max_len = 2048):
샘플 A: [tok1 ... tok512] [PAD × 1536]   ← 75% 낭비
샘플 B: [tok1 ... tok1800] [PAD × 248]   ← 12% 낭비
샘플 C: [tok1 ... tok2048]               ← 낭비 없음
```

실제 웹 데이터 기반 사전학습에서 평균 문서 길이가 수백 토큰인 경우 패딩 비율이 60-80%에 달하는 사례도 있다. 이는 곧 GPU FLOPs의 60-80%가 유효한 학습에 기여하지 않음을 의미한다.

## 패킹 메커니즘

여러 시퀀스를 하나의 버퍼 길이 $L$에 채워 넣는다:

```
패킹 후 (max_len = 2048):
버퍼: [샘플A 512 tok][샘플B 1800 tok][샘플D 236 tok 나머지]
```

```mermaid
flowchart LR
    Raw["데이터셋\n(길이 불균일)"] --> Shuffle[셔플 + 정렬]
    Shuffle --> Pack[시퀀스 연결\nFirst-Fit Decreasing]
    Pack --> Buf["패킹 버퍼\n(max_len 고정)"]
    Buf --> Mask[Attention Mask 생성\n문서 경계 마스킹]
    Mask --> Train[훈련]
```

## Attention Mask 처리: 문서 경계

패킹의 핵심 기술적 도전은 서로 다른 문서의 토큰이 서로 어텐션을 주고받지 못하도록 마스킹하는 것이다. 그렇지 않으면 문서 B의 앞부분이 문서 A의 내용을 "보게" 되어 훈련 데이터 오염이 발생한다.

### 방법 1: 블록 대각 어텐션 마스크

```
문서 경계 마스크 예시 (3문서 패킹):
     A A A B B B B C C
A  [ 1 1 1 0 0 0 0 0 0 ]   ← A는 A만 참조
A  [ 1 1 1 0 0 0 0 0 0 ]
A  [ 1 1 1 0 0 0 0 0 0 ]
B  [ 0 0 0 1 0 0 0 0 0 ]   ← B는 B만 참조
B  [ 0 0 0 1 1 0 0 0 0 ]
B  [ 0 0 0 1 1 1 0 0 0 ]
B  [ 0 0 0 1 1 1 1 0 0 ]
C  [ 0 0 0 0 0 0 0 1 0 ]   ← C는 C만 참조
C  [ 0 0 0 0 0 0 0 1 1 ]
```

블록 대각 + 하삼각(causal) 구조의 마스크를 사용한다.

### 방법 2: 포지션 ID 리셋

각 문서마다 포지션 ID를 0부터 다시 시작해 RoPE 등 위치 인코딩이 문서 경계를 넘지 않도록 한다. Flash Attention v2 이후 버전은 `cu_seqlens`(cumulative sequence lengths) 파라미터로 이 패턴을 효율적으로 지원한다.

## 패킹 전략 비교

| 전략 | 설명 | 장단점 |
|------|------|--------|
| First-Fit Decreasing | 가장 긴 샘플을 먼저 배치 | 패킹 효율 높음, 정렬 오버헤드 있음 |
| Best-Fit | 가장 잘 맞는 버퍼에 배치 | 효율 최대, 구현 복잡 |
| 단순 연결 | 순서대로 이어 붙이기 | 구현 간단, 효율 중간 |
| 길이 기반 버킷팅 | 유사 길이끼리 그룹화 | 패딩은 줄지만 패킹보다 비효율적 |

## [[distributed-training-overview]]에서의 고려사항

분산 학습 환경에서 패킹을 사용하면 각 GPU의 배치가 서로 다른 수의 실제 토큰을 포함하게 된다. 그래디언트 집계 시 토큰 수로 정규화하는 **토큰 평균 손실**을 사용해야 한다 (배치 평균이 아닌). 그렇지 않으면 작은 문서를 많이 담은 GPU가 적은 것을 담은 GPU보다 손실 기여도가 낮아지는 불균형이 생긴다.

## 미세조정(SFT)에서의 패킹

지도 미세조정(SFT) 단계에서 패킹은 더 조심해야 한다. 프롬프트-응답 쌍에서 응답(label) 부분의 손실만 계산하는 경우, 문서 경계 마스크와 함께 레이블 마스크를 동시에 올바르게 적용해야 한다. 오구현 시 크로스-오염(cross-contamination)이 발생해 모델이 랜덤 어시스턴트 응답 생성에 취약해진다.

## 실무 효과

- 패딩 비율 70%인 데이터셋에서 패킹 적용 시 처리 토큰 수 약 3.3배 증가
- GPU MFU(Model FLOPs Utilization) 개선 효과가 크며, 동일한 훈련 스텝에서 더 많은 실제 토큰 학습
- 단, 패킹으로 인한 문서 다양성 변화가 손실 랜드스케이프에 미치는 영향은 데이터셋마다 다름

## 관련 문서

- [[causal-language-modeling]] - 다음 토큰 예측 사전학습 목표
- [[distributed-training-overview]] - 분산 훈련에서의 손실 정규화
- [[flash-attention]] - cu_seqlens 기반 가변 길이 어텐션
- [[data-loader-optimization]] - 효율적인 배치 구성 전략
- [[sequence-length-curriculum]] - 길이 커리큘럼과 패킹의 상호작용
