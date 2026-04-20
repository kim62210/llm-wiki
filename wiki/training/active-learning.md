---
title: 능동 학습 (Active Learning)
category: training
page_type: concept
tags: [active-learning, uncertainty-sampling, query-strategy, label-efficiency, human-in-the-loop]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---

# 능동 학습 (Active Learning)

## 개요

능동 학습(Active Learning)은 모델이 학습에 가장 유용한 데이터를 스스로 선택하여 라벨링을 요청하는 학습 패러다임이다. 전체 데이터를 무작위로 라벨링하는 대신, 모델이 가장 불확실하거나 정보량이 높은 샘플을 우선적으로 쿼리함으로써 동일한 라벨 예산으로 더 높은 성능을 달성한다. 라벨링 비용이 높은 의료 영상, 법률 문서, 과학 데이터 분류 등에서 특히 효과적이다.

## 핵심 사이클

능동 학습은 반복적인 쿼리-학습 사이클로 진행된다:

1. **초기 학습**: 소규모 라벨 데이터셋으로 초기 모델 학습
2. **쿼리 전략 적용**: 비라벨 데이터 풀에서 쿼리 전략에 따라 가장 유용한 샘플 선택
3. **오라클 라벨링**: 선택된 샘플에 대해 전문가(오라클)가 라벨 부여
4. **모델 재학습**: 새로 라벨링된 데이터를 학습 데이터에 추가하고 모델 갱신
5. **종료 조건 확인**: 성능 목표 또는 예산 소진 시 종료, 아니면 2단계로 복귀

### 시나리오 분류

| 시나리오 | 비라벨 데이터 접근 | 특징 |
|---------|-----------------|------|
| **Pool-based** | 전체 비라벨 풀 접근 가능 | 가장 일반적, 풀에서 최적 샘플 선택 |
| **Stream-based** | 한 번에 하나씩 도착 | 각 샘플에 대해 쿼리 여부 즉시 결정 |
| **Membership synthesis** | 모델이 쿼리 샘플 자체를 생성 | 입력 공간에서 직접 유용한 샘플 합성 |

## 쿼리 전략 (Query Strategies)

### 1. 불확실성 샘플링 (Uncertainty Sampling)

모델이 가장 불확실해하는 샘플을 선택한다. 가장 직관적이고 널리 사용되는 전략이다.

| 기준 | 측정 방법 | 수식 개요 |
|------|---------|---------|
| **최소 확신도 (Least Confidence)** | 최고 확률 클래스의 확률이 가장 낮은 샘플 | 1 - max P(y\|x) |
| **마진 (Margin)** | 상위 2개 클래스 확률 차이가 가장 작은 샘플 | P(y1\|x) - P(y2\|x) |
| **엔트로피 (Entropy)** | 예측 분포의 엔트로피가 가장 높은 샘플 | -SUM P(y\|x) log P(y\|x) |

불확실성 유형에 따라 접근이 달라진다:
- **인식론적 불확실성(Epistemic)**: 데이터 부족으로 인한 불확실성 -- 라벨링으로 줄일 수 있음
- **고유 불확실성(Aleatoric)**: 데이터 자체의 노이즈로 인한 불확실성 -- 라벨링으로 줄일 수 없음

이상적인 능동 학습은 인식론적 불확실성이 높은 샘플을 우선 쿼리해야 한다.

### 2. 다양성 샘플링 (Diversity Sampling)

불확실성만 추구하면 결정 경계 근처의 유사한 샘플들만 반복 선택될 수 있다. 다양성 샘플링은 선택된 배치가 입력 공간을 고르게 커버하도록 보장한다.

- **코어셋 (Core-set)**: 선택된 샘플이 전체 데이터의 기하학적 커버리지를 최대화
- **클러스터 기반**: K-means 등으로 클러스터링 후 각 클러스터에서 대표 샘플 선택
- **배치 모드**: 한 번에 여러 샘플을 선택할 때 상호 다양성 보장

