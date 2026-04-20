---
title: Few-Shot Learning (소수 예시 학습)
aliases: [few-shot learning, few-shot prompting, 퓨샷 러닝, 소수 예시 학습]
category: concepts
page_type: concept
tags: [few-shot, prompting, in-context-learning, emergent-ability, 2020-2026]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Few-Shot Learning (소수 예시 학습)

## 정의

**Few-Shot Learning**은 소수의 입력-출력 예시만으로 모델이 새로운 태스크를 수행하도록 하는 기법이다. LLM 맥락에서는 프롬프트에 2-5개의 시연(demonstration)을 포함하여 모델의 행동을 유도하는 **few-shot prompting**으로 주로 사용된다. 가중치 업데이트 없이 추론 시점에서 작동하며, [[in-context-learning|인컨텍스트 학습(ICL)]]의 가장 대표적인 형태다.

## Brown et al. (2020): GPT-3의 발견

GPT-3 논문 "Language Models are Few-Shot Learners"에서 few-shot의 위력이 처음 대규모로 입증되었다. 175B 파라미터 모델이 수 개의 예시만으로 번역, 질의응답, 산술 등 다양한 태스크를 수행했다. 이 결과는 LLM 시대의 패러다임을 정의한 순간이었다.

## Few-Shot vs. Zero-Shot vs. Many-Shot

| 방식 | 예시 수 | 장점 | 한계 |
|---|---|---|---|
| [[zero-shot-learning|Zero-shot]] | 0개 | 예시 준비 불필요 | 복잡한 태스크에서 성능 저하 |
| One-shot | 1개 | 최소 비용으로 형식 안내 | 편향된 단일 예시 위험 |
| **Few-shot** | **2-5개** | **형식 + 패턴 모두 전달** | **토큰 비용, 예시 선택 민감** |
| Many-shot | 50-100개+ | 최고 성능 | 컨텍스트 창 소모, 비용 급증 |

2024년 Google의 "Many-Shot In-Context Learning" 논문에 따르면, 모델 성능은 예시 수에 따라 **50-100개에서 정점**을 찍는 경우가 많다. 이는 "few-shot"이라는 명칭과 달리, 더 많은 예시가 도움이 될 수 있음을 시사한다.

## 작동 메커니즘

Few-shot 프롬프팅에서 모델의 가중치는 변하지 않는다. 대신:

1. **패턴 인식**: 예시들의 입출력 구조에서 태스크 규칙을 추론
2. **형식 정렬**: 출력 포맷(JSON, 분류 라벨 등)을 예시와 일치시킴
3. **암묵적 경사 하강**: Transformer attention이 메타-옵티마이저처럼 작동하여 예시에서 학습 (Dai et al., 2023)

핵심은 모델이 예시를 "암기"하는 것이 아니라, 사전 훈련에서 학습한 잠재 개념(latent concept)을 예시가 **활성화**하는 것이다.

## 예시 선택의 중요성

Few-shot의 성능은 어떤 예시를 선택하느냐에 극도로 민감하다.

### 권장 사항

- **양성 + 음성 예시** 모두 포함: "이것은 O"뿐 아니라 "이것은 X" 패턴도 보여준다
- **다양성 확보**: 동일 패턴의 반복보다 다양한 케이스를 커버
- **수확 체감**: 2-3개 이후 추가 예시의 효과는 급격히 감소
- **순서 효과**: 예시의 배치 순서가 성능에 영향. 가장 관련 높은 예시를 마지막에 배치하는 것이 일반적으로 유효

### 자동 예시 선택

수동 선택의 한계를 넘기 위해:
- **유사도 기반 검색**: 쿼리와 의미적으로 가까운 예시를 벡터 DB에서 동적 검색
- **[[chain-of-thought|Auto-CoT]]**: 클러스터링 + 샘플링으로 자동 시연 생성
- **DSPy**: 프로그래밍 방식으로 예시 최적화

## Few-Shot의 한계

### 프롬프트 불안정성 (Prompt Brittleness)

예시의 형식, 순서, 심지어 줄바꿈 위치가 결과를 크게 바꿀 수 있다. 이 불안정성이 [[blind-prompting|맹목적 프롬프팅]]의 원인 중 하나다.

### 컨텍스트 창 소모

예시가 많을수록 실제 작업에 사용 가능한 [[context-engineering|컨텍스트]] 공간이 줄어든다. [[lost-in-the-middle|Lost-in-the-Middle]] 현상으로 중간에 배치된 예시가 무시될 수도 있다.

### 도메인 특수성

고도로 전문화된 태스크(의료, 법률)에서는 few-shot만으로 부족하고, [[supervised-fine-tuning|파인튜닝]]이 필요한 경우가 많다.

## 2025-2026년 동향

### 추론 모델과의 관계

[[ai-reasoning-models|추론 모델]](o1, o3 등)이 등장하면서 few-shot의 필요성이 변화하고 있다. 모델이 자체적으로 [[chain-of-thought|CoT]] 추론을 수행하므로, 추론 시연 예시의 가치가 감소한다. 그러나 **출력 형식 제어**를 위한 few-shot은 여전히 유효하다.

### Structured Output과의 관계

[[structured-output|구조화된 출력]]이 API 수준에서 지원되면서, JSON 형식 시연이라는 few-shot의 주요 용도 중 하나가 대체되고 있다. 그러나 constrained decoding이 지원되지 않는 환경에서는 few-shot이 여전히 형식 제어의 핵심 수단이다.

## 관련 문서
- [[in-context-learning-mechanics]] -- In-Context Learning 메커니즘
- [[few-shot-image-classification]] -- 퓨샷 이미지 분류 (Few-Shot Image Classification)

- [[in-context-learning]] -- few-shot이 속한 상위 개념
- [[zero-shot-learning]] -- 예시 없는 변형
- [[chain-of-thought]] -- few-shot + 추론 단계 결합
- [[prompt-engineering]] -- few-shot을 포함한 프롬프트 기법 전체
- [[structured-output]] -- few-shot의 형식 제어 역할 대체
- [[context-engineering]] -- 예시가 컨텍스트 창을 소모하는 문제
- [[harness-engineering]] -- few-shot을 자동화하는 하네스 설계
