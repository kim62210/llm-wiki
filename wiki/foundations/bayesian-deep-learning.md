---
title: 베이지안 딥러닝 (Bayesian Deep Learning)
category: foundations
page_type: concept
tags: [bayesian-deep-learning, bnn, mc-dropout, deep-ensembles, swag, laplace-approximation, uncertainty-quantification]
sources: [raw/2026-05-06-wiki-expand-scan.md]
created: 2026-05-06
updated: 2026-05-06
---

# 베이지안 딥러닝 (Bayesian Deep Learning)

베이지안 딥러닝(Bayesian Deep Learning, BDL)은 신경망 가중치(weight)를 결정론적 점 추정이 아니라 **확률 분포로 다루는** 접근의 총칭이다. 표준 딥러닝이 데이터를 가장 잘 설명하는 한 점 $\hat{w}$만 학습한다면, 베이지안 딥러닝은 가중치 사후 분포 $p(w \mid \mathcal{D})$ 자체 또는 그 근사를 학습해 **불확실성(uncertainty)** 을 정량화한다.

이 페이지는 BDL의 전체 스펙트럼(BNN, MC Dropout, Deep Ensembles, SWAG, Laplace 근사 등)과 실무 응용을 정리한다. 변분 BNN의 수식 디테일은 [[bayesian-neural-networks]] 페이지가 상세히 다루며, 본 페이지는 **방법론 카탈로그**의 성격을 갖는다.

## 왜 베이지안 딥러닝인가

표준 딥러닝의 한계:

- 점 추정만 출력 — "이 답이 얼마나 확신할 만한가?"에 답할 수 없음
- 분포 외(out-of-distribution, OOD) 입력에서도 자신만만하게 틀린 답 ("overconfident")
- 의료·금융·자율주행 등 고위험 도메인에서 의사결정 근거 부족

베이지안 관점은 가중치 분포 $p(w \mid \mathcal{D})$를 통해 **인식론적 불확실성(epistemic uncertainty)** 을 모델링한다. 데이터로 결정되지 않는 가중치 영역을 분포의 분산으로 표현한다.

```mermaid
flowchart TD
    Start[표준 DL\n점 추정 w_hat] --> Issue[과신/OOD 취약]
    Issue --> BDL[베이지안 딥러닝\np w | D]
    BDL --> M1[BNN\n변분 추론]
    BDL --> M2[MC Dropout\nGal 2016]
    BDL --> M3[Deep Ensembles\nLakshminarayanan 2017]
    BDL --> M4[SWAG\nMaddox 2019]
    BDL --> M5[Laplace 근사\n사후 가우시안]
    M1 --> App[OOD 검출\n능동 학습\n캘리브레이션\n의료 AI]
    M2 --> App
    M3 --> App
    M4 --> App
    M5 --> App
```

## 1. 변분 BNN (Variational BNN)

가중치 사후 $p(w \mid \mathcal{D})$를 다루기 쉬운 분포 $q_\phi(w)$로 근사하고 ELBO를 최대화한다.

$$
\mathcal{L}(\phi) = \mathbb{E}_{q_\phi(w)}[\log p(\mathcal{D} \mid w)] - \mathrm{KL}(q_\phi(w) \,\|\, p(w))
$$

대표 구현은 **Bayes by Backprop** (Blundell et al. 2015)으로, 각 가중치를 $\mathcal{N}(\mu, \sigma^2)$로 파라미터화하고 reparameterization trick으로 역전파한다. 자세한 수식과 구현은 [[bayesian-neural-networks]] 참고.

장점: 원리적으로 정확. 단점: 대형 모델에서 수렴 어려움, 추가 메모리 2배.

## 2. MC Dropout

Gal & Ghahramani (2016) "Dropout as a Bayesian Approximation"이 정립. 표준 dropout 학습된 네트워크를 **그대로** 베이지안 근사로 해석할 수 있음을 증명.

### 핵심 아이디어

- 학습 시: 표준 dropout
- 추론 시: dropout을 **켠 채로** $T$번 forward → 예측 평균과 분산을 불확실성으로 사용

$$
\hat{y} = \frac{1}{T}\sum_{t=1}^{T} f_{w_t}(x), \quad w_t \sim q_\text{dropout}
$$

> "dropout training in deep neural networks (NNs) [is] approximate Bayesian inference in deep Gaussian processes."
> — Gal & Ghahramani 2016

장점:
- 기존 모델 재학습 불필요
- 추가 파라미터 0
- 구현이 거의 trivial

한계: 드롭률에 민감, 인식론적 불확실성을 과소추정하는 경향이 있다는 후속 비판. [[gaussian-process]]와의 이론적 연결성은 흥미로운 지점.

## 3. Deep Ensembles

Lakshminarayanan et al. (2017). $M$개 신경망을 **서로 다른 random seed**로 독립 학습하고 예측을 평균.

```python
# 의사 코드
models = [train_model(seed=i) for i in range(M)]
preds = [m(x) for m in models]
mean = preds.mean()
var = preds.var()  # 불확실성
```

베이지안 정당화는 약하지만, **실증적으로 가장 강력한 baseline** 중 하나. SWAG, MC Dropout보다 정확도와 캘리브레이션이 좋은 경우가 많다 ([[deep-ensembles]] 페이지 참고).

