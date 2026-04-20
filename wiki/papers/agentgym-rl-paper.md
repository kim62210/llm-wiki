---
title: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning
category: papers
page_type: paper
tags: [paper, agentic-rl, long-horizon, reinforcement-learning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/03-arxiv-org-agentgym-rl-training-llm-agents-for-long-horizon-decision-ma.md]
created: 2026-04-10
updated: 2026-04-13
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

## 문제 설정

`AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 초록과 메타데이터를 함께 읽으며 문제 정의, 방법, 검증 환경의 세 층을 분리해서 보는 것이 좋다

## 리뷰 포인트

- `AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning** — https://arxiv.org/abs/2509.08755 · 초록 단서: Developing autonomous LLM agents capable of making a series of intelligent decisions to solve complex, real-world tasks is a fast-evolving frontier. Like human cognitive develop... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/03-arxiv-org-agentgym-rl-training-llm-agents-for-long-horizon-decision-ma.md`

## 프레임워크 구성

| 구성요소 | 논문이 제안한 것 | 의미 |
|---|---|---|
| 학습 틀 | AgentGym-RL의 modular, decoupled architecture | 다양한 환경과 알고리즘을 같은 RL 틀 안에서 실험하게 해 준다 |
| 목표 | SFT 없이도 interactive RL로 agent를 키우는 것 | supervised imitation이 아닌 **환경 상호작용 학습**을 전면에 둔다 |
| 안정화 전략 | ScalingInter-RL | 초기에는 상호작용 수를 제한해 exploitation을 강조하고, 이후 horizon을 늘려 exploration을 확장한다 |
| 기대 효과 | diverse behaviors, long-horizon collapse 완화 | 장기 과제에서 agent가 단조로운 전략에 갇히는 문제를 줄이려는 시도다 |

## 실무 함의

이 논문이 주는 핵심 메시지는 "agent를 잘 학습시키려면 모델 파라미터만 보지 말고 **환경 설계와 horizon curriculum**까지 같이 설계해야 한다"는 점이다. 즉 RL 인프라가 없는 팀은 바로 재현하기 어렵지만, [[multi-turn-agent-evaluation|evaluation]] harness를 점차 상호작용형으로 바꾸는 방향 자체는 실무에도 직접적인 힌트가 된다.

## 관련 문서
- [[loop-paper]]

- [[agentic-rl-survey-paper|The Landscape of Agentic Reinforcement Learning for LLMs: A Survey]]
- [[agentic-rl|Agentic RL (Tool-Integrated Reasoning 학습)]]
- [[rlvr|RLVR (Reinforcement Learning with Verifiable Rewards)]]
