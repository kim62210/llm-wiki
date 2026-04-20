---
source: arxiv
arxiv_id: "2604.08120"
title: "Small Vision-Language Models are Smart Compressors for Long Video Understanding"
authors: []
date: 2026-04-10
url: "https://arxiv.org/abs/2604.08120"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

긴 비디오 이해를 위해 소규모 Vision-Language Model을 로컬 시간 압축기(temporal compressor)로 활용하는 쿼리 인식 프레임워크 Tempo를 제안. 대규모 VLM을 전체 비디오에 직접 적용하는 대신, 소규모 VLM이 쿼리에 맞춰 비디오 토큰을 효율적으로 압축하는 방식.

## Key Points

- 핵심 기여: 소규모 VLM을 비디오 토큰 압축기로 활용하는 Tempo 프레임워크
- 쿼리 인식(query-aware) 압축: 질문과 관련된 시간 구간에 집중하여 토큰 수 절감
- 긴 비디오 효율성: 전체 비디오를 대규모 모델에 넣는 대신 압축된 표현만 전달
- 소규모 모델의 새로운 역할: 생성 모델이 아닌 압축/필터링 역할로의 활용 패러다임
