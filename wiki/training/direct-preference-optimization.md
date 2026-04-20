---
title: Direct Preference Optimization (DPO, SimPO, KTO)
category: training
page_type: concept
tags: [training, concept, dpo, simpo, kto, preference-optimization, post-training]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# Direct Preference Optimization (DPO, SimPO, KTO)

## 개요

Direct Preference Optimization(DPO)은 보상 모델과 강화학습 루프 없이 인간 선호도 데이터만으로 언어 모델을 직접 정렬하는 기법이다. 2023년 Rafailov 등이 "Your Language Model is Secretly a Reward Model" 논문에서 제안했으며, 기존 [[reward-model-training|보상 모델 학습]] + PPO 파이프라인의 복잡성과 불안정성을 근본적으로 단순화했다. DPO의 성공 이후 SimPO, KTO, ORPO 등 다양한 변형이 등장하며 후학습(post-training) 스택의 핵심 축으로 자리 잡았다.

## 핵심 메커니즘

### DPO의 원리

RLHF 파이프라인에서 보상 모델 r(x, y)을 학습한 뒤 PPO로 정책을 최적화하는 대신, DPO는 최적 정책과 보상 함수 사이의 닫힌 형태(closed-form) 관계를 활용한다. Bradley-Terry 모델 하에서 최적 정책은 참조 모델 대비 로그 확률 비율로 표현되므로, 보상 모델을 명시적으로 학습하지 않고 선호도 쌍(preferred/rejected)에 대한 이진 교차 엔트로피 손실만으로 정책을 직접 최적화할 수 있다.

DPO의 목적함수에서 y_w는 선호 응답, y_l은 비선호 응답이고, pi_ref는 참조 모델(SFT 모델)이다. beta는 [[kl-divergence-penalty|KL 발산 패널티]]의 강도를 조절하는 온도 파라미터로, 값이 클수록 참조 모델에 가깝게 유지되고, 작을수록 선호도 데이터에 적극적으로 적응한다. 이 구조는 보상 모델 + PPO의 2단계 파이프라인을 단일 분류 손실로 압축하여 구현 복잡도와 하이퍼파라미터 민감도를 크게 줄인다.

### SimPO: 참조 모델 없는 단순화

SimPO(Simple Preference Optimization, 2024)는 DPO에서 참조 모델 pi_ref를 완전히 제거한다. 시퀀스의 평균 로그 확률을 암묵적 보상으로 사용하여 모델 생성 과정과 보상 신호를 더 잘 정렬시킨다. 참조 모델을 제거함으로써 GPU 메모리 사용량이 절반으로 줄고, 학습 처리량이 증가한다. AlpacaEval 2에서 DPO 대비 최대 6.4점, Arena-Hard에서 최대 7.5점 향상을 보였으며, NeurIPS 2024에서 발표되었다.

### KTO: 쌍이 아닌 단일 피드백

KTO(Kahneman-Tversky Optimization)는 선호도 쌍 대신 개별 응답에 대한 이진 피드백(좋음/나쁨)만으로 학습한다. 행동경제학의 전망 이론(Prospect Theory)에서 영감을 받아 손실 회피(loss aversion) 개념을 목적함수에 반영한다. 인간은 동일 크기의 이익보다 손실에 더 크게 반응하므로, 나쁜 응답에서 멀어지는 그래디언트가 좋은 응답으로 가까워지는 그래디언트보다 더 강하게 작용한다. 실무에서는 쌍을 이루는 비교 데이터보다 단일 평가 데이터가 수집하기 훨씬 쉽기 때문에, [[preference-data-collection|선호도 데이터 수집]] 비용을 크게 줄일 수 있다.

### ORPO: 지도학습과 선호 최적화의 통합

ORPO(Odds Ratio Preference Optimization)는 SFT와 선호도 최적화를 단일 단계로 통합한다. 일반적인 교차 엔트로피 손실에 오즈비(odds ratio) 기반 페널티를 추가하여, 별도의 SFT 단계 없이 지시 따르기와 선호 정렬을 동시에 학습한다. 학습 파이프라인이 한 단계 줄어드는 실무적 이점이 있다.

