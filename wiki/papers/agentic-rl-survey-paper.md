---
title: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey
category: papers
page_type: paper
tags: [paper, agentic-rl, survey, reinforcement-learning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/01-arxiv-org-the-landscape-of-agentic-reinforcement-learning-for-llms-a-s.md]
created: 2026-04-10
updated: 2026-04-10
---

# The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

LLM 에이전트를 위한 강화학습 연구 지형을 정리한 대형 서베이다. 단일 알고리즘 소개가 아니라, agentic RL의 문제 설정·학습 루프·평가·응용 축을 한꺼번에 조망한다.

## 핵심 기여

- LLM 기반 에이전트 학습을 RL 관점에서 체계적으로 정리
- tool use, planning, trajectory optimization, long-horizon interaction을 하나의 학습 문제로 묶음
- 다양한 벤치마크와 알고리즘 계열을 연결해 연구 지형도를 제공

## 결과와 시사점

- 에이전트 학습은 단순 reasoning 최적화가 아니라 **도구 사용과 환경 상호작용의 학습**으로 이동하고 있다.
- long-horizon agent를 다루려면 reward 설계, trajectory credit assignment, evaluation 환경이 함께 바뀌어야 한다.

## 한계

서베이 특성상 전체 흐름을 잘 보여 주지만, 어떤 방법이 특정 환경에서 결정적으로 우월한지까지는 말해주지 않는다.

## 실무 적용 관점

이 문서는 “에이전트 RL”을 하나의 buzzword가 아니라, **어떤 환경에서 어떤 보상과 어떤 검증 체계를 붙여야 하는가**의 문제로 읽게 해 준다.

## 관련 문서

- [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents (Multi-Turn RLVR)]]
- [[rlvr|RLVR (Reinforcement Learning with Verifiable Rewards)]]
- [[agentic-rl|Agentic RL (Tool-Integrated Reasoning 학습)]]

