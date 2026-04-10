---
title: SGLang Documentation — SGLang
source_url: http://docs.sglang.io
final_url: http://docs.sglang.io
status: 200
content_type: text/html; charset=utf-8
topics: [SGLang on GB300 NVL72 with NVFP4]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:08.107245+00:00
---

# SGLang Documentation — SGLang

## 원본 URL

http://docs.sglang.io

## 추출 본문

SGLang Documentation — SGLang
Skip to main content

Back to top

Ctrl+K

Get Started

Install SGLang

Basic Usage

Sending Requests

OpenAI-Compatible APIs

Ollama-Compatible API

Offline Engine API

SGLang Native APIs

Sampling Parameters

Popular Model Usage (DeepSeek, GPT-OSS, GLM, Llama, MiniMax, Qwen, and more)

Advanced Features

Server Arguments

Loading Models from Object Storage

Hyperparameter Tuning

Attention Backend

Speculative Decoding

Structured Outputs

Structured Outputs For Reasoning Models

Tool Parser

Reasoning Parser

Quantization

Quantized KV Cache

Expert Parallelism

DP, DPA and SGLang DP Router

LoRA Serving

PD Disaggregation

EPD Disaggregation

Pipeline Parallelism for Long Context

Hierarchical KV Caching (HiCache)

Query VLM with Offline Engine

DP for Multi-Modal Encoder in SGLang

Cuda Graph for Multi-Modal Encoder in SGLang

Piecewise CUDA Graph

SGLang Model Gateway

Deterministic Inference

Observability

Checkpoint Engine Integration

SGLang for RL Systems

Supported Models

Text Generation

Retrieval & Ranking

Specialized Models

Extending SGLang

SGLang Diffusion

SGLang Diffusion

Install SGLang-Diffusion

Compatibility Matrix

SGLang Diffusion CLI

SGLang Diffusion OpenAI API

Performance

Ring SP Benchmark: Wan2.2-TI2V-5B (u1r2 vs Baseline)

Attention Backends

Caching Acceleration

Quantization

Contributing to SGLang Diffusion

Hardware Platforms

AMD GPUs

CPU Servers

TPU

NVIDIA Jetson Orin

Ascend NPUs

XPU

Developer Guide

Contribution Guide

Development Guide Using Docker

Development Guide for JIT Kernels

Benchmark and Profiling

Bench Serving Guide

Evaluating New Models with SGLang

References

Troubleshooting and Frequently Asked Questions

Environment Variables

Production Metrics

Production Request Tracing

Multi-Node Deployment

Custom Chat Template

Frontend Language

Post-Training Integration

Release Lookup

Learn More and Join the Community

Repository

Show source

Suggest edit

Open issue

.rst

.pdf

SGLang Documentation

SGLang Documentation#
StarFork

SGLang is a high-performance serving framework for large language models and multimodal models.
It is designed to deliver low-latency and high-throughput inference across a wide range of setups, from a single GPU to large distributed clusters.
Its core features include:

Fast Runtime: Provides efficient serving with RadixAttention for prefix caching, a zero-overhead CPU scheduler, prefill-decode disaggregation, speculative decoding, continuous batching, paged attention, tensor/pipeline/expert/data parallelism, structured outputs, chunked prefill, quantization (FP4/FP8/INT4/AWQ/GPTQ), and multi-LoRA batching.

Broad Model Support: Supports a wide range of language models (Llama, Qwen, DeepSeek, Kimi, GLM, GPT, Gemma, Mistral, etc.), embedding models (e5-mistral, gte, mcdse), reward models (Skywork), and diffusion models (WAN, Qwen-Image), with easy extensibility for adding new models. Compatible with most Hugging Face models and OpenAI APIs.

Extensive Hardware Support: Runs on NVIDIA GPUs (GB200/B300/H100/A100/Spark/5090), AMD GPUs (MI355/MI300), Intel Xeon CPUs, Google TPUs, Ascend NPUs, and more.

