---
title: Context Folding & Sub-Trajectory Compression
category: agents
page_type: concept
tags: [agents, concept, context, folding]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/context-folding.md, raw/hot-topics-sources/2026-04-10/029-scaling-long-horizon-llm-agent-via-context-folding.md, raw/hot-topics-sources/2026-04-10/004-agentfold-long-horizon-web-agents-with-proactive-context-management.md, raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md, raw/hot-topics-sources/2026-04-10/001-effective-context-engineering-for-ai-agents.md, raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md]
created: 2026-04-10
updated: 2026-04-10
---
# Context Folding & Sub-Trajectory Compression

에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법.

## 왜 중요한가

2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.

## 대표 레퍼런스

- [Scaling Long-Horizon LLM Agent via Context-Folding (FoldGRPO)](https://arxiv.org/abs/2510.11967)
- [AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699)
- [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615)
- [Effective context engineering for AI agents (Anthropic)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)

## 2026년 4월 큐레이션 요약

- 정의: 에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법.
- 왜 중요한가: 2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×3, anthropic.com×1, trychroma.com×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/context-folding.md`

### source별 핵심 신호

- **[2510.11967] Scaling Long-Horizon LLM Agent via Context-Folding** (`arxiv.org`): https://arxiv.org/abs/2510.11967
  - 메모: Large language model (LLM) agents are fundamentally constrained by context length on long-horizon tasks. We introduce Context-Folding, a framework that empowers agents to actively manage their working context.
- **[2510.24699] AgentFold: Long-Horizon Web Agents with Proactive Context Management** (`arxiv.org`): https://arxiv.org/abs/2510.24699
  - 메모: LLM-based web agents show immense promise for information seeking, yet their effectiveness on long-horizon tasks is hindered by a fundamental trade-off in context management.
- **[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents** (`arxiv.org`): https://arxiv.org/abs/2510.00615
  - 메모: Large language models (LLMs) are increasingly deployed as agents in dynamic, real-world environments, where success requires both reasoning and effective tool use.
- **Effective context engineering for AI agents \ Anthropic** (`anthropic.com`): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - 메모: Effective context engineering for AI agents
- **Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma** (`trychroma.com`): https://www.trychroma.com/research/context-rot
  - 메모: Context Rot: How Increasing Input Tokens Impacts LLM Performance

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents (Multi-Turn RLVR)]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[subagents|Subagents]]
