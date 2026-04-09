---
title: "Writing Code is Cheap Now"
aliases: ["code is cheap", "Writing Code is Cheap Now"]
category: concepts
page_type: concept
tags: [agentic-engineering, economics, habits, simon-willison]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Writing Code is Cheap Now

Simon Willison이 [[agentic engineering guide]] Section 1에서 제시한 핵심 원칙.

## 기본 주장

> "The biggest challenge in adopting agentic engineering practices is getting comfortable with the consequences of the fact that writing code is cheap now."

코드 작성은 역사적으로 **비쌌다**. 깨끗하고 테스트된 코드 몇 백 줄을 쓰려면 숙련 개발자도 하루 이상이 필요했다. 지금까지 우리의 엔지니어링 습관 대부분은 이 제약에서 비롯됐다.

## 매크로 레벨 영향

기존 의사결정:
- 프로젝트 설계, 추정, 계획에 큰 시간 투자 → 비싼 코딩 시간을 효율적으로 쓰기 위함
- 제품 기능은 개발 비용 대비 가치로 평가 → 원가를 여러 배 회수해야 함

지금 달라진 점: 개발 비용 추정의 분모가 변했다.

## 마이크로 레벨 영향

기존 의사결정 ("이 함수 리팩토링해야 할까?", "에지 케이스 테스트를 더 써야 할까?", "디버그 UI를 만들 가치가 있을까?")은 **가용 시간과 예상 트레이드오프**에 기반했다.

코딩 에이전트는 이 트레이드오프 계산을 뒤집는다. 병렬 에이전트까지 고려하면 한 엔지니어가 동시에 여러 곳에서 구현, 리팩토링, 테스트, 문서화를 진행할 수 있다.

## 하지만 *좋은* 코드는 여전히 비싸다

> "Delivering new code has dropped in price to almost free... but delivering good code remains significantly more expensive than that."

Simon이 정의하는 "good code" 체크리스트:

1. **작동한다** — 의도한 대로 작동하고 버그가 없다
2. **작동함을 안다** — 적합성을 확인하는 절차를 거쳤다
3. **올바른 문제를 푼다**
4. **에러 케이스를 우아하게 처리** — happy path만 고려하지 않음
5. **단순하고 최소** — 인간과 기계 모두 이해 가능
6. **테스트로 보호된다** — 회귀 방지 포함
7. **적절한 수준으로 문서화되고, 문서가 현재 상태를 반영**
8. **미래 변경을 지원** — YAGNI와 "미래 변경을 막지 않기" 사이의 균형
9. **관련 "-ilities"** — accessibility, testability, reliability, security, maintainability, observability, scalability, usability

이 모든 것을 검증하는 책임은 여전히 개발자에게 있다.

## 새로운 습관 형성

> "Any time our instinct says 'don't build that, it's not worth the time' fire off a prompt anyway, in an asynchronous agent session where the worst that can happen is you check ten minutes later and find that it wasn't worth the tokens."

핵심 전환:
- **Old**: 시간 없으니 안 함
- **New**: 일단 비동기 에이전트 세션으로 던지고 10분 후에 확인

## 왜 중요한가 (실무 관점)

- 리팩토링, 테스트 커버리지 확대, 문서 업데이트 같은 "좋지만 시간 없던 일들"이 다시 economically feasible해진다
- 탐색적 프로토타이핑이 값싸지면서 의사결정 전에 여러 접근을 실험 가능
- 단, 이 낮아진 비용이 *품질 하락*의 변명이 되면 안 된다 → [[better code with agents]]

## 관련 문서

- [[agentic engineering]]
- [[agentic engineering guide]]
- [[better code with agents]]
- [[anti-patterns in agentic engineering]]
- [[hoard things you know how to do]]
