---
title: LLM을 위한 강화학습 (Reinforcement Learning for LLM)
category: training
page_type: concept
tags: [training, reinforcement-learning, rlhf, rlvr, grpo, dapo, prm, agentic-rl, hub]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

이 페이지는 LLM 학습에 활용되는 강화학습(RL) 기법들의 허브다. 2025-2026년 사이 LLM 포스트 트레이닝의 지형이 근본적으로 변화했다. 1년 전만 해도 표준 레시피는 수조 토큰 사전학습 후 RLHF(인간 선호 라벨 기반 PPO)를 적용하는 것이었다. 2026년 현재 이 레시피는 사실상 대체되었다. DeepSeek-R1에서 Nemotron 3 Super, GPT-5.3 Codex에 이르기까지 주요 모델들이 서로 다른 포스트 트레이닝 스택을 사용한다.

현재의 모듈형 포스트 트레이닝 스택은 세 계층으로 구성된다: SFT(지시 따르기), 선호 최적화(정렬), 검증 가능한 보상 기반 RL(추론 능력). 이 페이지에서 다루는 RL 기법들은 주로 세 번째 계층에 해당한다.

## 핵심 기법 맵

### [[rlvr|RLVR (Reinforcement Learning with Verifiable Rewards)]]

2025년의 가장 중대한 전환은 인간 선호 라벨에서 검증 가능한 보상(verifiable rewards)으로의 이동이었다. [[rlvr|RLVR]]은 정답 검증이 가능한 과제(수학, 코드, 형식 논리 등)에서 프로그래밍적으로 정답을 확인하고, 이를 보상 신호로 사용하여 모델을 학습시킨다. DeepSeek-R1이 순수 RLVR만으로 자기 성찰, 동적 전략 적응 같은 창발적 추론 능력을 만들어낼 수 있음을 시연하면서 패러다임이 확립되었다.

핵심 장점은 인간 라벨러 없이 무한한 학습 신호를 생성할 수 있다는 점이다. 2026년에는 수학/코드를 넘어 과학, 법률 추론 등으로 적용 도메인이 확장되고 있다.

### [[grpo|GRPO (Group Relative Policy Optimization)]]

[[grpo|GRPO]]는 프롬프트당 여러 응답을 샘플링하고, 그룹 내 비교를 통해 어드밴티지를 계산하는 RL 알고리즘이다. PPO와 달리 별도의 크리틱(value) 모델이 불필요하여 메모리와 컴퓨트 비용을 절감하면서 동등하거나 더 나은 성능을 달성한다. DeepSeek-R1의 핵심 학습 알고리즘이며, 2026년 현재 추론 모델 학습의 지배적 알고리즘이 되었다.

PPO와의 핵심 차이: PPO는 상태-가치 함수를 추정하는 크리틱 네트워크가 필요하지만, GRPO는 동일 프롬프트에 대한 그룹 내 응답들의 상대적 보상으로 어드밴티지를 계산한다. 이 설계가 대규모 학습의 안정성과 효율성을 크게 개선한다.

### [[dapo|DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)]]

[[dapo|DAPO]]는 긴 체인-오브-소트(chain-of-thought) 출력을 가진 추론 모델 학습 시 발생하는 특정 불안정성을 해결한다. 4가지 핵심 기법을 도입한다.

1. **Clip-Higher**: 정책 비율의 상한 클리핑을 완화하여 탐색(exploration)을 촉진한다
2. **Dynamic Sampling**: 학습 중 유효하지 않은 샘플을 동적으로 필터링하여 그래디언트 품질을 유지한다
3. **Token-level Policy Gradient Loss**: 시퀀스 수준이 아닌 토큰 수준에서 정책 그래디언트를 계산하여 긴 응답에 대한 편향을 줄인다
4. **Overlong Reward Shaping**: 과도하게 긴 응답에 페널티를 부여하여 효율적 추론을 유도한다

