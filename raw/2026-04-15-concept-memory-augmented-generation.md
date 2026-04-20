---
source: web
title: "Memory-Augmented Generation (MAG) - Persistent Memory for LLMs"
url: "https://www.emergentmind.com/topics/memory-augmented-llm"
date: 2026-04-01
fetched: 2026-04-15
status: pending_ingest
---

## Overview

Memory-Augmented Generation(MAG)은 LLM에 명시적 외부 메모리를 통합하여 유한한 컨텍스트 윈도우, 부실한 장기 기억, 업데이트 불가능성 등의 한계를 극복하는 패러다임.

## Why MAG

- 순수 LLM: 무상태(stateless) 상호작용, 컨텍스트 윈도우 제한
- Full-context 접근: 비용 폭발, p95 지연 증가
- MAG: 외부 메모리로 선택적 검색, 비용/지연 절감

## Key Systems (2025-2026)

| 시스템 | 특징 |
|--------|------|
| Mem0 | 범용 메모리 레이어, LLM judge 메트릭 26% 개선 |
| LightMem | 경량 MAG, 성능-효율 균형 |
| MAGMA | 멀티그래프 기반 에이전틱 메모리 아키텍처 |
| EverMemOS | 자기조직화 메모리 OS, 구조화된 장기 추론 |
| Memori | 효율적 컨텍스트 인식 LLM 에이전트용 영속 메모리 레이어 |

## Performance

- Mem0/MIRIX: LLM judge 메트릭 최대 26% 상대 개선
- p95 지연 91% 감소
- 토큰 비용 90% 이상 절감 (full-context 대비)

## Architecture Patterns

1. **Retrieval-based Memory**: 벡터 DB에 과거 상호작용 저장, 유사도 검색
2. **Graph-based Memory**: 지식 그래프로 엔티티/관계 구조화
3. **Hierarchical Memory**: 단기/장기/에피소딕 메모리 계층
4. **Self-Organizing Memory**: 자동 분류/정리/망각
