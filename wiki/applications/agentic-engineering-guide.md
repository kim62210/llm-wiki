---
title: Agentic Engineering Patterns 가이드 (Simon Willison)
aliases: ["agentic engineering guide", "Agentic Engineering Patterns"]
category: applications
page_type: summary
tags: [agentic-engineering, coding-agents, simon-willison, best-practices, guide]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Agentic Engineering Patterns 가이드

Simon Willison이 2026-02-23에 시작한 가이드 시리즈. 코딩 에이전트(Claude Code, OpenAI Codex, Gemini CLI 등)를 사용하는 프로페셔널 소프트웨어 엔지니어를 위한 패턴 모음이다. 1994년 GoF *Design Patterns* 책에서 영감을 받았으며, 블로그 챕터 형식으로 지속 업데이트되는 "살아있는 가이드"로 설계되었다.

## 왜 중요한가

코딩 에이전트가 코드 작성 비용을 극적으로 낮추면서 기존의 엔지니어링 직관이 무너졌다. 이 가이드는 "[[vibe coding]]"과 구별되는, 프로덕션 수준의 코드를 목표로 하는 전문가 수준의 실천 패턴을 정리한다.

> "Agentic Engineering represents professional software engineers using coding agents to improve and accelerate their work." — Simon Willison

## 가이드 구조

### Section 1: 원칙 (Principles)
- [[agentic engineering]] — "코딩 에이전트의 도움을 받아 소프트웨어를 개발하는 실천"의 정의
- [[code is cheap]] — 코드 작성 비용이 거의 0에 가까워졌다는 새로운 현실
- [[hoard things you know how to do]] — 재사용 가능한 작동 예제를 축적하기
- [[better code with agents]] — 에이전트로 더 나은 코드를 쓸 수도 있다는 선택
- [[anti-patterns in agentic engineering]] — 특히 "리뷰 안 한 코드를 PR로 던지기" 금지

### Section 2: 코딩 에이전트와 작업하기
- [[how coding agents work]] — LLM 하네스, 시스템 프롬프트, 도구 호출 루프
- [[git with coding agents]] — Git을 에이전트의 시간 여행 도구로 활용
- [[subagents]] — 컨텍스트 창을 보존하기 위한 하위 에이전트 패턴

### Section 3: 테스트와 QA
- [[red-green TDD]] — 에이전트에게 가장 강력한 짧은 프롬프트 중 하나
- [[first run the tests]] — 기존 코드베이스 온보딩을 위한 네 단어 프롬프트
- [[agentic manual testing]] — Playwright/Rodney/Showboat로 수동 테스트 자동화

### Section 4: 코드 이해
- [[linear walkthroughs]] — 에이전트가 자기 코드를 설명하게 하기
- [[interactive explanations]] — [[cognitive debt]]를 갚기 위한 애니메이션 설명

### Section 5: 주석 달린 프롬프트 (Annotated Prompts)
- [[gif optimization case study]] — Gifsicle → WASM 예제

### Section 6: 부록
- [[prompts library]] — Simon Willison이 상시 사용하는 프롬프트 모음

## 핵심 인사이트

1. **코드 작성은 싸졌지만 *좋은* 코드는 여전히 비싸다** — 엔지니어의 일은 "무엇이 좋은 코드인가"를 판단하고 검증하는 데로 이동한다.
2. **리뷰 안 한 코드는 동료에게 던지지 마라** — 에이전트 PR을 그대로 남에게 떠넘기는 것은 무임승차다.
3. **테스트는 선택이 아니다** — 에이전트가 테스트를 분 단위로 작성할 수 있는 지금, 테스트 없는 변경은 정당화되지 않는다.
4. **이해 상실은 인지 부채(cognitive debt)다** — 내가 작성하지 않은 코드를 이해하지 못하면 이후 기능 기획이 느려진다.
5. **재사용 가능한 지식을 축적하라** — "트릭은 한 번만 알아내면 된다"는 관점에서 개인 예제 저장소를 키워라.

## 실무 적용 관점

- 새 프로젝트 시작 시: "First run the tests" → "Use red/green TDD" 조합으로 에이전트를 테스팅 마인드에 고정
- 기존 대형 코드베이스 탐색: [[subagents]]의 Explore 패턴으로 컨텍스트 창 보호
- UI 검증: [[Playwright]], [[Rodney]], [[agent-browser]], [[Showboat]]로 에이전트가 직접 브라우저 테스트
- 이해가 부족할 때: 선형 walkthrough → 인터랙티브 애니메이션 단계로 [[cognitive debt]] 상환

## 관련 문서

- [[agentic engineering]]
- [[vibe coding]]
- [[coding agent]]
- [[how coding agents work]]
- [[code is cheap]]
- [[red-green TDD]]
- [[subagents]]
- [[anti-patterns in agentic engineering]]
- [[agentic manual testing]]
- [[interactive explanations]]
- [[prompts library]]
- [[Claude Code]]

## 출처
- 원본: https://simonwillison.net/guides/agentic-engineering-patterns
- 소개 포스트: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
- raw 파일: `raw/2026-04-09-simon-willison-agentic-engineering-patterns.md`
