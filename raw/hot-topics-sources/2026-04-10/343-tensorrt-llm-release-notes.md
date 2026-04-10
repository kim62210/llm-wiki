---
title: Release Notes — TensorRT LLM
source_url: https://nvidia.github.io/TensorRT-LLM/release-notes.html
final_url: https://nvidia.github.io/TensorRT-LLM/release-notes.html
status: 200
content_type: text/html; charset=utf-8
topics: [TensorRT-LLM 1.3 with Day-0 Model Support]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:10.283855+00:00
---

# Release Notes — TensorRT LLM

## 원본 URL

https://nvidia.github.io/TensorRT-LLM/release-notes.html

## 추출 본문

Release Notes — TensorRT LLM
Skip to main content

Back to topCtrl+K

TensorRT LLM

 Choose version 

SearchCtrl+K

SearchCtrl+K

TensorRT LLM

 Choose version 

Table of Contents

Getting Started

Overview

Quick Start Guide

Installation
Pre-built release container images on NGC

Installing on Linux via 
pip

Building from Source Code on Linux

Supported Hardware

Deployment Guide

LLM Examples
Generate text

Generate text asynchronously

Generate text in streaming

Distributed LLM Generation

Generate text with guided decoding

Control generated text using logits processor

Generate text with multiple LoRA adapters

Sparse Attention

Speculative Decoding

KV Cache Connector

KV Cache Offloading

Runtime Configuration Examples

Sampling Techniques Showcase

Run LLM-API with pytorch backend on Slurm

Run trtllm-bench with pytorch backend on Slurm

Run trtllm-serve with pytorch backend on Slurm

Online Serving Examples
Aiperf Client

Aiperf Client For Multimodal

Curl Chat Client

Curl Chat Client For Multimodal

Curl Completion Client

Curl Responses Client

Deepseek R1 Reasoning Parser

OpenAI Chat Client

OpenAI Chat Client for Multimodal

OpenAI Completion Client

Openai Completion Client For Lora

OpenAI Completion Client with JSON Schema

OpenAI Responses Client

Prometheus Metrics

Dynamo K8s Example

Model Recipes
Deployment Guide for Nemotron v3 Super on TensorRT LLM - Blackwell & Hopper Hardware

Deployment Guide for DeepSeek R1 on TensorRT LLM - Blackwell & Hopper Hardware

Deployment Guide for Llama3.3 70B on TensorRT LLM - Blackwell & Hopper Hardware

Deployment Guide for Llama4 Scout 17B on TensorRT LLM - Blackwell & Hopper Hardware

Deployment Guide for GPT-OSS on TensorRT-LLM - Blackwell Hardware

Deployment Guide for Qwen3 on TensorRT LLM - Blackwell & Hopper Hardware

Deployment Guide for Qwen3 Next on TensorRT LLM - Blackwell & Hopper Hardware

Deployment Guide for Kimi K2 Thinking on TensorRT LLM - Blackwell

Deployment Guide for GLM-5 on TensorRT LLM - Blackwell Hardware

CPU Affinity configuration in TensorRT LLM

Models

Supported Models

Visual Generation (Beta)

Adding a New Model

CLI Reference

trtllm-bench

trtllm-eval

trtllm-serve
trtllm-serve

Run benchmarking with 
trtllm-serve

API Reference

LLM API Introduction

API Reference

Features

Feature Combination Matrix

Multi-Head, Multi-Query, and Group-Query Attention

Disaggregated Serving

KV Cache System

Long Sequences

LoRA (Low-Rank Adaptation)

Multimodal Support in TensorRT LLM

Overlap Scheduler

Paged Attention, IFB, and Request Scheduling

Parallelism in TensorRT LLM

Quantization

Sampling

Additional Outputs

Guided Decoding

Speculative Decoding

Checkpoint Loading

AutoDeploy (Beta)

Ray Orchestrator (Prototype)

Torch Compile & Piecewise CUDA Graph

Helix Parallelism

KV Cache Connector

Sparse Attention

Developer Guide

Architecture Overview

Performance Analysis

TensorRT LLM Benchmarking

Continuous Integration Overview

Using Dev Containers

LLM API Change Guide

Introduction to KV Cache Transmission

Blogs

DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72

Optimizing MoE Communication with One-Sided AlltoAll Over NVLink

Sparse Attention in TensorRT LLM

Accelerating Long-Context Inference with Skip Softmax Attention

Optimizing DeepSeek-V3.2 on NVIDIA Blackwell GPUs

Scaling Expert Parallelism in TensorRT LLM (Part 3: Pushing the Performance Boundary)

Inference Time Compute Implementation in TensorRT LLM

Combining Guided Decoding and Speculative Decoding: Making CPU and GPU Cooperate Seamlessly

Running GPT-OSS-120B with Eagle3 Speculative Decoding on GB200/B200 (TensorRT LLM)

ADP Balance Strategy

Running a High Performance GPT-OSS-120B Inference Server with TensorRT LLM

Scaling Expert Parallelism in TensorRT LLM (Part 2: Performance Status and Optimization)

N-Gram Speculative Decoding in TensorRT LLM

How to launch Llama4 Maverick + Eagle3 TensorRT LLM server

Disaggregated Serving in TensorRT LLM

Scaling Expert Parallelism in TensorRT LLM (Part 1: Design and Implementation of Large-scale EP)

Optimizing DeepSeek R1 Throughput on NVIDIA Blackwell GPUs: A Deep Dive for Developers

DeepSeek R1 MTP Implementation and Optimization

Pushing Latency Boundaries: Optimizing DeepSeek-R1 Performance on NVIDIA B200 GPUs

How to get best performance on DeepSeek-R1 in TensorRT LLM

H200 achieves nearly 12,000 tokens/sec on Llama2-13B with TensorRT LLM

New XQA-kernel provides 2.4x more Llama-70B throughput within the same latency budget

H100 has 4.6x A100 Performance in TensorRT LLM, achieving 10,000 tok/s at 100ms to first token

Falcon-180B on a single H200 GPU with INT4 AWQ, and 6.7x faster Llama-70B over A100

Speed up inference with SOTA quantization techniques in TRT-LLM

Quick Links

Releases

Github Code

Roadmap

Use TensorRT Engine

LLM API with TensorRT Engine

Release Notes

Release Notes#

All published functionality in the Release Notes has been fully tested and verified with known limitations documented. To share feedback about this release, access our NVIDIA Developer Forum.

TensorRT-LLM Release 1.2#

Key Features and Enhancements#

DGX Spark Support (Beta)

Added beta support for single-node DGX Spark.

Validated models and precision formats:

GPT-OSS-20B, GPT-OSS-120B (MXFP4)

Llama-3.1-8B-Instruct (FP16/FP8/NVFP4)

Llama-3.3-70B-Instruct (FP8/NVFP4)

Qwen3-8B, Qwen3-14B (FP16/FP8/NVFP4)

Qwen3-32B (FP16/NVFP4)

Qwen3-30B-A3B (FP16/NVFP4)

NVIDIA-Nemotron-Nano-9B-v2 (FP4)

Llama-3.3-Nemotron-Super-49B-v1.5 (FP8)

Phi-4-multimodal-instruct (FP16/FP8/NVFP4)

Phi-4-reasoning-plus (FP16/FP8/NVFP4)

Infrastructure Changes#

API Changes#

Fixed Issues#

Known Issues#

DGX Spark: DGX Spark support is in beta. Only single-node configurations and the models listed above have been validated in this release.

Disaggregated Serving: A hang may occur in disaggregated serving with context pipeline parallelism and generation tensor parallelism configurations.

TensorRT-LLM Release 1.1#

Key Features and Enhancements#

Model Support

Add GPT-OSS model support.

Add Hunyuan-Dense model support. Thanks to the contribution from @sorenwu.

Add Hunyuan-MoE model support. Thanks to the contribution from @qianbiaoxiang.

Add Seed-OSS model support. Thanks to the contribution from @Nekofish-L.

