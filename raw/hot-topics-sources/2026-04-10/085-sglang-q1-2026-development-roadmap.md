---
title: Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub
source_url: https://github.com/sgl-project/sglang/issues/12780
final_url: https://github.com/sgl-project/sglang/issues/12780
status: 200
content_type: text/html; charset=utf-8
topics: [Prefill/Decode Disaggregated Serving, SGLang on GB300 NVL72 with NVFP4]
sections: [Inference Optimization, Infra & Serving]
fetched_at: 2026-04-10T01:43:37.452697+00:00
---

# Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub

## 원본 URL

https://github.com/sgl-project/sglang/issues/12780

## 추출 본문

Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang · GitHub

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

 sgl-project
/sglangPublic

Notifications
You must be signed in to change notification settings

Fork
 5.3k

 Star
25.6k

Code

Issues599

Pull requests2.2k

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

Development Roadmap (2026 Q1)#12780

New issue
Copy link

New issue
Copy link

Open

0 / 10 of 1 issue completed

Open

Development Roadmap (2026 Q1)#12780

0 / 10 of 1 issue completed

Copy link

Assignees

Description

hnyls2002

opened on Nov 6, 2025

Issue body actions

SGLang Roadmap — 2026 Q1

Contributions and feedback are welcome. Join Slack.

Focus

Feature compatibility & reliability: Full compatibility and production-level reliability across P/D disaggregation, all parallelisms, speculative decoding, HiCache, and load balancing.

Usability: Easy installation on NV/AMD/TPU/CPU; simple large-scale deployment (k8s, OME).

Kernel optimization for next-gen hardware (GB300/GB200, B300/B200, MI350/MI355, TPU).

Reinforcement learning framework integration and training-inference mismatch mitigation.

Multimodal: Enhance diffusion models for video and image generation. Omni model support.

Base Engine Features

Turn on overlap scheduler for speculative decoding by default

PoC: @hnyls2002

Slack: #spec-decoding

Issue: [Feature] Overlap Spec Support #11762

Turn on prefill CUDA graph by default

PoC: @Oasis-Git@ispobock@BBuf

Slack: #piecewise-cuda-graph

Issue: [Feature] Roadmap for Prefill (Piecewise) CUDA Graph #11490

General memory pool and prefix cache for hybrid models

PoC: @cctry@xiezhq-hermann

Slack: #prefix-cache, #kv-cache-store

Issue: [Feature] Memory Cache System Refactoring Road Map (Mem Cache V2) #12587

Mixed chunked prefill refactor

PoC: @hzh0425@yizhang2077

Issue: [Feature] Mixed ChunkPrefill Optimization Roadmap #13626

Torch compile stack (Looking for PoC)

Slack: #torch-compile

PR: [WIP] Support torch compile based pass manager framework #10987

Issue: [RFC] SGLang unified kernel fusion and torch compile optimisations #10118

SRT core/plugin refactor

Goal: make the core reusable, so people can do customization easily and maintain their out-of-the-tree code.

DP attention and attention backend refactor

Goal: make attention backends fully stateless, unify the sync positions of dp attention.

Parallelism

Pipeline parallelism refactor for long-context prefill and high-throughput decoding

PoC: @ShangmingCai

Slack: #pipeline-parallel

Issue: [Roadmap] Pipeline parallelism roadmap #11857

Expert parallelism refactor

PoC: @ch-wan

Slack: #expert-parallel

Issue: [Roadmap] MoE Refactor #8715

Elastic parallel PRs: [1/N] Introduce Mooncake Backend and Mooncake EP to Support Elastic EP #10423, [4/N]Elastic EP support deepep backend #11837

Context parallelism

Prefill CP: [Feature] Support context parallel for Qwen3 model #16632

Megatron SP: [WIP][Feature] support tp-sp on qwen2/3 & deepseek v2/3/3.2 #12820

Decode CP:

[Feature] Add DCP support for GQA with flashinfer #14982

[feature] implement dcp for deepseek_v2 #14194

[Feature] Add DCP support for DeepSeek v3.2 #18167

[Feature] Helix (TP + CP) Parallelism: A2A Communication + Decoupled Attention/FFN Parallelism #19436

Compatibility goals

All parallelisms + speculative decoding

All parallelisms + PD disaggregation

