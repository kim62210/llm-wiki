---
title: 베이지안 신경망
category: foundations
page_type: concept
tags: [베이지안, 불확실성, 변분추론, MCDropout, 가중치사후분포, 불확실성정량화]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 베이지안 신경망

## 개요

베이지안 신경망(Bayesian Neural Networks, BNN)은 모델 파라미터(가중치)를 결정론적 값이 아닌 **확률 분포**로 취급하는 신경망이다. 표준 딥러닝이 점 추정(point estimate) $\hat{w} = \arg\max_w p(w|D)$를 구하는 반면, BNN은 가중치의 사후 분포(posterior distribution) $p(w|D)$ 전체를 학습한다.

핵심 이점은 **인식론적 불확실성(epistemic uncertainty)** 정량화다. 모델이 "이 입력에 대한 예측은 확신하기 어렵다"는 것을 수치로 표현할 수 있어, 의료·자율주행·과학 실험 등 고위험 응용에서 중요하다.

## 베이지안 추론 기초

### 사전 분포 (Prior)

$p(w)$: 데이터를 보기 전 가중치에 대한 믿음. 보통 등방성 가우시안:

$$p(w) = \mathcal{N}(0, \sigma_0^2 I)$$

이는 $L_2$ 정규화(가중치 감쇠)와 동치다.

### 우도 (Likelihood)

$p(D|w) = \prod_{i} p(y_i | x_i, w)$: 주어진 가중치 $w$에서 데이터를 관찰할 확률.

### 사후 분포 (Posterior)

베이즈 정리로 가중치의 사후 분포를 구한다:

$$p(w|D) = \frac{p(D|w) p(w)}{p(D)}$$

**문제**: 분모 $p(D) = \int p(D|w) p(w) dw$가 신경망에서 적분 계산 불가(intractable).

### 예측 분포 (Predictive Distribution)

새로운 입력 $x^*$에 대한 예측은 가중치에 대한 주변화(marginalization):

$$p(y^*|x^*, D) = \int p(y^*|x^*, w) p(w|D) dw$$

이 적분이 불확실성의 원천. 가중치가 다양한 해에 분산될수록 예측의 불확실성이 커진다.

## 변분 추론 BNN (Variational BNN)

### ELBO (Evidence Lower BOund)

다루기 쉬운 분포 $q_\phi(w)$로 진짜 사후 분포를 근사:

$$\log p(D) \geq \mathbb{E}_{q_\phi(w)}[\log p(D|w)] - D_\text{KL}(q_\phi(w) \| p(w))$$

우변이 ELBO. 최대화 = $\log p(D)$ 최대화 근사.

KL 항을 최소화하면 $q_\phi$가 사전 분포에 가까워지고(정규화 효과), 재구성 항을 최대화하면 데이터를 잘 설명한다.

### Bayes by Backprop (Blundell et al., 2015)

가중치를 가우시안 분포 $q_\phi(w) = \mathcal{N}(\mu, \sigma^2)$로 파라미터화:

- 각 가중치마다 $\mu$와 $\rho$ (소프트플러스를 통해 $\sigma = \log(1 + e^\rho) > 0$) 두 파라미터 학습
- 재매개변수화 트릭(reparameterization trick): $w = \mu + \sigma \odot \epsilon$, $\epsilon \sim \mathcal{N}(0, I)$
- 표준 역전파로 $\nabla_{\mu, \rho} \text{ELBO}$ 계산 가능

```mermaid
flowchart TD
    A[입력 x] --> B[샘플링\nw ~ q_phi w = mu + sigma · eps]
    B --> C[순전파\nf_w x]
    C --> D[재구성 손실\n-log p y | x,w]
    D --> E[ELBO 최적화\n재구성 - KL]
    E --> F[mu, rho 파라미터 업데이트\n역전파]
    F --> B
    G[KL 정규화\nKL q_phi || p w] --> E
    style B fill:#fff3cd
    style E fill:#d4edda
```

변분 BNN의 학습 루프: 가중치를 샘플링해 순전파하고 ELBO를 최대화한다.

## MC Dropout (Monte Carlo Dropout)

Gal & Ghahramani (2016)이 제안. 기존 딥러닝 모델의 **드롭아웃이 베이지안 근사**임을 증명.

### 핵심 아이디어

추론(inference) 시에도 드롭아웃을 켜고, $T$번 다른 드롭 패턴으로 순전파:

$$p(y^*|x^*, D) \approx \frac{1}{T}\sum_{t=1}^T p(y^*|x^*, w_t), \quad w_t \sim q_\text{dropout}$$

### 불확실성 분해

$T$번 예측의 평균과 분산으로 불확실성 추정:

$$\hat{y} = \frac{1}{T}\sum_t \hat{y}_t \quad \text{(예측 평균)}$$

