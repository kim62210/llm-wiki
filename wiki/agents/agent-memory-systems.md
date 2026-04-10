---
title: Agent Memory Systems (Episodic / Semantic / Working)
category: agents
page_type: concept
tags: [agents, concept, agent, memory, systems, agent-architecture]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/agent-memory-systems.md, raw/hot-topics-sources/2026-04-10/016-memory-in-the-age-of-ai-agents.md, raw/hot-topics-sources/2026-04-10/017-iclr-2026-memagents-workshop-proposal.md, raw/hot-topics-sources/2026-04-10/018-agent-r-training-language-model-agents-to-reflect-via-iterative-self-training.md, raw/hot-topics-sources/2026-04-10/019-agent-memory-paper-list.md, raw/hot-topics-sources/2026-04-10/020-awesome-memory-for-agents.md]
created: 2026-04-10
updated: 2026-04-10
---
# Agent Memory Systems (Episodic / Semantic / Working)

이 페이지는 Agent Memory Systems (Episodic / Semantic / Working)를 다룬다. 핵심은 에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층.

## 왜 지금 중요한가

2025년 12월 47명의 저자가 참여한 "Memory in the Age of AI Agents" 서베이가 token-level/parametric/latent 분류 체계를 정립했고, ICLR 2026 MemAgents 워크숍이 정식 워크숍으로 채택되며 2026년 1월 이후 메모리 RL 학습 논문이 폭발적으로 증가했다.

## 대표 자료

- [Memory in the Age of AI Agents (Survey)](https://arxiv.org/abs/2512.13564)
- [ICLR 2026 MemAgents Workshop Proposal](https://openreview.net/pdf?id=U51WxL382H)
- [Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training](https://arxiv.org/abs/2501.11425)
- [Agent Memory Paper List (GitHub)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)
- [Awesome-Memory-for-Agents (Tsinghua C3I)](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents)

## 2026년 4월 큐레이션 요약

- 정의: 에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층.
- 왜 중요한가: 2025년 12월 47명의 저자가 참여한 "Memory in the Age of AI Agents" 서베이가 token-level/parametric/latent 분류 체계를 정립했고, ICLR 2026 MemAgents 워크숍이 정식 워크숍으로 채택되며 2026년 1월 이후 메모리 RL 학습 논문이 폭발적으로 증가했다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×2, github.com×2, openreview.net×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/agent-memory-systems.md`

### source별 핵심 신호

- **[2512.13564] Memory in the Age of AI Agents** (`arxiv.org`): https://arxiv.org/abs/2512.13564
  - 메모: Memory has emerged, and will continue to remain, a core capability of foundation model-based agents.
- **ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems (MemAgents)** (`openreview.net`): https://openreview.net/forum?id=U51WxL382H
  - 메모: ** Agentic systems are already being deployed in high-stakes settings such as robotics, autonomous web interaction, and software maintenance, and their capabilities ultimately hinge on memory.
- **[2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training** (`arxiv.org`): https://arxiv.org/abs/2501.11425
  - 메모: Large Language Models (LLMs) agents are increasingly pivotal for addressing complex tasks in interactive environments.
- **GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of "Memory in the Age of AI Agents: A Survey" · GitHub** (`github.com`): https://github.com/Shichun-Liu/Agent-Memory-Paper-List
  - 메모: To see all available qualifiers, see our documentation.
- **GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub** (`github.com`): https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents
  - 메모: To see all available qualifiers, see our documentation.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[generator-evaluator-architecture]]
- [[agent-skills]]
