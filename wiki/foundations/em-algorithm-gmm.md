---
title: EM 알고리즘과 가우시안 혼합 모델 (EM Algorithm & GMM)
category: foundations
page_type: concept
tags: [em-algorithm, gmm, clustering, expectation-maximization]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# EM 알고리즘과 가우시안 혼합 모델 (EM Algorithm & GMM)

EM(Expectation-Maximization) 알고리즘은 잠재 변수(latent variable)가 있는 확률 모델에서 최대 우도 추정(MLE)을 수행하는 반복 최적화 기법이다. 가우시안 혼합 모델(Gaussian Mixture Model, GMM)이 가장 대표적인 적용 사례다.

## EM 알고리즘 원리

관측 데이터 $X$와 잠재 변수 $Z$가 있을 때, 완전 데이터 로그 우도(complete-data log-likelihood)의 기대값을 최대화하는 방식으로 파라미터 $\theta$를 추정한다.

$$\log P(X \mid \theta) \geq \mathbb{E}_{Z \mid X, \theta^{(t)}}[\log P(X, Z \mid \theta)] - \text{const} = \text{ELBO}$$

```mermaid
flowchart TD
    INIT[파라미터 초기화 θ⁰] --> E
    E["E-step\n잠재변수 사후확률 계산\nQ(θ | θᵗ) = E[log P(X,Z|θ)]"] --> M
    M["M-step\nQ를 최대화하는 θ 갱신\nθᵗ⁺¹ = argmax Q(θ | θᵗ)"] --> CHECK{수렴 확인\n|θᵗ⁺¹ - θᵗ| < ε}
    CHECK -->|No| E
    CHECK -->|Yes| END[최종 파라미터]
```

**E-step**: 현재 파라미터 $\theta^{(t)}$로 각 데이터 포인트가 어떤 잠재 상태에 속할 확률(소프트 할당)을 계산한다.

**M-step**: E-step에서 계산한 소프트 할당을 고정하고, 기대 완전 우도를 최대화하는 파라미터를 갱신한다.

EM은 매 반복마다 로그 우도가 단조 증가(monotonically increases)함을 보장한다. 단, 전역 최적이 아닌 지역 최적으로 수렴할 수 있다.

## 가우시안 혼합 모델 (GMM)

$K$개의 가우시안 분포의 가중 합으로 복잡한 데이터 분포를 표현한다:

$$P(x) = \sum_{k=1}^{K} \pi_k \cdot \mathcal{N}(x \mid \mu_k, \Sigma_k)$$

- $\pi_k$: 혼합 계수(mixing coefficient), $\sum_k \pi_k = 1$
- $\mu_k$: $k$번째 성분의 평균
- $\Sigma_k$: $k$번째 성분의 공분산 행렬

### GMM E-step: 책임도(Responsibility) 계산

각 데이터 포인트 $x_n$이 성분 $k$에 속할 사후 확률:

$$r_{nk} = \frac{\pi_k \mathcal{N}(x_n \mid \mu_k, \Sigma_k)}{\sum_{j=1}^{K} \pi_j \mathcal{N}(x_n \mid \mu_j, \Sigma_j)}$$

### GMM M-step: 파라미터 갱신

$$N_k = \sum_n r_{nk}, \quad \mu_k^{new} = \frac{1}{N_k}\sum_n r_{nk} x_n$$
$$\Sigma_k^{new} = \frac{1}{N_k}\sum_n r_{nk}(x_n - \mu_k^{new})(x_n - \mu_k^{new})^T, \quad \pi_k^{new} = \frac{N_k}{N}$$

## K-Means와의 관계

K-Means는 GMM에서 다음 제약을 적용한 특수 사례다:
- 모든 성분의 공분산이 동일한 단위 행렬: $\Sigma_k = \sigma^2 I$
- $\sigma \to 0$ 극한에서 소프트 할당 $r_{nk}$이 0 또는 1의 **하드 할당**으로 수렴

| 항목 | K-Means | GMM |
|------|---------|-----|
| 할당 방식 | Hard (0 또는 1) | Soft (0~1 확률) |
| 클러스터 형태 | 구형(원형) | 타원형 (Σ가 다양) |
| 출력 | 클러스터 레이블 | 소속 확률 |
| EM 관점 | Hard EM | Soft EM |
| 속도 | 빠름 | 느림 |

## ELBO와 VAE의 연결

EM이 최적화하는 ELBO(Evidence Lower BOund)는 변분 추론(variational inference)의 목적함수와 동일하다:

$$\text{ELBO} = \mathbb{E}_{q(z)}[\log p(x \mid z)] - D_{KL}[q(z) \| p(z)]$$

VAE(Variational Autoencoder)는 $q(z \mid x)$를 신경망(encoder)으로 근사하고 ELBO를 역전파로 최적화하는 방식으로, EM의 연속선상에 있다. EM의 E-step을 신경망으로 근사한 것이 VAE의 핵심 아이디어다.

## 실무 주의사항

- **초기화 민감성**: K-Means로 초기화하면 안정적인 수렴에 도움
- **공분산 행렬 타입**: Full, Diagonal, Tied, Spherical 중 데이터에 맞게 선택. Full은 표현력이 높지만 sample 수가 적으면 singular 문제 발생
- **K 선택**: BIC(Bayesian Information Criterion) 또는 AIC 사용
- `sklearn.mixture.GaussianMixture`로 간편하게 적용 가능

## 관련 문서

- [[K-평균 군집화]]
- [[autoencoders-vae]]
- [[naive-bayes]]
