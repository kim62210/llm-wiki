---
title: FlashInfer Kernel Library for LLM Serving
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# FlashInfer Kernel Library for LLM Serving

## 기존 큐레이션 요약

- 정의: vLLM/SGLang/TRT-LLM이 공유하는 attention·MoE·GEMM 커널 라이브러리.
- 왜 중요한가: NVIDIA가 2026년 들어 TensorRT-LLM의 최고 성능 커널을 FlashInfer에 직접 릴리스하기 시작했고, v0.6.x에서 Blackwell FP4 GEMM·스펙 디코드 1.14배 가속을 제공하며 MLSys 2026 커널 컨테스트 기반이 되었다.

## 개별 원문 수집 스냅샷

### FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving

- URL: https://arxiv.org/abs/2501.01005
- raw snapshot: `raw/hot-topics-sources/2026-04-10/100-flashinfer-efficient-and-customizable-attention-engine-for-llm-inference-serving.md`
- 수집 제목: [2501.01005] FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving

[2501.01005] FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2501.01005 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Distributed, Parallel, and Cluster Computing arXiv:2501.01005 (cs) [Submitted on 2 Jan 2025 (v1), last revised 21 Apr 2025 (this version, v2)] Title:FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving Authors:Zihao Ye, 

### flashinfer-ai/flashinfer GitHub repository

- URL: https://github.com/flashinfer-ai/flashinfer
- raw snapshot: `raw/hot-topics-sources/2026-04-10/101-flashinfer-ai-flashinfer-github-repository.md`
- 수집 제목: GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub

GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams 

### Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer

- URL: https://developer.nvidia.com/blog/run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer
- raw snapshot: `raw/hot-topics-sources/2026-04-10/102-run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer.md`
- 수집 제목: Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​ | NVIDIA Technical Blog

Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​ | NVIDIA Technical Blog DEVELOPER Home Blog Forums Docs Downloads Training Join Technical Blog Subscribe Related Resources Developer Tools & Techniques English中文 Run High-Performance LLM Inference Kernels from NVIDIA Using FlashInfer​​ Jun 13, 2025 By Luis Ceze, Zihao Ye, Tianqi Chen, Vinod Grover, Mehdi Amini and Nick Comly Like Discuss (0) L T F R E AI-Generated Summary Like Dislike FlashInfer is a customizable and efficient library for building LLM serving engines, optimizing KV-cache storage and featuring a customizable attention template that adapts to various settings through just-in-time compilation. The library splits LLM workloads into four operator families: Attention, GEMM, Communication, and Sampling, and

### MLSys 2026 FlashInfer AI Kernel Generation Contest

- URL: https://mlsys26.flashinfer.ai
- raw snapshot: `raw/hot-topics-sources/2026-04-10/103-mlsys-2026-flashinfer-ai-kernel-generation-contest.md`
- 수집 제목: NVIDIA Track | MLSys 2026 FlashInfer AI Kernel Generation Contest

NVIDIA Track | MLSys 2026 FlashInfer AI Kernel Generation Contest MLSys 2026 - NVIDIA Track Overview Tracks Timeline Prizes Register MLSys 2026 Competition - NVIDIA Track FlashInfer AI Kernel Generation Contest Create high-performance GPU kernels for state-of-the-art LLM architectures on NVIDIA Blackwell GPUs with humans and/or AI agents Register NowLearn MoreJoin Discord Organizer and Sponsors Contest Overview 🎯 The Challenge Create optimized CUDA kernels for cutting-edge LLM operations, either by hand or with AI agents. Receive kernel specifications and produce high-performance code for NVIDIA Blackwell B200 GPUs. 📊 Benchmark Compete across workloads derived from production models. Kernels are evaluated on correctness, speed, and win rate against FlashInfer baselines. Platform Submit and

### FlashInfer on ROCm: High-Throughput Prefill Attention via AITER

- URL: https://rocm.blogs.amd.com/artificial-intelligence/flashinfer-release2/README.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/104-flashinfer-on-rocm-high-throughput-prefill-attention-via-aiter.md`
- 수집 제목: FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER — ROCm Blogs

FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER — ROCm BlogsSkip to main content Back to top Ctrl+K ROCm™ Blogs Home AI HPC Data Science Systems Developers Robotics ROCm blogs FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER Contents What is FlashInfer? FlashInfer on ROCm Feature Support Matrix Porting to Modern CDNA Architectures Experimental AITER Backend Support Known Limitations Getting Started Single-request Prefill Attention with AITER Backend Batched Prefill with Paged KV Cache Summary Acknowledgements References Disclaimers FlashInfer on ROCm: High‑Throughput Prefill Attention via AITER# April 06, 2026 by Debasis Mandal, Diptorup Deb, Rishi Madduri, Anuya Welling, Mukhil Azhagan Mallaiyan Sathiaseelan, Yao Liu, Phani Vaddadi, Vish Vadlamani. 2 min rea
