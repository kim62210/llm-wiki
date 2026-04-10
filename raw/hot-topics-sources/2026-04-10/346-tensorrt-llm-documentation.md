---
title: Welcome to TensorRT LLM’s Documentation! — TensorRT LLM
source_url: https://nvidia.github.io/TensorRT-LLM
final_url: https://nvidia.github.io/TensorRT-LLM/
status: 200
content_type: text/html; charset=utf-8
topics: [TensorRT-LLM 1.3 with Day-0 Model Support]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:10.866799+00:00
---

# Welcome to TensorRT LLM’s Documentation! — TensorRT LLM

## 원본 URL

https://nvidia.github.io/TensorRT-LLM

## 추출 본문

Welcome to TensorRT LLM’s Documentation! — TensorRT LLM
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

Welcome to TensorRT LLM’s Documentation!#

Getting Started

Overview
About TensorRT LLM

Key Capabilities

What Can You Do With TensorRT LLM?

Quick Start Guide
Launch Docker Container

Deploy Online Serving with trtllm-serve

Run Offline Inference with LLM API

Run Offline Inference with VisualGen API

Next Steps

Installation

Supported Hardware

Deployment Guide

LLM Examples
Basics

Customization

Slurm

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
Preconfigured Recipes

Model-Specific Deployment Guides

CPU Affinity configuration in TensorRT LLM
NUMA-aware affinity in TensorRT LLM

Other environmental considerations

CPU affinity configuration examples

Models

Supported Models
Model-Feature Support Matrix (Key Models)

Multimodal Feature Support Matrix (PyTorch Backend)

Visual Generation Models
Supported Models

Feature Matrix

Visual Generation (Beta)
Background

Supported Models

Quick Start

Optimizations

Developer Guide

Adding a New Model
Table of Contents

Introduction

Prerequisites

Step-by-Step Guide

CLI Reference

trtllm-bench
Syntax

Dataset preparation

trtllm-eval
About

Usage and Examples

Syntax

trtllm-serve
trtllm-serve

Run benchmarking with 
trtllm-serve

API Reference

LLM API Introduction
Quick Start Example

Model Input

Tips and Troubleshooting

API Reference

LLM

AsyncLLM

MultimodalEncoder

CompletionOutput

RequestOutput

GuidedDecodingParams

SamplingParams

DisaggregatedParams

DisaggScheduleStyle

KvCacheConfig

KvCacheRetentionConfig

CudaGraphConfig

MoeConfig

LookaheadDecodingConfig

MedusaDecodingConfig

EagleDecodingConfig

Eagle3DecodingConfig

MTPDecodingConfig

SchedulerConfig

CapacitySchedulerPolicy

BuildConfig

QuantConfig

QuantAlgo

CalibConfig

BuildCacheConfig

RequestError

MpiCommSession

ExtendedRuntimePerfKnobConfig

BatchingType

ContextChunkingPolicy

DynamicBatchConfig

CacheTransceiverConfig

NGramDecodingConfig

PARDDecodingConfig

SADecodingConfig

SAEnhancerConfig

UserProvidedDecodingConfig

TorchCompileConfig

DraftTargetDecodingConfig

LlmArgs

TorchLlmArgs

TrtLlmArgs

AutoDecodingConfig

AttentionDpConfig

LoRARequest

SaveHiddenStatesDecodingConfig

RocketSparseAttentionConfig

DeepSeekSparseAttentionConfig

SkipSoftmaxAttentionConfig

Features

Feature Combination Matrix

Multi-Head, Multi-Query, and Group-Query Attention
Attention Backends

Implement a New Attention Backend

The Features of the 
TrtllmAttention
 Backend

Disaggregated Serving
Motivation

KV Cache Exchange

Usage

Environment Variables

Troubleshooting and FAQ

KV Cache System
The Basics

Reuse Across Requests

Limited Attention Window Size

MQA / GQA

Controlling KV Cache Behavior

Long Sequences
Chunked Context

Chunked attention

Sliding Window Attention

LoRA (Low-Rank Adaptation)
Table of Contents

Background

Basic Usage

Advanced Usage

TRTLLM serve with LoRA

TRTLLM bench with LoRA

Multimodal Support in TensorRT LLM
Background

Optimizations

Model Support Matrix

Examples

Overlap Scheduler
How It Works

Tradeoff

Usage

References

Paged Attention, IFB, and Request Scheduling
In-flight Batching

Chunked Context (a.k.a Chunked Prefill)

KV Cache

