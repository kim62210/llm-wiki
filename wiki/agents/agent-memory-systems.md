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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 2건, github.com 2건, openreview.net 1건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/agent-memory-systems.md`
- [[2512.13564] Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) — `raw/hot-topics-sources/2026-04-10/016-memory-in-the-age-of-ai-agents.md`
  - 메모: --- title: [2512.13564] Memory in the Age of AI Agents source_url: https://arxiv.org/abs/2512.13564 final_url: https://arxiv.org/abs/2512.13564 status: 200 content_type: text/html; charset=utf-8 topics: [Agent Memory Systems (Episodic / Semantic / Working)] sections: [Agent Archi
- [ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems (MemAgents)](https://openreview.net/forum?id=U51WxL382H) — `raw/hot-topics-sources/2026-04-10/017-iclr-2026-memagents-workshop-proposal.md`
  - 메모: **Keywords:**Agentic Systems, LLM-Based Agents, Explicit and In-Weights Memory, Neuroscience-Inspired Memory Architecture **TL;DR:**We propose a workshop devoted to memory layer for LLM-based agentic systems, bridging interdisciplinary researchers across reinforcement learning, m
- [[2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training](https://arxiv.org/abs/2501.11425) — `raw/hot-topics-sources/2026-04-10/018-agent-r-training-language-model-agents-to-reflect-via-iterative-self-training.md`
  - 메모: --- title: [2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training source_url: https://arxiv.org/abs/2501.11425 final_url: https://arxiv.org/abs/2501.11425 status: 200 content_type: text/html; charset=utf-8 topics: [Agent Memory Systems (Episod
- [GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of "Memory in the Age of AI Agents: A Survey" · GitHub](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) — `raw/hot-topics-sources/2026-04-10/019-agent-memory-paper-list.md`
  - 메모: --- title: GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of "Memory in the Age of AI Agents: A Survey" · GitHub source_url: https://github.com/Shichun-Liu/Agent-Memory-Paper-List final_url: https://github.com/Shichun-Liu/Agent-Memory-Paper-List status: 200 content_
- [GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) — `raw/hot-topics-sources/2026-04-10/020-awesome-memory-for-agents.md`
  - 메모: --- title: GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub source_url: https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents final_url: https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents status: 200 content

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[generator-evaluator-architecture]]
- [[agent-skills]]
