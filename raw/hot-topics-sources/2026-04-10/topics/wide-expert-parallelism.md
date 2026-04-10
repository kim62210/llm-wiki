---
title: Wide Expert Parallelism (Wide-EP) for MoE
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Wide Expert Parallelism (Wide-EP) for MoE

## 기존 큐레이션 요약

- 정의: DeepSeek급 MoE 모델을 32+ GPU에 걸쳐 전문가를 분산시키는 병렬화 전략.
- 왜 중요한가: 2025년 12월 vLLM이 H200에서 2.2k tok/s/GPU를 달성했고 2026년 2월 Blackwell 파트 I 블로그가 공개되었으며, 3월 SGLang의 Elastic EP가 부분 장애 내성을 추가해 MoE 대규모 서빙의 운영 성숙도가 급격히 올라갔다.

## 개별 원문 수집 스냅샷

### Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) - vLLM Blog (2026-02-03)

- URL: https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/083-driving-vllm-wideep-and-large-scale-serving-on-blackwell.md`
- 수집 제목: Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) | vLLM Blog

Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) | vLLM Blog Menu Search DocsDocumentationBlogEventsContactCommunityGitHub Theme DocsBlogEventsContactCommunitySearch⌘J Blog Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I) February 3, 202610 min read Meta and NVIDIA Team #large-scale-serving#performance#hardware Introduction Results Key Optimizations Lower-Precision Operations NVFP4 GEMM (MoE GEMMs, O-proj) FP8 GEMM for MLA NVFP4 MoE Dispatch Kernel Fusion RoPE \+ Quant \+ Q Write (Decode) RoPE \+ Quant (Prefill) Concat K Optimization Scaling Down Prefill Why Scaling Down Makes Sense Weight Offloading v2 Minimize Chunking Overheads MoE DP Chunk MoE Activation Chunk Output Processing Chunk Future Work Summary Team References T

### vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP (2025-12-17)

- URL: https://blog.vllm.ai/2025/12/17/large-scale-serving.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/088-vllm-large-scale-serving-deepseek-2-2k-tok-s-h200-with-wide-ep.md`
- 수집 제목: vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP | vLLM Blog

vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP | vLLM Blog Menu Search DocsDocumentationBlogEventsContactCommunityGitHub Theme DocsBlogEventsContactCommunitySearch⌘J Blog vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP December 17, 20258 min read vLLM Team #large-scale-serving#performance Introduction Results Key Components Wide-EP Dual-batch Overlap (DBO) Expert Parallel Load Balancing (EPLB) Disaggregated Serving Deployment Paths llm-d Dynamo Ray Serve LLM Roadmap Summary Table of Contents Introduction In v0.11.0, the last code from vLLM V0 engine was removed, marking the complete migration to the improved V1 engine architecture. This achievement would not have been possible without vLLM’s community of 1,969 contributors, authoring over 950 commits in

### Elastic EP in SGLang: Achieving Partial Failure Tolerance for DeepSeek MoE Deployments (2026-03-25)

- URL: https://www.lmsys.org/blog/2026-03-25-eep-partial-failure-tolerance
- raw snapshot: `raw/hot-topics-sources/2026-04-10/319-elastic-ep-in-sglang-achieving-partial-failure-tolerance-for-deepseek-moe-deploy.md`
- 수집 제목: Elastic EP in SGLang: Achieving Partial Failure Tolerance for DeepSeek MoE Deployments - LMSYS Blog | LMSYS Org

Elastic EP in SGLang: Achieving Partial Failure Tolerance for DeepSeek MoE Deployments - LMSYS Blog | LMSYS Org Projects Blog About Donations Contact Projects Blog About Donations Contact ‹ Back to Blog ‹ Back to Blog Contents 1. The Problem: The Necessity and Vulnerability of Wide EP 2. Solution Overview: Elastic EP and Its Potential The Effect 3. Detailed Structural Modifications 4. Facilitating Elastic EP: The Role of Mooncake 5. Enabling Elastic EP Acknowledgment Links Elastic EP in SGLang: Achieving Partial Failure Tolerance for DeepSeek MoE Deployments The Mooncake Team, Volcano EngineMarch 25, 2026 1. The Problem: The Necessity and Vulnerability of Wide EP To serve massive Mixture-of-Experts (MoE) models efficiently, deploying a "wide" Expert Parallelism (EP) strategy—often spanning

### Expert Parallel Deployment - vLLM Docs

- URL: https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment
- raw snapshot: `raw/hot-topics-sources/2026-04-10/086-vllm-expert-parallel-deployment-docs.md`
- 수집 제목: Expert Parallel Deployment - vLLM

Expert Parallel Deployment - vLLM Skip to content You are viewing the latest developer preview docs. Click here to view docs for the latest stable release. vLLM Expert Parallel Deployment Initializing search GitHub Home User Guide Developer Guide Benchmarking API Reference CLI Reference Community vLLM GitHub Home User Guide User Guide Getting Started Getting Started Quickstart Installation Installation GPU CPU TPU Examples Examples Basic Basic Offline Inference Online Serving Offline Inference Offline Inference Async LLM Streaming Audio Language Automatic Prefix Caching Batch LLM Inference Chat With Tools Context Extension Data Parallel Disaggregated Prefill V1 Disaggregated Prefill Encoder Decoder Multimodal Extract Hidden States KV Load Failure Recovery Test LLM Engine Example LLM Engine

### DeepEP: Expert-Parallel Communication Library GitHub

- URL: https://github.com/deepseek-ai/DeepEP
- raw snapshot: `raw/hot-topics-sources/2026-04-10/320-deepep-expert-parallel-communication-library-github.md`
- 수집 제목: GitHub - deepseek-ai/DeepEP: DeepEP: an efficient expert-parallel communication library · GitHub

GitHub - deepseek-ai/DeepEP: DeepEP: an efficient expert-parallel communication library · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and med
