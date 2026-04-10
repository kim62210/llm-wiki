---
title: GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub
source_url: https://github.com/kubernetes-sigs/gateway-api-inference-extension
final_url: https://github.com/kubernetes-sigs/gateway-api-inference-extension
status: 200
content_type: text/html; charset=utf-8
topics: [llm-d & Gateway API Inference Extension]
sections: [Infra & Serving]
fetched_at: 2026-04-10T01:44:09.207378+00:00
---

# GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub

## 원본 URL

https://github.com/kubernetes-sigs/gateway-api-inference-extension

## 추출 본문

GitHub - kubernetes-sigs/gateway-api-inference-extension: Gateway API Inference Extension · GitHub

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

 kubernetes-sigs
/gateway-api-inference-extensionPublic

Notifications
You must be signed in to change notification settings

Fork
 278

 Star
639

Code

Issues190

Pull requests35

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

kubernetes-sigs/gateway-api-inference-extension

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
1,669 Commits

1,669 Commits

.github

.github

api

api

apix

apix

benchmarking

benchmarking

client-go

client-go

cmd

cmd

config

config

conformance

conformance

docs

docs

hack

hack

internal

internal

latencypredictor

latencypredictor

pkg

pkg

sidecars/latencypredictorasync

sidecars/latencypredictorasync

site-src

site-src

test

test

tools

tools

version

version

.custom-gcl.yml

.custom-gcl.yml

.dockerignore

.dockerignore

.gitignore

.gitignore

.golangci-kal.yml

.golangci-kal.yml

.golangci.yml

.golangci.yml

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

OWNERS_ALIASES

OWNERS_ALIASES

PROJECT

PROJECT

README.md

README.md

RELEASE.md

RELEASE.md

SECURITY.md

SECURITY.md

SECURITY_CONTACTS

SECURITY_CONTACTS

bbr.Dockerfile

bbr.Dockerfile

cloudbuild.yaml

cloudbuild.yaml

code-of-conduct.md

code-of-conduct.md

crd-ref-docs.yaml

crd-ref-docs.yaml

go.mod

go.mod

go.sum

go.sum

go.work

go.work

mkdocs.yml

mkdocs.yml

netlify.toml

netlify.toml

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

Gateway API Inference Extension

Gateway API Inference Extension optimizes self-hosting Generative Models on Kubernetes.
This is achieved by leveraging Envoy's External Processing (ext-proc) to extend any gateway that supports both ext-proc and Gateway API into an inference gateway.

New!

Inference Gateway has partnered with vLLM to accelerate LLM serving optimizations with llm-d!

Concepts and Definitions

The following specific terms to this project:

Inference Gateway (IGW): A proxy/load-balancer which has been coupled with an

Endpoint Picker
. It provides optimized routing and load balancing for
serving Kubernetes self-hosted generative Artificial Intelligence (AI)
workloads. It simplifies the deployment, management, and observability of AI
inference workloads.

Inference Scheduler: An extendable component that makes decisions about which endpoint is optimal (best cost /
best performance) for an inference request based on 
Metrics and Capabilities

from Model Serving.

Metrics and Capabilities: Data provided by model serving platforms about
performance, availability and capabilities to optimize routing. Includes
things like Prefix Cache status or LoRA Adapters availability.

Endpoint Picker(EPP): An implementation of an 
Inference Scheduler
 with additional Routing, Flow, and Request Control layers to allow for sophisticated routing strategies. Additional info on the architecture of the EPP here.

Body Based Router(BBR): An optional additional ext-proc server that parses the http body of the inference prompt message and extracts information (currently the model name for OpenAI API style messages) into a format which can then be used by the gateway for routing purposes. Additional info here and in the documentation user guides.

The following are key industry terms that are important to understand for
this project:

Model: A generative AI model that has learned patterns from data and is
used for inference. Models vary in size and architecture, from smaller
domain-specific models to massive multi-billion parameter neural networks that
are optimized for diverse language tasks.

