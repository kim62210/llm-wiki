---
title: GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub
source_url: https://github.com/Arize-ai/phoenix
final_url: https://github.com/Arize-ai/phoenix
status: 200
content_type: text/html; charset=utf-8
topics: [Tool Selection & Tool Invocation Evaluators, Production Observability Platforms Convergence]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:59.955626+00:00
---

# GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub

## 원본 URL

https://github.com/Arize-ai/phoenix

## 추출 본문

GitHub - Arize-ai/phoenix: AI Observability & Evaluation · GitHub

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

 Arize-ai
/phoenixPublic

Notifications
You must be signed in to change notification settings

Fork
 801

 Star
9.2k

Code

Issues449

Pull requests55

Discussions

Actions

Projects

Wiki

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Wiki

 Security and quality

 Insights

Arize-ai/phoenix

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
8,186 Commits

8,186 Commits

.agents/skills

.agents/skills

.claude

.claude

.codex

.codex

.cursor

.cursor

.github

.github

.tours

.tours

.vscode

.vscode

api_reference

api_reference

app

app

docs

docs

examples

examples

helm

helm

internal_docs

internal_docs

js

js

kustomize

kustomize

packages

packages

prompts

prompts

requirements

requirements

schemas

schemas

scripts

scripts

src/phoenix

src/phoenix

styles/config/vocabularies/Mintlify

styles/config/vocabularies/Mintlify

tests

tests

tutorials

tutorials

.dockerignore

.dockerignore

.editorconfig

.editorconfig

.eslintignore

.eslintignore

.git-blame-ignore-revs

.git-blame-ignore-revs

.gitignore

.gitignore

.mintignore

.mintignore

.nvmrc

.nvmrc

.oxfmtrc.jsonc

.oxfmtrc.jsonc

.oxlintrc.json

.oxlintrc.json

.pre-commit-config.yaml

.pre-commit-config.yaml

.prettierignore

.prettierignore

.python-version

.python-version

.readthedocs.yaml

.readthedocs.yaml

.release-please-manifest.json

.release-please-manifest.json

.vale.ini

.vale.ini

AGENTS.md

AGENTS.md

CHANGELOG.md

CHANGELOG.md

CLA.md

CLA.md

CLAUDE.md

CLAUDE.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

DEVELOPMENT.md

DEVELOPMENT.md

Dockerfile

Dockerfile

IP_NOTICE

IP_NOTICE

LICENSE

LICENSE

MIGRATION.md

MIGRATION.md

Makefile

Makefile

README.md

README.md

REVIEW.md

REVIEW.md

SECURITY.md

SECURITY.md

cspell.json

cspell.json

docker-compose.yml

docker-compose.yml

docs.json

docs.json

pyment.conf

pyment.conf

pyproject.toml

pyproject.toml

pytest-quiet.ini

pytest-quiet.ini

release-please-config.json

release-please-config.json

sitemap.xml

sitemap.xml

tox.ini

tox.ini

uv.lock

uv.lock

View all files

Repository files navigation

README

Code of conduct

Contributing

License

Security

Phoenix is an open-source AI observability platform designed for experimentation, evaluation, and troubleshooting. It provides:

Tracing - Trace your LLM application's runtime using OpenTelemetry-based instrumentation.

Evaluation - Leverage LLMs to benchmark your application's performance using response and retrieval evals.

Datasets - Create versioned datasets of examples for experimentation, evaluation, and fine-tuning.

Experiments - Track and evaluate changes to prompts, LLMs, and retrieval.

Playground- Optimize prompts, compare models, adjust parameters, and replay traced LLM calls.

Prompt Management- Manage and test prompt changes systematically using version control, tagging, and experimentation.

Phoenix is vendor and language agnostic with out-of-the-box support for popular frameworks (OpenAI Agents SDK, Claude Agent SDK, LangGraph, Vercel AI SDK, Mastra, CrewAI, LlamaIndex, DSPy) and LLM providers (OpenAI, Anthropic, Google GenAI, Google ADK, AWS Bedrock, OpenRouter, LiteLLM, and more). For details on auto-instrumentation, check out the OpenInference project.

Phoenix runs practically anywhere, including your local machine, a Jupyter notebook, a containerized deployment, or in the cloud.

Installation

Install Phoenix via 
pip
 or 
conda

pip install arize-phoenix

Phoenix container images are available via Docker Hub and can be deployed using Docker or Kubernetes. Arize AI also provides cloud instances at app.phoenix.arize.com.

Packages

The 
arize-phoenix
 package includes the entire Phoenix platform. However, if you have deployed the Phoenix platform, there are lightweight Python sub-packages and TypeScript packages that can be used in conjunction with the platform.

Python Subpackages

PackageVersion & DocsDescriptionarize-phoenix-otelProvides a lightweight wrapper around OpenTelemetry primitives with Phoenix-aware defaultsarize-phoenix-clientLightweight client for interacting with the Phoenix server via its OpenAPI REST interfacearize-phoenix-evalsTooling to evaluate LLM applications including RAG relevance, answer relevance, and more

TypeScript Subpackages

PackageVersion & DocsDescription@arizeai/phoenix-otelProvides a lightweight wrapper around OpenTelemetry primitives with Phoenix-aware defaults@arizeai/phoenix-clientClient for the Arize Phoenix API@arizeai/phoenix-evalsTypeScript evaluation library for LLM applications (alpha release)@arizeai/phoenix-mcpMCP server implementation for Arize Phoenix providing unified interface to Phoenix's capabilities@arizeai/phoenix-cliCLI for fetching traces, datasets, and experiments for use with Claude Code, Cursor, and other coding agents

Tracing Integrations

