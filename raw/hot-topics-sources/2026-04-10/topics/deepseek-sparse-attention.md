---
title: DeepSeek Sparse Attention (DSA) for Long Context
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# DeepSeek Sparse Attention (DSA) for Long Context

## 기존 큐레이션 요약

- 정의: lightning indexer와 top-k 셀렉터로 토큰 단위 희소 attention을 구현하는 방식.
- 왜 중요한가: DeepSeek-V3.2에서 O(L²)를 O(Lk)로 축소하며 긴 컨텍스트 학습·추론 효율을 크게 개선했고, 2026년 초 SGLang이 NativeSparseAttnBackend를, HISA·SALS 등 후속 arxiv 논문이 쏟아지고 있다.

## 개별 원문 수집 스냅샷

### DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

- URL: https://arxiv.org/abs/2512.02556
- raw snapshot: `raw/hot-topics-sources/2026-04-10/090-deepseek-v3-2-pushing-the-frontier-of-open-large-language-models.md`
- 수집 제목: [2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2512.02556 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2512.02556 (cs) [Submitted on 2 Dec 2025] Title:DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models Authors:DeepSeek-AI, Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang, C

### DeepSeek-V3.2-Exp GitHub repository

- URL: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp
- raw snapshot: `raw/hot-topics-sources/2026-04-10/091-deepseek-v3-2-exp-github-repository.md`
- 수집 제목: GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub

GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Mod

### HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention

- URL: https://arxiv.org/html/2603.28458
- raw snapshot: `raw/hot-topics-sources/2026-04-10/092-hisa-efficient-hierarchical-indexing-for-fine-grained-sparse-attention.md`
- 수집 제목: HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention

HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse AttentionReport GitHub Issue× Title: Content selection saved. Describe the issue below: Description: Submit without GitHubSubmit in GitHub Back to arXiv Why HTML?Report IssueBack to AbstractDownload PDF Abstract 1 Introduction 2 Related Work Block sparse attention. Token sparse attention. Hierarchical sparse attention. 3 Preliminary Indexer in DSA. Sparse MLA in DSA. 4 Method 4.1 HISA: Hierarchical Indexed Sparse Attention Block partitioning and pooled keys. Stage 1: Block-level coarse filtering. Stage 2: Token-level refinement. Boundary behavior. 4.2 Complexity Analysis 5 Experiments 5.1 Kernel-Level Speedup 5.2 Needle-in-a-Haystack 5.3 LongBench Evaluation 5.4 Visualization of Attention Scores 5.5 Hyperparameter Sensitivity 6 

### SALS: Sparse Attention in Latent Space for KV cache Compression

- URL: https://arxiv.org/pdf/2510.24273
- raw snapshot: `raw/hot-topics-sources/2026-04-10/093-sals-sparse-attention-in-latent-space-for-kv-cache-compression.md`

%PDF-1.7 %¿÷¢þ 1 0 obj << /Metadata 3 0 R /Names 4 0 R /OpenAction 5 0 R /Outlines 6 0 R /PageMode /UseOutlines /Pages 7 0 R /Type /Catalog >> endobj 2 0 obj << /Author (Junlin Mu; Hantao Huang; Jihang Zhang; Minghui Yu; Tao Wang; Yidong Li) /Creator (arXiv GenPDF \(tex2pdf:e76afa9\)) /DOI (https://doi.org/10.48550/arXiv.2510.24273) /License (http://arxiv.org/licenses/nonexclusive-distrib/1.0/) /PTEX.Fullbanner (This is pdfTeX, Version 3.141592653-2.6-1.40.28 \(TeX Live 2025\) kpathsea version 6.4.1) /Producer (pikepdf 8.15.1) /Title (SALS: Sparse Attention in Latent Space for KV cache Compression) /Trapped /False /arXivID (https://arxiv.org/abs/2510.24273v1) >> endobj 3 0 obj << /Subtype /XML /Type /Metadata /Length 1703 >> stream <?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?> <x:x

### DeepSeek-V3.2 Usage Guide (vLLM Recipes)

- URL: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/094-deepseek-v3-2-usage-guide.md`
- 수집 제목: DeepSeek-V3.2 Usage Guide - vLLM Recipes

DeepSeek-V3.2 Usage Guide - vLLM Recipes Skip to content vLLM Recipes DeepSeek-V3.2 Usage Guide Initializing search GitHub vLLM Recipes GitHub vLLM Recipes DeepSeek DeepSeek DeepSeek-OCR Usage Guide DeepSeek-OCR Usage Guide DeepSeek-V3 (R1) Usage Guide DeepSeek-V3.1 Usage Guide DeepSeek-V3.2 Usage Guide DeepSeek-V3.2 Usage Guide Table of contents Introduction Installing DeepGEMM Installing vLLM Launching DeepSeek-V3.2 Performance tuning on Hopper/Blackwell GPUs Accuracy Benchmarking GSM8K AIME25 Benchmarking TP8 Benchmark Output EP/DP Mode Usage tips Tool Calling Example vLLM Server Print DeepSeek Offical API Print DeepSeek-V3.2-Exp Usage Guide Ernie Ernie Ernie4.5 Text Model Usage Guide Ernie4.5 VL Model Usage Guide GLM GLM GLM-4.X LLM Usage Guide GLM-5 and GLM-5.1 Series Usage GLM-ASR Us
