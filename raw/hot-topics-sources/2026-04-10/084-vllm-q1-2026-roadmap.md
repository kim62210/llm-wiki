---
title: [Roadmap] vLLM Roadmap Q1 2026 · Issue #32455 · vllm-project/vllm · GitHub
source_url: https://github.com/vllm-project/vllm/issues/32455
final_url: https://github.com/vllm-project/vllm/issues/32455
status: 200
content_type: text/html; charset=utf-8
topics: [Prefill/Decode Disaggregated Serving, vLLM V1 Engine on Blackwell (GB200/GB300)]
sections: [Inference Optimization, Infra & Serving]
fetched_at: 2026-04-10T01:43:37.389191+00:00
---

# [Roadmap] vLLM Roadmap Q1 2026 · Issue #32455 · vllm-project/vllm · GitHub

## 원본 URL

https://github.com/vllm-project/vllm/issues/32455

## 추출 본문

[Roadmap] vLLM Roadmap Q1 2026 · Issue #32455 · vllm-project/vllm · GitHub

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

 vllm-project
/vllmPublic

 Uh oh!

There was an error while loading. Please reload this page.

Notifications
You must be signed in to change notification settings

Fork
 15.4k

 Star
75.9k

Code

Issues1.9k

Pull requests2.4k

Discussions

Actions

Projects

Security and quality39

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Security and quality

 Insights

[Roadmap] vLLM Roadmap Q1 2026#32455

New issue
Copy link

New issue
Copy link

Open

Open

[Roadmap] vLLM Roadmap Q1 2026#32455

Copy link

Labels

rocmRelated to AMD ROCmRelated to AMD ROCm

Description

simon-mo

opened on Jan 16, 2026

Issue body actions

Hi vLLM Community,

We are tackling the roadmap a bit differently this year. In this roadmap, the planned objectives and milestones are captured by different areas. For each area, you will find more detailed tracking issues and lead committers to discuss with. Please continue to send feedback here!

Core Engine

Meeting Time/Link:

Channel: #sig-core

Members: @WoosukKwon

The team focuses on the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runner, KV Connector code path.

 Turn async scheduling on by default @njhill

 Turn model runner V2 on by default @WoosukKwon
 dual batch overlap

 piecewise cg

 pipeline parallelism

 more attention backends (right now it’s only flash attention)

 more testing

 CPU KV cache production ready: performance optimized, HMA support @orozery

 Process structure simplification/flattening prototype @zhuohan123

 Data structure clean up: improve efficiently for data structures that grow with number of tokens and number of requests (e.g., list[int] -> numpy arrays, removing dictionaries). @njhill

 Attention backend re-design

One goal this SIG will work on is interface stability and decoupling. Right now, we only provide backward compatibility on public APIs, 
LLM, AsyncLLM, LLMEngine
. Besides these we provide zero backward compatibility. We will gradually refactor the codebase, starting with a stable Model implementation API. A more stable API base improves the overall plugin ecosystem and modularity of vLLM.

 Stable model implementation API

 Model config refactor @zhuohan123

 Clean up

 Weight Loading

 Distributed Linear

 Quantization @robertgshaw2-redhat

Finally, low latency serving with spec decoding is in scope as well, led by @benchislett

 Stable support MTP (one layer) for Qwen3-Next and Deepseek

 Expand coverage and testing MTP with multiple layers

 Support and test EAGLE-3 thoroughly.

Large Scale Serving

Meeting Time/Link: See Channel

Channel: #sig-large-scale-serving

Members: @tlrmchlsmth

Project board: Large-Scale Serving

The team focuses on pushing vLLM to speed of light on disaggregated, wide EP, and elastic setting on clusters of H200, B200, and more importantly GB200. The team is also responsible for interfacing with ecosystem projects such as llm-d, Dynamo, and AMD team.

 Publish reproducible recipes for DeepSeek architecture on GB200 with 
vllm-router

 Finish the FusedMoE refactor, remove/deprecate unnecessary gemm and comm kernels.

 P/D and Wide EP recipes on AMD ROCm

 Achieve SoTA GB200 results on DeepSeek architecture by exploiting NVLink, CPU unified memory, FP4, and multi-stream concurrency.

 Publish GB300 early experiment

 Elastic EP in beta (ready for external testing)

 Minimize overheads from EPLB expert rearranging and use async EPLB by default when EPLB is enabled.

Evaluate the need to place vllm-router between API server and core engine.

Speed of Light

Meeting Time/Link: Tuesday 11:30AM PT

Channel: #sig-model-performance

Members: @robertgshaw2-redhat@simon-mo

The team focuses on pure performance and reliability engineering within vLLM. The work involves capturing performance traces, enabling the right set of kernels by default, and continuously monitoring it. The work also covers monitoring and logging for production stability. This is a combination of #sig-model-bash and performance dashboard effort.

 Performance dashboard and model bash for high priority models (DSV3.2, K2, gpt-oss, Qwen3-Next, Gemma3) on popular hardwares (GB200, H200, MI355).

 Profiling tooling

 Replicate InferenceMax and coordinate efforts for further improvements

Python overhead reduction via dummy model on GB200

Torch Compile

