---
title: GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub
source_url: https://github.com/flashinfer-ai/flashinfer
final_url: https://github.com/flashinfer-ai/flashinfer
status: 200
content_type: text/html; charset=utf-8
topics: [FlashInfer Kernel Library for LLM Serving]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.288445+00:00
---

# GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub

## 원본 URL

https://github.com/flashinfer-ai/flashinfer

## 추출 본문

GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 flashinfer-ai
/flashinferPublic

Notifications
You must be signed in to change notification settings

Fork
 880

 Star
5.4k

Code

Issues322

Pull requests206

Discussions

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Security and quality

 Insights

flashinfer-ai/flashinfer

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
2,156 Commits

2,156 Commits

.claude/skills

.claude/skills

.devcontainer

.devcontainer

.github

.github

3rdparty

3rdparty

benchmarks

benchmarks

ci

ci

csrc

csrc

docker

docker

docs

docs

flashinfer-cubin

flashinfer-cubin

flashinfer-jit-cache

flashinfer-jit-cache

flashinfer

flashinfer

include/flashinfer

include/flashinfer

licenses

licenses

profiler

profiler

scripts

scripts

tests

tests

.clang-format

.clang-format

.gitignore

.gitignore

.gitmodules

.gitmodules

.pre-commit-config.yaml

.pre-commit-config.yaml

CLAUDE.md

CLAUDE.md

CONTRIBUTING.md

CONTRIBUTING.md

Jenkinsfile

Jenkinsfile

LICENSE

LICENSE

NOTICE

NOTICE

README.md

README.md

build_backend.py

build_backend.py

build_utils.py

build_utils.py

pyproject.toml

pyproject.toml

pytest.ini

pytest.ini

requirements.txt

requirements.txt

version.txt

version.txt

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

High-Performance GPU Kernels for Inference

| Documentation | Latest Release | Blog | Slack | Discussion Forum |

FlashInfer is a library and kernel generator for inference that delivers state-of-the-art performance across diverse GPU architectures. It provides unified APIs for attention, GEMM, and MoE operations with multiple backend implementations including FlashAttention-2/3, cuDNN, CUTLASS, and TensorRT-LLM.

Why FlashInfer?

State-of-the-art Performance: Optimized kernels for prefill, decode, and mixed batching scenarios

Multiple Backends: Automatically selects the best backend for your hardware and workload

Modern Architecture Support: Support for SM75 (Turing) and later (through Blackwell)

Low-Precision Compute: FP8 and FP4 quantization for attention, GEMM, and MoE operations

Production-Ready: CUDAGraph and torch.compile compatible for low-latency serving

Core Features

Attention Kernels

Paged and Ragged KV-Cache: Efficient memory management for dynamic batch serving

Decode, Prefill, and Append: Optimized kernels for all attention phases

MLA Attention: Native support for DeepSeek's Multi-Latent Attention

Cascade Attention: Memory-efficient hierarchical KV-Cache for shared prefixes

Sparse Attention: Block-sparse and variable block-sparse patterns

POD-Attention: Fused prefill+decode for mixed batching

GEMM & Linear Operations

BF16 GEMM: BF16 matrix multiplication for SM10.0+ GPUs.

FP8 GEMM: Per-tensor and groupwise scaling

FP4 GEMM: NVFP4 and MXFP4 matrix multiplication for Blackwell GPUs

Grouped GEMM: Efficient batched matrix operations for LoRA and multi-expert routing

Mixture of Experts (MoE)

Fused MoE Kernels

Multiple Routing Methods: DeepSeek-V3, Llama-4, and standard top-k routing

Quantized MoE: FP8 and FP4 expert weights with block-wise scaling

Sampling & Decoding

Sorting-Free Sampling: Efficient Top-K, Top-P, and Min-P without sorting

Speculative Decoding: Chain speculative sampling support

Communication

AllReduce: Custom implementations

Multi-Node NVLink: MNNVL support for multi-node inference

NVSHMEM Integration: For distributed memory operations

Other Operators

RoPE: LLaMA-style rotary position embeddings (including LLaMA 3.1)

Normalization: RMSNorm, LayerNorm, Gemma-style fused operations

Activations: SiLU, GELU with fused gating

GPU Support

ArchitectureCompute CapabilityExample GPUsTuringSM 7.5T4, RTX 20 seriesAmpereSM 8.0, 8.6A100, A10, RTX 30 seriesAda LovelaceSM 8.9L4, L40, RTX 40 seriesHopperSM 9.0H100, H200BlackwellSM 10.0, 10.3B200, B300BlackwellSM 11.0Jetson ThorBlackwellSM 12.0, 12.1RTX 50 series, DGX Spark

Note: Not all features are supported across all compute capabilities.

News

Latest: 

Notable updates:

[2025-10-08] Blackwell support added in v0.4.0

[2025-03-10] Blog Post Sorting-Free GPU Kernels for LLM Sampling, which explains the design of sampling kernels in FlashInfer.

Getting Started

Installation

Quickstart:

pip install flashinfer-python

Package Options:

flashinfer-python: Core package that compiles/downloads kernels on first use

