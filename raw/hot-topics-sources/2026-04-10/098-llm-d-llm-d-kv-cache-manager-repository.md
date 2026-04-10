---
title: GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub
source_url: https://github.com/llm-d/llm-d-kv-cache-manager
final_url: https://github.com/llm-d/llm-d-kv-cache
status: 200
content_type: text/html; charset=utf-8
topics: [LMCache-Based Distributed KV Cache Offloading]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.395017+00:00
---

# GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub

## 원본 URL

https://github.com/llm-d/llm-d-kv-cache-manager

## 추출 본문

GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub

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
/llm-d-kv-cachePublic

Notifications
You must be signed in to change notification settings

Fork
 107

 Star
124

Code

Issues54

Pull requests35

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

llm-d/llm-d-kv-cache

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
307 Commits

307 Commits

.github

.github

api

api

benchmarking

benchmarking

deploy

deploy

docs

docs

examples

examples

hack

hack

hooks

hooks

kv_connectors

kv_connectors

pkg

pkg

services/uds_tokenizer

services/uds_tokenizer

tests

tests

vllm-setup-helm

vllm-setup-helm

.clang-format

.clang-format

.dockerignore

.dockerignore

.git-blame-ignore-revs

.git-blame-ignore-revs

.gitattributes

.gitattributes

.gitignore

.gitignore

.golangci.yml

.golangci.yml

.licenserc.yaml

.licenserc.yaml

.pre-commit-config.yaml

.pre-commit-config.yaml

.prowlabels.yaml

.prowlabels.yaml

CODEOWNERS

CODEOWNERS

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

Dockerfile

Dockerfile

LICENSE

LICENSE

Makefile

Makefile

OWNERS

OWNERS

README.md

README.md

_typos.toml

_typos.toml

go.mod

go.mod

go.sum

go.sum

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

KV-Cache

Introduction

Efficiently caching Key & Value (KV) tensors is crucial for optimizing LLM inference.
Reusing the KV-Cache, rather than recomputing it, significantly improves both Time To First Token (TTFT) and overall throughput, while also maximizing system resource-utilization.
As a distributed LLM inference platform, 
llm-d
 provides a comprehensive suite of KV-Cache management capabilities to achieve these goals.

This repository contains the 
llm-d-kv-cache
, a pluggable service designed to enable KV-Cache Aware Routing and lay the foundation for advanced, cross-node cache coordination in vLLM-based serving platforms.

Project Northstar

See the Project Northstar document for a detailed overview of the project's goals and vision.

KV-Cache Indexer Overview

The major component of this project is the KV-Cache Indexer is a high-performance library that keeps a global, near-real-time view of KV-Cache block locality across a fleet of vLLM pods.

It is powered by 
KVEvents
 streamed from vLLM, which provide structured metadata as KV-blocks are created or evicted from a vLLM instance's KV-cache.
This allows the indexer to track which blocks reside on which nodes and on which tier (e.g., GPU or CPU).
This metadata is the foundation for intelligent routing, enabling schedulers to make optimal, KV-cache-aware placement decisions.

The diagram below shows the primary data flows: the Read Path (scoring) and the Write Path (event ingestion).

graph TD
 subgraph "Inference Scheduler"
 A[Scheduler]

 subgraph "KV-Cache"
 B[`kvcache.Indexer`]
 C[`kvblock.Index`]
 D[`kvevents.Pool`]
 end
 end

 subgraph "vLLM Fleet"
 E[vLLM Pod 1]
 F[vLLM Pod 2]
 G[...]
 end

 A--"1: Score(prompt, pods)"-->B
 B--"2: Query Index"-->C
 B--"3: Return Scores"-->A
 
 E--"A: Emit KVEvents"-->D
 F--"A: Emit KVEvents"-->D
 D--"B: Update Index"-->C

Loading

Read Path:

1: Scoring Request: A scheduler asks the KVCache Indexer to score a set of pods for a given prompt

2: Index Query: The indexer calculates the necessary KV-block keys from the prompt and queries the KV-Block Index to see which pods have those blocks

3: Return Scores: The indexer returns a map of pods and their corresponding KV-cache-hit scores to the scheduler

Write Path:

A: Event Ingestion: As vLLM pods create or evict KV-blocks, they emit 
KVEvents
 containing metadata about these changes

B: Index Update: The Event Subscriber consumes these events and updates the KV-Block Index in near-real-time

For a more detailed breakdown, please see the high-level Architecture and the Configuration docs.

Examples

KVCache Indexer:
A reference implementation showing how to run and use the 
kvcache.Indexer
 module

KVCache Aware Scorer:
A reference implementation of how to integrate the 
kvcache.Indexer
 into a scheduler like the 
llm-d-inference-scheduler

KV-Events:
Demonstrates how the KV-Cache libraries handles KV-Events through both an offline example with a dummy ZMQ publisher and an online example using a vLLM Helm chart.

About

 Distributed KV cache scheduling & offloading libraries
 

www.llm-d.ai

Topics

 ai

 incubating

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

124
 stars

Watchers

30
 watching

Forks

107
 forks

 Report repository

Releases
 13

v0.7.1
 Latest

Apr 2, 2026

+ 12 releases

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

Go54.8%

Python25.8%

C++9.7%

Makefile3.6%

C2.4%

Cuda1.1%

Other2.6%

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
