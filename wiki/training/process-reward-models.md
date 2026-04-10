---
title: Process Reward Models (PRM) 재부상
category: training
page_type: concept
tags: [training, concept, process, reward, models, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/process-reward-models.md, raw/hot-topics-sources/2026-04-10/276-process-reward-models-that-think.md, raw/hot-topics-sources/2026-04-10/277-r-prm-reasoning-driven-process-reward-modeling.md, raw/hot-topics-sources/2026-04-10/278-more-bang-for-the-buck-process-reward-modeling-with-entropy-driven-uncertainty.md, raw/hot-topics-sources/2026-04-10/279-the-lessons-of-developing-process-reward-models-in-mathematical-reasoning.md, raw/hot-topics-sources/2026-04-10/280-online-process-reward-learning-for-agentic-reinforcement-learning.md]
created: 2026-04-10
updated: 2026-04-10
---
# Process Reward Models (PRM) 재부상

이 페이지는 Process Reward Models (PRM) 재부상를 다룬다. 핵심은 추론 과정의 각 단계를 평가해 보상을 주는 스텝-레벨 검증자 모델이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

추론 과정의 각 단계를 평가해 보상을 주는 스텝-레벨 검증자 모델.

## 왜 지금 중요한가

2026년 들어 "Process Reward Models That Think", R-PRM, EDU-PRM 등 CoT 기반 생성형 PRM이 기존 판별형 접근을 추월하며 ORM 독주에 제동을 걸고 있다.

## 대표 자료

- [Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty](https://arxiv.org/abs/2503.22233)
- [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2501.07301)
- [Online Process Reward Learning for Agentic Reinforcement Learning](https://arxiv.org/html/2509.19199v1)

## 2026년 4월 큐레이션 요약

- 정의: 추론 과정의 각 단계를 평가해 보상을 주는 스텝-레벨 검증자 모델.
- 왜 중요한가: 2026년 들어 "Process Reward Models That Think", R-PRM, EDU-PRM 등 CoT 기반 생성형 PRM이 기존 판별형 접근을 추월하며 ORM 독주에 제동을 걸고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×5

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/process-reward-models.md`

### source별 핵심 신호

- **[2504.16828] Process Reward Models That Think** (`arxiv.org`): https://arxiv.org/abs/2504.16828
  - 메모: Step-by-step verifiers -- also known as process reward models (PRMs) -- are a key ingredient for test-time scaling. PRMs require step-level supervision, making them expensive to train.
- **[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling** (`arxiv.org`): https://arxiv.org/abs/2503.21295
  - 메모: Large language models (LLMs) inevitably make mistakes when performing step-by-step mathematical reasoning. Process Reward Models (PRMs) have emerged as a promising solution by evaluating each reasoning step.
- **[2503.22233] More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty** (`arxiv.org`): https://arxiv.org/abs/2503.22233
  - 메모: We introduce the Entropy-Driven Uncertainty Process Reward Model (EDU-PRM), a novel entropy-driven training framework for process reward modeling that enables dynamic, uncertainty-aligned segmentation of complex reasonin
- **[2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning** (`arxiv.org`): https://arxiv.org/abs/2501.07301
  - 메모: Process Reward Models (PRMs) emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), which aim to identify and mitigate intermediate errors in the reasoning proce
- **Online Process Reward Leanring for Agentic Reinforcement Learning** (`arxiv.org`): https://arxiv.org/html/2509.19199v1
  - 메모: Sample efficiency and training stability.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[dapo]]
- [[on-policy-distillation]]
