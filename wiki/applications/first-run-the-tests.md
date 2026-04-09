---
title: "First Run the Tests"
aliases: ["first run the tests", "First Run the Tests"]
category: applications
page_type: concept
tags: [testing, prompts, onboarding, coding-agents]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# First Run the Tests

Simon Willison이 [[agentic engineering guide]] Section 3에서 제안하는 **네 단어 프롬프트**.

## 기본 원칙

> "Automated tests are no longer optional when working with coding agents."

테스트 작성이 "시간/비용이 많이 든다"는 전통적 변명은 에이전트가 분 단위로 테스트를 만들어내는 지금 더 이상 유효하지 않다.

> "If the code has never been executed it's pure luck if it actually works when deployed to production."

## 프롬프트

새 세션에서 기존 프로젝트에 대해 작업을 시작할 때:

> First run the tests

Python 프로젝트에 pyproject.toml이 있으면:

> Run "uv run pytest"

## 이 짧은 프롬프트의 네 가지 효과

Simon이 설명하는 효과:

### 1. 테스트 스위트 존재를 알린다
에이전트에게 "이 프로젝트엔 테스트 스위트가 있다"는 사실을 각인시키고, 실행 방법을 스스로 찾게 한다. 한 번 실행 방법을 알아내면 이후에도 변경 후 자동으로 테스트를 돌릴 확률이 높아진다.

### 2. 프로젝트 규모의 프록시
대부분의 테스트 하네스는 "총 N개 테스트 중 M개 통과" 같은 요약을 출력한다. 이는 에이전트에게:
- 프로젝트 크기/복잡도의 대략적 감
- "테스트를 더 보고 싶으면 이 파일들을 읽어라" 힌트

를 제공한다.

### 3. 테스팅 마인드 확립
테스트를 먼저 실행했으니, 이후 변경을 할 때도 "새 테스트를 확장할까?" 생각이 자연스럽게 이어진다. 에이전트는 이미 테스트에 편향되어 있지만, 기존 스위트가 있으면 이 편향이 훨씬 강해진다.

### 4. 온보딩 가속
기존 코드베이스를 파악하려면 테스트부터 보는 것이 빠른 경로다. Claude Code 같은 에이전트에 기존 기능을 물으면 높은 확률로 관련 테스트를 찾아 읽는다.

## [[red-green TDD]]와의 시너지

세션 시작 패턴:

```
First run the tests
```
↓
```
Add a new feature X. Use red/green TDD.
```

두 개의 짧은 프롬프트가 에이전트를 강한 테스팅 규율에 묶는다.

## 비슷한 패턴

Simon이 언급하는 "established software engineering discipline이 LLM에 이미 내장되어 있음"을 활용한 다른 짧은 프롬프트:
- "Use red/green TDD"
- "First run the tests"

두 프롬프트 모두 긴 설명 없이 이미 잘 훈련된 행동을 trigger한다.

## 실무 적용

- 새 저장소에서 작업 시작할 때 자동 첫 프롬프트로 등록
- CI/pre-commit 훅에서도 응용 가능
- "Run the tests"로 충분하지만 "First"가 순서/우선순위를 강조

## 관련 문서

- [[red-green TDD]]
- [[agentic manual testing]]
- [[agentic engineering guide]]
- [[prompts library]]
