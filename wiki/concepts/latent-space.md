---
title: Latent Space (잠재 공간)
category: concepts
page_type: concept
tags: [concepts, concept, latent-space, representation-learning, embeddings, generative-models]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---
# Latent Space (잠재 공간)

고차원 데이터의 본질적 구조를 저차원 연속 벡터로 압축한 표현 공간. 유사한 항목이 가까이 위치하는 매니폴드(manifold) 위에 데이터를 배치하며, VAE, GAN, Diffusion Model, LLM 임베딩 등 현대 딥러닝의 거의 모든 생성/표현 모델에서 핵심 역할을 한다.

## 왜 중요한가

잠재 공간은 딥러닝에서 데이터를 "이해"하는 방식 그 자체이다. 원본 데이터(이미지의 픽셀, 텍스트의 토큰)는 고차원이고 희소하지만, 잠재 공간에서는 의미적으로 유사한 데이터가 가까이 모여 연속적인 구조를 형성한다. 이 압축된 표현 덕분에 생성(generation), 보간(interpolation), 전이 학습(transfer learning), 의미 검색(semantic search)이 가능해진다.

## 수학적 기초

잠재 공간은 잠재 변수(latent variable)의 집합으로 위치가 정의되며, 이 변수들은 관측 데이터 간의 유사성에서 도출된다. 일반적으로 원본 특성 공간보다 낮은 차원을 가지며, 이는 차원 축소(dimensionality reduction)와 데이터 압축의 한 형태이다. 머신러닝으로 학습되며, 이후 분류기나 지도 학습 예측기에서 특성 공간으로 활용된다.

## 모델별 역할

### VAE (Variational Autoencoder)

인코더가 입력 데이터를 잠재 공간의 확률 분포(평균과 분산)로 매핑하고, 디코더가 이 분포에서 샘플링하여 데이터를 복원한다. VAE는 인코딩과 디코딩을 동시에 학습하며, 잠재 공간이 곧 임베딩 공간이 된다. KL divergence 정규화가 잠재 공간을 매끄러운 연속 분포로 만들어, 공간 내 임의의 점에서 샘플링해도 의미 있는 출력을 생성할 수 있다.

### GAN (Generative Adversarial Network)

생성자(Generator)가 저차원 노이즈 벡터(잠재 코드)를 입력받아 현실적인 데이터를 생성하고, 판별자(Discriminator)가 진위를 판별한다. GAN의 잠재 공간은 VAE와 달리 명시적 확률 분포 제약이 없어 더 날카로운 출력을 생성하지만, 공간의 구조가 불연속적일 수 있고 mode collapse 위험이 있다. VAE-GAN 하이브리드 아키텍처는 두 접근의 장점을 결합한다.

### Diffusion Model

Latent Diffusion Model(LDM, Stable Diffusion의 기반)은 VAE 스타일 인코더로 입력을 저차원 잠재 표현으로 먼저 변환한 뒤, 이 잠재 공간에서 확산(diffusion) 과정을 적용한다. 픽셀 공간에서 직접 확산하는 것 대비 계산 비용을 크게 줄이면서도, 잠재 공간의 구조적 장점을 활용하여 고품질 생성이 가능하다. 최근 연구에서는 의미 분리 VAE(Semantic-Disentangled VAE)를 통해 잠재 공간의 해석 가능성과 생성 품질을 동시에 개선하는 접근이 제안되었다.

### LLM 임베딩

대규모 언어 모델은 토큰을 고차원 잠재 공간의 벡터로 매핑한다. Word2Vec과 GloVe가 단어 수준 임베딩의 초기 사례이며, "king - man + woman = queen" 같은 의미적 산술이 잠재 공간의 구조를 보여주는 대표적 예시이다. 트랜스포머 기반 LLM에서는 각 레이어가 잠재 표현을 점진적으로 정제하며, 마지막 레이어의 표현이 다음 토큰 예측이나 의미 검색에 사용된다. IBM Granite과 같은 모델은 이 잠재 공간을 활용해 특정 문맥에서 단어 간 복잡한 관계를 탐색한다.

## 시각화 기법

잠재 공간은 통상 수백~수천 차원이므로 직접 시각화가 불가능하다. 주요 차원 축소 기법으로 2D/3D 투영이 사용된다:

- **t-SNE (t-distributed Stochastic Neighbor Embedding)**: 국소적 이웃 구조를 보존하여 클러스터 시각화에 강하지만, 전역 거리 관계는 왜곡될 수 있다.
- **UMAP (Uniform Manifold Approximation and Projection)**: t-SNE보다 전역 구조를 더 잘 보존하며 계산이 빠르다. 대규모 데이터셋에서 선호된다.
- **PCA (Principal Component Analysis)**: 선형 투영으로 빠르지만, 비선형 구조를 포착하지 못한다. 초기 탐색이나 전처리에 사용된다.

잠재 공간의 거리는 물리적 단위가 없으므로, 해석은 애플리케이션 맥락에 의존한다.

## 핵심 도전 과제

- **블랙박스 특성**: 모델의 잠재 공간은 직관적이지 않으며, 각 차원이 무엇을 인코딩하는지 해석하기 어렵다.
- **디센탱글먼트 (Disentanglement)**: 잠재 변수 각각이 독립적인 의미 요인을 포착하도록 만드는 것은 비지도 학습의 핵심 난제이다.
- **보간 품질**: 잠재 공간이 매끄럽지 않으면 두 점 사이의 보간 결과가 비현실적이 된다 (특히 GAN에서 문제).
- **스케일**: LLM의 잠재 공간은 수만 차원에 달하며, 표현 용량과 계산 비용 간 트레이드오프가 존재한다.

## 응용 분야

| 분야 | 잠재 공간 활용 |
|------|--------------|
| 이미지 생성 | VAE/GAN/Diffusion의 잠재 코드에서 샘플링하여 새 이미지 생성 |
| 의미 검색 | 텍스트/이미지를 잠재 벡터로 인코딩, 코사인 유사도로 검색 |
| 스타일 전이 | 잠재 공간에서 콘텐츠와 스타일 벡터를 분리/재조합 |
| 약물 발견 | 분자 구조를 잠재 공간에 매핑, 보간으로 신규 후보 탐색 |
| 추천 시스템 | 사용자와 아이템을 공유 잠재 공간에 임베딩하여 유사도 기반 추천 |
| 얼굴 인식 | 시아미즈 네트워크로 얼굴을 잠재 벡터로 변환, 거리 기반 매칭 |

## 대표 레퍼런스

- [Latent space (Wikipedia)](https://en.wikipedia.org/wiki/Latent_space)
- [Generative modelling in latent space (Sander Dieleman, 2025)](https://sander.ai/2025/04/15/latents.html)
- [Improving Diffusion Models as an Alternative To GANs (NVIDIA)](https://developer.nvidia.com/blog/improving-diffusion-models-as-an-alternative-to-gans-part-2/)

## 관련 문서

- [[approximate-nearest-neighbor|Approximate Nearest Neighbor]]
- [[ai-reasoning-models|AI Reasoning Models]]
