---
title: Contextual Retrieval (Anthropic)
category: rag
page_type: concept
tags: [rag, concept, contextual, retrieval, rag-and-context-engineering]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/contextual-retrieval.md, raw/hot-topics-sources/2026-04-10/172-introducing-contextual-retrieval.md, raw/hot-topics-sources/2026-04-10/173-voyage-context-3-focused-chunk-level-details-with-global-document-context.md, raw/hot-topics-sources/2026-04-10/174-late-chunking-in-long-context-[[contextual-embeddings|embedding]]-models.md, raw/hot-topics-sources/2026-04-10/175-late-chunking-github.md, raw/hot-topics-sources/2026-04-10/176-contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases.md]
created: 2026-04-10
updated: 2026-04-13
---
# Contextual Retrieval (Anthropic)

이 페이지는 Contextual Retrieval (Anthropic)를 다룬다. 핵심은 청크마다 문서 맥락을 LLM으로 사전 주입한 뒤 임베딩·BM25를 계산하는 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

청크마다 문서 맥락을 LLM으로 사전 주입한 뒤 임베딩·BM25를 계산하는 기법.

## 왜 지금 중요한가

Anthropic의 원본 기법이 2026년에도 reranking과 결합 시 실패율 67% 감소라는 기준선으로 인용되며, Voyage·Jina 등이 후속 모델(voyage-context-3, late chunking v2)을 내놓는 "contextual embedding" 생태계로 확장됐다.

## 대표 자료

- [Introducing Contextual Retrieval (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
- [voyage-context-3: Focused Chunk-Level Details With Global Document Context](https://blog.voyageai.com/2025/07/23/voyage-context-3/)
- [Late Chunking in Long-Context Embedding Models (Jina AI)](https://jina.ai/news/late-chunking-in-long-context-embedding-models/)
- [Late Chunking GitHub (jina-ai/late-chunking)](https://github.com/jina-ai/late-chunking)
- [Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases (AWS)](https://aws.amazon.com/blogs/machine-learning/contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases/)

## 운영 관점

Anthropic의 원본 기법이 2026년에도 reranking과 결합 시 실패율 67% 감소라는 기준선으로 인용되며, Voyage·Jina 등이 후속 모델(voyage-context-3, late chunking v2)을 내놓는 "contextual embedding" 생태계로 확장됐다. 실제 운영에서는 retrieval quality 하나만 보는 것이 아니라 latency, index 비용, update 빈도, multi-hop 질의 대응 여부를 함께 봐야 한다.

## 실무 관점

실무에서는 검색 품질만이 아니라 컨텍스트 예산, chunking, 메모리 구조, 재랭킹, 운영 비용까지 함께 고려해야 한다. 그래서 이 토픽은 검색 정확도보다 '어떤 상황에서 어떤 구조를 쓰는가' 관점으로 읽는 것이 유용하다. Contextual Retrieval이 제공하는 맥락 풍부화 청크는 [[agentic-knowledge-base-patterns|Agentic Knowledge Base Patterns]]에서 에이전트가 지식 베이스를 탐색하는 방식의 품질을 직접 결정한다.

## 관련 문서
- [[letta-stateful-agent-runtime]]

- [[ai-hot-topics-2026-04]]
- [[agentic-rag]]
- [[rag-architecture-evolution-2026]] -- 2026년 [[agentic-rag|RAG]] 아키텍처 전반 진화 동향
- [[letta-stateful-agent-runtime]]
- [[agentic-knowledge-base-patterns]] -- 에이전트 지식 베이스 탐색 패턴

