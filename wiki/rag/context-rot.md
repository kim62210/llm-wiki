---
title: Context Rot & Effective Context Window
category: rag
page_type: concept
tags: [rag, concept, context, rot]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
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

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[agentic-rag|Agentic RAG with Hierarchical Retrieval Interfaces]]
