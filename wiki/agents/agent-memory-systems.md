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

## 해석 포인트

Agent Memory Systems (Episodic / Semantic / Working)은 **에이전트의 상태 지속성과 회수 정확도를 좌우하는 메모리 계층 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×2, github.com×2, openreview.net×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층.
- 왜 중요한가: 2025년 12월 47명의 저자가 참여한 "Memory in the Age of AI Agents" 서베이가 token-level/parametric/latent 분류 체계를 정립했고, ICLR 2026 MemAgents 워크숍이 정식 워크숍으로 채택되며 2026년 1월 이후 메모리 RL 학습 논문이 폭발적으로 증가했다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×2, github.com×2, openreview.net×1

## 핵심 구조

에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층. 에이전트 토픽은 보통 모델 자체보다 **루프 구조, 상태 관리, 작업 분해, 검증 방식**이 핵심이다. 이번 source 묶음도 `arxiv.org×2, github.com×2, openreview.net×1`를 오가며 설계 패턴과 구현 사례를 함께 보여 준다.

## 핵심 포인트

Agent Memory Systems (Episodic / Semantic / Working)는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 이 페이지는 Agent Memory Systems (Episodic / Semantic / Working)를 다룬다. 핵심은 에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arxiv.org×2, github.com×2, openreview.net×1로 분포한다. 연구 신호와 구현체가 같이 보여서 실험 결과와 적용 방법을 연결해 보기 좋다.

## 실무 관점

실무에서는 장기 실행, 상태 관리, 실패 복구, 평가 루프를 함께 설계해야 이 토픽이 효과를 낸다. 즉 개별 아이디어보다 에이전트 시스템 전체의 제약 속에서 읽는 것이 중요하다.

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