flashinfer-cubin: Pre-compiled kernel binaries for all supported GPU architectures

flashinfer-jit-cache: Pre-built kernel cache for specific CUDA versions

For faster initialization and offline usage, install the optional packages to have most kernels pre-compiled:

pip install flashinfer-python flashinfer-cubin
# JIT cache (replace cu129 with your CUDA version)
pip install flashinfer-jit-cache --index-url https://flashinfer.ai/whl/cu129

Verify Installation

flashinfer show-config

Basic Usage

importtorchimportflashinfer# Single decode attentionq=torch.randn(32, 128, device="cuda", dtype=torch.float16) # [num_qo_heads, head_dim]k=torch.randn(2048, 32, 128, device="cuda", dtype=torch.float16) # [kv_len, num_kv_heads, head_dim]v=torch.randn(2048, 32, 128, device="cuda", dtype=torch.float16)

output=flashinfer.single_decode_with_kv_cache(q, k, v)

See documentation for comprehensive API reference and tutorials.

Install from Source

git clone https://github.com/flashinfer-ai/flashinfer.git --recursive
cd flashinfer
python -m pip install -v .

For development, install in editable mode:

python -m pip install --no-build-isolation -e . -v

Note: When using 
--no-build-isolation
, pip does not automatically install build dependencies. FlashInfer requires 
setuptools>=77
. If you encounter an error like 
AttributeError: module 'setuptools.build_meta' has no attribute 'prepare_metadata_for_build_editable'
, upgrade pip and setuptools first:

python -m pip install --upgrade pip setuptools

Build optional packages:

# flashinfer-cubincd flashinfer-cubin
python -m build --no-isolation --wheel
python -m pip install dist/*.whl

# flashinfer-jit-cache (customize for your target GPUs)export FLASHINFER_CUDA_ARCH_LIST="7.5 8.0 8.9 9.0a 10.0a 10.3a 11.0a 12.0f"cd flashinfer-jit-cache
python -m build --no-isolation --wheel
python -m pip install dist/*.whl

For more details, see the Install from Source documentation.

Nightly Builds

pip install -U --pre flashinfer-python --index-url https://flashinfer.ai/whl/nightly/ --no-deps
pip install flashinfer-python # Install dependencies from PyPI
pip install -U --pre flashinfer-cubin --index-url https://flashinfer.ai/whl/nightly/
# JIT cache (replace cu129 with your CUDA version)
pip install -U --pre flashinfer-jit-cache --index-url https://flashinfer.ai/whl/nightly/cu129

CLI Tools

FlashInfer provides several CLI commands for configuration, module management, and development:

# Verify installation and view configuration
flashinfer show-config

# List and inspect modules
flashinfer list-modules
flashinfer module-status

# Manage artifacts and cache
flashinfer download-cubin
flashinfer clear-cache

# For developers: generate compile_commands.json for IDE integration
flashinfer export-compile-commands [output_path]

For complete documentation, see the CLI reference.

API Logging

FlashInfer provides comprehensive API logging for debugging. Enable it using environment variables:

# Enable logging (levels: 0=off (default), 1=basic, 3=detailed, 5=statistics)export FLASHINFER_LOGLEVEL=3

# Set log destination (stdout (default), stderr, or file path)export FLASHINFER_LOGDEST=stdout

For detailed information about logging levels, configuration, and advanced features, see Logging in our documentation.

Custom Attention Variants

Users can customize their own attention variants with additional parameters. For more details, refer to our JIT examples.

CUDA Support

Supported CUDA Versions: 12.6, 12.8, 13.0, 13.1

Note: FlashInfer strives to follow PyTorch's supported CUDA versions plus the latest CUDA release.

Adoption

FlashInfer powers inference in:

SGLang

vLLM

TensorRT-LLM

TGI (Text Generation Inference)

MLC-LLM

LightLLM

lorax

ScaleLLM

Acknowledgement

FlashInfer is inspired by FlashAttention, vLLM, stream-K, CUTLASS, and AITemplate.

Citation

If you find FlashInfer helpful in your project or research, please consider citing our paper:

@article{ye2025flashinfer,
 title = {FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving},
 author = { Ye, Zihao and Chen, Lequn and Lai, Ruihang and Lin, Wuwei and Zhang, Yineng and Wang, Stephanie and Chen, Tianqi and Kasikci, Baris and Grover, Vinod and Krishnamurthy, Arvind and Ceze, Luis},
 journal = {arXiv preprint arXiv:2501.01005},
 year = {2025},
 url = {https://arxiv.org/abs/2501.01005}
}

About

 FlashInfer: Kernel Library for LLM Serving
 

flashinfer.ai

Topics

 gpu

 cuda

 jit

 pytorch

 nvidia

 moe

 attention

 llm-inference

 large-large-models

 distributed-inference

Resources

 Readme

License

 Apache-2.0 license
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

5.4k
 stars

Watchers

48
 watching

Forks

880
 forks

 Report repository

Releases
 221

Release v0.6.7.post3
 Latest

Apr 6, 2026

+ 220 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python47.0%

Cuda29.3%

C++22.5%

Jinja0.6%

Shell0.4%

C0.2%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.
