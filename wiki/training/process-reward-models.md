---
title: Process Reward Models (PRM) 재부상
category: training
page_type: concept
tags: [training, concept, process, reward, models, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/process-reward-models.md, raw/hot-topics-sources/2026-04-10/276-process-reward-models-that-think.md, raw/hot-topics-sources/2026-04-10/277-r-prm-reasoning-driven-process-reward-modeling.md, raw/hot-topics-sources/2026-04-10/278-more-bang-for-the-buck-process-reward-modeling-with-entropy-driven-uncertainty.md, raw/hot-topics-sources/2026-04-10/279-the-lessons-of-developing-process-reward-models-in-mathematical-reasoning.md, raw/hot-topics-sources/2026-04-10/280-online-process-reward-learning-for-agentic-reinforcement-learning.md]
created: 2026-04-10
updated: 2026-04-13
---
# Process Reward Models (PRM) 재부상

이 페이지는 Process Reward Models (PRM) 재부상를 다룬다. 핵심은 추론 과정의 각 단계를 평가해 보상을 주는 스텝-레벨 검증자 모델이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

추론 과정의 각 단계를 평가해 보상을 주는 스텝-레벨 검증자 모델.

## 왜 지금 중요한가

2026년 들어 "Process Reward Models That Think", R-PRM, EDU-PRM 등 [[test-time-compute-scaling|CoT]] 기반 생성형 PRM이 기존 판별형 접근을 추월하며 ORM 독주에 제동을 걸고 있다.

## 대표 자료

- [Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty](https://arxiv.org/abs/2503.22233)
- [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2501.07301)
- [Online Process Reward Learning for Agentic Reinforcement Learning](https://arxiv.org/html/2509.19199v1)

## 실무 관점

특히 "Online Process Reward Learning for Agentic Reinforcement Learning"(arXiv 2509.19199) 논문이 보여주듯, PRM은 에이전트 실행 중 스텝별 평가를 위한 [[agent-trajectory-evaluation|Agent Trajectory Evaluation]] 프레임워크와 직접 연결된다 -- PRM이 제공하는 스텝-레벨 신호는 에이전트 궤적의 품질 측정 기준이 된다.

## 관련 문서
- [[test-time-compute-scaling]]
- [[direct-preference-optimization]]

- [[ai-hot-topics-2026-04]]
- [[dapo]]
- [[on-policy-distillation]]
- [[agent-trajectory-evaluation]]

