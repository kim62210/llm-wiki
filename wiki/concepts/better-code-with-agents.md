---
title: Better Code With Agents
aliases: ["better code with agents"]
category: concepts
page_type: concept
tags: [code-quality, technical-debt, refactoring, simon-willison]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Better Code With Agents

Simon Willison이 [[agentic engineering guide]]에서 제시하는 원칙: 코딩 에이전트를 도입한다고 해서 코드 품질이 반드시 하락하는 것은 아니다. 오히려 *더 나은* 코드를 쓸 기회다.

## 핵심 주장

> "Shipping worse code with agents is a choice. We can choose to ship code that is better instead."

## 기술 부채 상환 기회

에이전트가 특히 잘 처리하는, 개념적으로는 단순하지만 시간이 많이 드는 작업들:

- **API 설계 문제** — 여러 위치에 걸친 변경이 필요한 경우
- **네이밍 불일치** — 코드베이스 전반의 일관성 확보
- **중복 기능 통합** — 비슷한 로직을 하나로 모으기
- **거대 파일 분할** — 모듈화

이런 작업들은 **비동기 에이전트**에 맡기기 좋다. Simon이 예로 드는 도구: Gemini Jules, OpenAI Codex, [[Claude Code]]. 백그라운드에서 돌리면 본인 워크플로우를 중단하지 않는다.

평가 프로세스: PR 리뷰 → 필요 시 반복. 비용이 낮으므로 품질 개선이 경제적으로 feasible해진다.

## 해법 공간 탐색 확대

LLM은 놓치기 쉬운 기존 관행적 해법을 찾아준다. 또한 **비용 효율적 탐색 프로토타이핑**이 가능해진다:

- 여러 기술 접근을 에이전트로 동시에 시뮬레이션
- 커밋하기 전에 실증 검증

## Compound Engineering Loop

Every(미디어)의 방법론에서 차용한 개념. 성공한 접근을 문서화해 향후 에이전트 실행에 재투입하는 반복 개선 루프. 시간이 지나면서 품질 향상이 복리로 쌓인다.

## [[code is cheap]]과의 관계

- [[code is cheap]]: 코드 작성이 싸졌으니 이전에 "시간 없음"으로 포기했던 일들을 다시 하자
- Better code: 그 중 많은 일이 "*품질* 개선" 작업이다

두 원칙이 만나는 지점 = "더 많은 리팩토링, 더 많은 테스트, 더 많은 문서화를 실제로 할 수 있게 됐다."

## 안티패턴과의 대비

반대편에는 [[anti-patterns in agentic engineering]]이 있다. 대표적으로 리뷰 없이 에이전트 PR을 남에게 던지는 것 — 이는 품질을 *낮추는* 선택이다.

## 실무 적용

- 비동기 에이전트 세션을 "부채 상환 슬롯"으로 예약
- 리팩토링 아이디어가 떠오르면 메모해두고 배치로 에이전트에 할당
- 성공한 접근은 프롬프트 템플릿으로 저장 ([[prompts library]])

## 관련 문서

- [[code is cheap]]
- [[anti-patterns in agentic engineering]]
- [[red-green TDD]]
- [[agentic engineering guide]]
