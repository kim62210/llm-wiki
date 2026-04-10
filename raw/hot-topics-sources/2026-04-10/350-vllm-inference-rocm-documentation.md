---
title: vLLM inference — ROCm Documentation
source_url: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html
final_url: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html
status: 200
content_type: text/html; charset=utf-8
topics: [AMD ROCm as First-Class vLLM Platform]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:11.556971+00:00
---

# vLLM inference — ROCm Documentation

## 원본 URL

https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html

## 추출 본문

vLLM inference — ROCm Documentation
Skip to main content

Back to top

Ctrl+K

The ROCm 7.12.0 technology preview release documentation is available at ROCm Preview documentation. For production use, continue to use ROCm 7.2.1 documentation.

ROCm™ Software 7.2.1
Version List

 GitHub
 

 Community
 

 Blogs
 

 ROCm Developer Hub
 

 ROCm Toolkits
 
ROCm Data Science

ROCm Finance

ROCm Life Science

ROCm LLMExt

ROCm Simulation

 Systems and Infra Docs
 

 Infinity Hub
 

 Support
 

ROCm Documentation

What is ROCm?

Release notes

Compatibility matrix
Linux system requirements

Windows system requirements

Install

ROCm on Linux

HIP SDK on Windows

ROCm on Radeon and Ryzen

Deep learning frameworks
PyTorch compatibility

TensorFlow compatibility

JAX compatibility

DGL compatibility

Build ROCm from source

How to

Use ROCm for AI
Installation

System setup
System validation

Multi-node setup

System health benchmarks

Training
Train a model with Primus and Megatron-LM
Train a model with Megatron-LM (legacy)

Train a model with Primus and PyTorch
Train a model with PyTorch (legacy)

Train a model with Primus and JAX MaxText

Train a model with LLM Foundry

Scale model training

Fine-tuning LLMs
Conceptual overview

Fine-tuning
Use a single GPU

Use multiple GPUs

Inference
Run models from Hugging Face

LLM inference frameworks

vLLM inference

PyTorch inference performance testing

SGLang inference performance testing

vLLM distributed inference with MoRI

SGLang distributed inference with MoRI

SGLang distributed inference with Mooncake

xDiT diffusion inference

Deploy your model

Inference optimization
Model quantization techniques

Model acceleration libraries

Optimize with Composable Kernel

Optimize Triton kernels

Profile and debug

Workload optimization

vLLM V1 performance optimization

AI tutorials

Use ROCm for HPC

System optimization

AMD Instinct MI300X performance guides

System debugging

Use advanced compiler features
ROCm compiler infrastructure

Use AddressSanitizer

OpenMP support

Set the number of CUs

Troubleshoot BAR access limitation

ROCm examples

Conceptual

GPU architecture overview
MI300 microarchitecture
AMD Instinct MI300/CDNA3 ISA

White paper

MI300 and MI200 performance counters

MI350 Series performance counters

MI250 microarchitecture
AMD Instinct MI200/CDNA2 ISA

White paper

MI100 microarchitecture
AMD Instinct MI100/CDNA1 ISA

White paper

File structure (Linux FHS)

GPU isolation techniques

Using CMake

Inception v3 with PyTorch

Reference

ROCm libraries

ROCm tools, compilers, and runtime API

GPU hardware specifications

Hardware atomics operation support

Environment variables

Data types and precision support

Graph safe support

ROCm glossary
Device hardware

Device software

Host software

Performance

Contribute

Contributing to the ROCm documentation
ROCm documentation toolchain

Building documentation

Providing feedback about the ROCm documentation

ROCm licenses

Use ROCm for AI

Use ROCm for AI inference

vLLM inference

vLLM inference

 Contents 

What’s new

Get started

Further reading

Previous versions

vLLM inference#

 2026-02-25
 

 4 min read time
 

 Applies to Linux
 

The ROCm-enabled vLLM Docker image offers a prebuilt,
optimized environment for large language model (LLM) inference on AMD Instinct
MI355X, MI350X, MI325X and MI300X GPUs. This ROCm vLLM Docker image integrates
vLLM and PyTorch tailored specifically for AMD Instinct data center GPUs.

This container integrates ROCm, PyTorch, and vLLM with optimizations tailored
for AMD Instinct data center GPUs, enabling consistent and reproducible
inference deployments.

What’s new#

For vLLM release notes on model support, hardware and performance improvements,
and other highlights, see the vLLM Releases page on GitHub.

It’s now recommended to use the upstream vLLM documentation at docs.vllm.ai for the latest inference and deployment guides.

Get started#

For a consistent and portable inference environment, it’s recommended to use Docker. vLLM
offers a Docker image vllm/vllm-openai-rocm for deployment on AMD
GPUs. Use the following command to pull the latest Docker image from Docker Hub.

dockerpullvllm/vllm-openai-rocm:latest

After pulling the Docker image, follow the vLLM usage documentation: Using
vLLM.

Further reading#

See vLLM inference and vLLM V1 performance optimization for
a brief introduction to vLLM and optimization strategies.

For a list of other ready-made Docker images for AI with ROCm, see
AMD Infinity Hub.

Previous versions#

It’s now recommended to use the upstream vLLM documentation at docs.vllm.ai for the latest deployment guides.

You can find legacy versions of this documentation at
vLLM inference performance testing version history which provide instructions for
inference performance testing for select models. See the Use AMD’s Docker
images
note in the vLLM documentation for more information.

previous

LLM inference frameworks

next

PyTorch inference performance testing

 Contents
 

What’s new

Get started

Further reading

Previous versions

Terms and Conditions

ROCm Licenses and Disclaimers

Privacy

Trademarks

Supply Chain Transparency

Fair and Open Competition

UK Tax Strategy

Cookie Policy

Cookie Settings

© 2026 Advanced Micro Devices, Inc
