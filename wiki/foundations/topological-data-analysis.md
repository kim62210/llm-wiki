---
title: 위상 데이터 분석 (TDA)
category: foundations
page_type: concept
tags: [위상수학, TDA, 지속호몰로지, 마퍼, 표현학습, 데이터분석]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 위상 데이터 분석 (TDA)

## 개요

위상 데이터 분석(Topological Data Analysis, TDA)은 위상수학(topology)의 도구를 사용하여 데이터의 형태(shape)와 구조를 분석하는 분야다. 데이터를 점 구름(point cloud)으로 보고, 스케일에 따라 어떤 위상적 구조(연결성, 구멍, 공동 등)가 나타나고 사라지는지를 추적한다.

핵심 통찰: **데이터의 형태가 데이터에 대한 정보를 담고 있다.** 좌표나 거리의 세부 수치보다 연결성, 구멍, 루프 같은 구조적 특성이 데이터의 본질을 더 잘 나타낼 수 있다.

머신러닝에서 TDA는 특징 추출, 신경망의 표현 공간 분석, 데이터 품질 평가 등에 적용된다.

## 위상수학 기초 개념

### 단체 복합체 (Simplicial Complex)

- **0-단체(0-simplex)**: 점 (꼭짓점)
- **1-단체(1-simplex)**: 선분 (에지)
- **2-단체(2-simplex)**: 삼각형 (면)
- **$k$-단체($k$-simplex)**: $k+1$개 꼭짓점으로 이루어진 $k$차원 볼록 집합

단체 복합체는 이들의 모음으로, 닫힌 조건(face closure property)을 만족해야 한다.

### 호몰로지 (Homology)

위상 공간의 "구멍"을 대수적으로 분류하는 도구:

- $H_0$: 연결 성분의 수
- $H_1$: 1차원 구멍 (루프)의 수
- $H_2$: 2차원 공동(void)의 수
- $H_k$: $k$차원 구멍의 수

**베티 수(Betti number)** $\beta_k = \text{rank}(H_k)$는 각 차원의 독립적 구멍 수를 센다.

## 지속 호몰로지 (Persistent Homology)

### 기본 원리

점 구름에서 스케일(반경) $\epsilon$을 점차 증가시키며 Vietoris-Rips 복합체(또는 Cech 복합체)를 구성한다:

- $\epsilon$이 작을 때: 점들이 분리된 상태
- $\epsilon$이 커질수록: 이웃 점들이 연결되어 구조가 형성

호몰로지 군의 생성자(generator)가 특정 스케일 $b$에서 **탄생(birth)**하고 다른 스케일 $d$에서 **소멸(death)**한다.

### 지속도 쌍 (Persistence Pair)

각 위상 특성은 $(b, d)$ 쌍으로 표현된다:
- $b$ (birth): 특성이 나타난 스케일
- $d$ (death): 특성이 사라진 스케일
- $d - b$ (persistence): 특성의 "수명"

수명이 긴 특성 = 진짜 구조적 특성
수명이 짧은 특성 = 노이즈

```mermaid
flowchart LR
    A[점 구름 데이터] --> B[스케일 ε 증가]
    B --> C[Vietoris-Rips\n복합체 구성]
    C --> D[호몰로지 계산\nH0, H1, H2...]
    D --> E[지속도 쌍 birth-death 추출]
    E --> F[지속 다이어그램\nPersistence Diagram]
    F --> G[지속 바코드\nBarcode]
    G --> H[위상적 특징 벡터화]
    H --> I[ML 파이프라인 입력]
```

TDA의 전체 파이프라인: 데이터 -> 위상 특성 추출 -> 머신러닝 입력.

### 지속 다이어그램 (Persistence Diagram)

각 위상 특성을 평면의 점 $(b, d)$으로 표현한 집합. 대각선($b = d$) 위의 점은 수명이 없는 노이즈, 대각선에서 멀리 떨어진 점이 유의미한 구조.

### 지속 바코드 (Persistence Barcode)

각 위상 특성을 수평선 구간 $[b, d]$으로 표현. 긴 구간이 강한 구조적 신호.

### 병목 거리 (Bottleneck Distance)

두 지속 다이어그램 사이의 거리. TDA 특성의 안정성(stability) 정리:

$$d_B(D(X), D(Y)) \leq \|X - Y\|_\infty$$

입력의 작은 변화가 지속 다이어그램의 작은 변화를 낳는다. **TDA 특성은 노이즈에 강건(robust)**하다.

## 마퍼 알고리즘 (Mapper Algorithm)

Singh, Mémoli, Carlsson (2007)이 제안한 고차원 데이터 시각화·요약 도구.

