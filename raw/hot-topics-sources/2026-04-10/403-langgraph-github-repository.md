---
title: GitHub - langchain-ai/langgraph: Build resilient language agents as graphs. · GitHub
source_url: https://github.com/langchain-ai/langgraph
final_url: https://github.com/langchain-ai/langgraph
status: 200
content_type: text/html; charset=utf-8
topics: [LangGraph 1.0 / 2.0 (Agent Orchestration Framework)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:22.769627+00:00
---

# GitHub - langchain-ai/langgraph: Build resilient language agents as graphs. · GitHub

## 원본 URL

https://github.com/langchain-ai/langgraph

## 추출 본문

GitHub - langchain-ai/langgraph: Build resilient language agents as graphs. · GitHub

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
/langgraphPublic

Notifications
You must be signed in to change notification settings

Fork
 4.9k

 Star
28.8k

Code

Issues250

Pull requests240

Actions

Projects

Security and quality5

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

langchain-ai/langgraph

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
6,714 Commits

6,714 Commits

.github

.github

docs

docs

examples

examples

libs

libs

.gitignore

.gitignore

.markdownlint.json

.markdownlint.json

AGENTS.md

AGENTS.md

CLAUDE.md

CLAUDE.md

LICENSE

LICENSE

Makefile

Makefile

README.md

README.md

View all files

Repository files navigation

README

Code of conduct

Contributing

MIT license

Security

Low-level orchestration framework for building stateful agents.

Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful agents.

pip install -U langgraph

If you're looking to quickly build agents with LangChain's 
create_agent
 (built on LangGraph), check out the LangChain Agents documentation.

Note

Looking for the JS/TS library? Check out LangGraph.js and the JS docs.

Why use LangGraph?

LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent:

Durable execution — Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off.

Human-in-the-loop — Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution.

Comprehensive memory — Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions.

Debugging with LangSmith — Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.

Production-ready deployment — Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.

Tip

For developing, debugging, and deploying AI agents and LLM applications, see LangSmith.

LangGraph ecosystem

While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents.

To improve your LLM application development, pair LangGraph with:

Deep Agents(new!) – Build agents that can plan, use subagents, and leverage file systems for complex tasks.

LangChain – Provides integrations and composable components to streamline LLM application development.

LangSmith – Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time.

LangSmith Deployment – Deploy and scale agents effortlessly with a purpose-built deployment platform for long-running, stateful workflows. Discover, reuse, configure, and share agents across teams – and iterate quickly with visual prototyping in LangSmith Studio.

Documentation

docs.langchain.com – Comprehensive documentation, including conceptual overviews and guides

reference.langchain.com/python/langgraph – API reference docs for LangGraph packages

LangGraph Quickstart – Get started building with LangGraph

Chat LangChain – Chat with the LangChain documentation and get answers to your questions

Discussions: Visit the LangChain Forum to connect with the community and share all of your technical questions, ideas, and feedback.

Additional resources

Guides – Quick, actionable code snippets for topics such as streaming, adding memory & persistence, and design patterns (e.g. branching, subgraphs, etc.).

LangChain Academy – Learn the basics of LangGraph in our free, structured course.

Case studies – Hear how industry leaders use LangGraph to ship AI applications at scale.

Contributing Guide – Learn how to contribute to LangChain projects and find good first issues.

Code of Conduct – Our community guidelines and standards for participation.

Acknowledgements

LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

About

 Build resilient language agents as graphs.
 

docs.langchain.com/oss/python/langgraph/

Topics

 python

 open-source

 enterprise

 framework

 ai

 gemini

 openai

 multiagent

 agents

 ai-agents

 rag

 pydantic

 llm

 generative-ai

 chatgpt

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

28.8k
 stars

Watchers

150
 watching

Forks

4.9k
 forks

 Report repository

Releases
 494

langgraph-cli==0.4.21
 Latest

Apr 8, 2026

+ 493 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.4%

Other0.6%

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
