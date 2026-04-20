---
title: KL 발산 패널티 (KL Divergence Penalty)
category: training
page_type: concept
tags: [training, concept, kl-divergence, rlhf, policy-drift, regularization, ppo]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# KL 발산 패널티 (KL Divergence Penalty)

## 개요

KL 발산 패널티는 RLHF 파이프라인에서 정책 모델이 SFT 참조 모델에서 지나치게 벗어나는 것을 방지하는 정규화 메커니즘이다. 보상 최대화만 추구하면 정책이 비정상적이고 반복적이거나 의미 없는 출력을 생성하는 영역으로 이탈(policy drift)할 수 있다. KL 발산 패널티는 이 이탈을 제약하여 학습 안정성을 확보하고, [[reward-model-training|보상 모델]]의 분포 외 영역에서 발생하는 보상 해킹을 억제한다.

## 수학적 정의

Kullback-Leibler 발산은 두 확률 분포 사이의 비대칭적 거리 측도다. RLHF에서는 현재 정책 pi_theta와 참조 정책 pi_ref 사이의 KL 발산을 측정한다:

```
D_KL(pi_theta || pi_ref) = E_x~pi_theta [log(pi_theta(x) / pi_ref(x))]
```

이 값이 0이면 두 분포가 동일하고, 값이 클수록 정책이 참조 모델에서 멀리 벗어난 것이다.

## RLHF에서의 역할

### PPO 목적함수에의 통합

표준 RLHF 파이프라인에서 PPO의 보상 신호는 [[reward-model-training|보상 모델]]의 출력에서 KL 페널티를 차감한 형태로 구성된다:

```
R_total(x, y) = R_reward_model(x, y) - beta * D_KL(pi_theta(y|x) || pi_ref(y|x))
```

beta는 보상 최대화와 정책 제약 사이의 균형을 조절하는 하이퍼파라미터다. beta가 크면 참조 모델에 가깝게 유지되지만 보상 최적화가 제한되고, beta가 작으면 보상을 적극 추구하지만 정책 이탈과 보상 해킹 위험이 증가한다.

### 토큰 수준 구현

PPO는 보통 토큰 수준에서 작동하므로, KL 페널티도 토큰별로 계산된다. 실무에서는 전체 KL 발산 대신 RL 정책과 SFT 정책의 로그 확률 차이로 근사하는 것이 일반적이다:

```
KL_approx(t) = log pi_theta(x_t | x_{<t}) - log pi_ref(x_t | x_{<t})
```

이 근사는 계산이 빠르면서도 정책 이탈을 효과적으로 억제한다.

## 정책 이탈 (Policy Drift)

### 문제 현상

KL 제약 없이 보상만 최대화하면 다음과 같은 퇴행(degeneration)이 발생한다:

- **반복적 출력**: 보상이 높은 구절을 반복 생성
- **스타일 과최적화**: 자신감 있는 톤, 과도한 구조화 등 표면적 패턴에 수렴
- **[[hallucination|환각]] 증가**: 보상 모델이 사실성보다 유창성에 반응하면 거짓 정보 생성 증가
- **모드 붕괴**: 응답 다양성이 급격히 감소
- **언어 능력 망각**: 기본적인 문법, 어휘 사용 능력이 저하

### 참조 모델의 역할

참조 모델(pi_ref)은 보통 SFT 단계를 마친 모델의 가중치를 복사하여 고정(freeze)한 것이다. 학습 중 그래디언트 업데이트를 받지 않으므로, SFT에서 획득한 언어 능력과 지시 따르기 능력을 보존하는 닻(anchor) 역할을 한다. 추론 시에도 KL 계산을 위해 참조 모델을 메모리에 유지해야 하므로, GPU 메모리 비용이 2배로 증가하는 실무적 부담이 있다.

## [[grpo|GRPO]]와 [[dapo|DAPO]]에서의 KL

