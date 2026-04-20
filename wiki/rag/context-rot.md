---
title: Context Rot & Effective Context Window
category: rag
page_type: concept
tags: [rag, concept, context, rot]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/context-rot.md, raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md, raw/hot-topics-sources/2026-04-10/163-ruler-what-s-the-real-context-size-of-your-[[long-context-scaling|long-context]]-language-models.md, raw/hot-topics-sources/2026-04-10/164-longbench-v2-towards-deeper-understanding-and-reasoning-on-realistic-long-contex.md, raw/hot-topics-sources/2026-04-10/165-longbench-v2-project-page.md, raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md]
created: 2026-04-10
updated: 2026-04-13
---
# Context Rot & Effective Context Window

입력 길이가 늘수록 LLM 성능이 단조적으로 저하되는 현상.

## 왜 중요한가

2026년 1M-10M 토큰 윈도우가 쏟아지지만 Chroma·Morph 보고서가 모든 프런티어 모델의 유효 [[context-engineering|컨텍스트]]가 광고의 60-70%에 불과함을 재확인하며, "effective context" 측정이 RAG 설계의 핵심 화두가 됐다.

## 대표 레퍼런스

- [Context Rot: How Increasing Input Tokens Impacts LLM Performance (Chroma)](https://www.trychroma.com/research/context-rot)
- [RULER: What's the Real Context Size of Your Long-Context Language Models? (NVIDIA)](https://github.com/NVIDIA/RULER)
- [LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://arxiv.org/abs/2412.15204)
- [LongBench v2 Project Page](https://longbench2.github.io/)
- [[[lost-in-the-middle-paper|Lost in the Middle]]: How Language Models Use Long Contexts (TACL)](https://arxiv.org/abs/2307.03172)

## 운영 관점

2026년 1M-10M 토큰 윈도우가 쏟아지지만 Chroma·Morph 보고서가 모든 프런티어 모델의 유효 컨텍스트가 광고의 60-70%에 불과함을 재확인하며, "effective context" 측정이 RAG 설계의 핵심 화두가 됐다. 실제 운영에서는 retrieval quality 하나만 보는 것이 아니라 latency, index 비용, update 빈도, multi-hop 질의 대응 여부를 함께 봐야 한다.

## 실무 관점

실무에서는 검색 품질만이 아니라 컨텍스트 예산, chunking, 메모리 구조, 재랭킹, 운영 비용까지 함께 고려해야 한다. 그래서 이 토픽은 검색 정확도보다 '어떤 상황에서 어떤 구조를 쓰는가' 관점으로 읽는 것이 유용하다.

## 관련 문서
- [[chunkkv-paper]]
- [[lost-in-the-middle-paper]]

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agentic-rag|Agentic RAG with Hierarchical Retrieval Interfaces]]
- [[context-rot-report|Context Rot Report]] — 컨텍스트 길이 증가와 실제 유효성 저하 보고서

