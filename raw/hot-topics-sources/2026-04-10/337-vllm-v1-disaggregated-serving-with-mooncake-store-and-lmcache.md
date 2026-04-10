---
title: vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake
source_url: https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html
final_url: https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html
status: 200
content_type: text/html; charset=utf-8
topics: [LMCache + Mooncake KV Cache Layer]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.679167+00:00
---

# vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake

## 원본 URL

https://kvcache-ai.github.io/Mooncake/getting_started/examples/vllm-integration/vllmv1-lmcache-integration.html

## 추출 본문

vLLM V1 Disaggregated Serving with Mooncake Store and LMCache — Mooncake
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

vLLM V1 Disaggregated Serving with Mooncake Store and LMCache

 Contents 

Overview

Deployment

Additional Resources

vLLM V1 Disaggregated Serving with Mooncake Store and LMCache#

Overview#

The vLLM v1 version has been released with support for PD disaggregation. The detailed design document can be found here. LMCache immediately implemented the corresponding connector to support storage, transmission, and loading of KVCache, enabling collaborative operation with PD nodes. Mooncake, as LMCache’s backend storage engine, has undergone extensive optimizations in usability, performance, and stability. This document explains how to deploy a PD disaggregated serving demo using LMCache + Mooncake.

Deployment#

First, you need to prepare two GPU-equipped machines, which we will refer to as Machine A and Machine B. Install vLLM, Mooncake and LMCache on both Machine A and Machine B. For specific installation instructions, please refer to the official documentation of each repository.

Start the Mooncake Master node on Machine A:

mooncake_master-port50052-max_threads64-metrics_port9004\--enable_http_metadata_server=true\--http_metadata_server_host=0.0.0.0\--http_metadata_server_port=8080

Launch the Decoder instance on machine A

Modify the vllm/examples/others/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh file.

diff --git a/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh b/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.shindex 831ef0bb5..a2ff0744c 100644--- a/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh+++ b/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.shelif [[ $1 == "decoder" ]]; then
 # Decoder listens on port 8200
- decode_config_file=$SCRIPT_DIR/configs/lmcache-decoder-config.yaml+ decode_config_file=$SCRIPT_DIR/configs/mooncake-decoder-config.yaml UCX_TLS=cuda_ipc,cuda_copy,tcp \
 LMCACHE_CONFIG_FILE=$decode_config_file \
 LMCACHE_USE_EXPERIMENTAL=True \
 VLLM_ENABLE_V1_MULTIPROCESSING=1 \
 VLLM_WORKER_MULTIPROC_METHOD=spawn \
 CUDA_VISIBLE_DEVICES=1 \

Add the 
mooncake-decoder-config.yaml
 file

chunk_size:256remote_url:"mooncakestore://{IPofMachineA}:50052/"remote_serde:"naive"local_cpu:Falsemax_local_cpu_size:100extra_config:local_hostname:"{IPofMachineA}"metadata_server:"http://{IPofMachineA}:8080/metadata"protocol:"rdma"device_name:"mlx5_0"# Multiple RDMA devices can be specified as comma-separated listmaster_server_address:"{IPofMachineA}:50052"global_segment_size:32212254720# 30GBlocal_buffer_size:1073741824# 1GBtransfer_timeout:1save_chunk_meta:False

Launch the Decoder instance using command

bashdisagg_vllm_launcher.shdecoderQwen/Qwen2.5-7B-Instruct-GPTQ-Int4

Launch the Prefiller instance on machine B

Modify the vllm/examples/others/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh file.

diff --git a/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh b/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.shindex 831ef0bb5..9e5a3f044 100644--- a/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh+++ b/examples/lmcache/disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh@@ -18,12 +18,14 @@ fiif [[ $1 == "prefiller" ]]; then
 # Prefiller listens on port 8100
- prefill_config_file=$SCRIPT_DIR/configs/lmcache-prefiller-config.yaml+ prefill_config_file=$SCRIPT_DIR/configs/mooncake-prefiller-config.yaml

Add the 
mooncake-prefiller-config.yaml
 file

chunk_size:256remote_url:"mooncakestore://{IPofMachineA}:50052/"remote_serde:"naive"local_cpu:Falsemax_local_cpu_size:100extra_config:local_hostname:"{IPofMachineB}"metadata_server:"http://{IPofMachineA}:8080/metadata"protocol:"rdma"device_name:"mlx5_0"# Multiple RDMA devices can be specified as comma-separated listmaster_server_address:"{IPofMachineA}:50052"global_segment_size:32212254720# 30GBlocal_buffer_size:1073741824# 1GBtransfer_timeout:1save_chunk_meta:False

Launch the Prefiller instance using command

bashdisagg_vllm_launcher.shprefillerQwen/Qwen2.5-7B-Instruct-GPTQ-Int4

Prepare the router 
disagg_proxy_server

We use the disagg_proxy_server provided by LMCache. According to LMCache/LMCache#1342, when using Mooncake Store as the backend, you need to comment out 
wait_decode_kv_ready(req_id)
 in the proxy code.

Launch the 
disagg_proxy_server
 using command

python3disagg_proxy_server.py--hostlocalhost--port9000--prefiller-hostIP_of_Machine_B--prefiller-port8100--decoder-hostIP_of_Machine_A--decoder-port8200

Now we can send the requests to the 
disagg_proxy_server
 to test PD disaggregated serving.

Additional Resources#

Mooncake x LMCache: Unite to Pioneer KVCache-Centric LLM Serving System

Using Mooncake in LMCache

Using LMCache in vLLM

previous

vLLM Disaggregated Serving

next

vLLM V0 Disaggregated Serving Demo

 Contents
 

Overview

Deployment

Additional Resources

By the Mooncake Team

 
 © Copyright 2026, Mooncake Team.
