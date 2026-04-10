---
title: GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub
source_url: https://github.com/mlc-ai/xgrammar
final_url: https://github.com/mlc-ai/xgrammar
status: 200
content_type: text/html; charset=utf-8
topics: [XGrammar-2 Constrained Decoding for Agentic LLMs]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:40.131061+00:00
---

# GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub

## 원본 URL

https://github.com/mlc-ai/xgrammar

## 추출 본문

GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub

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

 mlc-ai
/xgrammarPublic

Notifications
You must be signed in to change notification settings

Fork
 136

 Star
1.6k

Code

Issues17

Pull requests12

Actions

Projects

Security and quality4

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

mlc-ai/xgrammar

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
402 Commits

402 Commits

.github

.github

3rdparty

3rdparty

assets

assets

cmake

cmake

cpp

cpp

docs

docs

examples

examples

include/xgrammar

include/xgrammar

python/xgrammar

python/xgrammar

scripts

scripts

site

site

tests

tests

web

web

.clang-format

.clang-format

.cmake-format.yaml

.cmake-format.yaml

.gitignore

.gitignore

.gitmodules

.gitmodules

.pre-commit-config.yaml

.pre-commit-config.yaml

.yamlfmt

.yamlfmt

CMakeLists.txt

CMakeLists.txt

CODEOWNERS

CODEOWNERS

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

NOTICE

NOTICE

README.md

README.md

pyproject.toml

pyproject.toml

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

Efficient, Flexible and Portable Structured Generation

Get Started | Documentation | Blogpost | Technical Report

News

[2025/12] XGrammar has been officially integrated into Mirai

[2025/09] XGrammar has been officially integrated into OpenVINO GenAI

[2025/02] XGrammar has been officially integrated into Modular's MAX

[2025/01] XGrammar has been officially integrated into TensorRT-LLM.

[2024/12] XGrammar has been officially integrated into vLLM.

[2024/12] We presented research talks on XGrammar at CMU, UC Berkeley, MIT, THU, SJTU, Ant Group, LMSys, Qingke AI, Camel AI. The slides can be found here.

[2024/11] XGrammar has been officially integrated into SGLang.

[2024/11] XGrammar has been officially integrated into MLC-LLM.

[2024/11] We officially released XGrammar v0.1.0!

Overview

XGrammar is an open-source library for efficient, flexible, and portable structured generation.

It leverages constrained decoding to ensure 100% structural correctness of the output. It supports general context-free grammar to enable a broad range of structures, including JSON, regex, custom context-free grammar, etc.

XGrammar uses careful optimizations to achieve extremely low overhead in structured generation. It has achieved near-zero overhead in JSON generation, making it one of the fastest structured generation engines available.

XGrammar features universal deployment. It supports:

Platforms: Linux, macOS, Windows

Hardware: CPU, NVIDIA GPU, AMD GPU, Apple Silicon, TPU, etc.

Languages: Python, C++, and JavaScript APIs

Models: Qwen, Llama, DeepSeek, Phi, Gemma, etc.

XGrammar is very easy to integrate with LLM inference engines. It is the default structured generation backend for most LLM inference engines, including vLLM, SGLang, TensorRT-LLM, and MLC-LLM, as well as many other companies. You can also try out their structured generation modes!

Get Started

Install XGrammar:

pip install xgrammar

For use with MPS on Apple Silicon, install with:

pip install "xgrammar[metal]"

Import XGrammar:

importxgrammarasxgr

Please visit our documentation to get started with XGrammar.

Installation

Quick start

Third-Party Bindings

Rust: xgrammar-rs — Community Rust bindings for XGrammar.

Collaborators

XGrammar has been widely adopted in industry, open-source projects, and academia. Our collaborators include:

WebLLM

Citation

If you find XGrammar useful in your research, please consider citing our papers:

@article{dong2024xgrammar,
 title={Xgrammar: Flexible and efficient structured generation engine for large language models},
 author={Dong, Yixin and Ruan, Charlie F and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},
 journal={Proceedings of Machine Learning and Systems 7},
 year={2024}
}
@misc{li2026xgrammar2efficientdynamicstructured,
 title={XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs},
 author={Linzhang Li and Yixin Dong and Guanjie Wang and Ziyi Xu and Alexander Jiang and Tianqi Chen},
 year={2026},
 eprint={2601.04426},
 archivePrefix={arXiv},
 primaryClass={cs.AI},
 url={https://arxiv.org/abs/2601.04426},
}

About

 Fast, Flexible and Portable Structured Generation
 

xgrammar.mlc.ai/docs

Topics

 large-language-models

 structured-generation

Resources

 Readme

License

 Apache-2.0 license
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

1.6k
 stars

Watchers

19
 watching

Forks

136
 forks

 Report repository

Releases
 26

v0.1.33
 Latest

Mar 27, 2026

+ 25 releases

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

C++51.7%

Python43.1%

TypeScript3.5%

Cuda0.5%

CMake0.4%

Shell0.3%

Other0.5%

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
