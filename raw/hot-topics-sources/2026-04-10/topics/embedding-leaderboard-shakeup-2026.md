---
title: Qwen3 / Voyage-4 Embedding Leaderboard Shakeup
section: RAG & Context Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Qwen3 / Voyage-4 Embedding Leaderboard Shakeup

## 기존 큐레이션 요약

- 정의: MTEB v2·다국어 벤치마크를 주도하는 최신 오픈·상용 임베딩 모델 세대.
- 왜 중요한가: Qwen3-Embedding-8B가 MTEB Multilingual 1위(70.58)를 차지하며 오픈웨이트가 Gemini Embedding과 격차를 급속 좁혔고, Voyage는 voyage-4/4-large/4-lite/4-nano (Apache 2.0)를 2026년 전반에 투입하며 상용·오픈 양쪽의 기준선을 끌어올렸다.

## 개별 원문 수집 스냅샷

### Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models (arXiv 2506.05176)

- URL: https://arxiv.org/abs/2506.05176
- raw snapshot: `raw/hot-topics-sources/2026-04-10/192-qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models.md`
- 수집 제목: [2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models

[2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2506.05176 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2506.05176 (cs) [Submitted on 5 Jun 2025 (v1), last revised 11 Jun 2025 (this version, v3)] Title:Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models Authors:Yanzhao Zhang, Mingxin Li, Din

### Qwen3 Embedding Blog Announcement

- URL: https://qwenlm.github.io/blog/qwen3-embedding
- raw snapshot: `raw/hot-topics-sources/2026-04-10/193-qwen3-embedding-blog-announcement.md`
- 수집 제목: Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen

Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen We have a new blog! View this page at qwen.ai. This page will automatically redirect in 5 seconds. If you are not redirected automatically, please click the button below. Go Now Blog Publication About Try Qwen Chat Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models June 5, 2025 · 4 min · 798 words · Qwen Team | Translations: 简体中文 GITHUBHUGGING FACEMODELSCOPEDISCORD We release Qwen3 Embedding series, a new proprietary model of the Qwen model family. These models are specifically designed for text embedding, retrieval, and reranking tasks, built on the Qwen3 foundation model. Leveraging Qwen3’s robust multilingual text understanding capabilities, the series achieves state-o

### Qwen3-Embedding-8B on Hugging Face

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-8B
- raw snapshot: `raw/hot-topics-sources/2026-04-10/194-qwen3-embedding-8b-on-hugging-face.md`
- 수집 제목: Qwen/Qwen3-Embedding-8B · Hugging Face

Qwen/Qwen3-Embedding-8B · Hugging Face Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Log In Sign Up Qwen / Qwen3-Embedding-8B like643 Follow Qwen78.6k Feature Extraction sentence-transformers Safetensors Transformers qwen3 text-generation sentence-similarity text-embeddings-inference arxiv:2506.05176 License:apache-2.0 Model cardFilesFiles and versions xet Community 28 Deploy Use this model Qwen3-Embedding-8B Highlights Qwen3 Embedding Series Model list Usage Sentence Transformers Usage Transformers Usage vLLM Usage Text Embeddings Inference (TEI) Usage Evaluation MTEB (Multilingual) MTEB (Eng v2) C-MTEB (MTEB Chinese) Citation Qwen3-Embedding-8B Highlights The Qwen3 Embedding model series is the latest proprietary model of the Qwen family, specifically designed f

### voyage-3-large: the new state-of-the-art general-purpose embedding model (Voyage AI Blog)

- URL: https://blog.voyageai.com/2025/01/07/voyage-3-large
- raw snapshot: `raw/hot-topics-sources/2026-04-10/195-voyage-3-large-the-new-state-of-the-art-general-purpose-embedding-model.md`
- 수집 제목: voyage-3-large: the new state-of-the-art general-purpose embedding model – Voyage AI

voyage-3-large: the new state-of-the-art general-purpose embedding model – Voyage AI Home Documentation Blog Company Careers News By Voyage AI · January 7, 2025 voyage-3-large: the new state-of-the-art general-purpose embedding model TL;DR – Introducing voyage-3-large , a new state-of-the-art general-purpose and multilingual embedding model that ranks first across eight evaluated domains spanning 100 datasets, including law, finance, and code. It outperforms OpenAI-v3-large and Cohere-v3-English by an average of 9.74% and 20.71%, respectively. Enabled by Matryoshka learning and quantization-aware training, voyage-3-large supports smaller dimensions and int8 and binary quantization that dramatically reduce vectorDB costs with minimal impact on retrieval quality. We are excited to announce v

### Voyage AI Text Embeddings Documentation

- URL: https://docs.voyageai.com/docs/embeddings
- raw snapshot: `raw/hot-topics-sources/2026-04-10/196-voyage-ai-text-embeddings-documentation.md`
- 수집 제목: Text Embeddings

Text Embeddings Jump to Content GuidesAPI ReferenceChangelogDiscussionsHomeDocumentationBlogAbout Guides HomeDocumentationBlogAbout GuidesAPI ReferenceChangelogDiscussions Text Embeddings All Pages Start typing to search… GET STARTED Introduction API Key and Python Client Quickstart Tutorial CAPABILITIES Text Embeddings Contextualized Chunk Embeddings Multimodal Embeddings Rerankers GUIDES Tokenization Flexible Dimensions and Quantization Batch Inference Error Codes Rate Limits Pricing Organizations and Projects Service Level Objectives DEPLOYMENT ON VPC AWS Marketplace Model Package MongoDB Voyage AI Models in AWS Voyage AI Models in AWS Azure Marketplace Managed Application MongoDB Voyage AI Models in Azure Voyage AI Models in Azure ACCESS VIA DATA PLATFORMS Snowflake Community Integrati
