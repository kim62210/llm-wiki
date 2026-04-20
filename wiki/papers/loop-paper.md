---
title: Reinforcement Learning for Long-Horizon Interactive LLM Agents
category: papers
page_type: paper
tags: [paper, long-horizon, interactive-agents, reinforcement-learning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/02-arxiv-org-reinforcement-learning-for-long-horizon-interactive-llm-agen.md]
created: 2026-04-10
updated: 2026-04-13
---
# Reinforcement Learning for Long-Horizon Interactive LLM Agents

장기 상호작용 에이전트를 RL 문제로 직접 모델링한 초기 핵심 논문이다.

## 핵심 기여

- long-horizon interactive agent를 RL 대상으로 정식화
- multi-turn interaction을 학습 루프 안에 포함
- 이후 [[long-horizon-rl-training-for-agents|agent RL]] 계열 연구의 출발점 역할을 수행

## 결과와 시사점

- 장기 상호작용 에이전트는 static reasoning보다 [[langgraph-durable-execution|trajectory]] 전체 최적화가 중요하다.
- 이후 [[agentgym-rl-paper|AgentGym]]-RL, ReSearch 같은 연구가 이 흐름 위에서 확장된다.

## 한계

reward 설계와 environment 구성의 난이도가 높고, 계산 비용도 크다.

## 실무 적용 관점

long-horizon agent 학습을 생각할 때, 먼저 상호작용을 어떤 상태/행동/보상 구조로 정의할지 묻게 만든다.

## 문제 설정

`Reinforcement Learning for Long-Horizon Interactive LLM Agents`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `Reinforcement Learning for Long-Horizon Interactive LLM Agents`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **Reinforcement Learning for Long-Horizon Interactive LLM Agents** — https://arxiv.org/abs/2502.01600 · 초록 단서: Interactive digital agents (IDAs) leverage APIs of stateful digital environments to perform tasks in response to user requests. While IDAs powered by instruction-tuned large lan... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/02-arxiv-org-reinforcement-learning-for-long-horizon-interactive-llm-agen.md`

## 관련 문서

- [[agentgym-rl-paper|AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning]]
- [[agentic-rl-survey-paper|The Landscape of Agentic Reinforcement Learning for LLMs: A Survey]]
- [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents (Multi-Turn RLVR)]]
