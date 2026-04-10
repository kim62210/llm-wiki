---
title: Instructor Patching
category: tooling
page_type: summary
tags: [tooling, summary, instructor, patching, providers]
sources: [raw/recursive-sources/2026-04-10-mastra-instructor-advanced/instructor-patching.md]
created: 2026-04-10
updated: 2026-04-10
---

# Instructor Patching

Instructor의 patching 문서 요약이다. LLM client patching이 무엇인지, patching modes, provider별 기본 모드, manual patching을 중심으로 설명한다.

## 구조도

```mermaid
flowchart LR
    A[원본 LLM client] --> B[Instructor patching]
    B --> C[provider별 mode 적용]
    C --> D[structured output interface]
```

Instructor patching은 새로운 런타임을 만드는 대신 기존 LLM client 위에 structured-output 동작을 덧입히는 접근이다.

## 핵심 구조

- 문서는 patching의 개념, patching modes, provider별 기본 모드, manual patching, provider-specific considerations를 설명한다.
- 즉 Instructor는 클라이언트를 완전히 대체하기보다, 기존 클라이언트에 기능을 덧입히는 전략을 취한다.
- 이 패턴이 Instructor의 얇은 채택 비용을 만드는 핵심이다.

## 왜 중요한가

- 많은 팀은 LLM client를 이미 앱 곳곳에서 사용 중이라, 완전 교체보다 patching 방식이 현실적이다.
- 하지만 patching은 내부 동작을 부분적으로 바꾸는 만큼 provider별 차이와 mode 선택이 중요하다.
- 따라서 “쉽다”는 인상 뒤에 있는 구현 경계를 이해해야 안정적으로 쓸 수 있다.

## 실무 관점

- 기본 모드가 무엇인지 확인하지 않고 쓰면 provider별 미묘한 차이로 예상치 못한 동작이 생길 수 있다.
- manual patching은 고급 옵션이므로 팀 내 표준화가 필요하다.
- 이 문서는 Instructor를 도입할 때 실제 앱 코드에 어떤 방식으로 꽂히는지 이해하게 만든다.

## 관련 문서

- [[instructor|Instructor]]
- [[instructor-overview|Instructor Overview]]
- [[instructor-retrying|Instructor Retrying]]
