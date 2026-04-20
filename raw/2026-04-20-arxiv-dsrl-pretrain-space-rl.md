---
source: arxiv
arxiv_id: "2604.14142"
title: "From P(y|x) to P(y): Investigating Reinforcement Learning in Pre-train Space"
authors: ["Yuqiao Tan", "Minzheng Wang", "Bo Liu", "Zichen Liu", "Tian Liang", "Shizhu He", "Jun Zhao", "Kang Liu"]
date: 2026-04-15
url: "https://arxiv.org/abs/2604.14142"
fetched: 2026-04-20
status: pending_ingest
tags: [rlvr, pretrain-space-rl, dual-space-rl, policy-reincarnation, negative-sample-reinforcement, reasoning-rl]
---

## Abstract

RLVR(reinforcement learning with verifiable rewards)은 P(y|x) 최적화지만 **base model의 output 분포에 근본적으로 bounded**. 이 논문은 **P(y) 주변분포(marginal distribution)**를 pretrain space에서 최적화해 reasoning horizon을 확장하는 **Dual Space RL (DSRL)** + **Policy Reincarnation** 제안.

## 핵심 분포 구분

| 분포 | 해석 | 한계 |
|------|------|------|
| **P(y\|x)** | 입력별 조건부 출력 | base model 기존 capability 경계 |
| **P(y)** | 전체 출력 주변분포 | 기존 RLVR이 놓치는 영역 |

Reasoning pattern의 **잠재적 공간**을 P(y)로 재표현, pretrain space 조작으로 확장.

## DSRL 2단계

1. **NSR-PreRL (Negative Sample Reinforcement in Pretrain Space)**
   - 공격적 pruning + expansion
   - 부적절한 reasoning pathway 빠르게 제거
   - **Reflection/transition thought가 6.54x / 14.89x 증가** (경험적)
2. **표준 RL (conventional RLVR)**
   - fine-grained refinement
   - NSR-PreRL로 확장된 horizon을 정교화

Two-stage가 **Policy Reincarnation**로 포맷화 — 모델이 두 훈련 단계로 "환생"하며 다른 목표로 진화.

## 경험적 결과

- Strong baselines 대비 일관적 개선
- Reflection/transition thought 증가 → reasoning quality 개선 (superficial improvement 아님)
- Subspace를 refined correct reasoning으로 집중

## 함의

- **RL-from-scratch vs RL-on-pretrained 이분법 너머**: pretrain space에서의 RL도 가능
- Negative sample이 positive보다 공간 제약력 큼 — exploration 가속
- Base model capability를 "넘어서는" 경로 제시

## 기존 페이지 업데이트 후보

- `wiki/training/rlvr-reinforcement-learning-verifiable-rewards.md` (있으면)
- `wiki/training/reasoning-rl.md` (있으면)
- `wiki/concepts/negative-sample-reinforcement.md` (신규 후보)
- `wiki/concepts/policy-reincarnation.md` (신규 후보)

## Raw 요약 키워드
DSRL, Dual Space RL, Policy Reincarnation, NSR-PreRL, pretrain space RL, P(y|x) to P(y), 14.89x transition, 6.54x reflection, reasoning horizon expansion
