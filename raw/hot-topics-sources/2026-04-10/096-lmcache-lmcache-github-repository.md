---
title: GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub
source_url: https://github.com/LMCache/LMCache
final_url: https://github.com/LMCache/LMCache
status: 200
content_type: text/html; charset=utf-8
topics: [LMCache-Based Distributed KV Cache Offloading, LMCache + Mooncake KV Cache Layer]
sections: [Inference Optimization, Infra & Serving]
fetched_at: 2026-04-10T01:43:38.806818+00:00
---

# GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub

## 원본 URL

https://github.com/LMCache/LMCache

## 추출 본문

GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub

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

 LMCache
/LMCachePublic

Notifications
You must be signed in to change notification settings

Fork
 1.1k

 Star
7.9k

Code

Issues120

Pull requests165

Actions

Projects

Wiki

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Wiki

 Security and quality

 Insights

LMCache/LMCache

dev

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
1,388 Commits

1,388 Commits

.buildkite

.buildkite

.cursor

.cursor

.gemini

.gemini

.github

.github

asset

asset

benchmarks

benchmarks

csrc

csrc

docker

docker

docs

docs

examples

examples

lmcache

lmcache

operator

operator

requirements

requirements

rust/raw_block

rust/raw_block

tests

tests

tools

tools

.clang-format

.clang-format

.gitignore

.gitignore

.isort.cfg

.isort.cfg

.pre-commit-config.yaml

.pre-commit-config.yaml

AGENTS.md

AGENTS.md

CMakeLists.txt

CMakeLists.txt

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

MANIFEST.in

MANIFEST.in

README.md

README.md

SECURITY.md

SECURITY.md

format.sh

format.sh

pyproject.toml

pyproject.toml

setup.py

setup.py

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

| Blog
| Documentation
| Join Slack
| Interest Form
| Roadmap

Summary

LMCache is an LLM serving engine extension to reduce TTFT and increase throughput, especially under long-context scenarios. By storing the KV caches of reusable texts all over the datacenter (including GPU, CPU, Disk and even S3) with a wide range of acceleration technqiue (zero cpu copy, NIXL, GDS and more). LMCache reuses the KV caches of any reused text (not necessarily prefix) in any serving engine instance. Thus, LMCache saves precious GPU cycles and reduces user response delay.

By combining LMCache with vLLM, developers achieve 3-10x delay savings and GPU cycle reduction in many LLM use cases, including multi-round QA and RAG.

LMCache is used, integrated, or referenced across a growing ecosystem of LLM serving platforms, infrastructure providers, and open-source projects:

Initiated and officially supported by: Tensormesh

Adopted by inference providers: GMI cloud (blog post), Google cloud (blog post), CoreWeave (blog post) and more

Integrated with data and storage infrastructure providers: Redis (blog post), Weka (blog post), PliOps (blog post) and more

Used by open-source projects and platforms: vLLM
, SGLang
, vLLM Production Stack, llm-d, NVIDIA dynamo, KServe and more.

For more details, please check our Ray Summit talk and technical report.

Features

 🔥 Integration with vLLM v1 with the following features:

High performance CPU KVCache offloading

Disaggregated prefill

P2P KVCache sharing

 Integration with SGLang for KV cache offloading

 Storage support as follows:

CPU

Disk

NIXL

 Installation support through pip and latest vLLM

Installation

To use LMCache, simply install 
lmcache
 from your package manager, e.g. pip:

pip install lmcache

Works on Linux NVIDIA GPU platform.

More detailed installation instructions are available in the docs, particularly if you are not using the latest stable version of vllm or using another serving engine with different dependencies. Any "undefined symbol" or torch mismatch versions can be resolved in the documentation.

Getting started

The best way to get started is to checkout the Quickstart Examples in the docs.

Documentation

Check out the LMCache documentation which is available online.

We also post regularly in LMCache blogs.

Examples

Go hands-on with our examples,
demonstrating how to address different use cases with LMCache.

Interested in Connecting?

Fill out the interest form, sign up for our newsletter, join LMCache slack, or drop an email, and our team will reach out to you!

Community meeting

The community meeting Zoom Link for LMCache is hosted bi-weekly. All are welcome to join!

Meetings are held bi-weekly on: Tuesdays at 9:00 AM PT – Add to Google Calendar

We keep notes from each meeting on this document for summaries of standups, discussion, and action items.

Recordings of meetings are available on the YouTube LMCache channel.

Contributing

We welcome and value all contributions and collaborations. Please check out Contributing Guide on how to contribute.

We continually update [Onboarding] Welcoming contributors with good first issues!

Citation

If you use LMCache for your research, please cite our papers:

@inproceedings{liu2024cachegen,
 title={Cachegen: Kv cache compression and streaming for fast large language model serving},
 author={Liu, Yuhan and Li, Hanchen and Cheng, Yihua and Ray, Siddhant and Huang, Yuyang and Zhang, Qizheng and Du, Kuntai and Yao, Jiayi and Lu, Shan and Ananthanarayanan, Ganesh and others},
 booktitle={Proceedings of the ACM SIGCOMM 2024 Conference},
 pages={38--56},
 year={2024}
}

@article{cheng2024large,
 title={Do Large Language Models Need a Content Delivery Network?},
 author={Cheng, Yihua and Du, Kuntai and Yao, Jiayi and Jiang, Junchen},
 journal={arXiv preprint arXiv:2409.13761},
 year={2024}
}

@inproceedings{10.1145/3689031.3696098,
 author = {Yao, Jiayi and Li, Hanchen and Liu, Yuhan and Ray, Siddhant and Cheng, Yihua and Zhang, Qizheng and Du, Kuntai and Lu, Shan and Jiang, Junchen},
 title = {CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion},
 year = {2025},
 url = {https://doi.org/10.1145/3689031.3696098},
 doi = {10.1145/3689031.3696098},
 booktitle = {Proceedings of the Twentieth European Conference on Computer Systems},
 pages = {94–109},
}

@article{cheng2025lmcache,
 title={LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference},
 author={Cheng, Yihua and Liu, Yuhan and Yao, Jiayi and An, Yuwei and Chen, Xiaokun and Feng, Shaoting and Huang, Yuyang and Shen, Samuel and Du, Kuntai and Jiang, Junchen},
 journal={arXiv preprint arXiv:2510.09665},
 year={2025}
}

Socials

Linkedin | Twitter | Youtube

License

The LMCache codebase is licensed under Apache License 2.0. See the LICENSE file for details.

About

 Supercharge Your LLM with the Fastest KV Cache Layer
 

lmcache.ai/

Topics

 fast

 amd

 cuda

 inference

 pytorch

 speed

 rocm

 kv-cache

 llm

 vllm

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

7.9k
 stars

Watchers

42
 watching

Forks

1.1k
 forks

 Report repository

Releases
 33

v0.4.3
 Latest

Apr 6, 2026

+ 32 releases

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

Python88.7%

Shell4.3%

Cuda1.9%

Go1.9%

C++1.9%

JavaScript0.4%

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
