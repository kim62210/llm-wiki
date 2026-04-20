---
title: BAML
category: tooling
page_type: entity
project: BAML
tags: [tooling, entity, baml, dev-tooling-and-frameworks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/baml.md, raw/hot-topics-sources/2026-04-10/423-baml-official-docs.md, raw/hot-topics-sources/2026-04-10/424-boundary-ml-homepage.md, raw/hot-topics-sources/2026-04-10/425-boundaryml-baml-github.md, raw/hot-topics-sources/2026-04-10/426-structured-outputs-create-false-confidence-baml-blog.md, raw/hot-topics-sources/2026-04-10/427-baml-go-package.md]
created: 2026-04-10
updated: 2026-04-13
---
# BAML

이 페이지는 BAML를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL이기 때문이다.

## 정의

프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL.

## 왜 지금 중요한가

Schema-Aligned Parsing(SAP) 알고리즘으로 새 모델 출시 Day-1부터 구조화 출력이 작동하고, 2026년 들어 Python/TS/Ruby/Go/Java/C#/Rust까지 지원 언어가 확장되며 "스트링 기반 프롬프트 → 스키마 엔지니어링" 전환의 대표 도구가 됐다.

## 개요

이 페이지는 **BAML** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [BAML Official Docs](https://docs.boundaryml.com/home)
- [Boundary ML Homepage](https://boundaryml.com/)
- [BoundaryML/baml GitHub](https://github.com/BoundaryML/baml)
- [Structured Outputs Create False Confidence — BAML Blog](https://boundaryml.com/blog/structured-outputs-create-false-confidence)
- [baml Go Package](https://pkg.go.dev/github.com/boundaryml/baml)

## 하위 문서 읽기 경로

- [[baml-what-is-baml|What is BAML?]] - BAML DSL이 어떤 문제를 풀고 어떤 추상화 층위를 갖는지 정리

## 관련 문서
- [[llm-structured-output]] -- LLM 구조화 출력 (Structured Output)

- [[baml-what-is-baml]] - “What is BAML?” 문서 요약 (개발자 온보딩 경로)
- [[pydantic-ai]] - agent runtime까지 포함하는 더 넓은 추상화 비교 대상
- [[claude-agent-sdk]] - BAML과 함께 사용되는 Anthropic 에이전트 SDK
- [[instructor]] - 얇은 runtime [[instructor-validation|validation]] 계층, BAML의 대안 비교군
