---
title: GitHub - ai-dynamo/dynamo: A Datacenter Scale Distributed Inference Serving Framework · GitHub
source_url: https://github.com/ai-dynamo/dynamo
final_url: https://github.com/ai-dynamo/dynamo
status: 200
content_type: text/html; charset=utf-8
topics: [NVIDIA Dynamo 1.0 Inference OS]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:05.247176+00:00
---

# GitHub - ai-dynamo/dynamo: A Datacenter Scale Distributed Inference Serving Framework · GitHub

## 원본 URL

https://github.com/ai-dynamo/dynamo

## 추출 본문

GitHub - ai-dynamo/dynamo: A Datacenter Scale Distributed Inference Serving Framework · GitHub

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

 ai-dynamo
/dynamoPublic

Notifications
You must be signed in to change notification settings

Fork
 1k

 Star
6.5k

Code

Issues201

Pull requests374

Discussions

Actions

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Security and quality

 Insights

ai-dynamo/dynamo

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
4,288 Commits

4,288 Commits

.ai

.ai

.cargo

.cargo

.claude/skills

.claude/skills

.devcontainer

.devcontainer

.github

.github

benchmarks

benchmarks

components

components

container

container

deploy

deploy

docs

docs

examples

examples

fern

fern

lib

lib

recipes

recipes

tests

tests

.clang-format

.clang-format

.coderabbit.yaml

.coderabbit.yaml

.dockerignore

.dockerignore

.gitattributes

.gitattributes

.gitignore

.gitignore

.lycheeignore

.lycheeignore

.pre-commit-config.yaml

.pre-commit-config.yaml

ATTRIBUTIONS-Go.md

ATTRIBUTIONS-Go.md

ATTRIBUTIONS-Python.md

ATTRIBUTIONS-Python.md

ATTRIBUTIONS-Rust.md

ATTRIBUTIONS-Rust.md

ATTRIBUTIONS-container-frontend.md

ATTRIBUTIONS-container-frontend.md

ATTRIBUTIONS.md

ATTRIBUTIONS.md

CODEOWNERS

CODEOWNERS

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

Cargo.lock

Cargo.lock

Cargo.toml

Cargo.toml

DCO.md

DCO.md

LICENSE

LICENSE

README.md

README.md

SECURITY.md

SECURITY.md

codespell.txt

codespell.txt

deny.toml

deny.toml

dynamo.code-workspace

dynamo.code-workspace

hatch_build.py

hatch_build.py

pyproject.toml

pyproject.toml

rust-toolchain.toml

rust-toolchain.toml

View all files

Repository files navigation

README

Code of conduct

Contributing

License

Security

| Docs | Roadmap | Recipes | Examples | Prebuilt Containers | Blog | Design Proposals |

Dynamo

The open-source, datacenter-scale inference stack. Dynamo is the orchestration layer above inference engines — it doesn't replace SGLang, TensorRT-LLM, or vLLM, it turns them into a coordinated multi-node inference system. Disaggregated serving, intelligent routing, multi-tier KV caching, and automatic scaling work together to maximize throughput and minimize latency for LLM, reasoning, multimodal, and video generation workloads.

Built in Rust for performance, Python for extensibility.

When to use Dynamo

You're serving LLMs across multiple GPUs or nodes and need to coordinate them

You want KV-aware routing to avoid redundant prefill computation

You need to independently scale prefill and decode (disaggregated serving)

You want automatic scaling that meets latency SLAs at minimum total cost of ownership (TCO)

You need fast cold-starts when spinning up new replicas

If you're running a single model on a single GPU, your inference engine alone is probably sufficient.

Feature support at a glance:
SGLangTensorRT-LLMvLLMDisaggregated Serving✅✅✅KV-Aware Routing✅✅✅SLA-Based Planner✅✅✅KVBM🚧✅✅Multimodal✅✅✅Tool Calling✅✅✅

Full Feature Matrix → — LoRA, request migration, speculative decoding, and feature interactions.

Key Results

