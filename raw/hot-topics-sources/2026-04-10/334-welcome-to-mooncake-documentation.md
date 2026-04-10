---
title: Welcome to Mooncake — Mooncake
source_url: https://kvcache-ai.github.io/Mooncake
final_url: https://kvcache-ai.github.io/Mooncake/
status: 200
content_type: text/html; charset=utf-8
topics: [LMCache + Mooncake KV Cache Layer]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.700613+00:00
---

# Welcome to Mooncake — Mooncake

## 원본 URL

https://kvcache-ai.github.io/Mooncake

## 추출 본문

Welcome to Mooncake — Mooncake
Skip to main content

Back to top

Ctrl+K

Getting Started

Build Guide

Quick Start

Supported Communication Protocols

Mooncake HF3FS Plugin

Mooncake x LMCache: Unite to Pioneer KVCache-Centric LLM Serving System

LMDeploy Disaggregated Serving with MooncakeTransferEngine

SGLang Disaggregated Serving with MooncakeTransferEngine

SGLang HiCache with Mooncake Backend

vLLM Disaggregated Serving

Performance

PD Disaggregation Performance

Benchmark performance on NVIDIA A10

Benchmark performance on NVIDIA A10

SGLang HiCache with Mooncake Backend Benchmark

vLLM with Mooncake Transfer Engine Benchmark

Allocator Performance

Python API Reference

Mooncake Store Python API

Transfer Engine Python API

Mooncake Store HTTP Service

Mooncake EP & Mooncake Backend

Design Documents

Mooncake Architecture

Mooncake Store

P2P Store

Transfer Engine

TENT: Transfer Engine NEXT

Mooncake Transfer Engine Benchmark Tool (
tebench
) Guide

Mooncake x SGLang HiCache System Design

Troubleshooting

Error Code Explanation

Troubleshooting

Deployment

Mooncake Store Deployment & Operations Guide

Community

Governance

Repository

Suggest edit

.md

.pdf

Welcome to Mooncake

 Contents 

Documentation

Welcome to Mooncake#

A KVCache-centric Disaggregated Architecture for LLM Serving.

StarWatchFork

Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI.
Now both the Transfer Engine and Mooncake Store are open-sourced!
This repository also hosts its technical report and the open-sourced traces.

🔄 Updates

Mar 19, 2026: TorchSpec: Speculative Decoding Training at Scale is open sourced, using Mooncake to decouple inference and training via efficient hidden states management.

Feb 12, 2026: Mooncake Joins PyTorch Ecosystem We are thrilled to announce that Mooncake has officially joined the PyTorch Ecosystem!

Jan 28, 2026: FlexKV, a distributed KV store and cache system from Tencent and NVIDIA in collaboration with the community, now supports distributed KVCache reuse with the Mooncake Transfer Engine.

Dec 23, 2025: SGLang introduces Encode-Prefill-Decode (EPD) Disaggregation with Mooncake as a transfer backend. This integration allows decoupling compute-intensive multimodal encoders (e.g., Vision Transformers) from language model nodes, utilizing Mooncake’s RDMA engine for zero-copy transfer of large multimodal embeddings.

Dec 19, 2025: Mooncake Transfer Engine has been integrated into TensorRT LLM for KVCache transfer in PD-disaggregated inference.

Dec 19, 2025: Mooncake Transfer Engine has been directly integrated into vLLM v1 as a KV Connector in PD-disaggregated setups.

Nov 07, 2025: RBG + SGLang HiCache + Mooncake, a role-based out-of-the-box solution for cloud native deployment, which is elastic, scalable, and high-performance.

Sept 18, 2025: Mooncake Store empowers vLLM Ascend by serving as the distributed KV cache pool backend.

Sept 10, 2025: SGLang officially supports Mooncake Store as a hierarchical KV caching storage backend. The integration extends RadixAttention with multi-tier KV cache storage across device, host, and remote storage layers.

Sept 10, 2025: The official & high-performance version of Mooncake P2P Store is open-sourced as checkpoint-engine. It has been successfully applied in K1.5 and K2 production training, updating Kimi-K2 model (1T parameters) across thousands of GPUs in ~20s.

Aug 23, 2025: xLLM high-performance inference engine builds hybrid KV cache management based on Mooncake, supporting global KV cache management with intelligent offloading and prefetching.

Aug 18, 2025: vLLM-Ascend integrates Mooncake Transfer Engine for KV cache register and disaggregate prefill, enabling efficient distributed inference on Ascend NPUs.

Jul 20, 2025: Mooncake powers the deployment of Kimi K2 on 128 H200 GPUs with PD disaggregation and large-scale expert parallelism, achieving 224k tokens/sec prefill throughput and 288k tokens/sec decode throughput.

Jun 20, 2025: Mooncake becomes a PD disaggregation backend for LMDeploy.

May 9, 2025: NIXL officially supports Mooncake Transfer Engine as a backend plugin.