Features

KV Cache & Context:

Connector API: Introduced a new KV Cache Connector API for state transfer in disaggregated serving.

Reuse & Offloading: Enabled KV cache reuse for MLA (Multi-Head Latent Attention) and added examples for host offloading.

Salting: Implemented KV cache salting for secure cache reuse.

Speculative Decoding:

Guided Decoding Integration: Enabled guided decoding to work in conjunction with speculative decoding (including 2-model and draft model chunked prefill).

Eagle: Added multi-layer Eagle support and optimizations.

Disaggregated Serving:

Added support for Guided Decoding in disaggregated mode.

Optimized KV cache transfer for uneven pipeline parallelism.

Performance:

DeepEP: Optimized low-precision (FP4) combined kernels and all-to-all communication.

AutoTuner: Refactored tuning config and generalized tactic selection for better kernel performance.

CuteDSL: Integrated CuteDSL NVFP4 grouped GEMM for Blackwell.

Hardware:

B300/GB300: Added support for B300/GB300.

Benchmark

New Benchmarks:

Disaggregated Serving: Added dedicated performance tests for disaggregated serving scenarios (
test_perf.py
).

Multimodal: Enabled 
benchmark_serving
 support for multimodal models.

NIM: Added specific performance test cases for NIM (NVIDIA Inference Microservices) integration.

Tooling Improvements:

trtllm-bench: Added support for sampler options, accurate device iteration timing, and improved data loading for benchmark datasets.

Metrics: Enhanced reporting to include KV cache size metrics in benchmark results.

Scaffolding: Added benchmark support for scaffolding examples.

Documentation

Deployment Guides: Added comprehensive deployment guides for GPT-OSS, DeepSeek-R1, and VDR 1.0.

Feature Documentation: Created new documentation for KV Cache Connector, LoRA feature usage, and AutoDeploy.

Tech Blogs: Published blogs on “Combining Guided Decoding and Speculative Decoding” and “ADP Balance Strategy”.

Quick Start: Refined Quick Start guides with new links to ModelOpt checkpoints and updated installation steps (Linux/Windows).

API Reference: Enhanced LLM API documentation by explicitly labeling stable vs. unstable APIs.

Performance: Updated online benchmarking documentation and performance overview pages.

Examples: Refined Slurm examples and added K2 tool calling examples.

Infrastructure Changes#

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:25.10-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:25.10-py3
.

The dependent public PyTorch version is updated to 2.9.0.

The dependent NVIDIA ModelOpt version is updated to 0.37.

The dependent xgrammar version is updated to 0.1.25.

The dependent transformers version is updated to 4.56.0.

The dependent NIXL version is updated to 0.5.0.

API Changes#

Breaking Change: The C++ TRTLLM sampler is now enabled by default, replacing the legacy implementation. A new 
sampler_type
 argument has been introduced to 
SamplingConfig
 to explicitly control sampler selection.

KV Cache Connector API: Introduced a new KV Cache Connector API to facilitate state transfer between Disaggregated Serving workers (Context and Generation phases).

LLM API Enhancements:

Added support for 
prompt_logprobs
 in the PyTorch backend.

Standardized 
topk
 logprob returns across TRT and PyTorch backends.

Added stable labels to arguments in the 
LLM
 class to better indicate API stability.

Response API: Added basic functionality for the Responses API to better handle streaming and non-streaming responses.

Multimodal Inputs: Updated the 
MultimodalParams
 API to support 
SharedTensor
, improving memory management for visual language models.

Wait and Cancel API: Added tests and support for handling non-existent and completed request cancellations in the executor.

Fixed Issues#

DeepSeek-V3/R1:

Fixed potential hangs in DeepSeek-V3 pipelines by adjusting MNNVL configurations.

Resolved illegal memory access errors in FP8 Scout and DeepSeek models.

Fixed weight loading issues for DeepSeek-R1 W4A8 checkpoints (TP16 scenarios).

Llama 4: Fixed FP4 generation issues and corrected all-reduce operations in the last decoder layer.

Mistral/Pixtral: Fixed a batching bug in Mistral 3.1 where processing multiple requests with images in the same batch caused failures.

Qwen: Fixed Qwen2.5-VL failures related to CUDA graph padding and transformers version compatibility.

Gemma: Fixed out-of-bounds vector access for models with multiple layer types and resolved accuracy issues in Gemma 2.

Speculative Decoding:

Fixed race conditions in one-model speculative decoding.

Resolved CUDA graph warmup issues that caused failures when using speculative decoding.

Fixed KV cache recompute logic in 
draft_target
 speculative decoding.

MoE (Mixture of Experts):

Fixed OOM issues in fused MoE kernels by optimizing workspace pre-allocation.

Corrected Cutlass MoE integration to fix accuracy issues on Blackwell hardware.

Fixed W4A8 MoE kernel issues on Hopper architecture.

General:

Fixed a potential hang caused by Python multiprocessing when prefetching weights.

Resolved an issue where 
torch.onnx.export
 would fail with newer PyTorch versions by correctly falling back to non-dynamo modes.

Fixed numerical stability issues for XQA kernels when using speculative decoding.

Fixed a memory leak in the 
cacheTransceiver
 that could lead to hangs in disaggregated serving.

Known Issues#

GB300 Multi-Node: Support for GB300 in multi-node configurations is currently in beta and not fully validated in this release. GB300 multi-node configurations have been validated in 1.2.0rc4+.

TensorRT-LLM Release 1.0#

TensorRT LLM 1.0 brings 2 major changes: the PyTorch-based architecture is now stable and the default experience, and the LLM API is now stable. For more details on new developments in 1.0, please see below.

Key Features and Enhancements#

Model Support

Add Mistral3.1 VLM model support

Add TensorRT-Engine Qwen3 (dense) model support

Add phi-4-multimodal model support

Add EXAONE 4.0 model support

Add Qwen3 MoE support to TensorRT backend

Features

Add support for sm121

Add LoRA support for Gemma3

Support PyTorch LoRA adapter eviction

Add LoRA support for PyTorch backend in trtllm-serve

Add support of scheduling attention dp request

Remove padding of FusedMoE in attention DP

Support torch compile for attention dp

Add KV events support for sliding window attention

Add TRTLLM MoE nvfp4 cubins for mid-high concurrency; attention_dp for TRTLLM MoE

Add Piecewise CUDA Graph support for MLA

Support multiCtasKvMode for high-throughput MLA kernels

Enable kvcache to be reused during request generation

Add ADP schedule balance optimization

Add chunked prefill support for MLA (Blackwell)

Enable Multi-block mode for Hopper spec dec XQA kernel

Add vLLM KV Pool support for XQA kernel

Allow sending more than 2GiB through MPI by using mpi4py.util.pkl5

Add support for fused gate_up_proj scales for FP8 blockwise

Support FP8 row-wise dense GEMM in torch flow

Enable fp8 SwiGLU to minimize host overhead

Add Deepseek R1 FP8 Support on Blackwell

Add support for MXFP8xMXFP4 in pytorch

Support nvfp4 model and fp8 kv cache for MLA chunked prefill (Blackwell)

Opensource MOE MXFP8-MXFP4 implementation

Add support for Modelopt fp8_pb_wo quantization scheme

Support deepEP fp4 post quant all2all dispatch

Fuse w4a8 moe pre-quant scale on Hopper

Support Weight-Only-Quantization in PyTorch Workflow

Add support for per expert activation scaling factors

Add ReDrafter support for Qwen

Enable CUDA Graph for Nemotron-H

Add support for YARN in NemotronNAS models

Switch to internal version of MMProjector in Gemma3

Disable add special tokens for Llama3.3 70B

Auto-enable ngram with concurrency <= 32

Support turning on/off spec decoding dynamically

Support structural tag in C++ runtime and upgrade xgrammar to 0.1.21

Add support for external multimodal embeddings

Add support for disaggregation with pp with pytorch backend

Add status tags to LLM API reference

