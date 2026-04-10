---
title: Contextual Retrieval (Anthropic)
category: rag
page_type: concept
tags: [rag, concept, contextual, retrieval, rag-and-context-engineering]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
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

## 2026년 4월 핫토픽 맥락

Anthropic의 원본 기법이 2026년에도 reranking과 결합 시 실패율 67% 감소라는 기준선으로 인용되며, Voyage·Jina 등이 후속 모델(voyage-context-3, late chunking v2)을 내놓는 "contextual embedding" 생태계로 확장됐다.

### 추가 레퍼런스

- [Introducing Contextual Retrieval (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
- [voyage-context-3: Focused Chunk-Level Details With Global Document Context](https://blog.voyageai.com/2025/07/23/voyage-context-3/)
- [Late Chunking in Long-Context Embedding Models (Jina AI)](https://jina.ai/news/late-chunking-in-long-context-embedding-models/)
- [Late Chunking GitHub (jina-ai/late-chunking)](https://github.com/jina-ai/late-chunking)
- [Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases (AWS)](https://aws.amazon.com/blogs/machine-learning/contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases/)

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[agentic-rag]]
- [[letta]]