May 8, 2025: Mooncake x LMCache unite to pioneer KVCache-centric LLM serving system.

May 5, 2025: Supported by Mooncake Team, SGLang release guidance to deploy DeepSeek with PD Disaggregation on 96 H100 GPUs.

Apr 22, 2025: LMCache officially supports Mooncake Store as a remote connector.

Apr 10, 2025: SGLang officially supports Mooncake Transfer Engine for disaggregated prefilling and KV cache transfer.

Mar 7, 2025: We open-sourced the Mooncake Store, a distributed KVCache based on Transfer Engine. vLLM’s xPyD disaggregated prefilling & decoding based on Mooncake Store will be released soon.

Feb 25, 2025: Mooncake receives the Best Paper Award at FAST 2025!

Feb 21, 2025: The updated traces used in our FAST’25 paper have been released.

Dec 16, 2024: vLLM officially supports Mooncake Transfer Engine for disaggregated prefilling and KV cache transfer.

Nov 28, 2024: We open-sourced the Transfer Engine, the central component of Mooncake. We also provide two demonstrations of Transfer Engine: a P2P Store and vLLM integration.

July 9, 2024: We open-sourced the trace as a JSONL file.

June 27, 2024: We present a series of Chinese blogs with more discussions on zhihu 1, 2, 3, 4, 5, 6, 7.

June 26, 2024: Initial technical report release.

Documentation#

Getting Started

Build Guide
PyPI Package

Automatic

Manual

Use Mooncake in Docker Containers

Advanced Compile Options

Quick Start
Installation

Transfer Engine Quick Start

Mooncake Store Quick Start

Supported Communication Protocols
Quick Reference

Commonly Used Protocols (Python API)

Advanced Protocols (C++ Transfer Engine)

Configuration Examples

Choosing the Right Protocol

Troubleshooting

See Also

Mooncake HF3FS Plugin
Prerequisites

Usage

Mooncake x LMCache: Unite to Pioneer KVCache-Centric LLM Serving System
About Mooncake

About LMCache

Collaboration Highlights

Getting Started

Performance Benchmarking and Results

Future Developments

LMDeploy Disaggregated Serving with MooncakeTransferEngine
Overview

Installation

Configuration

Notes

SGLang Disaggregated Serving with MooncakeTransferEngine
Overview

Installation

Configuration

SGLang HiCache with Mooncake Backend
Quick Start: SGLang HiCache with Mooncake Backend

Complete Guide: SGLang HiCache with Mooncake Backend

vLLM Disaggregated Serving
vLLM V1 Disaggregated Serving with Mooncake Store and LMCache

vLLM V0 Disaggregated Serving Demo

vLLM V0 Disaggregated Serving with MooncakeStore

vLLM v1 backend Disaggregated Serving with MooncakeConnector

Performance

PD Disaggregation Performance

Benchmark performance on NVIDIA A10

Benchmark performance on NVIDIA A10

SGLang HiCache with Mooncake Backend Benchmark

vLLM with Mooncake Transfer Engine Benchmark

Allocator Performance

Python API Reference

Mooncake Store Python API

Transfer Engine Python API

Mooncake Store HTTP Service

Mooncake EP & Mooncake Backend

Design Documents

Mooncake Architecture
Architectural Overview

Mooncake Store
Introduction

Architecture

Client C++ API

Mooncake Store Python API

Compilation and Usage

Example Code

Version Management Policy

P2P Store
Overview

P2P Store Sample Program

P2P Store API

Transfer Engine
Overview

Example: Transfer Engine Bench

Transfer Engine C/C++ API

Using Transfer Engine to Your Projects

Advanced Runtime Options

C++ API Reference

EFA Transport (AWS)

Ascend Transport Component

Benchmark and Tuning Guide

TENT: Transfer Engine NEXT
Background

Core Design

Architecture Overview

Typical Use Cases

Summary

TENT C++ API Reference

TENT Metrics System

Mooncake Transfer Engine Benchmark Tool (
tebench
) Guide
1. Build and Deployment

2. Execution Model

3. Quick Start

4. Output Metrics

5. Runtime Configuration

Mooncake x SGLang HiCache System Design
Overall Architecture

HiRadixTree: Metadata Organization in HiCache

Overall Workflow

Local Match

Prefetch from L3

Data Write-back

Multi-Rank Synchronization

Data Transfer Optimization

Integration with PD-Disaggregation Deployment Mode

Troubleshooting

Error Code Explanation

Troubleshooting

Deployment

Mooncake Store Deployment & Operations Guide
Master Startup Flags (with defaults)

Metrics Endpoints

Client/Engine Tuning (Env Vars, with defaults)

Set the Log Level for yalantinglibs coro_rpc and coro_http

Quick Tips

Community

Governance

next

Build Guide

 Contents
 

Documentation

By the Mooncake Team

 
 © Copyright 2026, Mooncake Team.
