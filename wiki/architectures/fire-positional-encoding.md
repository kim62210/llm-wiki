---
title: FIRE / DAPE 위치 인코딩
category: architectures
page_type: concept
tags: [fire, dape, positional-encoding, learnable, mlp-based, extrapolation]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-17
updated: 2026-04-17
---

# FIRE / DAPE 위치 인코딩

MLP 기반 **학습 가능한 위치 편향**을 어텐션에 추가하는 방식. [[alibi-positional-encoding|ALiBi]]가 고정 선형 편향을 사용하는 데 반해, FIRE(Functional Interpolation for Relative Embeddings)는 상대 거리를 MLP에 통과시켜 **데이터 적응적 위치 편향**을 생성한다.

```mermaid
flowchart LR
    D[상대 거리 i-j] --> Norm[정규화 0-1]
    Norm --> MLP[소형 MLP]
    MLP --> Bias[위치 편향 b_ij]
    Bias --> Attn[어텐션 점수 + b_ij]
```

## 위치 인코딩 계보에서의 위치

| 방식 | 학습 가능 | 외삽 | 적용 위치 |
|------|----------|------|----------|
| Sinusoidal | 아니오 | 제한적 | 입력 임베딩 |
| [[rotary-position-embedding\|RoPE]] | 아니오 | NTK/YaRN 필요 | Q,K 회전 |
| [[alibi-positional-encoding\|ALiBi]] | 아니오 | 자연적 | 어텐션 편향 |
| **FIRE** | **예 (MLP)** | **자연적** | **어텐션 편향** |

FIRE는 학습을 통해 비선형 거리-편향 관계를 포착하면서, 정규화된 입력 덕분에 학습 길이를 넘는 외삽도 자연스럽게 처리한다.

## 관련 문서

- [[alibi-positional-encoding]] -- ALiBi
- [[rotary-position-embedding]] -- RoPE
- [[positional-interpolation]] -- 위치 보간
- [[long-context-scaling]] -- Long Context Scaling
