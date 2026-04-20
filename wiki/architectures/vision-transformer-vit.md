---
title: Vision Transformer (ViT)
category: architectures
page_type: concept
tags: [vit, vision-transformer, image-classification, patch-embedding, cls-token]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# Vision Transformer (ViT)

Dosovitskiy et al. (2020)이 제안한 이미지 분류용 순수 Transformer 아키텍처. 이미지를 고정 크기 **패치(patch)**로 분할하고 선형 임베딩한 후 표준 [[transformer-architecture|Transformer]] 인코더에 입력한다. "An Image is Worth 16x16 Words"라는 제목이 핵심을 요약한다.

## 아키텍처

```mermaid
flowchart LR
    Img[이미지 224x224] --> Patch[16x16 패치 196개]
    Patch --> Linear[선형 임베딩 + 위치 인코딩]
    Linear --> CLS[CLS 토큰 추가]
    CLS --> Encoder[Transformer 인코더 x L]
    Encoder --> Head[CLS 출력 -> 분류 헤드]
```

## 핵심 설계 결정

| 요소 | 설명 |
|------|------|
| 패치 크기 | 16x16 (224x224 이미지 -> 196 토큰) |
| 위치 인코딩 | 학습 가능한 1D 벡터 (2D 인코딩 대비 차이 미미) |
| CLS 토큰 | BERT 스타일, 전체 이미지 표현 집약 |
| 사전학습 | **대규모 데이터**(JFT-300M) 필수 -- 소규모에서는 [[cnn|CNN]] 대비 열세 |

## 후속 발전

- **DeiT (Data-efficient ViT)**: 증류 토큰으로 ImageNet만으로도 학습 가능
- **BEiT**: [[masked-autoencoder-mae|MAE]] 스타일 마스킹 사전학습
- **[[swin-transformer|Swin Transformer]]**: 계층적 구조 + 시프팅 윈도우
- **[[dinov2|DINOv2]]**: 자기지도 학습으로 범용 비전 표현

## [[cnn|CNN]]과의 관계

ViT는 **귀납적 편향(inductive bias)**이 적다 -- CNN의 지역성(locality)과 이동 불변성(translation invariance)이 없어 대규모 데이터가 필요하지만, 데이터가 충분하면 CNN을 능가한다.

## 관련 문서
- [[mapo-multimodal-agentic-paper]] -- MAPO: 멀티모달 에이전트 정책 최적화
- [[tempo-video-vlm-compressor-paper]] -- Tempo: 소규모 VLM을 비디오 시간 압축기로 활용
- [[patchtst-timeseries]] -- PatchTST - 패치 기반 시계열 Transformer

- [[transformer-architecture]] -- Transformer 아키텍처
- [[swin-transformer]] -- Swin Transformer
- [[dinov2]] -- DINOv2
- [[masked-autoencoder-mae]] -- MAE
- [[clip]] -- CLIP (ViT 이미지 인코더)
