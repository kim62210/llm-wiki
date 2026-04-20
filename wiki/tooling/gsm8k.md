---
title: GSM8K
category: tooling
page_type: entity
tags: [tooling, entity, benchmark, evaluation, math-reasoning, gsm8k]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# GSM8K

GSM8K(Grade School Math 8K)는 OpenAI와 Surge AI가 공동 제작한 초등학교 수준 수학 문장제 벤치마크다. 2021년 "Training Verifiers to Solve Math Word Problems" 논문(arXiv:2110.14168)과 함께 공개되었으며, 언어 모델의 다단계 수학적 추론(multi-step mathematical reasoning) 능력을 평가한다. 개념적으로는 "뛰어난 중학생이면 풀 수 있는" 수준이지만, 발표 당시 최대 규모 모델조차 일관된 높은 성능을 달성하지 못하여 추론 능력의 핵심 벤치마크로 자리잡았다.

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 이름 | Grade School Math 8K (GSM8K) |
| 개발 | OpenAI + Surge AI |
| 논문 | "Training Verifiers to Solve Math Word Problems" (2021) |
| 저장소 | github.com/openai/grade-school-math |
| 문제 수 | 8,500개 (학습 7,500 + 테스트 1,319) |
| 형식 | 자연어 문장제 + 수치 정답 |
| 풀이 단계 | 2~8단계 |
| 사용 연산 | 사칙연산 (+, -, *, /) |
| 핵심 메트릭 | 정확도(exact match accuracy) |

## 데이터셋 설계

GSM8K의 핵심 설계 원칙은 "개념적으로 단순하지만 추론 단계가 필요한" 문제다.

**문제 특성**:
- 모든 문제는 일상적 상황(쇼핑, 나이, 거리 계산 등)을 배경으로 한다
- 풀이에 2~8단계의 연쇄 추론이 필요하다
- 사칙연산만 사용하며, 고급 수학 지식은 불필요하다
- 정답은 항상 양의 정수다

**다양성**: 인간 문제 출제자(human problem writers)가 언어적 다양성을 확보하도록 작성했다. 같은 유형의 문제라도 표현 방식이 다르다.

**풀이 과정 포함**: 각 문제에 단계별 풀이(chain of thought)가 정답과 함께 제공되어, 모델의 추론 과정을 학습시키거나 평가하는 데 활용할 수 있다.

## 왜 GSM8K가 어려운가

초등학교 수학이 AI에게 어려운 이유는 수학 자체가 아니라 추론 체인(reasoning chain)의 일관성 때문이다.

**오류 누적**: 다단계 추론에서 한 단계의 오류가 이후 모든 단계에 전파된다. 단계가 길어질수록 정답률이 급격히 떨어진다.

**자연어 이해**: "3배 더 많은"과 "3배인"을 구분하는 등 문제의 언어적 뉘앙스를 정확히 파악해야 한다.

**상태 추적**: 여러 변수(인원 수, 금액, 시간 등)를 동시에 추적하면서 정확한 계산을 유지해야 한다.

## 성능 추이와 포화

GSM8K는 추론 능력 발전의 바로미터 역할을 해왔다.

- **GPT-3 (2021)**: 약 20% 정확도
- **PaLM 540B (2022)**: 약 58%
- **GPT-4 (2023)**: 약 92%
- **o1 (2024)**: 약 95%
- **2025~2026 frontier 모델**: 95% 이상 달성이 일반적

95% 이상의 정확도에 도달하면서, GSM8K도 [[benchmark-saturation-goodharts-law]]에서 논의하는 포화 현상에 접어들었다. 이에 대응하여 여러 연구가 진행되었다.

## GSM8K-Platinum과 신뢰성 문제

2025년 GSM8K-Platinum 프로젝트(gradientscience.org)에서 원본 GSM8K 테스트 셋의 오류를 체계적으로 분석한 결과, 상당수 문제에서 정답 오류나 모호한 표현이 발견되었다. 이 정제된 버전에서 일부 모델의 성능이 원본 대비 크게 하락하여, 기존 점수의 일부가 데이터 결함에 의해 부풀려졌을 가능성이 제기되었다.

## 후속 벤치마크

- **GSM-Plus**: 원본 문제에 수치 변형, 조건 변경 등을 적용하여 모델의 강건성(robustness)을 테스트
- **MATH**: 경시대회 수준의 수학 문제로 난이도 대폭 상향
- **GSM8K-V**: 시각적 맥락(그래프, 도표)에서 수학 문제를 해결하는 VLM(Vision Language Model) 벤치마크
- **MathVista**: 수학 + 시각적 추론 통합 벤치마크
- **[[humanity-last-exam]]**: 수학을 포함한 다분야 극난이도 평가

## 실무 활용 가이드

**Chain-of-Thought 효과 측정**: GSM8K는 CoT 프롬프팅의 효과가 가장 극적으로 나타나는 벤치마크 중 하나다. CoT 유무에 따른 성능 차이가 30% 이상 벌어지기도 한다.

**소형 모델 변별**: frontier 모델에서는 포화되었지만, 7B~70B 급 오픈소스 모델 비교에서는 여전히 변별력이 있다.

**파인튜닝 효과 검증**: SFT나 RLHF 후 추론 능력이 유지되는지 확인하는 regression test로 활용 가능하다.

**평가 실행**: [[evaluation-harness]]에서 `lm_eval --tasks gsm8k` 명령으로 표준화된 환경에서 실행할 수 있으며, [[deepeval]]에서도 내장 지원한다.

## 관련 문서

- [[mmlu]] -- 지식 평가 벤치마크
- [[humaneval]] -- 코드 생성 벤치마크
- [[truthfulqa]] -- 진실성 벤치마크
- [[benchmark-contamination]] -- 데이터 오염 문제
- [[benchmark-saturation-goodharts-law]] -- 벤치마크 포화
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[humanity-last-exam]] -- 극난이도 벤치마크
- [[livebench]] -- 동적 벤치마크