Inference: The process of running a generative AI model, such as a large
language model, diffusion model etc, to generate text, embeddings, or other
outputs from input data.

Model server: A service (in our case, containerized) responsible for
receiving inference requests and returning predictions from a model.

Accelerator: specialized hardware, such as Graphics Processing Units
(GPUs) that can be attached to Kubernetes nodes to speed up computations,
particularly for training and inference tasks.

For deeper insights and more advanced concepts, refer to our proposals.

Technical Overview

This extension upgrades an ext-proc capable proxy or gateway - such as Envoy Gateway, kgateway, or the GKE Gateway - to become an inference gateway - supporting inference platform teams self-hosting Generative Models (with a current focus on large language models) on Kubernetes. This integration makes it easy to expose and control access to your local OpenAI-compatible chat completion endpoints to other workloads on or off cluster, or to integrate your self-hosted models alongside model-as-a-service providers in a higher level AI Gateway like LiteLLM, Solo AI Gateway, or Apigee.

The Inference Gateway:

Improves the tail latency and throughput of LLM completion requests against Kubernetes-hosted model servers using an extensible request scheduling algorithm that is kv-cache and request cost aware, avoiding evictions or queueing as load increases

Provides Kubernetes-native declarative APIs to route client model names to use-case specific LoRA adapters and control incremental rollout of new adapter versions, A/B traffic splitting, and safe blue-green base model and model server upgrades

Adds end to end observability around service objective attainment

Ensures operational guardrails between different client model names, allowing a platform team to safely serve many different GenAI workloads on the same pool of shared foundation model servers for higher utilization and fewer required accelerators

Model Server Integration

IGW’s pluggable architecture was leveraged to enable the llm-d Inference Scheduler.

Llm-d customizes vLLM & IGW to create a disaggregated serving solution. We've worked closely with this team to enable this integration. IGW will continue to work closely with llm-d to generalize the disaggregated serving plugin(s), & set a standard for disaggregated serving to be used across any protocol-adherent model server.

IGW has enhanced support for vLLM via llm-d, and broad support for any model servers implementing the protocol. More details can be found in model server integration.

Status

This project is GA'd! The latest release can be found here.

Please file any bugs or feature requests you have. We are always happy to welcome new collaborators and users.

Getting Started

Follow our Getting Started Guide to get the inference-extension up and running on your cluster!

See our website for detailed API documentation on leveraging our Kubernetes-native declarative APIs

Roadmap

As Inference Gateway builds towards a GA release. We will continue to expand our capabilities, namely:

Prefix-cache aware load balancing with interfaces for remote caches

Recommended LoRA adapter pipeline for automated rollout

Fairness and priority between workloads within the same criticality band

HPA support for autoscaling on aggregate metrics derived from the load balancer

Support for large multi-modal inputs and outputs

Support for other GenAI model types (diffusion and other non-completion protocols)

Heterogeneous accelerators - serve workloads on multiple types of accelerator using latency and request cost-aware load balancing

Disaggregated serving support with independently scaling pools

End-to-End Tests

Follow this README to learn more about running the inference-extension end-to-end test suite on your cluster.

Contributing

Our community meeting is weekly at Thursday 10AM PDT (Zoom, Meeting Notes).

We currently utilize the #gateway-api-inference-extension channel in Kubernetes Slack workspace for communications.

Contributions are readily welcomed, follow the dev guide to start contributing!

Code of conduct

Participation in the Kubernetes community is governed by the Kubernetes Code of Conduct.

About

 Gateway API Inference Extension
 

gateway-api-inference-extension.sigs.k8s.io/

Topics

 k8s-sig-network

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

639
 stars

Watchers

20
 watching

Forks

278
 forks

 Report repository

Releases
 38

v1.4.0
 Latest

Mar 20, 2026

+ 37 releases

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

Go65.5%

Jupyter Notebook24.9%

Python7.0%

Makefile1.1%

Shell1.1%

Go Template0.2%

Other0.2%

 Generated from kubernetes/kubernetes-template-project

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
