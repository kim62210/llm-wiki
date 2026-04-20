---
title: MMLU
category: tooling
page_type: entity
tags: [tooling, entity, benchmark, evaluation, mmlu, multitask, knowledge]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# MMLU

MMLU(Massive Multitask Language Understanding)는 대규모 언어 모델의 광범위한 지식과 문제 해결 능력을 평가하기 위한 다지선다형 벤치마크다. 2020년 9월 Dan Hendrycks et al.이 발표했으며(arXiv:2009.03300), STEM, 인문학, 사회과학, 법학 등 57개 학문 분야에 걸쳐 15,908개 문제를 포함한다. 2024년 7월 기준 1억 건 이상 다운로드되며 LLM 능력 비교의 대표 벤치마크로 자리잡았다.

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 이름 | Massive Multitask Language Understanding (MMLU) |
| 저자 | Dan Hendrycks, Collin Burns, Steven Basart et al. |
| 발표 | 2020년 9월 (arXiv:2009.03300) |
| 데이터셋 | Hugging Face: cais/mmlu |
| 문제 수 | 15,908문제 (test 14,042 / dev 285 / validation 1,531 / auxiliary 99,842) |
| 분야 | 57개 과목 |
| 형식 | 4지선다 (A/B/C/D) |
| 평가 방식 | 정확도(accuracy) |
| 라이선스 | MIT |

## 설계 의도

MMLU는 기존 벤치마크(GLUE, SuperGLUE)가 모델 발전 속도를 따라가지 못하는 상황에서 탄생했다. 핵심 설계 원칙은 세 가지다.

**다양성**: 초등 수학부터 대학원 수준 법학, 의학, 물리학까지 57개 과목을 포함하여 단일 도메인 편향을 방지한다.

**난이도**: 전문가 수준의 지식을 요구하는 문제를 포함한다. 단순 패턴 매칭이 아닌 실제 이해와 추론이 필요하다.

**멀티태스크**: 하나의 벤치마크로 모델의 범용 지식 수준을 빠르게 파악할 수 있도록 설계되었다.

## 57개 과목 구성

MMLU는 대략 네 개 대분류로 나뉜다.

- **STEM**: 수학, 물리, 화학, 컴퓨터 과학, 공학 등
- **인문학**: 역사, 철학, 법학 등
- **사회과학**: 정치학, 경제학, 심리학, 사회학 등
- **기타**: 영양학, 종교, 전문 자격시험(CPA, 의사면허 등) 분야

각 과목에는 few-shot 예시용 dev 셋(5문제)과 evaluation용 test 셋이 별도로 존재한다.

## MMLU의 포화와 신뢰성 문제

2024년 중반 이후 주요 LLM들이 MMLU에서 88% 이상의 정확도를 기록하면서, 모델 간 유의미한 차별화가 어려워졌다.

**점수 수렴**: Claude 3.5 Sonnet, GPT-4o, Llama 3.1 405B 모두 88% 수준에 수렴하여, MMLU 점수만으로 모델 우열을 판단하기 어려운 상황이 되었다. 이는 [[benchmark-saturation-goodharts-law]]에서 논의하는 전형적 포화 현상이다.

**오류 문제**: 2024년 연구에서 MMLU 문제의 약 6.5%에 정답 오류(ground-truth error)가 있다는 것이 밝혀졌다. 이는 최상위 모델들의 정확도 차이(1~2%)보다 큰 규모여서, 순위의 신뢰성을 심각하게 훼손한다.

**데이터 오염**: 주요 모델의 학습 데이터에 MMLU 문제가 포함되었을 가능성이 지속적으로 제기되며, [[benchmark-contamination]] 문제를 대표하는 사례가 되었다.

## 후속 벤치마크

MMLU의 한계를 인식하고 여러 후속 벤치마크가 등장했다.

- **MMLU-Pro** (NeurIPS 2024): 10지선다로 확대하고 추론 중심 문제 비율을 높여 난이도와 변별력을 강화. Chain-of-Thought 프롬프팅 사용 시 성능이 더 크게 향상되어, 진정한 추론 능력을 측정한다
- **GPQA**: 대학원 수준 과학 문제로 전문가도 어려워하는 난이도
- **[[humanity-last-exam]]**: 인류 최후의 시험이라는 이름 그대로, 기존 벤치마크 포화를 극복하기 위한 극난이도 평가
- **[[livebench]]**: 동적 업데이트로 데이터 오염을 원천 차단

## 실무 활용 가이드

**현재 시점(2026년)에서의 활용**: MMLU 점수는 여전히 모델 카드에 빠지지 않는 기본 지표이나, 단독으로 모델 선택의 근거로 삼기는 어렵다. 최소한 [[humaneval]](코드), [[gsm8k]](수학), [[truthfulqa]](진실성) 등 영역 특화 벤치마크와 함께 봐야 한다.

**Few-shot 설정 표준화**: 5-shot이 표준이지만, 0-shot이나 chain-of-thought 프롬프팅으로 평가하는 경우도 있다. 비교 시 반드시 동일한 shot 수와 프롬프트 형식을 사용해야 한다.

**평가 실행**: [[evaluation-harness]]에서 `lm_eval --model hf --tasks mmlu` 명령으로 표준화된 환경에서 실행할 수 있다.

**과목별 분석**: MMLU는 57개 과목별 정확도를 개별 보고할 수 있다. 전체 평균보다 특정 도메인(예: 의료, 법률, 컴퓨터 과학)의 성능이 모델 선택에 더 직접적인 정보를 제공한다. 자체 서비스의 주력 도메인에 해당하는 과목 점수를 별도로 확인하는 것이 바람직하다.

**MMLU-Pro 병행**: 포화 문제를 감안하여, MMLU와 MMLU-Pro를 함께 보고하는 것이 2025년 이후의 권장 관행이다. MMLU-Pro는 10지선다 형식과 추론 중심 문제로 변별력이 유지되며, CoT 유무에 따른 성능 차이도 의미 있는 분석 축이다.

## 관련 문서

- [[humaneval]] -- 코드 생성 벤치마크
- [[gsm8k]] -- 수학 추론 벤치마크
- [[truthfulqa]] -- 진실성 벤치마크
- [[mt-bench]] -- 다중 턴 대화 벤치마크
- [[benchmark-contamination]] -- 데이터 오염 문제
- [[benchmark-saturation-goodharts-law]] -- 벤치마크 포화
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[humanity-last-exam]] -- 극난이도 벤치마크
- [[livebench]] -- 동적 벤치마크
- [[swe-bench-pro]] -- 소프트웨어 엔지니어링 벤치마크
