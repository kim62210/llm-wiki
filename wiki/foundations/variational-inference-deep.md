---
title: 변분 추론 심화 (ELBO/Reparametrization)
category: foundations
page_type: concept
tags: [변분추론, ELBO, 재매개변수화, 베이지안, VAE, 평균장근사]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 변분 추론 심화 (ELBO/Reparametrization)

## 정의와 동기

변분 추론(Variational Inference, VI)은 다루기 어려운 사후 분포 $p(z|x)$를 단순한 근사 분포 $q(z)$로 근사하는 확률론적 방법이다. 베이지안 딥러닝, 변분 오토인코더(VAE), 정규화 흐름(normalizing flows) 등의 이론적 기반이 된다.

### 왜 사후 분포를 직접 계산하기 어려운가

베이즈 정리에 따르면:

$$p(z|x) = \frac{p(x|z) p(z)}{p(x)}$$

분모 $p(x) = \int p(x|z) p(z) dz$는 잠재 공간 전체의 적분이 필요하며, 대부분의 실용적 모델에서 이 적분이 비가산(intractable)하다.

변분 추론은 이 계산 문제를 **최적화 문제**로 전환한다.

---

## ELBO (Evidence Lower BOund)

### 유도

$q(z)$가 진짜 사후 분포 $p(z|x)$에 얼마나 가까운지를 KL 발산(KL-divergence)으로 측정한다:

$$KL(q(z) \| p(z|x)) = \mathbb{E}_q\left[\log \frac{q(z)}{p(z|x)}\right]$$

이를 전개하면:

$$KL(q \| p) = \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(z,x)] + \log p(x)$$

$\log p(x) \geq 0$이므로:

$$\log p(x) = \underbrace{\mathbb{E}_q[\log p(x,z)] - \mathbb{E}_q[\log q(z)]}_{\text{ELBO}} + KL(q \| p)$$

KL 발산이 항상 $\geq 0$이므로:

$$\log p(x) \geq \text{ELBO}$$

**ELBO를 최대화 = KL 발산 최소화 = $q$가 $p(z|x)$에 근사**

### ELBO 분해

ELBO는 두 항으로 분해할 수 있다:

$$\text{ELBO} = \underbrace{\mathbb{E}_q[\log p(x|z)]}_{\text{재구성 항}} - \underbrace{KL(q(z) \| p(z))}_{\text{정규화 항}}$$

| 항 | 의미 | 역할 |
|----|------|------|
| 재구성 항 | $z$가 $x$를 잘 설명하는가 | 데이터 적합도 |
| 정규화 항 | $q(z)$가 사전 분포에서 벗어나는 정도 | 과적합 방지 |

VAE에서 이 두 항은 각각 픽셀 재구성 손실(MSE/BCE)과 KL 정규화 손실에 대응한다.

---

## 재매개변수화 트릭 (Reparametrization Trick)

### 문제: 샘플링의 미분 불가능성

ELBO 최적화에서 $\mathbb{E}_{q(z;\phi)}[\cdot]$의 $\phi$에 대한 그래디언트를 계산해야 한다. 그러나 $z \sim q(z;\phi)$에서 샘플링은 미분 불가능한 연산이다.

### 해결: 노이즈 분리

$z$를 확정적 변환으로 표현한다:

$$z = \mu_\phi + \sigma_\phi \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

이제 확률성은 $\epsilon$에, 학습 가능한 파라미터는 $\mu_\phi, \sigma_\phi$에 분리된다.

```python
class VAEEncoder(nn.Module):
    def forward(self, x):
        h = self.encoder_net(x)
        mu = self.fc_mu(h)
        log_var = self.fc_logvar(h)
        return mu, log_var

    def reparametrize(self, mu, log_var):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)  # 확률성은 여기에
        z = mu + eps * std           # 미분 가능한 변환
        return z
```

역전파 시 그래디언트는 $\mu_\phi$와 $\sigma_\phi$를 통해 흐르며, $\epsilon$ 경로는 그래디언트 흐름에 기여하지 않는다.

---

## 흐름도: 변분 추론 전체 파이프라인

```mermaid
flowchart TD
    X[관측 데이터 x] --> Enc[인코더 q_φ z|x\n μ, σ 출력]
    Enc --> Rep[재매개변수화\n z = μ + σ·ε\n ε ~ N0,I]
    Rep --> Dec[디코더 p_θ x|z\n 재구성 x']
    Dec --> Recon[재구성 손실\n E_q log p x|z]
    Enc --> KL[KL 발산\n KL q_φ || p z]
    Recon --> ELBO[ELBO 최대화\n = 재구성 - KL]
    KL --> ELBO
    ELBO --> Opt[역전파 + 최적화\n φ와 θ 동시 갱신]
```

재매개변수화 트릭을 통해 샘플링 연산을 미분 가능하게 만들어 전체 파이프라인을 end-to-end로 학습한다.

---

## 평균장 근사 (Mean-Field Approximation)

변분 추론에서 $q(z)$의 형태를 어떻게 선택하느냐가 중요하다. 평균장 근사는 가장 단순한 선택 중 하나다.

### 정의

잠재 변수들이 독립적이라고 가정:

$$q(z) = \prod_{i} q_i(z_i)$$

### 장단점

| 항목 | 내용 |
|------|------|
| 장점 | 각 $q_i$를 독립적으로 최적화 가능, 계산 효율 |
| 단점 | 변수 간 상관관계 무시, 사후 분포 근사 품질 제한 |
| 적용 | 토픽 모델(LDA), 초기 BNN |

### 더 표현력 있는 대안

- **정규화 흐름(Normalizing Flows)**: 단순 분포를 연속 가역 변환으로 복잡하게 만듦
- **계층적 변분 추론**: 다단계 잠재 변수 구조

---

## 정규화 흐름과의 결합

평균장 근사의 표현력 한계를 극복하기 위해 $q(z)$를 정규화 흐름으로 표현한다:

$$z_K = f_K \circ f_{K-1} \circ \cdots \circ f_1(z_0), \quad z_0 \sim q_0$$

변환된 분포의 로그 밀도는 야코비안 행렬식으로 계산:

$$\log q_K(z_K) = \log q_0(z_0) - \sum_{k=1}^{K} \log \left|\det \frac{\partial f_k}{\partial z_{k-1}}\right|$$

이를 통해 임의로 복잡한 $q(z)$를 표현할 수 있다.

---

## 실무 활용

### VAE 학습 팁

- **KL annealing**: 초기에 KL 항의 가중치를 0에서 점진적으로 증가시켜 "posterior collapse" 방지
- **Free bits**: KL 값이 특정 임계값 이하일 때 그래디언트를 차단해 안정적 학습
- **$\beta$-VAE**: KL 항에 $\beta > 1$ 가중치를 주어 disentangled 표현 학습

```python
def vae_loss(x, x_recon, mu, log_var, beta=1.0):
    recon_loss = F.binary_cross_entropy(x_recon, x, reduction='sum')
    kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    return recon_loss + beta * kl_loss
```

### 베이지안 신경망(BNN)에서의 활용

- 각 가중치를 확률 분포로 모델링
- 평균장 VI로 사후 분포 근사
- 불확실성 정량화와 과적합 방지 동시 달성

---

## 관련 문서

- [[bayesian-inference]] - 베이지안 추론 기초
- [[normalizing-flows]] - 정규화 흐름과의 결합
- [[deep-ensembles]] - 변분 추론 대안으로서의 앙상블
- [[swag-stochastic-weight-averaging]] - SWAG의 가우시안 사후 분포 근사
- [[continuous-normalizing-flows]] - 연속 정규화 흐름 (CNF)
