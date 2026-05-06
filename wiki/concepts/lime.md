---
title: LIME (Local Interpretable Model-agnostic Explanations)
category: concepts
page_type: concept
tags: [lime, xai, explainability, surrogate-model, local-explanation, model-agnostic, interpretable-ml]
sources: []
created: 2026-04-27
updated: 2026-04-27
---

# LIME (Local Interpretable Model-agnostic Explanations)

## 개요

LIME은 Marco Ribeiro 등이 2016년 KDD에서 발표한 모델 불가지론적(model-agnostic) 로컬 설명 방법론이다. 블랙박스 모델의 **특정 예측 근방에서** 해석 가능한 간단한 모델(surrogate model)로 근사하여 설명을 제공한다.

핵심 아이디어: 복잡한 모델은 전역적으로는 비선형이지만, **작은 지역(local region)에서는 선형에 가깝게 근사**할 수 있다.

> "We want to explain why a model made a specific prediction by finding an interpretable model locally around the prediction."
> - Ribeiro et al., 2016

LIME은 [[shap]]이 등장하기 전 XAI([[explainable-ai]])의 사실상 표준으로 사용되었으며, 현재도 빠른 프로토타이핑이나 SHAP이 적용 어려운 상황에서 활용된다.

## 핵심 개념: 로컬 서로게이트

LIME의 핵심 직관은 "전역 설명은 어렵지만, 특정 점 근방의 로컬 동작은 단순한 모델로 설명할 수 있다"는 것이다.

```mermaid
flowchart LR
    Input[설명할 샘플 x] --> Perturb[입력 변형\nPerturb]
    Perturb --> BlackBox[블랙박스 모델\nf 예측]
    BlackBox --> Weighted[거리 기반\n가중치 부여]
    Weighted --> Surrogate[로컬 선형 모델\ng 학습]
    Surrogate --> Explain[로컬 설명\n특성 가중치]

    Input --> Weighted
```

LIME의 파이프라인: 원본 샘플 주변을 변형하고, 블랙박스 예측값으로 레이블을 달아 거리 가중 로컬 모델을 학습한다.

## 알고리즘 상세

LIME은 다음 최적화 문제를 푼다:

$$\xi(x) = \arg\min_{g \in G} \mathcal{L}(f, g, \pi_x) + \Omega(g)$$

- $f$: 설명할 블랙박스 모델
- $g$: 서로게이트 모델 (선형 모델, 결정 트리 등)
- $G$: 해석 가능한 모델 공간
- $\pi_x(z)$: 샘플 $z$와 $x$ 사이의 근접도(proximity) 가중치
- $\mathcal{L}$: 서로게이트가 블랙박스를 얼마나 잘 모방하는지의 손실
- $\Omega(g)$: 모델 복잡도 (특성 수 제한으로 희소성 유도)

### 단계별 알고리즘

1. **샘플링**: 설명할 샘플 $x$ 주변에 변형 샘플 $z'$ 생성
   - 표 데이터: 특성값을 무작위로 대체
   - 텍스트: 단어 제거(masking)
   - 이미지: 슈퍼픽셀 단위 블라인드 처리

2. **블랙박스 예측**: 각 변형 샘플 $z'$에 대해 $f(z')$ 계산

3. **거리 가중치**: $\pi_x(z') = \exp\left(-\frac{D(x, z')^2}{\sigma^2}\right)$ (지수 커널)

4. **서로게이트 학습**: 가중 최소제곱법으로 희소 선형 모델 학습 (Lasso 또는 Ridge)

5. **설명 추출**: 학습된 선형 계수가 각 특성의 로컬 기여도

## 데이터 타입별 LIME 동작

### 표 데이터 (Tabular LIME)

```python
import lime
import lime.lime_tabular

explainer = lime.lime_tabular.LimeTabularExplainer(
    X_train.values,
    feature_names=X_train.columns.tolist(),
    class_names=['거절', '승인'],
    discretize_continuous=True  # 연속 특성을 구간으로 이산화
)

explanation = explainer.explain_instance(
    X_test.iloc[0].values,
    model.predict_proba,
    num_features=10,     # 상위 10개 특성만 표시
    num_samples=5000     # 샘플링 수 (많을수록 안정적)
)

explanation.show_in_notebook()
```

이산화(discretize_continuous=True)는 "나이 > 40" 같은 조건으로 표현하여 이해하기 쉽게 만든다.

### 텍스트 데이터 (Text LIME)

```python
import lime.lime_text

explainer = lime.lime_text.LimeTextExplainer(class_names=['부정', '긍정'])

explanation = explainer.explain_instance(
    "이 영화는 정말 훌륭하지만 너무 길다",
    classifier.predict_proba,
    num_features=6
)

# 각 단어의 기여도 출력
for word, weight in explanation.as_list():
    print(f"{word}: {weight:.4f}")
```

텍스트에서는 단어/토큰 단위로 제거(masking)하며 변형 샘플을 생성한다.

### 이미지 데이터 (Image LIME)

```python
from lime import lime_image
from skimage.segmentation import mark_boundaries

explainer = lime_image.LimeImageExplainer()

explanation = explainer.explain_instance(
    image_array,
    model.predict,
    top_labels=5,
    hide_color=0,          # 제거 슈퍼픽셀을 검은색으로
    num_samples=1000,
    segmentation_fn=None   # 기본 QuickShift 세그멘테이션
)

# 상위 클래스의 긍정/부정 기여 슈퍼픽셀 시각화
image_boundary, mask = explanation.get_image_and_mask(
    label=explanation.top_labels[0],
    positive_only=False,
    num_features=10,
    hide_rest=False
)
```

