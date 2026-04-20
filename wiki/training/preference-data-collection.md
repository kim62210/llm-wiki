---
title: 선호도 데이터 수집 (Preference Data Collection)
category: training
page_type: concept
tags: [training, concept, preference-data, hh-rlhf, ultrafeedback, rlhf, data-curation]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 선호도 데이터 수집 (Preference Data Collection)

## 개요

선호도 데이터는 RLHF와 [[direct-preference-optimization|DPO]] 계열 후학습의 원재료다. 동일 프롬프트에 대해 두 개 이상의 모델 응답을 인간 또는 AI가 비교하여 "어떤 응답이 더 나은가"를 라벨링한 데이터셋을 말한다. 데이터의 품질, 다양성, 규모가 정렬 성능을 직접 결정하므로, 수집 파이프라인 설계는 후학습 전체의 성패를 좌우하는 핵심 단계다.

## 주요 선호도 데이터셋

### HH-RLHF (Anthropic)

Anthropic이 공개한 Helpful and Harmless RLHF 데이터셋으로, "Training a Helpful and Harmless Assistant with RLHF" 논문의 기반 데이터다. 인간 크라우드워커가 동일 모델 패밀리에서 생성된 응답 쌍을 비교하여 유용성(helpfulness)과 무해성(harmlessness) 기준으로 선호도를 표기했다. 같은 모델 패밀리에서 생성된 응답을 비교하기 때문에 응답 쌍 간 유사도가 높은 편이며, 이는 미묘한 품질 차이를 구분하는 보상 모델 학습에 유리하다. [[extended-constitutional-ai|확장 헌법적 AI]]의 RL-CAI 단계에서 사용되는 선호도 데이터의 원형이기도 하다.

### UltraFeedback

HH-RLHF의 한계(단일 모델 패밀리, 제한된 도메인)를 극복하기 위해 설계된 대규모 선호도 데이터셋이다. 다양한 출처의 지시문(instruction)을 수집하고, 여러 LLM에서 응답을 생성한 뒤 GPT-4가 수치적 점수와 텍스트 피드백을 모두 제공하는 방식으로 구축했다. 재현 가능하고 확장 가능한 선호도 데이터 구축 파이프라인을 제시했다는 점에서 의의가 크다. AI 피드백을 활용한다는 점에서 [[rlaif-scalable-oversight|RLAIF]]의 실용적 구현 사례이기도 하다.

### 기타 주요 데이터셋

- **OpenAssistant Conversations (OASST)**: 커뮤니티 기반 대화 트리 구조, 다국어 지원
- **Nectar**: 7개 LLM의 응답을 GPT-4로 랭킹, 182K 프롬프트
- **Chatbot Arena**: 실시간 사용자 블라인드 투표 기반, Elo 랭킹 도출

## 수집 방법론

### 인간 비교 (Human Comparison)

가장 전통적인 방식으로, 크라우드워커가 두 응답을 비교하여 선호도를 표기한다.

- **장점**: 실제 인간 선호 반영, [[reward-model-training|보상 모델]]의 금본위(gold standard)
- **단점**: 비용이 높고(건당 $1+), 라벨러 간 일치도(inter-annotator agreement)가 60-80% 수준으로 노이즈 존재
- **주의점**: 라벨링 지침의 구체성이 데이터 품질을 결정하며, "유용성"과 "무해성"이 충돌하는 경우 우선순위 기준을 사전에 정의해야 한다

### AI 피드백 (AI Feedback)

GPT-4 같은 강력한 모델이 인간 대신 선호도를 평가한다. UltraFeedback이 대표적 사례다.

- **장점**: 비용 $0.01 미만/건, 대규모 확장 가능, 일관성 높음
- **단점**: 모델 고유의 체계적 편향(길이 선호, 형식 선호) 전파 위험
- **완화 전략**: [[rlaif-scalable-oversight|RLAIF]]의 교차 검증 루프, 다중 모델 앙상블, 인간 검증 샘플링

### 암묵적 피드백 (Implicit Feedback)

