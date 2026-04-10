---
title: Contextual Retrieval (Anthropic)
section: RAG & Context Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Contextual Retrieval (Anthropic)

## 기존 큐레이션 요약

- 정의: 청크마다 문서 맥락을 LLM으로 사전 주입한 뒤 임베딩·BM25를 계산하는 기법.
- 왜 중요한가: Anthropic의 원본 기법이 2026년에도 reranking과 결합 시 실패율 67% 감소라는 기준선으로 인용되며, Voyage·Jina 등이 후속 모델(voyage-context-3, late chunking v2)을 내놓는 "contextual embedding" 생태계로 확장됐다.

## 개별 원문 수집 스냅샷

### Introducing Contextual Retrieval (Anthropic)

- URL: https://www.anthropic.com/news/contextual-retrieval
- raw snapshot: `raw/hot-topics-sources/2026-04-10/172-introducing-contextual-retrieval.md`
- 수집 제목: Contextual Retrieval in AI Systems \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Introducing Contextual Retrieval Published Sep 19, 2024 For an AI model to be useful in specific contexts, it often needs access to background knowledge. For an AI model to be useful in specific contexts, it often needs access to background knowledge. For example, customer support chatbots need knowledge about the specific business they're being used for, and legal analyst bots need to know about a vast array of past cases. Developers typically enhance an AI model's knowledge using Retrieval-Augmented Generation (RAG). RAG is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt, significantly enhancing the model's response

### voyage-context-3: Focused Chunk-Level Details With Global Document Context

- URL: https://blog.voyageai.com/2025/07/23/voyage-context-3
- raw snapshot: `raw/hot-topics-sources/2026-04-10/173-voyage-context-3-focused-chunk-level-details-with-global-document-context.md`
- 수집 제목: Introducing voyage-context-3: focused chunk-level details with global document context – Voyage AI

Introducing voyage-context-3: focused chunk-level details with global document context – Voyage AI Home Documentation Blog Company Careers News By Voyage AI · July 23, 2025 Introducing voyage-context-3: focused chunk-level details with global document context TL;DR – We’re excited to introduce voyage-context-3 , a contextualized chunk embedding model that produces vectors for chunks that capture the full document context without any manual metadata and context augmentation, leading to higher retrieval accuracies than with or without augmentation. It’s also simpler, faster and cheaper, and is a drop-in replacement for standard embeddings without downstream workflow changes, also reducing chunking strategy sensitivity. On chunk-level and document-level retrieval tasks, voyage-context-3 outpe

### Late Chunking in Long-Context Embedding Models (Jina AI)

- URL: https://jina.ai/news/late-chunking-in-long-context-embedding-models
- raw snapshot: `raw/hot-topics-sources/2026-04-10/174-late-chunking-in-long-context-embedding-models.md`
- 수집 제목: Late Chunking in Long-Context Embedding Models

Late Chunking in Long-Context Embedding Models searchreorder News Models API keyboard_arrow_down Reader Convert any URL to Markdown for better grounding LLMs. Embeddings World-class multimodal multilingual embeddings. Reranker World-class reranker for maximizing search relevancy. Elastic Inference Service Run Jina models natively inside Elasticsearch. MCP terminalCLIarticlellms.txtsmart_toyAgentsdata_objectSchemamenu_bookDocs Log in login language Theme routine The Lost Context Problem The Solution: Late Chunking Implementation and Qualitative Evaluation Quantitative Evaluation on BEIR Conclusion star Featured Tech blog August 22, 2024 Late Chunking in Long-Context Embedding Models Chunking long documents while preserving contextual information is challenging. We introduce the "Late Chunki

### Late Chunking GitHub (jina-ai/late-chunking)

- URL: https://github.com/jina-ai/late-chunking
- raw snapshot: `raw/hot-topics-sources/2026-04-10/175-late-chunking-github.md`
- 수집 제목: GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub

GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Sm

### Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases (AWS)

- URL: https://aws.amazon.com/blogs/machine-learning/contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases
- raw snapshot: `raw/hot-topics-sources/2026-04-10/176-contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases.md`
- 수집 제목: Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases | Artificial Intelligence

Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases | Artificial Intelligence Skip to Main Content Filter: All English Contact us AWS Marketplace Support My account Search Filter: All Sign in to console Create account AWS Blogs Home Blogs Editions Artificial Intelligence Contextual retrieval in Anthropic using Amazon Bedrock Knowledge Bases by Suheel Farooq, Sharon Li, Venkata Moparthi, Qingwei Li, and Vinita Shadangion 05 JUN 2025in Amazon Bedrock, Amazon Bedrock Knowledge Bases, Amazon Machine Learning, Foundation models, Generative AI, Intermediate (200)Permalink Comments Share For an AI model to perform effectively in specialized domains, it requires access to relevant background knowledge. A customer support chat assistant, for instance, needs detailed information a
