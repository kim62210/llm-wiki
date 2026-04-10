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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 4건, huggingface.co 1건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/grpo.md`
- [266-deepseekmath-pushing-the-limits-of-mathematical-reasoning](https://arxiv.org/pdf/2402.03300) — `raw/hot-topics-sources/2026-04-10/266-deepseekmath-pushing-the-limits-of-mathematical-reasoning.md`
  - 메모: --- title: DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO 원전) source_url: https://arxiv.org/pdf/2402.03300 final_url: https://arxiv.org/pdf/2402.03300 status: 200 content_type: application/pdf topics: [GRPO (Group Relative Policy Optimization)] sections: [Traini
- [[2603.01162] Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic](https://arxiv.org/abs/2603.01162) — `raw/hot-topics-sources/2026-04-10/267-demystifying-group-relative-policy-optimization-its-policy-gradient-is-a-u-stati.md`
  - 메모: --- title: [2603.01162] Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic source_url: https://arxiv.org/abs/2603.01162 final_url: https://arxiv.org/abs/2603.01162 status: 200 content_type: text/html; charset=utf-8 topics: [GRPO (Group Relative 
- [[2510.08191] Training-Free Group Relative Policy Optimization](https://arxiv.org/abs/2510.08191) — `raw/hot-topics-sources/2026-04-10/268-training-free-group-relative-policy-optimization.md`
  - 메모: --- title: [2510.08191] Training-Free Group Relative Policy Optimization source_url: https://arxiv.org/abs/2510.08191 final_url: https://arxiv.org/abs/2510.08191 status: 200 content_type: text/html; charset=utf-8 topics: [GRPO (Group Relative Policy Optimization)] sections: [Trai
- [[2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning](https://arxiv.org/abs/2510.19807) — `raw/hot-topics-sources/2026-04-10/269-scaf-grpo-scaffolded-group-relative-policy-optimization-for-enhancing-llm-reason.md`
  - 메모: --- title: [2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning source_url: https://arxiv.org/abs/2510.19807 final_url: https://arxiv.org/abs/2510.19807 status: 200 content_type: text/html; charset=utf-8 topics: [GRPO (Group Relative P
- [Understanding GRPO: PPO without the critic](https://huggingface.co/blog/garg-aayush/derive-grpo-loss) — `raw/hot-topics-sources/2026-04-10/270-understanding-grpo-ppo-without-the-critic.md`
  - 메모: --- title: Understanding GRPO: PPO without the critic source_url: https://huggingface.co/blog/garg-aayush/derive-grpo-loss final_url: https://huggingface.co/blog/garg-aayush/derive-grpo-loss status: 200 content_type: text/html; charset=utf-8 topics: [GRPO (Group Relative Policy O

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[rlvr]]
- [[dapo]]
