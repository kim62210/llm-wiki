---
title: Mooncake | LMCache
source_url: https://docs.lmcache.ai/kv_cache/mooncake.html
final_url: https://docs.lmcache.ai/kv_cache/mooncake.html
status: 200
content_type: text/html; charset=utf-8
topics: [LMCache + Mooncake KV Cache Layer]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.864734+00:00
---

# Mooncake | LMCache

## 원본 URL

https://docs.lmcache.ai/kv_cache/mooncake.html

## 추출 본문

Mooncake | LMCache

 Skip to content
 

LMCache
Toggle navigation menu

⌘
 K
 

LMCache

Getting Started

Installation

Quickstart Examples
Example: Offload KV cache to CPU

Example: Share KV cache across multiple LLMs

Example: Disaggregated prefill

Example: Multimodal KV Cache Support

TroubleShoot

FAQ

KV Cache offloading and sharing

CPU RAM

Local storage

GDS Backend

Redis

InfiniStore

Mooncake

ValKey

Weka

Disaggregated prefill

Using NIXL
1p1d

XpYd

Using shared storage

KV Cache management

LMCache Controller

Lookup the KV cache

Persist the KV cache

Clear the KV cache

Move the KV cache

Compress the KV cache

Check finish of a control event

KV Cache Optimizations

Compression
CacheGen

Blending

Use LMCache in production

Docker deployment

Kubernetes deployment

Developer Guide

Contributing Guide

Dockerfile

Usage Data Module
Usage Stats Collection

API Reference

Configuring LMCache

Adding new storage backends

vLLM Dynamic Connector

KV Caching for Multimodal Models with vLLM

Community

Community meetings

Blogs

LMCache
/
Mooncake

Mooncake#

Overview#

Mooncake is an open-source distributed KV cache storage system designed specifically for LLM inference scenarios.
The system creates a distributed memory pool by aggregating memory space contributed by various client nodes, enabling efficient resource utilization across clusters.

By pooling underutilized DRAM and SSD resources from multiple nodes, the system forms a unified distributed storage service that maximizes resource efficiency.

Key Features#

Distributed memory pooling: Aggregates memory contributions from multiple client nodes into a unified storage pool

High bandwidth utilization: Supports striping and parallel I/O transfer of large objects, fully utilizing multi-NIC aggregated bandwidth

RDMA optimization: Built on Transfer Engine with support for TCP, RDMA (InfiniBand/RoCEv2/eRDMA/NVIDIA GPUDirect)

Dynamic resource scaling: Supports dynamically adding and removing nodes for elastic resource management

For detailed architecture information, see the Mooncake Architecture Guide.

Quick Start#

Install Mooncake via pip:

pipinstallmooncake-transfer-engine

This package includes all necessary components:

mooncake_master
: Master service that manages cluster metadata and coordinates distributed storage operations

mooncake_http_metadata_server
: HTTP-based metadata server used by the underlying transfer engine for connection establishment

Mooncake Python bindings

For production deployments or custom builds, see the Build Instructions.

Setup and Deployment#

Prerequisites:

Machine with at least one GPU for vLLM inference

RDMA-capable network hardware and drivers (recommended) or TCP network

Python 3.8+ with pip

vLLM and LMCache installed

Step 1: Start Infrastructure Services

Start the metadata server:

# HTTP metadata server (recommended for development)mooncake_http_metadata_server

Start the Mooncake master service:

# Master service (use -v=1 for verbose logging)mooncake_master

Expected output:

Master service started on port 50051
HTTP metrics server started on port 9003
Master Metrics: Storage: 0.00 B / 0.00 B | Keys: 0 | ...

Step 2: Create Configuration File

Create your 
mooncake-config.yaml
:

chunk_size:256local_device:"cpu"remote_url:"mooncakestore://127.0.0.1:50051/"remote_serde:"naive"local_cpu:Falsemax_local_cpu_size:5extra_config:local_hostname:"localhost"metadata_server:"http://127.0.0.1:8080/metadata"protocol:"tcp"master_server_address:"localhost:50051"global_segment_size:3355443200local_buffer_size:1073741824transfer_timeout:1

Step 3: Start vLLM with Mooncake

LMCACHE_CONFIG_FILE="mooncake-config.yaml"\LMCACHE_USE_EXPERIMENTAL=True\vllmserve\meta-llama/Llama-3.1-70B-Instruct\--max-model-len65536\--kv-transfer-config\'{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}'

Step 4: Verify the Setup

Test the integration with a sample request:

curl-XPOST"http://localhost:8000/v1/completions"\-H"Content-Type: application/json"\-d'{ "model": "meta-llama/Llama-3.1-70B-Instruct", "prompt": "The future of AI is", "max_tokens": 100, "temperature": 0.7 }'

Debugging Tips:

Enable verbose logging:

mooncake_master-v=1

Check service status:

# Check if services are runningpsaux|grepmooncake
netstat-tlnp|grep-E"(8080|50051)"

Monitor metrics:

Access metrics at 
http://localhost:9003
 when master service is running.

Configuration#

LMCache Parameters:

Parameter

Default

Description

chunk_size

256

Number of tokens per KV chunk

local_device

“cpu”

Local storage device type

remote_url

Required

Mooncake store connection URL (format: 
mooncakestore://host:port/
)

remote_serde

“naive”

Serialization method for remote storage

local_cpu

False

Enable/disable local CPU caching (set to False for pure Mooncake evaluation)

max_local_cpu_size

Required

Maximum local CPU cache size in GB (required even when local_cpu is False)

Mooncake Parameters (via extra_config):

Parameter

Default

Description

local_hostname

Required

Hostname/IP of the local node for Mooncake client identification

metadata_server

Required

Address of metadata coordination server (etcd/Redis/HTTP format)

master_server_address

Required

Mooncake master service address (host:port format)

protocol

“tcp”

Communication protocol (“rdma” for high performance, “tcp” for compatibility)

device_name

“”

RDMA device specification (e.g., “erdma_0,erdma_1” or “mlx5_0,mlx5_1”)

global_segment_size

3355443200

Memory size contributed by each vLLM worker in bytes (~3.1GB)

local_buffer_size

1073741824

Local buffer allocation size in bytes (~1GB)

transfer_timeout

1

Timeout for transfer operations in seconds

Important

Understanding global_segment_size: This parameter defines the amount of memory each vLLM worker contributes to the distributed memory pool.
The total cluster memory available for KV cache storage will be: 
number_of_vllm_workers×global_segment_size
.

Adjust this value based on your available system memory and expected cache requirements.

Additional Resources#

Mooncake Store Architecture

Transfer Engine Documentation

Build Instructions

GitHub Repository

LMCache Integration Guide

 InfiniStore
 

 ValKey
 

On this page

Overview
Key Features

Quick Start
Setup and Deployment

Configuration

Additional Resources

© 2024, The LMCache Team Built with Sphinx 8.2.3
