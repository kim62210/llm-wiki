---
title: Reinforcement Learning for Long-Horizon Interactive LLM Agents
category: papers
page_type: paper
tags: [paper, long-horizon, interactive-agents, reinforcement-learning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/02-arxiv-org-reinforcement-learning-for-long-horizon-interactive-llm-agen.md]
created: 2026-04-10
updated: 2026-04-10
---

# Reinforcement Learning for Long-Horizon Interactive LLM Agents

장기 상호작용 에이전트를 RL 문제로 직접 모델링한 초기 핵심 논문이다.

## 핵심 기여

- long-horizon interactive agent를 RL 대상으로 정식화
- multi-turn interaction을 학습 루프 안에 포함
- 이후 agent RL 계열 연구의 출발점 역할을 수행

## 결과와 시사점

- 장기 상호작용 에이전트는 static reasoning보다 trajectory 전체 최적화가 중요하다.
- 이후 AgentGym-RL, ReSearch 같은 연구가 이 흐름 위에서 확장된다.

## 한계

reward 설계와 environment 구성의 난이도가 높고, 계산 비용도 크다.

## 실무 적용 관점

long-horizon agent 학습을 생각할 때, 먼저 상호작용을 어떤 상태/행동/보상 구조로 정의할지 묻게 만든다.

## 관련 문서

- [[agentgym-rl-paper|AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning]]
- [[agentic-rl-survey-paper|The Landscape of Agentic Reinforcement Learning for LLMs: A Survey]]
- [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents (Multi-Turn RLVR)]]

