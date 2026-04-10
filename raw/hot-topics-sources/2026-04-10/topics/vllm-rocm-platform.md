---
title: AMD ROCm as First-Class vLLM Platform
section: Infra & Serving
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# AMD ROCm as First-Class vLLM Platform

## 기존 큐레이션 요약

- 정의: vLLM ROCm 백엔드가 MI300X/MI325X/MI350X에서 7개 어텐션 백엔드를 제공.
- 왜 중요한가: 2025년 12월 29일 ROCm CI 파이프라인이 상시 가동되었고 2026년 1월 6일 공식 ROCm vLLM-omni Docker 이미지가 공개되었으며, 2월 27일 vLLM 공식 블로그가 AMD를 first-class platform으로 선언하면서 GPU 공급 병목의 실질적 대안으로 급부상했다.

## 개별 원문 수집 스냅샷

### Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm (2026-02-27)

- URL: https://blog.vllm.ai/2026/02/27/rocm-attention-backend.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/348-beyond-porting-how-vllm-orchestrates-high-performance-inference-on-amd-rocm.md`
- 수집 제목: Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm | vLLM Blog

Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm | vLLM Blog Menu Search DocsDocumentationBlogEventsContactCommunityGitHub Theme DocsBlogEventsContactCommunitySearch⌘J Blog Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm February 27, 202619 min read AMD and Embedded LLM #performance#hardware Introduction The Challenge: Mixed Workloads in Every Batch Other MHA Backends Unified Attention Backends ROCMATTN: Legacy 2-Path Backend The ROCMAITERFA Backend: Kernel Orchestration for AMD Key Innovations Why Explicit 3-Path Routing? Three-Path Processing in Detail Interactive Animation: ROCMAITERFA Request Flow The AITER MLA Backends: Optimized for DeepSeek The Hybrid Approach Absorbed vs Non-Absorbed Recipe Why the Assembly Decode Kernel Matt

### ROCm Becomes a First-Class Platform in the vLLM Ecosystem - ROCm Blogs

- URL: https://rocm.blogs.amd.com/software-tools-optimization/vllm-omni/README.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/349-rocm-becomes-a-first-class-platform-in-the-vllm-ecosystem-rocm-blogs.md`
- 수집 제목: ROCm Becomes a First-Class Platform in the vLLM Ecosystem — ROCm Blogs

ROCm Becomes a First-Class Platform in the vLLM Ecosystem — ROCm BlogsSkip to main content Back to top Ctrl+K ROCm™ Blogs Home AI HPC Data Science Systems Developers Robotics ROCm blogs ROCm Becomes a First-Class Platform in the vLLM Ecosystem Contents vLLM Core (v0.12.0 and v0.13.0): New Features and Performance Optimizations vLLM Core (v0.14.0): A New Standard for Stability ROCm Improvements in v0.14.0 CI Reliability You Can Trust Official Docker Image Releases Quick Start with Docker Easy Installation with vLLM Wheel vLLM-omni: High-Performance Omni-Modality on AMD Day-0 ROCm Support Hardware Validation & Support Production-Ready Infrastructure ROCm Configurations Full Model Support on ROCm Supported Input and Output Modalities Get Started in Seconds Summary Acknowledgements References 

### vLLM Inference - ROCm Documentation

- URL: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/350-vllm-inference-rocm-documentation.md`
- 수집 제목: vLLM inference — ROCm Documentation

vLLM inference — ROCm Documentation Skip to main content Back to top Ctrl+K The ROCm 7.12.0 technology preview release documentation is available at ROCm Preview documentation. For production use, continue to use ROCm 7.2.1 documentation. ROCm™ Software 7.2.1 Version List GitHub Community Blogs ROCm Developer Hub ROCm Toolkits ROCm Data Science ROCm Finance ROCm Life Science ROCm LLMExt ROCm Simulation Systems and Infra Docs Infinity Hub Support ROCm Documentation What is ROCm? Release notes Compatibility matrix Linux system requirements Windows system requirements Install ROCm on Linux HIP SDK on Windows ROCm on Radeon and Ryzen Deep learning frameworks PyTorch compatibility TensorFlow compatibility JAX compatibility DGL compatibility Build ROCm from source How to Use ROCm for AI Installa

### LLM Inference Frameworks - ROCm Documentation

- URL: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/351-llm-inference-frameworks-rocm-documentation.md`
- 수집 제목: LLM inference frameworks — ROCm Documentation

LLM inference frameworks — ROCm Documentation Skip to main content Back to top Ctrl+K The ROCm 7.12.0 technology preview release documentation is available at ROCm Preview documentation. For production use, continue to use ROCm 7.2.1 documentation. ROCm™ Software 7.2.1 Version List GitHub Community Blogs ROCm Developer Hub ROCm Toolkits ROCm Data Science ROCm Finance ROCm Life Science ROCm LLMExt ROCm Simulation Systems and Infra Docs Infinity Hub Support ROCm Documentation What is ROCm? Release notes Compatibility matrix Linux system requirements Windows system requirements Install ROCm on Linux HIP SDK on Windows ROCm on Radeon and Ryzen Deep learning frameworks PyTorch compatibility TensorFlow compatibility JAX compatibility DGL compatibility Build ROCm from source How to Use ROCm for A

### SGLang: Fast Serving Framework on AMD Instinct GPUs - ROCm Blogs

- URL: https://rocm.blogs.amd.com/artificial-intelligence/sglang/README.html
- raw snapshot: `raw/hot-topics-sources/2026-04-10/352-sglang-fast-serving-framework-on-amd-instinct-gpus-rocm-blogs.md`
- 수집 제목: SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD Instinct GPUs — ROCm Blogs

SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD Instinct GPUs — ROCm BlogsSkip to main content Back to top Ctrl+K ROCm™ Blogs Home AI HPC Data Science Systems Developers Robotics ROCm blogs SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD Instinct GPUs Contents What is SGLang? Why SGLang? Use Cases Key Features of SGLang Fast Backend Runtime Flexible Frontend Language Extensive Model Support Docker Setup on Instinct GPUs Generic Build Steps for ROCm Docker Image Quick Start with SGLang Steps to Get Started Using Quantized Models Serving LLaVA NeXT Model Frontend: Structured Generation Language (SGLang) Language Features Multi-Modality Running the Multi-Modality Example JSON Decoding Advanced Multi-GPU Deployment Enable 
