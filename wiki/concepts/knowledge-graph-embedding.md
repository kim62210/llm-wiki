---
title: 지식 그래프 임베딩
category: concepts
page_type: concept
tags: [knowledge-graph, embedding, TransE, RotatE, ComplEx, link-prediction]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# 지식 그래프 임베딩

지식 그래프 임베딩(Knowledge Graph Embedding, KGE)은 [[knowledge-graph]]의 엔티티(entity)와 관계(relation)를 저차원 연속 벡터 공간에 매핑하는 기법이다. 원래의 심볼릭 지식 구조를 수치 벡터로 변환함으로써 머신러닝 모델에서 직접 활용하거나 누락된 사실을 추론(링크 예측)하는 데 쓰인다.

## 핵심 개념: 트리플(Triple)

지식 그래프는 (주어, 관계, 목적어) 트리플의 집합으로 표현된다:

- (서울, 수도, 대한민국)
- (AlphaFold, 개발사, DeepMind)
- (아스피린, 치료, 두통)

임베딩의 목표는 **참인 트리플은 높은 점수, 거짓 트리플은 낮은 점수**가 나오도록 학습하는 것이다.

## 주요 임베딩 모델

```mermaid
flowchart TD
    KGE[지식 그래프 임베딩] --> Trans[이동(Translation) 계열]
    KGE --> Semantic[의미론적 계열]
    KGE --> Rotate[회전(Rotation) 계열]

    Trans --> TransE
    Trans --> TransR
    Trans --> TransH

    Semantic --> DistMult
    Semantic --> ComplEx
    Semantic --> AnalygyE

    Rotate --> RotatE
    Rotate --> QuatE
```

### TransE

가장 단순하고 영향력 있는 모델이다. 관계 $r$을 엔티티 임베딩 공간에서의 **이동 벡터(translation)**로 해석한다:

$$\mathbf{h} + \mathbf{r} \approx \mathbf{t} \quad \text{(참인 트리플일 때)}$$

- 점수 함수: $f(h, r, t) = -||\mathbf{h} + \mathbf{r} - \mathbf{t}||$
- 장점: 단순, 빠른 학습, 직관적 해석
- 단점: 1-N, N-1, N-N 관계 처리 불가, 대칭·역 관계 표현 한계

### TransR / TransH

TransE의 한계를 보완한 변형들이다:

- **TransH**: 관계별 초평면(hyperplane)에 투영해 N-N 관계 처리
- **TransR**: 엔티티와 관계를 별도 공간으로 투영 후 이동 연산 수행

### DistMult

이중선형(bilinear) 모델로 관계를 대각 행렬로 표현한다:

$$f(h, r, t) = \mathbf{h}^T \text{diag}(\mathbf{r}) \mathbf{t}$$

대칭 관계를 자연스럽게 처리하지만, 비대칭 관계 표현이 어렵다.

### ComplEx

복소수(complex number) 공간으로 임베딩을 확장해 비대칭 관계를 처리한다:

$$f(h, r, t) = \text{Re}(\mathbf{h}^T \text{diag}(\mathbf{r}) \bar{\mathbf{t}})$$

$\bar{\mathbf{t}}$는 복소 켤레(complex conjugate)다. 비대칭·역관계·대칭 관계를 모두 표현 가능하다.

### RotatE

관계를 복소수 공간에서의 **회전(rotation)**으로 모델링한다:

$$\mathbf{t} = \mathbf{h} \circ \mathbf{r}, \quad |\mathbf{r}_i| = 1$$

각 관계 벡터의 원소가 단위 복소수이므로 각도만 제어된다. 대칭, 비대칭, 역, 합성(composition) 관계 패턴을 모두 표현한다.

| 모델 | 대칭 | 비대칭 | 역관계 | 합성 |
|------|------|--------|--------|------|
| TransE | X | O | X | O |
| DistMult | O | X | X | X |
| ComplEx | O | O | O | X |
| RotatE | O | O | O | O |

## 학습 방법

### 부정 샘플링 (Negative Sampling)

참인 트리플 $(h, r, t)$에 대해 머리 또는 꼬리를 교체해 거짓 트리플을 만든다. 모델은 참 트리플의 점수가 더 높도록 마진 손실(margin loss)을 최소화한다:

$$\mathcal{L} = \sum_{(h,r,t) \in S} \sum_{(h',r,t') \in S'} \max(0,\ \gamma - f(h,r,t) + f(h',r,t'))$$

### 자기필터링 부정 샘플링 (Self-Adversarial)

RotatE에서 제안한 방법으로, 현재 모델이 높은 점수를 주는 거짓 트리플을 더 많이 샘플링해 학습 효율을 높인다.

## [[link-prediction-gnn]]과의 관계

전통적 KGE는 트리플 점수 함수만 학습하지만, GNN 기반 접근은 **그래프 구조(이웃 정보)**를 활용해 더 풍부한 표현을 학습한다:

- **RGCN**: 관계별 GNN 레이어로 엔티티 임베딩 학습
- **CompGCN**: KGE 점수 함수를 GNN 집계에 통합
- **KG-BERT**: 트리플을 텍스트로 직렬화해 BERT로 인코딩

## 실무 활용

- **추천 시스템**: 사용자-아이템-속성 지식 그래프에서 링크 예측으로 추천
- **질의 응답**: 복잡한 다중 홉 추론 (e.g., "A의 창업자의 출신 대학은?")
- **생물의학**: 단백질-질병-약물 지식 그래프에서 새로운 치료 관계 발견
- **RAG 강화**: 검색 시스템에서 의미론적 관계 기반 쿼리 확장

## [[embedding-layers]]와의 연결

KGE는 NLP의 [[embedding-layers]]와 유사하게 심볼릭 객체를 밀집 벡터로 변환한다. 차이점은 **관계(relation) 자체도 임베딩**되며, 엔티티 쌍 사이의 구조적 제약을 학습한다는 것이다.

## 관련 문서

- [[knowledge-graph]] - 지식 그래프 기본 개념과 구축 방법
- [[link-prediction-gnn]] - GNN 기반 링크 예측 방법
- [[embedding-layers]] - 일반 임베딩 레이어 원리
- [[graph-neural-networks]] - GNN 기반 KGE 확장 방법
