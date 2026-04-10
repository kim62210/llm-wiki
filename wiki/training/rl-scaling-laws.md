---
title: RL Scaling Laws (ScaleRL)
category: training
page_type: concept
tags: [training, concept, scaling, laws, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/rl-scaling-laws.md, raw/hot-topics-sources/2026-04-10/286-the-art-of-scaling-reinforcement-learning-compute-for-llms.md, raw/hot-topics-sources/2026-04-10/287-how-to-scale-rl.md, raw/hot-topics-sources/2026-04-10/288-scaling-laws-for-robotics-and-rl-not-quite-yet.md, raw/hot-topics-sources/2026-04-10/289-scaling-laws-for-value-based-rl.md, raw/hot-topics-sources/2026-04-10/290-what-comes-next-with-reinforcement-learning.md]
created: 2026-04-10
updated: 2026-04-10
---
# RL Scaling Laws (ScaleRL)

이 페이지는 RL Scaling Laws (ScaleRL)를 다룬다. 핵심은 RL 컴퓨트 규모에 따른 성능을 예측 가능한 곡선으로 모델링하는 방법론이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

RL 컴퓨트 규모에 따른 성능을 예측 가능한 곡선으로 모델링하는 방법론.

## 왜 지금 중요한가

Meta 주도의 40만 GPU-시간 규모 연구가 RL을 "예술"에서 "과학"으로 전환시키며, 2026년 post-training 연구의 핵심 프레임워크로 자리잡고 있다.

## 대표 자료

- [The Art of Scaling Reinforcement Learning Compute for LLMs](https://arxiv.org/abs/2510.13786)
- [How to scale RL (Nathan Lambert, Interconnects)](https://www.interconnects.ai/p/the-new-rl-scaling-laws)
- [Scaling laws for robotics & RL: Not quite yet (Interconnects)](https://www.interconnects.ai/p/scaling-rl-axes)
- [Scaling Laws for Value-Based RL](https://value-scaling.github.io/)
- [What comes next with reinforcement learning (Interconnects)](https://www.interconnects.ai/p/what-comes-next-with-reinforcement)

## 2026년 4월 큐레이션 요약

- 정의: RL 컴퓨트 규모에 따른 성능을 예측 가능한 곡선으로 모델링하는 방법론.
- 왜 중요한가: Meta 주도의 40만 GPU-시간 규모 연구가 RL을 "예술"에서 "과학"으로 전환시키며, 2026년 post-training 연구의 핵심 프레임워크로 자리잡고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: interconnects.ai×3, arxiv.org×1, value-scaling.github.io×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/rl-scaling-laws.md`

### source별 핵심 신호

- **[2510.13786] The Art of Scaling Reinforcement Learning Compute for LLMs** (`arxiv.org`): https://arxiv.org/abs/2510.13786
  - 메모: Reinforcement learning (RL) has become central to training large language models (LLMs), yet the field lacks predictive scaling methodologies comparable to those established for pre-training.
- **How to scale RL - by Nathan Lambert - Interconnects AI** (`interconnects.ai`): https://www.interconnects.ai/p/the-new-rl-scaling-laws
  - 메모: 1. I’ll be in SF this week for the PyTorch conference (22-23), AI Infra Summit (21st), and other local events. Come say hi.
- **Scaling laws for robotics & RL: Not quite yet** (`interconnects.ai`): https://www.interconnects.ai/p/scaling-rl-axes
  - 메모: Co-authored another blog post on dialog agents: What Makes a Dialog Agent Useful?
- **Scaling Laws for Value-Based RL** (`value-scaling.github.io`): https://value-scaling.github.io
  - 메모: In the era of large-scale AI, it is important to prototype new training methodologies at small scales before running at large scales or datasets.
- **What comes next with reinforcement learning** (`interconnects.ai`): https://www.interconnects.ai/p/what-comes-next-with-reinforcement
  - 메모: First, some housekeeping. The blog’s paid discord (access or upgrade here) has been very active and high-quality recently, especially parsing recent AI training tactics like RLVR for agents/planning.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[on-policy-distillation]]
- [[corpus-grounded-self-play]]
