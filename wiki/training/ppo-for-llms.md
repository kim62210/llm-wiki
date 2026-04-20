---
title: PPO for LLMs (Proximal Policy Optimization)
category: training
page_type: concept
tags: [training, concept, ppo, rlhf, policy-gradient, clipping, gae, kl-penalty, reinforcement-learning]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---

# PPO for LLMs (Proximal Policy Optimization)

## 개요

PPO(Proximal Policy Optimization)는 Schulman et al.(2017)이 제안한 정책 경사(policy gradient) 강화학습 알고리즘으로, [[rlhf-pipeline|RLHF 파이프라인]]의 3단계(정책 최적화)에서 사실상의 표준으로 자리잡았다. PPO의 핵심 아이디어는 정책 업데이트 크기를 클리핑(clipping)으로 제한하여, TRPO(Trust Region Policy Optimization)의 안정성을 유지하면서도 구현이 훨씬 단순하고 샘플 효율성이 높다는 것이다. ChatGPT, Claude, Gemini 등 프론티어 모델의 인간 정렬(alignment) 학습에 PPO가 핵심적으로 사용되었다. 2026년 현재 [[grpo]], [[dapo]] 등 PPO 변형과 DPO 같은 대안이 활발히 채택되고 있지만, PPO의 기본 구조는 LLM 강화학습의 표준 참조점으로 남아 있다.

## PPO 클리핑 목적함수

PPO-CLIP의 핵심 손실 함수:

```
L_PPO(theta) = E[min(r_t(theta) * A_t, clip(r_t(theta), 1-epsilon, 1+epsilon) * A_t)]
```

| 기호 | 의미 |
|------|------|
| r_t(theta) = pi_theta(a_t\|s_t) / pi_old(a_t\|s_t) | 새 정책과 이전 정책의 확률 비율 |
| A_t | 어드밴티지 추정치 (GAE로 계산) |
| epsilon | 클리핑 파라미터 (일반적으로 0.2) |

`min()` 함수가 핵심이다. 확률 비율이 신뢰 영역(trust region) [1-epsilon, 1+epsilon] 바깥으로 이동하면, 클리핑된 항이 그래디언트 기여를 차단하여 정책이 급격하게 변하는 것을 방지한다. 이것이 TRPO의 복잡한 제약 최적화를 단순한 클리핑으로 대체하면서도 학습 안정성을 유지하는 메커니즘이다.

### 클리핑의 동작 원리

- **어드밴티지가 양수일 때** (좋은 행동): r_t가 1+epsilon을 초과하면 클리핑. 좋은 행동의 확률을 과도하게 높이는 것을 방지
- **어드밴티지가 음수일 때** (나쁜 행동): r_t가 1-epsilon 미만이면 클리핑. 나쁜 행동의 확률을 과도하게 낮추는 것을 방지

이 비대칭적 제어가 PPO의 안정성을 보장한다.

## GAE (Generalized Advantage Estimation)

PPO는 원시 보상(raw reward) 대신 어드밴티지(advantage)를 사용하여 분산을 줄인다. GAE는 여러 시간 스텝의 어드밴티지를 지수 가중 평균으로 결합한다:

```
A_t^GAE(gamma, lambda) = sum_{l=0}^{inf} (gamma * lambda)^l * delta_{t+l}
```

여기서 delta_t = r_t + gamma * V(s_{t+1}) - V(s_t)는 시간차(TD) 오차다.

| 파라미터 | 역할 | 일반적 값 |
|---------|------|----------|
| gamma | 할인율. 미래 보상의 현재 가치 | 0.99-1.0 |
| lambda | 편향-분산 트레이드오프 제어 | 0.95 |

lambda가 0이면 1-스텝 TD만 사용(높은 편향, 낮은 분산), lambda가 1이면 전체 궤적 사용(낮은 편향, 높은 분산). lambda = 0.95가 실무에서 가장 널리 사용되는 절충점이다.

LLM 맥락에서 GAE는 토큰 수준에서 계산된다. 각 토큰 생성이 하나의 "행동"이 되고, [[reward-model-training|보상 모델]]의 점수가 시퀀스 끝에서 부여되면 GAE가 이 보상을 개별 토큰에 역전파한다.

## 4-모델 아키텍처

PPO 기반 RLHF는 동시에 4개의 대규모 모델을 운영한다:

