---
title: Open Post-Training Recipes (Tülu 3 / OLMo 3)
category: training
page_type: summary
tags: [training, summary, open, post, recipes, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/open-post-training-recipes.md, raw/hot-topics-sources/2026-04-10/305-tulu-3-pushing-frontiers-in-open-language-model-post-training.md, raw/hot-topics-sources/2026-04-10/306-tulu-3-opens-language-model-post-training.md, raw/hot-topics-sources/2026-04-10/307-olmo-3-charting-a-path-through-the-model-flow-to-lead-open-source-ai.md, raw/hot-topics-sources/2026-04-10/308-scaling-the-tulu-3-post-training-recipes-to-surpass-deepseek-v3.md, raw/hot-topics-sources/2026-04-10/309-allenai-open-instruct.md]
created: 2026-04-10
updated: 2026-04-15
---
# Open Post-Training Recipes (Tülu 3 / OLMo 3)

Ai2(Allen Institute for AI)가 공개한 SFT(Supervised Fine-Tuning) → DPO(Direct Preference Optimization) → RLVR(Reinforcement Learning with Verifiable Rewards) 전체 파이프라인의 완전 오픈소스 포스트 트레이닝(post-training) 레시피.

## 정의

SFT → DPO → RLVR 전체 파이프라인을 완전 공개한 오픈소스 포스트 트레이닝 레시피. 데이터, 코드, 학습 곡선, 평가 결과까지 모두 포함해 재현 가능한(reproducible) 방식으로 배포.

## 왜 중요한가

Ai2가 Tülu 3에 이어 OLMo 3까지 데이터·코드·학습 곡선을 전부 공개하며, 폐쇄형 모델 대비 "따라잡기(catch-up)" 속도가 2026년 화두가 됐다. 특히 Tülu 3 405B 스케일에서 DeepSeek V3를 능가한 결과는 오픈소스 포스트 트레이닝의 실효성을 강하게 증명했다.

## 3단계 파이프라인

```mermaid
flowchart LR
    Base[기반 모델\n예: Llama 3.1] --> SFT
    SFT[SFT\n지도 파인튜닝] --> DPO
    DPO[DPO\n선호 최적화] --> RLVR
    RLVR[RLVR\n검증 가능한 보상 RL] --> Final[최종 모델\nTülu / OLMo]
```

각 단계는 독립적으로 선택·조합할 수 있어 레시피 유연성이 높다.

## 단계별 세부 내용

### 1단계: SFT
- 다양한 태스크 형식의 합성 데이터(synthetic data)와 인간 작성 예시 혼합
- 채팅 포맷, 코드 생성, 추론 문제 등 광범위 커버리지
- open-instruct 코드베이스로 구현

### 2단계: DPO (Direct Preference Optimization)
- 사람이 직접 비교한 선호 데이터 없이 합성 선호 쌍(preference pair) 사용
- RLHF(Reinforcement Learning from Human Feedback) 대비 구현 단순, 안정적
- 거절(refusal)·안전성·지시 따르기(instruction-following) 향상

### 3단계: RLVR (RL with Verifiable Rewards)
- 코드 실행·수학 풀이처럼 **자동 검증 가능한** 태스크에만 적용
- 외부 검증기가 스칼라 보상 제공 → 표준 PPO 또는 GRPO로 업데이트
- 추론(reasoning) 능력 비약적 향상의 핵심 단계

## Tülu 3 vs OLMo 3 비교

| 항목 | Tülu 3 | OLMo 3 |
|------|--------|--------|
| 기반 모델 | Llama 3.1 | OLMo 2 (자체 사전학습) |
| 최대 규모 | 405B | 미정 (확장 중) |
| 공개 범위 | 데이터·코드·레시피 | 모델 가중치·학습 과정 포함 |
| 특징 | DeepSeek V3 능가 (405B) | 완전 오픈 생태계 |

## 실무 적용 관점

- **알맞은 출발점 선택**: 소규모 팀은 Tülu 3 8B 레시피부터 시작해 단계별로 확장하는 것이 현실적
- **RLVR 적용 조건**: 검증 가능한 태스크가 없으면 DPO까지만 적용하고 RLVR 단계 생략
- **open-instruct 코드베이스**: 커스텀 데이터셋으로 교체하면 도메인별 포스트 트레이닝 가능

## 대표 자료

- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/pdf/2411.15124)
- [Tülu 3 opens language model post-training (Ai2 blog)](https://allenai.org/blog/tulu-3)
- [OLMo 3: Charting a path through the model flow to lead open-source AI (Ai2 blog)](https://allenai.org/blog/olmo3)
- [Scaling the Tülu 3 post-training recipes to surpass DeepSeek V3 (Ai2 blog)](https://allenai.org/blog/tulu-3-405B)
- [AllenAI open-instruct (post-training codebase)](https://github.com/allenai/open-instruct)

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[test-time-training-and-self-improvement|Test-Time Training & Self-Improvement]]
- [[on-policy-distillation|On-Policy Distillation]]
- [[rl-scaling-laws|RL Scaling Laws (ScaleRL)]]
- [[corpus-grounded-self-play|Corpus-Grounded Self-Play (SPICE 계열)]]
