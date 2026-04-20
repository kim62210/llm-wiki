---
source: arxiv
arxiv_id: "2604.10701"
title: "Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning"
authors: ["Zikang Shan", "Han Zhong", "Liwei Wang", "Li Zhao"]
date: 2026-04-12
url: "https://arxiv.org/abs/2604.10701"
fetched: 2026-04-20
status: pending_ingest
tags: [generative-critic, value-model, actor-critic, in-context-conditioning, llm-rl, chain-of-thought-value-estimation]
---

## Abstract

현대 LLM RL이 **value-free (PPO w/o value)** 쪽으로 이동하는 추세에 반대. **Generative Actor-Critic (GenAC)**이 CoT reasoning 기반 critic을 통해 value model을 다시 가치있게 만든다고 주장. Discriminative one-shot scalar critic은 representation complexity로 인해 scale 안정성 낮음을 경험적으로 증명.

## 핵심 구조: Generative Critic

**기존 방식** (discriminative):
- 한 번에 scalar value 예측 (state/action → value)
- Scaling 불안정 (모델 커질수록 reliable 하지 않음)

**GenAC** (generative):
- CoT reasoning → value 판단
- 여러 reasoning path 탐색 후 commitment
- **인간의 가치 평가와 유사한 구조** (근거 → 결론)

## In-Context Conditioning

- Actor policy가 훈련 중 진화 → critic이 뒤쳐지면 value drift
- Generative critic이 **현재 actor 행동 샘플을 in-context**로 받아 calibration 유지
- 기존 value function drift 문제 완화

## 경험적 결과

| 지표 | GenAC vs baseline |
|------|-------------------|
| Value approximation accuracy | 우위 (value-based/value-free 모두 대비) |
| **Ranking reliability** (trajectory 순서 판별) | 유의미 개선 |
| OOD generalization | 개선 |
| Downstream RL 성능 | 일관적 향상 |

PPO + 표준 value model 대비 일관 우세. Value-free (GRPO 등) 대비도 credit assignment 품질 우위.

## 시사점

- "Value model은 죽었다" 내러티브에 대한 반론
- CoT가 critic에도 유효 (action 선택만이 아니라)
- **Sample-efficient LLM RL**의 유망 방향
- Actor와 critic 둘 다 generative → 통합 아키텍처 가능성

## 기존 페이지 업데이트 후보

- `wiki/training/rlhf-dpo.md` 또는 `wiki/concepts/actor-critic.md` (있으면)
- `wiki/concepts/value-model-llm-rl.md` (신규 후보)
- `wiki/concepts/credit-assignment-rl.md` (신규 후보)
- `wiki/concepts/process-reward-model.md`와 교차참조

## Raw 요약 키워드
GenAC, generative critic, value model, in-context conditioning, CoT value estimation, ranking reliability, PPO baseline, value-free RL critique, OOD generalization
