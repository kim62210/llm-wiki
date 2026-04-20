---
title: MAE - 마스크드 오토인코더 (Masked Autoencoders)
category: architectures
page_type: concept
tags: [mae, masked-autoencoder, self-supervised, vision]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# MAE - 마스크드 오토인코더 (Masked Autoencoders)

MAE(Masked Autoencoder)는 He et al. (Meta AI, 2021)이 제안한 자기지도 비전 사전학습 방법이다. NLP의 BERT(Masked Language Modeling)를 비전에 대응시키되, **75%라는 매우 높은 마스킹 비율**과 **비대칭 인코더-디코더** 구조라는 두 가지 핵심 차이로 비전 특성에 최적화했다.

## 핵심 아이디어

### 왜 75% 마스킹인가

BERT는 15% 마스킹을 사용한다. 비전에서 75%가 적절한 이유는 **이미지의 중복성(redundancy)**이 텍스트보다 훨씬 높기 때문이다. 인접 픽셀은 매우 유사한 정보를 담는다. 낮은 마스킹 비율로는 단순한 보간(interpolation)만으로 복원할 수 있어 의미 있는 표현을 학습하지 못한다. 75% 이상을 가려야 모델이 **전체 맥락을 이해**해야만 복원할 수 있다.

### 비대칭 인코더-디코더

```mermaid
flowchart LR
    subgraph 입력
        IMG["이미지 패치\n196개 (16x16)"]
    end
    subgraph 인코더 "인코더 (ViT-Large)"
        VIS["가시 패치\n~49개 (25%)"]
        ENC["Transformer\n블록 × 24"]
        VIS --> ENC
    end
    subgraph 디코더 "디코더 (경량)"
        MASK["마스크 토큰\n~147개"]
        DEC["Transformer\n블록 × 8"]
        MASK --> DEC
        ENC --> DEC
        DEC --> RECON["픽셀 복원"]
    end
    IMG --> VIS
    IMG --> MASK
```

- **인코더**: 가시(visible) 패치만 처리. 전체 패치의 25%이므로 연산 대폭 절감
- **디코더**: 가시 패치의 인코딩 + 마스크 토큰(학습 가능한 벡터) 전체를 처리해 픽셀 복원
- 디코더는 얕고 좁게 설계. 사전학습 후 버려지며, 인코더만 다운스트림에 사용

## BERT MLM과의 비교

| 항목 | BERT MLM | MAE |
|------|----------|-----|
| 입력 | 텍스트 토큰 | 이미지 패치 |
| 마스킹 비율 | 15% | 75% |
| 인코더 입력 | 전체 (마스크 포함) | 가시 패치만 |
| 복원 대상 | 원본 토큰 | 픽셀 값 |
| 중복성 | 낮음 | 높음 → 높은 마스킹 필요 |

## 학습 목표

복원 손실(reconstruction loss)은 마스크된 패치의 **정규화된 픽셀 값** MSE(Mean Squared Error)다.

$$L = \frac{1}{|\mathcal{M}|} \sum_{p \in \mathcal{M}} \left\| x_p - \hat{x}_p \right\|^2$$

$\mathcal{M}$은 마스크된 패치 집합, $x_p$는 원본 픽셀, $\hat{x}_p$는 복원된 픽셀이다. 패치 내부를 정규화(normalize per patch)해 고주파 디테일 학습을 강화한다.

## 사전학습 효율성

MAE는 기존 대조 학습(contrastive learning) 방법 대비 **3배 빠른 학습**을 제공한다. 인코더가 전체 패치의 25%만 처리하기 때문이다. ViT-Huge를 1600 에폭 학습해도 합리적인 시간 내에 완료된다.

## 파인튜닝 결과

| 모델 | 방법 | ImageNet top-1 |
|------|------|---------------|
| ViT-B | 지도학습 | 81.8% |
| ViT-B | MAE 사전학습 + FT | 83.1% |
| ViT-L | 지도학습 | 82.6% |
| ViT-L | MAE 사전학습 + FT | 85.9% |
| ViT-H | MAE 사전학습 + FT | 86.9% |

## 관련 문서
- [[vision-transformer|Vision Transformer]]
- [[bert|BERT]]
- [[dinov2|DINOv2]]
- [[convnext|ConvNeXt]]
- [[swin-transformer|Swin Transformer]]
