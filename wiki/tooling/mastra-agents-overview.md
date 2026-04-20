---
title: Mastra Agents Overview
category: tooling
page_type: summary
tags: [tooling, summary, mastra, agents, typescript]
sources: [raw/recursive-sources/2026-04-10-mastra-instructor-advanced/mastra-agents-overview.md]
created: 2026-04-10
updated: 2026-04-13
---
# Mastra Agents Overview

[[mastra|Mastra]] agents overview 문서 요약이다. agent를 언제 써야 하는지, quickstart 이후 어떻게 확장하고 multi-agent 시스템으로 발전시키는지 정리한다.

## 구조도

```mermaid
flowchart TD
    A[언제 agent를 쓰는가] --> B[quickstart]
    B --> C[agent 사용]
    C --> D[agent 확장]
    D --> E[multi-agent systems]
```

Mastra의 agent 문서는 단일 agent 생성법보다, 언제 agent abstraction이 적합한지와 어떻게 확장하는지가 중심이다.

## 핵심 구조

- 문서는 “when to use agents”에서 출발해 quickstart, agent 사용, agent 확장, multi-agent systems 순서로 agent abstraction을 설명한다.
- 즉 Mastra에서 agent는 단순 helper가 아니라, 앱 안의 작업 단위를 구조화하는 핵심 컴포넌트다.
- multi-agent가 같은 문서에 바로 이어지는 점은 Mastra가 처음부터 협업형 구조를 염두에 둔다는 신호다.

## 왜 중요한가

- TS 프레임워크 계열에서는 “언제 workflow를 쓰고 언제 agent를 쓰는가” 경계가 특히 중요하다.
- Mastra docs가 이 질문을 전면에 내세우는 건, agent를 무분별하게 늘리는 대신 적합한 문제에 쓰게 만들기 위함으로 읽힌다.
- 또한 expand your agent 섹션은 기능 목록보다 성장 경로를 보여 준다.

## 실무 관점

- 처음에는 단일 agent로 시작하고, 실제 병목이 보일 때 [[mastra-workflows-overview|workflow로 고정하거나]] multi-agent로 올라가는 식이 안전하다.
- 따라서 이 문서는 [[mastra-workflows-overview|Mastra Workflows Overview]]와 나란히 읽어야 설계 판단이 쉬워진다.
- Mastra를 채택하는 팀은 agent와 workflow를 각각 어떤 문제에 배치할지 규칙을 먼저 정하는 편이 좋다.

## 원문이 다루는 흐름

참조 source는 `Mastra Agents Overview`를 하나의 정의로 닫지 않고, 주변 설계 맥락과 읽기 순서를 함께 제공한다. 그래서 짧은 소개문만으로 끝내기보다 **구조와 적용 포인트**를 같이 정리해야 위키 문서로서 가치가 생긴다.

- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **Agents overview | Mastra Docs** — snapshot: `raw/recursive-sources/2026-04-10-mastra-instructor-advanced/mastra-agents-overview.md` · source: https://mastra.ai/docs/agents/overview · 볼 섹션: 핵심 heading 추출이 제한적

## 관련 문서

- [[mastra|Mastra]]
- [[mastra-get-started|Mastra Get Started]]
- [[mastra-workflows-overview|Mastra Workflows Overview]]
- [[mastra-memory-overview|Mastra Memory Overview]]