## DPO vs PPO-RLHF 비교

| 항목 | PPO-RLHF | DPO | SimPO |
|------|----------|-----|-------|
| 보상 모델 | 별도 학습 필요 | 불필요 (암묵적) | 불필요 |
| 참조 모델 | KL 계산용 필요 | 필요 | 불필요 |
| 학습 안정성 | 낮음 (PPO 하이퍼파라미터 민감) | 높음 | 높음 |
| 구현 복잡도 | 높음 (4개 모델 동시 운용) | 낮음 (분류 손실) | 매우 낮음 |
| 온라인 탐색 | 가능 | 불가 (오프라인) | 불가 (오프라인) |
| 데이터 요구 | 선호도 쌍 + 보상 학습 데이터 | 선호도 쌍 | 선호도 쌍 |

## 한계와 열린 문제

- **오프라인 학습의 제약**: DPO 계열은 고정된 선호도 데이터셋에서 학습하므로, 학습 중 정책이 생성하는 분포와 데이터 분포 사이의 괴리(distribution shift)가 발생한다. 이는 [[grpo|GRPO]]나 [[rlvr|RLVR]] 같은 온라인 RL 방식이 여전히 필요한 이유다.
- **보상 해킹 가능성**: 암묵적 보상이 길이, 형식, 문체 같은 표면적 단서에 과적합될 수 있다. [[reward-model-training|보상 모델 학습]]에서 다루는 보상 해킹 문제가 DPO에서도 유사하게 나타난다.
- **선호도 데이터 품질 의존**: 학습 성능이 [[preference-data-collection|선호도 데이터]]의 품질에 직접적으로 의존하며, 노이즈가 많은 데이터에서 성능이 급격히 하락한다.
- **다단계 추론에서의 한계**: 수학이나 코딩 같은 긴 추론 체인에서는 최종 결과만 비교하는 DPO보다 [[process-reward-models|프로세스 보상 모델]]이나 [[grpo|GRPO]] 기반 접근이 더 효과적이다.

## 2026년 현재 위치

2025-2026년 시점에서 후학습 스택은 단일 기법이 아닌 조합으로 운영된다. 일반적인 패턴은 SFT -> DPO/SimPO (초기 정렬) -> 온라인 RL([[grpo|GRPO]], [[dapo|DAPO]]) (추론 강화)의 순서다. DPO 계열은 빠르고 안정적인 초기 정렬에, 온라인 RL은 추론 능력 극대화에 각각 강점을 보이며 상호 보완적으로 사용된다.

## 대표 자료

- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model (Rafailov et al., 2023)](https://arxiv.org/abs/2305.18290)
- [SimPO: Simple Preference Optimization with a Reference-Free Reward (NeurIPS 2024)](https://arxiv.org/abs/2405.14734)
- [A Comprehensive Survey of Direct Preference Optimization (2024)](https://arxiv.org/html/2410.15595v3)

## 관련 문서
- [[trl-library]] -- TRL -- HuggingFace 포스트트레이닝 풀스택 라이브러리
- [[sparse-bitnet]] -- Sparse-BitNet -- 1.58-bit 극저비트 + N:M 희소성 결합 학습
- [[qwen-25-training]] -- Qwen 2.5 학습 (18T 토큰, 다국어, Long-Context)
- [[phi-4-training]] -- Phi-4 학습 (합성 데이터 40%, PTS DPO, 교사 모델 초월)
- [[axolotl]] -- Axolotl -- YAML 기반 LLM 파인튜닝 프레임워크

- [[grpo]] -- DPO의 오프라인 한계를 극복하는 온라인 RL 대안
- [[dapo]] -- GRPO 기반 대규모 추론 RL 시스템
- [[rlvr]] -- 검증 가능한 보상을 활용한 온라인 RL
- [[reward-model-training]] -- DPO가 대체하려는 명시적 보상 모델 학습
- [[kl-divergence-penalty]] -- DPO의 beta 파라미터가 암묵적으로 수행하는 역할
- [[preference-data-collection]] -- DPO 학습에 필요한 선호도 데이터 구축
- [[process-reward-models]] -- 다단계 추론에서 DPO를 보완하는 스텝별 보상
