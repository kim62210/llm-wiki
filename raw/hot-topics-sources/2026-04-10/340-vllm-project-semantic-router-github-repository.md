---
title: GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub
source_url: https://github.com/vllm-project/semantic-router
final_url: https://github.com/vllm-project/semantic-router
status: 200
content_type: text/html; charset=utf-8
topics: [vLLM Semantic Router (Iris / Athena)]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:10.589533+00:00
---

# GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub

## 원본 URL

https://github.com/vllm-project/semantic-router

## 추출 본문

GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub

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
/semantic-routerPublic

Notifications
You must be signed in to change notification settings

Fork
 605

 Star
3.7k

Code

Issues92

Pull requests77

Discussions

Actions

Projects

Security and quality0

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

vllm-project/semantic-router

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
1,258 Commits

1,258 Commits

.agents/skills/harness

.agents/skills/harness

.github

.github

bench

bench

candle-binding

candle-binding

config

config

dashboard

dashboard

deploy

deploy

docs

docs

e2e

e2e

ml-binding

ml-binding

nlp-binding

nlp-binding

onnx-binding

onnx-binding

paper

paper

perf

perf

scripts

scripts

src

src

tools

tools

website

website

.crd-ref-docs.yaml

.crd-ref-docs.yaml

.dockerignore

.dockerignore

.editorconfig

.editorconfig

.gitattributes

.gitattributes

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

.prowlabels.yaml

.prowlabels.yaml

AGENTS.md

AGENTS.md

CODEOWNERS

CODEOWNERS

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

GOVERNANCE.md

GOVERNANCE.md

LICENSE

LICENSE

Makefile

Makefile

OWNER

OWNER

README.md

README.md

install.sh

install.sh

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

Documentation |
 Playground |
 Blog |
 Publications |
 Hugging Face

About

In the LLM era, the number of models is exploding. Different models vary across capability, scale, cost, and privacy boundaries. Choosing and connecting the right models to build semantic AI infrastructure is a system problem.

vLLM Semantic Router is a signal-driven intelligent router for that problem. It helps teams build model systems that are more efficient, safer, and more adaptive across cloud, data center, and edge environments.

It delivers three core values:

Token economics: reduce wasted tokens, increase effective output, and maximize the value of every token.

LLM safety: detect jailbreaks, sensitive leakage, and hallucinations so agents remain controllable, trustworthy, and auditable.

Fullmesh intelligence: build personal AI at the edge and intelligent MaaS in the cloud by coordinating local, private, and frontier models across cost, privacy, and capability boundaries.

Getting Started

Install

curl -fsSL https://vllm-semantic-router.com/install.sh | bash

For platform notes, detailed setup options, and troubleshooting, see the Installation Guide.

Important

Online playground default credentials:

username: 
love@vllm-sr.ai

password: 
vllm-sr

Latest News

[2026/03/24] Vision Paper Released: The Workload-Router-Pool Architecture for LLM Inference Optimization

[2026/03/10] v0.2 Released: vLLM Semantic Router v0.2 Athena Release

[2026/02/27] White Paper Released: Signal Driven Decision Routing for Mixture-of-Modality Models

[2026/01/05] Iris v0.1 Released: vLLM Semantic Router v0.1 Iris: The First Major Release

[2025/12/16] Collaboration: AMD × vLLM Semantic Router: Building the System Intelligence Together

[2025/11/19] New Blog: Signal-Decision Driven Architecture: Reshaping Semantic Routing at Scale

[2025/11/03] Paper Published: Category-Aware Semantic Caching for Heterogeneous LLM Workloads

[2025/10/12] Paper Accepted: When to Reason: Semantic Router for vLLM
Earlier announcements
[2025/12/15] New Blog: Token-Level Truth: Real-Time Hallucination Detection for Production LLMs

[2025/10/27] New Blog: Scaling Semantic Routing with Extensible LoRA

[2025/10/08] Collaboration: vLLM Semantic Router with vLLM Production Stack Team.

[2025/09/01] Released the project: vLLM Semantic Router: Next Phase in LLM inference.

More announcements are available on the Blog and Publications pages.

Community

For questions, feedback, or to contribute, please join the 
#semantic-router
 channel in vLLM Slack.

Community Meetings

We host bi-weekly community meetings to sync with contributors across different time zones:

First Tuesday of the month: 9:00-10:00 AM EST (accommodates US EST, EU, and Asia Pacific contributors)

Zoom Link

Google Calendar Invite

ics file

Third Tuesday of the month: 1:00-2:00 PM EST (accommodates US EST and California contributors)

Zoom Link

Google Calendar Invite

ics file

Meeting recordings: YouTube

Contributing

If you want to contribute, start with CONTRIBUTING.md.

For repository-native development workflow and validation commands, use AGENTS.md as the entrypoint and docs/agent/README.md as the canonical index.

Citation

If you find Semantic Router helpful in your research or projects, please consider citing it:

@misc{semanticrouter2025,
 title={vLLM Semantic Router},
 author={vLLM Semantic Router Team},
 year={2025},
 howpublished={\url{https://github.com/vllm-project/semantic-router}},
}

Star History

Sponsors

We are grateful to our sponsors who support us:

AMD provides us with GPU resources and ROCm™ software for training and researching frontier router models, enhancing E2E testing, and building the online models playground.

About

 System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge
 

vllm-semantic-router.com

Topics

 kubernetes

 rust

 golang

 mcp

 fine-tuning

 pii-detection

 mixture-of-models

 huggingface-transformers

 bert-classification

 llm

 prompt-engineering

 vllm

 huggingface-candle

 ai-gateway

 semantic-router

 prompt-guard

 llmrouter

 openclaw

Resources

 Readme

License

 Apache-2.0 license
 

Code of conduct

 Code of conduct
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

3.7k
 stars

Watchers

58
 watching

Forks

605
 forks

 Report repository

Releases
 2

v0.2.0 - Athena
 Latest

Mar 10, 2026

+ 1 release

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Go42.6%

Python18.6%

TypeScript15.0%

Rust11.8%

CSS4.2%

Shell3.0%

Other4.8%

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
