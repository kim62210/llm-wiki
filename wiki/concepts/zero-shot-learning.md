---
title: Zero-Shot Learning (제로샷 학습)
aliases: [zero-shot learning, zero-shot prompting, 제로샷, 제로샷 학습]
category: concepts
page_type: concept
tags: [zero-shot, prompting, instruction-tuning, transfer-learning, 2021-2026]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Zero-Shot Learning (제로샷 학습)

## 정의

**Zero-Shot Learning**은 태스크에 대한 시연 예시 없이, 지시(instruction)만으로 모델이 새로운 태스크를 수행하는 능력이다. LLM 맥락에서는 프롬프트에 예시를 포함하지 않고 태스크 설명만 제공하는 **zero-shot prompting**을 의미한다. 사전 훈련과 [[instruction-tuning|인스트럭션 튜닝]]에서 축적된 지식만으로 미지의 태스크에 일반화하는 것이 핵심이다.

## 작동 원리

### 사전 훈련의 역할

대규모 코퍼스에서 [[causal-language-modeling|다음 토큰 예측]]으로 훈련된 LLM은 다양한 태스크 패턴을 암묵적으로 학습한다. "다음 문장을 요약하시오"라는 프롬프트를 보면, 훈련 데이터에서 본 유사한 패턴으로부터 요약 행위를 수행한다.

### 인스트럭션 튜닝의 결정적 역할

Wei et al. (2021)의 "Finetuned Language Models Are Zero-Shot Learners" (FLAN)가 핵심 전환점이었다. 다양한 태스크를 지시 형식으로 파인튜닝하면, 본 적 없는 태스크에서의 zero-shot 성능이 **극적으로 향상**된다. 이후 Instruction Tuning은 현대 LLM 훈련의 표준 단계가 되었다.

### Zero-Shot CoT

Kojima et al. (2022)의 발견: 프롬프트 끝에 **"Let's think step by step"**을 추가하는 것만으로 모델이 자체적으로 [[chain-of-thought|추론 체인]]을 생성한다. 예시 없이도 복잡한 추론이 가능해진 전환점.

## Few-Shot과의 비교

| 측면 | Zero-Shot | [[few-shot-learning|Few-Shot]] |
|---|---|---|
| 예시 수 | 0개 | 2-5개 |
| 컨텍스트 비용 | 최소 | 예시만큼 소모 |
| 형식 제어 | 약함 | 강함 (예시가 템플릿) |
| 성능 (비추론 모델) | 보통 | 높음 |
| 성능 (추론 모델) | 높음 | 비슷하거나 동일 |
| 준비 비용 | 없음 | 예시 선택/설계 필요 |

핵심 트레이드오프: zero-shot은 **편의성과 비용**에서 우위, few-shot은 **정밀한 형식 제어**에서 우위.

## 모델 크기와 Zero-Shot 성능

Zero-shot 능력은 모델 크기에 강하게 의존한다.

- **소형 모델 (1-7B)**: 단순 분류, 감정 분석 등 기본 태스크에서만 유효
- **중형 모델 (13-70B)**: 대부분의 NLP 태스크에서 실용적 성능
- **대형 모델 (100B+)**: 복잡한 추론, 코드 생성, 다단계 작업까지 가능

2025년 연구에서 Mistral-7B-Instruct가 10개 few-shot 예시로 달성한 F1 95%는, 파인튜닝된 모델의 F1 96.2%에 근접했다. 이는 작은 모델이라도 적절한 [[instruction-tuning|인스트럭션 튜닝]]과 소수 예시 결합이 파인튜닝 수준에 도달할 수 있음을 보여준다.

## 프롬프트 설계 전략

### 상세한 지시

Zero-shot에서 성능을 최대화하려면 프롬프트에 **구체적인 정의와 맥락**을 포함해야 한다. "분류하시오"보다 "다음 텍스트를 [긍정/부정/중립] 중 하나로 감정 분류하시오. 긍정은 제품에 대한 만족을 표현한 경우, ..."와 같이 각 라벨의 정의를 명시하면 성능이 현저히 향상된다.

### 역할 부여

"당신은 경험 많은 의학 전문가입니다"와 같은 역할 설정이 zero-shot 성능을 향상시킨다. 모델이 사전 훈련에서 학습한 해당 도메인의 지식을 더 효과적으로 활성화한다.

### 출력 형식 명시

[[structured-output|구조화된 출력]]을 원할 때, zero-shot에서는 형식을 명시적으로 기술해야 한다: "JSON 형식으로 응답하시오. 키는 'label'과 'confidence'."

## 2025-2026년 동향

### 추론 모델의 등장

[[ai-reasoning-models|추론 모델]](o1, o3, DeepSeek-R1 등)은 내부적으로 확장된 추론 과정을 수행한다. 이 모델들에서는 zero-shot이 few-shot과 거의 동일한 성능을 보이며, 명시적 CoT 프롬프팅도 불필요한 경우가 많다.

### 인스트럭션 튜닝의 고도화

2024-2025년의 인스트럭션 튜닝 발전으로 zero-shot 성능 자체가 크게 향상되었다. 많은 실무 시나리오에서 few-shot 없이도 충분한 품질을 달성할 수 있게 되었다.

### 멀티모달 Zero-Shot

텍스트뿐 아니라 [[multimodal-foundation-models|멀티모달 모델]]에서 이미지, 오디오에 대한 zero-shot 태스크 수행이 가능해졌다. CLIP(OpenAI)의 이미지 분류, Whisper의 음성 인식이 대표적이다.

## 관련 문서

- [[few-shot-learning]] -- 예시 포함 변형
- [[in-context-learning]] -- zero-shot과 few-shot을 포괄하는 상위 개념
- [[chain-of-thought]] -- Zero-Shot CoT
- [[instruction-tuning]] -- zero-shot 성능의 핵심 요소
- [[prompt-engineering]] -- zero-shot을 포함한 프롬프트 전략
- [[transfer-learning]] -- zero-shot의 이론적 기반
