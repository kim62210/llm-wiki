---
title: Informer 희소 어텐션
category: architectures
page_type: concept
tags: [시계열, Informer, ProbSparse, 희소어텐션, 장기예측, Transformer]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# Informer 희소 어텐션

## 개요

Informer는 2021년 AAAI Best Paper로 선정된 시계열 예측 모델로, 표준 Transformer가 장기 시계열 예측(Long Sequence Time-Series Forecasting, LSTF)에서 겪는 **이차 복잡도 문제**를 해결하기 위해 ProbSparse 셀프 어텐션을 제안했다.

[[time-series-forecasting-dl|딥러닝 기반 시계열 예측]] 분야에서 Transformer를 장기 예측에 실용적으로 적용한 선구적 연구다. [[sparse-attention-patterns|희소 어텐션 패턴]] 기법을 시계열 도메인에 최초로 성공적으로 적용한 사례 중 하나다.

## 문제 배경

표준 Transformer의 셀프 어텐션(Self-Attention)은 시퀀스 길이 $L$에 대해 $O(L^2)$의 시간·메모리 복잡도를 가진다. 수백~수천 스텝의 장기 예측에서 이는 심각한 병목이 된다.

```mermaid
flowchart LR
    Standard[표준 Attention\nO(L^2) 복잡도] -->|문제| Long[장기 시계열에서\n메모리/시간 폭발]
    Long --> Informer[Informer\nProbSparse Attention\nO(L log L)]
    Informer --> LSTF[장기 예측 가능\n수백~수천 스텝]
```

## ProbSparse 셀프 어텐션

### 핵심 관찰

Transformer 어텐션 행렬을 분석하면, 대부분의 쿼리(query)는 극소수의 키(key)에만 집중한다 — 즉, 어텐션 분포가 희소(sparse)하다. 나머지 쿼리-키 쌍은 어텐션 가중치가 균등 분포(uniform distribution)에 가까워 사실상 무의미하다.

### 알고리즘

1. **쿼리 중요도 측정**: 각 쿼리의 어텐션 분포가 균등 분포와 얼마나 다른지를 KL 발산으로 측정
2. **상위 $u = O(\ln L)$개 쿼리 선택**: KL 발산이 큰 쿼리, 즉 실제로 의미 있는 어텐션을 수행하는 쿼리만 선택
3. **나머지 쿼리 처리**: 선택되지 않은 쿼리는 값(value) 행렬의 평균으로 대체

결과적으로 전체 복잡도가 $O(L \log L)$로 감소한다.

```mermaid
flowchart TD
    Q[쿼리 행렬 Q] --> Sample[랜덤 샘플링으로\nKL 발산 근사]
    Sample --> TopU[상위 u개 쿼리 선택\nu = c * ln(L_Q)]
    K[키 행렬 K] --> TopU
    TopU --> SparseAttn[선택된 쿼리만\n풀 어텐션 계산]
    Rest[나머지 쿼리] --> AvgV[Value 평균으로\n대체]
    SparseAttn --> Output[희소 어텐션 출력]
    AvgV --> Output
```

## Distilling 연산 (Self-attention Distilling)

Informer는 ProbSparse 외에도 인코더에서 레이어를 거칠수록 시퀀스를 절반씩 축소하는 **증류(distilling)** 연산을 도입한다. 맥스 풀링과 유사하게 작동하여 주요 시간 패턴만 남기고 시퀀스 길이를 점진적으로 줄인다.

## 생성형 디코더

표준 Transformer가 스텝 하나씩 자기회귀적으로 예측하는 것과 달리, Informer는 **생성형 디코더(Generative Style Decoder)**를 사용해 전체 예측 시퀀스를 한 번에 출력한다. 이를 통해 누적 오류(error accumulation)를 줄이고 추론 속도를 높인다.

## 성능 및 영향

Informer는 ETTh1, ETTh2, ETTm1, Weather, Exchange Rate 등의 벤치마크에서 당시 SOTA(state-of-the-art) 결과를 달성했다. 이후 이 벤치마크들은 장기 시계열 예측 연구의 표준 평가 데이터셋이 되었다.

단, 이후 연구(PatchTST, DLinear 등)에서 일부 데이터셋에 대해 단순 선형 모델이 Informer를 능가하는 결과가 나와, 복잡한 어텐션 구조의 필요성에 대한 논쟁이 이어졌다.

## 후속 모델과의 관계

| 모델 | Informer 대비 개선점 |
|------|---------------------|
| Autoformer | 자기상관(autocorrelation) 기반 어텐션 대체 |
| FEDformer | 주파수 도메인 어텐션 |
| [[patchtst]] | 채널 독립 + 패치 기반으로 단순화 |
| iTransformer | 채널-토큰 반전(inverted) 어텐션 |

## 관련 문서

- [[time-series-forecasting-dl]] - 딥러닝 기반 시계열 예측 전반
- [[sparse-attention-patterns]] - 희소 어텐션 패턴 일반 개념
- [[patchtst]] - Informer 계열의 한계를 극복한 패치 기반 접근
- [[moirai-unified-forecasting]] - 파운데이션 모델 수준으로의 발전
