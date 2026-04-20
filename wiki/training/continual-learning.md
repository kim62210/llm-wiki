---
title: 지속적 학습 (Continual Learning)
category: training
page_type: concept
tags: [continual-learning, catastrophic-forgetting, lifelong-learning, incremental-learning, stability-plasticity]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---

# 지속적 학습 (Continual Learning)

## 개요

지속적 학습(Continual Learning)은 모델이 새로운 태스크나 데이터를 순차적으로 학습하면서도 이전에 습득한 지식을 유지하는 학습 패러다임이다. 인간이 평생에 걸쳐 새로운 기술을 배우면서도 기존 지식을 잃지 않는 것과 유사한 능력을 기계에 부여하려는 시도로, "평생 학습(Lifelong Learning)" 또는 "점진적 학습(Incremental Learning)"이라고도 불린다. 지속적 학습의 핵심 과제는 **파국적 망각(catastrophic forgetting)** -- 새 태스크를 학습할 때 이전 태스크의 성능이 급격히 하락하는 현상 -- 을 극복하는 것이다.

## 파국적 망각 (Catastrophic Forgetting)

### 발생 원인

신경망의 파라미터는 모든 태스크에 공유된다. 새 태스크를 학습하면 경사 하강법이 새 태스크의 손실을 최소화하는 방향으로 가중치를 갱신하는데, 이 과정에서 이전 태스크에 중요했던 파라미터 값이 덮어씌워진다. 이것이 **안정성-가소성 딜레마(stability-plasticity dilemma)**의 핵심이다:

| 속성 | 설명 | 극단적 경우 |
|------|------|------------|
| **안정성(Stability)** | 기존 지식 보존 능력 | 새 태스크 학습 불가 |
| **가소성(Plasticity)** | 새 지식 흡수 능력 | 이전 지식 완전 망각 |

### 허위 망각 (Spurious Forgetting)

최근 연구(ICLR 2024)에서는 성능 하락의 상당 부분이 실제 지식 상실이 아니라 **태스크 정렬(task alignment) 저하** 때문이라는 관점이 제시되었다. 즉 모델이 지식 자체를 잃은 것이 아니라, 해당 지식을 올바른 맥락에서 활성화하는 능력이 저하된 것이다. 이 발견은 완화 전략의 방향성에 중요한 시사점을 제공한다.

## 완화 전략

지속적 학습의 망각 완화 전략은 크게 세 가지 범주로 분류된다.

### 1. 정규화 기반 (Regularization-based)

이전 태스크에 중요한 파라미터의 변경을 제한하는 방식이다.

| 기법 | 핵심 아이디어 | 특징 |
|------|-------------|------|
| **EWC (Elastic Weight Consolidation)** | Fisher 정보 행렬로 파라미터 중요도 측정, 중요 파라미터 변경에 페널티 | 태스크별 Fisher 행렬 저장 필요 |
| **SI (Synaptic Intelligence)** | 학습 경로를 따라 파라미터 기여도를 온라인으로 추적 | EWC보다 메모리 효율적 |
| **LwF (Learning without Forgetting)** | [[knowledge-distillation|지식 증류]] 활용, 이전 모델 출력을 소프트 타겟으로 사용 | 이전 데이터 불필요 |

정규화 기법은 추가 메모리가 적지만, 태스크 수가 많아지면 제약 조건이 누적되어 새 태스크 학습 능력이 저하될 수 있다.

### 2. 리플레이 기반 (Replay-based)

이전 태스크의 데이터(또는 그 대리물)를 새 태스크 학습 시 함께 사용한다.

- **경험 리플레이 (Experience Replay)**: 이전 태스크 샘플의 일부를 메모리 버퍼에 저장하고 새 태스크 학습 시 혼합
- **생성적 리플레이 (Generative Replay)**: GAN이나 [[autoencoders-vae|VAE]] 등 생성 모델로 이전 태스크의 유사 데이터를 합성
- **기능적 리플레이 (Functional Replay)**: 입출력 매핑 자체를 보존하여 특정 입력에 대한 모델 행동 유지

