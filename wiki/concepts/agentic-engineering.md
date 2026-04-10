---
title: Agentic Engineering
aliases: ["agentic engineering"]
category: concepts
page_type: concept
tags: [agentic-engineering, coding-agents, definition, paradigm]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md, raw/2026-04-09-evolution-of-ai-agentic-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Agentic Engineering

## 정의

**Agentic Engineering** = "코딩 에이전트(coding agent)의 도움을 받아 소프트웨어를 개발하는 실천"

Simon Willison이 [[agentic engineering guide]]에서 정의한 용어. 프로페셔널 소프트웨어 엔지니어가 코딩 에이전트를 활용해 자신의 작업을 개선하고 가속화하는 것을 가리킨다.

## 구성 요소

1. **[[coding agent]]** — 코드를 작성하고 *실행*할 수 있는 에이전트 (Claude Code, OpenAI Codex, Gemini CLI 등)
2. **Tools in a loop** — 에이전트는 "목표 달성을 위해 도구를 반복 실행하는 소프트웨어"
3. **Human judgment** — 무엇을 쓸지 결정, 트레이드오프 판단, 상황에 맞는 선택

## Vibe Coding과의 구별

Andrej Karpathy가 2025년 2월에 만든 용어 "[[vibe coding]]"은 LLM에 프롬프트를 던져 리뷰하지 않은 프로토타입 코드를 얻는 방식이다. Agentic engineering은 이와 달리 "production ready standard"를 목표로 한다.

| 구분 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 대상 | 비프로그래머 또는 실험 | 프로페셔널 엔지니어 |
| 품질 | 프로토타입 수준, 리뷰 없음 | 프로덕션 준비 수준 |
| 검증 | 거의 없음 | 테스트, 리뷰, 반복 |
| 지속성 | 일회성 | 유지보수 전제 |

## 효과적 실천을 위한 요건

Simon Willison이 정리한 네 가지:

1. **도구 제공** — 에이전트에게 필요한 도구(bash, python, 브라우저 자동화 등)를 갖춰줄 것
2. **문제 명세** — 적절한 수준의 디테일로 문제를 기술
3. **검증과 반복** — 결과를 확인하고 iterate
4. **지침 업데이트** — 얻은 교훈을 다음 작업에 반영

## 왜 "code execution"이 핵심인가

> "Without the ability to directly run the code, anything output by an LLM is of limited value."

코드를 직접 실행할 수 있는 능력이 agentic engineering의 근간이다. 단순 코드 생성 LLM과 coding agent의 결정적 차이.

## 3 에라 관점에서의 위치

[[evolution of agentic patterns|패러다임 연대기]]에 따르면 agentic engineering은 단일 시점의 용어가 아니라 세 에라를 관통하는 "프로페셔널한 에이전트 활용" 자세다:

- [[prompt engineering]] 시대: 좋은 프롬프트 + 리뷰
- [[context engineering]] 시대: 컨텍스트 설계 + 검증
- [[harness engineering]] 시대: 하네스 구축 + 측정

각 시대마다 "무엇에 엄밀함을 투자할지"는 달라지지만 (→ [[relocating rigor]]) 검증·리뷰·반복을 포기하지 않는다는 원칙은 동일하다. 이것이 [[vibe coding]]과 agentic engineering을 가르는 기준선이다.

## 관련 문서

- [[agentic engineering guide]]
- [[coding agent]]
- [[vibe coding]]
- [[how coding agents work]]
- [[code is cheap]]
- [[evolution of agentic patterns]]
- [[prompt engineering]]
- [[context engineering]]
- [[harness engineering]]
