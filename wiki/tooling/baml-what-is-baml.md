---
title: What is BAML?
category: tooling
page_type: summary
tags: [tooling, summary, baml, structured-output, prompt-dsl]
sources: [raw/recursive-sources/2026-04-10-baml-instructor-vercel-mastra/baml-what-is-baml.md]
created: 2026-04-10
updated: 2026-04-10
---

# What is BAML?

BoundaryML의 “What is BAML?” 문서 요약이다. BAML을 구조화 출력과 LLM 함수 인터페이스를 위한 전용 DSL로 보는 관점을 정리한다.

## 구조도

```mermaid
flowchart LR
    A[BAML spec] --> B[prompt / function contract]
    B --> C[typed client generation]
    C --> D[structured LLM integration]
```

BAML의 핵심은 프롬프트 문자열을 직접 흩뿌리는 대신, 구조화된 계약을 별도 DSL로 끌어내는 데 있다.

## 핵심 구조

- 문서는 BAML을 LLM 함수 인터페이스와 structured output을 위한 별도 명세 언어로 소개한다.
- 핵심은 프롬프트와 출력 구조를 코드 여기저기에 흩뿌리지 않고, 명시적 계약 파일로 끌어내는 것이다.
- 이 접근은 프롬프트 엔지니어링을 코드 생성 가능한 인터페이스 설계로 바꾼다.

## 왜 중요한가

- BAML은 structured output 라이브러리의 한 종류이면서도, 더 강하게 “전용 언어 + 생성된 클라이언트” 쪽으로 기운다.
- 따라서 Python/TS 앱 코드에서 prompt contract drift를 줄이는 데 유용할 수 있다.
- 이는 [[instructor|Instructor]]나 [[pydantic-ai|Pydantic AI]]와는 다른 추상화 층위다.

## 실무 관점

- 도입 전에 팀이 원하는 것이 단순 schema validation인지, 아니면 prompt/interface 분리 자체인지 먼저 판단해야 한다.
- BAML의 장점은 명시적 계약과 코드 생성에 있지만, 그만큼 DSL 학습 비용도 따른다.
- 그래서 대규모 structured-output surface를 장기 유지하려는 팀에서 특히 의미가 크다.

## 관련 문서

- [[baml|BAML]]
- [[instructor|Instructor]]
- [[pydantic-ai|Pydantic AI]]

## 비교표

| 도구 | 주된 추상화 | 강점 | 주의점 |
| --- | --- | --- | --- |
| BAML | 전용 DSL + 생성된 클라이언트 | prompt/interface 분리 강함 | DSL 학습 비용 |
| Instructor | 런타임 검증/재시도 레이어 | 빠르고 얇은 통합 | 계약 분리 수준은 낮음 |
| Pydantic AI | agent/runtime abstraction | 더 넓은 시스템 경계 제공 | 더 무거운 도입 |

## 읽는 순서

- 이 문서로 BAML의 추상화 층위를 이해한다.
- [[instructor|Instructor]]와 비교해 “얇은 검증층 vs 전용 계약 언어” 차이를 본다.
- 구조화 출력 문제가 agent runtime 문제로 커질 경우 [[pydantic-ai|Pydantic AI]]까지 확장해 읽는다.

