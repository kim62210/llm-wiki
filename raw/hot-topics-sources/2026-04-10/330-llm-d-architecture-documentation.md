---
title: llm-d Architecture | llm-d
source_url: https://llm-d.ai/docs/architecture
final_url: https://llm-d.ai/docs/architecture
status: 200
content_type: text/html; charset=utf-8
topics: [llm-d & Gateway API Inference Extension]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:08.397783+00:00
---

# llm-d Architecture | llm-d

## 원본 URL

https://llm-d.ai/docs/architecture

## 추출 본문

llm-d Architecture | llm-d

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

llm-d Architecture

On this page

llm-d Architecture

Achieve SOTA Inference Performance On Any Accelerator

llm-d is a high-performance distributed inference serving stack optimized for production deployments on Kubernetes. We help you achieve the fastest "time to state-of-the-art (SOTA) performance" for key OSS large language models across most hardware accelerators and infrastructure providers with well-tested guides and real-world benchmarks.

What does llm-d offer to production inference?​

Model servers like vLLM and SGLang handle efficiently running large language models on accelerators. llm-d provides state of the art orchestration above model servers to serve high-scale real world traffic efficiently and reliably:

Intelligent Inference Scheduling - Deploy vLLM behind a Gateway API-based load balancer enhanced with an inference scheduler to decrease serving latency and increase throughput with prefix-cache aware routing, utilization-based load balancing, fairness and prioritization for multi-tenant serving, and predicted latency balancing (experimental).

Disaggregated Serving (prefill/decode disaggregation) - Reduce time to first token (TTFT) and get more predictable time per output token (TPOT) by splitting inference into prefill servers handling prompts and decode servers handling responses, primarily on large models such as gpt-oss-120b and when processing very long prompts.

Wide Expert-Parallelism - Deploy very large Mixture-of-Experts (MoE) models like DeepSeek-R1 for much higher throughput for RL and latency-insensitive workloads, using Data Parallelism and Expert Parallelism over fast accelerator networks.

Tiered KV Prefix Caching with CPU and Storage Offload - Improve prefix cache hit rate by offloading KV-cache entries to CPU memory, local SSD, and remote high-performance filesystem storage.

Workload Autoscaling - Autoscale multi-model workloads on heterogeneous shared hardware with SLO-aware cost optimization using the Workload Variant Autoscaler or autoscale workloads on homogeneous hardware where each model scales independently using HPA with IGW metrics.

These guides provide tested and benchmarked recipes and Helm charts to start serving quickly with best practices common to production deployments. They are extensible and customizable for particulars of your models and use cases, using standard open source components like Kubernetes, Kubernetes Gateway API, NIXL, and vLLM. Our intent is to eliminate the heavy lifting common in tuning and deploying generative AI inference on modern accelerators.

Get Started Now​

We recommend new users start with a deployment of the inference scheduler and vLLM together through our step-by-step quickstart.

Latest News 🔥​

[2026-02] The v0.5 introduces reproducible benchmark workflows, hierarchical KV offloading, cache-aware LoRA routing, active-active HA, UCCL-based transport resilience, and scale-to-zero autoscaling; validated ~3.1k tok/s per B200 decode GPU (wide-EP) and up to 50k output tok/s on a 16×16 B200 prefill/decode topology with order-of-magnitude TTFT reduction vs round-robin baseline.

[2025-12] The v0.4 release demonstrates 40% reduction in per output token latency for DeepSeek V3.1 on H200 GPUs, Intel XPU and Google TPU disaggregation support for lower time to first token, a new well-lit path for prefix cache offload to vLLM-native CPU memory tiering, and a preview of the workload variant autoscaler improving model-as-a-service efficiency.

🧱 Architecture​

llm-d accelerates distributed inference by integrating industry-standard open technologies: vLLM as default model server and engine, Kubernetes Inference Gateway as control plane API and load balancing orchestrator, and Kubernetes as infrastructure orchestrator and workload control plane.

