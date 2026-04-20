---
title: 차원 축소 시각화 (t-SNE & UMAP)
category: foundations
page_type: concept
tags: [tsne, umap, dimensionality-reduction, visualization]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 차원 축소 시각화 (t-SNE & UMAP)

고차원 데이터를 2차원 또는 3차원으로 압축하여 시각화하는 비선형 차원 축소 기법. 임베딩 공간의 클러스터 구조를 직관적으로 파악하는 데 사용된다.

## 처리 파이프라인

```mermaid
flowchart LR
    HD[고차원 데이터\n예: 768-dim 임베딩] --> SIM[유사도 계산\n고차원 거리 → 확률]
    SIM --> OPT[저차원 배치 최적화\n2D/3D 좌표 학습]
    OPT --> VIS[시각화\n클러스터 패턴 확인]
```

## t-SNE (t-distributed Stochastic Neighbor Embedding)

### 핵심 원리

1. **고차원**: 각 점 쌍의 유사도를 가우시안 분포 기반 확률로 변환
   $$p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$$

2. **저차원**: **Student-t 분포**(자유도 1 = Cauchy 분포)를 사용
   $$q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l}(1 + \|y_k - y_l\|^2)^{-1}}$$
   Student-t 분포는 가우시안보다 꼬리(tail)가 두꺼워 먼 점들의 군집 간 반발력을 증폭시킨다.

3. **최적화**: KL 발산 최소화
   $$\mathcal{L} = \sum_i KL(P_i \| Q_i) = \sum_{i,j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$

### Perplexity 파라미터

각 점의 $\sigma_i$를 결정하는 핵심 하이퍼파라미터. "효과적인 이웃 수"를 의미한다.

- 권장 범위: 5 ~ 50, 일반적으로 30
- 작으면: 너무 세밀한 클러스터, 전체 구조 손실
- 크면: 지역 구조 손실, 큰 클러스터만 보임
- 데이터 크기가 커지면 perplexity도 함께 키우는 것이 좋음

## UMAP (Uniform Manifold Approximation and Projection)

### 핵심 원리

리만 기하학(Riemannian geometry)과 퍼지 위상(fuzzy topology)을 기반으로 한다. 데이터가 저차원 다양체(manifold) 위에 균등하게 분포한다고 가정한다.

1. **고차원**: 각 점에서 지역 거리 메트릭을 추정하고 k-NN 그래프 구성
   $$v_{i|j} = \exp\left(-\frac{d(x_i, x_j) - \rho_i}{\sigma_i}\right)$$
   ($\rho_i$: 가장 가까운 이웃까지의 거리 - 지역 연결성 보장)

2. **저차원**: 유사한 퍼지 그래프 구조를 최소화
   $$\mathcal{L} = \sum_{(i,j) \in E} w_{ij} \log \frac{w_{ij}}{q_{ij}} + (1 - w_{ij}) \log \frac{1-w_{ij}}{1-q_{ij}}$$

## t-SNE vs UMAP 비교

| 항목 | t-SNE | UMAP |
|------|-------|------|
| 속도 | 느림 ($O(n \log n)$ with BH) | 빠름 (대용량 처리 가능) |
| 전역 구조 보존 | 취약 (클러스터 간 거리 무의미) | 상대적으로 보존 |
| 지역 구조 보존 | 우수 | 우수 |
| 재현성 | 낮음 (실행마다 다름) | 낮음, 단 `random_state` 고정 시 재현 가능 |
| 확장성 | 수만~수십만 한계 | 수백만 데이터 처리 가능 |
| 변환 일반화 | 새 데이터 변환 불가 | `transform()` 가능 |
| 이론적 기반 | 확률론적 | 위상수학(리만 기하) |
| 하이퍼파라미터 | perplexity, n_iter | n_neighbors, min_dist |

## 임베딩 시각화 활용

- **LLM 토큰 임베딩**: 의미 군집 확인 (품사, 주제별 클러스터)
- **분류 모델 latent space**: 클래스 분리 가능성 사전 진단
- **이상 탐지**: 주요 군집 외 고립점 식별
- **파인튜닝 전후 비교**: 임베딩 공간 변화 시각화

## 주요 주의사항

- t-SNE/UMAP의 **클러스터 간 거리는 해석 불가** - 클러스터 내부 구조에만 집중
- 같은 데이터도 하이퍼파라미터에 따라 전혀 다른 그림이 나올 수 있음
- 분류 목적으로 거리를 정량화하려면 코사인 유사도를 원공간에서 직접 계산
- 고차원 정보 손실은 불가피 - 시각화는 어디까지나 탐색 도구

## 관련 문서

- [[pca]]
- [[embedding-layers]]
- [[self-supervised-learning]]
