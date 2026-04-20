---
title: 확산 모델 (Diffusion Models)
category: foundations
page_type: concept
tags: [diffusion, DDPM, DDIM, stable-diffusion, denoising, score-matching, latent-diffusion, image-generation]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

확산 모델(Diffusion Model)은 데이터에 점진적으로 노이즈를 추가하는 전방 과정(forward process)을 학습한 뒤, 이를 역전시켜 노이즈에서 데이터를 생성하는 역방 과정(reverse process)을 수행하는 생성 모델이다. Ho et al.(2020)의 DDPM(Denoising Diffusion Probabilistic Model)이 실질적인 시작점이며, DDIM(2020)이 샘플링 속도를 개선하고, Rombach et al.(2022)의 Latent Diffusion이 [[autoencoders-vae|VAE]]의 잠재 공간에서 확산을 수행하여 Stable Diffusion의 기반이 되었다. 현재 이미지, 비디오, 오디오, 3D 생성의 핵심 패러다임이다.

## 핵심 원리

### 전방 과정 (Forward Process / Diffusion)

원본 데이터 x_0에 T단계에 걸쳐 가우시안 노이즈를 점진적으로 추가한다. 충분히 많은 단계를 거치면 x_T는 순수 가우시안 노이즈에 수렴한다:

```
q(x_t | x_{t-1}) = N(x_t; sqrt(1 - beta_t) * x_{t-1}, beta_t * I)
```

노이즈 스케줄 beta_1, ..., beta_T가 각 단계의 노이즈 강도를 결정한다. 마르코프 체인으로 정의되며, 임의의 시점 t에서 x_t를 닫힌 형태(closed form)로 직접 계산할 수 있다:

```
x_t = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * epsilon
(alpha_bar_t = prod_{s=1}^{t} (1 - beta_s),  epsilon ~ N(0, I))
```

### 역방 과정 (Reverse Process / Denoising)

신경망 epsilon_theta가 x_t에서 추가된 노이즈 epsilon을 예측한다. 학습 목적함수는 단순한 MSE다:

```
L = E[||epsilon - epsilon_theta(x_t, t)||^2]
```

생성 시에는 x_T ~ N(0, I)에서 시작하여 T단계에 걸쳐 노이즈를 제거해 나간다.

## DDPM vs DDIM

| 항목 | DDPM | DDIM |
|------|------|------|
| 샘플링 과정 | 확률적 (마르코프) | 결정론적 (비마르코프) |
| 필요 단계 | 1000 (원래) | 20-50으로 축소 가능 |
| 재현성 | 매번 다른 결과 | 동일 노이즈 -> 동일 결과 |
| 보간 | 어려움 | 잠재 공간에서 직접 보간 가능 |
| 추가 학습 | 불필요 | DDPM으로 학습한 모델 그대로 사용 |

DDIM의 핵심 통찰은 DDPM의 전방 과정을 비마르코프(non-Markovian) 과정으로 재정의하여, 동일한 학습된 모델에서 샘플링 단계를 자유롭게 줄일 수 있다는 점이다.

## Latent Diffusion과 Stable Diffusion

### 픽셀 공간의 한계

고해상도 이미지(512x512 이상)에서 직접 확산을 수행하면 연산 비용이 막대하다. Rombach et al.(2022)은 사전 학습된 [[autoencoders-vae|VAE]]로 이미지를 저차원 잠재 공간(예: 64x64x4)으로 압축한 뒤, 이 잠재 공간에서 확산 과정을 수행하는 Latent Diffusion Model(LDM)을 제안했다.

### Stable Diffusion 구조

```
[텍스트 프롬프트] -> [CLIP 텍스트 인코더] -> 텍스트 임베딩
                                                |
[순수 노이즈 z_T] -> [U-Net 디노이징 (교차 어텐션)] -> [잠재 벡터 z_0] -> [VAE 디코더] -> [이미지]
```

- **VAE 인코더/디코더**: [[cnn]] 기반, 픽셀 공간과 잠재 공간 간 변환
- **U-Net**: 디노이징을 수행하는 핵심 네트워크, 잔차 블록 + [[self-attention-mechanism]] + 교차 어텐션
- **교차 어텐션(cross-attention)**: 텍스트 조건을 디노이징 과정에 주입

## Score Matching 관점

확산 모델은 스코어 매칭(score matching) 프레임워크와 이론적으로 동치다. Song & Ermon(2019)의 연구에서 정립되었다:

- **스코어 함수**: 데이터 로그 확률의 기울기 nabla_x log p(x)
- DDPM의 노이즈 예측 epsilon_theta는 스코어 함수의 스케일된 버전
- 생성은 앙주뱅 동역학(Langevin dynamics)으로 해석 가능

이 통합 관점은 연속 시간 확산(SDE/ODE 프레임워크)으로 확장되어 더 유연한 샘플링 전략을 가능하게 했다.

## 조건부 생성 (Conditional Generation)

### Classifier-Free Guidance (CFG)

현재 가장 널리 사용되는 조건부 생성 기법이다. 학습 시 일정 비율로 조건을 드롭아웃하여 조건부/비조건부 모델을 동시에 학습하고, 생성 시 두 예측의 차이를 증폭한다:

```
epsilon_guided = epsilon_uncond + w * (epsilon_cond - epsilon_uncond)
```

가이던스 스케일 w가 클수록 조건에 충실하지만 다양성이 감소한다.

## 현재 위치와 후속 발전

확산 모델은 DALL-E 2, Midjourney, Stable Diffusion, Imagen 등 텍스트-이미지 생성의 핵심이며, Sora, Runway Gen-3 등 비디오 생성으로 확장되고 있다. 주요 연구 방향은 샘플링 가속(Consistency Models, Rectified Flow), 아키텍처 개선(DiT -- [[transformer-architecture]] 기반 디노이징), 그리고 3D/4D 생성이다.

## 대표 자료

- [Ho et al., "Denoising Diffusion Probabilistic Models (DDPM)" (arXiv:2006.11239)](https://arxiv.org/abs/2006.11239)
- [Song et al., "Denoising Diffusion Implicit Models (DDIM)" (arXiv:2010.02502)](https://arxiv.org/abs/2010.02502)
- [Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models" (arXiv:2112.10752)](https://arxiv.org/abs/2112.10752)

## 관련 문서

- [[autoencoders-vae]] -- Latent Diffusion의 잠재 공간을 제공하는 VAE
- [[gans]] -- 확산 모델 이전의 주류 생성 모델
- [[cnn]] -- U-Net 백본의 기반 아키텍처
- [[self-attention-mechanism]] -- U-Net 내부 어텐션 계층
- [[transformer-architecture]] -- DiT (Diffusion Transformer) 아키텍처
