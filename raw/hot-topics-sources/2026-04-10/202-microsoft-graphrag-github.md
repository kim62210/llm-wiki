---
title: GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub
source_url: https://github.com/microsoft/graphrag
final_url: https://github.com/microsoft/graphrag
status: 200
content_type: text/html; charset=utf-8
topics: [GraphRAG / LightRAG / LazyGraphRAG in Production]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:53.965143+00:00
---

# GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub

## 원본 URL

https://github.com/microsoft/graphrag

## 추출 본문

GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub

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

 microsoft
/graphragPublic

Notifications
You must be signed in to change notification settings

Fork
 3.4k

 Star
32.1k

Code

Issues35

Pull requests55

Discussions

Actions

Projects

Models

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Models

 Security and quality

 Insights

microsoft/graphrag

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
463 Commits

463 Commits

.github

.github

.semversioner

.semversioner

.vscode

.vscode

docs

docs

packages

packages

scripts

scripts

tests

tests

unified-search-app

unified-search-app

.gitattributes

.gitattributes

.gitignore

.gitignore

.vsts-ci.yml

.vsts-ci.yml

CHANGELOG.md

CHANGELOG.md

CODEOWNERS

CODEOWNERS

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

DEVELOPING.md

DEVELOPING.md

LICENSE

LICENSE

RAI_TRANSPARENCY.md

RAI_TRANSPARENCY.md

README.md

README.md

RELEASE.md

RELEASE.md

SECURITY.md

SECURITY.md

SUPPORT.md

SUPPORT.md

breaking-changes.md

breaking-changes.md

cspell.config.yaml

cspell.config.yaml

dictionary.txt

dictionary.txt

mkdocs.yaml

mkdocs.yaml

pyproject.toml

pyproject.toml

uv.lock

uv.lock

View all files

Repository files navigation

README

Code of conduct

Contributing

MIT license

Security

GraphRAG

👉 Microsoft Research Blog Post

👉 Read the docs

👉 GraphRAG Arxiv

Overview

The GraphRAG project is a data pipeline and transformation suite that is designed to extract meaningful, structured data from unstructured text using the power of LLMs.

To learn more about GraphRAG and how it can be used to enhance your LLM's ability to reason about your private data, please visit the Microsoft Research Blog Post.

Quickstart

To get started with the GraphRAG system we recommend trying the command line quickstart.

Repository Guidance

This repository presents a methodology for using knowledge graph memory structures to enhance LLM outputs. Please note that the provided code serves as a demonstration and is not an officially supported Microsoft offering.

⚠️Warning: GraphRAG indexing can be an expensive operation, please read all of the documentation to understand the process and costs involved, and start small.

Diving Deeper

To learn about our contribution guidelines, see CONTRIBUTING.md

To start developing GraphRAG, see DEVELOPING.md

Join the conversation and provide feedback in the GitHub Discussions tab!

Prompt Tuning

Using GraphRAG with your data out of the box may not yield the best possible results.
We strongly recommend to fine-tune your prompts following the Prompt Tuning Guide in our documentation.

Versioning

Please see the breaking changes document for notes on our approach to versioning the project.

Always run 
graphrag init --root [path] --force
 between minor version bumps to ensure you have the latest config format. Run the provided migration notebook between major version bumps if you want to avoid re-indexing prior datasets. Note that this will overwrite your configuration and prompts, so backup if necessary.

Responsible AI FAQ

See RAI_TRANSPARENCY.md

What is GraphRAG?

What can GraphRAG do?

What are GraphRAG’s intended use(s)?

How was GraphRAG evaluated? What metrics are used to measure performance?

What are the limitations of GraphRAG? How can users minimize the impact of GraphRAG’s limitations when using the system?

What operational factors and settings allow for effective and responsible use of GraphRAG?

Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
Microsoft's Trademark & Brand Guidelines.
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

Privacy

Microsoft Privacy Statement

About

 A modular graph-based Retrieval-Augmented Generation (RAG) system
 

microsoft.github.io/graphrag/

Topics

 gpt

 rag

 gpt-4

 gpt4

 llm

 llms

 graphrag

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

32.1k
 stars

Watchers

191
 watching

Forks

3.4k
 forks

 Report repository

Releases
 38

v3.0.8
 Latest

Mar 27, 2026

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

Python88.2%

Jupyter Notebook11.8%

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
