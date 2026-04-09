---
title: Cognitive Debt
aliases: ["cognitive debt"]
category: concepts
page_type: concept
tags: [cognitive-debt, code-understanding, agentic-engineering]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Cognitive Debt

Simon Willison이 [[agentic engineering guide]]에서 소개한 개념. 기술 부채(technical debt)와 쌍을 이루는 새로운 용어.

## 정의

> "When we lose track of how code written by our agents works we take on cognitive debt."

**Cognitive debt** = 에이전트가 쓴 코드가 어떻게 동작하는지 내가 이해하지 못할 때 쌓이는 부채.

## 왜 발생하는가

코딩 에이전트 시대에 특히 심각해지는 이유:
- 에이전트가 수백~수천 줄 코드를 단번에 생성
- 그 결과물을 읽지 않고 실행 → 작동하면 넘어감
- [[vibe coding|Vibe coding]] 워크플로우가 대표적 원인
- 코드량이 늘어날수록 "이해 안 한 코드"의 양이 복리로 증가

## 왜 문제인가

### 간단한 코드면 OK

Simon의 구분:
> "For a lot of things this doesn't matter: if the code fetches some data from a database and outputs it as JSON the implementation details are likely simple enough that we don't need to care. We can try out the new feature and make a very solid guess at how it works, then glance over the code to be sure."

### 하지만 핵심 코드면 치명적

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

- 새 기능 기획 시 영향도 판단 불가
- 버그 원인 추론 불가
- 성능/보안 평가 불가
- 결국 기술 부채와 같은 방식으로 진행 속도 저하

## 상환 방법

> "How do we pay down cognitive debt? By improving our understanding of how the code works."

Simon이 제시하는 구체적 기법:

### 1. [[linear walkthroughs|Linear Walkthroughs]]
에이전트에게 코드베이스를 구조화된 형태로 설명하게 한다. [[Showboat]]로 문서화. 파일 단위, 함수 단위의 텍스트 설명.

### 2. [[interactive explanations|Interactive Explanations]]
정적 설명으로 부족한 부분(알고리즘, 기하, 공간 배치 등)은 인터랙티브 애니메이션/시뮬레이션으로 시각화. 예: Archimedean spiral word cloud 애니메이션.

### 3. (암묵적) 자신이 직접 읽기
에이전트 설명에 의존하기 전에, 본인이 한 번 쭉 읽어보는 것 자체가 기본 상환 수단.

## Technical Debt과의 비교

| 구분 | Technical Debt | Cognitive Debt |
|------|----------------|----------------|
| 무엇 | 코드가 나쁘다 | 내가 코드를 모른다 |
| 상환 | 리팩토링 | 이해 쌓기 |
| 증상 | 변경이 느려짐 | 변경 기획이 느려짐 |
| 원인 | 타협/쇼트컷 | 리뷰 안 함 / [[vibe coding]] |

두 부채는 겹칠 수 있지만 개념적으로 분리된다. 깨끗한 코드여도 이해하지 못하면 cognitive debt이다.

## 실무 함의

- 모든 에이전트 작업 후 이해 체크: "이 코드를 한 문장으로 설명할 수 있나?"
- 코어 기능일수록 이해 우선도 높임
- 주기적으로 [[linear walkthroughs]]로 전체 앱 복습
- 막히면 [[interactive explanations]]

## 관련 문서

- [[linear walkthroughs]]
- [[interactive explanations]]
- [[vibe coding]]
- [[anti-patterns in agentic engineering]]
- [[agentic engineering guide]]
