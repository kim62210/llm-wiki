---
title: GRPO (Group Relative Policy Optimization)
category: training
page_type: concept
tags: [training, concept, grpo, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
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

## 2026년 4월 핫토픽 맥락

DeepSeek-R1이 채택한 이후 오픈소스 추론 모델 학습의 표준이 되었고, 2026년에는 Scaf-GRPO, Training-Free GRPO, CPPO 등 수많은 파생 기법이 쏟아지고 있다.

### 추가 레퍼런스

- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO 원전)](https://arxiv.org/pdf/2402.03300)
- [Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic](https://arxiv.org/abs/2603.01162)
- [Training-Free Group Relative Policy Optimization](https://arxiv.org/abs/2510.08191)
- [Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning](https://arxiv.org/abs/2510.19807)
- [Understanding GRPO: PPO without the critic (HuggingFace blog)](https://huggingface.co/blog/garg-aayush/derive-grpo-loss)

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[rlvr]]
- [[dapo]]