The schedulers

Revisiting Paged Context Attention and Context Chunking

Parallelism in TensorRT LLM
Overview of Parallelism Strategies

Module-level Parallelism Guide

Wide Expert Parallelism (Wide-EP)

Quantization
Quantization in TensorRT LLM

Usage

Model Support Matrix

Hardware Support Matrix

Quick Links

Sampling
General usage

Beam search

Logits processor

Additional Outputs
Options

Guided Decoding
Online API: 
trtllm-serve

Offline API: LLM API

Speculative Decoding
Quick Start

Suffix Automaton (SA) Enhancement

Usage with 
trtllm-bench
 and 
trtllm-serve

Checkpoint Loading
Table of Contents

Overview

Core Components

Built-in Checkpoint Formats

Using Checkpoint Loaders

Creating Custom Checkpoint Loaders

AutoDeploy (Beta)
Seamless Model Deployment from PyTorch to TensorRT LLM

Key Features

Get Started

Support Matrix

Advanced Usage

Roadmap

Ray Orchestrator (Prototype)
Motivation

Basic Usage

Features

Roadmap

Architecture

Torch Compile & Piecewise CUDA Graph
Table of Contents

Usage

Tips for Piecewise CUDA Graph

Known Issue

Development Guide

Helix Parallelism
How Helix Works

When to Use Helix

Supported Models

Configuration

Testing Helix with TensorRT-LLM

KV Cache Connector
Use Cases

Architecture

Example Implementation

Sparse Attention
Background and Motivation

Algorithm Overview

Quick Start

Sparse Attention Implementation

Developer Guide

Architecture Overview
Runtime Optimizations

Visual Generation

Performance Analysis
Feature Descriptions

Coordinating with NVIDIA Nsight Systems Launch

Coordinating with PyTorch profiler (PyTorch workflow only)

Examples

MoE Expert Load Balance Analysis (Perfect Router)

TensorRT LLM Benchmarking
Table of Contents

Before Benchmarking

Throughput Benchmarking

Online Serving Benchmarking

Continuous Integration Overview
Table of Contents

CI pipelines

Test definitions

Unit tests

Jenkins stage names

Finding the stage for a test

Waiving tests

Triggering CI Best Practices

Using Dev Containers
Container image selection

Volume Mounts

Overriding Docker Compose configuration

LLM API Change Guide
Overview

API Types and Stability Guarantees

API Schema Management

API Change Principles

Modifying LLM Constructor Arguments

Modifying LLM Class Methods

Common Workflows

Introduction to KV Cache Transmission
Table of Contents

Workflow

Key Components

Customization

Evolution Outlook

Blogs

DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72
Table of Contents

Motivation

DWDP Overview

DWDP Implementation

Key Optimizations

Evaluation

Summary

Future Work

Acknowledgment

Optimizing MoE Communication with One-Sided AlltoAll Over NVLink
Table of Contents

Background

Design Overview

Implementation Details

Performance Benchmark

Future Work And Conclusion

Sparse Attention in TensorRT LLM
Introduction and Motivation

Overview of Sparse Attention in TensorRT LLM

Sparse Attention Framework Design

Algorithm Implementations

Evaluation

Summary and Future Work

Accelerating Long-Context Inference with Skip Softmax Attention
Table of Contents

Method Overview

Example Usage

Accuracy Evaluation

Performance Benchmark

Reproduction

Conclusion

Optimizing DeepSeek-V3.2 on NVIDIA Blackwell GPUs
Table of Contents

Introduction

DeepSeek Sparse Attention (DSA)

Precision Strategy

Parallel Strategy

Key Features

Key Optimizations

How to Reproduce

Future Works

Acknowledgement

Scaling Expert Parallelism in TensorRT LLM (Part 3: Pushing the Performance Boundary)
Table of Contents

Overview

Lower precision

Rethink network structure

More kernel overlap, fusion and optimization

End-to-End Performance

Acknowledgements

Inference Time Compute Implementation in TensorRT LLM
Table of Contents

Background and Motivation

Introduction for Scaffolding: A Framework for inference-time compute

An Example: Implement Dynasor-CoT on Scaffolding

Feature List on Scaffolding

Future Work

Combining Guided Decoding and Speculative Decoding: Making CPU and GPU Cooperate Seamlessly
Table of Contents

Background and Challenges

Trace Grammar State for Draft Token Proposal and Rejection

Make Grammar Computation Capturable by CUDA Graph

Performance and Analysis

Acknowledgements

