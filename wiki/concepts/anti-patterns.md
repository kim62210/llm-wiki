---
title: Anti-patterns in Agentic Engineering
aliases: ["anti-patterns in agentic engineering", "anti-patterns"]
category: concepts
page_type: concept
tags: [anti-patterns, code-review, pull-requests, collaboration]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Anti-patterns in Agentic Engineering

Simon Willison이 [[agentic engineering guide]] Section 1에서 경고하는 "하지 말아야 할 행동들".

## 1. 리뷰하지 않은 코드를 동료에게 떠넘기기

**이것이 가장 흔하고 가장 짜증나는 안티패턴이다.**

> "Don't file pull requests with code you haven't reviewed yourself."

### 왜 문제인가

에이전트가 만들어낸 수백~수천 줄 코드를 본인이 검증하지 않고 PR로 올리면, 실제 검증 작업을 다른 사람에게 떠넘기는 것이다.

> "They could have prompted an agent themselves. What value are you even providing?"

리뷰어가 바로 프롬프트를 던졌으면 얻었을 결과를 당신이 떠넘긴 것뿐이다.

## 좋은 Agentic Engineering PR의 조건

Simon이 정리한 체크리스트:

### 1. 작동하는 코드 + 확신
> "Your job is to deliver code that works."

에이전트가 썼든 사람이 썼든, 작동 여부를 스스로 확인한 뒤에만 PR을 올린다. 수동 테스트([[agentic manual testing]])와 자동 테스트([[red-green TDD]], [[first run the tests]])를 조합.

### 2. 작은 변경
리뷰어에게 과도한 인지 부담을 주지 않도록:
- 여러 개의 작은 PR > 하나의 큰 PR
- 에이전트가 Git 조작을 대신 해주므로 커밋 분리가 쉽다 → [[git with coding agents]]

### 3. 추가 컨텍스트
- 이 변경이 기여하는 **상위 목표**가 무엇인가?
- 관련 이슈/스펙 링크
- 왜 이 접근을 선택했는가

### 4. PR 설명도 직접 검토
에이전트는 **그럴듯해 보이는 PR 설명**을 잘 쓴다. 하지만:
- 검증하지 않은 설명을 남에게 읽게 하는 것은 무례
- 반드시 읽고, 검증하고, 필요 시 수정

## 개인 기여 증거 포함하기

에이전트 코드 남용이 쉬운 환경에서는, 리뷰어의 시간이 낭비되지 않을 것임을 증거로 보여주는 편이 예의다:

- **수동 테스트 노트** — 어떤 시나리오를 직접 돌려봤는가
- **구현 선택에 대한 해설** — 왜 이 접근인가
- **스크린샷/비디오** — UI가 실제로 동작하는 모습

## 이 안티패턴을 피하는 실무 규칙

1. 에이전트 PR 초안을 받으면 **먼저 본인이 checkout해서 돌려본다**
2. [[first run the tests]] 프롬프트로 에이전트가 테스트를 통과시키게 한다
3. 코드를 직접 한 줄씩 읽고, 이해되지 않으면 [[linear walkthroughs]] 또는 [[interactive explanations]]로 이해를 쌓는다
4. PR 설명을 직접 다시 쓰거나 최소한 한 번 검토한다

## 왜 중요한가

에이전트로 인한 품질 하락은 [[better code with agents|선택의 문제]]다. 이 안티패턴을 방치하면:
- 팀 내 불신이 쌓인다
- 리뷰어의 시간이 낭비된다
- 프로덕션에 검증되지 않은 코드가 들어간다

## 관련 문서

- [[better code with agents]]
- [[code is cheap]]
- [[first run the tests]]
- [[red-green TDD]]
- [[agentic manual testing]]
- [[git with coding agents]]
- [[agentic engineering guide]]
