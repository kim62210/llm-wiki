---
title: Orchestrator-Worker Multi-Agent Pattern
category: agents
page_type: concept
tags: [agents, concept, orchestrator, worker, pattern]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Orchestrator-Worker Multi-Agent Pattern

리드 에이전트가 작업을 분해해 병렬 서브에이전트에게 위임하고 결과를 합성하는 분산형 에이전트 아키텍처.

## 왜 중요한가

Anthropic이 Claude의 Research 기능 백엔드로 공개한 이 패턴이 단일 Opus 4 대비 90.2% 향상을 보인 이후 사실상 표준이 되었고, 2026년 4월 8일 출시된 Claude Managed Agents는 이 패턴을 매니지드 인프라로 제품화했다.

## 대표 레퍼런스

- [How we built our multi-agent research system (Anthropic)](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Orchestrator-Workers Workflow Cookbook (Anthropic)](https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/orchestrator_workers.ipynb)
- [Create custom subagents (Claude Code Docs)](https://code.claude.com/docs/en/sub-agents)
- [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)
- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[context-engineering|Context Engineering for Long-Horizon Agents]]
- [[generator-evaluator-architecture|Generator-Evaluator Harness Architecture]]
- [[subagents|Subagents]]
