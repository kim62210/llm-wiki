---
source: arxiv
arxiv_id: "2604.12285"
title: "GAM: Hierarchical Graph-based Agentic Memory for LLM Agents"
authors: ["Zhaofen Wu", "Hanrong Zhang", "Fulin Lin", "Wujiang Xu", "Xinran Xu", "Yankai Chen", "Henry Peng Zou", "Shaowen Chen", "Weizhi Zhang", "Xue Liu", "Philip S. Yu", "Hongwei Wang"]
date: 2026-04-14
url: "https://arxiv.org/abs/2604.12285"
fetched: 2026-04-20
status: pending_ingest
---

## Abstract

LLM 에이전트의 메모리에서 새로운 정보 획득과 기존 지식 유지 사이의 근본적 갈등을 해결하는 프레임워크. 스트림 기반 메모리는 빠르게 업데이트되지만 노이즈 간섭에 취약하고, 구조적 메모리는 지식을 보존하지만 변화하는 컨텍스트에 적응이 어려운 문제를 다룬다.

GAM은 메모리 인코딩과 통합(consolidation)을 분리하는 계층적 그래프 기반 에이전트 메모리 프레임워크를 제안한다.

## Key Points

- 핵심 기여: 메모리 인코딩과 통합의 분리(decoupling)로 간섭 감소 + 장기 일관성 유지
- 방법론: 진행 중인 대화를 Event Progression Graph로 격리하고, 의미적 전환 시점에만 Topic Associative Network로 통합
- 검색: 그래프 가이드 다중 요인(multi-factor) 검색 전략으로 컨텍스트 정밀도 향상
- 결과: LoCoMo, LongDialQA 벤치마크에서 SOTA 대비 추론 정확도 및 효율성 개선
