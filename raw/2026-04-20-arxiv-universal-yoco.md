---
source: arxiv
arxiv_id: "2604.01220"
title: "Universal YOCO for Efficient Depth Scaling"
authors: []
date: 2026-04-01
url: "https://arxiv.org/abs/2604.01220"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

표준 Transformer가 추론 시점에서 계산을 효율적으로 스케일링하기 어려운 문제를 해결하는 논문. YOCO(You Only Cache Once) 디코더-디코더 아키텍처에 재귀적 계산(recursive computation)을 결합하여, 파라미터 공유를 통한 다중 반복 수행이 가능한 Universal Self-Decoder를 구현한다.

## Key Points

- 핵심 기여: YOCO 아키텍처 + 재귀적 계산 = Universal Self-Decoder
- 파라미터 공유를 통한 다중 반복으로 깊이(depth) 스케일링 효율 달성
- 추론 시점 계산(inference-time compute) 효율적 확장 문제 해결
- YOCO 원래 장점(캐시 1회만) 유지하면서 깊이 방향 표현력 확장
