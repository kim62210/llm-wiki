---
source: arxiv
arxiv_id: "2412.09871"
title: "Byte Latent Transformer: Patches Scale Better Than Tokens"
authors: ["Meta FAIR"]
date: 2024-12-13
url: "https://arxiv.org/abs/2412.09871"
fetched: 2026-04-15
status: pending_ingest
---

## Abstract

The Byte Latent Transformer (BLT) is a tokenizer-free architecture that learns from raw byte data. It matches the performance of tokenization-based models at scale with significant improvements in efficiency and robustness.

BLT dynamically groups bytes into patches based on the entropy of the next byte, allocating more compute to complex/unpredictable parts and less to predictable parts.

## Key Points

- 핵심 기여: 토크나이저 없이 원시 바이트에서 직접 학습하는 아키텍처
- 엔트로피 기반 동적 패칭: 예측 가능한 데이터에는 긴 패치, 복잡한 데이터에는 짧은 패치
- 훈련/추론 효율성 향상: 예측 가능한 데이터에서 긴 패치 선택으로 효율 개선
- 추론 및 long-tail 일반화에서 질적 개선
- BoundlessBPE와 함께 토크나이저 없는 미래 방향 제시