Multiple load balancing strategies for DP attention/system (minimal tokens, shortest queue) [Feature] Load Balance Refactor for DP-Attention #16080

GB200/GB300 NVL72 optimizations

PoC: @Fridge003@fzyzcjy

More details in PD Disaggregation/Large Scale Serving section of SGLang Nvidia Collaboration Roadmap (2026 Q1) #17130

Slack: #deepseek-large-scale-serving

Server Reliability

Illegal memory access fixes. [Bug] illegal memory access / illegal instruction / memory leak #11968

Runtime memory/paging checker.

Grammar crash fault tolerance.

Server crash fault tolerance.

Kernel

JIT kernels

Roadmap: [Roadmap] JIT kernel development #17035[Feature] sgl-kernel wheel slimming plan tracking #17865

PoC: @DarkSharpness

Integrate Flashinfer kernels

More details in Flashinfer section of SGLang Nvidia Collaboration Roadmap (2026 Q1) #17130

Slack: #flashinfer-kernels

Tune FP8 gemm in Cutlass

Slack: #kernel-dev

Communication kernel work

Slack: #kernel-dev

NCCL symmetric memory (PRs: Add support for NCCL symmetric memory for TP allreduces #8238, Register allgather/reducescatter buffers with symm memory #12572)

Overlap TP communication with compute (e.g., Support TP overlap #9058)

Integrate additional A2A kernels (e.g., pplx)

Automated nightly fusion detection

Workflow: https://github.com/sgl-project/sglang/actions/runs/19004823026

Slack: #ci-cd-build-release

Speculative Decoding

General speculative algorithm abstraction to support multiple algorithms

Hybrid algorithm combining Eagle and ngram

Adaptive algorithm that adjusts speculative parameters during runtime

Support for dllm draft models in sglang, associated with SpecForge RFC: dLLM (DFlash) Online Training in SpecForge SpecForge#412@jinleic@yilian49@xiaomin-D@sleepcoo

Slack: #spec-decoding

PD Disaggregation

Support radix cache on decode engines [P/D disagg] - support decode side radix cache #19746

Refactor scheduler loop to reuse more code

More plans: [Roadmap] Distributed Serving Enhancement on 2025 H2 #8210

Auto scaling in OME

Comprehensive NIXL and Dynamo integration

Slack: #pd-disaggregation

KV Cache System & Memory Pool

PoC: @xiezhq-hermann

Issue: [Feature] HiCache for Hybrid and Sparse LLMs #12826.

slack #kv-cache-store

Sparse attention and KV cache scheduler for GPU/CPU

PR: [Feature] Support Sparse Attention and KV cache scheduling between CPU and GPU for GQA/DSA. #11191

Diffusion (Multimodal Generation)

PoC: @mickqian

Roadmap:

25Q3: [Roadmap] Diffusion (2025 Q4) #12799

26Q1: [Roadmap] SGLang-Diffusion (26 Q1) #18286

Slack: #diffusion

Multimodal Models

Day-0 support for major models; add more OCR models

Contributors: @mick@JustinTong0323@yuan-luo

Performance improvements: better prefix & embedding cache

Faster CUDA IPC in MQ for large video/images

PR: [FEAT] Shared mem pool based cuda ipc for multi-modal data transport #11917

Omni Support [RFC] SGLang-Omni Design #16546

Slack: #multi-modal

Quantization

General support for various quantization formats and refactor

Issue: [Roadmap] Quantization Modifications #15194

ModelOpt support

PoC: @Edwardf0t1

More details in Model Optimizer section of SGLang Nvidia Collaboration Roadmap (2026 Q1) #17130

Slack: #modelopt

Communication quantization (fp4/fp8 allreduce/allgather/alltoall)

Slack: #quantization

Multi-LoRA Serving

Major roadmap: [Roadmap] Lora Support #2929

PoC: @Fridge003

LoRA for speculative decoding Support spec decoding when LoRA is applied to target model  #12903

Contributor: @ConnorLi96@lifuhuang

Overlap Weight Loading with Compute [Feature] overlap LoRA weight loading with compute #15512

Contributor: @glenliu21@ConnorLi96@lifuhuang

LoRA for MoE layers [LoRA][III] Add LoRA support for MoE layers and enable TP #14105

Contributors: @ConnorLi96@Jonahcb

Slack: #lora

Prefill-Only

Major roadmap: [Roadmap] SGLang Prefill-Only 2026 CY26H1 Roadmap #15344

PoC: @sundar24295s

Slack: #prefill-only

RL Framework Integration

AReaL, slime, verl integration (sorted alphabetically)

Customized weight refitting from RDMA, etc @zhaochenyang20@JD-ETH

Open recipe of large-scale MoE training (Deepseek/Kimi/GLM) + GRPO training

Systematic and algorithm mitigation for training-inference mismatch @zhaochenyang20@fzyzcjy@Fridge003@zyzshishui

Support SGLang Gateway as the DP scheduler for rollout in the RL framework

Tinker-like serverless RL APIs; @zhaochenyang20

Native NVFP8 Training; @GeLee-Q@xieck13@fy1214

VLM RL with FSDP; @nanjiangwill@minleminzui

Speculative Training; @guapisolo

Slack: #reinforcement-learning, #slime-rl-framework

Diffusion Language Models (DLLMs)

PoC: Zehuan Li, Jinwei Yao, Chenyang Zhao

RFC: Block Diffusion Large Language Model (dLLM) Framework

Roadmap: [Roadmap] Diffusion LLMs (2025 Q4 & 2026 Q1) #14199

Hardware

AMD roadmap (2025 Q4): @HaiShaw
[Roadmap] AMD Instinct Development (2025Q4) #12890

TPU roadmap (2025 Q4)

Development Roadmap (2025 Q4) sglang-jax#190

Slack: #dev-jax-tpu

NPU roadmap (2025 Q4): @iforgetmyname@ZhengdQin
[Roadmap] Ascend NPU Development (2026 Q1) #13664

Intel CPU/XPU roadmap (2025 Q4):

[Roadmap] Intel CPU Roadmap (2025Q4) #12802

[Roadmap] Intel XPU Roadmap (2025Q4) #12806

Better multi-backend abstraction: @Alcanderian

Model Coverage

Day-0 model support for all major models

PoC: @wisclmy0611@JustinTong0323

Slack: #dev

Model Gateway & API Layer

Support multimodality and image processor in gRPC mode

Support PII and classify API for classifying intent and complexity of the input

Semantic Routing Support

Allow Gateway to actively listen to SGLang server's KV cache events to better handle routing decisions in gRPC mode

Allow SGLang server to start with both gRPC and HTTP server

Model Gateway terminal UI

Reactive UI to launch workers remotely; this should support both local machines and remote

Natively support Anthropic Message API instead of wrapping around chat completion in gRPC mode

Gateway SDK, supporting GoLang, Python, and Node.js for every Rust crate (policies, tokenizer, parsers, etc)

Metrics enhancement, including tracing, model-specific metrics (TTFT, TPOT, etc)

PoC: @slin1237@CatherineSue

Issue: SGLang Autonomous Model Gateway Roadmap #13098

Slack: #router-sig

Tracing and Profiling

Roadmap of request tracing: HiCache, PP, and SD. [Roadmap] roadmap of request tracing (2025 Q4 and 2026 Q1) #13511

Advanced Priority Scheduling

[Roadmap] Priority based traffic management (priority scheduling, batching, and concurrency control) #13526

PoC: @harrisonlimh

CI / Release / Maintenance

CI suites refactor: [Roadmap] CI suites organization #13808

PoC: @alisonshao@Kangyan-Zhou

Improve CI monitor workflow

Automatically track accuracy & performance metrics with standard format

Regression detection & alerts

Add performance dashboard for popular model (deepseek r1) in track of performance changes

Improve nightly tests

Add more models (Deepseek, GPT-OSS, Qwen3-next)

Full feature coverage CI with all combinations (every two days)

Coverage of latest hardware (B300/GB200)

More details in CI/CD section of SGLang Nvidia Collaboration Roadmap (2026 Q1) #17130

Slack: #ci-cd-build-release, #help-desk

Reactions are currently unavailable

Metadata

Metadata

Assignees

CatherineSue

hnyls2002

ispobock

slin1237

xiezhq-hermann

Labels

No labels

No labels

Type

No type

Projects

No projects

Milestone

No milestone

Relationships

None yet

Development

No branches or pull requests

Issue actions

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
