---
title: Red/Green TDD with Coding Agents
aliases: ["red-green TDD", "red/green TDD", "Red/Green TDD"]
category: applications
page_type: concept
tags: [tdd, testing, prompts, red-green, agents]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Red/Green TDD with Coding Agents

Simon Willison이 [[agentic engineering guide]] Section 3의 핵심 프롬프트 패턴으로 소개한 기법.

## 한 줄 요약

> "Use red/green TDD" is a pleasingly succinct way to get better results out of a coding agent.

이 네 단어는 에이전트에게 "TDD, 테스트 먼저, 실패 확인 후 구현" 전체 규율을 한 번에 전달한다.

## TDD 복습

**Test Driven Development (TDD)** = 모든 코드 변경이 자동 테스트로 뒷받침되도록 하는 프로그래밍 스타일.

가장 엄격한 형태는 **test-first development**:
1. **Red**: 테스트를 먼저 쓰고, 실행해서 실패를 확인
2. **Green**: 테스트가 통과하도록 구현을 iterate

## 왜 코딩 에이전트에 이상적인가

코딩 에이전트의 주요 리스크 두 가지:
1. **작동하지 않는 코드**를 쓸 수 있다
2. **불필요한 코드**(쓰이지 않는 코드)를 쓸 수 있다

Test-first는 이 두 가지를 **동시에 방어**한다:
- 먼저 테스트가 있으니 구현이 꼭 필요한 것만 쓰인다
- 테스트가 통과하면 의도된 동작이 검증된다
- 미래 변경 시 회귀 방지 스위트로 작동

```mermaid
stateDiagram-v2
    [*] --> WriteTest: 요구사항 이해
    WriteTest --> RunRed: 테스트 작성
    RunRed --> CheckRed{실패<br/>확인?}
    CheckRed --> WriteTest: 이미 통과<br/>= 테스트 무효
    CheckRed --> WriteImpl: 실패 확인 OK<br/>(Red)
    WriteImpl --> RunGreen: 구현 작성
    RunGreen --> CheckGreen{통과?}
    CheckGreen --> WriteImpl: 실패 → 수정
    CheckGreen --> Refactor: 통과 (Green)
    Refactor --> [*]: 다음 기능
```

핵심은 **Red 단계를 반드시 거치는 것**. "이미 통과하는" 테스트는 새 구현을 검증하지 못하므로 실격이다.

Simon은 특히 프로젝트가 커질수록 "새 변경이 기존 기능을 깰 확률"이 올라가고, 포괄적 테스트 스위트가 이를 막는 가장 효과적인 수단이라고 강조한다.

## "Red" 단계 확인의 중요성

테스트가 **실패하는 것을 먼저 확인**해야 한다. 이 단계를 건너뛰면:
- 이미 통과하는 테스트를 만들 수 있음
- 새 구현을 실제로 검증하지 못함

"red/green"이라는 이름이 바로 이 순서를 강조한다. Red를 본 뒤에야 Green으로 이동할 수 있다.

## 프롬프트 예시

Simon이 제시하는 최소 프롬프트:

> Build a Python function to extract headers from a markdown string. Use red/green TDD.

"use red/green TDD" 네 단어만으로 에이전트는:
1. 먼저 pytest/unittest 기반 테스트 작성
2. 실행해서 실패 확인
3. 구현 작성
4. 다시 실행해서 통과 확인
5. 필요 시 엣지 케이스 테스트 추가

## [[first run the tests]]와의 조합

새 세션 시작 시:

1. "First run the tests" → 에이전트에게 테스트 스위트가 있다는 것과 실행 방법을 학습시킴
2. "Use red/green TDD" → 새 변경을 TDD로 진행

두 네 단어 프롬프트의 조합이 에이전트를 강력한 테스팅 마인드에 고정시킨다.

## 실무 팁

- **한국어 프롬프트에서도 "red/green TDD"는 영어 그대로** 사용하는 편이 에이전트 이해도가 높다
- 복잡한 기능일수록 TDD 지시가 효과적 (단순 CRUD에도 하락 부작용 거의 없음)
- 실패를 건너뛰는 에이전트가 보이면 "먼저 실패를 확인하라"를 추가

## 관련 문서

- [[first run the tests]]
- [[agentic manual testing]]
- [[better code with agents]]
- [[anti-patterns in agentic engineering]]
- [[agentic engineering guide]]
