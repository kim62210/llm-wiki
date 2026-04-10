---
title: LMCache-Based Distributed KV Cache Offloading
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# LMCache-Based Distributed KV Cache Offloading

## 기존 큐레이션 요약

- 정의: GPU 외부(CPU/디스크/S3)로 KV 캐시를 오프로드하고 크로스 엔진 재사용하는 계층.
- 왜 중요한가: 2025년 말 vLLM V1 + LMCache 조합이 multi-round QA·RAG에서 3-10배 지연 절감을 기록했고, llm-d의 KV-Cache Aware Routing과 함께 2026년 초 엔터프라이즈 표준 스택으로 부상했다.

## 개별 원문 수집 스냅샷

### LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference (arxiv)

- URL: https://arxiv.org/abs/2510.09665
- raw snapshot: `raw/hot-topics-sources/2026-04-10/095-lmcache-an-efficient-kv-cache-layer-for-enterprise-scale-llm-inference.md`
- 수집 제목: [2510.09665] LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference

[2510.09665] LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.09665 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2510.09665 (cs) [Submitted on 8 Oct 2025 (v1), last revised 5 Dec 2025 (this version, v2)] Title:LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference Authors:Yuhan Liu, Yihua Cheng, Jiayi Yao, Yuwei An, Xiaokun Chen, 

### LMCache/LMCache GitHub repository

- URL: https://github.com/LMCache/LMCache
- raw snapshot: `raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md`
- 수집 제목: GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub

GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams

### llm-d KV Cache Architecture documentation

- URL: https://llm-d.ai/docs/architecture/Components/kv-cache
- raw snapshot: `raw/hot-topics-sources/2026-04-10/097-llm-d-kv-cache-architecture-documentation.md`
- 수집 제목: KV Cache | llm-d

KV Cache | llm-d Skip to main content 🎉 llm-d 0.5 is now released! Check out hierarchical KV offloading, cache-aware LoRA routing, resilient networking with UCCL, and scale-to-zero autoscaling. Read the announcement → ArchitectureGuidesUsageCommunityBlogVideos Join Slack llm-d Architecture Latest Release Components Inference Scheduler Model Service Inference Simulator Infrastructure KV Cache Benchmark Tools Workload Variant Autoscaler Components KV Cache On this page KV-Cache Introduction​ Efficiently caching Key & Value (KV) tensors is crucial for optimizing LLM inference. Reusing the KV-Cache, rather than recomputing it, significantly improves both Time To First Token (TTFT) and overall throughput, while also maximizing system resource-utilization. As a distributed LLM inference platform

### llm-d/llm-d-kv-cache-manager repository

- URL: https://github.com/llm-d/llm-d-kv-cache-manager
- raw snapshot: `raw/hot-topics-sources/2026-04-10/098-llm-d-llm-d-kv-cache-manager-repository.md`
- 수집 제목: GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub

GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and mediu

### NixlConnector Usage Guide (vLLM)

- URL: https://docs.vllm.ai/en/stable/features/nixl_connector_usage
- raw snapshot: `raw/hot-topics-sources/2026-04-10/099-nixlconnector-usage-guide.md`
- 수집 제목: NixlConnector Usage Guide - vLLM

NixlConnector Usage Guide - vLLM Skip to content vLLM NixlConnector Usage Guide Initializing search GitHub Home User Guide Developer Guide Benchmarking API Reference CLI Reference Community vLLM GitHub Home User Guide User Guide Getting Started Getting Started Quickstart Installation Installation GPU CPU TPU Examples Examples Basic Basic Offline Inference Online Serving Offline Inference Offline Inference Async LLM Streaming Audio Language Automatic Prefix Caching Batch LLM Inference Chat With Tools Context Extension Data Parallel Disaggregated Prefill V1 Disaggregated Prefill Encoder Decoder Multimodal Extract Hidden States KV Load Failure Recovery Test LLM Engine Example LLM Engine Reset Kv Load Sharded State Custom Logits Processors LoRA With Quantization Inference Metrics Mistral-Small