ResultContext7x higher throughput per GPUDeepSeek R1 on GB200 NVL72 w/ Dynamo vs B200 without (InferenceX)7x faster model startupModelExpress weight streaming (DeepSeek-V3 on H200)2x faster time to first tokenKV-aware routing, Qwen3-Coder 480B (Baseten benchmark)80% fewer SLA breachesPlanner autoscaling at 5% lower TCO (Alibaba APSARA 2025 @ 2:50:00)750x higher throughputDeepSeek-R1 on GB300 NVL72 (InferenceXv2)

What Dynamo Does

Most inference engines optimize a single GPU or a single node. Dynamo is the orchestration layer above them — it turns a cluster of GPUs into a coordinated inference system.

Architecture Deep Dive →

Core Capabilities

CapabilityWhat it doesWhy it mattersDisaggregated Prefill/DecodeSeparates prefill and decode into independently scalable GPU poolsMaximizes GPU utilization; each phase runs on hardware tuned for its workloadKV-Aware RoutingRoutes requests based on worker load and KV cache overlapEliminates redundant prefill computation — 2x faster TTFTKV Block Manager (KVBM)Offloads KV cache across GPU → CPU → SSD → remote storageExtends effective context length beyond GPU memoryModelExpressStreams model weights GPU-to-GPU via NIXL/NVLink7x faster cold-start for new replicasPlannerSLA-driven autoscaler that profiles workloads and right-sizes poolsMeets latency targets at minimum total cost of ownership (TCO)GroveK8s operator for topology-aware gang scheduling (NVL72)Places workloads optimally across racks, hosts, and NUMA nodesAIConfiguratorSimulates 10K+ deployment configs in secondsFinds optimal serving config without burning GPU-hoursFault ToleranceCanary health checks + in-flight request migrationWorkers fail; user requests don't

New in 1.0

Zero-config deploy (DGDR)(beta): Specify model, HW, and SLA in one YAML — AIConfigurator auto-profiles the workload, Planner optimizes the topology, and Dynamo deploys

Agentic inference: Per-request hints for latency priority, expected output length, and cache pinning TTL. LangChain + NeMo Agent Toolkit integrations

Multimodal E/P/D: Disaggregated encode/prefill/decode with embedding cache — 30% faster TTFT on image workloads

Video generation: Native FastVideo + SGLang Diffusion support — real-time 1080p on single B200

K8s Inference Gateway plugin: KV-aware routing inside the standard Kubernetes gateway

Storage-tier KV offload: S3/Azure blob support + global KV events for cluster-wide cache visibility

Quick Start

Option A: Container (fastest)

# Pull a prebuilt container (SGLang example)
docker run --gpus all --network host --rm -it nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.0.1

# Inside the container — start frontend and worker
python3 -m dynamo.frontend --http-port 8000 --discovery-backend file > /dev/null 2>&1&
python3 -m dynamo.sglang --model-path Qwen/Qwen3-0.6B --discovery-backend file &# Send a request
curl -s localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "Qwen/Qwen3-0.6B", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 100}'| jq

Also available: 
tensorrtllm-runtime:1.0.1
 and 
vllm-runtime:1.0.1
.

Option B: Install from PyPI

pip install "ai-dynamo[sglang]"# or [vllm] or [trtllm]

Then start the frontend and a worker as shown above. See the full installation guide for system dependencies and backend-specific notes.

Option C: Kubernetes (recommended)

For production multi-node clusters, install the Dynamo Platform and deploy with a single manifest:

# Zero-config deploy: specify model + SLA, Dynamo handles the restapiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentRequestmetadata:
 name: my-modelspec:
 model: Qwen/Qwen3-0.6Bbackend: vllmsla:
 ttft: 200.0# msitl: 20.0# msautoApply: true

Pre-built recipes for common models:
ModelFrameworkModeRecipeLlama-3-70BvLLMAggregatedViewDeepSeek-R1SGLangDisaggregatedViewQwen3-32B-FP8TensorRT-LLMAggregatedView
See recipes/ for the full list. Cloud-specific guides: AWS EKS · Google GKE

Building from Source

