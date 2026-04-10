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
- [Agent Tool Selection (Arize AX Docs)](https://arize.com/docs/ax/evaluate/llm-as-a-judge/arize-evaluators-llm-as-a-judge/agent-tool-selection)
- [Phoenix GitHub Repository](https://github.com/Arize-ai/phoenix)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arize.com 4건, github.com 1건
- source 조합: 구현체, 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/tool-invocation-evaluators.md`
- [Release Notes - Phoenix](https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators) — `raw/hot-topics-sources/2026-04-10/232-tool-selection-and-tool-invocation-evaluators-release-notes.md`
  - 메모: --- title: Release Notes - Phoenix source_url: https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators final_url: https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators st
- [How to Evaluate Tool-Calling Agents - Arize AI](https://arize.com/blog/how-to-evaluate-tool-calling-agents) — `raw/hot-topics-sources/2026-04-10/233-how-to-evaluate-tool-calling-agents.md`
  - 메모: --- title: How to Evaluate Tool-Calling Agents - Arize AI source_url: https://arize.com/blog/how-to-evaluate-tool-calling-agents final_url: https://arize.com/blog/how-to-evaluate-tool-calling-agents/ status: 200 content_type: text/html; charset=UTF-8 topics: [Tool Selection & Too
- [Tool Invocation - Phoenix](https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation) — `raw/hot-topics-sources/2026-04-10/234-tool-invocation-evaluator-docs.md`
  - 메모: --- title: Tool Invocation - Phoenix source_url: https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation final_url: https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation status: 200 content_type: text/html; charset=utf-8 topics: [Tool Sel
- [Agent evaluation - Arize AX Docs](https://arize.com/docs/ax/evaluate/evaluation-concepts/agent-evaluation) — `raw/hot-topics-sources/2026-04-10/235-agent-tool-selection.md`
  - 메모: Getting agents to work is hard. LLMs are non-deterministic. A bad response upstream leads to a strange response downstream. Agents can take inefficient paths and still get to the right solution. Frameworks make building easier, but debugging harder.An agent is characterized by wh
- [GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub](https://github.com/Arize-ai/phoenix) — `raw/hot-topics-sources/2026-04-10/236-phoenix-github-repository.md`
  - 메모: --- title: GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub source_url: https://github.com/Arize-ai/phoenix final_url: https://github.com/Arize-ai/phoenix status: 200 content_type: text/html; charset=utf-8 topics: [Tool Selection & Tool Invocation Evaluators, Pro

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[multi-turn-agent-evaluation|Multi-Turn Agent Evaluation]]
- [[rubric-based-evals|Rubric-Based Evaluation Frameworks]]
- [[context-engineering|Context Engineering]]