ByteDance가 개발한 오픈소스 시스템으로, 대규모 추론 RL의 실용적 구현에 기여했다.

### [[process-reward-models|PRM (Process Reward Models)]]

[[process-reward-models|PRM]]은 최종 결과만 평가하는 결과 보상 모델(ORM)과 달리, 추론 과정의 각 단계를 개별적으로 평가하여 보상을 부여하는 스텝 레벨 검증자다. 올바른 추론 과정을 거쳐 올바른 답에 도달하는 것과, 잘못된 추론으로 우연히 올바른 답을 얻는 것을 구분할 수 있다.

PRM은 두 가지 맥락에서 활용된다. 첫째, 학습 시간에 RLVR/GRPO의 보상 신호를 보강한다. 둘째, 추론 시간에 여러 후보 응답 중 최선을 선택하는 검증자(verifier)로 활용된다. 2026년에는 PRM이 에이전트 도구 호출 궤적의 각 단계를 평가하는 온라인 PRM으로 확장되고 있다.

### [[agentic-rl|Agentic RL (Tool-Integrated Reasoning 학습)]]

[[agentic-rl|Agentic RL]]은 도구 호출, 환경 상호작용을 포함한 에이전트 궤적 전체를 RL로 최적화하는 패러다임이다. 단순한 텍스트 생성을 넘어, 검색, 코드 실행, API 호출 등을 포함한 복합 행동 시퀀스에서 보상을 최대화한다.

기존 RLVR/GRPO가 텍스트 추론 능력을 최적화한다면, Agentic RL은 환경과의 상호작용 능력까지 최적화한다. 에이전트가 어떤 도구를 언제, 어떤 순서로 호출할지를 학습하며, 이는 [[process-reward-models|PRM]]의 온라인 변형과 결합되어 궤적의 각 단계를 평가한다.

## 기법 간 관계

```
RLHF (인간 선호)
  |
  +-- DPO/SimPO (오프라인, 크리틱/보상 모델 불필요)
  |
  +-- PPO (온라인, 크리틱 모델 필요)
       |
       +-- GRPO (크리틱 제거, 그룹 상대 비교)
       |    |
       |    +-- DAPO (긴 CoT 안정성 개선)
       |
       +-- RLVR (검증 가능한 보상으로 전환)
            |
            +-- PRM (스텝-레벨 보상 세분화)
            |
            +-- Agentic RL (도구 호출 궤적 최적화)
```

## 2026년 트렌드

**GRPO가 지배적**: 추론 모델 학습에서 PPO를 사실상 대체했다. Training-Free GRPO, Scaffolded GRPO(Scaf-GRPO) 등 변형이 활발히 연구되고 있다.

**RLVR의 도메인 확장**: 수학/코드를 넘어, 프로그래밍적으로 검증 가능한 모든 도메인(과학, 법률 형식 논증, 데이터 분석 등)으로 확산 중이다.

**Agentic RL의 부상**: 에이전트 시스템이 프로덕션에 진입하면서, 도구 사용 능력의 RL 최적화가 핵심 연구 영역으로 부상했다.

**추론 시간 스케일링과의 결합**: 학습 시간 RL(학습 컴퓨트 투자)과 추론 시간 스케일링(추론 컴퓨트 투자)의 최적 균형을 찾는 연구가 활발하다.

## 관련 문서

- [[rlvr]] -- 검증 가능한 보상 기반 강화학습
- [[grpo]] -- Group Relative Policy Optimization
- [[dapo]] -- GRPO의 안정성 개선 변형
- [[process-reward-models]] -- 스텝 레벨 보상 모델
- [[agentic-rl]] -- 에이전트 도구 사용 RL
- [[rl-scaling-laws]] -- RL 학습의 스케일링 법칙
- [[test-time-compute-scaling]] -- 추론 시간 컴퓨트 스케일링
- [[knowledge-distillation]] -- 추론 능력의 증류
- [[on-policy-distillation]] -- 온-폴리시 증류