비용: $M$배 학습 + $M$배 추론. M=5가 흔히 쓰인다.

## 4. SWAG (Stochastic Weight Averaging-Gaussian)

Maddox et al. (2019) "A Simple Baseline for Bayesian Uncertainty in Deep Learning" (NeurIPS 2019). SGD 학습 궤적의 통계로 가우시안 사후를 추정.

### 알고리즘

1. 일반 학습으로 수렴 근처에 도달
2. 학습률을 다소 높여 SGD를 계속 굴리며 가중치 스냅샷을 수집
3. 스냅샷의 평균 $\bar{w}$ (SWA solution)를 1차 모멘트로
4. 2차 모멘트는 **대각 + 저계수(low-rank)** 공분산으로 근사
5. 추론 시 가우시안에서 $w$를 샘플링해 앙상블

> "the SGD iterates ... act like samples from a Gaussian distribution; SWAG fits this Gaussian distribution by capturing the SWA mean and a covariance matrix."
> — Maddox et al. 2019

장점: 표준 SGD 파이프라인에 최소 수정. 매우 큰 모델까지 스케일. 자세한 구현은 [[swag-stochastic-weight-averaging]] 참고.

## 5. Laplace 근사 (Laplace Approximation)

학습된 MAP 추정 $\hat{w}$ 주변에서 사후의 2차 테일러 전개:

$$
p(w \mid \mathcal{D}) \approx \mathcal{N}(\hat{w}, H^{-1}), \quad H = -\nabla^2 \log p(\hat{w} \mid \mathcal{D})
$$

문제: 헤시안이 $O(p^2)$로 대형 모델에 불가능. 해결책:
- **Diagonal Laplace**: 헤시안 대각만
- **KFAC**: Kronecker-factored 근사
- **Last-layer Laplace**: 마지막 레이어만 베이지안

라이브러리: `laplace-torch` (Daxberger et al. 2021).

## 두 종류의 불확실성

| 종류 | 정의 | 줄이는 방법 |
|------|------|--------------|
| **Epistemic** (인식론적) | 모델 자체의 불확실성 | 더 많은 데이터 |
| **Aleatoric** (우발적) | 데이터 노이즈 | 줄일 수 없음 (센서 향상 등) |

OOD 입력에서는 epistemic이 크게 증가, in-distribution 노이즈는 aleatoric이 지배. 두 가지 분리는 의사결정에서 중요하다.

## 응용 분야

### OOD 검출
훈련 분포 바깥 입력을 분산이 큰 예측으로 식별. [교차검증 필요: epistemic 분산 단독으로는 종종 불충분, 앙상블/SWAG가 더 신뢰성 높음]

### 능동 학습 (Active Learning)
가장 불확실한 샘플을 다음 라벨링 후보로 선택 (BALD: Bayesian Active Learning by Disagreement). [[bald-batchbald-active-learning]] 참고.

### 의료 AI / 자율주행
"모르겠다" 출력 가능 — high-stakes 도메인에서 자동화 vs 인간 위임 결정에 활용.

### 강화학습 탐험
가치함수의 불확실성으로 탐험 보상 (e.g., Bayesian DQN). 

### 캘리브레이션
신뢰도 출력이 실제 정확도와 일치하도록. ECE (Expected Calibration Error)로 평가.

## 방법론 비교

| 방법 | 추가 학습비용 | 추론비용 | 메모리 | 구현 난이도 | 정확도/캘리브레이션 |
|------|---------------|----------|--------|--------------|---------------------|
| 변분 BNN | 1.5-2x | T forward | 2x | 중 | 중 |
| MC Dropout | 0 | T forward | 1x | 매우 낮음 | 중-약 |
| Deep Ensembles | M배 | M배 | M배 | 낮음 | 매우 높음 |
| SWAG | 약간 | T forward | 1.x | 중 | 높음 |
| Last-layer Laplace | 작음 | 1x + posterior | 작음 | 중 | 중-높음 |

## 한계

- **스케일링 어려움**: 대형 LLM에 변분 BNN/Laplace 적용은 여전히 활발한 연구 영역
- **이론적 정당성과 경험적 성능 불일치**: Deep ensembles는 베이지안 정당화가 약하지만 실증적으로 우수
- **Hyperparameter 민감도**: prior 선택, 드롭률, 앙상블 크기 모두 결과에 민감
- **출력 캘리브레이션**: 베이지안 추론이 자동으로 잘 캘리브레이션된 출력을 보장하지 않음 — temperature scaling 등 후처리 필요

## 관련 문서

- [[bayesian-neural-networks]] - 변분 BNN 수식과 Bayes by Backprop 구현 상세
- [[deep-ensembles]] - 앙상블 기반 베이지안 근사
- [[swag-stochastic-weight-averaging]] - SWAG 구체 구현
- [[gaussian-process]] - MC Dropout과의 이론적 연결
- [[variational-inference-deep]] - 변분 추론 기초
- [[ensemble-methods]] - 일반 앙상블 기법
- [[bald-batchbald-active-learning]] - 능동 학습에서 BNN 활용
- [[bayesian-inference]] - 베이지안 추론의 수학적 토대
- [[uncertainty-estimation]] - 불확실성 추정 일반
