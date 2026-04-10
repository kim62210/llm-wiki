---
title: KV Cache | llm-d
source_url: https://llm-d.ai/docs/architecture/Components/kv-cache
final_url: https://llm-d.ai/docs/architecture/Components/kv-cache
status: 200
content_type: text/html; charset=utf-8
topics: [LMCache-Based Distributed KV Cache Offloading]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:38.344460+00:00
---

# KV Cache | llm-d

## 원본 URL

https://llm-d.ai/docs/architecture/Components/kv-cache

## 추출 본문

KV Cache | llm-d

Skip to main content

🎉 llm-d 0.5 is now released! Check out hierarchical KV offloading, cache-aware LoRA routing, resilient networking with UCCL, and scale-to-zero autoscaling. Read the announcement →

ArchitectureGuidesUsageCommunityBlogVideos

Join Slack

llm-d Architecture

Latest Release

Components

Inference Scheduler

Model Service

Inference Simulator

Infrastructure

KV Cache

Benchmark Tools

Workload Variant Autoscaler

Components

KV Cache

On this page

KV-Cache

Introduction​

Efficiently caching Key & Value (KV) tensors is crucial for optimizing LLM inference.
Reusing the KV-Cache, rather than recomputing it, significantly improves both Time To First Token (TTFT) and overall throughput, while also maximizing system resource-utilization.
As a distributed LLM inference platform, 
llm-d
 provides a comprehensive suite of KV-Cache management capabilities to achieve these goals.

This repository contains the 
llm-d-kv-cache
, a pluggable service designed to enable KV-Cache Aware Routing and lay the foundation for advanced, cross-node cache coordination in vLLM-based serving platforms.

Project Northstar​

See the Project Northstar document for a detailed overview of the project's goals and vision.

KV-Cache Indexer Overview​

The major component of this project is the KV-Cache Indexer is a high-performance library that keeps a global, near-real-time view of KV-Cache block locality across a fleet of vLLM pods.

It is powered by 
KVEvents
 streamed from vLLM, which provide structured metadata as KV-blocks are created or evicted from a vLLM instance's KV-cache.
This allows the indexer to track which blocks reside on which nodes and on which tier (e.g., GPU or CPU).
This metadata is the foundation for intelligent routing, enabling schedulers to make optimal, KV-cache-aware placement decisions.

The diagram below shows the primary data flows: the Read Path (scoring) and the Write Path (event ingestion).

Read Path:

1: Scoring Request: A scheduler asks the KVCache Indexer to score a set of pods for a given prompt

2: Index Query: The indexer calculates the necessary KV-block keys from the prompt and queries the KV-Block Index to see which pods have those blocks

3: Return Scores: The indexer returns a map of pods and their corresponding KV-cache-hit scores to the scheduler

Write Path:

A: Event Ingestion: As vLLM pods create or evict KV-blocks, they emit 
KVEvents
 containing metadata about these changes

B: Index Update: The Event Subscriber consumes these events and updates the KV-Block Index in near-real-time

For a more detailed breakdown, please see the high-level Architecture and the Configuration docs.

Examples​

KVCache Indexer:
A reference implementation showing how to run and use the 
kvcache.Indexer
 module

KVCache Aware Scorer:
A reference implementation of how to integrate the 
kvcache.Indexer
 into a scheduler like the 
llm-d-inference-scheduler

KV-Events:
Demonstrates how the KV-Cache libraries handles KV-Events through both an offline example with a dummy ZMQ publisher and an online example using a vLLM Helm chart.

Content Source

This content is automatically synced from README.md on the 
main
 branch of the llm-d/llm-d-kv-cache repository.

📝 To suggest changes, please edit the source file or create an issue.

Previous

Infrastructure

Next

Benchmark Tools

Introduction

Project Northstar

KV-Cache Indexer Overview
Examples

Architecture

Overview

Latest Release

Inference Scheduler

KV Cache

Model Service

Benchmark Tools

Guides

Getting Started

Prerequisites

Inference Scheduling

Prefill/Decode Disaggregation

Wide Expert Parallelism

Community

Contact us

Contributing

Code of Conduct

More

Blog

Privacy Policy

Social

Join our Slack
