---
title: Multi-Token Prediction (MTP)
category: training
page_type: concept
tags: [multi-token-prediction, mtp, next-token-prediction, deepseek-v3, speculative-decoding, training-objective]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# Multi-Token Prediction (MTP)

## 개요

Multi-Token Prediction(MTP, 다중 토큰 예측)은 표준 다음 토큰 예측(next-token prediction)을 확장하여, 각 위치에서 다음 $k$개 토큰을 동시에 예측하도록 언어 모델을 훈련하는 기법이다. Meta AI가 2024년에 이론적·실험적 근거를 제시했고, DeepSeek-V3에서 사전학습 보조 목표로 실용화되며 주목받고 있다.

## 동기: 단일 토큰 예측의 한계

[[causal-language-modeling]]의 표준 목표인 단일 토큰 예측은 각 스텝에서 바로 다음 토큰 하나만 예측한다. 이 방식은 개념적으로 단순하지만, 모델이 장기 의존성이나 계획적 생성(planning ahead)을 직접 학습하기 어렵다는 비판이 있다. 예를 들어 코드 생성에서 변수 이름을 선택할 때 이후 수십 토큰의 맥락을 고려해야 하지만, 단일 토큰 목표는 그 피드백 신호를 즉각 제공하지 않는다.

## 아키텍처

MTP는 메인 모델 위에 $k$개의 독립 예측 헤드를 추가한다. 각 헤드는 서로 다른 미래 오프셋 $+1, +2, \ldots, +k$를 담당한다.

```mermaid
flowchart TD
    Input["입력 시퀀스 x_1 ... x_t"] --> Backbone[공유 Transformer 백본]
    Backbone --> H1[헤드 1\n다음 토큰 x_{t+1} 예측]
    Backbone --> H2[헤드 2\n두 번째 토큰 x_{t+2} 예측]
    Backbone --> Hk[헤드 k\nk번째 토큰 x_{t+k} 예측]
    H1 --> L1[손실 L_1]
    H2 --> L2[손실 L_2]
    Hk --> Lk[손실 L_k]
    L1 --> Total[총 손실\nL = L_1 + α·L_2 + ... + α·L_k]
    L2 --> Total
    Lk --> Total
```

각 예측 헤드는 일반적으로 가벼운 MLP 또는 공유 임베딩 행렬로 구현된다. 추가 파라미터 수는 전체 모델에 비해 소량이다.

## DeepSeek-V3의 구현

DeepSeek-V3는 MTP를 보조 훈련 목표로 활용한다. 구체적으로:

- $k = 1$ (기본 헤드 + 1개 추가 헤드, 즉 $k=2$에 해당)
- 추가 헤드 손실에 가중치 $\lambda$ 적용 (실험적으로 $\lambda = 0.3$ 전후)
- 추론(inference) 시에는 추가 헤드를 [[speculative-decoding]] 드래프트 생성에 활용

DeepSeek-V3 보고서에서 MTP를 제거한 Ablation 실험 결과, 코딩 및 수학 벤치마크에서 유의미한 성능 저하가 관찰되었다.

## 훈련 손실 공식

위치 $t$에서 $k$-step MTP 손실:

$$\mathcal{L}_{MTP} = -\sum_{t=1}^{T} \sum_{j=1}^{k} \alpha_j \log P_j(x_{t+j} \mid x_{\le t})$$

- $P_j$: $j$번째 오프셋 헤드의 확률 분포
- $\alpha_j$: 오프셋별 가중치 ($\alpha_1 = 1$, $\alpha_{j>1}$은 하이퍼파라미터)
- 원거리 오프셋일수록 예측이 어려우므로 $\alpha_j$를 줄이는 것이 일반적

## [[speculative-decoding]]과의 시너지

MTP의 실용적 부산물은 추론 시 투기적 디코딩(speculative decoding)에 직접 활용할 수 있다는 점이다. $k$개의 추가 헤드가 병렬로 드래프트 토큰을 제안하고, 메인 모델이 이를 검증하는 방식으로 디코딩 속도를 향상시킬 수 있다.

표준 speculative decoding이 별도의 드래프트 모델을 필요로 하는 것과 달리, MTP 헤드는 이미 메인 모델에 내장되어 있어 추가 배포 복잡성이 없다.

## 코드 생성·수학 추론에서의 효과

MTP의 효과는 특히 **긴 추론 체인**이 필요한 태스크에서 두드러진다:

- 코드: 함수 내 변수명, 타입, 인자 순서를 일관되게 예측해야 하는 패턴
- 수학: 연산 시퀀스의 일관성 (예: 등호 앞뒤 식의 동일성)
- 구조적 텍스트: JSON, XML 등 닫는 괄호/태그 예측

이들 태스크에서 MTP는 모델이 "미래 제약"을 현재 토큰 선택에 반영하도록 강제하는 학습 압력을 만들어낸다.

## 메모리 및 연산 오버헤드

| 항목 | 단일 토큰 예측 | MTP (k=4) |
|------|--------------|-----------|
| 추가 파라미터 | 0 | 헤드 × k, 약 1-3% 증가 |
| 훈련 FLOPs | 기준 | 약 10-20% 증가 (데이터 의존) |
| 메모리 | 기준 | 약간 증가 |
| 추론 지연 | 기준 | 동일 (헤드 비활성화 가능) |

추론 시 추가 헤드를 완전히 비활성화하면 지연 증가 없이 훈련 이점만 유지할 수 있다.

## 관련 문서

- [[causal-language-modeling]] - 표준 다음 토큰 예측 훈련 목표
- [[speculative-decoding]] - MTP 헤드를 드래프트로 활용하는 추론 가속
- [[deepseek-v3-training]] - DeepSeek-V3 사전학습 세부 구현
- [[training-stability]] - 보조 손실 추가 시 훈련 안정성 고려사항
