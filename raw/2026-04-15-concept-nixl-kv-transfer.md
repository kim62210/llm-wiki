---
source: web
title: "NIXL - RDMA-Based KV Cache Transfer for Disaggregated Inference"
url: "https://www.spheron.network/blog/prefill-decode-disaggregation-gpu-cloud/"
date: 2026-03-25
fetched: 2026-04-15
status: pending_ingest
---

## Overview

NIXL은 2026년 기준 vLLM과 NVIDIA Dynamo 모두에서 KV 캐시 전송의 표준 메커니즘. Prefill-Decode disaggregation을 위해 GPU 간 KV 캐시를 sub-millisecond로 전송.

## Why NIXL

Prefill-Decode 분리 아키텍처에서 핵심 병목:
- Prefill 노드에서 생성된 KV 캐시를 Decode 노드로 전송해야 함
- Llama 3.1 70B (FP8, 8k 컨텍스트, 배치 8): 배치당 ~10GB KV 캐시 전송 필요
- 기존 TCP/IP로는 지연 시간이 과도

## Technical Details

- RDMA (Remote Direct Memory Access) 사용
- InfiniBand 또는 RoCE 인터커넥트
- Sub-millisecond 지연 시간
- 커널 바이패스로 CPU 오버헤드 최소화
- NVLink도 같은 노드 내 GPU 간 전송에 활용

## Ecosystem

- vLLM: disaggregated prefill 실험적 지원
- NVIDIA Dynamo: 프로덕션급 PD disaggregation
- SGLang: 독립적 PD disaggregation 구현
- llm-d: Kubernetes 네이티브 PD disaggregation

## Requirements

- 같은 로컬 네트워크의 워커
- 고속 인터커넥트 (InfiniBand/NVLink 이상)
- RDMA 지원 NIC
