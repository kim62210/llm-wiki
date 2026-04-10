---
title: Long-Horizon RL Training for Agents (Multi-Turn RLVR)
category: agents
page_type: concept
tags: [agents, concept, long, horizon, rl, training, for]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/long-horizon-rl-training-for-agents.md, raw/hot-topics-sources/2026-04-10/010-the-landscape-of-agentic-reinforcement-learning-for-llms-a-survey.md, raw/hot-topics-sources/2026-04-10/026-reinforcement-learning-for-long-horizon-interactive-llm-agents.md, raw/hot-topics-sources/2026-04-10/027-agentgym-rl-training-llm-agents-for-long-horizon-decision-making-through-multi-t.md, raw/hot-topics-sources/2026-04-10/014-reveal-self-evolving-code-agents-via-iterative-generation-verification.md, raw/hot-topics-sources/2026-04-10/028-research-learning-to-reason-with-search-for-llms-via-reinforcement-learning.md]
created: 2026-04-10
updated: 2026-04-10
---
# Long-Horizon RL Training for Agents (Multi-Turn RLVR)

멀티 턴 환경에서 검증 가능한 보상으로 에이전트의 도구 사용·계획·자기수정 능력을 직접 학습시키는 강화학습 기법.

## 왜 중요한가

2026년 3월 NVIDIA의 ProRL Agent (Rollout-as-a-Service), AgentGym-RL, ScalingInter-RL 등 멀티 턴 RL 인프라가 동시 공개되었고, 500편 이상을 종합한 "Landscape of Agentic RL" 서베이가 학습 가능한 에이전트로의 패러다임 시프트를 정식화하면서 학계·산업계 모두 RL 기반 에이전트 훈련을 1순위 연구 과제로 격상시켰다.

## 대표 레퍼런스

- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547)
- [Reinforcement Learning for Long-Horizon Interactive LLM Agents (LOOP)](https://arxiv.org/abs/2502.01600)
- [AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn RL](https://arxiv.org/abs/2509.08755)
- [ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification](https://arxiv.org/abs/2506.11442)
- [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.19470)

## 2026년 4월 큐레이션 요약

- 정의: 멀티 턴 환경에서 검증 가능한 보상으로 에이전트의 도구 사용·계획·자기수정 능력을 직접 학습시키는 강화학습 기법.
- 왜 중요한가: 2026년 3월 NVIDIA의 ProRL Agent (Rollout-as-a-Service), AgentGym-RL, ScalingInter-RL 등 멀티 턴 RL 인프라가 동시 공개되었고, 500편 이상을 종합한 "Landscape of Agentic RL" 서베이가 학습 가능한 에이전트로의 패러다임 시프트를 정식화하면서 학계·산업계 모두 RL 기반 에이전트 훈련을 1순위 연구 과제로 격상시켰다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×5

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/long-horizon-rl-training-for-agents.md`

### source별 핵심 신호

- **[2509.02547] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey** (`arxiv.org`): https://arxiv.org/abs/2509.02547
  - 메모: The emergence of agentic reinforcement learning (Agentic RL) marks a paradigm shift from conventional reinforcement learning applied to large language models (LLM RL), reframing LLMs from passive sequence generators into
- **[2502.01600] Reinforcement Learning for Long-Horizon Interactive LLM Agents** (`arxiv.org`): https://arxiv.org/abs/2502.01600
  - 메모: Interactive digital agents (IDAs) leverage APIs of stateful digital environments to perform tasks in response to user requests.
- **[2509.08755] AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning** (`arxiv.org`): https://arxiv.org/abs/2509.08755
  - 메모: Developing autonomous LLM agents capable of making a series of intelligent decisions to solve complex, real-world tasks is a fast-evolving frontier.
- **[2506.11442] ReVeal: Self-Evolving Code Agents via Reliable Self-Verification** (`arxiv.org`): https://arxiv.org/abs/2506.11442
  - 메모: Reinforcement learning with verifiable rewards (RLVR) has advanced the reasoning capabilities of large language models.
- **[2503.19470] ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning** (`arxiv.org`): https://arxiv.org/abs/2503.19470
  - 메모: Large Language Models (LLMs) have shown remarkable capabilities in reasoning, exemplified by the success of OpenAI-o1 and DeepSeek-R1.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agent-skills|Agent Skills]]
- [[context-folding|Context Folding & Sub-Trajectory Compression]]
- [[subagents|Subagents]]
