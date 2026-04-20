---
title: In-Context Learning (인컨텍스트 학습)
aliases: [in-context learning, ICL, 인컨텍스트 학습, 맥락 내 학습]
category: concepts
page_type: concept
tags: [in-context-learning, ICL, emergent-ability, transformer, meta-learning, 2020-2026]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# In-Context Learning (인컨텍스트 학습)

## 정의

**In-Context Learning (ICL)**은 LLM이 프롬프트에 제공된 시연(demonstration)으로부터 태스크를 학습하는 능력이다. 파인튜닝과 달리 **가중치 업데이트가 전혀 없으며**, 추론 시점에 컨텍스트 창 내의 정보만으로 새로운 태스크에 적응한다. [[zero-shot-learning|Zero-shot]], [[few-shot-learning|few-shot]], many-shot 프롬프팅이 모두 ICL의 하위 형태다.

## GPT-3에서의 발견 (2020)

Brown et al.의 GPT-3 논문이 ICL을 처음으로 대규모 실증했다. 175B 파라미터 모델이 프롬프트의 예시만으로 번역, 산술, 질의응답을 수행한다는 발견은 "모델 재훈련 없이 태스크를 전환할 수 있다"는 패러다임 전환을 의미했다.

## ICL vs. 파인튜닝

| 측면 | ICL | 파인튜닝 |
|---|---|---|
| 가중치 변경 | 없음 | 있음 (gradient update) |
| 지식 지속성 | 임시 (추론 종료 시 소멸) | 영구 (모델에 내재화) |
| 비용 | 추론 비용만 (컨텍스트 토큰) | 훈련 비용 (GPU 시간) |
| 유연성 | 프롬프트 변경만으로 태스크 전환 | 태스크당 별도 모델/어댑터 |
| 전문성 | 범용 수준 | 도메인 특화 가능 |
| 데이터 필요량 | 2-100개 예시 | 수백~수만 개 |

핵심 트레이드오프: ICL은 **즉각성과 유연성**, 파인튜닝은 **깊은 전문성과 영속성**.

## 내부 메커니즘

ICL이 어떻게 작동하는지는 2025-2026년 현재도 활발한 연구 주제다.

### 베이지안 추론 가설

모델이 프롬프트의 예시를 사용하여 사전 훈련에서 학습한 **잠재 개념(latent concept)**을 "찾아내는" 과정이다. 예시는 새로운 지식을 전달하는 것이 아니라, 이미 있는 지식 중 관련 있는 것을 **활성화**한다.

### 암묵적 경사 하강 가설

Dai et al. (2023)의 발견: Transformer의 attention 메커니즘이 **메타-옵티마이저**처럼 작동한다. Forward pass 동안 attention 레이어가 예시로부터 gradient descent와 유사한 업데이트를 수행하되, 실제 가중치는 변경하지 않는다.

### 세 단계 처리 과정 (ICLR 2025)

최근 연구가 ICL의 내부 처리를 세 단계로 분해했다:

1. **Input Text Encode**: 입력 텍스트를 선형 표현으로 인코딩
2. **Semantics Merge**: 인코딩된 표현을 라벨 토큰과 병합
3. **Feature Retrieval and Copy**: 유사한 표현을 검색하여 쿼리에 복사

### 위상 전이 (Phase Transition)

컨텍스트 길이 또는 예시 수가 증가하면, 모델의 내부 표현 공간이 **급격한 위상 전이**를 겪는다. 사전 훈련된 시맨틱 구조에서 프롬프트가 암시하는 구조로 재정렬되는 현상이다.

## ICL의 형태별 특성

### Zero-Shot ICL

태스크 설명만 제공. [[instruction-tuning|인스트럭션 튜닝]]된 모델에서 효과적. 모델의 사전 지식에 전적으로 의존한다.

### Few-Shot ICL

2-5개 예시 제공. 가장 일반적인 ICL 형태. 예시의 선택, 순서, 형식이 성능에 큰 영향을 미치는 **프롬프트 민감성**이 주요 과제다.

### Many-Shot ICL

50-100개 이상의 예시 제공. Google의 2024년 연구에 따르면 성능이 예시 수에 따라 계속 향상되어 50-100개에서 정점을 찍는 경우가 많다. 컨텍스트 창 한계가 실질적 제약이다.

## ICL의 한계

### 피상적 학습

Microsoft Research (2025)의 결론: ICL은 수학적으로 "학습"이 맞지만, **취약하고 피상적인 종류의 학습**이다. 태스크의 깊은 이해보다 프롬프트의 통계적 단서에 의존한다.

### 프롬프트 민감성

예시의 형식, 순서, 심지어 줄바꿈이 결과를 크게 바꿀 수 있다. 동일한 예시 집합도 배치 순서에 따라 성능이 크게 변동한다.

### 모델 크기 의존성

소형 모델은 ICL 능력이 현저히 떨어진다. 충분한 파라미터가 있어야 프롬프트에서 태스크를 추론하는 메타 능력이 발현된다.

## 2025-2026년 확장

### Vector-ICL (ICLR 2025)

연속 데이터와 LLM 임베딩 공간을 잇는 브릿지. 비지도 사전 훈련만으로도 전통적 few-shot ICL과 동등하거나 우수한 성능 (6개 태스크 중 4개).

### 멀티모달 ICL

Large Vision-Language Models (LVLMs)가 인터리브드 이미지-텍스트 데이터 훈련을 통해 **자연스럽게 멀티모달 ICL 능력을 획득**했다.

### In-Context Adaptation (ICLR 2026)

Adaptive Context Engineering (ACE): 컨텍스트를 전략적으로 재구성하여 Transformer의 적응 능력을 향상. GPT2와 MEMORYMOSAICS 아키텍처 기반으로 유의미한 개선 달성.

### 에이전트에서의 ICL

LLM 에이전트가 ICL을 활용하여 이전 에피소드의 경험으로부터 학습하는 패턴이 연구되고 있다. [[agent-memory-systems|에이전트 메모리 시스템]]과 결합하여 세션 간 지속적 개선을 달성하는 방향.

## 관련 문서
- [[prompt-engineering-survey]] -- 프롬프트 엔지니어링 종합
- [[gpt-3-paper]] -- Language Models are Few-Shot Learners (GPT-3, Brown et al., 2020)

- [[few-shot-learning]] -- ICL의 가장 대표적 형태
- [[zero-shot-learning]] -- 예시 없는 ICL
- [[chain-of-thought]] -- ICL + 추론 단계 결합
- [[context-engineering]] -- 컨텍스트 창 관리의 상위 프레임워크
- [[prompt-engineering]] -- ICL을 활용하는 프롬프트 설계
- [[mechanistic-interpretability-2026]] -- ICL 내부 메커니즘 연구
- [[representation-engineering]] -- ICL의 표현 공간 변화 연구
- [[instruction-tuning]] -- zero-shot ICL 성능의 핵심
