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

## 2026년 4월 큐레이션 요약

- 정의: 올바른 도구 선택과 올바른 파라미터 호출을 분리해 평가.
- 왜 중요한가: Arize Phoenix가 2026년 1-2월 두 개의 전용 평가자를 출시하면서, "잘못된 도구 선택"과 "올바른 도구+잘못된 인자"를 분리 진단하는 것이 tool-calling 에이전트 디버깅의 표준 패턴이 되었다.
- 직접 수집 원문: 5개
- 주요 도메인: arize.com×4, github.com×1

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
