---
title: GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub
source_url: https://github.com/sgl-project/sglang
final_url: https://github.com/sgl-project/sglang
status: 200
content_type: text/html; charset=utf-8
topics: [SGLang on GB300 NVL72 with NVFP4]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:08.447711+00:00
---

# GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub

## 원본 URL

https://github.com/sgl-project/sglang

## 추출 본문

GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub

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

sgl-project/sglang

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
11,462 Commits

11,462 Commits

.claude/skills

.claude/skills

.devcontainer

.devcontainer

.github

.github

3rdparty/amd

3rdparty/amd

assets

assets

benchmark

benchmark

docker

docker

docs

docs

examples

examples

python

python

scripts

scripts

sgl-kernel

sgl-kernel

sgl-model-gateway

sgl-model-gateway

test

test

.codespellrc

.codespellrc

.coveragerc

.coveragerc

.dockerignore

.dockerignore

.gitignore

.gitignore

.isort.cfg

.isort.cfg

.pre-commit-config.yaml

.pre-commit-config.yaml

LICENSE

LICENSE

README.md

README.md

View all files

Repository files navigation

README

Apache-2.0 license

Blog |
Documentation |
Roadmap |
Join Slack |
Weekly Dev Meeting |
Slides

News

[2026/02] 🔥 Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72 (blog).

[2026/01] 🔥 SGLang Diffusion accelerates video and image generation (blog).

[2025/12] SGLang provides day-0 support for latest open models (MiMo-V2-Flash, Nemotron 3 Nano, Mistral Large 3, LLaDA 2.0 Diffusion LLM, MiniMax M2).

[2025/10] 🔥 SGLang now runs natively on TPU with the SGLang-Jax backend (blog).

[2025/09] Deploying DeepSeek on GB200 NVL72 with PD and Large Scale EP (Part II): 3.8x Prefill, 4.8x Decode Throughput (blog).

[2025/09] SGLang Day 0 Support for DeepSeek-V3.2 with Sparse Attention (blog).

[2025/08] SGLang x AMD SF Meetup on 8/22: Hands-on GPU workshop, tech talks by AMD/xAI/SGLang, and networking (Roadmap, Large-scale EP, Highlights, AITER/MoRI, Wave).
More
[2025/11] SGLang Diffusion accelerates video and image generation (blog).

[2025/10] PyTorch Conference 2025 SGLang Talk (slide).

[2025/10] SGLang x Nvidia SF Meetup on 10/2 (recap).

[2025/08] SGLang provides day-0 support for OpenAI gpt-oss model (instructions)

[2025/06] SGLang, the high-performance serving infrastructure powering trillions of tokens daily, has been awarded the third batch of the Open Source AI Grant by a16z (a16z blog).

[2025/05] Deploying DeepSeek with PD Disaggregation and Large-scale Expert Parallelism on 96 H100 GPUs (blog).

[2025/06] Deploying DeepSeek on GB200 NVL72 with PD and Large Scale EP (Part I): 2.7x Higher Decoding Throughput (blog).

[2025/03] Supercharge DeepSeek-R1 Inference on AMD Instinct MI300X (AMD blog)

[2025/03] SGLang Joins PyTorch Ecosystem: Efficient LLM Serving Engine (PyTorch blog)

[2025/02] Unlock DeepSeek-R1 Inference Performance on AMD Instinct™ MI300X GPU (AMD blog)

[2025/01] SGLang provides day one support for DeepSeek V3/R1 models on NVIDIA and AMD GPUs with DeepSeek-specific optimizations. (instructions, AMD blog, 10+ other companies)

[2024/12] v0.4 Release: Zero-Overhead Batch Scheduler, Cache-Aware Load Balancer, Faster Structured Outputs (blog).

[2024/10] The First SGLang Online Meetup (slides).

[2024/09] v0.3 Release: 7x Faster DeepSeek MLA, 1.5x Faster torch.compile, Multi-Image/Video LLaVA-OneVision (blog).

[2024/07] v0.2 Release: Faster Llama3 Serving with SGLang Runtime (vs. TensorRT-LLM, vLLM) (blog).