Support JSON Schema in OpenAI-Compatible API

Support chunked prefill on spec decode 2 model

Add KV cache reuse support for multimodal models

Support nanobind bindings

Add support for two-model engine KV cache reuse

Add Eagle-3 support for qwen3 dense model

Migrate Eagle-3 and draft/target speculation to Drafter

Enable guided decoding with overlap scheduler

Support n-gram speculative decoding with disagg

Add beam search support to the PyTorch Workflow

Add LLGuidance Support for PyTorch Backend

Add NGrams V2 support

Add MTP support for Online EPLB

Support disaggregated serving in TRTLLM Sampler

Add core infrastructure to enable loading of custom checkpoint formats

Support TRTLLM_DEEP_EP_TOKEN_LIMIT to allow run deep-ep on memory-constrained GPUs

Use huge page mapping for host accessible memory on GB200

Add user-provided speculative decoding support

Add streaming scaffolding_llm.generate_async support

Detokenize option in /v1/completions request

Integrate TRT-LLM Gen FP4 block scale MoE with Pytorch workflow kernel autotuner

Remove support for llmapi + TRT backend in Triton

Add request_perf_metrics to triton LLMAPI backend

Add support for Triton request cancellation

Benchmark:

Add support for benchmarking individual gemms in MOE benchmark (#6080)

Add speculative metrics for trtllm-bench

Add the ability to write a request timeline for trtllm-bench

Add no_kv_cache_reuse option and streaming support for trtllm-serve bench

Add latency support for trtllm-bench

Add Acceptance Rate calculation to benchmark_serving

Add wide-ep benchmarking scripts

Update trtllm-bench to support new Pytorch default

Add support for TRTLLM CustomDataset

Make benchmark_serving part of the library

Documentation:

Refactored the doc structure to focus on the PyTorch workflow.

Improved the LLMAPI and API reference documentation. Stable APIs are now protected and will remain consistent in subsequent versions following v1.0.

Removed legacy documentation related to the TensorRT workflow.

Infrastructure Changes#

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:25.06-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:25.06-py3
.

The dependent NVIDIA ModelOpt version is updated to 0.33.

The dependent xgrammar version is updated to 0.1.21.

The dependent transformers version is updated to 4.53.1.

API Changes#

BREAKING CHANGE Promote PyTorch to be the default LLM backend

BREAKING CHANGE Change default backend to PyTorch in trtllm-serve

BREAKING CHANGE Unify KvCacheConfig in LLM class for pytorch backend

BREAKING CHANGE Rename cuda_graph_config padding_enabled field

BREAKING CHANGE Rename mixed_sampler to enable_mixed_sampler

BREAKING CHANGE Rename LLM.autotuner_enabled to enable_autotuner

Add back allreduce_strategy parameter into TorchLlmArgs

Add LlmArgs option to force using dynamic quantization

Change default LoRA cache sizes and change peft_cache_config cache size fields to take effect when not explicitly set in lora_config

Remove deprecated LoRA LLM args, that are already specified in lora_config

Add request_perf_metrics to LLMAPI

Remove batch_manager::KvCacheConfig and use executor::KvCacheConfig instead

Remove TrtGptModelOptionalParams

Remove ptuning knobs from TorchLlmArgs

Fixed Issues#

Fix illegal memory access in MLA (#6437)

Fix nemotronNAS loading for TP>1 (#6447)

Fix wide EP when using DeepEP with online EPLB (#6429)

Fix bugs caused by None attention_bias during Qwen3 model convert engine (#6344)

Fix PD + MTP + overlap scheduler accuracy issue (#6136)

Fix bug of Qwen3 when using fp4 on sm120 (#6065)

Fix TMA error with GEMM+AR on TP=2 (#6075)

Fix scaffolding aime test in test_e2e (#6140)

Fix KV Cache overrides in trtllm-bench (#6103)

Fix MOE benchmark to rotate buffers to prevent L2 cache reuse (#4135)

Fix eagle3 two model disaggregated serving test (#6014)

Fix chunked prefill + overlap scheduling (#5761)

Fix mgmn postprocess error (#5835)

Fallback to cubins for fp8 fmha kernels on Ada (#5779)

Fix disagg + speculative decoding (#5558)

Fix test_generate_with_seed CI failure. (#5772)

Fix prompt adapter TP2 case (#5782)

Fix disaggregate serving with attention DP (#4993)

Fix a quote error introduced in #5534 (#5816)

Fix the accuracy issue when reduce_fusion is enabled for GEMMA model. (#5801)

Fix lost requests for disaggregated serving (#5815)

Update unit tests: skip all_close assert for dropout in attention, increase tolerance for rope op test (#5855)

Fix GEMM+AR fusion on blackwell (#5563)

Fix llama4 multimodal support (#5809)

Fix Llama4 Scout FP4 crash issue (#5925)

Fix max batch size and max tokens in kv cache estimations for Nemotron-H (#5371)

Fix moe regression for sm120 (#5823)

Fix Qwen2.5VL FP8 support (#5029)

Fix the illegal memory access issue in moe gemm on SM120 (#5636)

Fix tileN cannot % 16==0 & support sm89 deepgemm bmm (#5531)

Fix incremental detokenization (#5825)

Fix MoE workspace info by storing Torch tensor itself instead of data_ptr (#5900)

Fix mistral unit tests due to transformers upgrade (#5904)

Fix the Llama3.1 405B hanging issue. (#5698) (#5925)

Fix Gemma3 unit tests due to transformers upgrade (#5921)

Fix alltoall for llama4 (apply_router_weight_on_input=True) (#5902)

Remove SpecConfig and fix thread leak issues (#5931)

Fast redux detection in trtllm gen routing kernel (#5941)

Fix cancel request logic (#5800)

Fix errors in wide-ep scripts (#5992)

Fix error in post-merge-tests (#5949)

Fix missing arg to alltoall_prepare_maybe_dispatch (#5669)

Fix attention DP doesn’t work with embedding TP (#5642)

Fix broken cyclic reference detect (#5417)

Fix permission for local user issues in NGC docker container. (#5373)

Fix mtp vanilla draft inputs (#5568)

Fix mPtrExpertCounts allocation in MoE TRT-LLM backend (nvfp4) (#5519)

Fix block scale fp8 support for deepseek v3 on Blackwell. (#5514)

Fix the issue MoE autotune fallback failed to query default heuristic (#5520)

Fix the unexpected keyword argument ‘streaming’ (#5436)

Known Issues#

When using disaggregated serving with pipeline parallelism and KV cache reuse, a hang can occur. This will be fixed in a future release. In the meantime, disabling KV cache reuse will fix this issue.

Running multi-node cases where each node has just a single GPU is known to fail. This will be addressed in a future release.

For the Llama 3.x and Llama 4 models, there is an issue with pipeline parallelism when using FP8 and NVFP4 weights. As a workaround, you can set the environment variable 
exportTRTLLM_LLAMA_EAGER_FUSION_DISABLED=1
.

TensorRT-LLM Release 0.21.0#

Key Features and Enhancements#

Model Support

Added Gemma3 VLM support

Features

Added large-scale EP support

Integrated NIXL into the communication layer of the disaggregated service

Added fabric Memory support for KV Cache Transfer

Added MCP in ScaffoldingLLM

Added support for w4a8_mxfp4_fp8 quantization

Added support for fp8 rowwise quantization

Added generation logits support in TRTLLM Sampler

Added log probs support in TRTLLM Sampler

Optimized TRTLLM Sampler perf single beam single step

Enabled Disaggregated serving for Qwen-3

Added EAGLE3 support for Qwen-3

Fused finalize and allreduce for Qwen-MoE model

Refactored Fused MoE module

Added support for chunked attention on Blackwell and Hopper

Introduced sliding-window attention kernels for the generation phase on Blackwell

Updated DeepSeek FP8 TRT-LLM Gen cubins to improve performance in large batch size scenarios

Added FP8 block-scale GEMM support on SM89

Enabled overlap scheduler between draft forwards

Added Piecewise cuda graph support for MLA

Added model-agnostic one-engine eagle3

Enabled Finalize + Allreduce + add + rmsnorm fusion

Integrated TRT-LLM Gen FP8 block scale MoE with Pytorch workflow kernel autotuner

Added support for Eagle3 + disaggregated serving in two model speculative decoding flow

Validated Llama 3.1 models on H200 NVL

Benchmark:

Added all_reduce.py benchmark script for testing

Added beam width to trtllm-bench latency command

Fixed trtllm-bench iter_stats and cuda_graph_batch_sizes errors

Enabled trtllm-bench to run LoRA and add basic e2e perf testing capability for LoRA

Supported post_proc for bench

Added no_kv_cache_reuse option and streaming support for trtllm serve bench

Infrastructure Changes#

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:25.05-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:25.05-py3
.

The dependent public PyTorch version is updated to 2.7.1.

The dependent TensorRT version is updated to 10.11.

The dependent NVIDIA ModelOpt version is updated to 0.31.

The dependent NCCL version is updated to 2.27.5.

API Changes#

Set _AutoDeployLlmArgs as primary config object

Removed decoder request from decoder interface

Enhanced the torch_compile_config in llm args

Removed the redundant use_kv_cache field from PytorchConfig

Moved allreduce_strategy from committed api to reference

Fixed Issues#

Fixed disaggregated service hang when MNNVL two-shot AllReduce is enabled (#4678)

Fixed EP load balancer with MTP layer and route offset by EP rank (#4767)

Fixed cuda graph padding for spec decoding (#4853)

Fixed llama 4 long context issue (#4809)

Fixed max_num_sequences calculation with overlap scheduling (#4532)

Fixed chunked prefill + overlap scheduling (#5761)

Fixed trtllm-bench hang issue due to LLM API IPC (#4798)

Fixed index out of bounds error in spec decoding (#5954)

Fixed MTP illegal memory access in cuda graph warmup (#5947)

Fixed no free slots error with spec decode + disagg (#5975)

Fixed one-off attention window size for Gemma3 1B (#5564)

Known Issues#

accuracy/test_cli_flow::TestGpt2::test_beam_search_large is broken.

Enabling disaggregated serving, MTP, and the overlap scheduler at the same time can lead to accuracy problems.

In 0.21, full chunked attention support has been added to make sure LLaMA4 model can functionally run with > 8K seq length, while there is a known performance regression(only affect LLaMA4 model) on Hopper due to this functional enhancement. The root cause of the regression has been identified already and the fix will be part of the future release.

TensorRT-LLM Release 0.20.0#

Key Features and Enhancements#

Model Support

Added Qwen3 support. Refer to “Qwen3” section in 
examples/models/core/qwen/README.md
.

Added HyperCLOVAX-SEED-Vision support in PyTorch flow. Refer to 
examples/models/contrib/hyperclovax/README.md

Added Dynasor-CoT in scaffolding examples. Refer to 
examples/scaffolding/contrib/Dynasor/README.md

Added Mistral Small 3.1 24B VLM support in TRT workflow

Added Gemma3-1b-it support in PyTorch workflow

Added Nemotron-H model support

Added Eagle-3 support for LLAMA4

PyTorch workflow

Added lora support

Added return logits support

Adopt new logprob definition in PyTorch flow

Enabled per-request stats with PyTorch backend

Enabled LogitsProcessor in PyTorch backend

Benchmark:

Add beam width to low latency.

Fix trtllm-bench iter_stats and cuda_graph_batch_sizes errors.

Remove deprecated Python runtime benchmark

Add benchmark support for scaffolding

Multimodal models

Added support in trtllm-serve

Added support in trtllm-bench, the support is limited to image only for now

Supported DeepSeek-R1 W4A8 on Hopper

Add the RTX Pro 6000 support on single GPU

Integrated Llama4 input processor

Added CGA reduction FHMA kernels on Blackwell

Enabled chunked context for FlashInfer

Supported KV cache reuse for MLA

Added Piecewise CUDA Graph support

Supported multiple LoRA adapters and TP

Added KV cache-aware router for disaggregated serving

Unfused attention for native support

Added group_rms_norm kernel to normalize multiple inputs in a single operator

Added smart router for the MoE module

Added head size 72 support for QKV preprocessing kernel

Added MNNVL MoE A2A support

Optimized Large Embedding Tables in Multimodal Models

Supported Top-K logprobs and prompt_logprobs in LLMAPI

Enabled overlap scheduler in TRT workflow via executor API

Infrastructure Changes#

TRT-LLM team formally releases docker image on NGC.

The pre-built TensorRT-LLM wheel on PyPI is linked against PyTorch 2.7.0 now, which uses the CXX11 ABI

The dependent TensorRT version is updated to 10.10.0

The dependent CUDA version is updated to 12.9.0

The dependent public PyTorch version is updated to 2.7.0

The dependent NVIDIA ModelOpt version is updated to 0.29.0

The dependent NCCL version is maintained at 2.25.1

Open-sourced XQA kernels

Dependent datasets version was upgraded to 3.1.0

Migrate Triton Backend from TensorRT LLM repo to TensorRT LLM submodule

Downgrade gcc toolset version from 13 to 11

API Changes#

[BREAKING CHANGE] Enable scheduling overlap by default

Remove deprecated GptSession/V1 from TRT workflow

Set _AutoDeployLlmArgs as primary config object

Allow overriding CLI arguments with YAML file in trtllm-serve

Introduced multimodal embedding field in LlmRequest

Fixed Issues#

Fix hang bug when context server doesn’t have enough capacity for KV Cache (#3095)

Fix C++ decoder synchronization in PyTorch (#3106)

Fix bug related to creating CUDA stream as default parameter, which will be initialized during importing (#3764)

Fix attention DP bug on Qwen3 MoE model (#4141)

Fix illegal memory access when running LLaMA 4 with CUDA Graph enabled (#4101)

Reset planned states to avoid memory leak in TrtllmAttentionWrapper (#4227)

Known Issues#

multi-GPU model support on RTX Pro 6000

TensorRT-LLM Release 0.19.0#

Key Features and Enhancements#

The C++ runtime is now open sourced.

PyTorch workflow

Added DeepSeek V3/R1 support. Refer to 
examples/deepseek_v3/README.md
, also to the blog 
docs/source/blogs/Best_perf_practice_on_DeepSeek-R1_in_TensorRT-LLM.md
.

Added Llava-Next support.

Added BERT support.

Added a C++ based decoder, which added support for:

TopK / TopP.

Bad words.

Stop words.

Embedding bias.

Added Autotuner for custom-op-compatible tuning process.

Added a Python-based Autotuner core framework for kernel tuning.

Applied the Autotuner to fused MoE and NVFP4 linear operators for concept and performance evaluations.

Added guided decoding support (XGrammar integration).

Added pipeline parallelism support for the overlap scheduler in 
PyExecutor
.

Added Qwen2VL model support.

Added mixed precision quantization support.

Added pipeline parallelism with attention DP support.

Added no-cache attention support.

Added 
PeftCacheManager
 support.

Added Qwen2.5‑VL support and refactored Qwen2‑VL.

Added trtllm‑gen FP4 GEMM support.

Added Qwen2 MoE support.

Applied 
AutoTuner
 to both Fused MoE and NVFP4 Linear operators.

Introduced a 
UserBuffers
 allocator.

Added Deepseek eager mode AllReduce fusion support.

Added Multi-Token Prediction (MTP) support. Refer to the “Multi-Token Prediction (MTP)” section of 
examples/deepseek_v3/README.md
.

Added FlashMLA support for SM90.

Added support for enabling MTP with CUDA graph padding.

Added initial EAGLE-3 implementation.

Added support for FP8 MLA on NVIDIA Hopper and Blackwell GPUs.

AutoDeploy for PyTorch workflow.

The AutoDeploy for PyTorch workflow is an experimental feature in 
tensorrt_llm._torch.auto_deploy
.

AutoDeploy provides an automated path from off-the-shelf models to optimized deployment in the TensorRT-LLM runtime.

Check out 
examples/auto_deploy/README.md
 for more details.

LLM API

[BREAKING CHANGE] Added dynamic logits processor support, and deprecated static logits processor.

Added batched logits processor support.

Added EAGLE support.

Added abort request support.

Added 
get_stats
 support.

Added multi-node support for Slurm-based clusters, refer to 
examples/llm-api/llm_mgmn_*.sh
.

Added InternLM-XComposer2 support. Refer to “InternLM-XComposer2” section in 
examples/multimodal/README.md
.

Added INT4-AWQ support for MoE models. Refer to the “AWQ Quantization” section in 
examples/mixtral/README.md
.

Added Qwen2-Audio support. Refer to 
examples/qwen2audio/README.md
.

Added Language-Adapter support. Refer to 
examples/language_adapter/README.md
.

Added STDiT for OpenSoRA text-to-video support. Refer to 
examples/stdit/README.md
.

Added vision encoders with tensor parallelism and context parallelism support. Refer to 
examples/vit/README.md
.

Added EXAONE-Deep support. Refer to 
examples/exaone/README.md
.

Added support for Phi-4-mini and Phi‑4‑MM.

Added Gemma3 text‑only model support. Refer to “Run Gemma 3” section at 
examples/gemma/README.md
.

Added FP8 quantization support for Qwen2-VL.

Added batched inference support for the LLM API MMLU example 
examples/mmlu_llmapi.py
.

Added FP4 quantization-layernorm fusion plugin support. (Llama models only)

Added Mamba-Hybrid support.

Added NVILA video support. The support includes 1 prompt - N media and N prompt - N media batching modes.

Added a 
--quantize_lm_head
 option 
examples/quantization/quantize.py
 to support 
lm_head
 quantization.

Added batched tensor FP4 quantization support.

Added a 
/metrics
 endpoint for 
trtllm-serve
 to log iteration statistics.

Added LoRA support for Phi-2 model.

Added returning context logits support for 
trtllm-serve
.

Added one-shot version for UserBuffer AllReduce-Normalization on FP16/BF16.

Added request BW metric measurement for 
disaggServerBenchmark
.

Updated logits bitmask kernel to v3.

Enabled CUDA graphs when attention DP was used and active requests on different GPUs were uneven.

Added iteration log support for 
trtllm-bench
.

fp8_blockscale_gemm
 is now open-sourced.

Added AWQ support for ModelOpt checkpoints.

Added Linear block scale layout support in FP4 quantization.

Added pre-quantized FP8 checkpoint support for Nemotron-mini-4b-instruct.

Added Variable-Beam-Width-Search (VBWS) support (part2).

Added LoRA support for Gemma.

Refactored scaffolding worker, added OpenAI API worker support.

Optionally split MoE inputs into chunks to reduce GPU memory usage.

Added UCX IP interface support.

[BREAKING CHANGE] Added output of first token to additional generation outputs.

Added FP8 support for SM120 architecture.

Registered 
ENABLE_MULTI_DEVICE
 and 
ENABLE_UCX
 as CMake options.

Made the scaffolding Controller more generic.

Breaking change: Added individual gatherContext support for each additional output.

Enabled 
PyExecutor
 inference flow to estimate 
max_num_tokens
 for 
kv_cache_manager
.

Added 
TLLM_OVERRIDE_LAYER_NUM
 and 
TLLM_TRACE_MODEL_FORWARD
 environment variables for debugging.

Supported aborting disconnected requests.

Added an option to run disaggregated serving without context servers.

Fixed and improved allreduce and fusion kernels.

Enhanced the integrated robustness of scaffolding via 
init.py
.

API Changes#

Exposed 
kv_cache_retention_config
 from C++ 
executor
 API to the LLM API.

Moved 
BuildConfig
 arguments to 
LlmArgs
.

Removed speculative decoding parameters from stateful decoders.

Exposed 
DecoderState
 via bindings and integrated it in decoder.

Refactored the 
LlmArgs
 with 
Pydantic
 and migrated remaining pybinding configurations to Python.

Refactored disaggregated serving scripts.

Added 
numNodes
 to 
ParallelConfig
.

Redesigned the multi‑stream API for DeepSeek.

Fixed Issues#

Fixed misused length argument of PluginField. Thanks to the contribution from @jl749 in #2712. This also fixes #2685.

Fixed a Llama-3.2 SmoothQuant convert checkpoint issue. (#2677)

Fixed a bug when loading an engine using LoRA through the LLM API. (#2782)

Fixed incorrect batch slot usage in 
addCumLogProbs
 kernel. Thanks to the contribution from @aotman in #2787.

Fixed incorrect output for Llama-3.2-11B-Vision-Instruct. (#2796)

Removed the necessity of 
--extra-index-urlhttps://pypi.nvidia.com
 when running 
pipinstalltensorrt-llm
.

Infrastructure Changes#

The dependent NVIDIA ModelOpt version is updated to 0.27.

Known Issues#

The PyTorch workflow on SBSA is incompatible with bare metal environments like Ubuntu 24.04. Please use the PyTorch NGC Container for optimal support on SBSA platforms.

TensorRT-LLM Release 0.18.2#

Key Features and Enhancements#

This update addresses known security issues. For the latest NVIDIA Vulnerability Disclosure Information visit https://www.nvidia.com/en-us/security/.

TensorRT-LLM Release 0.18.1#

Key Features and Enhancements#

The 0.18.x series of releases builds upon the 0.17.0 release, focusing exclusively on dependency updates without incorporating features from the previous 0.18.0.dev pre-releases. These features will be included in future stable releases.

Infrastructure Changes#

The dependent 
transformers
 package version is updated to 4.48.3.

TensorRT-LLM Release 0.18.0#

Key Features and Enhancements#

Features that were previously available in the 0.18.0.dev pre-releases are not included in this release.

[BREAKING CHANGE] Windows platform support is deprecated as of v0.18.0. All Windows-related code and functionality will be completely removed in future releases.

Known Issues#

The PyTorch workflow on SBSA is incompatible with bare metal environments like Ubuntu 24.04. Please use the PyTorch NGC Container for optimal support on SBSA platforms.

Infrastructure Changes#

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:25.03-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:25.03-py3
.

The dependent TensorRT version is updated to 10.9.

The dependent CUDA version is updated to 12.8.1.

The dependent NVIDIA ModelOpt version is updated to 0.25 for Linux platform.

TensorRT-LLM Release 0.17.0#

Key Features and Enhancements#

Blackwell support

NOTE: pip installation is not supported for TRT-LLM 0.17 on Blackwell platforms only. Instead, it is recommended that the user build from source using NVIDIA NGC 25.01 PyTorch container.

Added support for B200.

Added support for GeForce RTX 50 series using Windows Subsystem for Linux (WSL) for limited models.

Added NVFP4 Gemm support for Llama and Mixtral models.

Added NVFP4 support for the 
LLM
 API and 
trtllm-bench
 command.

GB200 NVL is not fully supported.

Added benchmark script to measure perf benefits of KV cache host offload with expected runtime improvements from GH200.

PyTorch workflow

The PyTorch workflow is an experimental feature in 
tensorrt_llm._torch
. The following is a list of supported infrastructure, models, and features that can be used with the PyTorch workflow.

Added support for H100/H200/B200.

Added support for Llama models, Mixtral, QWen, Vila.

Added support for FP16/BF16/FP8/NVFP4 Gemm and fused Mixture-Of-Experts (MOE), FP16/BF16/FP8 KVCache.

Added custom context and decoding attention kernels support via PyTorch custom op.

Added support for chunked context (default off).

Added CudaGraph support for decoding only.

Added overlap scheduler support to overlap prepare inputs and model forward by decoding 1 extra token.

Added FP8 context FMHA support for the W4A8 quantization workflow.

Added ModelOpt quantized checkpoint support for the 
LLM
 API.

Added FP8 support for the Llama-3.2 VLM model. Refer to the “MLLaMA” section in 
examples/multimodal/README.md
.

Added PDL support for 
userbuffer
 based AllReduce-Norm fusion kernel.

Added runtime support for seamless lookahead decoding.

Added token-aligned arbitrary output tensors support for the C++ 
executor
 API.

API Changes#

[BREAKING CHANGE] KV cache reuse is enabled automatically when 
paged_context_fmha
 is enabled.

Added 
--concurrency
 support for the 
throughput
 subcommand of 
trtllm-bench
.

Known Issues#

Need 
--extra-index-urlhttps://pypi.nvidia.com
 when running 
pipinstalltensorrt-llm
 due to new third-party dependencies.

The PYPI SBSA wheel is incompatible with PyTorch 2.5.1 due to a break in the PyTorch ABI/API, as detailed in the related GitHub issue.

The PyTorch workflow on SBSA is incompatible with bare metal environments like Ubuntu 24.04. Please use the PyTorch NGC Container for optimal support on SBSA platforms.

Fixed Issues#

Fixed incorrect LoRA output dimension. Thanks for the contribution from @akhoroshev in #2484.

Added NVIDIA H200 GPU into the 
cluster_key
 for auto parallelism feature. (#2552)

Fixed a typo in the 
__post_init__
 function of 
LLmArgs
 Class. Thanks for the contribution from @topenkoff in #2691.

Fixed workspace size issue in the GPT attention plugin. Thanks for the contribution from @AIDC-AI.

Fixed Deepseek-V2 model accuracy.

Infrastructure Changes#

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:25.01-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:25.01-py3
.

The dependent TensorRT version is updated to 10.8.0.

The dependent CUDA version is updated to 12.8.0.

The dependent ModelOpt version is updated to 0.23 for Linux platform, while 0.17 is still used on Windows platform.

TensorRT-LLM Release 0.16.0#

Key Features and Enhancements#

Added guided decoding support with XGrammar backend.

Added quantization support for RecurrentGemma. Refer to 
examples/recurrentgemma/README.md
.

Added ulysses context parallel support. Refer to an example on building LLaMA 7B using 2-way tensor parallelism and 2-way context parallelism at 
examples/llama/README.md
.

Added W4A8 quantization support to BF16 models on Ada (SM89).

Added PDL support for the FP8 GEMM plugins.

Added a runtime 
max_num_tokens
 dynamic tuning feature, which can be enabled by setting 
--enable_max_num_tokens_tuning
 to 
gptManagerBenchmark
.

Added typical acceptance support for EAGLE.

Supported chunked context and sliding window attention to be enabled together.

Added head size 64 support for the XQA kernel.

Added the following features to the LLM API:

Lookahead decoding.

DeepSeek V1 support.

Medusa support.

max_num_tokens
 and 
max_batch_size
 arguments to control the runtime parameters.

extended_runtime_perf_knob_config
 to enable various performance configurations.

Added LogN scaling support for Qwen models.

Added 
AutoAWQ
 checkpoints support for Qwen. Refer to the “INT4-AWQ” section in 
examples/qwen/README.md
.

Added 
AutoAWQ
 and 
AutoGPTQ
 Hugging Face checkpoints support for LLaMA. (#2458)

Added 
allottedTimeMs
 to the C++ 
Request
 class to support per-request timeout.

[BREAKING CHANGE] Removed NVIDIA V100 GPU support.

API Changes#

[BREAKING CHANGE] Removed 
enable_xqa
 argument from 
trtllm-build
.

[BREAKING CHANGE] Chunked context is enabled by default when KV cache and paged context FMHA is enabled on non-RNN based models.

[BREAKING CHANGE] Enabled embedding sharing automatically when possible and remove the flag 
--use_embedding_sharing
 from convert checkpoints scripts.

[BREAKING CHANGE] The 
if__name__=="__main__"
 entry point is required for both single-GPU and multi-GPU cases when using the 
LLM
 API.

[BREAKING CHANGE] Cancelled requests now return empty results.

Added the 
enable_chunked_prefill
 flag to the 
LlmArgs
 of the 
LLM
 API.

Integrated BERT and RoBERTa models to the 
trtllm-build
 command.

Model Updates#

Added Qwen2-VL support. Refer to the “Qwen2-VL” section of 
examples/multimodal/README.md
.

Added multimodal evaluation examples. Refer to 
examples/multimodal
.

Added Stable Diffusion XL support. Refer to 
examples/sdxl/README.md
. Thanks for the contribution from @Zars19 in #1514.

Fixed Issues#

Fixed unnecessary batch logits post processor calls. (#2439)

Fixed a typo in the error message. (#2473)

Fixed the in-place clamp operation usage in smooth quant. Thanks for the contribution from @StarrickLiu in #2485.

Fixed 
sampling_params
 to only be setup if 
end_id
 is None and 
tokenizer
 is not None in the 
LLM
 API. Thanks to the contribution from @mfuntowicz in #2573.

Infrastructure Changes#

Updated the base Docker image for TensorRT-LLM to 
nvcr.io/nvidia/pytorch:24.11-py3
.

Updated the base Docker image for TensorRT-LLM Backend to 
nvcr.io/nvidia/tritonserver:24.11-py3
.

Updated to TensorRT v10.7.

Updated to CUDA v12.6.3.

Added support for Python 3.10 and 3.12 to TensorRT-LLM Python wheels on PyPI.

Updated to ModelOpt v0.21 for Linux platform, while v0.17 is still used on Windows platform.

Known Issues#

There is a known AllReduce performance issue on AMD-based CPU platforms on NCCL 2.23.4, which can be worked around by 
exportNCCL_P2P_LEVEL=SYS
.

TensorRT-LLM Release 0.15.0#

Key Features and Enhancements#

Added support for EAGLE. Refer to 
examples/eagle/README.md
.

Added functional support for GH200 systems.

Added AutoQ (mixed precision) support.

Added a 
trtllm-serve
 command to start a FastAPI based server.

Added FP8 support for Nemotron NAS 51B. Refer to 
examples/nemotron_nas/README.md
.

Added INT8 support for GPTQ quantization.

Added TensorRT native support for INT8 Smooth Quantization.

Added quantization support for Exaone model. Refer to 
examples/exaone/README.md
.

Enabled Medusa for Qwen2 models. Refer to “Medusa with Qwen2” section in 
examples/medusa/README.md
.

Optimized pipeline parallelism with ReduceScatter and AllGather for Mixtral models.

Added support for 
Qwen2ForSequenceClassification
 model architecture.

Added Python plugin support to simplify plugin development efforts. Refer to 
examples/python_plugin/README.md
.

Added different rank dimensions support for LoRA modules when using the Hugging Face format. Thanks for the contribution from @AlessioNetti in #2366.

Enabled embedding sharing by default. Refer to “Embedding Parallelism, Embedding Sharing, and Look-Up Plugin” section in 
docs/source/performance/perf-best-practices.md
 for information about the required conditions for embedding sharing.

Added support for per-token per-channel FP8 (namely row-wise FP8) on Ada.

Extended the maximum supported 
beam_width
 to 
256
.

Added FP8 and INT8 SmoothQuant quantization support for the InternVL2-4B variant (LLM model only). Refer to 
examples/multimodal/README.md
.

Added support for prompt-lookup speculative decoding. Refer to 
examples/prompt_lookup/README.md
.

Integrated the QServe w4a8 per-group/per-channel quantization. Refer to “w4aINT8 quantization (QServe)” section in 
examples/llama/README.md
.

Added a C++ example for fast logits using the 
executor
 API. Refer to “executorExampleFastLogits” section in 
examples/cpp/executor/README.md
.

[BREAKING CHANGE] NVIDIA Volta GPU support is removed in this and future releases.

Added the following enhancements to the LLM API:

[BREAKING CHANGE] Moved the runtime initialization from the first invocation of 
LLM.generate
 to 
LLM.__init__
 for better generation performance without warmup.

Added 
n
 and 
best_of
 arguments to the 
SamplingParams
 class. These arguments enable returning multiple generations for a single request.

Added 
ignore_eos
, 
detokenize
, 
skip_special_tokens
, 
spaces_between_special_tokens
, and 
truncate_prompt_tokens
 arguments to the 
SamplingParams
 class. These arguments enable more control over the tokenizer behavior.

Added support for incremental detokenization to improve the detokenization performance for streaming generation.

Added the 
enable_prompt_adapter
 argument to the 
LLM
 class and the 
prompt_adapter_request
 argument for the 
LLM.generate
 method. These arguments enable prompt tuning.

Added support for a 
gpt_variant
 argument to the 
examples/gpt/convert_checkpoint.py
 file. This enhancement enables checkpoint conversion with more GPT model variants. Thanks to the contribution from @tonylek in #2352.

API Changes#

[BREAKING CHANGE] Moved the flag 
builder_force_num_profiles
 in 
trtllm-build
 command to the 
BUILDER_FORCE_NUM_PROFILES
 environment variable.

[BREAKING CHANGE] Modified defaults for 
BuildConfig
 class so that they are aligned with the 
trtllm-build
 command.

[BREAKING CHANGE] Removed Python bindings of 
GptManager
.

[BREAKING CHANGE] 
auto
 is used as the default value for 
--dtype
 option in quantize and checkpoints conversion scripts.

[BREAKING CHANGE] Deprecated 
gptManager
 API path in 
gptManagerBenchmark
.

[BREAKING CHANGE] Deprecated the 
beam_width
 and 
num_return_sequences
 arguments to the 
SamplingParams
 class in the LLM API. Use the 
n
, 
best_of
 and 
use_beam_search
 arguments instead.

Exposed 
--trust_remote_code
 argument to the OpenAI API server. (#2357)

Model Updates#

Added support for Llama 3.2 and llama 3.2-Vision model. Refer to 
examples/mllama/README.md
 for more details on the llama 3.2-Vision model.

Added support for Deepseek-v2. Refer to 
examples/deepseek_v2/README.md
.

Added support for Cohere Command R models. Refer to 
examples/commandr/README.md
.

Added support for Falcon 2, refer to 
examples/falcon/README.md
, thanks to the contribution from @puneeshkhanna in #1926.

Added support for InternVL2. Refer to 
examples/multimodal/README.md
.

Added support for Qwen2-0.5B and Qwen2.5-1.5B model. (#2388)

Added support for Minitron. Refer to 
examples/nemotron
.

Added a GPT Variant - Granite(20B and 34B). Refer to “GPT Variant - Granite” section in 
examples/gpt/README.md
.

Added support for LLaVA-OneVision model. Refer to “LLaVA, LLaVa-NeXT, LLaVA-OneVision and VILA” section in 
examples/multimodal/README.md
.

Fixed Issues#

Fixed a slice error in forward function. (#1480)

Fixed an issue that appears when building BERT. (#2373)

Fixed an issue that model is not loaded when building BERT. (#2379)

Fixed the broken executor examples. (#2294)

Fixed the issue that the kernel 
moeTopK()
 cannot find the correct expert when the number of experts is not a power of two. Thanks @dongjiyingdjy for reporting this bug.

Fixed an assertion failure on 
crossKvCacheFraction
. (#2419)

Fixed an issue when using smoothquant to quantize Qwen2 model. (#2370)

Fixed a PDL typo in 
docs/source/performance/perf-benchmarking.md
, thanks @MARD1NO for pointing it out in #2425.

Infrastructure Changes#

The base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:24.10-py3
.

The base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:24.10-py3
.

The dependent TensorRT version is updated to 10.6.

The dependent CUDA version is updated to 12.6.2.

The dependent PyTorch version is updated to 2.5.1.

The dependent ModelOpt version is updated to 0.19 for Linux platform, while 0.17 is still used on Windows platform.

Documentation#

Added a copy button for code snippets in the documentation. (#2288)

TensorRT-LLM Release 0.14.0#

Key Features and Enhancements#

Enhanced the 
LLM
 class in the LLM API.

Added support for calibration with offline dataset.

Added support for Mamba2.

Added support for 
finish_reason
 and 
stop_reason
.

Added FP8 support for CodeLlama.

Added 
__repr__
 methods for class 
Module
, thanks to the contribution from @1ytic in #2191.

Added BFloat16 support for fused gated MLP.

Updated ReDrafter beam search logic to match Apple ReDrafter v1.1.

Improved 
customAllReduce
 performance.

Draft model now can copy logits directly over MPI to the target model’s process in 
orchestrator
 mode. This fast logits copy reduces the delay between draft token generation and the beginning of target model inference.

NVIDIA Volta GPU support is deprecated and will be removed in a future release.

API Changes#

[BREAKING CHANGE] The default 
max_batch_size
 of the 
trtllm-build
 command is set to 
2048
.

[BREAKING CHANGE] Remove 
builder_opt
 from the 
BuildConfig
 class and the 
trtllm-build
 command.

Add logits post-processor support to the 
ModelRunnerCpp
 class.

Added 
isParticipant
 method to the C++ 
Executor
 API to check if the current process is a participant in the executor instance.

Model Updates#

Added support for NemotronNas, see 
examples/nemotron_nas/README.md
.

Added support for Deepseek-v1, see 
examples/deepseek_v1/README.md
.

Added support for Phi-3.5 models, see 
examples/phi/README.md
.

Fixed Issues#

Fixed a typo in 
tensorrt_llm/models/model_weights_loader.py
, thanks to the contribution from @wangkuiyi in #2152.

Fixed duplicated import module in 
tensorrt_llm/runtime/generation.py
, thanks to the contribution from @lkm2835 in #2182.

Enabled 
share_embedding
 for the models that have no 
lm_head
 in legacy checkpoint conversion path, thanks to the contribution from @lkm2835 in #2232.

Fixed 
kv_cache_type
 issue in the Python benchmark, thanks to the contribution from @qingquansong in #2219.

Fixed an issue with SmoothQuant calibration with custom datasets. Thanks to the contribution by @Bhuvanesh09 in #2243.

Fixed an issue surrounding 
trtllm-build--fast-build
 with fake or random weights. Thanks to @ZJLi2013 for flagging it in #2135.

Fixed missing 
use_fused_mlp
 when constructing 
BuildConfig
 from dict, thanks for the fix from @ethnzhng in #2081.

Fixed lookahead batch layout for 
numNewTokensCumSum
. (#2263)

Infrastructure Changes#

The dependent ModelOpt version is updated to v0.17.

Documentation#

@Sherlock113 added a tech blog to the latest news in #2169, thanks for the contribution.

Known Issues#

Replit Code is not supported with the transformers 4.45+

TensorRT-LLM Release 0.13.0#

Key Features and Enhancements#

Supported lookahead decoding (experimental), see 
docs/source/speculative_decoding.md
.

Added some enhancements to the 
ModelWeightsLoader
 (a unified checkpoint converter, see 
docs/source/architecture/model-weights-loader.md
).

Supported Qwen models.

Supported auto-padding for indivisible TP shape in INT4-wo/INT8-wo/INT4-GPTQ.

Improved performance on 
*.bin
 and 
*.pth
.

Supported OpenAI Whisper in C++ runtime.

Added some enhancements to the 
LLM
 class.

Supported LoRA.

Supported engine building using dummy weights.

Supported 
trust_remote_code
 for customized models and tokenizers downloaded from Hugging Face Hub.

Supported beam search for streaming mode.

Supported tensor parallelism for Mamba2.

Supported returning generation logits for streaming mode.

Added 
curand
 and 
bfloat16
 support for 
ReDrafter
.

Added sparse mixer normalization mode for MoE models.

Added support for QKV scaling in FP8 FMHA.

Supported FP8 for MoE LoRA.

Supported KV cache reuse for P-Tuning and LoRA.

Supported in-flight batching for CogVLM models.

Supported LoRA for the 
ModelRunnerCpp
 class.

Supported 
head_size=48
 cases for FMHA kernels.

Added FP8 examples for DiT models, see 
examples/dit/README.md
.

Supported decoder with encoder input features for the C++ 
executor
 API.

API Changes#

[BREAKING CHANGE] Set 
use_fused_mlp
 to 
True
 by default.

[BREAKING CHANGE] Enabled 
multi_block_mode
 by default.

[BREAKING CHANGE] Enabled 
strongly_typed
 by default in 
builder
 API.

[BREAKING CHANGE] Renamed 
maxNewTokens
, 
randomSeed
 and 
minLength
 to 
maxTokens
, 
seed
 and 
minTokens
 following OpenAI style.

The 
LLM
 class

[BREAKING CHANGE] Updated 
LLM.generate
 arguments to include 
PromptInputs
 and 
tqdm
.

The C++ 
executor
 API

[BREAKING CHANGE] Added 
LogitsPostProcessorConfig
.

Added 
FinishReason
 to 
Result
.

Model Updates#

Supported Gemma 2, see “Run Gemma 2” section in 
examples/gemma/README.md
.

Fixed Issues#

Fixed an accuracy issue when enabling remove padding issue for cross attention. (#1999)

Fixed the failure in converting qwen2-0.5b-instruct when using 
smoothquant
. (#2087)

Matched the 
exclude_modules
 pattern in 
convert_utils.py
 to the changes in 
quantize.py
. (#2113)

Fixed build engine error when 
FORCE_NCCL_ALL_REDUCE_STRATEGY
 is set.

Fixed unexpected truncation in the quant mode of 
gpt_attention
.

Fixed the hang caused by race condition when canceling requests.

Fixed the default factory for 
LoraConfig
. (#1323)

Infrastructure Changes#

Base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:24.07-py3
.

Base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:24.07-py3
.

The dependent TensorRT version is updated to 10.4.0.

The dependent CUDA version is updated to 12.5.1.

The dependent PyTorch version is updated to 2.4.0.

The dependent ModelOpt version is updated to v0.15.

TensorRT-LLM Release 0.12.0#

Key Features and Enhancements#

Supported LoRA for MoE models.

The 
ModelWeightsLoader
 is enabled for LLaMA family models (experimental), see 
docs/source/architecture/model-weights-loader.md
.

Supported FP8 FMHA for NVIDIA Ada Lovelace Architecture.

Supported GPT-J, Phi, Phi-3, Qwen, GPT, GLM, Baichuan, Falcon and Gemma models for the 
LLM
 class.

Supported FP8 OOTB MoE.

Supported Starcoder2 SmoothQuant. (#1886)

Supported ReDrafter Speculative Decoding, see “ReDrafter” section in 
docs/source/speculative_decoding.md
.

Supported padding removal for BERT, thanks to the contribution from @Altair-Alpha in #1834.

Added in-flight batching support for GLM 10B model.

Supported 
gelu_pytorch_tanh
 activation function, thanks to the contribution from @ttim in #1897.

Added 
chunk_length
 parameter to Whisper, thanks to the contribution from @MahmoudAshraf97 in #1909.

Added 
concurrency
 argument for 
gptManagerBenchmark
.

Executor API supports requests with different beam widths, see 
docs/source/executor.md#sending-requests-with-different-beam-widths
.

Added the flag 
--fast_build
 to 
trtllm-build
 command (experimental).

API Changes#

[BREAKING CHANGE] 
max_output_len
 is removed from 
trtllm-build
 command, if you want to limit sequence length on engine build stage, specify 
max_seq_len
.

[BREAKING CHANGE] The 
use_custom_all_reduce
 argument is removed from 
trtllm-build
.

[BREAKING CHANGE] The 
multi_block_mode
 argument is moved from build stage (
trtllm-build
 and builder API) to the runtime.

[BREAKING CHANGE] The build time argument 
context_fmha_fp32_acc
 is moved to runtime for decoder models.

[BREAKING CHANGE] The arguments 
tp_size
, 
pp_size
 and 
cp_size
 are removed from 
trtllm-build
 command.

The C++ batch manager API is deprecated in favor of the C++ 
executor
 API, and it will be removed in a future release of TensorRT-LLM.

Added a version API to the C++ library, a 
cpp/include/tensorrt_llm/executor/version.h
 file is going to be generated.

Model Updates#

Supported LLaMA 3.1 model.

Supported Mamba-2 model.

Supported EXAONE model, see 
examples/exaone/README.md
.

Supported Qwen 2 model.

Supported GLM4 models, see 
examples/chatglm/README.md
.

Added LLaVa-1.6 (LLaVa-NeXT) multimodal support, see “LLaVA, LLaVa-NeXT and VILA” section in 
examples/multimodal/README.md
.

Fixed Issues#

Fixed wrong pad token for the CodeQwen models. (#1953)

Fixed typo in 
cluster_infos
 defined in 
tensorrt_llm/auto_parallel/cluster_info.py
, thanks to the contribution from @saeyoonoh in #1987.

Removed duplicated flags in the command at 
docs/source/reference/troubleshooting.md
, thanks for the contribution from @hattizai in #1937.

Fixed segmentation fault in TopP sampling layer, thanks to the contribution from @akhoroshev in #2039. (#2040)

Fixed the failure when converting the checkpoint for Mistral Nemo model. (#1985)

Propagated 
exclude_modules
 to weight-only quantization, thanks to the contribution from @fjosw in #2056.

Fixed wrong links in README, thanks to the contribution from @Tayef-Shah in #2028.

Fixed some typos in the documentation, thanks to the contribution from @lfz941 in #1939.

Fixed the engine build failure when deduced 
max_seq_len
 is not an integer. (#2018)

Infrastructure Changes#

Base Docker image for TensorRT-LLM is updated to 
nvcr.io/nvidia/pytorch:24.07-py3
.

Base Docker image for TensorRT-LLM Backend is updated to 
nvcr.io/nvidia/tritonserver:24.07-py3
.

The dependent TensorRT version is updated to 10.3.0.

The dependent CUDA version is updated to 12.5.1.

The dependent PyTorch version is updated to 2.4.0.

The dependent ModelOpt version is updated to v0.15.0.

Known Issues#

On Windows, installation of TensorRT-LLM may succeed, but you might hit 
OSError:exception:accessviolationreading0x0000000000000000
 when importing the library in Python.

TensorRT-LLM Release 0.11.0#

Key Features and Enhancements#

Supported very long context for LLaMA (see “Long context evaluation” section in 
examples/llama/README.md
).

Low latency optimization

Added a reduce-norm feature which aims to fuse the ResidualAdd and LayerNorm kernels after AllReduce into a single kernel, which is recommended to be enabled when the batch size is small and the generation phase time is dominant.

Added FP8 support to the GEMM plugin, which benefits the cases when batch size is smaller than 4.

Added a fused GEMM-SwiGLU plugin for FP8 on SM90.

LoRA enhancements

Supported running FP8 LLaMA with FP16 LoRA checkpoints.

Added support for quantized base model and FP16/BF16 LoRA.

SQ OOTB (- INT8 A/W) + FP16/BF16/FP32 LoRA​

INT8/ INT4 Weight-Only (INT8 /W) + FP16/BF16/FP32 LoRA​

Weight-Only Group-wise + FP16/BF16/FP32 LoRA

Added LoRA support to Qwen2, see “Run models with LoRA” section in 
examples/qwen/README.md
.

Added support for Phi-3-mini/small FP8 base + FP16/BF16 LoRA, see “Run Phi-3 with LoRA” section in 
examples/phi/README.md
.

Added support for starcoder-v2 FP8 base + FP16/BF16 LoRA, see “Run StarCoder2 with LoRA” section in 
examples/gpt/README.md
.

Encoder-decoder models C++ runtime enhancements

Supported paged KV cache and inflight batching. (#800)

Suppor
