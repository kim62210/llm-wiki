---
title: ViT (Vision Transformer)
category: architectures
page_type: concept
tags: [vit, vision-transformer, image-classification, patch-embedding, transformer, dosovitskiy]
sources: [raw/2026-05-06-wiki-expand-scan.md, https://arxiv.org/abs/2010.11929]
created: 2026-05-06
updated: 2026-05-06
---

# ViT (Vision Transformer)

Dosovitskiy et al.(Google Brain, 2020, ICLR 2021)이 제안한 이미지를 처리하는 **순수 Transformer 아키텍처**. 이미지를 16×16 patch 시퀀스로 분할해 token처럼 다루고 표준 [[transformer-architecture|Transformer]] encoder로 처리한다. CNN에 의존하지 않고도 충분히 큰 데이터로 사전학습하면 SOTA를 능가함을 보였다. 이름 그대로 "An Image is Worth 16x16 Words"가 핵심 직관이다.

## 1. 핵심 통찰

> "A pure transformer applied directly to sequences of image patches can perform very well on image classification tasks."
> — Dosovitskiy et al. 2020 abstract

기존 Vision은 CNN의 inductive bias(지역성, 이동 불변성, 계층적 특징)에 의존했다. ViT는 이를 거의 제거하고 attention만으로 픽셀 패턴을 학습한다. 대신 **데이터·계산량이 충분히 클 때만** CNN을 능가한다.

## 2. 아키텍처

```mermaid
flowchart LR
    Img[224x224 이미지] --> Split[16x16 patches<br/>196개 토큰]
    Split --> Embed[Patch Embedding<br/>Linear 투영]
    Embed --> Add[+ Position Embedding<br/>+ CLS Token]
    Add --> Encoder[Transformer Encoder<br/>L = 12 / 24 / 32]
    Encoder --> CLS_out[CLS 출력]
    CLS_out --> MLP[MLP Head]
    MLP --> Class[클래스 확률]
```

### 핵심 구성요소

| 단계 | 설명 |
|------|------|
| **Patch embedding** | $H \times W \times C$ 이미지를 $N = HW/P^2$ 개의 $P \times P$ patch로 분할, 각 패치를 평탄화 후 선형 사상 |
| **[CLS] token** | BERT 스타일 학습 가능 토큰을 시퀀스 앞에 concat — 분류 시 이 토큰의 출력만 사용 |
| **Position embedding** | 학습 가능한 1D 벡터 (논문은 2D·상대 인코딩과 비교했지만 차이 미미) |
| **Encoder** | 표준 multi-head self-attention + MLP (ViT-Base: L=12, H=12, D=768) |

## 3. 모델 변형 (논문 기준)

| 모델 | Layers (L) | Hidden (D) | Heads (H) | Params |
|------|-----------|-----------|-----------|--------|
| ViT-Base | 12 | 768 | 12 | 86M |
| ViT-Large | 24 | 1024 | 16 | 307M |
| ViT-Huge | 32 | 1280 | 16 | 632M |

## 4. 사전학습 데이터의 결정적 영향

ViT의 가장 중요한 발견: **데이터 규모가 작으면 CNN이 더 낫다, 크면 ViT가 이긴다**.

- ImageNet-1k(1.3M): ResNet 우세
- ImageNet-21k(14M): ViT 비등
- JFT-300M(Google 내부, 300M): ViT 명백히 우세

> "Vision Transformer attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train."
> — Dosovitskiy et al. 2020

이유: CNN의 inductive bias가 적은 데이터에서는 도움이 되지만, 충분한 데이터에서는 오히려 표현력 제약으로 작용. ViT는 attention의 유연성으로 데이터에서 직접 패턴을 학습.

## 5. 후속 연구

- **DeiT** (Touvron et al. 2021): 증류 토큰을 추가해 ImageNet-1k만으로도 학습 — JFT 의존성 제거 → [[deit-data-efficient-image-transformer]]
- **[[swin-transformer|Swin Transformer]]**: 계층적 구조 + shifted window attention — detection·segmentation 강력
- **[[masked-autoencoder-mae|MAE]]**: 75% 패치 마스킹 자기지도 사전학습 → 라벨 없이 강한 representation
- **[[beit-bert-pretraining-images|BEiT]]**: BERT 스타일 masked image modeling
- **[[dinov2|DINOv2]]**: self-distillation 기반 범용 비전 표현
- **[[mobilevit-efficient-vit|MobileViT]] / EfficientFormer**: 모바일 효율 변형
- **[[hierarchical-vit-design|Hierarchical ViT]]**: 다중 해상도 구조

## 6. 멀티모달 확장

ViT는 **이미지 인코더 표준**이 되어 멀티모달 모델의 기반이 됐다.

- **[[clip|CLIP]]**: ViT 이미지 인코더 + Transformer 텍스트 인코더로 contrastive 학습
- **[[blip-paper|BLIP]] / [[blip-2-paper|BLIP-2]]**: ViT + 언어 모델 결합
- **[[vision-language-model-architectures|VLM]] 일반**: 대부분 ViT (또는 그 변형)을 vision backbone으로 사용
- **[[internvit-6b|InternViT]]**: 대규모 ViT (6B parameters)

## 7. 왜 중요한가 — 실무 관점

- **표준 vision backbone**: 2020년대 비전 모델 대부분이 ViT 또는 변형 사용. CNN은 점차 ViT로 교체됨
- **사전학습 가중치 풍부**: timm, HuggingFace에 다양한 사이즈·해상도·데이터셋 가중치 공개
- **확장성**: parameter scaling, image resolution scaling, patch size scaling 모두 명확한 trade-off가 있어 튜닝 가이드 형성
- **Cross-modal 호환**: 텍스트 transformer와 동일 구조라 통합 멀티모달 학습이 자연스러움

## 8. 한계와 trade-off

- **데이터 hungry**: 작은 데이터셋(<1M)에서는 augmentation·distillation 없이는 ResNet에 밀림
- **고해상도 비용**: token 수가 $(H/P)^2$로 quadratic attention 비용 폭증 — Swin·hierarchical 변형으로 완화
- **위치 인코딩 외삽**: 학습 해상도와 다른 입력 해상도에서 position embedding 보간 필요
- **localization 약함**: detection·segmentation에는 추가 구조(FPN, Mask Decoder) 필요

## 관련 문서

- [[transformer-architecture]] — ViT의 기반 인코더
- [[vision-transformer-vit]] — 동일 주제 상세 페이지
- [[vit-patch-embedding]] — patch embedding 단계 상세
- [[vit-register-tokens]] — register token 후속 연구
- [[vit-distillation-techniques]] — DeiT 등 증류 기법
- [[positional-encoding]] — 1D vs 2D 비교
- [[masked-image-modeling]] — MAE·BEiT 사전학습
- [[clip]] — ViT를 활용한 대표 멀티모달 모델
- [[vision-language-models]] — VLM 일반론
- [[swin-transformer]] — 계층적 ViT
- [[internvit-6b]] — 대규모 ViT
