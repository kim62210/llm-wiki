---
source: arxiv
arxiv_id: "2604.09459"
title: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models"
authors: ["Chenchen Zhang"]
date: 2026-04-10
url: "https://arxiv.org/abs/2604.09459"
fetched: 2026-04-20
status: pending_ingest
tags: [survey, credit-assignment, reasoning-rl, agentic-rl, process-reward-model, hindsight-counterfactual, privileged-asymmetric-critic, turn-level-mdp]
---

## Abstract

LLM RL에서 **sparse reward → credit assignment 난이도**를 reasoning (500~30k tokens) vs agentic (100+ turns, 100k~1M tokens) 두 도메인으로 나눠 **47개 방법을 2024~2026 초 기간에 걸쳐 정리**한 서베이.

## 2차원 분류 체계

| 축 1 (granularity) | 축 2 (methodology) |
|--------------------|---------------------|
| Token | Monte Carlo |
| Segment | Temporal Difference |
| Step | Model-based |
| Turn | Game-theoretic |
| Multi-agent | Information-theoretic |

## Reasoning RL vs Agentic RL

**Reasoning RL** (길지만 단일 turn)
- Process Reward Models (PRM)
- "Critic-free group comparison" — GRPO 계열

**Agentic RL** (multi-turn, 100+ turn)
- Hindsight counterfactual analysis — 대안 action trajectory 분석
- Privileged asymmetric critic — 배포 시 없는 정보를 훈련 시에만 critic이 활용
- **Turn-level MDP reformulation** — 시간 추상화를 재구조화

## 핵심 기여

Zhang이 제공한 **3가지 재사용 자원**:

1. Machine-readable inventory (47 papers, taxonomy labels, evidence levels)
2. 표준화된 reporting checklist — 기존 문헌의 체계적 gap 식별
3. 벤치마크 프로토콜 스펙 (controlled bifurcation + method selection decision tree)

## 오픈 챌린지

- Episode length scale 확대 시 기존 방법 확장성
- Partial observability와 credit fidelity의 상호작용
- **Granularity 최적화** — 태스크별 권장 granularity가 무엇인가
- Cross-method 비교 표준 부재

## 함의

- Reasoning credit assignment는 **성숙 단계** (clear frontrunners)
- Agentic credit assignment는 **fragmentation 단계** (turn-level MDP 재구성이 근본 필요)
- Million-token trajectory가 reasoning 기법과 근본적으로 다름

## 기존 페이지 업데이트 후보

- `wiki/training/rlhf-dpo.md` 또는 `wiki/concepts/credit-assignment-rl.md` (있으면)
- `wiki/concepts/process-reward-model.md` (있으면)
- `wiki/agents/long-horizon-rl-training-for-agents.md` 확장
- `wiki/concepts/privileged-asymmetric-critic.md` (신규)
- `wiki/concepts/turn-level-mdp.md` (신규)

## Raw 요약 키워드
credit assignment survey, 47 methods 2024-2026, reasoning RL vs agentic RL, process reward model, hindsight counterfactual, privileged asymmetric critic, turn-level MDP, granularity taxonomy
