---
source: arxiv
arxiv_id: "2604.13634"
title: "Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference"
authors: ["Xuwen Zhou", "Fangxin Liu", "Chao Wang", "Xiao Zheng", "Hao Zheng", "Min He", "Li Jiang", "Haibing Guan"]
date: 2026-04-15
url: "https://arxiv.org/abs/2604.13634"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

Calibrated Speculative Decoding은 훈련이 필요 없는(training-free) 프레임워크로, 온라인 교정 메모리(Online Correction Memory)를 통해 과거 거부 이력에서 학습하고 시맨틱 일관성 게이팅(Semantic Consistency Gating)으로 정확한 토큰 매칭 대신 확률 비율을 활용한다. 최대 2.33배의 처리량 향상을 달성하며, 기존 검증 방식에서 버려지던 유효 토큰을 복구한다.

## Key Points

- Training-free framework
- Online Correction Memory learns from historical rejections
- Semantic Consistency Gating uses probability ratios instead of exact token matching
- 2.33x peak throughput speedup
- Recovers valid tokens discarded by standard verification
