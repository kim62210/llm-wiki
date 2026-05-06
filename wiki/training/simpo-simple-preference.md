---
title: SimPO - 단순 선호 최적화
category: training
page_type: concept
tags: [preference-optimization, dpo, reward-model, reference-free, alignment]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# SimPO - 단순 선호 최적화

## 배경과 문제 의식

[[direct-preference-optimization|DPO(Direct Preference Optimization)]]는 보상 모델(reward model) 없이 선호 데이터로 직접 LLM을 정렬하는 효과적인 방법이다. 그러나 DPO는 **참조 모델(reference model)** 을 요구하며, 학습 중 참조 모델의 로그 확률을 매 단계마다 계산해야 한다. 이는 다음 문제를 낳는다:

1. **메모리 비용**: 학습 중 정책 모델과 참조 모델 두 개를 동시에 GPU에 올려야 함.
2. **길이 편향**: DPO 손실은 시퀀스 길이를 명시적으로 정규화하지 않아, 모델이 더 긴 응답을 선호하도록 편향될 수 있음.
3. **참조 모델 의존성**: 참조 모델 품질에 성능이 좌우되며, 반드시 동일 분포의 SFT 체크포인트가 필요함.

SimPO(Simple Preference Optimization)는 이 세 가지 문제를 모두 해결하는 **참조 모델 없는(reference-free)** 선호 최적화 방법이다.

## 핵심 아이디어: 평균 로그 확률 보상

SimPO의 핵심은 응답의 **평균 로그 확률(average log probability)** 을 암묵적 보상으로 사용하는 것이다. 시퀀스 $y = (y_1, \ldots, y_L)$의 보상을 다음과 같이 정의한다:

$$r(x, y) = \frac{1}{|y|} \sum_{i=1}^{|y|} \log \pi_\theta(y_i \mid x, y_{<i})$$

여기서 $|y|$는 응답 길이이고 $\pi_\theta$는 학습 중인 정책 모델이다. **참조 모델이 전혀 등장하지 않는다**.

### DPO와 SimPO 보상 비교

| 방법 | 암묵적 보상 | 참조 모델 필요 |
|------|------------|--------------|
| DPO | $\log \frac{\pi_\theta(y \mid x)}{\pi_{\text{ref}}(y \mid x)}$ | 필수 |
| SimPO | $\frac{1}{\|y\|} \log \pi_\theta(y \mid x)$ | 불필요 |

### 목표 보상 마진 (Target Reward Margin)

SimPO는 단순히 선호 응답의 보상이 기각 응답보다 높으면 충분하다고 보지 않는다. **최소 마진 $\gamma > 0$** 을 요구해, 충분히 구별 가능한 차이를 학습하도록 강제한다:

$$r(x, y_w) - r(x, y_l) \geq \gamma$$

여기서 $y_w$는 선호(winner) 응답, $y_l$은 기각(loser) 응답이다.

## 손실 함수

최종 SimPO 손실은 Bradley-Terry 모델 기반의 분류 손실 형태다:

$$\mathcal{L}_{\text{SimPO}} = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \left( \frac{\log \pi_\theta(y_w \mid x)}{|y_w|} - \frac{\log \pi_\theta(y_l \mid x)}{|y_l|} \right) - \gamma \right) \right]$$

- $\beta$: 선호 차이의 스케일을 조절하는 온도 파라미터
- $\gamma$: 목표 보상 마진 (hyperparameter, 보통 0.5-1.5 범위)
- $\sigma$: 시그모이드 함수

## 학습 파이프라인

```mermaid
flowchart LR
    Data[선호 데이터\n(x, y_w, y_l)] --> Reward_W[y_w 평균 로그 확률\n계산]
    Data --> Reward_L[y_l 평균 로그 확률\n계산]
    Reward_W --> Diff[보상 차이\n계산]
    Reward_L --> Diff
    Gamma[목표 마진 γ] --> Loss[SimPO 손실]
    Diff --> Loss
    Loss --> Update[정책 모델 업데이트]
    Update --> Reward_W
```

참조 모델이 파이프라인에 전혀 등장하지 않아 구조가 단순하다.

## DPO 대비 장점

### 메모리 효율

참조 모델 제거로 GPU 메모리 사용량이 약 50% 감소한다. 대형 모델에서는 이 차이가 결정적이다.

### 길이 정규화 효과

길이 $|y|$로 나누는 정규화 덕분에 모델이 불필요하게 긴 응답을 생성해 보상을 높이려는 인센티브가 사라진다. DPO는 이 문제로 인해 응답 길이가 학습 후 크게 증가하는 경향이 있다.

### 안정성

목표 마진 $\gamma$ 덕분에 선호/기각 응답의 보상이 수렴하지 않고 명확한 간격을 유지하도록 학습된다. DPO에서 자주 발생하는 보상 해킹(reward hacking) 현상이 줄어든다.

## 실험 결과

원논문에서 SimPO는 AlpacaEval 2, Arena-Hard, MT-Bench 벤치마크에서 DPO, IPO, [[kto|KTO]] 등 다양한 참조 기반 방법과 비교되었다:

- Llama-3-8B-Instruct 기반: AlpacaEval 2에서 DPO 대비 길이 제어 효과 명확.
- Mistral-7B 기반: Arena-Hard 점수에서 동급 PEFT 방법 중 최상위.
- 참조 모델 없이도 DPO와 동등하거나 우수한 결과.

## 하이퍼파라미터 가이드

| 파라미터 | 권장 범위 | 역할 |
|---------|-----------|------|
| $\beta$ | 2.0 - 2.5 | 온도 스케일 |
| $\gamma$ | 0.5 - 1.5 | 목표 마진 크기 |
| 학습률 | 5e-7 - 1e-6 | 안정적 수렴 |
| 배치 크기 | 128 이상 | 안정적 그래디언트 추정 |

$\gamma = 0$으로 설정하면 길이 정규화가 추가된 참조 없는 DPO와 동등해진다.

## 실무 적용 관점

SimPO는 특히 다음 상황에서 DPO의 실질적 대안이다:

- **GPU 메모리 제약**: 참조 모델을 올릴 여유가 없을 때.
- **SFT 체크포인트 부재**: 적절한 참조 모델을 구하기 어려울 때.
- **길이 제어 필요**: 간결한 응답을 학습시켜야 할 때.
- **빠른 실험**: 단순한 파이프라인으로 빠르게 정렬을 시도할 때.

## 관련 문서

- [[direct-preference-optimization]] - DPO 핵심 메커니즘과 비교 기준
- [[ipo-identity-preference]] - DPO 과적합을 다른 방식으로 해결
- [[cpo-contrastive-preference]] - SimPO + SFT 결합 방법
- [[kto]] - 쌍(pair)이 없는 선호 최적화
- [[orpo]] - 참조 모델 없는 또 다른 선호 최적화
- [[dpo-paper]] - DPO 원논문 요약
- [[rlhf-and-alignment]] - RLHF와 정렬 전반 개요
- [[preference-data-collection]] - 선호 데이터 수집 방법