$$\text{Var}(y^*) \approx \underbrace{\frac{1}{T}\sum_t \hat{y}_t^2 - \hat{y}^2}_{\text{인식론적 불확실성}} + \underbrace{\text{평균 예측 분산}}_{\text{우발적 불확실성}}$$

### 장점과 한계

| 측면 | 내용 |
|------|------|
| 구현 난이도 | 낮음 (기존 모델에 바로 적용) |
| 추가 파라미터 | 없음 |
| 계산 비용 | $T$배 증가 |
| 근사 품질 | 드롭 확률에 민감, 과소추정 경향 |

## 라플라스 근사 (Laplace Approximation)

학습된 MAP(최대 사후 확률) 추정치 $\hat{w}$를 중심으로 2차 테일러 전개:

$$\log p(w|D) \approx \log p(\hat{w}|D) - \frac{1}{2}(w - \hat{w})^\top H (w - \hat{w})$$

$H = -\nabla^2 \log p(\hat{w}|D)$: 음로그 사후의 헤시안.

사후 분포를 $q(w) = \mathcal{N}(\hat{w}, H^{-1})$으로 근사한다.

**문제**: 대형 신경망에서 헤시안 계산과 저장이 $O(p^2)$. KFAC나 대각 근사로 완화.

## SWAG (Stochastic Weight Averaging-Gaussian)

Maddox et al. (2019). SGD 학습 궤적에서 가우시안 사후를 추정:

1. 학습 후 반기에 학습률을 높이며 가중치 스냅샷 수집
2. 스냅샷의 평균 $\bar{w}$와 공분산 추정 (대각 + 저계수 수정)
3. 추론 시 추정된 가우시안에서 샘플링 후 앙상블

표준 학습 파이프라인에 최소한의 수정만으로 강력한 불확실성 추정 달성.

## 불확실성의 두 종류

### 인식론적 불확실성 (Epistemic Uncertainty)

모델이 충분한 데이터를 보지 못해서 생기는 불확실성. 데이터를 더 추가하면 감소 가능.

- 훈련 분포 바깥(out-of-distribution, OOD) 샘플에서 높음
- 모델 파라미터의 불확실성 = 가중치 사후 분포의 분산

### 우발적 불확실성 (Aleatoric Uncertainty)

데이터 자체에 내재된 노이즈. 데이터를 더 추가해도 감소하지 않음.

- 레이블 노이즈, 센서 오차, 고유 무작위성
- 출력 분포의 분산으로 모델링 ($p(y|x, w)$의 분산 파라미터 추가 학습)

## 활성 학습 (Active Learning)과의 결합

BNN의 불확실성은 능동 학습에서 어떤 데이터를 다음에 수집할지 결정하는 획득 함수(acquisition function)로 사용된다:

- **최대 불확실성**: 예측 엔트로피가 가장 높은 샘플 선택
- **BALD** (Bayesian Active Learning by Disagreement): 상호 정보 최대화
- **BatchBALD**: 배치 선택 시 다양성 고려

## 딥러닝 일반화와 BNN

BNN 관점에서 딥러닝의 일반화를 재해석할 수 있다:

- **평탄한 최솟값(flat minima)**: 헤시안 고유값이 작은 지역 = 넓은 사후 분포 = 좋은 일반화
- **SGD의 암묵적 베이즈**: SGD가 암묵적으로 평탄 최솟값을 선호하므로 라플라스 근사 BNN과 유사
- **앙상블 = 베이즈 모델 평균**: 딥 앙상블이 BNN의 실용적 근사라는 연구 결과

## 실용 선택 가이드

| 방법 | 적합한 상황 | 계산 비용 |
|------|------------|----------|
| MC Dropout | 빠른 프로토타입, 기존 모델 활용 | 낮음 |
| Bayes by Backprop | 완전한 BNN, 소규모 모델 | 2배 파라미터 |
| SWAG | 대형 모델, 높은 성능 필요 | 중간 |
| 라플라스 근사 | 학습 완료 후 불확실성 추가 | 사후 처리 |
| 딥 앙상블 | 최고 성능, 계산 비용 허용 | $T$배 |

## 관련 문서

- [[bayesian-inference]] - 베이지안 추론 기초
- [[kl-divergence]] - ELBO의 KL 항
- [[gaussian-process]] - GP와 BNN의 관계 (NTK 이론 연결)
- [[pac-bayes-bounds]] - PAC-Bayes: BNN의 일반화 이론
- [[fisher-information-matrix]] - 라플라스 근사의 헤시안 계산
- [[optimization-theory]] - 평탄 최솟값과 일반화
- [[normalizing-flows]] - 더 정확한 사후 근사를 위한 흐름 모델
