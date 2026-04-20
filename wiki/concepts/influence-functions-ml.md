---
title: "영향 함수 (Influence Functions)"
category: concepts
page_type: concept
tags: [해석가능성, 데이터 영향도, 그래디언트]
sources: []
created: 2026-04-20
updated: 2026-04-20
---

# 영향 함수 (Influence Functions)

## 개요

영향 함수(Influence Functions)는 특정 훈련 데이터 포인트를 제거했을 때 모델 예측이 어떻게 변할지를, 실제로 모델을 재학습하지 않고 근사적으로 추정하는 기법이다. Koh & Liang(2017)이 ICML Best Paper로 발표했으며, 통계학의 강건 추정(robust statistics)에서 사용되던 영향 함수 개념을 딥러닝에 적용했다.

## 핵심 아이디어

모델 파라미터 $\hat{\theta}$가 훈련 데이터 전체로 학습되었을 때, 특정 포인트 $z = (x, y)$를 가중치 $\epsilon$으로 "upweight"하면 파라미터가 얼마나 달라지는지를 1차 테일러 전개로 근사한다:

$$\hat{\theta}_{\epsilon, z} - \hat{\theta} \approx -\epsilon H_{\hat{\theta}}^{-1} \nabla_\theta L(z, \hat{\theta})$$

여기서 $H_{\hat{\theta}}$는 헤시안(Hessian) 행렬이다. 훈련 포인트 $z$를 제거하는 것은 $\epsilon = -1/n$으로 upweight하는 것과 같다.

## 계산 방법

### 헤시안-벡터 곱 (HVP)

```mermaid
flowchart LR
    A[입력 z 또는 z_test] --> B[그래디언트 계산]
    B --> C[HVP: 역헤시안-벡터 곱]
    C --> D[파라미터 변화량 추정]
    D --> E[예측 변화 계산]
```

직접 헤시안 역행렬을 구하면 $O(p^2)$ 메모리와 $O(p^3)$ 연산이 필요하다($p$는 파라미터 수). 대신 켤레 기울기법(conjugate gradient)이나 LiSSA(Linear time Stochastic Second-order Algorithm)를 사용해 역헤시안-벡터 곱(inverse Hessian-vector product)을 효율적으로 근사한다.

훈련 포인트 $z$가 테스트 포인트 $z_{test}$의 손실에 미치는 영향:

$$\mathcal{I}_{up,loss}(z, z_{test}) = -\nabla_\theta L(z_{test}, \hat{\theta})^T H_{\hat{\theta}}^{-1} \nabla_\theta L(z, \hat{\theta})$$

## 주요 활용

### 1. 데이터 디버깅

특정 예측이 잘못된 경우, 그 예측에 가장 큰 영향을 준 훈련 샘플을 찾아낸다. 모델 예측 오류의 근본 원인을 데이터 수준에서 진단할 수 있다.

### 2. 유해 샘플 탐지

음수 영향도를 가진 훈련 샘플(모델 성능을 해치는 샘플)을 식별한다. 데이터 품질 감사와 중독 공격 탐지에 활용된다.

### 3. 모델 해석 및 설명

"이 예측은 왜 이렇게 나왔는가?"라는 질문에 대해 가장 영향력 있는 훈련 사례를 제시하는 방식으로 설명을 제공한다.

## 한계

### 볼록 가정 (Convexity Assumption)

영향 함수는 손실 함수가 볼록(convex)하고 헤시안이 양정치(positive definite)라는 가정에 의존한다. 딥러닝 모델은 비볼록 손실 함수를 가지므로, 이 근사의 품질이 보장되지 않는다.

### 대규모 모델에서의 근사 오류

파라미터가 수십억 개인 LLM에서는 HVP 근사 자체가 부정확해지고, 계산 비용도 상당히 높아진다. 실험적으로 소규모 모델에서는 잘 작동하지만 대규모 모델에서는 상관관계가 낮아지는 경우가 보고되었다.

## 후속 발전

### TracIn (Pruthi et al., 2020)

훈련 궤적(training trajectory)을 따라 체크포인트별로 영향도를 누적합산한다. 단일 수렴점이 아닌 최적화 경로 전체를 고려해 더 안정적인 추정을 제공한다.

$$\text{TracIn}(z, z_{test}) = \sum_{t} \eta_t \nabla L(z_{test}, \theta_t) \cdot \nabla L(z, \theta_t)$$

### DataInf (Kwon et al., 2023)

파인튜닝된 LLM에 특화된 근사 방법. LoRA 구조를 활용해 역헤시안-벡터 곱을 효율적으로 계산하여 대규모 모델에서도 실용적으로 영향도를 추정할 수 있다.

## LLM 시대의 적용 어려움

| 문제 | 설명 | 대안 |
|------|------|------|
| 비볼록 손실 | 근사 품질 저하 | TracIn의 궤적 적분 방식 |
| 파라미터 규모 | 역헤시안 계산 불가 | DataInf의 LoRA 분해 활용 |
| 비결정론성 | 샘플링 기반 추론 | 임베딩 유사도 기반 근사 |
| 재학습 비용 | 체크포인트 많아야 함 | 그래디언트 코사인 유사도 |

LLM 시대에는 영향 함수 대신 검색 증강 해석(RAG-style attribution), 어텐션 분석, 데이터 귀속(data attribution) 벤치마크 등 다양한 대안이 연구되고 있다.

## 관련 문서
- [[ggda-group-attribution]] -- 그룹 데이터 귀속 (GGDA)

- [[data-shapley-valuation]] - Shapley 값 기반 데이터 가치 평가
- [[data-centric-ai]] - 데이터 품질 중심 AI 패러다임
- [[mechanistic-interpretability-circuits]] - 모델 내부 해석 접근법
- [[shap-feature-importance]] - 특성 기여도 분석 (SHAP)
- [[data-poisoning-attacks]] - 데이터 중독 공격과 방어
