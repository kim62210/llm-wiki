---
source: arxiv
arxiv_id: "2603.03296"
title: "PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents"
authors: ["Ke Yang", "Zixi Chen", "Xuan He", "Jize Jiang", "Michel Galley", "Chenglong Wang", "Jianfeng Gao", "Jiawei Han", "ChengXiang Zhai"]
date: 2026-03-06
url: "https://arxiv.org/abs/2603.03296"
fetched: 2026-04-20
status: pending_ingest
tags: [agent-memory, plugin-memory, knowledge-graph, graphrag-alternative, task-agnostic, long-horizon]
---

## Abstract

LLM 에이전트의 장기 메모리 문제를 다루는 **task-agnostic plugin memory module**. 임의 LLM 에이전트에 부착 가능하며, episodic memory를 raw experience가 아닌 "propositional·prescriptive knowledge"의 compact knowledge graph로 구조화.

## 핵심 아이디어

- **Knowledge as unit of memory**: 엔티티·텍스트 청크가 아닌 **knowledge proposition**을 메모리 단위로 사용
- 인지과학 원리 차용 — 인간이 경험을 abstract knowledge로 저장하는 방식 모방
- Task-specific redesign 불필요 → 어떤 에이전트든 plug-and-play

## GraphRAG와의 차이

| 비교 | GraphRAG | PlugMem |
|------|----------|---------|
| 메모리 단위 | 엔티티 / text chunk | Propositional / prescriptive knowledge |
| 구조 | Entity-centric graph | Knowledge-centric graph |
| 재사용성 | Task-specific tuning 필요 | Task-agnostic |
| 정보 밀도 | 중간 | **최고** (비교 실험 기준) |

## 벤치마크 결과

세 가지 benchmark에서 평가:

1. **Long-horizon conversational QA** (LoCoMo 등)
2. **Multi-hop knowledge retrieval**
3. **Web agent tasks**

→ Task-agnostic baseline 대비 일관되게 우수, task-specific memory design도 초과.

## 정보 밀도 분석

Information-theoretic 분석으로 "per-unit memory가 담는 정보량"을 측정, PlugMem이 compact한 표현을 유지함을 증명.

## 시사점

- 메모리 설계가 "어떤 정보를 어떻게 저장하는가"에서 "어떤 추상화 단위로 저장하는가"로 이동
- Plug-and-play 메모리가 에이전트 표준 인프라가 될 가능성
- Knowledge-centric 접근이 [[agent-memory-systems]], [[knowledge-graph-llm]] 설계 원칙과 수렴

## Raw 요약 키워드
PlugMem, task-agnostic memory, knowledge-centric graph, propositional knowledge, GraphRAG comparison, LoCoMo, information density
