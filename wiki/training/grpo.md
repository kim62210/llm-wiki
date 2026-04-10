---
title: GRPO (Group Relative Policy Optimization)
category: training
page_type: concept
tags: [training, concept, grpo, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/grpo.md, raw/hot-topics-sources/2026-04-10/266-deepseekmath-pushing-the-limits-of-mathematical-reasoning.md, raw/hot-topics-sources/2026-04-10/267-demystifying-group-relative-policy-optimization-its-policy-gradient-is-a-u-stati.md, raw/hot-topics-sources/2026-04-10/268-training-free-group-relative-policy-optimization.md, raw/hot-topics-sources/2026-04-10/269-scaf-grpo-scaffolded-group-relative-policy-optimization-for-enhancing-llm-reason.md, raw/hot-topics-sources/2026-04-10/270-understanding-grpo-ppo-without-the-critic.md]
created: 2026-04-10
updated: 2026-04-10
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

## 2026년 4월 큐레이션 요약

- 정의: 크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형.
- 왜 중요한가: DeepSeek-R1이 채택한 이후 오픈소스 추론 모델 학습의 표준이 되었고, 2026년에는 Scaf-GRPO, Training-Free GRPO, CPPO 등 수많은 파생 기법이 쏟아지고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×4, huggingface.co×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/grpo.md`

### source별 핵심 신호

- **DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO 원전)** (`arxiv.org`): https://arxiv.org/pdf/2402.03300
  - 메모: a#A%áÀß¯«ÀÌjDÕå²»«ífðãc;ZæÕÁÌ«¶­®MfGÑÏ}í
- **[2603.01162] Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic** (`arxiv.org`): https://arxiv.org/abs/2603.01162
  - 메모: Group relative policy optimization (GRPO), a core methodological component of DeepSeekMath and DeepSeek-R1, has emerged as a cornerstone for scaling reasoning capabilities of large language models.
- **[2510.08191] Training-Free Group Relative Policy Optimization** (`arxiv.org`): https://arxiv.org/abs/2510.08191
  - 메모: Recent advances in Large Language Model (LLM) agents have demonstrated their promising general capabilities.
- **[2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning** (`arxiv.org`): https://arxiv.org/abs/2510.19807
  - 메모: Reinforcement learning from verifiable rewards has emerged as a powerful technique for enhancing the complex reasoning abilities of Large Language Models (LLMs).
- **Understanding GRPO: PPO without the critic** (`huggingface.co`): https://huggingface.co/blog/garg-aayush/derive-grpo-loss
  - 메모: In my previous posts, I worked through the derivations of PPO and DPO for LLM post-training. PPO gave us a full-fledged RL approach with clipped surrogate objectives, value functions and GAE-based advantage estimation.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[rlvr]]
- [[dapo]]
