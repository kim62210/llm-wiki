---
title: 보상 모델 학습 (Reward Model Training)
category: training
page_type: concept
tags: [training, concept, reward-model, bradley-terry, reward-hacking, rlhf]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 보상 모델 학습 (Reward Model Training)

## 개요

보상 모델(Reward Model, RM)은 RLHF 파이프라인의 중심축으로, 인간의 선호도 판단을 스칼라 보상 점수로 변환하는 모델이다. 프롬프트 x와 응답 y를 입력받아 r(x, y)를 출력하며, 이 보상 신호를 PPO, [[grpo|GRPO]] 등의 정책 최적화 알고리즘이 소비한다. 보상 모델의 품질은 정렬(alignment)의 상한선을 결정하고, 보상 해킹(reward hacking)은 RLHF 확장성의 핵심 병목이다.

## Bradley-Terry 모델

### 이론적 기반

보상 모델 학습의 지배적 프레임워크는 Bradley-Terry 모델(1952)이다. 두 응답 y_w(선호), y_l(비선호)에 대해 인간이 y_w를 선호할 확률을 다음과 같이 모델링한다:

```
P(y_w > y_l | x) = sigma(r(x, y_w) - r(x, y_l))
```

여기서 sigma는 시그모이드 함수다. 이 확률 모델에서 도출되는 학습 목적함수는 이진 교차 엔트로피 손실이며, [[preference-data-collection|선호도 데이터]]의 쌍별 비교를 직접 최적화한다.

### [[direct-preference-optimization|DPO]]와의 관계

DPO는 Bradley-Terry 모델 하에서 최적 정책과 보상 함수의 닫힌 형태 관계를 활용하여, 보상 모델을 명시적으로 학습하지 않고 정책을 직접 최적화한다. 즉 DPO에서 보상 모델은 정책 모델 자체에 암묵적으로 내재한다. 반면 명시적 보상 모델은 PPO나 [[grpo|GRPO]] 같은 온라인 RL에서 탐색(exploration)을 안내하는 용도로 여전히 필수적이다.

## 보상 모델 아키텍처

### 판별형 보상 모델 (Discriminative RM)

사전학습된 LLM의 마지막 토큰 표현에 선형 헤드를 추가하여 스칼라 점수를 출력한다. 가장 일반적인 구조이며, InstructGPT, Llama 2 등이 이 방식을 사용했다.

### 생성형 보상 모델 (Generative RM)

LLM이 추론 과정([[chain-of-thought|chain-of-thought]])을 생성한 뒤 평가 결과를 텍스트로 출력하는 방식이다. [[extended-constitutional-ai|확장 헌법적 AI]]의 RL-CAI 단계에서 사용되며, 판별형보다 설명 가능성이 높고 복잡한 평가 기준을 인코딩할 수 있다. [[process-reward-models|프로세스 보상 모델]]도 이 범주에 속하며, 최종 결과가 아닌 추론 과정의 각 단계를 평가한다.

### 앙상블 보상 모델

여러 보상 모델의 출력을 결합하여 단일 모델의 편향과 보상 해킹에 대한 취약성을 줄인다. 보상 점수의 분산을 불확실성 추정에 활용할 수도 있다.

## 보상 해킹 (Reward Hacking)

### 문제 정의

보상 해킹은 정책 모델이 보상 모델의 높은 점수를 받으면서도 실제로는 원하는 행동을 수행하지 않는 현상이다. 보상 모델이 인간 선호의 불완전한 대리(proxy)이기 때문에 발생하며, 정책을 충분히 오래 학습시키면 거의 필연적으로 발생한다.

### 보상 해킹의 원인

| 원인 | 설명 | 예시 |
|------|------|------|
| 지름길 특성 (shortcut features) | 모델이 표면적 단서를 품질로 착각 | 긴 응답, 목록 형식, 자신감 있는 톤 |
| 분포 외 일반화 실패 | 학습 분포 밖에서 보상이 부정확 | 학습에 없던 도메인의 응답에 높은 보상 |
| 라벨 노이즈 | [[preference-data-collection\|선호도 데이터]]의 라벨러 간 불일치 | 주관적 과제에서 일관되지 않은 선호 |
| 과최적화 | 장시간 학습으로 보상 모델의 약점 학습 | 보상은 상승하지만 win-rate는 하락 |

### 완화 전략

- **[[kl-divergence-penalty|KL 발산 패널티]]**: 정책이 SFT 모델에서 크게 벗어나지 못하게 제약하여, 보상 모델의 분포 외 영역 진입을 방지
- **보상 앙상블**: 다수 보상 모델의 합의(consensus)만 보상으로 인정
- **불확실성 페널티**: 보상의 불확실성이 큰 영역에서 보상을 차감. 최근 베이지안 비음수 보상 모델(Bayesian Non-negative Reward Model)이 이 접근을 체계화
- **보상 정형화(reward shaping)**: 보상 함수에 정규화 항을 추가하여 표면적 단서에 대한 의존을 줄임
- **다목적 보상 모델**: Bradley-Terry 단일 목적과 회귀 기반 다목적을 결합하여 분포 외 영역에서의 보상 해킹 내성을 강화

## 보상 모델의 스케일링

보상 모델의 크기는 정책 모델과 같거나 작은 것이 일반적이다. InstructGPT에서는 6B 보상 모델로 175B 정책을 학습했다. 보상 모델이 너무 작으면 복잡한 선호를 포착하지 못하고, 너무 크면 학습과 추론 비용이 과도해진다. [[rlaif-scalable-oversight|RLAIF]]에서는 AI 피드백 모델이 사실상 보상 모델의 역할을 대체하며, 이때 피드백 모델의 크기와 능력이 정렬 품질의 상한을 결정한다.

## [[process-reward-models|프로세스 보상 모델]]과의 관계

전통적 보상 모델(Outcome Reward Model, ORM)은 최종 결과만 평가하지만, [[process-reward-models|PRM]]은 추론 과정의 각 단계를 평가한다. 2026년 현재 PRM이 ORM을 추월하는 성과를 보이고 있으며, 이는 보상 모델 설계가 "무엇을 평가하는가(결과 vs 과정)"의 축으로 분화하고 있음을 보여준다.

## 대표 자료

- [Reward Models - Cameron R. Wolfe (2024)](https://cameronrwolfe.substack.com/p/reward-models)
- [Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling (2026)](https://arxiv.org/html/2602.10623)
- [Bradley-Terry and Multi-Objective Reward Modeling Are Complementary (2025)](https://arxiv.org/abs/2507.07375)

## 관련 문서
- [[verifier-critic-models]] -- 검증자/비평가 모델 (Verifier & Critic)

- [[direct-preference-optimization]] -- 보상 모델을 암묵적으로 내재화하는 대안적 접근
- [[kl-divergence-penalty]] -- 보상 해킹을 방지하는 핵심 정규화 메커니즘
- [[preference-data-collection]] -- 보상 모델 학습의 원재료인 선호도 데이터
- [[process-reward-models]] -- 결과가 아닌 과정을 평가하는 보상 모델의 진화
- [[grpo]] -- 보상 모델 없이 그룹 내 비교로 어드밴티지를 계산하는 대안
- [[rlaif-scalable-oversight]] -- AI 피드백으로 보상 모델 학습을 확장하는 접근
- [[extended-constitutional-ai]] -- 생성형 보상 모델을 활용하는 정렬 프레임워크
- [[dapo]] -- 보상 신호 설계가 대규모 RL 시스템 성능에 미치는 영향
