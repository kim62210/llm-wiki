---
title: GitHub - langchain-ai/deepagents: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. · GitHub
source_url: https://github.com/langchain-ai/deepagents
final_url: https://github.com/langchain-ai/deepagents
status: 200
content_type: text/html; charset=utf-8
topics: [Deep Agents (LangChain Harness for Long-Running Tasks)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:23.770457+00:00
---

# GitHub - langchain-ai/deepagents: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. · GitHub

## 원본 URL

https://github.com/langchain-ai/deepagents

## 추출 본문

GitHub - langchain-ai/deepagents: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. · GitHub

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

 langchain-ai
/deepagentsPublic

Notifications
You must be signed in to change notification settings

Fork
 2.8k

 Star
20.1k

Code

Issues151

Pull requests71

Discussions

Actions

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Security and quality

 Insights

langchain-ai/deepagents

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
1,413 Commits

1,413 Commits

.github

.github

.vscode

.vscode

examples

examples

libs

libs

.gitignore

.gitignore

.markdownlint.json

.markdownlint.json

.mcp.json

.mcp.json

.pre-commit-config.yaml

.pre-commit-config.yaml

.release-please-manifest.json

.release-please-manifest.json

AGENTS.md

AGENTS.md

LICENSE

LICENSE

README.md

README.md

action.yml

action.yml

deepagents-deploy.md

deepagents-deploy.md

release-please-config.json

release-please-config.json

View all files

Repository files navigation

README

Code of conduct

Contributing

MIT license

Security

The batteries-included agent harness.

Deep Agents is an agent harness. An opinionated, ready-to-run agent out of the box. Instead of wiring up prompts, tools, and context management yourself, you get a working agent immediately and customize what you need.

What's included:

Planning — 
write_todos
 for task breakdown and progress tracking

Filesystem — 
read_file
, 
write_file
, 
edit_file
, 
ls
, 
glob
, 
grep
 for reading and writing context

Shell access — 
execute
 for running commands (with sandboxing)

Sub-agents — 
task
 for delegating work with isolated context windows

Smart defaults — Prompts that teach the model how to use these tools effectively

Context management — Auto-summarization when conversations get long, large outputs saved to files

Note

Looking for the JS/TS library? Check out deepagents.js.

Quickstart

pip install deepagents
# or
uv add deepagents

fromdeepagentsimportcreate_deep_agentagent=create_deep_agent()
result=agent.invoke({"messages": [{"role": "user", "content": "Research LangGraph and write a summary"}]})

The agent can plan, read/write files, and manage its own context. Add tools, customize prompts, or swap models as needed.

Tip

For developing, debugging, and deploying AI agents and LLM applications, see LangSmith.

Customization

Add your own tools, swap models, customize prompts, configure sub-agents, and more. See the documentation for full details.

fromlangchain.chat_modelsimportinit_chat_modelagent=create_deep_agent(
 model=init_chat_model("openai:gpt-4o"),
 tools=[my_custom_tool],
 system_prompt="You are a research assistant.",
)

MCP is supported via 
langchain-mcp-adapters
.

Deep Agents CLI

A pre-built coding agent in your terminal — similar to Claude Code or Cursor — powered by any LLM. One install command and you're up and running.

curl -LsSf https://raw.githubusercontent.com/langchain-ai/deepagents/main/libs/cli/scripts/install.sh | bash

Highlights:

Interactive TUI — rich terminal interface with streaming responses

Web search — ground responses in live information

Headless mode — run non-interactively for scripting and CI

Plus all SDK features out of the box — remote sandboxes, persistent memory, custom skills, and human-in-the-loop approval

See the CLI documentation for the full feature set.

LangGraph Native

create_deep_agent
 returns a compiled LangGraph graph. Use it with streaming, Studio, checkpointers, or any LangGraph feature.

FAQ

Why should I use this?

100% open source — MIT licensed, fully extensible

Provider agnostic — Works with any Large Language Model that supports tool calling, including both frontier and open models

Built on LangGraph — Production-ready runtime with streaming, persistence, and checkpointing

Batteries included — Planning, file access, sub-agents, and context management work out of the box

Get started in seconds — 
uv add deepagents
 and you have a working agent

Customize in minutes — Add tools, swap models, tune prompts when you need to

Documentation

docs.langchain.com – Comprehensive documentation, including conceptual overviews and guides

reference.langchain.com/python – API reference docs for Deep Agents packages

Chat LangChain – Chat with the LangChain documentation and get answers to your questions

Discussions: Visit the LangChain Forum to connect with the community and share all of your technical questions, ideas, and feedback.

Additional resources

Examples — Working agents and patterns

Contributing Guide – Learn how to contribute to LangChain projects and find good first issues.

Code of Conduct – Our community guidelines and standards for participation.

Acknowledgements

This project was primarily inspired by Claude Code, and initially was largely an attempt to see what made Claude Code general purpose, and make it even more so.

Security

Deep Agents follows a "trust the LLM" model. The agent can do anything its tools allow. Enforce boundaries at the tool/sandbox level, not by expecting the model to self-police. See the security policy for more information.

About

 Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks.
 

docs.langchain.com/deepagents

Topics

 ai

 langchain

 langgraph

 deepagents

Resources

 Readme

License

 MIT license
 

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

20.1k
 stars

Watchers

111
 watching

Forks

2.8k
 forks

 Report repository

Releases
 87

deepagents==0.5.1
 Latest

Apr 7, 2026

+ 86 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.3%

Other0.7%

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
