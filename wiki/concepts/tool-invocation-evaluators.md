---
title: Tool Selection & Tool Invocation Evaluators
category: concepts
page_type: concept
tags: [concepts, concept, tool, invocation, evaluators]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/tool-invocation-evaluators.md, raw/hot-topics-sources/2026-04-10/232-tool-selection-and-tool-invocation-evaluators-release-notes.md, raw/hot-topics-sources/2026-04-10/233-how-to-evaluate-tool-calling-agents.md, raw/hot-topics-sources/2026-04-10/234-tool-invocation-evaluator-docs.md, raw/hot-topics-sources/2026-04-10/235-agent-tool-selection.md, raw/hot-topics-sources/2026-04-10/236-phoenix-github-repository.md]
created: 2026-04-10
updated: 2026-04-10
---
# Tool Selection & Tool Invocation Evaluators

올바른 도구 선택과 올바른 파라미터 호출을 분리해 평가.

## 왜 중요한가

Arize Phoenix가 2026년 1-2월 두 개의 전용 평가자를 출시하면서, "잘못된 도구 선택"과 "올바른 도구+잘못된 인자"를 분리 진단하는 것이 tool-calling 에이전트 디버깅의 표준 패턴이 되었다.

## 대표 레퍼런스

- [Tool Selection and Tool Invocation Evaluators Release Notes (Phoenix, 2026-02-01)](https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators)
- [How to Evaluate Tool-Calling Agents (Arize Blog, 2026-03-02)](https://arize.com/blog/how-to-evaluate-tool-calling-agents/)
- [Tool Invocation Evaluator Docs (Phoenix)](https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation)
- [Agent Tool Selection (Arize AX Docs)](https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation)
- [Phoenix GitHub Repository](https://github.com/Arize-ai/phoenix)

## 해석 포인트

Tool Selection & Tool Invocation Evaluators은 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arize.com×4, github.com×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 올바른 도구 선택과 올바른 파라미터 호출을 분리해 평가.
- 왜 중요한가: Arize Phoenix가 2026년 1-2월 두 개의 전용 평가자를 출시하면서, "잘못된 도구 선택"과 "올바른 도구+잘못된 인자"를 분리 진단하는 것이 tool-calling 에이전트 디버깅의 표준 패턴이 되었다.
- 직접 수집 원문: 5개
- 주요 도메인: arize.com×4, github.com×1

## 핵심 메커니즘

올바른 도구 선택과 올바른 파라미터 호출을 분리해 평가. 이 개념은 단일 문장 정의보다 **어떤 failure mode를 설명하는지, 어떤 구조적 trade-off를 드러내는지**를 함께 볼 때 가치가 커진다.

## 핵심 포인트

Tool Selection & Tool Invocation Evaluators는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 올바른 도구 선택과 올바른 파라미터 호출을 분리해 평가.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arize.com×4, github.com×1로 분포한다. 구현 저장소 비중이 높아 실제 사용·통합 관점이 두드러진다.

## 실무 관점

개념 페이지는 용어 정의에서 끝나지 않고, 어떤 시스템 설계 문제를 해결하려고 등장했는지와 어디까지가 적용 범위인지까지 함께 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/tool-invocation-evaluators.md`

### source별 핵심 신호

- **Release Notes - Phoenix** (`arize.com`): https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators
  - 메모: January 31, 2026Available in arize-phoenix-evals 0.16.0+ (Python) and @arizeai/phoenix-evals 1.3.0+ (TypeScript)Phoenix now provides two specialized evaluators for assessing AI agent tool usage.
- **How to Evaluate Tool-Calling Agents - Arize AI** (`arize.com`): https://arize.com/blog/how-to-evaluate-tool-calling-agents/
  - 메모: The model selects the wrong tool (or calls a tool when it should have answered directly).
- **Tool Invocation - Phoenix** (`arize.com`): https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation
  - 메모: The Tool Invocation evaluator determines whether an LLM invoked a tool correctly with proper arguments, formatting, and safe content.
- **Agent evaluation - Arize AX Docs** (`arize.com`): https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation
  - 메모: Getting agents to work is hard. LLMs are non-deterministic. A bad response upstream leads to a strange response downstream. Agents can take inefficient paths and still get to the right solution.
- **GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub** (`github.com`): https://github.com/Arize-ai/phoenix
  - 메모: To see all available qualifiers, see our documentation.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[multi-turn-agent-evaluation|Multi-Turn Agent Evaluation]]
- [[rubric-based-evals|Rubric-Based Evaluation Frameworks]]
- [[context-engineering|Context Engineering]]
