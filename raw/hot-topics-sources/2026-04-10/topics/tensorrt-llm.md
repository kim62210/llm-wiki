---
title: TensorRT-LLM 1.3 with Day-0 Model Support
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# TensorRT-LLM 1.3 with Day-0 Model Support

## 기존 큐레이션 요약

- 정의: NVIDIA의 프로덕션 LLM 엔진으로 Day-0 GPT-OSS 지원과 새 C++ 샘플러를 기본화.
- 왜 중요한가: 2026년 3월 1.3.0rc 시리즈가 활발히 릴리스되면서 GPT-OSS-120B/20B와 EXAONE 4.0 Day-0 지원, B200에서 Llama 4 40k+ tok/s를 기록하며 NVIDIA 하드웨어의 공식 속도 기준점으로 자리잡았다.

## 개별 원문 수집 스냅샷

### TensorRT-LLM Release Notes

- URL: https://nvidia.github.io/TensorRT-LLM/release-notes.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/343-tensorrt-llm-release-notes.md`
- 수집 제목: Release Notes — TensorRT LLM

Release Notes — TensorRT LLM Skip to main content Back to topCtrl+K TensorRT LLM Choose version SearchCtrl+K SearchCtrl+K TensorRT LLM Choose version Table of Contents Getting Started Overview Quick Start Guide Installation Pre-built release container images on NGC Installing on Linux via pip Building from Source Code on Linux Supported Hardware Deployment Guide LLM Examples Generate text Generate text asynchronously Generate text in streaming Distributed LLM Generation Generate text with guided decoding Control generated text using logits processor Generate text with multiple LoRA adapters Sparse Attention Speculative Decoding KV Cache Connector KV Cache Offloading Runtime Configuration Examples Sampling Techniques Showcase Run LLM-API with pytorch backend on Slurm Run trtllm-bench with p

### NVIDIA/TensorRT-LLM GitHub Releases

- URL: https://github.com/NVIDIA/TensorRT-LLM/releases
- raw snapshot: `raw/hot-topics-sources/2026-04-10/344-nvidia-tensorrt-llm-github-releases.md`
- 수집 제목: Releases · NVIDIA/TensorRT-LLM · GitHub

Releases · NVIDIA/TensorRT-LLM · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernizati

### NVIDIA/TensorRT-LLM GitHub Repository

- URL: https://github.com/NVIDIA/TensorRT-LLM
- raw snapshot: `raw/hot-topics-sources/2026-04-10/345-nvidia-tensorrt-llm-github-repository.md`
- 수집 제목: GitHub - NVIDIA/TensorRT-LLM: TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way. · GitHub

GitHub - NVIDIA/TensorRT-LLM: TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitH

### TensorRT LLM Documentation

- URL: https://nvidia.github.io/TensorRT-LLM
- raw snapshot: `raw/hot-topics-sources/2026-04-10/346-tensorrt-llm-documentation.md`
- 수집 제목: Welcome to TensorRT LLM’s Documentation! — TensorRT LLM

Welcome to TensorRT LLM’s Documentation! — TensorRT LLM Skip to main content Back to topCtrl+K TensorRT LLM Choose version SearchCtrl+K SearchCtrl+K TensorRT LLM Choose version Table of Contents Getting Started Overview Quick Start Guide Installation Pre-built release container images on NGC Installing on Linux via pip Building from Source Code on Linux Supported Hardware Deployment Guide LLM Examples Generate text Generate text asynchronously Generate text in streaming Distributed LLM Generation Generate text with guided decoding Control generated text using logits processor Generate text with multiple LoRA adapters Sparse Attention Speculative Decoding KV Cache Connector KV Cache Offloading Runtime Configuration Examples Sampling Techniques Showcase Run LLM-API with pytorch backend on Sl

### TensorRT LLM Speculative Sampling Documentation

- URL: https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/347-tensorrt-llm-speculative-sampling-documentation.md`
- 수집 제목: Speculative Sampling — TensorRT-LLM

Speculative Sampling — TensorRT-LLM Skip to main content Back to topCtrl+K TensorRT-LLM Choose version SearchCtrl+K SearchCtrl+K TensorRT-LLM Choose version Table of Contents Getting Started Overview Quick Start Guide Installation Pre-built release container images on NGC Installing on Linux via pip Building from Source Code on Linux Deployment Guide LLM Examples Generate text Generate text asynchronously Generate text in streaming Distributed LLM Generation Generate text with guided decoding Control generated text using logits processor Generate text with multiple LoRA adapters Speculative Decoding KV Cache Connector Runtime Configuration Examples Sampling Techniques Showcase Run LLM-API with pytorch backend on Slurm Run trtllm-bench with pytorch backend on Slurm Run trtllm-serve with pyt
