---
title: Vibe Coding
aliases: ["vibe coding"]
category: concepts
page_type: concept
tags: [vibe-coding, karpathy, coding-agents, terminology, vibe-coding-hangover]
sources:
  - raw/2026-04-09-simon-willison-agentic-engineering-patterns.md
  - raw/2026-04-09-evolution-of-ai-agentic-patterns.md
created: 2026-04-09
updated: 2026-04-09
---

# Vibe Coding

## 정의

**Vibe coding**은 Andrej Karpathy가 2025년 2월에 만든 용어로, LLM에 프롬프트를 던져 리뷰하지 않은 프로토타입 수준의 코드를 얻는 방식을 가리킨다.

원문 정의 (Simon Willison 인용):
> "Vibe coding describes prompting LLMs to write unreviewed, prototype-quality code."

## 특징

- **비프로그래머도 사용 가능** — 코드 지식 없이 작동하는 결과물을 얻을 수 있다
- **리뷰 없음** — 생성된 코드를 검토하지 않고 그대로 실행
- **일회성** — 유지보수나 프로덕션 투입 전제가 아니다
- **"느낌(vibe)"에 의존** — 세부 구현보다 결과물 느낌으로 평가

## Agentic Engineering과의 대비

Simon Willison은 [[agentic engineering guide]]에서 vibe coding과 [[agentic engineering]]을 명확히 구분한다:

- **Vibe coding**: 결과의 "vibe"가 맞으면 OK. 코드 자체는 블랙박스로 남음.
- **Agentic engineering**: 프로페셔널 엔지니어가 프로덕션 기준의 코드를 에이전트로 생산.

## 언제 쓸 수 있는가

Simon 본인도 vibe coding을 활용한다. 예: SwiftUI 슬라이드 프레젠테이션 앱 "Present"를 Claude Code + Opus 4.6로 "vibe coded"했다. 단, 이후 [[linear walkthroughs]] 기법으로 자기 코드를 다시 이해했다.

**적절한 사용처**:
- 일회성 프로토타입
- 개념 검증 (proof of concept)
- 학습/탐색
- 개인 도구

**부적절한 사용처**:
- 팀이 유지보수할 프로덕션 코드
- 보안/신뢰성 중요 시스템
- 동료가 리뷰해야 하는 PR (→ [[anti-patterns in agentic engineering]])

## 인지 부채와의 관계

Vibe coded 코드는 작성자가 세부 구현을 모르는 상태로 쌓이기 쉽다. 이는 Simon이 말하는 [[cognitive debt]]의 전형적 원인이다. 코어 기능이 블랙박스가 되면 이후 기능 기획이 어려워진다.

## Vibe Coding Hangover (2025년 9월)

[[evolution of agentic patterns|에이전틱 패턴 연대기]]에 따르면 2025년 초 "vibe coding" 용어 인기 이후 몇 달 만에 그 한계가 드러났다. Fast Company가 2025년 9월에 보도한 현실:

- 3개월 된 AI MVP들이 투자자 자금을 받은 뒤 버그 축적
- 아무도 코드베이스를 이해하지 못해 기능 확장 불가
- "빠르게 만들었지만 유지 불가능한 프로토타입"이 프로덕션으로 끌려가는 현상

CodeRabbit의 코드 품질 분석 메트릭:
- AI 생성 코드: 메이저 이슈 발생률 **1.7배 높음**
- 보안 취약점 비율 **45% 증가**

이 "숙취"는 [[relocating rigor|엄밀함]]이 이동하지 않고 **증발**한 결과였다. [[prompt engineering]]이 벽에 부딪히고 [[context engineering]], [[harness engineering]]으로 패러다임이 이동한 중요한 경험적 근거 중 하나가 된다.

### Simon Willison의 교정

> "If you reviewed and tested, it's not vibe coding — it's engineering."
> ("리뷰하고 테스트했다면 그건 vibe coding이 아니라 engineering이다.")

이 문장은 vibe coding과 [[agentic engineering]]의 경계를 명확히 했다.

## 관련 문서

- [[agentic engineering]]
- [[agentic engineering guide]]
- [[cognitive debt]]
- [[linear walkthroughs]]
- [[anti-patterns in agentic engineering]]
- [[evolution of agentic patterns]] — 2025-09 Vibe Coding Hangover 사건 수록
- [[blind prompting]] — vibe coding의 "측정 없음" 측면
- [[relocating rigor]] — 엄밀함 증발 관점
