---
title: Context Rot & Effective Context Window
category: rag
page_type: concept
tags: [rag, concept, context, rot]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/context-rot.md, raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md, raw/hot-topics-sources/2026-04-10/163-ruler-what-s-the-real-context-size-of-your-long-context-language-models.md, raw/hot-topics-sources/2026-04-10/164-longbench-v2-towards-deeper-understanding-and-reasoning-on-realistic-long-contex.md, raw/hot-topics-sources/2026-04-10/165-longbench-v2-project-page.md, raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md]
created: 2026-04-10
updated: 2026-04-10
---
# Context Rot & Effective Context Window

입력 길이가 늘수록 LLM 성능이 단조적으로 저하되는 현상.

## 왜 중요한가

2026년 1M-10M 토큰 윈도우가 쏟아지지만 Chroma·Morph 보고서가 모든 프런티어 모델의 유효 컨텍스트가 광고의 60-70%에 불과함을 재확인하며, "effective context" 측정이 RAG 설계의 핵심 화두가 됐다.

## 대표 레퍼런스

- [Context Rot: How Increasing Input Tokens Impacts LLM Performance (Chroma)](https://www.trychroma.com/research/context-rot)
- [RULER: What's the Real Context Size of Your Long-Context Language Models? (NVIDIA)](https://github.com/NVIDIA/RULER)
- [LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://arxiv.org/abs/2412.15204)
- [LongBench v2 Project Page](https://longbench2.github.io/)
- [Lost in the Middle: How Language Models Use Long Contexts (TACL)](https://arxiv.org/abs/2307.03172)

## 2026년 4월 큐레이션 요약

- 정의: 입력 길이가 늘수록 LLM 성능이 단조적으로 저하되는 현상.
- 왜 중요한가: 2026년 1M-10M 토큰 윈도우가 쏟아지지만 Chroma·Morph 보고서가 모든 프런티어 모델의 유효 컨텍스트가 광고의 60-70%에 불과함을 재확인하며, "effective context" 측정이 RAG 설계의 핵심 화두가 됐다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×2, trychroma.com×1, github.com×1, longbench2.github.io×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/context-rot.md`

### source별 핵심 신호

- **Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma** (`trychroma.com`): https://www.trychroma.com/research/context-rot
  - 메모: Context Rot: How Increasing Input Tokens Impacts LLM Performance
- **GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub** (`github.com`): https://github.com/NVIDIA/RULER
  - 메모: To see all available qualifiers, see our documentation.
- **[2412.15204] LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks** (`arxiv.org`): https://arxiv.org/abs/2412.15204
  - 메모: This paper introduces LongBench v2, a benchmark designed to assess the ability of LLMs to handle long-context problems requiring deep understanding and reasoning across real-world multitasks.
- **LongBench v2** (`longbench2.github.io`): https://longbench2.github.io
  - 메모: Benchmarking Deeper Understanding and Reasoning on Realistic Long-context Multitasks
- **Lost in the Middle: How Language Models Use Long Contexts** (`arxiv.org`): https://arxiv.org/abs/2307.03172
  - 메모: While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agentic-rag|Agentic RAG with Hierarchical Retrieval Interfaces]]