```
Actor (정책 모델 pi_theta)     <-- 학습 대상, 응답 생성
Critic (가치 모델 V(s))        <-- 학습 대상, 상태 가치 추정
Reward Model (r(x,y))          <-- 동결, 응답 품질 점수 부여
Reference Model (pi_ref)       <-- 동결, KL 패널티 계산용 기준
```

| 모델 | 크기 | 업데이트 | 역할 |
|------|------|---------|------|
| Actor | 정책 모델 전체 | 학습 | 프롬프트에 대한 응답 생성 |
| Critic | 정책 모델과 동일 또는 별도 | 학습 | 각 상태(토큰 위치)의 기대 보상 추정, GAE 어드밴티지 계산 |
| Reward Model | 정책 대비 같거나 작음 | 동결 | 완성된 응답에 스칼라 보상 점수 부여 |
| Reference Model | 정책과 동일 | 동결 | KL 발산 계산을 위한 SFT 기준점 |

7B 모델 기준으로 이 4-모델 구조는 약 28GB의 기본 파라미터에 옵티마이저 상태, 활성화(activation), 그래디언트까지 더하면 100GB 이상의 VRAM을 요구한다. 이 메모리 부담이 PPO 대안을 탐색하게 된 주요 동기다.

## [[kl-divergence-penalty|KL 발산 패널티]]

PPO의 보상 신호는 [[reward-model-training|보상 모델]] 출력에서 KL 페널티를 차감한 형태로 구성된다:

```
R_total(x, y) = R_reward_model(x, y) - beta * D_KL(pi_theta(y|x) || pi_ref(y|x))
```

beta는 보상 최대화와 정책 제약 사이의 균형을 조절하며, beta가 없으면 정책이 보상 모델의 약점을 이용하는 보상 해킹(reward hacking)에 빠진다. 토큰 수준에서 KL은 두 정책의 로그 확률 차이로 근사된다:

```
KL_approx(t) = log pi_theta(x_t | x_{<t}) - log pi_ref(x_t | x_{<t})
```

### KL 추정기의 중요성

최근 연구(Shah et al., 2026)에서 KL 추정기의 배치 위치가 학습 안정성에 결정적 영향을 미친다는 것이 밝혀졌다:

| KL 추정기 | 배치 위치 | 결과 |
|----------|----------|------|
| K1 (나이브 MC) | 보상 내부 (stop_gradient) | 최적 성능 |
| K1 | 손실 내부 | 학습 붕괴 |
| K3 (PPO 원논문) | 보상 내부 | 완전 붕괴 |
| K3 | 손실 내부 | 안정적이나 차선 |

실무 표준: K1 추정기를 보상 내부에 배치하고 stop_gradient를 적용하는 것이 가장 안정적이다.

## LLM에서의 PPO 학습 루프

```
1. 프롬프트 배치 샘플링 (데이터셋에서)
2. Actor가 각 프롬프트에 대해 응답 생성 (on-policy)
3. Reward Model이 각 (프롬프트, 응답) 쌍에 보상 점수 부여
4. Reference Model이 각 토큰의 로그 확률 계산 (KL 패널티용)
5. Critic이 각 토큰 위치의 가치 추정
6. GAE로 토큰별 어드밴티지 계산
7. PPO-CLIP 목적함수로 Actor와 Critic 업데이트
8. 반복
```

핵심 특성: PPO는 온-폴리시(on-policy) 알고리즘이므로, 매 업데이트마다 현재 정책으로 새로운 응답을 생성해야 한다. 이 생성 단계가 LLM PPO 학습의 주요 병목이다.

## 실무적 과제

### 메모리 압박

4개의 대규모 모델을 동시에 GPU에 유지해야 하므로 메모리 요구가 극도로 높다. 완화 전략:
- 양자화 (8비트, 4비트)
- 모델 병렬화/샤딩
- 그래디언트 체크포인팅
- [[lora-qlora-finetuning|LoRA]] 파인튜닝으로 학습 파라미터 축소

### 학습 불안정성

- 정책 그래디언트의 높은 분산 (GAE로 완화)
- 보상 모델의 부정확한 신호
- beta 하이퍼파라미터 튜닝의 민감성
- 비정상 데이터 분포(on-policy 생성으로 인한)

### 데이터 비효율성

온-폴리시 특성상 이전 배치의 데이터를 재사용하지 못하므로, 오프-폴리시 방법(DPO 등) 대비 데이터 효율이 낮다.

## PPO 대안과의 비교

