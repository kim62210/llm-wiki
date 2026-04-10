---
title: Instructor Overview
category: tooling
page_type: summary
tags: [tooling, summary, instructor, structured-output, validation]
sources: [raw/recursive-sources/2026-04-10-baml-instructor-vercel-mastra/instructor-overview.md]
created: 2026-04-10
updated: 2026-04-10
---

# Instructor Overview

Instructor 공식 페이지 요약이다. 다중 언어 structured output 라이브러리로서 Instructor가 제공하는 검증, 재시도, 스키마 중심 개발 경험을 정리한다.

## 구조도

```mermaid
flowchart TD
    A[LLM 호출] --> B[Pydantic/typed schema]
    B --> C[validation + retry]
    C --> D[structured result]
```

Instructor는 모델 응답을 자유 텍스트로 받는 대신, 스키마·검증·재시도를 기본값으로 두는 얇은 통합층이다.

## 핵심 구조

- 공식 페이지는 Instructor를 다중 언어 structured output 라이브러리로 소개하며, quick start, validation, complex schemas, provider support를 한 번에 보여 준다.
- 핵심은 스키마 기반 결과 추출과 validation/retry 루프를 간단한 API로 감싼다는 점이다.
- 즉 model wrapper라기보다 “출력 품질을 계약화하는 보정층”에 가깝다.

## 왜 중요한가

- Instructor는 lightweight한 방식으로 structured outputs를 강화하고 싶을 때 자주 선택된다.
- Pydantic 모델과 자연스럽게 결합되므로 Python 애플리케이션에서 adoption friction이 낮다.
- 반면 더 큰 runtime abstraction을 원하는 경우에는 Pydantic AI나 BAML과 다른 선택이 될 수 있다.

## 실무 관점

- 구조화 출력 품질 문제를 빠르게 잡고 싶다면 Instructor는 좋은 첫 도구다.
- 하지만 tool use, long-running workflows, agent orchestration까지 한 번에 해결해 주는 프레임워크는 아니라는 점을 구분해야 한다.
- 즉 출력 검증 레이어로서의 위치를 명확히 이해하고 도입하는 것이 중요하다.

## 관련 문서

- [[instructor|Instructor]]
- [[baml|BAML]]
- [[pydantic-ai|Pydantic AI]]
