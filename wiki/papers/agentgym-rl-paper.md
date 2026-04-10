---
title: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning
category: papers
page_type: paper
tags: [paper, agentic-rl, long-horizon, reinforcement-learning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/03-arxiv-org-agentgym-rl-training-llm-agents-for-long-horizon-decision-ma.md]
created: 2026-04-10
updated: 2026-04-10
---

# AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning

장기 의사결정 문제를 푸는 LLM 에이전트를 multi-turn RL로 훈련시키는 프레임워크를 제안한 논문이다.

## 핵심 기여

- long-horizon interaction을 RL 학습 대상으로 직접 설정
- 단발 reasoning이 아니라 trajectory 전체의 품질을 최적화
- 환경 상호작용이 필요한 agent training을 위한 실험 틀 제공

## 결과와 시사점

- 장기 과제 성능은 모델의 단일 추론 능력만이 아니라 environment loop와 reward 설계에 크게 의존한다.
- agent benchmark와 training infrastructure가 함께 발전해야 함을 보여준다.

## 한계

multi-turn RL은 비용이 높고 reward 설계가 까다롭다. 따라서 재현성과 학습 안정성이 중요한 부담으로 남는다.

## 실무 적용 관점

agent를 훈련하려면 prompt tuning만으로는 부족하고, **interaction environment + verifier + reward**를 하나의 시스템으로 설계해야 한다는 점을 보여준다.

## 관련 문서

- [[agentic-rl-survey-paper|The Landscape of Agentic Reinforcement Learning for LLMs: A Survey]]
- [[agentic-rl|Agentic RL (Tool-Integrated Reasoning 학습)]]
- [[rlvr|RLVR (Reinforcement Learning with Verifiable Rewards)]]

