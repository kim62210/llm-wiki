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

## 해석 포인트

Hierarchical Planning with Agent Trees은 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×3, github.com×1, anthropic.com×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 복잡한 목표를 동적으로 구성되는 에이전트 트리로 분해하고 제어 흐름 노드로 서브에이전트들을 조정하는 계획 방식.
- 왜 중요한가: AAMAS 2026에 채택된 ReAcTree가 Qwen 2.5 72B로 ReAct(31%) 대비 61% 성공률을 달성하며 트리 기반 분해의 우월성을 입증했고, Plan-and-Act, Plan-Then-Execute, 다층 메모리 계획기 등이 동시 등장하면서 평면적 ReAct 루프의 한계가 명확해졌다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×3, github.com×1, anthropic.com×1

## 핵심 구조

복잡한 목표를 동적으로 구성되는 에이전트 트리로 분해하고 제어 흐름 노드로 서브에이전트들을 조정하는 계획 방식. 에이전트 토픽은 보통 모델 자체보다 **루프 구조, 상태 관리, 작업 분해, 검증 방식**이 핵심이다. 이번 source 묶음도 `arxiv.org×3, github.com×1, anthropic.com×1`를 오가며 설계 패턴과 구현 사례를 함께 보여 준다.

## 핵심 포인트

Hierarchical Planning with Agent Trees는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 복잡한 목표를 동적으로 구성되는 에이전트 트리로 분해하고 제어 흐름 노드로 서브에이전트들을 조정하는 계획 방식.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arxiv.org×3, anthropic.com×1, github.com×1로 분포한다. 연구·공식문서·구현체가 모두 섞여 있어서 개념과 운영을 함께 추적하기 좋다.

## 실무 관점

실무에서는 장기 실행, 상태 관리, 실패 복구, 평가 루프를 함께 설계해야 이 토픽이 효과를 낸다. 즉 개별 아이디어보다 에이전트 시스템 전체의 제약 속에서 읽는 것이 중요하다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/agent-trees.md`

### source별 핵심 신호

- **[2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning** (`arxiv.org`): https://arxiv.org/abs/2511.02424
  - 메모: Recent advancements in large language models (LLMs) have enabled significant progress in decision-making and task planning for embodied autonomous agents.
- **[2503.09572] Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks** (`arxiv.org`): https://arxiv.org/abs/2503.09572
  - 메모: Large language models (LLMs) have shown remarkable advancements in enabling language agents to tackle simple tasks. However, applying them for complex, multi-step, long-horizon tasks remains a challenge.
- **[2506.18096] Deep Research Agents: A Systematic Examination And Roadmap** (`arxiv.org`): https://arxiv.org/abs/2506.18096
  - 메모: The rapid progress of Large Language Models (LLMs) has given rise to a new category of autonomous AI systems, referred to as Deep Research (DR) agents.
- **GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains. · GitHub** (`github.com`): https://github.com/SkyworkAI/DeepResearchAgent
  - 메모: To see all available qualifiers, see our documentation.
- **How we built our multi-agent research system \ Anthropic** (`anthropic.com`): https://www.anthropic.com/engineering/multi-agent-research-system
  - 메모: How we built our multi-agent research system


## source 종합 해석

예를 들어 source note는 Recent advancements in large language models (LLMs) have enabled significant progress in decision-making and task planning for embodied autonomous agents.

또 다른 source는 Large language models (LLMs) have shown remarkable advancements in enabling language agents to tackle simple tasks. However, applying them for complex, multi-step, long-horizon tasks remains a challenge.

즉, 이 토픽이 중요한 이유는 `AAMAS 2026에 채택된 ReAcTree가 Qwen 2.5 72B로 ReAct(31%) 대비 61% 성공률을 달성하며 트리 기반 분해의 우월성을 입증했고, Plan-and-Act, Plan-Then-Execute, 다층 메모리 계획기 등이 동시 등장하면서 평면적 ReAct 루프의 한계가 명확해졌다.`라는 한 문장보다, 여러 source가 같은 문제를 서로 다른 층위(개념·측정·구현)에서 지지한다는 데 있다.

함께 읽을 문서로는 2026년 4월 AI 개발 핫토픽 100선, Context Folding & Sub-Trajectory Compression, Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- source note가 추상 개념/실험 결과/운영 사례 중 어디에 치우쳐 있는지 보면, 이 토픽을 실무에서 어떻게 다뤄야 하는지가 드러난다.
- `AAMAS 2026에 채택된 ReAcTree가 Qwen 2.5 72B로 ReAct(31%) 대비 61% 성공률을 달성하며 트리 기반 분해의 우월성을 입증했고, Plan-and-Act, Plan-Then-Execute, 다층 메모리 계획기 등이 동시 등장하면서 평면적 ReAct 루프의 한계가 명확해졌다.`라는 중요도 설명은 보통 과장되기 쉬우므로, 구체적 수치·벤치마크·운영 사례를 같이 확인해야 한다.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[context-folding|Context Folding & Sub-Trajectory Compression]]
- [[long-horizon-agent-benchmarks|Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)]]
- [[subagents|Subagents]]
