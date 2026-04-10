---
title: Hierarchical Planning with Agent Trees
category: agents
page_type: concept
tags: [agents, concept, agent, trees]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/agent-trees.md, raw/hot-topics-sources/2026-04-10/030-reactree-hierarchical-llm-agent-trees-with-control-flow-for-long-horizon-task-pl.md, raw/hot-topics-sources/2026-04-10/031-plan-and-act-improving-planning-of-agents-for-long-horizon-tasks.md, raw/hot-topics-sources/2026-04-10/032-deep-research-agents-a-systematic-examination-and-roadmap.md, raw/hot-topics-sources/2026-04-10/033-skyworkai-deepresearchagent.md, raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md]
created: 2026-04-10
updated: 2026-04-10
---
# Hierarchical Planning with Agent Trees

복잡한 목표를 동적으로 구성되는 에이전트 트리로 분해하고 제어 흐름 노드로 서브에이전트들을 조정하는 계획 방식.

## 왜 중요한가

AAMAS 2026에 채택된 ReAcTree가 Qwen 2.5 72B로 ReAct(31%) 대비 61% 성공률을 달성하며 트리 기반 분해의 우월성을 입증했고, Plan-and-Act, Plan-Then-Execute, 다층 메모리 계획기 등이 동시 등장하면서 평면적 ReAct 루프의 한계가 명확해졌다.

## 대표 레퍼런스

- [ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning](https://arxiv.org/abs/2511.02424)
- [Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](https://arxiv.org/abs/2503.09572)
- [Deep Research Agents: A Systematic Examination And Roadmap](https://arxiv.org/abs/2506.18096)
- [SkyworkAI/DeepResearchAgent (Hierarchical Multi-Agent System)](https://github.com/SkyworkAI/DeepResearchAgent)
- [How we built our multi-agent research system (Anthropic)](https://www.anthropic.com/engineering/multi-agent-research-system)

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/agent-trees.md`
- raw source: `raw/hot-topics-sources/2026-04-10/030-reactree-hierarchical-llm-agent-trees-with-control-flow-for-long-horizon-task-pl.md`
- raw source: `raw/hot-topics-sources/2026-04-10/031-plan-and-act-improving-planning-of-agents-for-long-horizon-tasks.md`
- raw source: `raw/hot-topics-sources/2026-04-10/032-deep-research-agents-a-systematic-examination-and-roadmap.md`
- raw source: `raw/hot-topics-sources/2026-04-10/033-skyworkai-deepresearchagent.md`
- raw source: `raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md`

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[context-folding|Context Folding & Sub-Trajectory Compression]]
- [[long-horizon-agent-benchmarks|Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)]]
- [[subagents|Subagents]]
