---
title: Expert Parallelism (전문가 병렬화)
category: training
page_type: concept
tags: [moe, expert-parallelism, distributed-training, all-to-all]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# Expert Parallelism (전문가 병렬화)

## 개념 요약

Expert Parallelism(EP)은 Mixture-of-Experts(MoE, 전문가 혼합) 모델에서 각 expert(전문가 네트워크)를 서로 다른 GPU/장치에 배치하는 병렬화 전략이다. Dense 모델의 Tensor Parallelism(텐서 병렬화)이나 Pipeline Parallelism(파이프라인 병렬화)과 달리, EP는 MoE 레이어의 희소 활성화(sparse activation) 구조를 직접 활용한다.

## 핵심 구조

```mermaid
flowchart LR
    Input[입력 토큰 배치] --> Router[라우터 (Gating)]
    Router -->|Top-K 선택| E1[Expert 1\nGPU 0]
    Router -->|Top-K 선택| E2[Expert 2\nGPU 1]
    Router -->|Top-K 선택| E3[Expert 3\nGPU 2]
    Router -->|Top-K 선택| E4[Expert N\nGPU N]
    E1 & E2 & E3 & E4 --> AllToAll2[All-to-All\n결과 집계]
    AllToAll2 --> Output[출력 집계]
    Input --> AllToAll1[All-to-All\n토큰 분산]
    AllToAll1 --> E1 & E2 & E3 & E4
```

위 다이어그램은 토큰이 라우터를 통해 선택된 expert GPU로 분산되고, 결과가 다시 집계되는 흐름을 보여준다.

## All-to-All 통신 패턴

EP의 핵심 통신 연산은 **All-to-All**이다. MoE 포워드 패스에서 두 번의 All-to-All이 발생한다:

1. **디스패치 단계**: 각 GPU의 토큰을 해당 expert가 있는 GPU로 전송
2. **집계 단계**: expert 처리 결과를 원래 토큰의 GPU로 반환

통신량은 `batch_size x sequence_length x hidden_dim x top_k` 규모이며, 노드 간 대역폭이 병목이 된다.

## Expert 부하분산 문제

라우터가 특정 expert에 편중되면(load imbalance) 일부 GPU는 과부하, 나머지는 유휴 상태가 된다. 이를 해결하는 주요 기법:

- **보조 손실(Auxiliary Loss)**: 균등 분산을 유도하는 손실 항 추가. `load_balancing_loss = alpha * CV^2`
- **Expert Capacity Buffer**: expert당 처리 가능 토큰 수를 고정하고 초과분은 drop
- **Token Dropping vs. Expert Choice**: 토큰이 expert를 선택하는 대신 expert가 처리할 토큰을 선택하는 방식

## DeepSeek V3의 보조손실 없는 라우팅

DeepSeek V3는 보조 손실 없이 부하분산을 달성한 "Auxiliary-Loss-Free Load Balancing" 방식을 도입했다. 라우팅 점수에 동적 바이어스(bias)를 더해 과부하 expert로의 쏠림을 실시간으로 억제한다. 학습 안정성을 해치지 않으면서 균형을 유지한다는 점에서 주목받는다.

## 다른 병렬화 전략과의 직교성

| 병렬화 전략 | 분할 대상 | MoE와 결합 여부 |
|-------------|-----------|----------------|
| Data Parallelism(DP) | 데이터 배치 | 자유롭게 결합 |
| Tensor Parallelism(TP) | 행렬 연산 내부 | 결합 가능 (복잡도 증가) |
| Pipeline Parallelism(PP) | 레이어 단위 | 결합 가능 |
| Expert Parallelism(EP) | Expert 단위 | MoE 전용 |

EP는 DP/TP/PP와 **직교적(orthogonal)**으로 결합할 수 있어 4D 병렬화(DP+TP+PP+EP) 구성이 가능하다. DeepSeek V3 학습은 이 조합을 사용한다.

## 실전 고려사항

- EP degree가 expert 수보다 크면 일부 GPU에 expert가 배치되지 않아 비효율 발생
- 노드 간 All-to-All은 노드 내 All-to-All보다 10-100배 느릴 수 있음 - expert 수를 노드당 GPU 수의 배수로 설계 권장
- Expert 수가 적고 EP degree가 큰 경우 Expert Replication(복제)으로 통신 절감 가능

## 관련 문서
- [[fsdp-vs-deepspeed]] -- FSDP vs DeepSpeed 비교 가이드

- [[tensor-pipeline-parallelism]] - TP/PP와의 결합 구조
- [[deepspeed-zero]] - ZeRO와 EP 연동
- [[deepseek-v3-training]] - EP 실제 적용 사례
- [[mixtral-training]] - MoE 모델 학습 전반
