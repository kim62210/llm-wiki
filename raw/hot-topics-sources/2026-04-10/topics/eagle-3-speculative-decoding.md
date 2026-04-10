---
title: EAGLE-3 Speculative Decoding
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# EAGLE-3 Speculative Decoding

## 기존 큐레이션 요약

- 정의: 멀티레이어 피처 융합과 training-time test로 드래프트 헤드를 학습시키는 가속법.
- 왜 중요한가: NeurIPS 2025 채택 후 2025년 말부터 vLLM, SGLang, TensorRT-LLM 모두에 통합되어 최대 6.5배 속도 향상을 기록했고, LMSys는 2025년 12월 Google Vertex AI 프로덕션 배포 사례를 공개했다.

## 개별 원문 수집 스냅샷

### EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

- URL: https://arxiv.org/abs/2503.01840
- raw snapshot: `raw/hot-topics-sources/2026-04-10/076-eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-.md`
- 수집 제목: [2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

[2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2503.01840 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2503.01840 (cs) [Submitted on 3 Mar 2025 (v1), last revised 23 Apr 2025 (this version, v3)] Title:EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test Authors:Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang View a PDF of t

### SafeAILab/EAGLE official repository

- URL: https://github.com/SafeAILab/EAGLE
- raw snapshot: `raw/hot-topics-sources/2026-04-10/077-safeailab-eagle-official-repository.md`
- 수집 제목: GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub

GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY 

### From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex (LMSYS)

- URL: https://lmsys.org/blog/2025-12-01-eagle3-vertex
- raw snapshot: `raw/hot-topics-sources/2026-04-10/078-from-research-to-production-accelerate-oss-llm-with-eagle-3-on-vertex.md`
- 수집 제목: From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex - LMSYS Blog | LMSYS Org

From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex - LMSYS Blog | LMSYS Org Projects Blog About Donations Contact Projects Blog About Donations Contact ‹ Back to Blog ‹ Back to Blog Contents Challenge #1: Preparing the data Lesson 1: Build a Synthetic Data Generation Pipeline Challenge #2: Engineering the training pipeline Lesson 2: Chat Templates Are Not Optional Lesson 3: Mind the Mask Challenge #3: Serving and Scaling Lesson 4: Your Serving Framework Is Key Lesson 5: Don't Let your CPU Bottleneck your GPU Benchmark Results Metric 1: Median Time Per Output Token (TPOT) Metric 2: Output Throughput Conclusion: Now It's Your Turn Thanks for reading Acknowledgements From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex Ivan Nardini, Charles Chen, Ying Wan

### Fly Eagle-3 fly: Faster inference with vLLM (Red Hat)

- URL: https://developers.redhat.com/articles/2025/07/01/fly-eagle3-fly-faster-inference-vllm-speculative-decoding
- raw snapshot: `raw/hot-topics-sources/2026-04-10/079-fly-eagle-3-fly-faster-inference-with-vllm.md`
- 수집 제목: Faster inference with vLLM & speculative decoding | Red Hat Developer

Faster inference with vLLM & speculative decoding | Red Hat Developer Skip to main content Products Platforms Red Hat Enterprise Linux Red Hat AI Red Hat OpenShift Red Hat Ansible Automation Platform See all Red Hat products Featured Red Hat build of OpenJDK Red Hat Developer Hub Red Hat JBoss Enterprise Application Platform Red Hat OpenShift Dev Spaces Red Hat OpenShift Local Red Hat Developer Sandbox Try Red Hat products and technologies without setup or configuration fees for 30 days with this shared Red Hat OpenShift and Kubernetes cluster. Try at no cost Technologies Featured AI/ML Linux Kubernetes Automation See all technologies Programming languages & frameworks Java Python JavaScript System design & architecture Red Hat architecture and design patterns Microservices Event-Driven Ar

### SGLang Speculative Decoding documentation

- URL: https://docs.sglang.io/advanced_features/speculative_decoding.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/080-sglang-speculative-decoding-documentation.md`
- 수집 제목: Speculative Decoding — SGLang

Speculative Decoding — SGLang Skip to main content Back to top Ctrl+K Get Started Install SGLang Basic Usage Sending Requests OpenAI-Compatible APIs Ollama-Compatible API Offline Engine API SGLang Native APIs Sampling Parameters Popular Model Usage (DeepSeek, GPT-OSS, GLM, Llama, MiniMax, Qwen, and more) Advanced Features Server Arguments Loading Models from Object Storage Hyperparameter Tuning Attention Backend Speculative Decoding Structured Outputs Structured Outputs For Reasoning Models Tool Parser Reasoning Parser Quantization Quantized KV Cache Expert Parallelism DP, DPA and SGLang DP Router LoRA Serving PD Disaggregation EPD Disaggregation Pipeline Parallelism for Long Context Hierarchical KV Caching (HiCache) Query VLM with Offline Engine DP for Multi-Modal Encoder in SGLang Cuda G
