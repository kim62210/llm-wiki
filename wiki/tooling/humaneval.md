---
title: HumanEval
category: tooling
page_type: entity
tags: [tooling, entity, benchmark, evaluation, code-generation, humaneval]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# HumanEval

HumanEval은 OpenAI가 2021년 Codex 논문("Evaluating Large Language Models Trained on Code")과 함께 공개한 코드 생성 벤치마크다. 164개의 수작업 프로그래밍 문제로 구성되어 있으며, 생성된 코드가 실제로 동작하는지를 단위 테스트(unit test)로 검증하는 기능적 정확성(functional correctness) 평가를 도입했다. pass@k 메트릭이라는 평가 방식을 대중화한 벤치마크이기도 하다.

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 이름 | HumanEval |
| 개발 | OpenAI |
| 논문 | "Evaluating Large Language Models Trained on Code" (2021) |
| 저장소 | github.com/openai/human-eval |
| 문제 수 | 164개 |
| 언어 | Python |
| 평균 테스트 수 | 문제당 7.7개 단위 테스트 |
| 핵심 메트릭 | pass@k |

## 데이터셋 구조

각 문제는 네 가지 요소로 구성된다.

- **함수 시그니처(function signature)**: 함수 이름과 매개변수
- **독스트링(docstring)**: 함수의 기능 설명, 입출력 예시 포함
- **함수 본문(body)**: 정답 구현 (평가 시 숨김)
- **단위 테스트**: 정확성 검증용 assert 문 (문제당 평균 7.7개)

문제 난이도는 간단한 문자열 처리부터 재귀, 동적 프로그래밍까지 다양하다. 다만 전체적으로 알고리즘 면접 수준이며, 실제 소프트웨어 엔지니어링의 복잡성(다중 파일, 라이브러리 의존성, 테스트 작성)은 반영하지 않는다.

## pass@k 메트릭

HumanEval의 핵심 기여는 pass@k 메트릭의 공식화다.

**정의**: 모델이 k개의 코드 샘플을 생성했을 때, 그 중 하나라도 모든 단위 테스트를 통과할 확률을 추정한다.

```
pass@k = E[1 - C(n-c, k) / C(n, k)]
```

여기서 n은 총 생성 샘플 수, c는 통과한 샘플 수, C는 조합(combination)이다.

**실무적 의미**:
- **pass@1**: 모델의 첫 시도 정확도. 실제 사용자 경험에 가장 가까운 지표
- **pass@10**: 10번 시도 중 하나라도 성공할 확률. 반복 샘플링 전략의 효과를 측정
- **pass@100**: 모델의 이론적 코드 생성 능력 상한

## 역사적 성능 추이

HumanEval 성능의 빠른 발전은 코드 생성 AI의 급속한 진보를 보여준다.

- **Codex (2021)**: pass@1 28.8%, pass@100 70.2% -- HumanEval과 함께 공개된 최초 결과
- **GPT-4 (2023)**: pass@1 약 67%
- **GPT-4o (2024)**: pass@1 약 90%
- **o1 (2024)**: pass@1 96.3% -- 사실상 포화 수준
- **2025~2026 frontier 모델**: pass@1 95% 이상이 일반적

이 추세는 HumanEval이 현재 최상위 모델을 변별하기 어려운 포화 상태에 도달했음을 의미한다 -- [[benchmark-saturation-goodharts-law]] 현상의 전형적 사례다.

## HumanEval의 한계

**범위 제한**: 164개 문제는 Python 전용이며, 실제 소프트웨어 개발의 극히 일부만 반영한다. 다중 파일 프로젝트, API 호출, 데이터베이스 상호작용, 에러 처리 같은 실무 과제는 포함하지 않는다.

**포화**: 최신 모델들이 95% 이상을 기록하면서 변별력을 잃었다.

**오염 우려**: 164개 문제가 인터넷에 널리 공개되어 있어 학습 데이터 오염([[benchmark-contamination]]) 가능성이 높다.

**단순한 테스트 케이스**: 문제당 평균 7.7개 테스트는 edge case를 충분히 커버하지 못한다. 테스트를 통과했지만 실제로는 틀린 해법이 존재할 수 있다.

## 후속 벤치마크

HumanEval의 한계를 보완하기 위해 다양한 후속 벤치마크가 등장했다.

- **HumanEval+**: 테스트 케이스를 대폭 확충하여 false positive를 줄인 강화판
- **MBPP (Mostly Basic Python Problems)**: 974개 문제로 규모 확대
- **MultiPL-E**: HumanEval을 18개 프로그래밍 언어로 확장
- **[[swe-bench-pro]]**: 실제 GitHub 이슈 해결을 통한 소프트웨어 엔지니어링 능력 평가 -- 단일 함수가 아닌 프로젝트 수준의 코드 변경을 평가
- **LiveCodeBench**: 새로운 프로그래밍 대회 문제를 지속 추가하여 오염 방지

## 실무 활용 가이드

**모델 선택 기준으로서**: 2026년 시점에서 HumanEval pass@1만으로 코딩 능력을 판단하기는 어렵다. [[swe-bench-pro]] 점수를 함께 참고하고, 가능하면 실제 업무 관련 코드 생성 태스크로 자체 평가를 수행하는 것이 바람직하다.

**평가 실행**: [[evaluation-harness]]에서 지원하며, [[deepeval]]에서도 HumanEval 벤치마크를 내장 제공한다.

**pass@k 선택**: 사용자 대면 서비스라면 pass@1이 핵심이다. 코드 리뷰/수정 파이프라인이 있다면 pass@5나 pass@10도 의미 있다.

## 관련 문서

- [[mmlu]] -- 지식 평가 벤치마크
- [[gsm8k]] -- 수학 추론 벤치마크
- [[swe-bench-pro]] -- 소프트웨어 엔지니어링 벤치마크
- [[swe-bench-ecosystem-2026]] -- SWE-bench 생태계
- [[benchmark-contamination]] -- 데이터 오염 문제
- [[benchmark-saturation-goodharts-law]] -- 벤치마크 포화
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[livebench]] -- 동적 벤치마크