[[grpo|GRPO]]도 KL 패널티를 사용하지만, 크리틱 모델 대신 그룹 내 보상 정규화로 어드밴티지를 계산하므로 별도의 크리틱이 불필요하다. [[dapo|DAPO]]는 Clip-Higher 기법으로 KL 제약의 비대칭성을 조절하여, 탐색(exploration)을 장려하면서도 안정성을 유지하는 전략을 취한다.

## [[direct-preference-optimization|DPO]]에서의 암묵적 KL

DPO의 목적함수에 포함된 beta 파라미터는 암묵적으로 KL 발산 패널티와 동일한 역할을 수행한다. DPO 손실의 구조를 분석하면, 정책 모델과 참조 모델의 로그 확률 비율에 beta를 곱하는 항이 KL 제약으로 작용한다. 따라서 DPO에서도 beta를 높이면 참조 모델에 가깝게, 낮추면 선호도 데이터에 더 적극적으로 적응하게 된다.

## beta 하이퍼파라미터 조정

### 실무 가이드라인

| beta 범위 | 특성 | 적합한 상황 |
|-----------|------|-------------|
| 0.01-0.05 | 약한 제약, 적극적 보상 추구 | 안전한 도메인, 강건한 보상 모델 |
| 0.05-0.2 | 일반적 범위 | 대부분의 RLHF 학습 |
| 0.2-0.5 | 강한 제약, 보수적 학습 | 안전 민감 응용, 초기 탐색 |

### 적응적 KL 제어

고정 beta 대신 학습 과정에서 KL 발산이 목표 범위를 유지하도록 beta를 동적으로 조절하는 방법도 사용된다. InstructGPT에서 도입된 이 접근은 학습 초기에는 자유로운 탐색을 허용하고, KL이 임계값을 초과하면 패널티를 강화하는 피드백 루프를 형성한다.

## KL 발산 모니터링

[[evaluation-during-training|학습 중 평가]]에서 KL 발산은 핵심 건강 지표(health metric)다:

- KL이 단조 증가하면 정책 이탈 진행 중
- KL이 급격히 감소하면 모드 붕괴 가능성
- 보상은 상승하는데 KL이 급증하면 보상 해킹 의심
- KL이 안정적이면서 보상이 완만히 상승하면 정상 학습

## 대안적 접근

- **클리핑 (PPO Clipping)**: KL 패널티 대신 정책 비율을 직접 클리핑. PPO의 원래 설계에 포함된 방법으로, KL 패널티와 병행 사용 가능
- **참조 모델 없는 최적화**: [[direct-preference-optimization|SimPO]] 같은 기법은 참조 모델 자체를 제거하여 KL 계산 비용과 메모리 부담을 해소
- **엔트로피 보너스**: 정책의 출력 엔트로피를 보상에 추가하여 다양성을 유지. KL과 상보적으로 사용 가능

## 대표 자료

- [KL Divergence Penalty in RLHF: Theory & Implementation (Brenndoerfer)](https://mbrenndoerfer.com/writing/kl-divergence-penalty-rlhf-training)
- [Secrets of RLHF in Large Language Models Part I: PPO (2023)](https://arxiv.org/html/2307.04964v1)
- [A Guide to Reinforcement Learning Post-Training for LLMs (HuggingFace, 2025)](https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms)

## 관련 문서

- [[reward-model-training]] -- KL 패널티가 보상 해킹을 억제하는 메커니즘
- [[direct-preference-optimization]] -- beta 파라미터를 통한 암묵적 KL 제어
- [[grpo]] -- KL 패널티를 포함한 그룹 기반 정책 최적화
- [[dapo]] -- KL 제약의 비대칭 클리핑 전략
- [[rlvr]] -- 검증 가능한 보상 환경에서의 정책 이탈 관리
- [[evaluation-during-training]] -- KL 발산을 학습 건강 지표로 추적
- [[extended-constitutional-ai]] -- RLHF 파이프라인에서 KL의 위치
- [[process-reward-models]] -- 단계별 보상과 KL 제약의 결합
