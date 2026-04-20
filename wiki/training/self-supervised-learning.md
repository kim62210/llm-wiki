---
title: 자기 지도 학습 (Self-Supervised Learning)
category: training
page_type: concept
tags: [self-supervised-learning, contrastive-learning, masked-modeling, pretext-task, representation-learning]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---

# 자기 지도 학습 (Self-Supervised Learning)

## 개요

자기 지도 학습(Self-Supervised Learning, SSL)은 수동 라벨링 없이 데이터 자체의 구조에서 감독 신호를 생성하여 표현(representation)을 학습하는 패러다임이다. 입력 데이터의 일부를 가리거나 변환한 뒤 원본을 복원하도록 학습하는 **프리텍스트 태스크(pretext task)**를 통해, 모델은 데이터의 의미적 구조를 포착하는 범용 표현을 습득한다. NLP에서 [[causal-language-modeling|인과 언어 모델링]]과 [[masked-language-modeling|마스크 언어 모델링]]이 대표적이며, 컴퓨터 비전에서는 대조 학습과 마스크 이미지 모델링이 주요 기법이다.

## 지도 학습과의 관계

| 학습 패러다임 | 라벨 | 학습 신호 | 데이터 효율성 |
|-------------|------|---------|-------------|
| **지도 학습** | 수동 라벨링 필요 | 외부 어노테이션 | 라벨 비용에 제한 |
| **비지도 학습** | 없음 | 데이터 분포/클러스터링 | 직접적 태스크 유용성 불확실 |
| **자기 지도 학습** | 자동 생성 | 데이터 구조에서 추출 | 대규모 비라벨 데이터 활용 |

자기 지도 학습은 비지도 학습의 한 형태이면서도, 학습 과정 자체는 지도 학습의 프레임워크(입력-정답 쌍)를 따른다. 차이점은 정답이 사람이 아닌 데이터 자체로부터 자동 생성된다는 것이다.

## 주요 기법

### 1. 대조 학습 (Contrastive Learning)

같은 데이터의 서로 다른 뷰(augmentation)를 가깝게, 다른 데이터의 뷰는 멀게 배치하여 표현을 학습한다.

**핵심 구성요소**:
- **양성 쌍(Positive Pair)**: 동일 이미지의 두 가지 변환 (크롭, 색상 변환, 회전 등)
- **음성 쌍(Negative Pair)**: 서로 다른 이미지의 변환
- **손실 함수**: InfoNCE(NT-Xent) -- 양성 쌍의 유사도를 최대화하고 음성 쌍은 최소화

**대표 기법**:

| 기법 | 특징 | 핵심 기여 |
|------|------|----------|
| **SimCLR** | 대규모 배치로 충분한 음성 샘플 확보 | 강력한 데이터 증강의 중요성 입증 |
| **MoCo** | 모멘텀 인코더 + 큐로 음성 샘플 유지 | 배치 크기 제약 극복 |
| **BYOL** | 음성 쌍 없이 학습 (predictor 네트워크) | 음성 샘플 불필요 증명 |
| **DINO** | 자기 증류 + 센터링으로 붕괴 방지 | ViT에 최적화된 SSL |

대조 학습의 핵심 도전은 **표현 붕괴(representation collapse)** -- 모든 입력이 동일한 표현으로 매핑되는 자명한 해 -- 를 방지하는 것이다. 음성 쌍, 예측기 네트워크, 정지 그래디언트 등 다양한 전략이 이를 해결한다.

### 2. 마스크 모델링 (Masked Modeling)

입력의 일부를 마스킹하고 마스킹된 부분을 예측하도록 학습한다.

**NLP에서의 마스크 모델링**:
- [[masked-language-modeling|MLM (Masked Language Modeling)]]: BERT의 핵심 학습 방식. 입력 토큰의 15%를 마스킹하고 원래 토큰 예측
- [[causal-language-modeling|CLM (Causal Language Modeling)]]: GPT 계열. 이전 토큰만으로 다음 토큰 예측 (자기회귀)

**비전에서의 마스크 모델링**:
- **MAE (Masked Autoencoder)**: 이미지 패치의 75%를 마스킹하고 픽셀 수준 복원. He et al. (2022)가 제안하여 비전 SSL에 혁신을 가져옴
- **BEiT**: 이산 시각 토큰을 예측 (BERT 방식의 비전 적용)
- **iBOT**: 마스크 이미지 모델링 + 자기 증류 결합

MAE의 75%라는 높은 마스킹 비율은 NLP의 15%와 대조적이다. 이미지의 공간적 중복성이 높아, 모델이 자명하지 않은 복원을 학습하려면 대부분의 정보를 가려야 한다.

### 3. 비대조 기법 (Non-Contrastive Methods)

음성 쌍 없이 양성 쌍만으로 학습하는 방법론이다.

- **VICReg**: 분산(Variance), 불변(Invariance), 공분산(Covariance) 정규화로 붕괴 방지
- **Barlow Twins**: 교차 상관 행렬을 단위 행렬에 가깝게 유도
- **SimSiam**: 정지 그래디언트만으로 붕괴를 방지하는 가장 단순한 형태

## NLP 사전학습과의 연결

현대 LLM의 사전학습은 본질적으로 자기 지도 학습이다:

| 모델 계열 | SSL 방식 | 프리텍스트 태스크 |
|----------|---------|----------------|
| **BERT** | 마스크 언어 모델링 | 마스킹된 토큰 예측 + 다음 문장 예측 |
| **GPT** | 인과 언어 모델링 | 다음 토큰 예측 |
| **T5** | Span corruption | 연속 토큰 구간을 마스킹, 해당 구간 생성 |
| **ELECTRA** | 대체 토큰 감지 | GAN 방식: 가짜 토큰 vs 진짜 토큰 판별 |

[[transformer-architecture|트랜스포머]]의 등장 이후, 자기 지도 학습은 대규모 비라벨 코퍼스로 범용 언어 표현을 학습하는 표준 패러다임이 되었으며, 이를 **기반 모델(foundation model)** 패러다임이라 부른다.

## 성능과 효과

- **ImageNet**: MAE로 사전학습한 ViT-H/14는 ImageNet에서 87.8% top-1 정확도를 달성하여, 대조 학습 기반 방법을 능가
- **라벨 효율성**: SSL 사전학습 후 1%의 라벨만으로 미세조정 시, 처음부터 100% 라벨로 학습한 지도 모델과 비슷한 성능 도달
- **전이 학습**: SSL로 학습한 표현은 다양한 다운스트림 태스크에 우수한 전이 성능을 보임

## 관련 문서

- [[causal-language-modeling]] -- GPT 계열의 자기 지도 학습 방식
- [[masked-language-modeling]] -- BERT 계열의 자기 지도 학습 방식
- [[autoencoders-vae]] -- MAE의 이론적 기반인 오토인코더
- [[transfer-learning]] -- SSL 사전학습의 전이 활용
- [[knowledge-distillation]] -- DINO 등 자기 증류 기법과의 접점
- [[contextual-embeddings]] -- SSL로 학습한 문맥적 표현

## 참고 자료

- [A Survey of the Self Supervised Learning Mechanisms for Vision Transformers (arXiv 2024)](https://arxiv.org/html/2408.17059v2)
- [Masked Image Modeling: A Survey (IJCV 2025)](https://link.springer.com/article/10.1007/s11263-025-02524-1)
- [A survey on design choices for self-supervised learning in computer vision (Springer 2026)](https://link.springer.com/article/10.1007/s10462-026-11506-9)