리플레이 기법은 직관적이고 효과적이지만, 메모리 버퍼 크기 관리와 개인정보가 포함된 데이터의 저장 문제가 존재한다.

### 3. 아키텍처 기반 (Architecture-based)

네트워크 구조 자체를 변경하여 태스크별 전용 용량을 확보한다.

- **파라미터 격리 (Parameter Isolation)**: 태스크별 서브네트워크를 할당 (PackNet, HAT 등)
- **동적 확장 (Dynamic Expansion)**: 새 태스크 학습 시 네트워크에 뉴런이나 모듈을 추가 (Progressive Neural Networks)
- **모듈러 접근 (Modular Approach)**: 공유 백본 + 태스크별 어댑터 구조

아키텍처 기반 방법은 태스크 간 간섭이 구조적으로 차단되지만, 태스크 수에 비례하여 모델 크기가 증가하는 한계가 있다.

## LLM 시대의 지속적 학습

대규모 언어 모델(LLM)에서 지속적 학습은 새로운 차원의 과제를 제시한다.

### 주요 시나리오

| 시나리오 | 설명 | 예시 |
|---------|------|------|
| **지속적 사전학습** | 새 도메인/언어 데이터로 기반 모델 확장 | 의료 코퍼스 추가 학습 |
| **지속적 미세조정** | 순차적 태스크에 대한 [[instruction-tuning\|지시 튜닝]] | 번역 -> 요약 -> QA 순차 학습 |
| **지속적 정렬** | [[rlhf-pipeline\|RLHF]]/DPO 기반 선호 정렬의 반복 갱신 | 정책 변경에 따른 정렬 업데이트 |

### LLM 특유의 도전

- **스케일**: 수십억 파라미터에 대한 Fisher 행렬 계산이 비현실적
- **지식 분산**: 지식이 레이어와 어텐션 헤드에 분산 저장되어 중요도 측정이 복잡
- **능력 상충**: 코딩 능력 강화가 창의적 글쓰기 능력을 저하시키는 등 고차원적 트레이드오프
- **평가 어려움**: 벤치마크 점수만으로는 미묘한 능력 변화를 포착하기 어려움

### 실용적 접근

현재 LLM에서 가장 널리 사용되는 지속적 학습 전략은 [[lora-qlora-finetuning|LoRA]]를 활용한 모듈러 접근이다. 태스크별 LoRA 어댑터를 학습하고, 추론 시 적절한 어댑터를 선택하거나 병합하는 방식은 기반 모델의 지식을 보존하면서 새 능력을 추가하는 효과적인 방법이다.

## 평가 지표

지속적 학습 시스템은 다음 지표로 평가한다:

| 지표 | 정의 |
|------|------|
| **평균 정확도 (Average Accuracy)** | 모든 태스크에 대한 현재 성능의 평균 |
| **망각 측정 (Forgetting Measure)** | 각 태스크의 최고 성능 대비 현재 성능 하락 정도 |
| **전방 전이 (Forward Transfer)** | 이전 태스크 학습이 미래 태스크에 미치는 긍정적 영향 |
| **후방 전이 (Backward Transfer)** | 새 태스크 학습이 이전 태스크 성능에 미치는 영향 (음수면 망각) |

## 관련 문서

- [[knowledge-distillation]] -- LwF 등 증류 기반 망각 완화 기법의 기반
- [[lora-qlora-finetuning]] -- LLM 지속적 학습의 실용적 접근법
- [[transfer-learning]] -- 지속적 학습과 밀접한 전이 학습 개념
- [[instruction-tuning]] -- 지속적 미세조정의 대표적 시나리오
- [[rlhf-pipeline]] -- 지속적 정렬의 기반 파이프라인

## 참고 자료

- [Continual Learning of Large Language Models: A Comprehensive Survey (ACM Computing Surveys 2025)](https://dl.acm.org/doi/10.1145/3735633)
- [A Comprehensive Survey of Continual Learning: Theory, Method and Application (arXiv)](https://arxiv.org/abs/2302.00487)
- [Efficient Streaming Language Models with Attention Sinks (ICLR 2024)](https://arxiv.org/abs/2309.17453)