llm-d adds:​

Model Server Optimizations in vLLM: The llm-d team contributes and maintains high performance distributed serving optimizations in upstream vLLM, including disaggregated serving, KV connector interfaces, support for frontier OSS mixture of experts models, and production-ready observability and resiliency.

Inference Scheduler: llm-d uses compatible Gateway implementations and their extensible balancing policies to make customizable “smart” load-balancing decisions specifically for LLMs without reimplementing a full-featured load balancer. Leveraging operational telemetry, the Inference Scheduler implements the filtering and scoring algorithms to make decisions with P/D-awareness, KV-cache-awareness, SLA-awareness, and load-awareness. Advanced users can implement their own scorers to further customize the algorithm while benefiting from IGW features like flow control and latency-aware balancing. The control plane for the load balancer is the Kubernetes API but can also be run standalone.

Disaggregated Serving Sidecar: llm-d orchestrates prefill and decode phases onto independent instances - the scheduler decides which instances should receive a given request, and the transaction is coordinated via a sidecar alongside decode instances. The sidecar instructs vLLM to provide point to point KV cache transfer over fast interconnects (IB/RoCE RDMA, TPU ICI, and DCN) via NIXL.

vLLM Native CPU Offloading and llm-d filesystem backend: llm-d uses vLLM's KVConnector abstraction to configure a pluggable KV cache hierarchy, including offloading KVs to host, remote storage, and systems like LMCache, Mooncake, and KVBM.

Variant Autoscaling over Hardware, Workload, and Traffic: A traffic- and hardware-aware autoscaler that (a) measures the capacity of each model server instance, (b) derive a load function that takes into account different request shapes and QoS, and (c) assesses recent traffic mix (QPS, QoS, and shapes) to calculate the optimal mix of instances to handle prefill, decode, and latency-tolerant requests, enabling use of HPA for SLO-level efficiency.

For more details of architecture see the project proposal.

What is in scope for llm-d​

llm-d currently targets improving the production serving experience around:

Online serving and online batch of Generative models running in PyTorch or JAX
Large language models (LLMs) with 1 billion or more parameters

Using most or all of the capacity of one or more hardware accelerators

Running in throughput, latency, or multiple-objective configurations

On recent generation datacenter-class accelerators - NVIDIA A100+, AMD MI250, Google TPU v5e or newer, and Intel GPU Max seriers or newer

On Kubernetes 1.29+, integrated via code into Ray, or as a standalone service

See the accelerator docs for points of contact for more details about the accelerators, networks, and configurations tested and our roadmap for what is coming next.

🔍 Observability​

Monitoring & Metrics - Prometheus, Grafana dashboards, and PromQL queries

Distributed Tracing - OpenTelemetry tracing across vLLM, routing proxy, and EPP

📦 Releases​

Our guides are living docs and kept current. For details about the Helm charts and component releases, visit our GitHub Releases page to review release notes.

Check out our roadmap for upcoming releases.

Contribute​

See our project overview for more details on our development process and governance.

Review our contributing guidelines for detailed information on how to contribute to the project.

Join one of our Special Interest Groups (SIGs) to contribute to specific areas of the project and collaborate with domain experts.

We use Slack to discuss development across organizations. Please join: Slack

We host a bi-weekly standup for contributors every other Wednesday at 12:30 PM ET, as well as meetings for various SIGs. You can find them in the shared llm-d calendar

We use Google Groups to share architecture diagrams and other content. Please join: Google Group

License​

This project is licensed under Apache License 2.0. See the LICENSE file for details.

Content Source

This content is automatically synced from README.md on the 
main
 branch of the llm-d/llm-d repository.

📝 To suggest changes, please edit the source file or create an issue.

Next

Latest Release

What does llm-d offer to production inference?

Get Started Now
Latest News 🔥

🧱 Architecture
llm-d adds:

What is in scope for llm-d

🔍 Observability

📦 Releases

Contribute

License

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
