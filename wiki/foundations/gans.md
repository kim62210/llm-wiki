---
title: 생성적 적대 신경망 (GANs)
category: foundations
page_type: concept
tags: [GAN, generative-adversarial-network, generator, discriminator, mode-collapse, WGAN, image-generation]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

생성적 적대 신경망(Generative Adversarial Network, GAN)은 Goodfellow et al.(2014)이 제안한 생성 모델로, 생성자(generator)와 판별자(discriminator) 두 네트워크가 경쟁적으로 학습하는 구조다. 생성자는 실제 데이터와 구별할 수 없는 가짜 데이터를 만들려 하고, 판별자는 진짜와 가짜를 구별하려 한다. 이 적대적 게임이 내쉬 균형(Nash equilibrium)에 도달하면 생성자가 실제 데이터 분포를 근사하게 된다. 이미지 생성 분야를 혁신했으나, 학습 불안정성과 모드 붕괴(mode collapse) 문제로 인해 현재는 [[diffusion-models]]에 주류를 넘겨주었다.

## 핵심 구조

### 적대적 학습 (Adversarial Training)

생성자 G와 판별자 D의 미니맥스 게임으로 정의된다:

```
min_G max_D  V(D, G) = E[log D(x)] + E[log(1 - D(G(z)))]
```

- **생성자 G**: 노이즈 벡터 z ~ p(z)를 입력받아 가짜 데이터 G(z) 생성
- **판별자 D**: 입력이 실제 데이터인지(D(x) -> 1) 생성 데이터인지(D(G(z)) -> 0) 판별

학습은 판별자와 생성자를 번갈아 업데이트하는 방식으로 진행된다.

### 학습 과정

```
1. 판별자 업데이트: 실제 데이터 -> D -> 1, 가짜 데이터 -> D -> 0 (판별 능력 강화)
2. 생성자 업데이트: 가짜 데이터 -> D -> 1 (판별자를 속이는 방향)
3. 1-2를 반복
```

## 학습의 핵심 난제

### 모드 붕괴 (Mode Collapse)

GAN의 가장 악명 높은 문제다. 생성자가 데이터 분포의 일부 모드(mode)만 학습하여 다양성이 극도로 떨어지는 현상이다. 예를 들어 MNIST 학습 시 숫자 "1"만 반복 생성하는 식이다. 원인은 생성자가 판별자를 속이는 특정 출력에 수렴하면, 판별자가 이를 거부해도 다른 모드를 탐색하지 못하는 데 있다.

### 학습 불안정성

판별자와 생성자의 균형이 깨지면 학습이 불안정해진다:

- **판별자가 너무 강하면**: 생성자의 기울기가 소실되어 학습이 멈춤
- **생성자가 너무 강하면**: 판별자가 무력화되어 의미 있는 피드백을 제공하지 못함
- **진동(oscillation)**: 두 네트워크가 수렴하지 않고 계속 진동

### 평가의 어려움

GAN은 명시적 우도(likelihood)를 계산하지 않으므로, 생성 품질을 객관적으로 평가하기 어렵다. FID(Frechet Inception Distance)와 IS(Inception Score)가 대리 지표로 사용되지만, 완전한 평가는 아니다.

## 주요 변형과 해결 시도

| 모델 | 핵심 기여 |
|------|----------|
| DCGAN (2015) | CNN 기반 안정적 구조, 배치 정규화 활용 |
| WGAN (2017) | Wasserstein 거리로 손실 함수 교체 -- 학습 안정성 대폭 개선 |
| WGAN-GP (2017) | 기울기 페널티(gradient penalty)로 WGAN의 가중치 클리핑 대체 |
| Progressive GAN (2017) | 저해상도에서 고해상도로 점진적 학습 -- 1024x1024 생성 |
| StyleGAN (2018) | 스타일 기반 생성자, 잠재 공간 분리, 고품질 얼굴 생성 |
| StyleGAN2 (2019) | 아티팩트 제거, 경로 정규화 |
| StyleGAN3 (2021) | 이동 등변(translation equivariance) 달성 |

### WGAN의 핵심 통찰

표준 GAN의 Jensen-Shannon 발산은 두 분포의 지지(support)가 겹치지 않을 때 의미 있는 기울기를 제공하지 못한다. WGAN은 Wasserstein-1 거리(Earth Mover's Distance)로 대체하여 이 문제를 해결했다. 판별자를 1-Lipschitz 함수로 제약하며(가중치 클리핑 또는 기울기 페널티), 이를 통해 판별자를 최적까지 학습해도 생성자에 유의미한 기울기가 전달된다.

## GAN vs 다른 생성 모델

| 항목 | GAN | [[autoencoders-vae|VAE]] | [[diffusion-models|Diffusion]] |
|------|-----|-----|-----------|
| 생성 품질 | 높음 (선명) | 낮음 (흐릿) | 매우 높음 |
| 학습 안정성 | 낮음 | 높음 | 높음 |
| 다양성 | 모드 붕괴 위험 | 높음 | 매우 높음 |
| 우도 계산 | 불가 | ELBO | 가능 |
| 샘플링 속도 | 매우 빠름 (단일 패스) | 빠름 | 느림 (반복 디노이징) |

## 현재 위치

이미지 생성의 주류는 [[diffusion-models]]로 이동했지만, GAN의 영향력은 여전하다. 실시간 이미지 변환, 초해상도(super-resolution), 데이터 증강 등 빠른 생성이 필요한 응용에서 GAN이 활용되며, Diffusion 모델의 샘플링을 가속하는 distillation에도 적대적 학습 원리가 적용된다. StyleGAN의 잠재 공간 조작 기법은 생성 모델의 해석 가능성 연구에 핵심 도구로 남아 있다.

## 대표 자료

- [Goodfellow et al., "Generative Adversarial Nets" (NeurIPS 2014)](https://arxiv.org/abs/1406.2661)
- [Arjovsky et al., "Wasserstein GAN" (arXiv:1701.07875)](https://arxiv.org/abs/1701.07875)
- [Karras et al., "A Style-Based Generator Architecture for GANs (StyleGAN)" (arXiv:1812.04948)](https://arxiv.org/abs/1812.04948)

## 관련 문서

- [[diffusion-models]] -- GAN을 대체한 현재의 주류 생성 모델
- [[autoencoders-vae]] -- 경쟁적 생성 모델 패러다임 (우도 기반)
- [[cnn]] -- 생성자/판별자의 백본 아키텍처
- [[transformer-architecture]] -- ViT-GAN 등 Transformer 기반 GAN 변형