### 3. 기대 모델 변화 (Expected Model Change)

쿼리된 샘플이 모델에 가장 큰 변화(그래디언트 크기 등)를 야기할 것으로 예상되는 샘플을 선택한다.

- **EGL (Expected Gradient Length)**: 예상 그래디언트 크기가 가장 큰 샘플 선택
- **BALD (Bayesian Active Learning by Disagreement)**: 베이지안 예측의 불일치 정도 기반

### 4. 하이브리드 전략

실전에서는 불확실성과 다양성을 결합한 하이브리드 전략이 가장 효과적이다.

- **BADGE**: 그래디언트 임베딩 공간에서 불확실성과 다양성을 동시에 포착
- **가중 결합**: alpha * uncertainty_score + (1-alpha) * diversity_score

## 딥러닝에서의 능동 학습

전통적 불확실성 샘플링은 딥러닝에서 추가적인 과제를 제시한다:

### 불확실성 추정의 어려움

일반적인 [[dropout|드롭아웃]] 기반 신경망의 softmax 확률은 **과신(overconfident)**하는 경향이 있어 불확실성 추정이 부정확하다.

**대응 방법**:
- **MC Dropout**: 추론 시에도 드롭아웃을 활성화하여 여러 번 예측, 분산으로 불확실성 추정
- **딥 앙상블**: 여러 모델의 예측 불일치로 불확실성 측정
- **베이지안 신경망**: 가중치의 사후 분포로부터 직접 불확실성 도출

### 배치 모드의 중요성

딥러닝은 학습 비용이 높으므로, 한 번에 여러 샘플을 선택하는 배치 모드 능동 학습이 필수적이다. 배치 내 샘플들의 중복성을 최소화하는 것이 핵심이다.

## LLM과 능동 학습

LLM의 [[instruction-tuning|지시 튜닝]]과 [[rlhf-pipeline|RLHF]]에서 능동 학습 원리가 적용된다:

| 적용 영역 | 능동 학습 활용 | 효과 |
|----------|-------------|------|
| **지시 데이터 선별** | 고품질/다양한 지시 데이터 우선 선택 | [[data-mixing-curriculum-learning\|데이터 큐레이션]] 효율화 |
| **선호 데이터 수집** | 모델이 불확실한 출력 쌍에 대해 인간 평가 요청 | RLHF 라벨링 비용 절감 |
| **평가 데이터 구축** | 모델 약점을 드러내는 평가 사례 능동 탐색 | [[error-analysis-for-evals\|효과적 평가]] 구축 |

## 성능 효과

능동 학습의 핵심 이점은 **라벨 효율성**이다:

- 일반적으로 전체 데이터의 20-30% 라벨링만으로 전체 라벨 사용 시의 90-95% 성능 달성
- 의료 영상 분류에서 라벨링 비용 50-70% 절감 보고
- 최근 벤치마크 연구에서 불확실성 샘플링이 표 형식 데이터셋에서 일관되게 우위를 보임

## 관련 문서

- [[instruction-tuning]] -- LLM 지시 데이터 능동 선별
- [[rlhf-pipeline]] -- 선호 데이터의 능동적 수집
- [[data-mixing-curriculum-learning]] -- 학습 데이터 구성 전략
- [[human-in-the-loop-patterns]] -- 오라클로서의 인간 참여 패턴
- [[error-analysis-for-evals]] -- 평가 데이터의 능동적 구축

## 참고 자료

- [Active Learning Literature Survey - Burr Settles (University of Wisconsin)](https://burrsettles.com/pub/settles.activelearning.pdf)
- [Learning with not Enough Data Part 2: Active Learning (Lil'Log)](https://lilianweng.github.io/posts/2022-02-20-active-learning/)
- [An Expanded Benchmark that Rediscovers the Edge of Uncertainty Sampling for Active Learning (arXiv)](https://arxiv.org/html/2306.08954v3)