| 측면 | PPO | [[grpo]] | DPO |
|------|-----|---------|-----|
| 데이터 | 온-폴리시 (새 데이터 생성) | 온-폴리시 (그룹 샘플링) | 오프-폴리시 (고정 데이터셋) |
| 모델 수 | 4 (Actor, Critic, RM, Ref) | 3 (Critic 제거) | 1-2 (Actor + Ref) |
| 메모리 | 매우 높음 (~100GB/7B) | 높음 (~25% 절감) | 낮음 (~30GB/7B) |
| 안정성 | 불안정할 수 있음 | PPO 대비 안정적 | 매우 안정적 |
| 강점 | 검증된 표준, 유연한 보상 | 메모리 절감, 단순 구현 | 단순함, 데이터 효율 |

### [[grpo|GRPO]]와의 관계

GRPO는 Critic 네트워크를 제거하고 그룹 내 보상 정규화로 어드밴티지를 계산한다:

```
A_i = (R_i - mean(R_1, ..., R_G)) / std(R_1, ..., R_G)
```

G개의 응답을 샘플링(보통 G=64)하여 그룹 내 상대 비교로 어드밴티지를 추정하므로, Critic이 불필요해져 약 25%의 메모리를 절감한다. DeepSeek-R1이 채택하면서 오픈소스 추론 모델 학습의 표준이 되었다.

### [[dapo|DAPO]]와의 관계

DAPO는 PPO 클리핑의 비대칭성을 활용한다. Clip-Higher 기법으로 상한 클리핑을 완화하여 탐색(exploration)을 장려하면서, Dynamic Sampling으로 보상 분포가 한쪽으로 치우친 프롬프트를 동적으로 필터링하여 학습 안정성을 확보한다.

## PPO가 대체되는 이유와 여전히 유효한 영역

### 대체 동향

1. **메모리 제약**: 4-모델 구조가 대규모에서 비현실적
2. **보상 모델 취약성**: 불완전한 보상 모델이 노이즈가 많은 학습 신호 제공
3. **데이터 비효율**: DPO 계열이 기존 선호 데이터를 재활용
4. **안정성**: DPO 계열이 실무에서 훨씬 안정적

### PPO가 여전히 유효한 영역

- **추론 집약적 태스크**: o1, DeepSeek-R1 등 추론 모델 학습
- **강건한 보상 모델이 있을 때**: [[process-reward-models|프로세스 보상 모델]] 활용 환경
- **검증 가능한 보상**: [[rlvr]] 환경(수학, 코드)에서의 RL 학습
- **탐색이 중요한 상황**: 온-폴리시 탐색이 오프-폴리시 고정 데이터보다 유리한 경우

## 알고리즘 계보

```
온-폴리시 (데이터 생성)
+-- REINFORCE (단순, 높은 분산)
+-- PPO (산업 표준, 4 모델)
|   +-- PPO-CLIP (가장 보편적)
|   +-- PPO-KLPEN (적응적 KL 패널티)
+-- GRPO (그룹 기준선, Critic 제거)
+-- DAPO (비대칭 클리핑 + 동적 샘플링)

오프-폴리시 (고정 데이터셋)
+-- DPO (선호 쌍)
+-- KTO (비쌍 선호/비선호)
+-- SimPO (참조 모델 불필요)
```

## 대표 자료

- [Proximal Policy Optimization Algorithms (Schulman et al., 2017)](https://arxiv.org/abs/1707.06347)
- [Illustrating RLHF (HuggingFace blog)](https://huggingface.co/blog/rlhf)
- [A Guide to Reinforcement Learning Post-Training for LLMs (HuggingFace, 2025)](https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms)

## 관련 문서

- [[rlhf-pipeline]] -- PPO가 3단계 정책 최적화에 사용되는 전체 파이프라인
- [[grpo]] -- PPO의 Critic 제거 변형, DeepSeek-R1이 채택
- [[dapo]] -- PPO 클리핑의 비대칭 활용과 동적 샘플링
- [[kl-divergence-penalty]] -- PPO 보상 함수의 핵심 정규화 메커니즘
- [[reward-model-training]] -- PPO가 소비하는 보상 신호의 원천
- [[direct-preference-optimization]] -- PPO의 오프-폴리시 대안
- [[process-reward-models]] -- PPO와 결합되는 단계별 보상 모델
- [[rlvr]] -- 검증 가능한 보상 환경에서의 PPO/GRPO 활용
- [[reinforcement-learning-for-llm]] -- LLM 강화학습의 상위 개념
- [[lora-qlora-finetuning]] -- PPO 메모리 부담을 줄이는 PEFT 기법
