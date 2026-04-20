---
title: 나이브 베이즈 분류기 (Naive Bayes Classifier)
category: foundations
page_type: concept
tags: [naive-bayes, bayesian, classification, text-classification]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 나이브 베이즈 분류기 (Naive Bayes Classifier)

베이즈 정리(Bayes' theorem)에 조건부 독립(conditional independence) 가정을 결합한 확률적 분류 알고리즘. "나이브(naive)"한 이유는 특징 간 조건부 독립이라는 현실에서는 지켜지기 어려운 가정을 단순화 목적으로 채택하기 때문이다.

## 핵심 수식

베이즈 정리 기반:

$$P(y \mid x_1, \ldots, x_n) = \frac{P(y) \cdot P(x_1, \ldots, x_n \mid y)}{P(x_1, \ldots, x_n)}$$

**조건부 독립 가정** 적용:

$$P(x_1, \ldots, x_n \mid y) = \prod_{i=1}^{n} P(x_i \mid y)$$

최종 분류 결정 (MAP 추정):

$$\hat{y} = \arg\max_y \; P(y) \cdot \prod_{i=1}^{n} P(x_i \mid y)$$

실제 계산에서는 언더플로우(underflow) 방지를 위해 log-sum을 사용한다.

## 세 가지 변형

| 변형 | 특징 분포 가정 | 주요 용도 |
|------|-------------|-----------|
| Gaussian NB | $P(x_i \mid y) \sim \mathcal{N}(\mu, \sigma^2)$ | 연속형 특징 (키, 몸무게 등) |
| Multinomial NB | 다항 분포 (단어 빈도) | 텍스트 분류, 문서 빈도 |
| Bernoulli NB | 이진 분포 (단어 출현 여부) | 단어 존재/부재만 사용하는 텍스트 |

텍스트 분류에서는 Multinomial NB가 가장 많이 쓰이며, 단문(short text)에는 Bernoulli NB도 경쟁력이 있다.

## Laplace Smoothing (라플라스 평활화)

훈련 데이터에 등장하지 않은 단어가 테스트 시 나타나면 $P(x_i \mid y) = 0$이 되어 전체 곱이 0이 된다. 이를 방지하기 위해 모든 카운트에 $\alpha$를 더한다:

$$P(x_i \mid y) = \frac{\text{count}(x_i, y) + \alpha}{\text{count}(y) + \alpha \cdot |V|}$$

- $\alpha = 1$: Laplace smoothing (가산 평활화)
- $\alpha < 1$: Lidstone smoothing
- $|V|$: 어휘(vocabulary) 크기

## 생성 모델 vs 판별 모델 비교

| 항목 | 생성 모델 (나이브 베이즈) | 판별 모델 (로지스틱 회귀) |
|------|------------------------|------------------------|
| 학습 대상 | $P(x, y)$ = 결합 분포 | $P(y \mid x)$ = 조건부 분포 직접 학습 |
| 새 데이터 생성 | 가능 | 불가능 |
| 데이터 효율 | 소량 데이터에서 유리 | 데이터 많을수록 판별 모델이 우세 |
| 가정 위반 내성 | 조건부 독립 위반 시 성능 저하 | 가정 없음 |
| 장점 | 빠른 훈련, 명시적 확률 출력 | 대체로 더 높은 정확도 |

## 스팸 필터(Spam Filter) 사례

1. 훈련: 스팸/정상 메일에서 단어 빈도 집계
2. 사전 확률: $P(\text{spam})$, $P(\text{ham})$ 계산
3. 조건부 확률: 각 단어 $w_i$에 대해 $P(w_i \mid \text{spam})$, $P(w_i \mid \text{ham})$ 저장
4. 예측: 새 메일의 단어 목록으로 로그 확률 합산 후 더 높은 클래스 선택

Multinomial NB 기반 스팸 필터는 1990년대 말부터 생산 환경에서 사용되었으며, 나이브 가정에도 불구하고 실전에서 매우 잘 작동한다.

## 실무 적용 시 주의점

- 로그 확률 사용: `log P(y) + sum(log P(x_i | y))` 형태로 계산
- 특징 독립 가정이 강하게 위반되는 경우(예: 인접 단어 관계) 성능 제한
- 연속형 특징에 Gaussian 가정이 맞지 않으면 구간화(binning) 또는 KDE 사용 고려
- 빠른 훈련과 해석 가능성이 중요한 베이스라인으로 항상 먼저 시도

## 관련 문서
- [[em-algorithm-gmm]] -- EM 알고리즘과 가우시안 혼합 모델 (EM Algorithm & GMM)

- [[probability-statistics-for-ml]]
- [[logistic-regression]]
- [[ensemble-methods]]
