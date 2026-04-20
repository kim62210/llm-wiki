---
title: 잠재 확산 모델 (Latent Diffusion Model / LDM)
category: architectures
page_type: concept
tags: [ldm, latent-diffusion, stable-diffusion, vae]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 잠재 확산 모델 (Latent Diffusion Model / LDM)

잠재 확산 모델(LDM)은 Rombach et al. (2022)이 제안한 방법으로, 확산(diffusion) 과정을 고차원 픽셀 공간이 아닌 **저차원 잠재 공간(latent space)**에서 수행한다. Stable Diffusion의 기반 아키텍처로, "픽셀 공간 확산 대비 수십 배 연산 절감"이라는 실용적 이점을 제공하면서도 이미지 품질을 유지한다.

## 2단계 학습 구조

```mermaid
flowchart TD
    subgraph 1단계 "1단계: VAE 학습"
        IMG1["픽셀 이미지\n512×512×3"] --> ENC["VAE 인코더"]
        ENC --> LAT["잠재 벡터\n64×64×4"]
        LAT --> DEC["VAE 디코더"]
        DEC --> RECON["재구성 이미지"]
    end
    subgraph 2단계 "2단계: 확산 모델 학습"
        LAT2["잠재 벡터 z\n64×64×4"] --> NOISE["노이즈 추가\nq(z_t|z_0)"]
        NOISE --> UNET["U-Net 디노이저\nε_θ(z_t, t, c)"]
        COND["조건 c\n(텍스트/클래스)"] --> UNET
        UNET --> PRED["노이즈 예측"]
    end
```

## VAE 잠재 공간

VAE(Variational Autoencoder) 인코더는 $512 \times 512 \times 3$ 픽셀 이미지를 $64 \times 64 \times 4$ 잠재 벡터로 압축한다. 공간 해상도 기준 64배 압축이다. 확산 모델은 이 잠재 공간에서 동작하므로:
- 자기 어텐션 시퀀스 길이: $512^2 = 262,144$ → $64^2 = 4,096$ (64배 감소)
- 연산 비용 감소: $O(n^2)$ 어텐션 기준 약 4,096배 감소

## 조건화 (Conditioning) 메커니즘

### 크로스 어텐션 텍스트 주입
텍스트 프롬프트를 CLIP 텍스트 인코더로 임베딩하고, U-Net 내부에서 **크로스 어텐션**으로 잠재 특징과 결합한다.

$$\text{CrossAttn}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d}}\right) V$$

- $Q$: U-Net 공간 특징에서 파생
- $K, V$: 텍스트 임베딩에서 파생

### Classifier-Free Guidance (CFG)
학습 시 10-20% 비율로 조건을 드롭(빈 텍스트 $\emptyset$ 대체)해 두 가지 모델을 동시에 학습한다.

샘플링 시 가이드된 예측:
$$\hat{\epsilon} = \epsilon_\theta(z_t, \emptyset) + w \cdot (\epsilon_\theta(z_t, c) - \epsilon_\theta(z_t, \emptyset))$$

$w$ (guidance scale)가 클수록 조건에 더 충실한 이미지를 생성하지만 다양성이 감소한다.

## SD/SDXL/SD3 진화

| 버전 | 특징 | 잠재 공간 |
|------|------|---------|
| SD 1.x | LDM 기반, CLIP ViT-L/14 | 64×64×4 |
| SD 2.x | OpenCLIP, 음성 프롬프트 개선 | 64×64×4 |
| SDXL | 두 CLIP 텍스트 인코더, 더 큰 U-Net | 128×128×4 |
| SD3 | Diffusion Transformer(DiT), Flow Matching | 16ch |

## LDM U-Net 내부 구조

U-Net은 확산 타임스텝 $t$와 조건 $c$를 동시에 처리하는 특수 구조다:
- **인코더**: ResNet 블록 + Self-Attention (저해상도 레벨만)
- **병목(Bottleneck)**: Self-Attention + Cross-Attention
- **디코더**: 스킵 연결로 인코더 특징 병합
- 각 블록에 타임스텝 임베딩($t$ → Sinusoidal → MLP → FiLM)이 주입됨

## 관련 문서
- [[diffusion-transformer|Diffusion Transformer (DiT)]]
- [[u-net|U-Net]]
- [[flow-matching|플로우 매칭]]
- [[consistency-models|일관성 모델]]
- [[cross-attention|크로스 어텐션]]
- [[clip|CLIP]]
