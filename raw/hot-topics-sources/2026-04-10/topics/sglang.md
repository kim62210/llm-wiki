---
title: SGLang on GB300 NVL72 with NVFP4
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# SGLang on GB300 NVL72 with NVFP4

## 기존 큐레이션 요약

- 정의: SGLang이 NVFP4 GEMM과 Dynamo 디스어그리게이션으로 GB300 NVL72에서 DeepSeek-R1을 최대 25배 가속.
- 왜 중요한가: 2026년 2월 InferenceXv2 벤치마크에서 H200 대비 25배, GB200 NVL72 대비 8배 성능 향상을 공개적으로 증명했고, GB300 세대 하드웨어의 전환점 벤치마크로 광범위하게 인용되고 있다.

## 개별 원문 수집 스냅샷

### Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 (2026-02-20)

- URL: https://lmsys.org/blog/2026-02-20-gb300-inferencex
- raw snapshot: `raw/hot-topics-sources/2026-04-10/325-unlocking-25x-inference-performance-with-sglang-on-nvidia-gb300-nvl72.md`
- 수집 제목: Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 - LMSYS Blog | LMSYS Org

Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 - LMSYS Blog | LMSYS Org Projects Blog About Donations Contact Projects Blog About Donations Contact ‹ Back to Blog ‹ Back to Blog Contents NVIDIA GB300 NVL72 with Blackwell Ultra GPUs 25x More SGLang Performance with GB300 NVL72 Inference Optimizations for Blackwell Ultra 8x More Performance on GB200 NVL72 Looking Ahead Acknowledgements Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 NVIDIA and Community SGLang DevelopersFebruary 20, 2026 The SGLang team has worked closely with NVIDIA across multiple GPU generations to unlock step-function gains in inference performance for large-scale deployments of Mixture of Expert (MoE) reasoning models. Building on prior results that delivered 4x speedups on B

### Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference (2026-02-19)

- URL: https://www.lmsys.org/blog/2026-02-19-gb300-longctx
- raw snapshot: `raw/hot-topics-sources/2026-04-10/326-deploying-deepseek-on-gb300-nvl72-big-wins-in-long-context-inference.md`
- 수집 제목: Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference - LMSYS Blog | LMSYS Org

Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference - LMSYS Blog | LMSYS Org Projects Blog About Donations Contact Projects Blog About Donations Contact ‹ Back to Blog ‹ Back to Blog Contents TL;DR Methods 1. Deployment & Integration with NVIDIA Dynamo 2. Prefill Path: PP Prefill, Long-Context TTFT, and Faster Kernels 3. Decode path: The Memory Bottleneck in Long-Context Inference 4. MTP Powered by the Overlap Scheduler Experiments 1. Max Throughput Analysis 2. Peak Capacity vs. Latency Constraints 3. Prefill Latency: Chunking Strategies and TTFT Optimizations 4. Kernel Comparison 5. Accuracy Future Work Acknowledgement Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference Nvidia & SGLang TeamFebruary 19, 2026 TL;DR As the latest addition to the Blackwell 

### sgl-project/sglang GitHub Repository

- URL: https://github.com/sgl-project/sglang
- raw snapshot: `raw/hot-topics-sources/2026-04-10/327-sgl-project-sglang-github-repository.md`
- 수집 제목: GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub

GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY C

### SGLang Development Roadmap (2026 Q1) - Issue #12780

- URL: https://github.com/sgl-project/sglang/issues/12780
- raw snapshot: `raw/hot-topics-sources/2026-04-10/085-sglang-q1-2026-development-roadmap.md`
- 수집 제목: Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub

Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Non

### SGLang Documentation

- URL: http://docs.sglang.io
- raw snapshot: `raw/hot-topics-sources/2026-04-10/328-sglang-documentation.md`
- 수집 제목: SGLang Documentation — SGLang

SGLang Documentation — SGLang Skip to main content Back to top Ctrl+K Get Started Install SGLang Basic Usage Sending Requests OpenAI-Compatible APIs Ollama-Compatible API Offline Engine API SGLang Native APIs Sampling Parameters Popular Model Usage (DeepSeek, GPT-OSS, GLM, Llama, MiniMax, Qwen, and more) Advanced Features Server Arguments Loading Models from Object Storage Hyperparameter Tuning Attention Backend Speculative Decoding Structured Outputs Structured Outputs For Reasoning Models Tool Parser Reasoning Parser Quantization Quantized KV Cache Expert Parallelism DP, DPA and SGLang DP Router LoRA Serving PD Disaggregation EPD Disaggregation Pipeline Parallelism for Long Context Hierarchical KV Caching (HiCache) Query VLM with Offline Engine DP for Multi-Modal Encoder in SGLang Cuda G
