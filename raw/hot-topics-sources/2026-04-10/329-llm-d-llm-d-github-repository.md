---
title: GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub
source_url: https://github.com/llm-d/llm-d
final_url: https://github.com/llm-d/llm-d
status: 200
content_type: text/html; charset=utf-8
topics: [llm-d & Gateway API Inference Extension]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:08.960293+00:00
---

# GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub

## 원본 URL

https://github.com/llm-d/llm-d

## 추출 본문

GitHub - llm-d/llm-d: Achieve state of the art inference performance with modern accelerators on Kubernetes · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 llm-d
/llm-dPublic

Notifications
You must be signed in to change notification settings

Fork
 397

 Star
3k

Code

Issues167

Pull requests58

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

llm-d/llm-d

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
622 Commits

622 Commits

.github

.github

docker

docker

docs

docs

guides

guides

helpers

helpers

hooks

hooks

patches

patches

scripts

scripts

.dockerignore

.dockerignore

.gitattributes

.gitattributes

.gitignore

.gitignore

.hadolint.yaml

.hadolint.yaml

.markdownlint.json

.markdownlint.json

.pre-commit-config.yaml

.pre-commit-config.yaml

.prowlabels.yaml

.prowlabels.yaml

ADOPTERS.md

ADOPTERS.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

DCO

DCO

LICENSE

LICENSE

MAINTAINERS.md

MAINTAINERS.md

Makefile

Makefile

ONBOARDING.md

ONBOARDING.md

OWNERS

OWNERS

PROJECT.md

PROJECT.md

PR_SIGNOFF.md

PR_SIGNOFF.md

README.md

README.md

RELEASE.md

RELEASE.md

SECURITY-INSIGHTS.md

SECURITY-INSIGHTS.md

SECURITY.md

SECURITY.md

SECURITY_CONTACTS.md

SECURITY_CONTACTS.md

SIGS.md

SIGS.md

THREAT-MODEL.md

THREAT-MODEL.md

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

Achieve SOTA Inference Performance On Any Accelerator

llm-d is a high-performance distributed inference serving stack optimized for production deployments on Kubernetes. We help you achieve the fastest "time to state-of-the-art (SOTA) performance" for key OSS large language models across most hardware accelerators and infrastructure providers with well-tested guides and real-world benchmarks.

What does llm-d offer to production inference?

Model servers like vLLM and SGLang handle efficiently running large language models on accelerators. llm-d provides state of the art orchestration above model servers to serve high-scale real world traffic efficiently and reliably:

Intelligent Inference Scheduling - Deploy vLLM behind a Gateway API-based load balancer enhanced with an inference scheduler to decrease serving latency and increase throughput with prefix-cache aware routing, utilization-based load balancing, fairness and prioritization for multi-tenant serving, and predicted latency balancing (experimental).

Disaggregated Serving (prefill/decode disaggregation) - Reduce time to first token (TTFT) and get more predictable time per output token (TPOT) by splitting inference into prefill servers handling prompts and decode servers handling responses, primarily on large models such as gpt-oss-120b and when processing very long prompts.

Wide Expert-Parallelism - Deploy very large Mixture-of-Experts (MoE) models like DeepSeek-R1 for much higher throughput for RL and latency-insensitive workloads, using Data Parallelism and Expert Parallelism over fast accelerator networks.

Tiered KV Prefix Caching with CPU and Storage Offload - Improve prefix cache hit rate by offloading KV-cache entries to CPU memory, local SSD, and remote high-performance filesystem storage.

Workload Autoscaling - Autoscale multi-model workloads on heterogeneous shared hardware with SLO-aware cost optimization using the Workload Variant Autoscaler or autoscale workloads on homogeneous hardware where each model scales independently using HPA with IGW metrics.

These guides provide tested and benchmarked recipes and Helm charts to start serving quickly with best practices common to production deployments. They are extensible and customizable for particulars of your models and use cases, using standard open source components like Kubernetes, Kubernetes Gateway API, NIXL, and vLLM. Our intent is to eliminate the heavy lifting common in tuning and deploying generative AI inference on modern accelerators.

Get Started Now

We recommend new users start with a deployment of the inference scheduler and vLLM together through our step-by-step quickstart.

Latest News 🔥

[2026-02] The v0.5 introduces reproducible benchmark workflows, hierarchical KV offloading, cache-aware LoRA routing, active-active HA, UCCL-based transport resilience, and scale-to-zero autoscaling; validated ~3.1k tok/s per B200 decode GPU (wide-EP) and up to 50k output tok/s on a 16×16 B200 prefill/decode topology with order-of-magnitude TTFT reduction vs round-robin baseline.