### 알고리즘 단계

1. **필터 함수(filter function)** $f: X \to \mathbb{R}$ 선택 (예: PCA 첫 성분, 밀도 추정값)
2. $f$의 치역을 겹치는 구간(bin) $\{U_i\}$로 분할
3. 각 구간 $f^{-1}(U_i)$에 속하는 점 집합에 클러스터링 적용
4. 클러스터를 노드, 공유 점이 있는 클러스터를 에지로 연결한 **마퍼 그래프** 생성

### 결과 해석

마퍼 그래프는 데이터 공간의 "골격(skeleton)"을 보여준다. 루프는 $H_1$ 구조, 가지는 분기, 밀집 영역은 클러스터를 나타낸다.

### 실용 활용

- 유방암 데이터: 특정 환자 그룹의 서브타입 발견
- 당뇨병 데이터: c-Peptide 음성 환자 하위 그룹
- NBA 선수 데이터: 포지션 분류의 새로운 관점

## ML과의 결합

### 위상적 손실 (Topological Loss)

신경망 학습 시 원하는 위상 구조를 유지하도록 손실에 TDA 항 추가:

$$L_\text{total} = L_\text{task} + \lambda \cdot L_\text{topo}$$

$L_\text{topo}$는 지속 다이어그램의 목표 구조와 현재 구조의 거리로 정의.

### 신경망 표현 분석

- **레이어별 위상**: 각 레이어의 활성화에 TDA를 적용하여 표현 공간의 위상 변화 추적
- **학습 과정 모니터링**: 에포크별 지속 다이어그램 변화로 학습 역학 이해
- **일반화 예측**: 테스트셋의 위상 구조가 훈련셋과 다르면 일반화 실패 예측

### 그래프 분류

분자, 소셜 네트워크 등 그래프 데이터에서 지속 호몰로지로 그래프 특성 추출:

$$\phi(G) = [\beta_0(G), \beta_1(G), \text{persistence diagram of } G]$$

GNN과 결합하여 보완적 특성 제공.

### 데이터 증강 품질 평가

생성 모델(GAN, 확산 모델)의 생성 품질을 평가할 때, 실제 데이터와 생성 데이터의 위상 구조 비교로 다양성(diversity)과 충실도(fidelity)를 동시 평가.

## 벡터화 방법

지속 다이어그램은 집합(set)이므로 표준 ML에 바로 사용하기 어렵다. 벡터화 방법:

### 1. 지속 랜드스케이프 (Persistence Landscape)

지속 다이어그램을 함수의 배열로 변환. $\mathbb{L}^2$ 공간에서 정의되어 평균·분산 등 통계 계산 가능.

### 2. 지속 이미지 (Persistence Image)

지속 다이어그램 위에 가우시안 커널을 올려 2D 이미지로 변환. CNN으로 처리 가능.

### 3. Betti 곡선 (Betti Curve)

스케일 $\epsilon$에 따른 $\beta_k(\epsilon)$ 값의 함수. 단순하지만 정보 손실이 크다.

### 4. 커널 방법

지속 다이어그램 사이의 커널 함수 정의 후 SVM/GP에 적용:

$$k(D_1, D_2) = e^{-d_B(D_1, D_2)^2 / (2\sigma^2)}$$

## 소프트웨어 도구

| 라이브러리 | 언어 | 주요 기능 |
|-----------|------|-----------|
| Ripser | C++/Python | 빠른 지속 호몰로지 계산 |
| Giotto-TDA | Python | scikit-learn 호환 TDA 파이프라인 |
| GUDHI | C++/Python | 포괄적 TDA 도구 모음 |
| KeplerMapper | Python | 마퍼 알고리즘 구현 |
| Scikit-TDA | Python | 여러 TDA 도구 통합 |

## 한계와 도전

- **계산 복잡도**: Vietoris-Rips 복합체 구성이 $O(n^2)$ 이상 (근사 방법 사용)
- **파라미터 선택**: 마퍼의 필터 함수, 커버 간격 등 하이퍼파라미터가 결과에 크게 영향
- **해석 어려움**: 지속 다이어그램에서 실제 데이터 의미로의 번역이 비직관적
- **고차원 확장**: 3차원 이상의 호몰로지 계산은 극히 느림

## 관련 문서

- [[representation-learning-theory]] - 표현 학습: TDA가 표현의 기하 구조를 분석
- [[kernel-methods]] - 커널 방법: TDA 특성의 커널화
- [[bias-variance-tradeoff]] - 지속 수명과 노이즈 강건성의 관계
- [[bayesian-inference]] - 위상적 베이지안 방법론과의 연결
