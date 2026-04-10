---
title: On-Policy Distillation
category: training
page_type: concept
tags: [training, concept, policy, distillation, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---
# On-Policy Distillation

이 페이지는 On-Policy Distillation를 다룬다. 핵심은 학생이 직접 롤아웃한 궤적에 교사 모델이 토큰별 밀집 피드백을 주는 증류 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

학생이 직접 롤아웃한 궤적에 교사 모델이 토큰별 밀집 피드백을 주는 증류 기법.

## 왜 지금 중요한가

Thinking Machines Lab이 Qwen3-8B에서 RL 대비 1/10 비용으로 동등 성능을 재현해 화제가 됐고, RL과 SFT의 장점을 결합한 post-training의 새 축으로 부상 중이다.

## 대표 자료

- [On-Policy Distillation (Thinking Machines Lab blog)](https://thinkingmachines.ai/blog/on-policy-distillation/)
- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)
- [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)
- [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](https://arxiv.org/html/2603.25562)
- [Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://arxiv.org/abs/2602.22495)

## 2026년 4월 핫토픽 맥락

Thinking Machines Lab이 Qwen3-8B에서 RL 대비 1/10 비용으로 동등 성능을 재현해 화제가 됐고, RL과 SFT의 장점을 결합한 post-training의 새 축으로 부상 중이다.

### 추가 레퍼런스

- [On-Policy Distillation (Thinking Machines Lab blog)](https://thinkingmachines.ai/blog/on-policy-distillation/)
- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)
- [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)
- [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](https://arxiv.org/html/2603.25562)
- [Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://arxiv.org/abs/2602.22495)

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[process-reward-models]]
- [[rl-scaling-laws]]