[2025-12] The v0.4 release demonstrates 40% reduction in per output token latency for DeepSeek V3.1 on H200 GPUs, Intel XPU and Google TPU disaggregation support for lower time to first token, a new well-lit path for prefix cache offload to vLLM-native CPU memory tiering, and a preview of the workload variant autoscaler improving model-as-a-service efficiency.

🧱 Architecture

llm-d accelerates distributed inference by integrating industry-standard open technologies: vLLM as default model server and engine, Kubernetes Inference Gateway as control plane API and load balancing orchestrator, and Kubernetes as infrastructure orchestrator and workload control plane.

llm-d adds:

Model Server Optimizations in vLLM: The llm-d team contributes and maintains high performance distributed serving optimizations in upstream vLLM, including disaggregated serving, KV connector interfaces, support for frontier OSS mixture of experts models, and production-ready observability and resiliency.

Inference Scheduler: llm-d uses compatible Gateway implementations and their extensible balancing policies to make customizable “smart” load-balancing decisions specifically for LLMs without reimplementing a full-featured load balancer. Leveraging operational telemetry, the Inference Scheduler implements the filtering and scoring algorithms to make decisions with P/D-awareness, KV-cache-awareness, SLA-awareness, and load-awareness. Advanced users can implement their own scorers to further customize the algorithm while benefiting from IGW features like flow control and latency-aware balancing. The control plane for the load balancer is the Kubernetes API but can also be run standalone.

Disaggregated Serving Sidecar: llm-d orchestrates prefill and decode phases onto independent instances - the scheduler decides which instances should receive a given request, and the transaction is coordinated via a sidecar alongside decode instances. The sidecar instructs vLLM to provide point to point KV cache transfer over fast interconnects (IB/RoCE RDMA, TPU ICI, and DCN) via NIXL.

vLLM Native CPU Offloading and llm-d filesystem backend: llm-d uses vLLM's KVConnector abstraction to configure a pluggable KV cache hierarchy, including offloading KVs to host, remote storage, and systems like LMCache, Mooncake, and KVBM.

Variant Autoscaling over Hardware, Workload, and Traffic: A traffic- and hardware-aware autoscaler that (a) measures the capacity of each model server instance, (b) derive a load function that takes into account different request shapes and QoS, and (c) assesses recent traffic mix (QPS, QoS, and shapes) to calculate the optimal mix of instances to handle prefill, decode, and latency-tolerant requests, enabling use of HPA for SLO-level efficiency.

For more details of architecture see the project proposal.

What is in scope for llm-d

llm-d currently targets improving the production serving experience around:

Online serving and online batch of Generative models running in PyTorch or JAX

Large language models (LLMs) with 1 billion or more parameters

Using most or all of the capacity of one or more hardware accelerators

Running in throughput, latency, or multiple-objective configurations

On recent generation datacenter-class accelerators - NVIDIA A100+, AMD MI250, Google TPU v5e or newer, and Intel GPU Max seriers or newer

On Kubernetes 1.29+, integrated via code into Ray, or as a standalone service

See the accelerator docs for points of contact for more details about the accelerators, networks, and configurations tested and our roadmap for what is coming next.

🔍 Observability

Monitoring & Metrics - Prometheus, Grafana dashboards, and PromQL queries

Distributed Tracing - OpenTelemetry tracing across vLLM, routing proxy, and EPP

📦 Releases

Our guides are living docs and kept current. For details about the Helm charts and component releases, visit our GitHub Releases page to review release notes.

Check out our roadmap for upcoming releases.

Contribute

See our project overview for more details on our development process and governance.

Review our contributing guidelines for detailed information on how to contribute to the project.

Join one of our Special Interest Groups (SIGs) to contribute to specific areas of the project and collaborate with domain experts.

We use Slack to discuss development across organizations. Please join: Slack

We host a bi-weekly standup for contributors every other Wednesday at 12:30 PM ET, as well as meetings for various SIGs. You can find them in the shared llm-d calendar

We use Google Groups to share architecture diagrams and other content. Please join: Google Group

License

This project is licensed under Apache License 2.0. See the LICENSE file for details.

About

 Achieve state of the art inference performance with modern accelerators on Kubernetes
 

www.llm-d.ai

Resources

 Readme

License

 Apache-2.0 license
 

Code of conduct

 Code of conduct
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

3k
 stars

Watchers

61
 watching

Forks

397
 forks

 Report repository

Releases
 7

Release v0.6.0
 Latest

Apr 3, 2026

+ 6 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Shell57.9%

Go Template15.6%

Python13.9%

Makefile11.1%

Dockerfile1.5%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.
