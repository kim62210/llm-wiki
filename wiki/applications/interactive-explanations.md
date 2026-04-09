---
title: Interactive Explanations
aliases: ["interactive explanations"]
category: applications
page_type: concept
tags: [code-understanding, visualization, cognitive-debt, animations]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Interactive Explanations

Simon Willison이 [[agentic engineering guide]] Section 4에서 제시하는 [[cognitive debt|인지 부채]] 상환 기법.

## 문제: Cognitive Debt

> "When we lose track of how code written by our agents works we take on cognitive debt."

일부 코드는 블랙박스여도 괜찮다 (DB에서 데이터 읽어 JSON으로 반환하는 단순 핸들러 등). 하지만 애플리케이션의 **코어**가 블랙박스가 되면:
- 자신감 있게 추론 불가
- 새 기능 기획이 어려워짐
- 기술 부채와 같은 방식으로 진행 속도를 떨어뜨림

해법: **이해를 쌓아 부채를 갚는 것**.

## 한 가지 유력한 기법: Interactive Explanations

정적 walkthrough만으로 부족할 때, **인터랙티브하게 알고리즘의 동작을 보여주는 설명**을 에이전트에게 만들게 한다.

## 사례: Word Cloud 알고리즘 이해

Simon의 경험:

### 1단계: Max Woolf 프롬프트 차용
Max Woolf의 글 "An AI agent coding skeptic tries AI agent coding, in excessive detail"에 등장한 프롬프트:

> "Create a Rust app that can create 'word cloud' data visualizations given a long input text"

Simon은 이에 영감을 받아 비동기 연구 프로젝트로 실험. Claude Code for web이 word cloud 이미지를 생성하는 Rust CLI 도구를 만들어줌.

### 2단계: 어떻게 동작하는지 궁금증
Claude의 보고서에 적힌 설명:

> "Archimedean spiral placement with per-word random angular offset for natural-looking layouts"

→ **이 문장만으로는 전혀 이해되지 않음.**

### 3단계: Linear Walkthrough
[[linear walkthroughs|선형 walkthrough]]를 요청해 Rust 코드 구조를 파악. 구조는 이해했지만 "Archimedean spiral placement"가 실제로 어떻게 작동하는지 **직관적** 이해가 부족.

### 4단계: 애니메이션 요청
기존 walkthrough 문서 링크를 Claude Code 세션에 붙이고 다음 프롬프트:

```
Build an animated-word-cloud.html page that accepts pasted text
(persisted in the URL fragment), builds a word cloud using the algorithm
with animation to make it clear to understand.
Include a slider for animation control with pause, speed adjustment,
and frame-by-frame stepping.
The visible word cloud can be downloaded as PNG at any stage.
```

Claude Opus 4.6 사용. Simon의 평가:

> "Claude Opus 4.6, which turns out to have quite good taste when it comes to building explanatory animations."

### 5단계: 이해가 "딸깍" 함

애니메이션을 자세히 보면:
- 각 단어마다 박스를 표시
- 박스가 기존 단어와 겹치는지 검사
- 겹치면 중심에서 나선(spiral) 방향으로 계속 이동하며 빈자리 탐색

> "I found that this animation really helped make the way the algorithm worked click for me."

## 왜 효과적인가

- LLM은 인터랙티브 HTML/JS를 만드는 데 능숙
- 정적 텍스트로 설명이 어려운 기하학/공간 알고리즘에 특히 유리
- **요구 시 맞춤 제작**이 가능 — 이해가 막힌 정확한 지점을 타겟팅 가능
- 슬라이더, 일시정지, 프레임 스텝 같은 컨트롤로 깊은 탐색 허용

## 활용 가능한 영역

Simon은 "인터랙티브 인터페이스와 애니메이션으로 개념을 설명하는 것을 오래 선호했다"고 말한다. 적용 가능 분야:
- 알고리즘 (정렬, 그래프 탐색, 기하 배치)
- 데이터 구조 (트리, 해시 테이블)
- 시스템 동작 (컴포넌트 간 메시지 흐름)
- 수학 개념 (벡터 연산, 확률 분포)

## [[linear walkthroughs]]와의 결합

권장 순서:
1. **Linear walkthrough** — 코드 구조와 파일 간 관계 파악
2. 특정 알고리즘/컴포넌트가 여전히 모호하면
3. **Interactive explanation** — 그 부분만 시각화 요청

## 관련 문서

- [[cognitive debt]]
- [[linear walkthroughs]]
- [[vibe coding]]
- [[Claude Code]]
- [[agentic engineering guide]]
