---
title: LLM inference frameworks — ROCm Documentation
source_url: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html
final_url: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html
status: 200
content_type: text/html; charset=utf-8
topics: [AMD ROCm as First-Class vLLM Platform]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:11.386843+00:00
---

# LLM inference frameworks — ROCm Documentation

## 원본 URL

https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html

## 추출 본문

LLM inference frameworks — ROCm Documentation
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

LLM...

LLM inference frameworks

 Contents 

vLLM inference
Installing vLLM

Hugging Face TGI
Install TGI

LLM inference frameworks#

 2025-12-29
 

 8 min read time
 

 Applies to Linux
 

This section discusses how to implement vLLM and Hugging Face TGI using
single-accelerator and
multi-accelerator systems.

vLLM inference#

vLLM is renowned for its PagedAttention algorithm that can reduce memory consumption and increase throughput thanks to
its paging scheme. Instead of allocating GPU high-bandwidth memory (HBM) for the maximum output token lengths of the
models, the paged attention of vLLM allocates GPU HBM dynamically for its actual decoding lengths. This paged attention
is also effective when multiple requests share the same key and value contents for a large value of beam search or
multiple parallel requests.

vLLM also incorporates many modern LLM acceleration and quantization algorithms, such as Flash Attention, HIP and CUDA
graphs, tensor parallel multi-GPU, GPTQ, AWQ, and token speculation.

Installing vLLM#

Run the following commands to build a Docker image 
vllm-rocm
.

gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
dockerbuild-fdocker/Dockerfile.rocm-tvllm-rocm.

vLLM on a single-accelerator system

To use vLLM as an API server to serve reference requests, first start a container using the vllm-rocm
Docker image.

dockerrun-it\--network=host\--group-add=video\--ipc=host\--cap-add=SYS_PTRACE\--security-optseccomp=unconfined\--device/dev/kfd\--device/dev/dri\-v<path/to/model>:/app/model\vllm-rocm\bash

Inside the container, start the API server to run on a single GPU on port 8000 using the following command.

python-mvllm.entrypoints.api_server--model/app/model--dtypefloat16--port8000&

The following log message is displayed in your command line indicates that the server is listening for requests.

To test, send it a curl request containing a prompt.

curlhttp://localhost:8000/generate-H"Content-Type: application/json"-d'{"prompt": "What is AMD Instinct?", "max_tokens": 80, "temperature": 0.0 }'

You should receive a response like the following.

{"text":["What is AMD Instinct?\nAmd Instinct is a brand new line of high-performance computing (HPC) processors from Advanced Micro Devices (AMD). These processors are designed to deliver unparalleled performance for HPC workloads, including scientific simulations, data analytics, and machine learning.\nThe Instinct lineup includes a range of processors, from the entry-level Inst"]}

vLLM on a multi-accelerator system

To use vLLM as an API server to serve reference requests, first start a container using the vllm-rocm
Docker image.

dockerrun-it\--network=host\--group-add=video\--ipc=host\--cap-add=SYS_PTRACE\--security-optseccomp=unconfined\--device/dev/kfd\--device/dev/dri\-v<path/to/model>:/app/model\vllm-rocm\bash

To run API server on multiple GPUs, use the 
-tp
 or 
--tensor-parallel-size
 parameter. For example, to use two
GPUs, start the API server using the following command.

python-mvllm.entrypoints.api_server--model/app/model--dtypefloat16-tp2--port8000&

To run multiple instances of API Servers, specify different ports for each server, and use 
ROCR_VISIBLE_DEVICES
 to
isolate each instance to a different GPU.

For example, to run two API servers, one on port 8000 using GPU 0 and 1, one on port 8001 using GPU 2 and 3, use a
a command like the following.

ROCR_VISIBLE_DEVICES=0,1python-mvllm.entrypoints.api_server--model/data/llama-2-7b-chat-hf--dtypefloat16–tp2--port8000&ROCR_VISIBLE_DEVICES=2,3python-mvllm.entrypoints.api_server--model/data/llama-2-7b-chat-hf--dtypefloat16–tp2--port8001&

To test, send it a curl request containing a prompt.

curlhttp://localhost:8000/generate-H"Content-Type: application/json"-d'{"prompt": "What is AMD Instinct?", "max_tokens": 80, "temperature": 0.0 }'

You should receive a response like the following.

{"text":["What is AMD Instinct?\nAmd Instinct is a brand new line of high-performance computing (HPC) processors from Advanced Micro Devices (AMD). These processors are designed to deliver unparalleled performance for HPC workloads, including scientific simulations, data analytics, and machine learning.\nThe Instinct lineup includes a range of processors, from the entry-level Inst"]}

See also

See vLLM V1 performance optimization for performance optimization tips.

ROCm provides a prebuilt optimized Docker image for validating the performance of LLM inference with vLLM
on the MI300X GPU. The Docker image includes ROCm, vLLM, and PyTorch.
For more information, see vLLM inference.

Hugging Face TGI#

Text Generation Inference (TGI) is LLM serving framework from Hugging
Face, and it also supports the majority of high-performance LLM
acceleration algorithms such as Flash Attention, Paged Attention,
CUDA/HIP graph, tensor parallel multi-GPU, GPTQ, AWQ, and token
speculation.

Tip

In addition to LLM serving capability, TGI also provides the Text Generation Inference benchmarking tool.

Install TGI#

Launch the TGI Docker container in the host machine.

dockerrun--nametgi--rm-it--cap-add=SYS_PTRACE--security-optseccomp=unconfined
--device=/dev/kfd--device=/dev/dri--group-addvideo--ipc=host--shm-size256g
--nethost-v$PWD:/data
--entrypoint"/bin/bash"
--envHUGGINGFACE_HUB_CACHE=/data
ghcr.io/huggingface/text-generation-inference:latest-rocm

TGI on a single-accelerator system

Inside the container, launch a model using TGI server on a single GPU.

exportROCM_USE_FLASH_ATTN_V2_TRITON=True
text-generation-launcher--model-idNousResearch/Meta-Llama-3-70B--dtypefloat16--port8000&

To test, send it a curl request containing a prompt.

curlhttp://localhost:8000/generate_stream-XPOST-d'{"inputs":"What is AMD Instinct?","parameters":{"max_new_tokens":20}}'-H'Content-Type: application/json'

You should receive a response like the following.

data:{"index":20,"token":{"id":304,"text":" in","logprob":-1.2822266,"special":false},"generated_text":" AMD Instinct is a new family of data center GPUs designed to accelerate the most demanding workloads in","details":null}

TGI on a multi-accelerator system

Inside the container, launch a model using TGI server on multiple GPUs (four in this case).

exportROCM_USE_FLASH_ATTN_V2_TRITON=True
text-generation-launcher--model-idNousResearch/Meta-Llama-3-8B--dtypefloat16--port8000--num-shard4&

To test, send it a curl request containing a prompt.

curlhttp://localhost:8000/generate_stream-XPOST-d'{"inputs":"What is AMD Instinct?","parameters":{"max_new_tokens":20}}'-H'Content-Type: application/json'

You should receive a response like the following.

data:{"index":20,"token":{"id":304,"text":" in","logprob":-1.2773438,"special":false},"generated_text":" AMD Instinct is a new family of data center GPUs designed to accelerate the most demanding workloads in","details":null}

previous

Running models from Hugging Face

next

vLLM inference

 Contents
 

vLLM inference
Installing vLLM

Hugging Face TGI
Install TGI

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