사용자의 재생성 요청, 편집, 이탈률 등 행동 데이터에서 선호 신호를 추출한다. Chatbot Arena의 실시간 투표가 이 범주에 가깝다. 노이즈가 많지만 실제 사용 맥락을 반영한다는 장점이 있다.

## 데이터 품질 관리

### 핵심 지표

| 지표 | 설명 | 목표 범위 |
|------|------|-----------|
| 라벨러 간 일치도 | Cohen's kappa 또는 Fleiss' kappa | 0.6 이상 |
| 프롬프트 다양성 | 도메인/난이도/길이 분포 | 균등 분포 |
| 응답 쌍 난이도 | 두 응답 간 품질 차이 | 너무 쉽지도 어렵지도 않은 중간 |
| 데이터 신선도 | 모델 버전과 데이터 생성 시점 차이 | 최소화 |

### 일반적 함정

- **위치 편향(Position Bias)**: 라벨러가 첫 번째 응답을 체계적으로 선호하는 경향. 응답 순서 무작위화로 완화
- **길이 편향(Length Bias)**: 긴 응답을 더 유용하다고 판단하는 경향. [[reward-model-training|보상 모델]]에 길이 정규화 적용
- **분포 이동(Distribution Shift)**: 선호도 데이터 생성 시점의 모델과 학습 대상 모델이 다를 때 성능 하락. 온라인 데이터 생성(on-policy sampling)으로 완화

## 규모와 비용의 트레이드오프

InstructGPT(2022)는 약 33K 비교 데이터, Llama 2(2023)는 1.4M 비교 데이터를 사용했다. 데이터 규모가 커질수록 인간 라벨링 비용이 선형으로 증가하므로, 실무에서는 소량의 고품질 인간 데이터 + 대량의 AI 생성 데이터를 혼합하는 전략이 일반적이다. 이 혼합 비율 자체가 [[data-mixing-curriculum-learning|데이터 믹싱]] 최적화의 대상이 된다.

## 데이터 포맷과 활용 경로

선호도 데이터는 수집 형태에 따라 소비할 수 있는 학습 기법이 달라진다:

- **쌍별 비교 (Pairwise)**: (x, y_w, y_l) 형태. [[direct-preference-optimization|DPO]], [[reward-model-training|보상 모델 학습]]에서 직접 사용. 가장 일반적인 형태
- **순위 (Ranking)**: (x, y_1 > y_2 > ... > y_n) 형태. Listwise 손실 함수나 PRO(Preference Ranking Optimization)에서 활용. 쌍별 비교보다 정보량이 많지만 수집 비용이 높음
- **단일 평가 (Pointwise)**: (x, y, score) 형태. KTO에서 활용 가능. 수집이 가장 쉬움
- **텍스트 피드백 포함**: 선호 라벨에 추가로 "왜 이 응답이 더 나은지" 텍스트 설명 포함. UltraFeedback이 이 방식을 채택하며, 생성형 [[reward-model-training|보상 모델]] 학습에 유용

데이터 포맷의 선택은 학습 기법과 밀접하게 연결되므로, 수집 파이프라인 설계 시 어떤 후학습 기법을 사용할지를 먼저 결정해야 한다.

## 대표 자료

- [Training a Helpful and Harmless Assistant with RLHF (Anthropic, HH-RLHF)](https://github.com/anthropics/hh-rlhf)
- [UltraFeedback: Boosting Language Models with Scaled AI Feedback](https://arxiv.org/abs/2310.01377)
- [Towards Data-Centric RLHF: Simple Metrics for Preference Dataset Comparison](https://arxiv.org/html/2409.09603v1)

## 관련 문서

- [[direct-preference-optimization]] -- 선호도 데이터를 직접 소비하는 학습 기법
- [[reward-model-training]] -- 선호도 데이터로 보상 모델을 학습하는 전통적 경로
- [[rlaif-scalable-oversight]] -- AI 피드백으로 인간 라벨링을 대체하는 접근
- [[extended-constitutional-ai]] -- 헌법 원칙 기반 합성 선호도 데이터 생성
- [[data-mixing-curriculum-learning]] -- 인간/AI 데이터 혼합 비율 최적화
