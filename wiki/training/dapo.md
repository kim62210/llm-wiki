---
title: DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)
category: training
page_type: concept
tags: [training, concept, dapo, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/dapo.md, raw/hot-topics-sources/2026-04-10/271-dapo-an-open-source-llm-reinforcement-learning-system-at-scale.md, raw/hot-topics-sources/2026-04-10/272-dapo-project-page.md, raw/hot-topics-sources/2026-04-10/273-dapo-github-repository.md, raw/hot-topics-sources/2026-04-10/274-vapo-efficient-and-reliable-reinforcement-learning-for-advanced-reasoning-tasks.md, raw/hot-topics-sources/2026-04-10/275-recent-reasoning-research-grpo-tweaks-base-model-rl-and-data-curation.md]
created: 2026-04-10
updated: 2026-04-13
---
# DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)

이 페이지는 DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)를 다룬다. 핵심은 Clip-Higher, Dynamic Sampling 등 4가지 기법을 결합한 대규모 추론 RL 시스템이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

Clip-Higher, Dynamic Sampling 등 4가지 기법을 결합한 대규모 추론 RL 시스템.

## 왜 지금 중요한가

ByteDance가 완전 오픈소스로 공개하며 Qwen2.5-32B에서 AIME24 50점을 달성, [[deepseek-r1-paper|DeepSeek-R1]]-Zero를 절반의 스텝으로 추월해 현재 오픈 RL 재현의 기준점이다.

## 대표 자료

- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- [DAPO Project Page](https://dapo-sia.github.io/)
- [DAPO GitHub Repository](https://github.com/BytedTsinghua-SIA/DAPO)
- [VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks](https://arxiv.org/abs/2504.05118)
- [Recent reasoning research: GRPO tweaks, base model RL, and data curation (Interconnects)](https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo)

## 실무 관점

DAPO의 Dynamic Sampling 설계는 코딩 에이전트처럼 결과 검증이 명확한 환경에서의 [[agentic-rl|Agentic RL]]과 맞닿아 있으며, 대규모 오픈소스 재현 기준점으로서 [[long-horizon-rl-training-for-agents|Long-Horizon RL 에이전트 학습]]의 출발점으로 활용된다.

## 관련 문서
- [[direct-preference-optimization]]

- [[ai-hot-topics-2026-04]]
- [[grpo]]
- [[process-reward-models]]
- [[agentic-rl]]
- [[long-horizon-rl-training-for-agents]]

