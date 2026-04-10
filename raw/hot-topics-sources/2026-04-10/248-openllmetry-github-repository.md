---
title: GitHub - traceloop/openllmetry: Open-source observability for your GenAI or LLM application, based on OpenTelemetry · GitHub
source_url: https://github.com/traceloop/openllmetry
final_url: https://github.com/traceloop/openllmetry
status: 200
content_type: text/html; charset=utf-8
topics: [OpenTelemetry GenAI Semantic Conventions]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.775100+00:00
---

# GitHub - traceloop/openllmetry: Open-source observability for your GenAI or LLM application, based on OpenTelemetry · GitHub

## 원본 URL

https://github.com/traceloop/openllmetry

## 추출 본문

GitHub - traceloop/openllmetry: Open-source observability for your GenAI or LLM application, based on OpenTelemetry · GitHub

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

 traceloop
/openllmetryPublic

Notifications
You must be signed in to change notification settings

Fork
 920

 Star
7k

Code

Issues123

Pull requests331

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

traceloop/openllmetry

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
1,352 Commits

1,352 Commits

.github

.github

img

img

packages

packages

scripts

scripts

.cz.toml

.cz.toml

.gitignore

.gitignore

CHANGELOG.md

CHANGELOG.md

CLAUDE.md

CLAUDE.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

GOVERNANCE.md

GOVERNANCE.md

LICENSE

LICENSE

MAINTAINERS.md

MAINTAINERS.md

README.md

README.md

SECURITY.md

SECURITY.md

nx.json

nx.json

package-lock.json

package-lock.json

package.json

package.json

View all files

Repository files navigation

README

Code of conduct

Contributing

Apache-2.0 license

Security

Open-source observability for your LLM application

Get started »

Slack |
 Docs |
 Website

🎉 New:
Our semantic conventions are now part of OpenTelemetry! Join the discussion and help us shape the future of LLM observability.

Looking for the JS/TS version? Check out OpenLLMetry-JS.

OpenLLMetry is a set of extensions built on top of OpenTelemetry that gives you complete observability over your LLM application. Because it uses OpenTelemetry under the hood, it can be connected to your existing observability solutions - Datadog, Honeycomb, and others.

It's built and maintained by Traceloop under the Apache 2.0 license.

The repo contains standard OpenTelemetry instrumentations for LLM providers and Vector DBs, as well as a Traceloop SDK that makes it easy to get started with OpenLLMetry, while still outputting standard OpenTelemetry data that can be connected to your observability stack.
If you already have OpenTelemetry instrumented, you can just add any of our instrumentations directly.

🚀 Getting Started

The easiest way to get started is to use our SDK.
For a complete guide, go to our docs.

Install the SDK:

pip install traceloop-sdk

Then, to start instrumenting your code, just add this line to your code:

fromtraceloop.sdkimportTraceloopTraceloop.init()

That's it. You're now tracing your code with OpenLLMetry!
If you're running this locally, you may want to disable batch sending, so you can see the traces immediately:

Traceloop.init(disable_batch=True)

⏫ Supported (and tested) destinations

✅ Traceloop

✅ Axiom

✅ Azure Application Insights

✅ Braintrust

✅ Dash0

✅ Datadog

✅ Dynatrace

✅ Google Cloud

✅ Grafana

✅ Highlight

✅ Honeycomb

✅ HyperDX

✅ IBM Instana

✅ KloudMate

✅ Laminar

✅ New Relic

✅ OpenTelemetry Collector

✅ Oracle Cloud

✅ Scorecard

✅ Service Now Cloud Observability

✅ SigNoz

✅ Sentry

✅ Splunk

✅ Tencent Cloud

See our docs for instructions on connecting to each one.

🪗 What do we instrument?

OpenLLMetry can instrument everything that OpenTelemetry already instruments - so things like your DB, API calls, and more. On top of that, we built a set of custom extensions that instrument things like your calls to OpenAI or Anthropic, or your Vector DB like Chroma, Pinecone, Qdrant or Weaviate.

✅ Aleph Alpha

✅ Anthropic

✅ Bedrock (AWS)

✅ Cohere

✅ Google Generative AI (Gemini)

✅ Groq

✅ HuggingFace

✅ IBM Watsonx AI

✅ Mistral AI

✅ Ollama

✅ OpenAI / Azure OpenAI

✅ Replicate

✅ SageMaker (AWS)

✅ Together AI

✅ Vertex AI (GCP)

✅ WRITER

Vector DBs

✅ Chroma

✅ LanceDB

✅ Marqo

✅ Milvus

✅ Pinecone

✅ Qdrant

✅ Weaviate

Frameworks

✅ Agno

✅ AWS Strands (built-in OTEL support)

✅ CrewAI

✅ Haystack

✅ LangChain

✅ Langflow

✅ LangGraph

✅ LiteLLM

✅ LlamaIndex

✅ OpenAI Agents

Protocol

✅ MCP

🔎 Telemetry

We no longer log or collect any telemetry in the SDK or in the instrumentations. Make sure to bump to v0.49.2 and above.

Why we collect telemetry

The primary purpose is to detect exceptions within instrumentations. Since LLM providers frequently update their APIs, this helps us quickly identify and fix any breaking changes.

We only collect anonymous data, with no personally identifiable information. You can view exactly what data we collect in our Privacy documentation.

Telemetry is only collected in the SDK. If you use the instrumentations directly without the SDK, no telemetry is collected.

🌱 Contributing

Whether big or small, we love contributions ❤️ Check out our guide to see how to get started.

Not sure where to get started? You can:

Book a free pairing session with one of our teammates!

Join our Slack, and ask us any questions there.

💚 Community & Support

Slack (For live discussion with the community and the Traceloop team)

GitHub Discussions (For help with building and deeper conversations about features)

GitHub Issues (For any bugs and errors you encounter using OpenLLMetry)

Twitter (Get news fast)

🙏 Special Thanks

To @patrickdebois, who suggested the great name we're now using for this repo!

💫 Contributors

About

 Open-source observability for your GenAI or LLM application, based on OpenTelemetry
 

www.traceloop.com/openllmetry

Topics

 python

 open-source

 monitoring

 metrics

 ml

 datascience

 help-wanted

 observability

 good-first-issue

 artifical-intelligence

 model-monitoring

 opentelemetry

 open-telemetry

 opentelemetry-python

 llm

 good-first-issues

 generative-ai

 llmops

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

7k
 stars

Watchers

21
 watching

Forks

920
 forks

 Report repository

Releases
 252

0.58.0
 Latest

Apr 9, 2026

+ 251 releases

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