Meeting Time: Thursday 12.30 ET (9.30 PT)

Meeting Notes: torch.compile SIG (also includes joining instructions)

Channel: #sig-torch-compile

Members: @ProExpertProg@zou3519

The team focuses on improving performance, portability, and developer productivity via PyTorch compilation integration. Work includes custom compile & fusion passes, vLLM IR for kernel registration, reducing compile time via caching, improving developer UX with torch.compile, and co-development of new torch.compile features.

 Enable more optimizations by default using optimization (
-O2
, 
-O3
) levels

 Migrate CustomOps to vLLM IR

 Integrate Helion into vLLM

 Improve cold and warm compilation time

 Unwrap wrapped custom ops (MLA, Fused MoE)

Improved perf dashboard to track compile speedups and breakdown warm and cold start times.

 torch.compile x nvsymmetric memory integration

Frontend

Meeting Time/Link: TBD

Channel: #sig-frontend

Members:

The team focuses on the OpenAI compatible API server, as well as various other protocols. Its scope also covers the implementation of renderer and tool parser, which are components responsible for input and output format interfacing with engine core.

 Use structural tag for tool parser, overall refactoring of tool parsing logits for simplicity and robustness

 Responses API

 Renderer refactoring

 Disaggregate everything

RL

Meeting Time/Link: TBD

Channel: #sig-post-training

Members: @youkaichao@robertgshaw2-redhat

The team focuses on delivering vLLM the best engine features for RL rollout including weight sync, kv cache reset, and ease-of-modification.

 Modular weight sync [RFC]: Native Weight Syncing APIs #31848

 Continue enhancement of test cases

 Publication of reproduction runs with SOTA open source RL techniques, collaborating with open source RL frameworks

 Harden external launcher mode

MultiModality

Meeting Time/Link: Every two weeks - calendar invites

Channel: #sig-multi-modality

Members: @ywang96@DarkLight1337

The team supports the abstractions, model support, and optimizations of multi-modality input.

 Streaming inputs: [Feature] add session based streaming input support to v1 #28973

 Input processing

Quantization

Meeting Time/Link: Every week, meeting

Channel: #sig-quantization

Members: @mgoin@dsikka

vLLM's quantization support, including native online, LLM Compressor, and external integrations like ModelOpt.

 vLLM native online quantization and UX refactor (remove 
--quantization
 explicit arguments, ignore list, non-uniform quantization, mxfp8)

 Remove the deprecated quantization schemes [RFC]: Deprecate Legacy Quantization Formats #30136

 Register all kernel backends with supported feature checks

 Register a single-source-of-truth oracle for each quantization format to dispatch to kernel backends

 nvfp4 + mxfp4 compression recipes + algorithms

Speculative Decoding

Meeting Time/Link: Every week, meeting

Channels: #sig-spec-decode, #speculators

Members: @benchislett@fynnsu@mgoin

Focuses on speculative decoding in vLLM and Speculators.

 For speculators, release all frontier model speculators on HF https://huggingface.co/collections/RedHatAI/speculator-models

 Hidden states extraction

Documentation, Recipes, Blog

Channel: #sig-docs, #blogs, #recipes

The team will focus on lowering the learning curve for vLLM and enhance usability through materials and educational content.

 Enhanced recipes for all popular models

 Technical blog on vLLM’s optimization and technical deep dive specific to different models

 Educational material for developer on architecture, internals, and meetup

CI, Build, and Release

Meeting Time/Link: Tuesday 11AM Pacific

Channel: #sig-ci

Members: @khluu

The team focuses on developing world class infrastructure for vLLM’s CI system and ensuring we have a secure and reliable build and release process.

 Meet two weeks release cadence (there should be six releases in Q1!)

 Time to first test in 10 minutes and E2E CI time to signal in 30 minutes.

 Release nightly wheels covering SOTA hardware support (e.g GB300).

 Automatic quarantine for flaky tests

 Automatic test target determination

 Auto-bisect workflow

 CI dashboard

The following are semi-open program that focus on iterations of vLLM, handling potentially sensitive informations.

Committer Development Program

This program, led by the lead maintainers, focus on continue to cultivate new committers and enhance the contribution experience of vLLM:

 Publish Reviewer Guideline (quality and speed choose two, each PR should bring clear improvements, higher PR bar)

 Iterate on community PR maintenance policy

 Iterate on issue triage

 Continue to develop active contributors into committers

Model Support Program

We will work on streamlining our model support process with model and hardware vendors. All frontier model releases should be accuracy validated on day 0 with automated suite for widely used configs, basic performance (no synchronization and enabled fused ops) on week 1, and matured support by month 1.

 Automation and tracking around model support

 Develop a new model authoring tool/framework to ease model porting and reduce human errors (related RFC) with the feedback from model vendors

 Model testing pipeline

 Standardize marketing promotions around new model release and distribution

 Improve recipes for ease of modifications and performance result

Ecosystem Project Roadmap

vLLM Omni

Semantic Router

Reactions are currently unavailable

Metadata

Metadata

Assignees

No one assigned

Labels

rocmRelated to AMD ROCmRelated to AMD ROCm

Type

No type

Projects

AMD

Status

Todo

Show more project fields

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
