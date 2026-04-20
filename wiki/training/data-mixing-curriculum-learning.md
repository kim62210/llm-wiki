---
title: 데이터 믹싱과 커리큘럼 학습 (Data Mixing & Curriculum Learning)
category: training
page_type: concept
tags: [training, concept, data-mixing, curriculum-learning, doremi, pretraining, data-curation]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 데이터 믹싱과 커리큘럼 학습 (Data Mixing & Curriculum Learning)

## 개요

LLM 사전학습의 성능은 모델 크기와 학습 데이터 양뿐 아니라, 데이터 도메인 간 혼합 비율(data mixture)과 학습 순서(curriculum)에 크게 좌우된다. Wikipedia, 도서, 웹 텍스트, 코드, 학술 논문 등 이질적인 도메인을 어떤 비율로 섞을지, 학습 과정에서 순서를 어떻게 조절할지는 사전학습 효율성의 핵심 레버다. DoReMi를 비롯한 자동화 기법이 이 문제를 수동 휴리스틱에서 원칙적 최적화로 전환시켰다.

## 데이터 믹싱: 왜 중요한가

### 문제 정의

사전학습 코퍼스는 보통 수십 개 도메인으로 구성된다. 각 도메인 d_i에 가중치 w_i를 부여하여 학습 배치를 구성하는데, 이 가중치 벡터 w = (w_1, ..., w_k)가 다운스트림 성능을 결정적으로 좌우한다. 예를 들어 The Pile은 22개 도메인으로 구성되며, 기본 가중치(도메인 크기 비례)로 학습한 모델과 최적화된 가중치로 학습한 모델 사이에 유의미한 성능 차이가 존재한다.

### 수동 vs 자동 접근

- **수동 휴리스틱**: 도메인 크기에 비례하거나, 이전 실험 경험에 기반해 가중치를 설정. GPT-3, LLaMA 등 초기 모델이 이 방식을 사용했다.
- **자동 최적화**: DoReMi, Online Data Mixing, Chameleon 등의 기법이 가중치 결정을 자동화한다.

## DoReMi: 도메인 재가중 최적화

### 핵심 메커니즘

DoReMi(Domain Reweighting with Minimax Optimization)는 NeurIPS 2023에서 발표된 기법으로, 소형 프록시 모델을 사용해 대형 모델의 최적 도메인 가중치를 결정한다.

```
단계 1: 소형 참조 모델 학습 (기본 가중치)
단계 2: 소형 프록시 모델을 Group DRO로 학습
        - 모든 도메인에서 참조 모델 대비 초과 손실을 최소화하는 가중치 탐색
        - 최악 도메인 성능을 끌어올리는 minimax 최적화
단계 3: 프록시 모델이 산출한 가중치로 대형 모델 학습
```

### 주요 결과

- 280M 프록시 모델로 8B 모델(30배 큰 모델)의 최적 가중치를 결정
- The Pile 기본 가중치 대비 평균 few-shot 정확도 6.5%p 향상
- 기준 성능에 도달하는 학습 스텝이 2.6배 감소
- 특정 도메인의 가중치를 낮추더라도 해당 도메인의 퍼플렉시티가 오히려 개선되는 현상 확인 -- 도메인 간 전이 학습 효과를 시사

### 의의

DoReMi의 핵심 통찰은 "프록시 모델의 최적 가중치가 대형 모델에도 전이된다"는 것이다. 이는 소형 모델에서 저비용으로 실험한 결과를 대형 모델 학습에 직접 적용할 수 있다는 뜻이며, [[data-decontamination|데이터 오염 방지]]와 함께 사전학습 데이터 관리의 양대 축을 형성한다.

## 커리큘럼 학습: 순서가 중요하다

### 개념

커리큘럼 학습은 인간의 교육 과정에서 영감을 받아, 쉬운 예제에서 어려운 예제로 점진적으로 학습 데이터를 제시하는 전략이다. LLM 맥락에서는 도메인 가중치를 학습 과정에 따라 동적으로 조절하는 것으로 확장된다.

### LLM에서의 적용

- **정적 믹싱**: DoReMi처럼 학습 전체에 걸쳐 고정된 가중치 사용
- **동적 커리큘럼**: 학습 단계에 따라 가중치를 변경. 초기에는 다양한 웹 텍스트로 기초 언어 능력을 쌓고, 후반에는 고품질 도서/학술 데이터 비중을 높이는 패턴
- **데이터 선별 커리큘럼**: 학습 진행에 따라 쉬운 데이터를 제거하고 어려운(높은 손실) 데이터를 집중 학습

### 효과와 한계

커리큘럼 학습은 동일 계산 예산에서 최종 성능을 개선하거나, 목표 성능에 더 빨리 도달하게 한다. 다만 "쉬움"과 "어려움"의 정의가 과제에 따라 달라지며, 잘못 설계된 커리큘럼은 오히려 성능을 하락시킬 수 있다. [[evaluation-during-training|학습 중 평가]]를 통해 커리큘럼의 효과를 실시간으로 모니터링하는 것이 필수적이다.

## 실무 고려사항

### 데이터 품질과 믹싱의 상호작용

도메인 가중치 최적화는 데이터 품질 관리와 결합해야 효과가 극대화된다. 저품질 도메인의 가중치를 높이면 오히려 성능이 하락하므로, 믹싱 최적화 전에 도메인별 품질 필터링이 선행되어야 한다.

### [[preference-data-collection|선호도 데이터]]와의 연결

후학습 단계에서도 데이터 믹싱 원리가 적용된다. 인간 라벨 데이터와 AI 생성 데이터의 혼합 비율, 도메인별 선호도 데이터의 분포 조절이 정렬 품질에 직접 영향을 미친다.

### 재현성 문제

데이터 믹싱 결정은 모델 성능에 큰 영향을 미치지만, 많은 모델 제공자가 정확한 믹싱 비율을 공개하지 않아 재현성이 떨어진다. DoReMi 같은 체계적 방법론은 이 투명성 문제를 부분적으로 해결한다.

## 대표 자료

- [DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)](https://arxiv.org/abs/2305.10429)
- [Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics (2026)](https://arxiv.org/html/2601.21698)
- [Chameleon: A Flexible Data-mixing Framework for Language Model Pretraining and Finetuning (2025)](https://arxiv.org/html/2505.24844)

## 관련 문서
- [[curriculum-learning-advanced]] -- 커리큘럼 학습 심화 (자기 학습 & 자동 난이도 조절)

- [[data-decontamination]] -- 학습 데이터에서 벤치마크 누출을 방지하는 또 다른 데이터 관리 축
- [[evaluation-during-training]] -- 믹싱/커리큘럼 효과를 실시간으로 측정하는 평가 체계
- [[preference-data-collection]] -- 후학습 단계의 데이터 혼합 최적화
- [[rlvr]] -- 검증 가능한 보상 기반 학습에서 도메인별 학습 커리큘럼 설계
- [[grpo]] -- 학습 안정성에 데이터 구성이 미치는 영향
