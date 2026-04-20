---
source: web
title: "Corrective RAG (CRAG) - Self-Reflective Retrieval with Correction"
url: "https://arxiv.org/abs/2501.09136"
date: 2026-01-15
fetched: 2026-04-15
status: pending_ingest
---

## Overview

Corrective RAG(CRAG)는 검색된 문서를 동적으로 평가하고, 교정 조치를 수행하며, 쿼리를 정제하여 생성 응답의 품질을 높이는 RAG 패턴.

## Core Mechanism

1. **검색 문서 평가**: 각 문서의 관련성을 동적으로 평가
2. **교정 단계 트리거**: 관련성 임계값 미달 시 교정 단계 실행
3. **쿼리 정제**: 의미 이해를 활용한 쿼리 재구성
4. **대안 소스 접근**: 컨텍스트 불충분 시 웹 검색 또는 대체 데이터 소스 접근

## CRAG vs Standard RAG

| 측면 | Standard RAG | Corrective RAG |
|------|-------------|----------------|
| 검색 결과 | 그대로 사용 | 관련성 평가 후 필터링 |
| 낮은 관련성 | 무시하거나 그대로 포함 | 교정 조치 + 재검색 |
| 쿼리 | 단일 쿼리 | 자동 정제/분해 |
| 환각 | 높은 위험 | 자기반성으로 감소 |

## Self-Reflective RAG

- 모델이 자신의 검색과 출력을 스스로 평가
- 증거가 약하거나 답변에 확신이 낮으면 재쿼리
- 고위험 도메인(의료, 법률)에서 환각 대폭 감소

## 2026 Status

- Agentic RAG에서 CRAG는 지배적 패턴으로 자리잡음
- 전문 에이전트가 검색과 검증을 병렬 처리
- A-RAG: 계층적 검색 인터페이스로 확장
