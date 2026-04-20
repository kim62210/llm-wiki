---
title: 오토인코더와 변분 오토인코더 (Autoencoders & VAE)
category: foundations
page_type: concept
tags: [autoencoder, VAE, variational-autoencoder, latent-space, representation-learning, generative-model, ELBO]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

오토인코더(Autoencoder)는 입력을 저차원 잠재 공간([[embedding-layers|latent space]])으로 압축(인코딩)한 뒤 다시 원본으로 복원(디코딩)하는 비지도 학습 신경망이다. 차원 축소, 특징 학습, 노이즈 제거 등에 활용된다. 변분 오토인코더(Variational Autoencoder, VAE)는 잠재 공간에 확률 분포를 부여하여 생성 모델로 확장한 것으로, Kingma & Welling(2013)이 제안했다. VAE의 잠재 공간 개념은 [[diffusion-models]]의 Latent Diffusion과 Stable Diffusion의 핵심 기반이 되었다.

## 오토인코더 (Autoencoder)

### 구조

인코더와 디코더로 구성된 대칭적 구조다:

```
입력 x --> [인코더] --> 잠재 벡터 z --> [디코더] --> 재구성 x'
```

목적함수는 재구성 오차(reconstruction error)를 최소화하는 것이다:

```
L = ||x - x'||^2    (MSE 기준)
```

잠재 벡터의 차원이 입력보다 작을 때, 인코더는 데이터의 핵심 특징만 추출하도록 강제된다. 이를 병목 오토인코더(bottleneck autoencoder)라 한다.

### 주요 변형

| 변형 | 핵심 아이디어 |
|------|-------------|
| Denoising AE | 노이즈가 추가된 입력에서 원본을 복원 -- 더 강건한 표현 학습 |
| Sparse AE | 잠재 표현에 희소성 제약 부여 -- 해석 가능한 특징 학습 |
| Contractive AE | 잠재 표현의 야코비안을 정규화 -- 입력 변동에 둔감한 표현 |

## 변분 오토인코더 (VAE)

### 오토인코더와의 차이

일반 오토인코더의 잠재 공간은 구조가 없는 임의의 벡터 공간이다. 새로운 데이터를 생성하려면 잠재 공간에서 점을 샘플링해야 하는데, 구조 없는 공간에서의 샘플링은 의미 있는 출력을 보장하지 않는다. VAE는 잠재 공간에 확률 분포(보통 표준 정규분포)를 부여하여 이 문제를 해결한다.

### 수학적 구조

인코더가 잠재 변수의 사후 분포 q(z|x)를 근사하고, 디코더가 우도 p(x|z)를 모델링한다:

```
인코더: x --> (mu, sigma)    -- 평균과 분산을 출력
샘플링: z = mu + sigma * epsilon    (epsilon ~ N(0, I))
디코더: z --> x'
```

### ELBO (Evidence Lower Bound)

VAE의 목적함수는 로그 주변 우도의 하한(ELBO)을 최대화하는 것이다:

```
ELBO = E[log p(x|z)] - KL(q(z|x) || p(z))
     = 재구성 항     - 정규화 항
```

- **재구성 항**: 디코더가 원본을 얼마나 잘 복원하는지 (재구성 품질)
- **KL 발산 항**: 인코더의 사후 분포가 사전 분포 p(z) = N(0, I)에 얼마나 가까운지 (잠재 공간 정규화)

두 항 사이의 균형이 VAE의 핵심 트레이드오프다. KL 항이 너무 강하면 모든 입력이 동일한 잠재 분포로 수렴하여 재구성 품질이 떨어지고(posterior collapse), 너무 약하면 잠재 공간의 구조가 무너진다.

### 재매개변수화 트릭 (Reparameterization Trick)

확률 샘플링은 미분 불가능하므로, 확률적 노드를 결정론적 경로로 변환하는 재매개변수화 트릭이 필수적이다:

```
z = mu + sigma * epsilon    (epsilon은 고정된 노이즈 분포에서 샘플링)
```

기울기가 mu와 sigma를 통해 인코더로 역전파될 수 있다.

## VAE의 한계와 후속 발전

VAE의 가장 큰 한계는 재구성 결과가 흐릿(blurry)하다는 점이다. 이는 픽셀 단위 MSE 손실과 가우시안 디코더 가정의 결과다. 이 한계를 극복하기 위한 발전이 이어졌다:

- **VQ-VAE (2017)**: 연속 잠재 공간 대신 이산 코드북(codebook) 사용 -- 날카로운 재구성
- **VQ-VAE-2 (2019)**: 계층적 이산 잠재 공간으로 고해상도 생성
- **Latent Diffusion (2022)**: VAE의 잠재 공간에서 [[diffusion-models]]을 수행 -- Stable Diffusion의 핵심 구조

## 현재 위치

VAE 자체를 단독 생성 모델로 사용하는 경우는 줄었지만, VAE의 잠재 공간은 Stable Diffusion, DALL-E 등 최신 생성 모델의 필수 구성 요소다. 또한 표현 학습, 이상 탐지, 약물 분자 설계 등에서 여전히 핵심 도구로 활용된다.

## 대표 자료

- [Kingma & Welling, "Auto-Encoding Variational Bayes" (arXiv:1312.6114)](https://arxiv.org/abs/1312.6114)
- [Doersch, "Tutorial on Variational Autoencoders" (arXiv:1606.05908)](https://arxiv.org/abs/1606.05908)
- [van den Oord et al., "Neural Discrete Representation Learning (VQ-VAE)" (arXiv:1711.00937)](https://arxiv.org/abs/1711.00937)

## 관련 문서
- [[hierarchical-vae]] -- 계층적 VAE (NVAE / VD-VAE)

- [[diffusion-models]] -- VAE 잠재 공간 위에서 확산 과정을 수행 (Latent Diffusion)
- [[gans]] -- VAE와 경쟁하는 생성 모델 패러다임
- [[cnn]] -- 인코더/디코더의 백본 아키텍처
- [[transformer-architecture]] -- 최신 VAE는 Transformer 기반 인코더/디코더 사용
