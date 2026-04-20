---
source: arxiv
arxiv_id: "2602.05665"
title: "Graph-based Agent Memory: Taxonomy, Techniques, and Applications"
authors: ["Chang Yang", "Chuang Zhou", "Yilin Xiao", "Su Dong", "Luyao Zhuang", "Yujing Zhang", "Zhu Wang", "Zijin Hong", "Zheng Yuan", "Zhishang Xiang", "Shengyuan Chen", "Huachi Zhou", "Qinggang Zhang", "Ninghao Liu", "Jinsong Su", "Xinrun Wang", "Yi Chang", "Xiao Huang"]
date: 2026-02-05
url: "https://arxiv.org/abs/2602.05665"
fetched: 2026-04-20
status: pending_ingest
tags: [agent-memory, graph-based-memory, knowledge-graph, long-horizon-tasks, memory-lifecycle, survey]
---

## Abstract

"Memory is the core module in LLM-based agents for long-horizon complex tasks (multi-turn dialogue, game playing, scientific discovery)". Graph-based memory 구조를 extraction, storage, retrieval, evolution 전 memory lifecycle 관점에서 종합 정리한 survey.

## 메모리 분류 차원

| 차원 | 분류 |
|------|------|
| **Temporal scope** | Short-term vs long-term |
| **Content type** | Knowledge-based vs experience-based |
| **Structure** | Non-structural vs structural (graph-based) |
| **Implementation** | Graph-based architectural approaches |

## 왜 Graph 구조인가

- **Relational dependency** 모델링에 최적
- **Hierarchical information** 계층화 가능
- 효율적 retrieval 지원 (노드/엣지 기반)
- Self-evolving memory (노드·엣지 동적 추가) 용이

## Memory Lifecycle

1. **Extraction**: 대화·경험에서 entity·relation 추출
2. **Storage**: Graph DB, vector index 병용
3. **Retrieval**: 그래프 탐색 + semantic similarity
4. **Evolution**: 새 정보 통합, 오래된 노드 압축·제거

## 대표 구현

- **GraphRAG** (엔티티/텍스트 청크 기반)
- **A-MEM** (Zettelkasten 방식, 동적 인덱싱)
- **LiCoMemory** (CogniGraph, 계층적 semantic indexing)
- **PlugMem** (knowledge-centric memory graph, task-agnostic)
- **H-MEM** (Hierarchical Memory, 인덱스 라우팅)

## 응용

- Multi-turn dialogue (LoCoMo, LongMemEval 벤치마크)
- Game playing agent의 장기 state tracking
- Scientific discovery agent의 iterative reasoning
- Coding agent의 codebase 이해·업데이트

## 오픈 챌린지

- 시간적 일관성(temporal consistency) 유지
- 메모리 스케일(수백만 entity) 시 retrieval latency
- 노이즈·잘못된 정보의 graph 전파 방지
- Retrieval-augmented vs pure memory 경계

## Raw 요약 키워드
graph memory, Zettelkasten, GraphRAG, A-MEM, LiCoMemory, PlugMem, H-MEM, memory lifecycle, LoCoMo