Active Community: SGLang is open-source and supported by a vibrant community with widespread industry adoption, powering over 400,000 GPUs worldwide.

RL & Post-Training Backbone: SGLang is a proven rollout backend used for training many frontier models, with native RL integrations and adoption by well-known post-training frameworks such as AReaL, Miles, slime, Tunix, verl and more.

Get Started

Install SGLang

Basic Usage

Sending Requests

OpenAI-Compatible APIs

Ollama-Compatible API

Offline Engine API

SGLang Native APIs

Sampling Parameters

Popular Model Usage (DeepSeek, GPT-OSS, GLM, Llama, MiniMax, Qwen, and more)

Advanced Features

Server Arguments

Loading Models from Object Storage

Hyperparameter Tuning

Attention Backend

Speculative Decoding

Structured Outputs

Structured Outputs For Reasoning Models

Tool Parser

Reasoning Parser

Quantization

Quantized KV Cache

Expert Parallelism

DP, DPA and SGLang DP Router

LoRA Serving

PD Disaggregation

EPD Disaggregation

Pipeline Parallelism for Long Context

Hierarchical KV Caching (HiCache)

Query VLM with Offline Engine

DP for Multi-Modal Encoder in SGLang

Cuda Graph for Multi-Modal Encoder in SGLang

Piecewise CUDA Graph

SGLang Model Gateway

Deterministic Inference

Observability

Checkpoint Engine Integration

SGLang for RL Systems

Supported Models

Text Generation
Large Language Models

Multimodal Language Models

Diffusion Language Models

Retrieval & Ranking
Embedding Models

Rerank Models

Classification API

Specialized Models
Reward Models

Extending SGLang
How to Support New Models

Transformers fallback in SGLang

Use Models From ModelScope

MindSpore Models

SGLang Diffusion

SGLang Diffusion
Key Features

Quick Start

Start Here

Additional Documentation

References

Install SGLang-Diffusion
Standard Installation (NVIDIA GPUs)

Platform-Specific: ROCm (AMD GPUs)

Platform-Specific: MUSA (Moore Threads GPUs)

Platform-Specific: Ascend NPU

Platform-Specific: Apple MPS

Compatibility Matrix
Models x Optimization

Supported Components

Verified LoRA Examples

Special requirements

SGLang Diffusion CLI
Overlay repos for non-diffusers models

Quick Start

Common Options

Configuration Files

Generate

Serve

Component Path Overrides

Diffusers Backend

SGLang Diffusion OpenAI API
Prerequisites

Serve

Endpoints

Performance
Overview

Start Here

Caching at a Glance

Current Baseline Snapshot

References

Ring SP Benchmark: Wan2.2-TI2V-5B (u1r2 vs Baseline)
Benchmark Setup

Online Serving

Benchmarks

Summary

Attention Backends
Overview

Backend options

Selection priority

Configuration

Platform support matrix

Usage

Caching Acceleration
Overview

Cache-DiT

TeaCache

References

Quantization
Quick Reference

Quant Families

NVFP4

Nunchaku (SVDQuant)

ModelSlim

Contributing to SGLang Diffusion
Contributor Guides

On AI-Assisted (“Vibe Coding”) PRs

Commit Message Convention

Performance Reporting

CI-Based Change Protection

Hardware Platforms

AMD GPUs

CPU Servers

TPU

NVIDIA Jetson Orin

Ascend NPUs

XPU

Developer Guide

Contribution Guide

Development Guide Using Docker

Development Guide for JIT Kernels

Benchmark and Profiling

Bench Serving Guide

Evaluating New Models with SGLang

References

Troubleshooting and Frequently Asked Questions

Environment Variables

Production Metrics

Production Request Tracing

Multi-Node Deployment

Custom Chat Template

Frontend Language

Post-Training Integration

Release Lookup

Learn More and Join the Community

next

Install SGLang

By SGLang Team

 
 © Copyright 2023-2026, SGLang.
 

 Last updated on Apr 10, 2026.