Running GPT-OSS-120B with Eagle3 Speculative Decoding on GB200/B200 (TensorRT LLM)
Prerequisites

Get the TensorRT LLM Container

Start the TensorRT LLM Container

Download the models (Base + Eagle3)

Create the Eagle3 Configuration

Launch the Server (Eagle3 Speculative Decoding)

Quick Health Check

Sample Chat Completions Request

ADP Balance Strategy
Table of Contents

Motivation and Background

Theoretical Analysis and Modeling

Experiments

Conclusion

Acknowledgement

Running a High Performance GPT-OSS-120B Inference Server with TensorRT LLM
Prerequisites

Launching the TensorRT LLM docker container

Running the TensorRT LLM Server

Launch the TensorRT-LLM Server

(H200 Only) Using OpenAI Triton Kernels for MoE

Test the Server with a Sample Request

(H200/H100 Only) Using OpenAI Triton Kernels for MoE

Troubleshooting Tips

Scaling Expert Parallelism in TensorRT LLM (Part 2: Performance Status and Optimization)
Table of Contents

Optimization Highlights

End-to-End Performance

Future Work

Acknowledgements

N-Gram Speculative Decoding in TensorRT LLM
Highlights

Table of Contents

Background & Motivation

Algorithm & Complexity

Performance Study

Auto‑Enablement with Heuristic

How to launch Llama4 Maverick + Eagle3 TensorRT LLM server
Prerequisites

Download Artifacts

Launching the server

Troubleshooting Tips

Performance Tuning

Disaggregated Serving in TensorRT LLM
Motivation

Disaggregated Serving in TensorRT LLM

KV Cache Exchange

Performance Studies

Future Work

Acknowledgement

Scaling Expert Parallelism in TensorRT LLM (Part 1: Design and Implementation of Large-scale EP)
Table of Contents

Motivation for large-scale EP

High-level design introduction

EP communication kernels

EP Load Balancer

E2E evaluation

Reproducing steps

Expanded thoughts

Acknowledgement

Optimizing DeepSeek R1 Throughput on NVIDIA Blackwell GPUs: A Deep Dive for Developers
Table of Contents

Introduction

Precision strategy

Parallel strategy

MLA Layers Optimizations

MoE Layers Optimizations

Runtime Optimizations

How to reproduce

Future Works

Acknowledgment

DeepSeek R1 MTP Implementation and Optimization
Table of Contents

MTP for inference

MTP implementation in TensorRT LLM

MTP optimization - Relaxed Acceptance

Evaluation

Future Works

Acknowledgment

Pushing Latency Boundaries: Optimizing DeepSeek-R1 Performance on NVIDIA B200 GPUs
Table of Contents

Background

Implementation Configuration

Key Optimizations

How to reproduce

Future Works

Acknowledgment

How to get best performance on DeepSeek-R1 in TensorRT LLM
Table of Contents

Prerequisites: Install TensorRT LLM and download models

Reproducing steps

Exploring more ISL/OSL combinations

H200 achieves nearly 12,000 tokens/sec on Llama2-13B with TensorRT LLM
H200 vs H100

Latest HBM Memory

New XQA-kernel provides 2.4x more Llama-70B throughput within the same latency budget
Llama-70B on H200 up to 2.4x increased throughput with XQA within same latency budget

H100 has 4.6x A100 Performance in TensorRT LLM, achieving 10,000 tok/s at 100ms to first token
MLPerf on H100 with FP8

What is H100 FP8?

Falcon-180B on a single H200 GPU with INT4 AWQ, and 6.7x faster Llama-70B over A100
Falcon-180B on a single H200 with INT4 AWQ

Llama-70B on H200 up to 6.7x A100

Speed up inference with SOTA quantization techniques in TRT-LLM
Quantization in TensorRT-LLM

Benchmark

Best practices to choose the right quantization methods

What’s coming next

Quick Links

Releases

Github Code

Roadmap

Indices and tables#

Index

Module Index

Search Page

next

Overview

 On this page
 

Welcome to TensorRT LLM’s Documentation!

Indices and tables

Privacy Policy
 | 
 
 
 
 Your Privacy Choices
 | 
 
 
 
 Terms of Service
 | 
 
 
 
 Accessibility
 | 
 
 
 
 Corporate Policies
 | 
 
 
 
 Product Security
 | 
 
 
 
 Contact

 
 Copyright © 2025, NVidia.
 

Last updated on April 08, 2026.

This page is generated by TensorRT-LLM commit 4e69c14.
