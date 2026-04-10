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

## 해석 포인트

GRPO (Group Relative Policy Optimization)은 **학습 데이터·보상·안정성의 트레이드오프를 다루는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×4, huggingface.co×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 학습 안정성, 보상 품질, compute 효율, 일반화를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형.
- 왜 중요한가: DeepSeek-R1이 채택한 이후 오픈소스 추론 모델 학습의 표준이 되었고, 2026년에는 Scaf-GRPO, Training-Free GRPO, CPPO 등 수많은 파생 기법이 쏟아지고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×4, huggingface.co×1

## 핵심 메커니즘

크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형. 이 유형의 topic은 보통 하나의 제품보다 **반복 가능한 패턴 / 평가 기준 / 설계 trade-off**로 읽는 편이 유용하다. 이번 source 묶음에서도 `arxiv.org, huggingface.co`가 함께 나오면서 개념, 구현, 평가가 연결되어 있다.

## 핵심 포인트

GRPO (Group Relative Policy Optimization)는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 이 페이지는 GRPO (Group Relative Policy Optimization)를 다룬다. 핵심은 크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arxiv.org×4, huggingface.co×1로 분포한다. 연구 논문 비중이 높아 메커니즘·평가·한계 쪽 정보가 중심이다.

## 실무 관점

학습/후학습 기법은 이름보다 목적 함수와 검증 방식이 중요하다. 보상 신호를 어떻게 만들고 어떤 실패 모드를 줄이는지, 그리고 추론 성능과 운영 비용이 어떻게 바뀌는지를 함께 봐야 실무 의미가 생긴다.

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