For contributors who want to build and develop locally. See the full build guide for details.

# Install system deps (Ubuntu 24.04)
sudo apt install -y build-essential libhwloc-dev libudev-dev pkg-config libclang-dev protobuf-compiler python3-dev cmake

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh &&source$HOME/.cargo/env

# Create venv and build
uv venv dynamo &&source dynamo/bin/activate
uv pip install pip maturin
cd lib/bindings/python && maturin develop --uv &&cd$PROJECT_ROOT
uv pip install -e lib/gpu_memory_service
uv pip install -e .

VSCode/Cursor users: see the 
.devcontainer
 for a pre-configured dev environment.

Community and Contributing

Dynamo is built in the open with an OSS-first development model. We welcome contributions of all kinds.

Contribution Guide — How to contribute code, docs, and recipes

Design Proposals — RFCs for major features

Office Hours — Biweekly community calls

Discord — Chat with the team and community

Dynamo Day Recordings — Deep dives from production users

Latest News

[03/15] Dynamo 1.0 is here — production-ready with strong community adoption

[03/15] NVIDIA Blackwell Ultra sets new inference records in MLPerf

[03/15] NVIDIA Blackwell leads on SemiAnalysis InferenceMax benchmarks

[12/05] Moonshot AI's Kimi K2 achieves 10x inference speedup with Dynamo on GB200

[12/02] Mistral AI runs Mistral Large 3 with 10x faster inference using Dynamo

[11/20] Dell integrates PowerScale with NIXL for 19x faster TTFT
Older news
Dynamo provides comprehensive benchmarking tools:

Benchmarking Guide – Compare deployment topologies using AIPerf

SLA-Driven Deployments – Optimize deployments to meet SLA requirements

Frontend OpenAPI Specification

The OpenAI-compatible frontend exposes an OpenAPI 3 spec at 
/openapi.json
. To generate without running the server:

cargo run -p dynamo-llm --bin generate-frontend-openapi

This writes to 
docs/reference/api/openapi.json
.

Service Discovery and Messaging

Dynamo uses TCP for inter-component communication. On Kubernetes, native resources (CRDs + EndpointSlices) handle service discovery. External services are optional for most deployments:
DeploymentetcdNATSNotesLocal Development❌ Not required❌ Not requiredPass 
--discovery-backend file
; vLLM also needs 
--kv-events-config '{"enable_kv_cache_events": false}'
Kubernetes❌ Not required❌ Not requiredK8s-native discovery; TCP request plane

Note: KV-Aware Routing requires NATS for prefix caching coordination.

For Slurm or other distributed deployments (and KV-aware routing):

etcd can be run directly as 
./etcd
.

nats needs JetStream enabled: 
nats-server -js
.

To quickly setup both: 
docker compose -f deploy/docker-compose.yml up -d

More News

[11/20] Dell integrates PowerScale with Dynamo's NIXL for 19x faster TTFT

[11/20] WEKA partners with NVIDIA on KV cache storage for Dynamo

[11/13] Dynamo Office Hours Playlist

[10/16] How Baseten achieved 2x faster inference with NVIDIA Dynamo

[12/01] InfoQ: NVIDIA Dynamo simplifies Kubernetes deployment for LLM inference

Reference

Support Matrix — Hardware, OS, CUDA, and backend versions

Feature Matrix — Detailed backend compatibility

Release Artifacts — Containers, wheels, Helm charts

Service Discovery — K8s-native vs etcd vs file-based discovery

Benchmarking Guide — Compare deployment topologies with AIPerf

About

 A Datacenter Scale Distributed Inference Serving Framework
 

docs.nvidia.com/dynamo/latest

Resources

 Readme

License

 View license
 

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

6.5k
 stars

Watchers

70
 watching

Forks

1k
 forks

 Report repository

Releases
 23

Dynamo v1.0.1
 Latest

Mar 16, 2026

+ 22 releases

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

Rust56.3%

Python29.4%

Go11.4%

Shell1.1%

Dockerfile0.7%

Cuda0.2%

Other0.9%

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
