---
title: GRPO (Group Relative Policy Optimization)
category: training
page_type: concept
tags: [training, concept, grpo, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/grpo.md, raw/hot-topics-sources/2026-04-10/266-deepseekmath-pushing-the-limits-of-mathematical-reasoning.md, raw/hot-topics-sources/2026-04-10/267-demystifying-group-relative-[[rlhf-pipeline|policy]]-optimization-its-policy-gradient-is-a-u-stati.md, raw/hot-topics-sources/2026-04-10/268-training-free-group-relative-policy-optimization.md, raw/hot-topics-sources/2026-04-10/269-scaf-grpo-scaffolded-group-relative-policy-optimization-for-enhancing-llm-reason.md, raw/hot-topics-sources/2026-04-10/270-understanding-grpo-ppo-without-the-critic.md]
created: 2026-04-10
updated: 2026-04-13
---
# GRPO (Group Relative Policy Optimization)

이 페이지는 GRPO (Group Relative Policy Optimization)를 다룬다. 핵심은 크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형.

## 왜 지금 중요한가

DeepSeek-R1이 채택한 이후 오픈소스 추론 모델 학습의 표준이 되었고, 2026년에는 Scaf-GRPO, Training-Free GRPO, CPPO 등 수많은 파생 기법이 쏟아지고 있다.

## 대표 자료

- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO 원전)](https://arxiv.org/pdf/2402.03300)
- [Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic](https://arxiv.org/abs/2603.01162)
- [Training-Free Group Relative Policy Optimization](https://arxiv.org/abs/2510.08191)
- [Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning](https://arxiv.org/abs/2510.19807)
- [Understanding GRPO: PPO without the critic (HuggingFace blog)](https://huggingface.co/blog/garg-aayush/derive-grpo-loss)

## 실무 관점

특히 GRPO 같은 그룹 보상 정규화 기법은 에이전트 시스템에서의 [[agentic-rl|Agentic RL]] 학습 루프로 직접 확장된다 -- 장기 과제 에이전트를 학습시키려면 [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents]] 방법론과의 결합이 필요하다.

## 관련 문서
- [[rejection-sampling-sft]] -- 거부 샘플링 미세조정 (Rejection Sampling Fine-Tuning)
- [[malt-paper]] -- MALT: Improving Reasoning with Multi-Agent LLM Training
- [[langmarl-paper]] -- LangMARL: Natural Language Multi-Agent Reinforcement Learning
- [[mit-training-efficiency]]
- [[direct-preference-optimization]]
- [[deepseek-r1-paper]]

- [[ai-hot-topics-2026-04]]
- [[rlvr]]
- [[dapo]]
- [[agentic-rl]]
- [[long-horizon-rl-training-for-agents]]

