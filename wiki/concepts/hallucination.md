---
title: Hallucination (환각)
aliases: [hallucination, 환각, LLM hallucination, AI 환각]
category: concepts
page_type: concept
tags: [hallucination, safety, alignment, trustworthiness, factuality, 2022-2026]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Hallucination (환각)

## 정의

**Hallucination(환각)**은 LLM이 사실과 다른 내용을 높은 확신을 가지고 생성하는 현상이다. 모델이 "모른다"고 말하는 대신 그럴듯하지만 틀린 정보를 만들어낸다. 2026년 현재 LLM의 가장 지속적인 신뢰성 문제로, 위키 내 56회 이상 언급될 만큼 AI 안전성 논의의 핵심 키워드다.

## 환각의 두 가지 유형

### Factuality Error (사실성 오류)

모델이 객관적으로 틀린 사실을 진술하는 경우다. 존재하지 않는 논문 인용, 잘못된 날짜, 허구의 통계 등이 해당한다.

### Faithfulness Error (충실성 오류)

주어진 소스나 프롬프트의 내용을 왜곡하거나 잘못 표현하는 경우다. 요약 작업에서 원문에 없는 내용을 추가하거나, [[rag-architecture-evolution-2026|RAG]] 파이프라인에서 검색된 문서와 다른 답변을 생성하는 것이 대표적이다.

## 파이프라인 단계별 발생 원인

환각은 LLM 개발의 여섯 단계 모두에서 발생할 수 있다.

### 1. 데이터 수집 및 전처리

웹 스케일 코퍼스에 포함된 노이즈, 편향, 모순 정보가 모델에 내재화된다. 훈련 데이터의 품질이 환각의 가장 근본적인 원인이다.

### 2. 모델 아키텍처

Transformer의 attention 메커니즘은 모든 토큰에 확률 분포를 할당하므로, 구조적으로 "확신 없음"을 표현하기 어렵다. Exposure bias(훈련 시 자기 생성 토큰 대신 정답만 봄)도 기여한다.

### 3. 사전 훈련

[[causal-language-modeling|다음 토큰 예측]] 목적 함수 자체가 문제다. OpenAI의 2025년 9월 논문이 핵심을 짚었다 -- 다음 토큰 훈련 목적과 주요 리더보드가 **보정된 불확실성보다 자신감 있는 추측을 보상**하므로, 모델은 허풍을 학습한다.

### 4. 파인튜닝 / RLHF

RLHF 단계에서 인간 평가자가 "길고 상세한 답변"을 선호하면, 모델은 불확실해도 자세하게 답하는 쪽으로 최적화된다. 이것은 [[reward-hacking|보상 해킹]]의 한 형태다.

### 5. 평가

벤치마크가 "답변 거부"를 페널티로 처리하면 모델은 모르는 것도 답하게 된다. [[truthfulqa|TruthfulQA]] 같은 전용 벤치마크가 이 문제를 측정하기 위해 설계되었다.

### 6. 추론 시점

[[temperature-sampling|temperature]], top-p 같은 샘플링 파라미터의 무작위성이 환각 확률을 높인다. 그러나 2025년 npj Digital Medicine 연구에 따르면, temperature 조정만으로는 환각률이 거의 변하지 않았다.

## 탐지 방법

### 내부 탐지 (외부 검증 불가능 시)

- **Cross-Layer Attention Probing (CLAP)**: 모델 활성화(activations)에 분류기를 훈련시켜 실시간 환각 플래그
- **MetaQA (ACM 2025)**: 동일 프롬프트의 약간의 변형(metamorphic mutations)으로 비일관성을 탐지. 폐쇄형 모델에도 적용 가능
- **[[mechanistic-interpretability-2026|기계적 해석 가능성]]**: 내부 회로 분석으로 환각 발생 뉴런을 특정하는 연구 진행 중

### 외부 탐지 (검증 소스 존재 시)

- Span-level verification: RAG 시스템에서 생성된 각 주장을 검색 문서와 대조
- Factuality-based reranking: 여러 후보 답변을 사실성 메트릭으로 재순위화
- [[bertscore|BERTScore]], [[truthfulqa|TruthfulQA]] 등 전용 평가 도구 활용

## 완화 전략

### 프롬프트 기반

2025년 다중 모델 연구에서, 구조화된 프롬프트 전략이 GPT-4o의 환각률을 **53%에서 23%로 감소**시켰다. [[chain-of-thought|CoT 프롬프팅]]은 프롬프트 민감 시나리오에서 환각을 크게 줄인다.

### RAG (검색 증강 생성)

[[rag-architecture-evolution-2026|RAG]] 기법은 적절히 구현 시 환각을 **최대 71%** 감소시킨다. 단, 검색 결과 자체의 품질과 span-level 검증이 전제되어야 한다.

### 훈련 기반

- **Calibration-aware rewards**: 과신과 과소신 모두 페널티. "모르겠다"에 대해 보상
- **타깃 파인튜닝**: 환각 집중 데이터셋으로 훈련 시 오류율 **90-96% 감소** (품질 저하 없이)
- **Best-of-N reranking**: 여러 후보를 생성한 뒤 사실성 메트릭으로 최선을 선택

### 설계 원칙

- 신뢰도 점수 노출: 사용자에게 모델의 확신 수준을 투명하게 제시
- "답변을 찾지 못했습니다" 옵션: 거부를 허용하는 시스템 설계
- [[ai-observability-patterns|관측 가능성 패턴]]과 결합한 실시간 모니터링

## 2025-2026년 현황

### 통계

- Mu-SHROOM, CCHall 벤치마크(2025): 영어 텍스트 외 **저자원 언어**와 **멀티모달 태스크**에서 환각률 현저히 높음
- 2025년 Scientific Reports 분석: 300만 건의 모바일 앱 리뷰 중 약 **1.75%**가 환각 관련 불만

### 패러다임 전환

2025년의 학계 합의는 "환각 제로"를 추구하는 것이 아니라 **보정된 불확실성(calibrated uncertainty)**을 목표로 하는 것이다. 모델이 틀릴 수 있음을 인정하고, 불확실할 때 그 사실을 정확히 전달하는 방향으로 연구가 수렴하고 있다.

## 관련 문서
- [[text-summarization]] -- 텍스트 요약 (Extractive/Abstractive)

- [[truthfulqa]] -- 환각 측정 전용 벤치마크
- [[ai-red-teaming-methodology]] -- 환각 유발 공격 포함
- [[reward-hacking]] -- RLHF 과정에서 환각을 강화하는 메커니즘
- [[rag-architecture-evolution-2026]] -- 검색 증강으로 환각 완화
- [[chain-of-thought]] -- CoT로 환각 감소
- [[temperature-sampling]] -- 샘플링 파라미터와 환각의 관계
- [[ai-observability-patterns]] -- 환각 실시간 모니터링
- [[mechanistic-interpretability-2026]] -- 환각 발생 내부 회로 분석
- [[prompt-engineering]] -- 프롬프트 전략으로 환각 완화