## LIME의 설계 철학: "신뢰 가능한 ML"

Ribeiro 등은 단순한 설명 도구를 넘어 **ML 시스템 신뢰성 구축**의 도구로 LIME을 설계했다.

### SP-LIME (Submodular Pick)

단일 예측 설명을 넘어 모델 전체를 대표하는 예시 집합을 선택하는 방법이다. 서브모듈러 함수 최적화를 통해 커버리지를 최대화하는 $B$개의 설명적 예시를 선택한다.

```python
# SP-LIME: 모델 전반을 이해하기 위한 대표 샘플 B개 선택
sp_explanation = explainer.explain_instance_with_data(
    X_test, model.predict_proba,
    num_features=10
)
```

## 한계점

### 1. 불안정성 (Instability)

LIME의 가장 큰 단점은 동일한 입력에서도 실행마다 다른 설명이 나올 수 있다는 것이다. 샘플링 무작위성이 결과에 큰 영향을 미친다.

```python
# 동일 입력, 다른 결과가 나올 수 있음
exp1 = explainer.explain_instance(x, model.predict_proba, num_samples=1000)
exp2 = explainer.explain_instance(x, model.predict_proba, num_samples=1000)
# exp1.as_list() != exp2.as_list()  # 가능
```

**완화 방법**: `num_samples` 증가, `random_state` 고정

### 2. "로컬" 정의의 모호성

$\sigma$ (커널 대역폭)가 "얼마나 로컬인가"를 결정하지만, 최적값이 데이터와 모델에 따라 다르며 자동 선택 방법이 없다.

### 3. 특성 상관관계 무시

독립적으로 특성을 변형하므로, 상관관계가 높은 특성들(예: 키와 몸무게)에서 비현실적인 샘플을 생성한다.

### 4. 고차원 데이터 취약성

특성 수가 많아질수록 로컬 선형 근사의 정확도가 떨어지고 필요한 샘플 수가 급증한다.

## LIME vs SHAP 상세 비교

| 항목 | LIME | [[shap]] |
|------|------|----------|
| 이론적 기반 | 로컬 선형 근사 | 게임 이론 Shapley 공리 |
| 일관성 | 보장 없음 | 공리적으로 보장 |
| 안정성 | 낮음 (샘플링 의존) | 높음 (결정론적, TreeSHAP) |
| 계산 속도 | 중간 (블랙박스 호출 ~1000-5000회) | TreeSHAP은 매우 빠름 |
| 전역 설명 | SP-LIME (제한적) | beeswarm plot (자연스러움) |
| 특성 상호작용 | 미지원 | SHAP Interaction Values |
| 이미지 설명 | 슈퍼픽셀 기반 | GradientSHAP, PartitionSHAP |
| 텍스트 설명 | 단어 단위 제거 | PartitionSHAP |
| 출력 형태 | 특성별 가중치 (조건부) | 특성별 실수값 기여도 |
| 라이브러리 성숙도 | 안정적이나 유지보수 둔화 | 활발히 개발 중 |

## 언제 LIME을 선택하는가

SHAP이 더 우수한 이론적 보장을 제공하지만, 다음 상황에서는 LIME이 적합하다:

1. **빠른 프로토타이핑**: 라이브러리 설치와 API가 단순
2. **조건부 설명**: "나이 > 40"처럼 규칙 형태의 설명이 필요할 때 (tabular discretize)
3. **임의 블랙박스**: API만 있는 외부 서비스 모델 설명
4. **텍스트 원문 설명**: 단어 단위 기여도 시각화가 직관적인 경우
5. **SHAP 계산 불가**: 특수 커스텀 모델에서 KernelSHAP도 통합이 어려운 경우

## 실무 적용 패턴

### A/B 테스트 실패 원인 분석

```python
# 특정 세그먼트에서 모델 동작 이상 감지
failed_cases = X_test[y_pred != y_true]
for idx in failed_cases.index[:5]:
    exp = explainer.explain_instance(
        X_test.loc[idx].values,
        model.predict_proba,
        num_features=5
    )
    print(f"샘플 {idx}:")
    for feature, weight in exp.as_list():
        print(f"  {feature}: {weight:+.3f}")
```

### 모델 신뢰 점검

```python
# "엉뚱한" 특성에 의존하는 모델 감지
def check_spurious_correlations(explainer, X_sample, known_spurious):
    explanations = [
        explainer.explain_instance(x, model.predict_proba, num_features=10)
        for x in X_sample.values
    ]
    spurious_weights = [
        sum(w for f, w in exp.as_list() if f in known_spurious)
        for exp in explanations
    ]
    return np.mean(np.abs(spurious_weights))
```

## 왜 중요한가

1. **최초 실용 XAI**: 2016년 LIME 발표는 모델 불가지론적 설명 가능성을 처음으로 실용화했고, 이후 [[explainable-ai]] 분야 폭발적 성장의 촉매가 되었다
2. **직관적 설명**: 조건부 형태("나이 > 40이고 소득 < 3000만원")의 설명은 비기술 이해관계자에게 전달하기 쉽다
3. **산업 표준의 선구자**: EU GDPR 설명 권리 이행을 위한 초기 솔루션으로 많이 사용됨

## 관련 문서

- [[explainable-ai]] - XAI 전체 분류 체계와 LIME의 위치
- [[shap]] - LIME의 이론적 개선판, Shapley 공리 기반 설명
- [[counterfactual-reasoning]] - "무엇이 달랐으면 다른 결과가 나왔을까" 형태의 보완적 설명
