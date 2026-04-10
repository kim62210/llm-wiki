---
title: Contextual Retrieval (Anthropic)
category: rag
page_type: concept
tags: [rag, concept, contextual, retrieval, rag-and-context-engineering]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/contextual-retrieval.md, raw/hot-topics-sources/2026-04-10/172-introducing-contextual-retrieval.md, raw/hot-topics-sources/2026-04-10/173-voyage-context-3-focused-chunk-level-details-with-global-document-context.md, raw/hot-topics-sources/2026-04-10/174-late-chunking-in-long-context-embedding-models.md, raw/hot-topics-sources/2026-04-10/175-late-chunking-github.md, raw/hot-topics-sources/2026-04-10/176-contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases.md]
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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: www.anthropic.com 1건, blog.voyageai.com 1건, jina.ai 1건
- source 조합: 구현체, 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/contextual-retrieval.md`
- [Contextual Retrieval in AI Systems \ Anthropic](https://www.anthropic.com/news/contextual-retrieval) — `raw/hot-topics-sources/2026-04-10/172-introducing-contextual-retrieval.md`
  - 메모: --- title: Contextual Retrieval in AI Systems \ Anthropic source_url: https://www.anthropic.com/news/contextual-retrieval final_url: https://www.anthropic.com/engineering/contextual-retrieval status: 200 content_type: text/html; charset=utf-8 topics: [Contextual Retrieval (Anthro
- [Introducing voyage-context-3: focused chunk-level details with global document context – Voyage AI](https://blog.voyageai.com/2025/07/23/voyage-context-3) — `raw/hot-topics-sources/2026-04-10/173-voyage-context-3-focused-chunk-level-details-with-global-document-context.md`
  - 메모: --- title: Introducing voyage-context-3: focused chunk-level details with global document context – Voyage AI source_url: https://blog.voyageai.com/2025/07/23/voyage-context-3 final_url: https://blog.voyageai.com/2025/07/23/voyage-context-3/ status: 200 content_type: text/html; c
- [Late Chunking in Long-Context Embedding Models](https://jina.ai/news/late-chunking-in-long-context-embedding-models) — `raw/hot-topics-sources/2026-04-10/174-late-chunking-in-long-context-embedding-models.md`
  - 메모: --- title: Late Chunking in Long-Context Embedding Models source_url: https://jina.ai/news/late-chunking-in-long-context-embedding-models final_url: https://jina.ai/news/late-chunking-in-long-context-embedding-models/ status: 200 content_type: text/html; charset=utf-8 topics: [Co
- [GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub](https://github.com/jina-ai/late-chunking) — `raw/hot-topics-sources/2026-04-10/175-late-chunking-github.md`
  - 메모: --- title: GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub source_url: https://github.com/jina-ai/late-chunking final_url: https://github.com/jina-ai/late-chunking status: 200 content_type: text/html; charset=utf-8 topic
- [Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases | Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases) — `raw/hot-topics-sources/2026-04-10/176-contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases.md`
  - 메모: --- title: Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases | Artificial Intelligence source_url: https://aws.amazon.com/blogs/machine-learning/contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases final_url: https://aws.amazon.com/blogs/mac

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[agentic-rag]]
- [[letta]]
