---
title: "DSRL: 사전학습 공간에서의 강화학습 - P(y|x)에서 P(y)로"
category: papers
page_type: paper
tags: [rlvr, dual-space-rl, policy-reincarnation, pretrain-space, nsr-prerl, reasoning-rl, negative-sample]
sources: [raw/2026-04-20-arxiv-dsrl-pretrain-space-rl.md]
created: 2026-04-20
updated: 2026-04-20
---

# DSRL: P(y|x)에서 P(y)로 - 사전학습 공간에서의 강화학습 (2604.14142)

> "RLVR은 P(y|x)를 최적화하지만 base model의 output 분포에 근본적으로 bounded된다."

기존 RLVR(Reinforcement Learning with Verifiable Rewards)은 조건부 분포 $P(y|x)$ 최적화에 머물러 base model이 이미 생성할 수 없는 패턴을 학습하기 어렵다는 한계가 있다. 이 논문은 **사전학습 공간(pretrain space)에서 주변분포(marginal distribution) $P(y)$를 직접 조작**해 reasoning horizon을 확장하는 **Dual Space RL (DSRL)** 프레임워크를 제안한다.

## 핵심 분포 구분

| 분포 | 해석 | 기존 RL의 접근 |
|------|------|----------------|
| $P(y\|x)$ | 입력별 조건부 출력 분포 | RLVR의 최적화 대상 |
| $P(y)$ | 전체 출력 주변분포 | DSRL이 새롭게 조작하는 공간 |

조건부 분포 최적화는 base model이 이미 내재화한 reasoning 패턴의 경계 내에서만 작동한다. 주변분포를 직접 조작하면 이 경계를 확장할 수 있다는 것이 핵심 통찰이다.

## DSRL 2단계 훈련 파이프라인

```mermaid
flowchart TD
    BaseModel[Base Model\nP(y|x) 경계 내] --> Stage1[1단계: NSR-PreRL\n사전학습 공간에서 RL\nNegative Sample Reinforcement]
    Stage1 --> Extended[Reasoning Horizon 확장\nReflection 6.54x 증가\nTransition thought 14.89x 증가]
    Extended --> Stage2[2단계: 표준 RLVR\nConventional RL Refinement\nfine-grained 정교화]
    Stage2 --> FinalModel[최종 모델\n확장된 horizon + 정교화]
    Stage1 -.->|Policy Reincarnation| Stage2
```

Policy Reincarnation은 두 훈련 단계를 연결하는 개념으로, 모델이 서로 다른 목표를 가진 두 단계로 "환생"해 진화함을 의미한다.

## 1단계: NSR-PreRL (Negative Sample Reinforcement in Pretrain Space)

- 사전학습 공간에서 동작하는 RL 단계
- **공격적 pruning + expansion**: 부적절한 reasoning pathway를 빠르게 제거하고 새로운 경로를 확장
- Negative sample이 positive보다 공간 제약력이 크기 때문에, 잘못된 패턴 제거로 탐색 공간을 효율적으로 좁힘
- 경험적 결과: reflection thought **6.54배**, transition thought **14.89배** 증가

## 2단계: 표준 RLVR

- 1단계에서 확장된 reasoning horizon을 정교화
- 기존 RLVR 방식(verifiable reward 기반)으로 fine-grained refinement
- NSR-PreRL이 만들어 놓은 확장된 공간에서 세밀한 최적화 진행

## Policy Reincarnation

두 단계 훈련을 연결하는 개념적 프레임:

- 모델이 서로 다른 학습 목표를 가진 두 단계로 "환생"
- 1단계(공간 확장) → 2단계(공간 정교화)로 목표가 전환
- 단순한 sequential fine-tuning과 달리, 두 단계가 상보적 역할을 명시적으로 분리

## 경험적 결과 요약

| 측정 항목 | 결과 |
|-----------|------|
| Reflection thought 증가 | 6.54x |
| Transition thought 증가 | 14.89x |
| Strong baseline 대비 | 일관적 개선 |
| Superficial improvement 여부 | 아님 (reasoning quality 개선 확인) |

## 실무 적용 관점

- **Base model 경계 극복**: 현재 모델이 생성하지 못하는 reasoning 패턴이 필요한 경우, 사전학습 공간 조작으로 capability 확장 가능
- **Negative sample 활용**: 실패 사례를 버리지 않고 공간 제약에 적극 활용
- **2단계 훈련 설계**: 탐색(exploration) 단계와 정제(refinement) 단계를 명시적으로 분리하는 파이프라인 설계 패턴

## 한계

- 사전학습 공간 조작을 위한 추가 계산 비용
- Reflection/transition thought 증가가 모든 도메인에서 성능으로 이어지는지 일반화 검증 필요
- 2단계 훈련 시 catastrophic forgetting 위험 관리 필요

## 관련 문서

- [[rlvr]] -- RLVR (Reinforcement Learning with Verifiable Rewards) 개요
- [[reinforcement-learning-for-llm]] -- LLM을 위한 강화학습 전반
- [[deepseek-r1-paper]] -- DeepSeek-R1: RLVR 기반 추론 강화 대표 사례
- [[process-reward-model-detail]] -- 프로세스 보상 모델 상세
- [[long-horizon-rl-training-for-agents]] -- 에이전트를 위한 장기 RL 훈련
