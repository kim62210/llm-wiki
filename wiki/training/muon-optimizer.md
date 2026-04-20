---
title: Muon 옵티마이저
category: training
page_type: concept
tags: [optimizer, muon, newton-schulz, orthogonalization, adamw-alternative]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# Muon 옵티마이저

## 개요

Muon(Momentum + Newton-Schulz)은 AdamW의 대안으로 제안된 옵티마이저로, 그래디언트에 Newton-Schulz 반복법 기반 직교화(orthogonalization)를 적용해 업데이트 행렬의 스펙트럼을 고르게 만든다. Jordan Juravsky 등이 2024년에 공개한 이후 소규모 언어 모델 훈련에서 AdamW 대비 빠른 수렴 속도를 보이며 주목받고 있다.

## 핵심 아이디어

AdamW는 각 파라미터를 독립적으로 스케일링하는 좌표별(coordinate-wise) 업데이트를 사용한다. 이 방식은 구현이 단순하지만, 행렬 파라미터(예: 어텐션 프로젝션, FFN 가중치)에서는 업데이트 방향이 최적이 아닐 수 있다.

Muon는 다음 두 단계를 결합한다:

1. **모멘텀 축적**: SGD와 같이 현재 그래디언트에 모멘텀을 적용
2. **Newton-Schulz 직교화**: 모멘텀 버퍼를 대칭 행렬로 취급하고, 반복 연산으로 해당 행렬을 직교(orthogonal) 기저에 가깝게 정규화

직교화된 업데이트 행렬은 모든 특이값(singular value)이 거의 동일하도록 압축된다. 이는 특정 방향으로만 과도하게 학습되는 문제를 줄이고, 레이어 전반에 균형 잡힌 표현 갱신을 유도한다.

## Newton-Schulz 직교화

Newton-Schulz 반복법은 행렬 $A$의 극분해(polar decomposition)를 수치적으로 구하는 알고리즘이다. 목표는 $A$에 가장 가까운 직교 행렬 $U$를 찾는 것이다.

업데이트 규칙 (간략화):

$$X_{k+1} = \frac{3}{2} X_k - \frac{1}{2} X_k X_k^\top X_k$$

수 회(보통 5회) 반복하면 $X$가 직교 행렬에 빠르게 수렴한다. 전체 SVD를 계산하는 것보다 훨씬 저렴하며, GPU에서 효율적으로 벡터화할 수 있다.

## 훈련 흐름

```mermaid
flowchart LR
    G[그래디언트 g_t] --> M[모멘텀 버퍼 m_t\nm_t = β·m_{t-1} + g_t]
    M --> NS[Newton-Schulz 직교화\n5회 반복]
    NS --> U[직교화 업데이트 U_t]
    U --> P[파라미터 갱신\nθ = θ - η·U_t]
    P --> LR[학습률 스케줄러]
```

직교화 단계는 배치 그래디언트가 2D 행렬인 경우에만 적용된다. 1D 파라미터(bias, LayerNorm 등)는 AdamW 또는 SGD로 별도 처리한다.

## AdamW와의 비교

| 항목 | AdamW | Muon |
|------|-------|------|
| 업데이트 방식 | 좌표별 2차 적응 | 행렬 단위 직교화 |
| 추가 메모리 | 1차·2차 모멘트 × 2 | 1차 모멘텀 × 1 |
| 수렴 속도 | 기준선 | 일부 벤치마크에서 더 빠름 |
| 적합 파라미터 | 전체 | 2D 행렬 (FC, Attention) |
| 분산 학습 지원 | 완전 지원 | DDP/FSDP 가능, 별도 동기화 필요 |

메모리 면에서는 AdamW의 2차 모멘트($v_t$)가 없으므로 파라미터당 메모리가 절약된다. 단 Newton-Schulz 반복에 소량의 추가 연산이 필요하다.

## 분산 학습에서의 고려사항

[[distributed-training-overview]]에서 다루듯, 분산 학습 시 각 GPU가 파라미터의 일부 샤드만 보유할 수 있다. Muon의 직교화는 전체 행렬을 필요로 하므로, FSDP([[data-parallelism-fsdp]] 참고) 환경에서는 직교화 전에 파라미터를 일시적으로 gather해야 한다. 구현 복잡도가 증가하지만, 최신 Muon 구현체들은 이를 자동으로 처리한다.

## 실무 적용 지침

- **적용 대상**: Transformer의 쿼리/키/값 프로젝션, FFN 가중치 등 2D 행렬 파라미터
- **제외 대상**: embedding, LayerNorm, bias — 이들은 AdamW로 유지
- **학습률**: AdamW 대비 약 2-5배 높은 학습률에서 좋은 결과 보고됨
- **하이퍼파라미터**: 모멘텀 계수 $\beta \approx 0.95$, Newton-Schulz 반복 횟수 5
- **스케일**: 소규모(~1B) 모델에서 효과가 검증됨. 대규모 모델에서의 검증은 진행 중

[[optimization-theory]] 문서에서 AdamW, SGD, Lion 등 다른 옵티마이저와의 이론적 관계를 함께 참고하면 Muon의 위치를 더 명확히 이해할 수 있다.

## 한계 및 주의사항

- 공개 코드베이스 기준 AdamW 대비 구현 복잡도가 높음
- 대규모(10B+) 모델에서의 체계적 비교 연구가 아직 부족
- 직교화로 인한 스텝당 추가 연산이 배치 크기가 작을 때 병목이 될 수 있음
- 1D 파라미터를 별도 옵티마이저로 관리해야 하므로 코드 분기 필요

## 관련 문서

- [[optimization-theory]] - AdamW, SGD, Lion 등 옵티마이저 이론 비교
- [[distributed-training-overview]] - 분산 훈련 개요, 동기화 전략
- [[data-parallelism-fsdp]] - FSDP 환경에서의 파라미터 샤딩
- [[training-stability]] - 손실 스파이크 방지 및 수렴 안정성
