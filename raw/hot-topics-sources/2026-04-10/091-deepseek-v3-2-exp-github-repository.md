---
title: GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub
source_url: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp
final_url: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp
status: 200
content_type: text/html; charset=utf-8
topics: [DeepSeek Sparse Attention (DSA) for Long Context]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:38.267427+00:00
---

# GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub

## 원본 URL

https://github.com/deepseek-ai/DeepSeek-V3.2-Exp

## 추출 본문

GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub

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

 deepseek-ai
/DeepSeek-V3.2-ExpPublic

Notifications
You must be signed in to change notification settings

Fork
 154

 Star
1.6k

Code

Issues21

Pull requests7

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

deepseek-ai/DeepSeek-V3.2-Exp

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
18 Commits

18 Commits

inference

inference

DeepSeek_V3_2.pdf

DeepSeek_V3_2.pdf

LICENSE

LICENSE

README.md

README.md

cost.jpg

cost.jpg

View all files

Repository files navigation

README

MIT license

DeepSeek-V3.2-Exp

Introduction

We are excited to announce the official release of DeepSeek-V3.2-Exp, an experimental version of our model. As an intermediate step toward our next-generation architecture, V3.2-Exp builds upon V3.1-Terminus by introducing DeepSeek Sparse Attention—a sparse attention mechanism designed to explore and validate optimizations for training and inference efficiency in long-context scenarios.

This experimental release represents our ongoing research into more efficient transformer architectures, particularly focusing on improving computational efficiency when processing extended text sequences.

DeepSeek Sparse Attention (DSA) achieves fine-grained sparse attention for the first time, delivering substantial improvements in long-context training and inference efficiency while maintaining virtually identical model output quality.

To rigorously evaluate the impact of introducing sparse attention, we deliberately aligned the training configurations of DeepSeek-V3.2-Exp with V3.1-Terminus. Across public benchmarks in various domains, DeepSeek-V3.2-Exp demonstrates performance on par with V3.1-Terminus.

BenchmarkDeepSeek-V3.1-TerminusDeepSeek-V3.2-ExpReasoning Mode w/o Tool UseMMLU-Pro85.085.0GPQA-Diamond80.779.9Humanity's Last Exam21.719.8LiveCodeBench74.974.1AIME 202588.489.3HMMT 202586.183.6Codeforces20462121Aider-Polyglot76.174.5Agentic Tool UseBrowseComp38.540.1BrowseComp-zh45.047.9SimpleQA96.897.1SWE Verified68.467.8SWE-bench Multilingual57.857.9Terminal-bench36.737.7

Update

2025.11.17: We have identified that previous versions of the inference demo code contained an implementation discrepancy in Rotary Position Embedding (RoPE) within the indexer module, potentially leading to degraded model performance. Specifically, the input tensor to RoPE in the indexer module requires a non-interleaved layout, whereas RoPE in the MLA module expects an interleaved layout. This issue has now been resolved. Please refer to the updated version of the inference demo code and take note of this implementation detail.

Open-Source Kernels

For TileLang kernels with better readability and research-purpose design, please refer to TileLang.

For high-performance CUDA kernels, indexer logit kernels (including paged versions) are available in DeepGEMM. Sparse attention kernels are released in FlashMLA.

How to Run Locally

HuggingFace

We provide an updated inference demo code in the inference folder to help the community quickly get started with our model and understand its architectural details.

First convert huggingface model weights to the the format required by our inference demo. Set 
MP
 to match your available GPU count:

cd inference
export EXPERTS=256
python convert.py --hf-ckpt-path ${HF_CKPT_PATH} --save-path ${SAVE_PATH} --n-experts ${EXPERTS} --model-parallel ${MP}

Launch the interactive chat interface and start exploring DeepSeek's capabilities:

export CONFIG=config_671B_v3.2.json
torchrun --nproc-per-node ${MP} generate.py --ckpt-path ${SAVE_PATH} --config ${CONFIG} --interactive

SGLang

Installation with Docker

# H200
docker pull lmsysorg/sglang:dsv32

# MI350
docker pull lmsysorg/sglang:dsv32-rocm

# NPUs
docker pull lmsysorg/sglang:dsv32-a2
docker pull lmsysorg/sglang:dsv32-a3

Launch Command

python -m sglang.launch_server --model deepseek-ai/DeepSeek-V3.2-Exp --tp 8 --dp 8 --enable-dp-attention

vLLM

vLLM provides day-0 support of DeepSeek-V3.2-Exp. See the recipes for up-to-date details.

License

This repository and the model weights are licensed under the MIT License.

Citation

@misc{deepseekai2024deepseekv32,
 title={DeepSeek-V3.2-Exp: Boosting Long-Context Efficiency with DeepSeek Sparse Attention}, 
 author={DeepSeek-AI},
 year={2025},
}

Contact

If you have any questions, please raise an issue or contact us at service@deepseek.com.

About

 No description, website, or topics provided.
 

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

1.6k
 stars

Watchers

10
 watching

Forks

154
 forks

 Report repository

Releases

No releases published

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python100.0%

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
