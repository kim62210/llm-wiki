---
title: RLVR (Reinforcement Learning with Verifiable Rewards)
category: training
page_type: concept
tags: [training, concept, rlvr, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/rlvr.md, raw/hot-topics-sources/2026-04-10/261-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learnin.md, raw/hot-topics-sources/2026-04-10/262-deepseek-r1-incentivizes-reasoning-in-llms-through-reinforcement-learning.md, raw/hot-topics-sources/2026-04-10/263-reinforcement-learning-with-verifiable-rewards-implicitly-incentivizes-correct-r.md, raw/hot-topics-sources/2026-04-10/264-rethinking-exploration-in-rlvr-from-entropy-regularization-to-refinement-via-bid.md, raw/hot-topics-sources/2026-04-10/265-decoupling-reasoning-and-confidence-resurrecting-calibration-in-rlvr.md]
created: 2026-04-10
updated: 2026-04-13
---
# RLVR (Reinforcement Learning with Verifiable Rewards)

이 페이지는 RLVR (Reinforcement Learning with Verifiable Rewards)를 다룬다. 핵심은 정답 검증 가능한 과제에서 보상 신호로 학습시키는 RL 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

정답 검증 가능한 과제에서 보상 신호로 학습시키는 RL 기법.

## 왜 지금 중요한가

[[deepseek-r1-paper|DeepSeek-R1]] 이후 추론 모델 학습의 지배적 패러다임이 되었고, 2026년 현재 수학/코드/과학 등 프로그램적 검증이 가능한 모든 도메인으로 확산 중이다.

## 대표 자료

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning (Nature)](https://www.nature.com/articles/s41586-025-09422-z)
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](https://arxiv.org/abs/2506.14245)
- [Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation](https://arxiv.org/abs/2604.04894)
- [Decoupling Reasoning and Confidence: Resurrecting Calibration in RLVR](https://arxiv.org/abs/2603.09117)

## 실무 관점

RLVR의 검증 가능한 보상 구조는 에이전트 과제 수행에 자연스럽게 적용된다 -- 수학·코드·과학 도메인에서 [[agentic-rl|Agentic RL]] 학습 루프로 이어지며, [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents]]가 다루는 장기 보상 지연(sparse reward) 문제와 직접 연결된다.

## 관련 문서
- [[direct-preference-optimization]]
- [[agentgym-rl-paper]]
- [[deepseek-r1-paper]]
- [[agentic-rl-survey-paper]]

- [[ai-hot-topics-2026-04]]
- [[grpo]]
- [[agentic-rl]]
- [[long-horizon-rl-training-for-agents]]

