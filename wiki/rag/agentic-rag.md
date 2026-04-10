---
title: Agentic RAG with Hierarchical Retrieval Interfaces
category: rag
page_type: concept
tags: [rag, concept, agentic, rag]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/agentic-rag.md, raw/hot-topics-sources/2026-04-10/167-a-rag-scaling-agentic-retrieval-augmented-generation-via-hierarchical-retrieval-.md, raw/hot-topics-sources/2026-04-10/168-agentic-retrieval-augmented-generation-a-survey-on-agentic-rag.md, raw/hot-topics-sources/2026-04-10/169-a-rag-github-repository.md, raw/hot-topics-sources/2026-04-10/170-agenticrag-survey-github.md, raw/hot-topics-sources/2026-04-10/171-hero-adaptive-orchestration-of-agentic-rag-on-heterogeneous-mobile-soc.md]
created: 2026-04-10
updated: 2026-04-10
---
# Agentic RAG with Hierarchical Retrieval Interfaces

LLM이 검색 도구를 스스로 호출·반복하며 다단계 탐색을 수행하는 RAG 패러다임.

## 왜 중요한가

2026년 2월 A-RAG 논문이 keyword/semantic/chunk-read 3-tool 인터페이스로 멀티홉 QA SOTA를 경신했고, Agentic RAG Survey가 4월 1일자로 개정되며 reflection·planning·tool-use를 기본으로 하는 RAG 파이프라인이 표준으로 자리잡고 있다.

## 대표 레퍼런스

- [A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces (arXiv 2602.03442)](https://arxiv.org/abs/2602.03442)
- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG (arXiv 2501.09136)](https://arxiv.org/abs/2501.09136)
- [A-RAG GitHub Repository](https://github.com/Ayanami0730/arag)
- [AgenticRAG-Survey GitHub (Singh et al.)](https://github.com/asinghcsu/AgenticRAG-Survey)
- [HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC (arXiv 2603.01661)](https://arxiv.org/abs/2603.01661)

## 2026년 4월 큐레이션 요약

- 정의: LLM이 검색 도구를 스스로 호출·반복하며 다단계 탐색을 수행하는 RAG 패러다임.
- 왜 중요한가: 2026년 2월 A-RAG 논문이 keyword/semantic/chunk-read 3-tool 인터페이스로 멀티홉 QA SOTA를 경신했고, Agentic RAG Survey가 4월 1일자로 개정되며 reflection·planning·tool-use를 기본으로 하는 RAG 파이프라인이 표준으로 자리잡고 있다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×3, github.com×2

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/agentic-rag.md`

### source별 핵심 신호

- **[2602.03442] A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces** (`arxiv.org`): https://arxiv.org/abs/2602.03442
  - 메모: Frontier language models have demonstrated strong reasoning and long-horizon tool-use capabilities. However, existing RAG systems fail to leverage these capabilities.
- **[2501.09136] Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** (`arxiv.org`): https://arxiv.org/abs/2501.09136
  - 메모: Large Language Models (LLMs) have advanced artificial intelligence by enabling human-like text generation and natural language understanding.
- **GitHub - Ayanami0730/arag: A-RAG: Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces. State-of-the-art RAG framework with keyword, semantic, and chunk read tools for multi-hop QA. · GitHub** (`github.com`): https://github.com/Ayanami0730/arag
  - 메모: To see all available qualifiers, see our documentation.
- **GitHub - asinghcsu/AgenticRAG-Survey: Agentic-RAG explores advanced Retrieval-Augmented Generation systems enhanced with AI LLM agents. · GitHub** (`github.com`): https://github.com/asinghcsu/AgenticRAG-Survey
  - 메모: To see all available qualifiers, see our documentation.
- **[2603.01661] HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC** (`arxiv.org`): https://arxiv.org/abs/2603.01661
  - 메모: With the increasing computational capability of mobile devices, deploying agentic retrieval-augmented generation (RAG) locally on heterogeneous System-on-Chips (SoCs) has become a promising way to enhance LLM-based appli

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[context-rot|Context Rot & Effective Context Window]]
- [[contextual-retrieval|Contextual Retrieval (Anthropic)]]
