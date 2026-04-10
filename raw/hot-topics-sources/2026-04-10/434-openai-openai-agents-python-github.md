---
title: GitHub - openai/openai-agents-python: A lightweight, powerful framework for multi-agent workflows · GitHub
source_url: https://github.com/openai/openai-agents-python
final_url: https://github.com/openai/openai-agents-python
status: 200
content_type: text/html; charset=utf-8
topics: [OpenAI Agents SDK]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:27.860440+00:00
---

# GitHub - openai/openai-agents-python: A lightweight, powerful framework for multi-agent workflows · GitHub

## 원본 URL

https://github.com/openai/openai-agents-python

## 추출 본문

GitHub - openai/openai-agents-python: A lightweight, powerful framework for multi-agent workflows · GitHub

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

 openai
/openai-agents-pythonPublic

Notifications
You must be signed in to change notification settings

Fork
 3.4k

 Star
20.7k

Code

Issues65

Pull requests13

Actions

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Security and quality

 Insights

openai/openai-agents-python

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
1,319 Commits

1,319 Commits

.agents/skills

.agents/skills

.codex

.codex

.github

.github

.vscode

.vscode

docs

docs

examples

examples

src/agents

src/agents

tests

tests

.gitignore

.gitignore

.prettierrc

.prettierrc

AGENTS.md

AGENTS.md

CLAUDE.md

CLAUDE.md

LICENSE

LICENSE

Makefile

Makefile

PLANS.md

PLANS.md

README.md

README.md

mkdocs.yml

mkdocs.yml

pyproject.toml

pyproject.toml

pyrightconfig.json

pyrightconfig.json

uv.lock

uv.lock

View all files

Repository files navigation

README

MIT license

OpenAI Agents SDK 

The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agnostic, supporting the OpenAI Responses and Chat Completions APIs, as well as 100+ other LLMs.

Note

Looking for the JavaScript/TypeScript version? Check out Agents SDK JS/TS.

Core concepts:

Agents: LLMs configured with instructions, tools, guardrails, and handoffs

Agents as tools / Handoffs: Delegating to other agents for specific tasks

Tools: Various Tools let agents take actions (functions, MCP, hosted tools)

Guardrails: Configurable safety checks for input and output validation

Human in the loop: Built-in mechanisms for involving humans across agent runs

Sessions: Automatic conversation history management across agent runs

Tracing: Built-in tracking of agent runs, allowing you to view, debug and optimize your workflows

Realtime Agents: Build powerful voice agents with 
gpt-realtime-1.5
 and full agent features

Explore the examples directory to see the SDK in action, and read our documentation for more details.

Get started

To get started, set up your Python environment (Python 3.10 or newer required), and then install OpenAI Agents SDK package.

venv

python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
pip install openai-agents

For voice support, install with the optional 
voice
 group: 
pip install 'openai-agents[voice]'
. For Redis session support, install with the optional 
redis
 group: 
pip install 'openai-agents[redis]'
.

uv

If you're familiar with uv, installing the package would be even easier:

uv init
uv add openai-agents

For voice support, install with the optional 
voice
 group: 
uv add 'openai-agents[voice]'
. For Redis session support, install with the optional 
redis
 group: 
uv add 'openai-agents[redis]'
.

Run your first agent

fromagentsimportAgent, Runneragent=Agent(name="Assistant", instructions="You are a helpful assistant")

result=Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,# Functions calling themselves,# Infinite loop's dance.

(If running this, ensure you set the 
OPENAI_API_KEY
 environment variable)

(For Jupyter notebook users, see hello_world_jupyter.ipynb)

Explore the examples directory to see the SDK in action, and read our documentation for more details.

Acknowledgements

We'd like to acknowledge the excellent work of the open-source community, especially:

Pydantic

Requests

MCP Python SDK

Griffe

This library has these optional dependencies:

websockets

SQLAlchemy

any-llm and LiteLLM

We also rely on the following tools to manage the project:

uv and ruff

mypy and Pyright

pytest and Coverage.py

MkDocs

We're committed to continuing to build the Agents SDK as an open source framework so others in the community can expand on our approach.

About

 A lightweight, powerful framework for multi-agent workflows
 

openai.github.io/openai-agents-python/

Topics

 python

 framework

 ai

 openai

 agents

 llm

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

20.7k
 stars

Watchers

190
 watching

Forks

3.4k
 forks

 Report repository

Releases
 81

v0.13.6
 Latest

Apr 9, 2026

+ 80 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.6%

Other0.4%

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