Phoenix is built on top of OpenTelemetry and is vendor, language, and framework agnostic. For details about tracing integrations and example applications, see the OpenInference project.

Python Integrations
IntegrationPackageVersionOpenAI
openinference-instrumentation-openai
OpenAI Agents
openinference-instrumentation-openai-agents
LlamaIndex
openinference-instrumentation-llama-index
DSPy
openinference-instrumentation-dspy
AWS Bedrock
openinference-instrumentation-bedrock
LangChain
openinference-instrumentation-langchain
MistralAI
openinference-instrumentation-mistralai
Google GenAI
openinference-instrumentation-google-genai
Google ADK
openinference-instrumentation-google-adk
Guardrails
openinference-instrumentation-guardrails
VertexAI
openinference-instrumentation-vertexai
CrewAI
openinference-instrumentation-crewai
Haystack
openinference-instrumentation-haystack
LiteLLM
openinference-instrumentation-litellm
Groq
openinference-instrumentation-groq
Instructor
openinference-instrumentation-instructor
Anthropic
openinference-instrumentation-anthropic
Smolagents
openinference-instrumentation-smolagents
Agno
openinference-instrumentation-agno
MCP
openinference-instrumentation-mcp
Pydantic AI
openinference-instrumentation-pydantic-ai
Autogen AgentChat
openinference-instrumentation-autogen-agentchat
Portkey
openinference-instrumentation-portkey
Agent Spec
openinference-instrumentation-agentspec
Claude Agent SDK
openinference-instrumentation-claude-agent-sdk

Span Processors

Normalize and convert data across other instrumentation libraries by adding span processors that unify data.
PackageDescriptionVersion
openinference-instrumentation-openlit
OpenInference Span Processor for OpenLIT traces.
openinference-instrumentation-openllmetry
OpenInference Span Processor for OpenLLMetry (Traceloop) traces.

JavaScript Integrations

IntegrationPackageVersionOpenAI
@arizeai/openinference-instrumentation-openai
LangChain.js
@arizeai/openinference-instrumentation-langchain
Vercel AI SDK
@arizeai/openinference-vercel
BeeAI
@arizeai/openinference-instrumentation-beeai
Claude Agent SDK
@arizeai/openinference-instrumentation-claude-agent-sdk
Mastra
@mastra/arize
MCP
@arizeai/openinference-instrumentation-mcp

Java Integrations

IntegrationPackageVersionLangChain4j
openinference-instrumentation-langchain4j
SpringAI
openinference-instrumentation-springAI
Arconia
openinference-instrumentation-springAI

Platforms

PlatformDescriptionDocsBeeAIAI agent framework with built-in observabilityIntegration GuideDifyOpen-source LLM app development platformIntegration GuideEnvoy AI GatewayAI Gateway built on Envoy Proxy for AI workloadsIntegration GuideLangFlowVisual framework for building multi-agent and RAG applicationsIntegration GuideLiteLLM ProxyProxy server for LLMsIntegration GuideFlowiseVisual framework for building LLM applicationsIntegration GuidePrompt FlowMicrosoft's prompt flow orchestration toolIntegration GuideNVIDIA NeMoNVIDIA NeMo Agent Toolkit for enterprise agentsIntegration GuideGraphiteMulti-agent LLM workflow framework with visual builderIntegration Guide

Coding Agent Skills

This repository includes skills that teach coding agents how to work with Phoenix. They are located in 
.agents/skills/
 and can be used with Claude Code, Cursor, and other compatible tools.
SkillDescriptionphoenix-cliDebug LLM applications using the Phoenix CLI — fetch traces, analyze errors, review experiments, and query the GraphQL APIphoenix-evalsBuild and run evaluators for AI/LLM applications using Phoenixphoenix-tracingOpenInference semantic conventions and instrumentation for tracing LLM applications

Security & Privacy

We take data security and privacy very seriously. For more details, see our Security and Privacy documentation.

Telemetry

By default, Phoenix collects basic web analytics (e.g., page views, UI interactions) to help us understand how Phoenix is used and improve the product. None of your trace data, evaluation results, or any sensitive information is ever collected.

You can opt-out of telemetry by setting the environment variable: 
PHOENIX_TELEMETRY_ENABLED=false

Community

Join our community to connect with thousands of AI builders.

🌍 Join our Slack community.

📚 Read our documentation.

💡 Ask questions and provide feedback in the #phoenix-support channel.

🌟 Leave a star on our GitHub.

🐞 Report bugs with GitHub Issues.

𝕏 Follow us on 𝕏.

🗺️ Check out our roadmap to see where we're heading next.

🧑‍🏫 Deep dive into everything Agents and LLM Evaluations on Arize's Learning Hubs.

Breaking Changes

See the migration guide for a list of breaking changes.

Copyright, Patent, and License

Copyright 2025 Arize AI, Inc. All Rights Reserved.

Portions of this code are patent protected by one or more U.S. Patents. See the IP_NOTICE.

This software is licensed under the terms of the Elastic License 2.0 (ELv2). See LICENSE.

About

 AI Observability & Evaluation
 

arize.com/docs/phoenix

Topics

 openai

 datasets

 agents

 ai-monitoring

 ai-observability

 prompt-engineering

 llms

 langchain

 llmops

 anthropic

 llamaindex

 llm-eval

 evals

 llm-evaluation

 aiengineering

 smolagents

Resources

 Readme

License

 View license
 

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

9.2k
 stars

Watchers

52
 watching

Forks

801
 forks

 Report repository

Releases
 660

arize-phoenix: v14.1.1
 Latest

Apr 8, 2026

+ 659 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Jupyter Notebook39.7%

Python34.5%

TypeScript25.3%

Shell0.1%

JavaScript0.1%

PLpgSQL0.1%

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
