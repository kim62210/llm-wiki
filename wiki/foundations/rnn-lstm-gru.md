---
title: 순환 신경망 (RNN, LSTM, GRU)
category: foundations
page_type: concept
tags: [RNN, LSTM, GRU, sequence-modeling, time-series, vanishing-gradient, gating-mechanism]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

순환 신경망(Recurrent Neural Network, RNN)은 시퀀스 데이터를 처리하기 위해 순환 연결(recurrent connection)을 도입한 신경망 아키텍처다. 이전 시점의 은닉 상태(hidden state)를 현재 시점의 입력과 함께 처리하여 시간적 의존성을 모델링한다. 그러나 기울기 소실/폭발 문제로 장기 의존성(long-term dependency) 학습이 어려워, 이를 해결하기 위해 LSTM(1997)과 GRU(2014)가 제안되었다. Transformer가 등장한 이후 NLP에서의 주도적 지위를 잃었지만, RNN의 순차 처리 원리는 [[mamba-3]] 같은 상태 공간 모델(SSM)에서 재해석되고 있다.

## 기본 RNN

### 동작 원리

각 시점 t에서 은닉 상태 h_t는 현재 입력 x_t와 이전 은닉 상태 h_{t-1}의 함수다:

```
h_t = tanh(W_hh * h_{t-1} + W_xh * x_t + b_h)
y_t = W_hy * h_t + b_y
```

이 구조는 이론적으로 임의 길이의 시퀀스를 처리할 수 있지만, 실제로는 역전파 과정에서 기울기가 시간축을 따라 반복적으로 곱해지면서 소실(vanishing)하거나 폭발(exploding)한다.

### 기울기 소실 문제

시점 T에서 시점 1까지의 기울기는 W_hh의 반복 곱으로 구성된다. W_hh의 최대 특이값이 1보다 작으면 기울기가 지수적으로 감소하고, 1보다 크면 지수적으로 증가한다. 이로 인해 기본 RNN은 10-20 시점 이상의 의존성을 학습하기 어렵다.

## LSTM (Long Short-Term Memory)

Hochreiter & Schmidhuber(1997)가 제안한 LSTM은 셀 상태(cell state)와 세 개의 게이트를 도입하여 기울기 소실 문제를 해결했다.

### 게이트 구조

| 게이트 | 역할 | 수식 |
|--------|------|------|
| 망각 게이트 (forget) | 이전 셀 상태에서 버릴 정보 결정 | f_t = sigmoid(W_f * [h_{t-1}, x_t] + b_f) |
| 입력 게이트 (input) | 새로 저장할 정보 결정 | i_t = sigmoid(W_i * [h_{t-1}, x_t] + b_i) |
| 출력 게이트 (output) | 셀 상태에서 출력할 정보 결정 | o_t = sigmoid(W_o * [h_{t-1}, x_t] + b_o) |

셀 상태 업데이트:

```
C_t = f_t * C_{t-1} + i_t * tanh(W_c * [h_{t-1}, x_t] + b_c)
h_t = o_t * tanh(C_t)
```

핵심 통찰은 셀 상태 C_t가 덧셈 연결(additive connection)으로 전파되어 기울기가 보존된다는 점이다. 이는 ResNet의 잔차 연결과 동일한 원리다.

## GRU (Gated Recurrent Unit)

Cho et al.(2014)이 제안한 GRU는 LSTM의 게이트 구조를 간소화한 변형이다. 셀 상태와 은닉 상태를 통합하고, 게이트를 두 개(리셋, 업데이트)로 축소했다:

```
z_t = sigmoid(W_z * [h_{t-1}, x_t])     -- 업데이트 게이트
r_t = sigmoid(W_r * [h_{t-1}, x_t])     -- 리셋 게이트
h_t = (1 - z_t) * h_{t-1} + z_t * tanh(W * [r_t * h_{t-1}, x_t])
```

업데이트 게이트 z_t가 LSTM의 망각 게이트와 입력 게이트 역할을 동시에 수행한다. 파라미터가 적어 학습이 빠르며, 소규모 데이터셋에서 LSTM과 유사하거나 더 나은 성능을 보인다.

## LSTM vs GRU 비교

| 항목 | LSTM | GRU |
|------|------|-----|
| 게이트 수 | 3 (forget, input, output) | 2 (reset, update) |
| 상태 벡터 | 셀 상태 + 은닉 상태 (분리) | 은닉 상태만 |
| 파라미터 수 | 더 많음 | 약 25% 적음 |
| 장기 의존성 | 강함 | 비슷하거나 약간 약함 |
| 학습 속도 | 느림 | 빠름 |

대규모 데이터와 긴 시퀀스에서는 LSTM이, 작은 데이터와 빠른 프로토타이핑에서는 GRU가 유리하다. 실질적 성능 차이보다 데이터셋 특성과 하이퍼파라미터 튜닝의 영향이 더 크다.

## RNN에서 Transformer로

RNN 계열의 근본적 한계는 순차적 처리(sequential processing)다. 시점 t의 계산이 시점 t-1에 의존하므로 병렬화가 불가능하다. "Attention Is All You Need"(Vaswani et al., 2017)에서 제안된 [[transformer-architecture]]는 [[self-attention-mechanism]]으로 모든 위치 간 관계를 병렬 계산하여 이 한계를 돌파했다. 그러나 RNN의 O(1) 상태 크기(고정 메모리)라는 장점은 [[mamba-3]]와 같은 SSM에서 재발견되어, 장문맥 추론 효율성의 핵심 원리로 활용되고 있다.

## 현재 위치

RNN/LSTM/GRU는 NLP의 주류에서 물러났지만, 시계열 예측, 음성 인식, 온디바이스 추론(고정 메모리) 등 특정 도메인에서 여전히 활용된다. 또한 LSTM의 게이트 메커니즘은 [[gated-attention]], [[gated-deltanet]] 등 현대 아키텍처의 핵심 설계 원리로 계승되고 있다.

## 대표 자료

- [Hochreiter & Schmidhuber, "Long Short-Term Memory" (1997)](https://www.bioinf.jku.at/publications/older/2604.pdf)
- [Cho et al., "Learning Phrase Representations using RNN Encoder-Decoder" (arXiv:1406.1078)](https://arxiv.org/abs/1406.1078)
- [Olah, "Understanding LSTM Networks" (colah's blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## 관련 문서

- [[transformer-architecture]] -- RNN의 순차 처리 한계를 극복한 아키텍처
- [[self-attention-mechanism]] -- RNN의 은닉 상태 대신 전역 참조를 구현
- [[mamba-3]] -- RNN의 순차 상태 업데이트를 SSM으로 재해석
- [[gated-attention]] -- LSTM 게이트 메커니즘의 현대적 적용
- [[gated-deltanet]] -- 게이트 기반 선형 어텐션 변형
- [[cnn]] -- 시퀀스 처리의 대안적 접근 (1D CNN)
