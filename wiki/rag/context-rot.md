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
- [Lost in the Middle: How Language Models Use Long Contexts (TACL)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 2건, www.trychroma.com 1건, github.com 1건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/context-rot.md`
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma](https://www.trychroma.com/research/context-rot) — `raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md`
  - 메모: --- title: Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma source_url: https://www.trychroma.com/research/context-rot final_url: https://www.trychroma.com/research/context-rot status: 200 content_type: text/html; charset=utf-8 topics: [Context Engineerin
- [GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub](https://github.com/NVIDIA/RULER) — `raw/hot-topics-sources/2026-04-10/163-ruler-what-s-the-real-context-size-of-your-long-context-language-models.md`
  - 메모: --- title: GitHub - NVIDIA/RULER: This repo contains the source code for RULER: What’s the Real Context Size of Your Long-Context Language Models? · GitHub source_url: https://github.com/NVIDIA/RULER final_url: https://github.com/NVIDIA/RULER status: 200 content_type: text/html; 
- [[2412.15204] LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://arxiv.org/abs/2412.15204) — `raw/hot-topics-sources/2026-04-10/164-longbench-v2-towards-deeper-understanding-and-reasoning-on-realistic-long-contex.md`
  - 메모: --- title: [2412.15204] LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks source_url: https://arxiv.org/abs/2412.15204 final_url: https://arxiv.org/abs/2412.15204 status: 200 content_type: text/html; charset=utf-8 topics: [Context Rot &
- [LongBench v2](https://longbench2.github.io) — `raw/hot-topics-sources/2026-04-10/165-longbench-v2-project-page.md`
  - 메모: --- title: LongBench v2 source_url: https://longbench2.github.io final_url: https://longbench2.github.io status: 200 content_type: text/html; charset=utf-8 topics: [Context Rot & Effective Context Window] sections: [RAG & Context Engineering] fetched_at: 2026-04-10T01:43:47.44754
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — `raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md`
  - 메모: # [2307.03172] Lost in the Middle: How Language Models Use Long Contexts We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors.[Donate](https://info.arxiv.org/about/donate.html) Sear

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agentic-rag|Agentic RAG with Hierarchical Retrieval Interfaces]]
