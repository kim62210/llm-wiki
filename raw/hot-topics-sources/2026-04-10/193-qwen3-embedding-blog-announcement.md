---
title: Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen
source_url: https://qwenlm.github.io/blog/qwen3-embedding
final_url: https://qwenlm.github.io/blog/qwen3-embedding/
status: 200
content_type: text/html; charset=utf-8
topics: [Qwen3 / Voyage-4 Embedding Leaderboard Shakeup]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:52.769770+00:00
---

# Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen

## 원본 URL

https://qwenlm.github.io/blog/qwen3-embedding

## 추출 본문

Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen

We have a new blog!
View this page at qwen.ai.

This page will automatically redirect in 5 seconds.

If you are not redirected automatically, please click the button below.

Go Now

Blog

Publication

About

Try Qwen Chat

Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models

June 5, 2025 · 4 min · 798 words · Qwen Team | Translations:
简体中文

GITHUBHUGGING FACEMODELSCOPEDISCORD

We release Qwen3 Embedding series, a new proprietary model of the Qwen model family. These models are specifically designed for text embedding, retrieval, and reranking tasks, built on the Qwen3 foundation model. Leveraging Qwen3’s robust multilingual text understanding capabilities, the series achieves state-of-the-art performance across multiple benchmarks for text embedding and reranking tasks. We have open-sourced this series of text embedding and reranking models under the Apache 2.0 license on Hugging Face and ModelScope, and published the technical report and related code on GitHub.

Evaluation results for reranking models
ModelParamMTEB-RCMTEB-RMMTEB-RMLDRMTEB-CodeFollowIRQwen3-Embedding-0.6B0.6B61.8271.0264.6450.2675.415.09Jina-multilingual-reranker-v2-base0.3B58.2263.3763.7339.6658.98-0.68gte-multilingual-reranker-base0.3B59.5174.0859.4466.3354.18-1.64BGE-reranker-v2-m30.6B57.0372.1658.3659.5141.38-0.01Qwen3-Reranker-0.6B0.6B65.8071.3166.3667.2873.425.41Qwen3-Reranker-4B4B69.7675.9472.7469.9781.2014.84Qwen3-Reranker-8B8B69.0277.4572.9470.1981.228.05

Note:

We use the text retrieval subsets of MTEB(eng, v2), MTEB(cmn, v1), MTEB (Multilingual) and MTEB (Code), which are denoted as MTEB-R, CMTEB-R, MMTEB-R and MTEB-Code.

All scores are our runs based on the top-100 candidates retrieved by dense embedding model Qwen3-Embedding-0.6B.

Key Features:

Exceptional Versatility: The embedding model has achieved state-of-the-art performance across a wide range of downstream application evaluations. The 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58). The reranking models excel in text retrieval scenarios, significantly improving search relevance.

Comprehensive Flexibility: The Qwen3 Embedding series offers a diverse range of sizes (from 0.6B to 8B) for both embedding and reranking models, catering to various use cases that prioritize efficiency and effectiveness. Developers can seamlessly combine these two modules. Additionally, the embedding model allows for flexible vector definitions across all dimensions, and both embedding and reranking models support user-defined instructions to enhance performance for specific tasks, languages, or scenarios.

Multilingual Capability: The Qwen3 Embedding series support over 100 languages, including various programming languages, and provides robust multilingual, cross-lingual, and code retrieval capabilities.

Model Overview:
Model TypeModelsSizeLayersSequence LengthEmbedding DimensionMRL SupportInstruction AwareText EmbeddingQwen3-Embedding-0.6B0.6B2832K1024YesYesQwen3-Embedding-4B4B3632K2560YesYesQwen3-Embedding-8B8B3632K4096YesYesText RerankingQwen3-Reranker-0.6B0.6B2832K--YesQwen3-Reranker-4B4B3632K--YesQwen3-Reranker-8B8B3632K--Yes
Note: “MRL Support” indicates whether the embedding model supports custom dimensions for the final embedding. “Instruction Aware” notes whether the embedding or reranking model supports customizing the input instruction according to different tasks.

Model Architecture#

Based on the Qwen3 foundation model, our Embedding and Reranking models are designed using dual-encoder and cross-encoder architectures. Through LoRA fine-tuning, we aim to fully preserve and enhance the text understanding capabilities of the base model. The Embedding model processes a single text segment as input, extracting the semantic representation by utilizing the hidden state vector corresponding to the final 
[EOS]
 token. In contrast, the Reranking model takes text pairs (such as user queries and candidate documents) as input, calculating and outputting a relevance score between the pairs using a cross-encoder structure.

Model Training#

The training framework for the Qwen3 Embedding series follows the multi-stage training paradigm established by the GTE-Qwen series. During the training of the Embedding model, we implemented a three-stage training structure: the first stage involves contrastive pre-training with a large volume of weakly supervised data; the second stage focuses on supervised training using high-quality labeled data; and the final stage integrates multiple candidate models through a merging strategy to enhance overall performance. This staged training mechanism effectively balances the model’s generalization ability and task adaptability. For the Reranking model, based on empirical validation results, we directly employed high-quality labeled data for supervised training, significantly improving training efficiency. Notably, during the first stage of weakly supervised training for the Embedding model, we developed an innovative multi-task adaptable prompt system. By leveraging the text generation capabilities of the Qwen3 foundation model, we dynamically generated weakly supervised text pairs tailored to different task types and languages. This approach addressed the limitations of traditional methods, which often relied on community forums or open-source data for text relevance pair collection, facilitating the efficient generation of large-scale weakly supervised data.

Future work#

The Qwen3 Embedding series models represent a new starting point. Through ongoing optimizations of the Qwen foundation model, we will enhance the training efficiency of text embeddings and reranking models, thereby improving deployment performance across various scenarios. Additionally, we plan to expand our multimodal representation system to establish cross-modal semantic understanding capabilities. We look forward to seeing more developers explore a wider range of scenarios based on the Qwen3 Embedding series, driving deeper applications of the model across diverse contexts.

© 2026 QwenPowered by
Hugo