[2024/02] SGLang enables 3x faster JSON decoding with compressed finite state machine (blog).

[2024/01] SGLang provides up to 5x faster inference with RadixAttention (blog).

[2024/01] SGLang powers the serving of the official LLaVA v1.6 release demo (usage).

About

SGLang is a high-performance serving framework for large language models and multimodal models.
It is designed to deliver low-latency and high-throughput inference across a wide range of setups, from a single GPU to large distributed clusters.
Its core features include:

Fast Runtime: Provides efficient serving with RadixAttention for prefix caching, a zero-overhead CPU scheduler, prefill-decode disaggregation, speculative decoding, continuous batching, paged attention, tensor/pipeline/expert/data parallelism, structured outputs, chunked prefill, quantization (FP4/FP8/INT4/AWQ/GPTQ), and multi-LoRA batching.

Broad Model Support: Supports a wide range of language models (Llama, Qwen, DeepSeek, Kimi, GLM, GPT, Gemma, Mistral, etc.), embedding models (e5-mistral, gte, mcdse), reward models (Skywork), and diffusion models (WAN, Qwen-Image), with easy extensibility for adding new models. Compatible with most Hugging Face models and OpenAI APIs.

Extensive Hardware Support: Runs on NVIDIA GPUs (GB200/B300/H100/A100/Spark/5090), AMD GPUs (MI355/MI300), Intel Xeon CPUs, Google TPUs, Ascend NPUs, and more.

Active Community: SGLang is open-source and supported by a vibrant community with widespread industry adoption, powering over 400,000 GPUs worldwide.

RL & Post-Training Backbone: SGLang is a proven rollout backend used for training many frontier models, with native RL integrations and adoption by well-known post-training frameworks such as AReaL, Miles, slime, Tunix, verl and more.

Getting Started

Install SGLang

Quick Start

Backend Tutorial

Frontend Tutorial

Contribution Guide

Benchmark and Performance

Learn more in the release blogs: v0.2 blog, v0.3 blog, v0.4 blog, Large-scale expert parallelism, GB200 rack-scale parallelism, GB300 long context.

Adoption and Sponsorship

SGLang has been deployed at large scale, generating trillions of tokens in production each day. It is trusted and adopted by a wide range of leading enterprises and institutions, including xAI, AMD, NVIDIA, Intel, LinkedIn, Cursor, Oracle Cloud, Google Cloud, Microsoft Azure, AWS, Atlas Cloud, Voltage Park, Nebius, DataCrunch, Novita, InnoMatrix, MIT, UCLA, the University of Washington, Stanford, UC Berkeley, Tsinghua University, Jam & Tea Studios, Baseten, and other major technology organizations.
As an open-source LLM inference engine, SGLang has become the de facto industry standard, with deployments running on over 400,000 GPUs worldwide.
SGLang is currently hosted under the non-profit open-source organization LMSYS.

Contact Us

For enterprises interested in adopting or deploying SGLang at scale, including technical consulting, sponsorship opportunities, or partnership inquiries, please contact us at sglang@lmsys.org.

Long-term active SGLang contributors are eligible for coding agent sponsorship, such as Cursor, Claude Code, or OpenAI Codex. Email sglang@lmsys.org with your most important commits or pull requests.

Acknowledgment

We learned the design and reused code from the following projects: Guidance, vLLM, LightLLM, FlashInfer, Outlines, and LMQL.

About

 SGLang is a high-performance serving framework for large language models and multimodal models.
 

sglang.io

Topics

 reinforcement-learning

 cuda

 inference

 transformer

 moe

 attention

 llama

 glm

 minimax

 wan

 diffusion

 vlm

 blackwell

 llm

 qwen

 deepseek

 gpt-oss

 qwen-image

Resources

 Readme

License

 Apache-2.0 license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

25.6k
 stars

Watchers

141
 watching

Forks

5.3k
 forks

 Report repository

Releases
 49

v0.5.10.post1
 Latest

Apr 9, 2026

+ 48 releases

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

Python82.1%

Rust7.9%

Cuda4.6%

C++3.9%

Shell0.5%

C0.3%

Other0.7%

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
