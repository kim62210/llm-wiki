---
title: ACON: Optimizing Context Compression for Long-horizon LLM Agents
category: papers
page_type: paper
tags: [paper, context-engineering, compression, agents]
sources: [raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md]
created: 2026-04-10
updated: 2026-04-10
---

# ACON: Optimizing Context Compression for Long-horizon LLM Agents

장기 실행 에이전트의 문맥 압축을 단순 요약 문제가 아니라 **실패 원인 기반 최적화 문제**로 다룬 논문이다.

## 핵심 기여

- 환경 관측과 상호작용 히스토리를 함께 압축하는 ACON 프레임워크 제안
- 압축 실패 사례를 바탕으로 자연어 압축 가이드라인을 반복 최적화하는 루프 도입
- 큰 압축기를 작은 모델로 distillation하여 추가 모듈 오버헤드를 줄이는 전략 제시

## 결과와 시사점

- AppWorld, OfficeBench, Multi-objective QA에서 peak token을 26~54% 줄이면서 성능을 상당 부분 유지
- 작은 압축기로 distillation해도 95% 이상 정확도를 보존

## 한계

압축 가이드라인 최적화 자체가 별도 루프를 필요로 하므로, 온라인 비용과 파이프라인 복잡도가 늘어날 수 있다.

## 실무 적용 관점

실무에서는 context engineering을 '무엇을 남길까' 수준이 아니라 **어떤 실패를 줄이기 위해 어떤 정보를 보존할까**의 문제로 전환하게 만든다.

## 관련 문서

- [[context-engineering]]
- [[context-folding]]
- [[agent-memory-systems]]
