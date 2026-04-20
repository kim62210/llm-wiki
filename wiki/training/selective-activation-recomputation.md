---
title: 선택적 활성값 재계산 (Selective Activation Recomputation)
category: training
page_type: concept
tags: [activation-recomputation, checkpointing, memory, gpu, nvidia-sac]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-17
updated: 2026-04-17
---

# 선택적 활성값 재계산

레이어 전체가 아닌 **연산 단위**로 체크포인트를 선택해 재계산 오버헤드를 최소화하는 메모리 절감 기법. NVIDIA의 SAC(Selective Activation Checkpointing)가 대표적.

```mermaid
flowchart TD
    subgraph Full[전체 재계산]
        F1[순전파] --> Save1[전부 저장 OR 전부 재계산]
    end
    subgraph Selective[선택적 재계산]
        S1[순전파] --> Keep[비싼 연산 결과 저장<br/>어텐션 출력]
        S1 --> Recomp[싼 연산만 재계산<br/>GeLU, LayerNorm]
    end
```

## 왜 "선택적"인가

| 연산 | 메모리 비용 | 재계산 비용 | 전략 |
|------|-----------|-----------|------|
| 어텐션 QKV | **높음** | 높음 | **저장** |
| GeLU/SwiGLU | 중간 | **낮음** | **재계산** |
| LayerNorm | 낮음 | **매우 낮음** | **재계산** |
| Dropout 마스크 | 낮음 | 재현 필요 | 저장 |

전체 활성값 체크포인팅은 순전파를 2회 수행해 ~33% 오버헤드. 선택적 재계산은 **5-10% 오버헤드**로 메모리를 대폭 절감.

## 관련 문서

- [[distributed-training-overview]] -- 분산 학습
- [[flash-attention]] -- FlashAttention (메모리 효율)
- [[data-parallelism-fsdp]] -- FSDP
