---
title: DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)
category: training
page_type: concept
tags: [training, concept, dapo, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/dapo.md, raw/hot-topics-sources/2026-04-10/271-dapo-an-open-source-llm-reinforcement-learning-system-at-scale.md, raw/hot-topics-sources/2026-04-10/272-dapo-project-page.md, raw/hot-topics-sources/2026-04-10/273-dapo-github-repository.md, raw/hot-topics-sources/2026-04-10/274-vapo-efficient-and-reliable-reinforcement-learning-for-advanced-reasoning-tasks.md, raw/hot-topics-sources/2026-04-10/275-recent-reasoning-research-grpo-tweaks-base-model-rl-and-data-curation.md]
created: 2026-04-10
updated: 2026-04-10
---
# DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)

이 페이지는 DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)를 다룬다. 핵심은 Clip-Higher, Dynamic Sampling 등 4가지 기법을 결합한 대규모 추론 RL 시스템이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

Clip-Higher, Dynamic Sampling 등 4가지 기법을 결합한 대규모 추론 RL 시스템.

## 왜 지금 중요한가

ByteDance가 완전 오픈소스로 공개하며 Qwen2.5-32B에서 AIME24 50점을 달성, DeepSeek-R1-Zero를 절반의 스텝으로 추월해 현재 오픈 RL 재현의 기준점이다.

## 대표 자료

- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- [DAPO Project Page](https://dapo-sia.github.io/)
- [DAPO GitHub Repository](https://github.com/BytedTsinghua-SIA/DAPO)
- [VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks](https://arxiv.org/abs/2504.05118)
- [Recent reasoning research: GRPO tweaks, base model RL, and data curation (Interconnects)](https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 2건, dapo-sia.github.io 1건, github.com 1건
- source 조합: 구현체

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/dapo.md`
- [[2503.14476] DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476) — `raw/hot-topics-sources/2026-04-10/271-dapo-an-open-source-llm-reinforcement-learning-system-at-scale.md`
  - 메모: --- title: [2503.14476] DAPO: An Open-Source LLM Reinforcement Learning System at Scale source_url: https://arxiv.org/abs/2503.14476 final_url: https://arxiv.org/abs/2503.14476 status: 200 content_type: text/html; charset=utf-8 topics: [DAPO (Decoupled Clip and Dynamic Sampling P
- [DAPO](https://dapo-sia.github.io) — `raw/hot-topics-sources/2026-04-10/272-dapo-project-page.md`
  - 메모: --- title: DAPO source_url: https://dapo-sia.github.io final_url: https://dapo-sia.github.io status: 200 content_type: text/html; charset=utf-8 topics: [DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)] sections: [Training & Post-training] fetched_at: 2026-04-10T01:
- [GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub](https://github.com/BytedTsinghua-SIA/DAPO) — `raw/hot-topics-sources/2026-04-10/273-dapo-github-repository.md`
  - 메모: --- title: GitHub - BytedTsinghua-SIA/DAPO: An Open-source RL System from ByteDance Seed and Tsinghua AIR · GitHub source_url: https://github.com/BytedTsinghua-SIA/DAPO final_url: https://github.com/BytedTsinghua-SIA/DAPO status: 200 content_type: text/html; charset=utf-8 topics:
- [[2504.05118] VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks](https://arxiv.org/abs/2504.05118) — `raw/hot-topics-sources/2026-04-10/274-vapo-efficient-and-reliable-reinforcement-learning-for-advanced-reasoning-tasks.md`
  - 메모: --- title: [2504.05118] VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks source_url: https://arxiv.org/abs/2504.05118 final_url: https://arxiv.org/abs/2504.05118 status: 200 content_type: text/html; charset=utf-8 topics: [DAPO (Decoupled Clip and D
- [Recent reasoning research: GRPO tweaks, base model RL, and data curation](https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo) — `raw/hot-topics-sources/2026-04-10/275-recent-reasoning-research-grpo-tweaks-base-model-rl-and-data-curation.md`
  - 메모: --- title: Recent reasoning research: GRPO tweaks, base model RL, and data curation source_url: https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo final_url: https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo status: 200 content_type: text/html; 

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[grpo]]
- [[process-reward-models]]
