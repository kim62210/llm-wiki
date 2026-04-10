---
title: GitHub - mem0ai/mem0: Universal memory layer for AI Agents · GitHub
source_url: https://github.com/mem0ai/mem0
final_url: https://github.com/mem0ai/mem0
status: 200
content_type: text/html; charset=utf-8
topics: [Mem0 Universal Memory Layer]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:51.261386+00:00
---

# GitHub - mem0ai/mem0: Universal memory layer for AI Agents · GitHub

## 원본 URL

https://github.com/mem0ai/mem0

## 추출 본문

GitHub - mem0ai/mem0: Universal memory layer for AI Agents · GitHub

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

 mem0ai
/mem0Public

Notifications
You must be signed in to change notification settings

Fork
 5.9k

 Star
52.5k

Code

Issues95

Pull requests134

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

mem0ai/mem0

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
2,095 Commits

2,095 Commits

.agents/plugins

.agents/plugins

.claude-plugin

.claude-plugin

.cursor-plugin

.cursor-plugin

.github

.github

cli

cli

cookbooks

cookbooks

docs

docs

embedchain

embedchain

evaluation

evaluation

examples

examples

mem0-plugin

mem0-plugin

mem0-ts

mem0-ts

mem0

mem0

openclaw

openclaw

openmemory

openmemory

server

server

skills

skills

tests

tests

vercel-ai-sdk

vercel-ai-sdk

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

AGENTS.md

AGENTS.md

CLAUDE.md

CLAUDE.md

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

LLM.md

LLM.md

MIGRATION_GUIDE_v1.0.md

MIGRATION_GUIDE_v1.0.md

Makefile

Makefile

README.md

README.md

poetry.lock

poetry.lock

pyproject.toml

pyproject.toml

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

Learn more
 ·
 Join Discord
 ·
 Demo

📄 Building Production-Ready AI Agents with Scalable Long-Term Memory →

⚡ +26% Accuracy vs. OpenAI Memory • 🚀 91% Faster • 💰 90% Fewer Tokens

🎉 mem0ai v1.0.0 is now available! This major release includes API modernization, improved vector store support, and enhanced GCP integration. See migration guide →

🔥 Research Highlights

+26% Accuracy over OpenAI Memory on the LOCOMO benchmark

91% Faster Responses than full-context, ensuring low-latency at scale

90% Lower Token Usage than full-context, cutting costs without compromise

Read the full paper

Introduction

Mem0 ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. It remembers user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and autonomous systems.

Key Features & Use Cases

Core Capabilities:

Multi-Level Memory: Seamlessly retains User, Session, and Agent state with adaptive personalization

Developer-Friendly: Intuitive API, cross-platform SDKs, and a fully managed service option

Applications:

AI Assistants: Consistent, context-rich conversations

Customer Support: Recall past tickets and user history for tailored help

Healthcare: Track patient preferences and history for personalized care

Productivity & Gaming: Adaptive workflows and environments based on user behavior

🚀 Quickstart Guide 

Choose between our hosted platform or self-hosted package:

Hosted Platform

Get up and running in minutes with automatic updates, analytics, and enterprise security.

Sign up on Mem0 Platform

Embed the memory layer via SDK or API keys

Self-Hosted (Open Source)

Install the sdk via pip:

pip install mem0ai

Install sdk via npm:

npm install mem0ai

CLI

Manage memories from your terminal:

npm install -g @mem0/cli # or: pip install mem0-cli

mem0 init
mem0 add "Prefers dark mode and vim keybindings" --user-id alice
mem0 search "What does Alice prefer?" --user-id alice

See the CLI documentation for the full command reference.

Basic Usage

Mem0 requires an LLM to function, with `gpt-4.1-nano-2025-04-14 from OpenAI as the default. However, it supports a variety of LLMs; for details, refer to our Supported LLMs documentation.

First step is to instantiate the memory:

fromopenaiimportOpenAIfrommem0importMemoryopenai_client=OpenAI()
memory=Memory()

defchat_with_memories(message: str, user_id: str="default_user") ->str:
 # Retrieve relevant memoriesrelevant_memories=memory.search(query=message, user_id=user_id, limit=3)
 memories_str="\n".join(f"- {entry['memory']}"forentryinrelevant_memories["results"])

 # Generate Assistant responsesystem_prompt=f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"messages= [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
 response=openai_client.chat.completions.create(model="gpt-4.1-nano-2025-04-14", messages=messages)
 assistant_response=response.choices[0].message.content# Create new memories from the conversationmessages.append({"role": "assistant", "content": assistant_response})
 memory.add(messages, user_id=user_id)

 returnassistant_responsedefmain():
 print("Chat with AI (type 'exit' to quit)")
 whileTrue:
 user_input=input("You: ").strip()
 ifuser_input.lower() =='exit':
 print("Goodbye!")
 breakprint(f"AI: {chat_with_memories(user_input)}")

if__name__=="__main__":
 main()

For detailed integration steps, see the Quickstart and API Reference.

🔗 Integrations & Demos

ChatGPT with Memory: Personalized chat powered by Mem0 (Live Demo)

Browser Extension: Store memories across ChatGPT, Perplexity, and Claude (Chrome Extension)

Langgraph Support: Build a customer bot with Langgraph + Mem0 (Guide)

CrewAI Integration: Tailor CrewAI outputs with Mem0 (Example)

📚 Documentation & Support

Full docs: https://docs.mem0.ai

Community: Discord · X (formerly Twitter)

Contact: founders@mem0.ai

Citation

We now have a paper you can cite:

@article{mem0,
 title={Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory},
 author={Chhikara, Prateek and Khant, Dev and Aryan, Saket and Singh, Taranjeet and Yadav, Deshraj},
 journal={arXiv preprint arXiv:2504.19413},
 year={2025}
}

⚖️ License

Apache 2.0 — see the LICENSE file for details.

About

 Universal memory layer for AI Agents
 

mem0.ai

Topics

 python

 application

 state-management

 ai

 memory

 chatbots

 memory-management

 agents

 ai-agents

 long-term-memory

 rag

 llm

 chatgpt

 genai

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

52.5k
 stars

Watchers

222
 watching

Forks

5.9k
 forks

 Report repository

Releases
 293

Mem0 OpenClaw Plugin (v1.0.5)
 Latest

Apr 9, 2026

+ 292 releases

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

Python61.0%

TypeScript29.0%

MDX4.8%

Jupyter Notebook2.9%

JavaScript1.1%

Shell0.7%

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
