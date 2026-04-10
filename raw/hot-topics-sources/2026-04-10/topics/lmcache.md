---
title: LMCache + Mooncake KV Cache Layer
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# LMCache + Mooncake KV Cache Layer

## 기존 큐레이션 요약

- 정의: GPU/CPU/디스크/원격 스토리지에 걸친 계층형 KV 캐시 재사용 레이어.
- 왜 중요한가: 2026년 2월 12일 Mooncake가 PyTorch Ecosystem에 공식 합류했고 LMCache v0.4.3이 4월 6일 릴리스되면서, vLLM V1의 기본 디스어그리게이션 커넥터로 채택되어 엔터프라이즈 LLM 추론의 사실상의 KV 캐시 관리 표준이 되었다.

## 개별 원문 수집 스냅샷

### LMCache/LMCache GitHub Repository

- URL: https://github.com/LMCache/LMCache
- raw snapshot: `raw/hot-topics-sources/2026-04-10/096-lmcache-lmcache-github-repository.md`
- 수집 제목: GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub

GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams

### Welcome to Mooncake Documentation

- URL: https://kvcache-ai.github.io/Mooncake
- raw snapshot: `raw/hot-topics-sources/2026-04-10/334-welcome-to-mooncake-documentation.md`
- 수집 제목: Welcome to Mooncake — Mooncake

Welcome to Mooncake — Mooncake Skip to main content Back to top Ctrl+K Getting Started Build Guide Quick Start Supported Communication Protocols Mooncake HF3FS Plugin Mooncake x LMCache: Unite to Pioneer KVCache-Centric LLM Serving System LMDeploy Disaggregated Serving with MooncakeTransferEngine SGLang Disaggregated Serving with MooncakeTransferEngine SGLang HiCache with Mooncake Backend vLLM Disaggregated Serving Performance PD Disaggregation Performance Benchmark performance on NVIDIA A10 Benchmark performance on NVIDIA A10 SGLang HiCache with Mooncake Backend Benchmark vLLM with Mooncake Transfer Engine Benchmark Allocator Performance Python API Reference Mooncake Store Python API Transfer Engine Python API Mooncake Store HTTP Service Mooncake EP & Mooncake Backend Design Documents Moo

### kvcache-ai/Mooncake GitHub Repository

- URL: https://github.com/kvcache-ai/Mooncake
- raw snapshot: `raw/hot-topics-sources/2026-04-10/335-kvcache-ai-mooncake-github-repository.md`
- 수집 제목: GitHub - kvcache-ai/Mooncake: Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI. · GitHub

GitHub - kvcache-ai/Mooncake: Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPAN

### Mooncake Integration - LMCache Docs

- URL: https://docs.lmcache.ai/kv_cache/mooncake.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/336-mooncake-integration-lmcache-docs.md`
- 수집 제목: Mooncake | LMCache

Mooncake | LMCache Skip to content LMCache Toggle navigation menu ⌘ K LMCache Getting Started Installation Quickstart Examples Example: Offload KV cache to CPU Example: Share KV cache across multiple LLMs Example: Disaggregated prefill Example: Multimodal KV Cache Support TroubleShoot FAQ KV Cache offloading and sharing CPU RAM Local storage GDS Backend Redis InfiniStore Mooncake ValKey Weka Disaggregated prefill Using NIXL 1p1d XpYd Using shared storage KV Cache management LMCache Controller Lookup the KV cache Persist the KV cache Clear the KV cache Move the KV cache Compress the KV cache Check finish of a control event KV Cache Optimizations Compression CacheGen Blending Use LMCache in production Docker deployment Kubernetes deployment Developer Guide Contributing Guide Dockerfile Usage

### vLLM V1 Disaggregated Serving with Mooncake Store and LMCache

- URL: https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/337-vllm-v1-disaggregated-serving-with-mooncake-store-and-lmcache.md`
- 수집 제목: vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake

vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake Skip to main content Back to top Ctrl+K Getting Started Build Guide Quick Start Supported Communication Protocols Mooncake HF3FS Plugin Mooncake x LMCache: Unite to Pioneer KVCache-Centric LLM Serving System LMDeploy Disaggregated Serving with MooncakeTransferEngine SGLang Disaggregated Serving with MooncakeTransferEngine SGLang HiCache with Mooncake Backend vLLM Disaggregated Serving vLLM V1 Disaggregated Serving with Mooncake Store and LMCache vLLM V0 Disaggregated Serving Demo vLLM V0 Disaggregated Serving with MooncakeStore vLLM v1 backend Disaggregated Serving with MooncakeConnector Performance PD Disaggregation Performance Benchmark performance on NVIDIA A10 Benchmark performance on NVIDIA A10 SGLang HiCache wit
