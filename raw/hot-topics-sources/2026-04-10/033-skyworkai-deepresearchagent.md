---
title: GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains. · GitHub
source_url: https://github.com/SkyworkAI/DeepResearchAgent
final_url: https://github.com/SkyworkAI/DeepResearchAgent
status: 200
content_type: text/html; charset=utf-8
topics: [Hierarchical Planning with Agent Trees]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:29.320524+00:00
---

# GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains. · GitHub

## 원본 URL

https://github.com/SkyworkAI/DeepResearchAgent

## 추출 본문

GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains. · GitHub

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

 SkyworkAI
/DeepResearchAgentPublic

Notifications
You must be signed in to change notification settings

Fork
 429

 Star
3.3k

Code

Issues2

Pull requests4

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

SkyworkAI/DeepResearchAgent

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
132 Commits

132 Commits

.github/workflows

.github/workflows

configs

configs

datasets

datasets

docs

docs

examples

examples

libs

libs

src

src

tests

tests

.env.template

.env.template

.gitignore

.gitignore

.gitmodules

.gitmodules

LICENSE

LICENSE

README.md

README.md

README_zh.md

README_zh.md

environment.yml

environment.yml

requirements.txt

requirements.txt

View all files

Repository files navigation

README

MIT license

Autogenesis

English | 中文说明

Autogenesis is a self-evolution protocol and runtime for LLM-based agent systems.

Recent agent protocols often under-specify cross-entity lifecycle/context management, version tracking, and safe evolution update interfaces, which encourages monolithic compositions and brittle glue code. Autogenesis addresses this by decoupling what evolves from how evolution occurs:

RSPL (Resource Substrate Protocol Layer): models prompts, agents, tools, environments, and memory as protocol-registered resources with explicit state, lifecycle, and versioned interfaces.

SEPL (Self Evolution Protocol Layer): specifies a closed-loop operator interface to propose, assess, and commit improvements with auditable lineage and rollback.

Built on Autogenesis, the system includes an Autogenesis-Agent style tool-calling agent that can dynamically instantiate/retrieve/refine resources and improve during execution.

Architecture

Self-evolution at a glance

At a high level, Autogenesis supports an iterative loop:

Act: an agent produces actions/outputs using an LLM and the available tools/environments.

Observe: capture outcomes, traces, intermediate reasoning, and environment feedback.

Optimize: update prompts/solutions/variables using an optimizer (e.g., reflection or RL-style methods).

Remember: persist summaries/insights/records to memory for later steps and sessions.

Core building blocks

Agents (
src/agent/
): runtime logic that decides what to do next (planning, tool-calling, domain agents, etc.).

Tools (
src/tool/
): callable capabilities exposed to agents (workflow tools + default tools).

Environments (
src/environment/
): stateful interfaces that tools/agents can interact with (filesystem, trading backtest envs, browser/mobile envs, etc.).

Memory (
src/memory/
): session/event memory systems for summarization, insights, and long-term state.

Optimizers (
src/optimizer/
): self-improvement algorithms that turn feedback into updated prompts/solutions/variables (reflection, GRPO, Reinforce++, etc.).

Tracing & versioning (
src/tracer/
, 
src/version/
): record trajectories and manage iterative artifacts across runs.

Config system (
configs/
, 
src/config/
): MMEngine-style configs to compose agents/tools/envs/memory/models consistently.

Design goals

Composable: add/replace agents, tools, environments, memory systems, and optimizers without rewriting the whole stack.

Inspectable: structured traces and memory events make it easier to analyze failures and improvement steps.

Evolvable: explicit optimizers + persistent memory enable iterative refinement rather than one-shot inference.

Repository layout

Autogenesis/
 configs/ # config composition (agents/tools/envs/memory/models)
 src/
 agent/ # agents
 environment/ # environments
 tool/ # tools
 memory/ # memory systems
 optimizer/ # self-evolution optimizers
 model/ # model manager + provider backends
 prompt/ # prompt templates / prompt manager
 tracer/ # tracing
 version/ # versioning
 libs/ # vendored libraries
 workdir/ # runtime artifacts (logs, traces, results, etc.)

Empirical studies

See empirical results and benchmark protocols in 
docs/empirical_studies.md
.

Optional: run a Tool-Calling Agent

Prerequisites:

Install dependencies in your environment

Copy 
.env.template
 to 
.env
 and set a model API key (e.g. 
OPENROUTER_API_KEY=...
)

Example:

python examples/run_tool_calling_agent.py --config configs/tool_calling_agent.py

Override model/workdir:

python examples/run_tool_calling_agent.py \
 --config configs/tool_calling_agent.py \
 --cfg-options model_name=openrouter/gpt-4o workdir=workdir/demo tag=demo

About

 DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains.
 

skyworkai.github.io/DeepResearchAgent/

Topics

 gaia

 multiagent-systems

 general-purpose

 multimodel

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

3.3k
 stars

Watchers

24
 watching

Forks

429
 forks

 Report repository

Releases
 2

self evoving
 Latest

Feb 24, 2026

+ 1 release

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

Python99.8%

Other0.2%

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
