---
title: GitHub - mastra-ai/mastra: From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. · GitHub
source_url: https://github.com/mastra-ai/mastra
final_url: https://github.com/mastra-ai/mastra
status: 200
content_type: text/html; charset=utf-8
topics: [Mastra (TypeScript Agent Framework)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:29.470274+00:00
---

# GitHub - mastra-ai/mastra: From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. · GitHub

## 원본 URL

https://github.com/mastra-ai/mastra

## 추출 본문

GitHub - mastra-ai/mastra: From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. · GitHub

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

 mastra-ai
/mastraPublic

Notifications
You must be signed in to change notification settings

Fork
 1.9k

 Star
22.8k

Code

Issues227

Pull requests204

Actions

Projects

Security and quality1

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

mastra-ai/mastra

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
14,134 Commits

14,134 Commits

.changeset

.changeset

.claude

.claude

.cursor

.cursor

.dev

.dev

.github

.github

.husky

.husky

.mastracode/commands

.mastracode/commands

.opencode

.opencode

.superset

.superset

__recordings__

__recordings__

auth

auth

browser

browser

client-sdks

client-sdks

communications

communications

deployers

deployers

docs

docs

e2e-tests

e2e-tests

ee

ee

examples

examples

explorations

explorations

integrations/opencode

integrations/opencode

mastracode

mastracode

observability

observability

packages

packages

patches

patches

pubsub/google-cloud-pubsub

pubsub/google-cloud-pubsub

scripts

scripts

server-adapters

server-adapters

stores

stores

templates

templates

voice

voice

workflows

workflows

workspaces

workspaces

.coderabbit.yaml

.coderabbit.yaml

.gitignore

.gitignore

.prettierignore

.prettierignore

.prettierrc

.prettierrc

.stylelintrc.json

.stylelintrc.json

.vercelignore

.vercelignore

1

1

AGENTS.md

AGENTS.md

CLAUDE.md

CLAUDE.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

CONTRIBUTING.md

CONTRIBUTING.md

DEVELOPMENT.md

DEVELOPMENT.md

LICENSE.md

LICENSE.md

README.md

README.md

package.json

package.json

pnpm-lock.yaml

pnpm-lock.yaml

pnpm-workspace.yaml

pnpm-workspace.yaml

renovate.json

renovate.json

test.log

test.log

tsconfig.build.json

tsconfig.build.json

tsconfig.json

tsconfig.json

tsconfig.node.json

tsconfig.node.json

turbo.json

turbo.json

vitest.config.observability.ts

vitest.config.observability.ts

vitest.config.ts

vitest.config.ts

View all files

Repository files navigation

README

Code of conduct

Contributing

License

Mastra

Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

It includes everything you need to go from early prototypes to production-ready applications. Mastra integrates with frontend and backend frameworks like React, Next.js, and Node, or you can deploy it anywhere as a standalone server. It's the easiest way to build, tune, and scale reliable AI products.

Why Mastra?

Purpose-built for TypeScript and designed around established AI patterns, Mastra gives you everything you need to build great AI applications out-of-the-box.

Some highlights include:

Model routing - Connect to 40+ providers through one standard interface. Use models from OpenAI, Anthropic, Gemini, and more.

Agents - Build autonomous agents that use LLMs and tools to solve open-ended tasks. Agents reason about goals, decide which tools to use, and iterate internally until the model emits a final answer or an optional stopping condition is met.

Workflows - When you need explicit control over execution, use Mastra's graph-based workflow engine to orchestrate complex multi-step processes. Mastra workflows use an intuitive syntax for control flow (
.then()
, 
.branch()
, 
.parallel()
).

Human-in-the-loop - Suspend an agent or workflow and await user input or approval before resuming. Mastra uses storage to remember execution state, so you can pause indefinitely and resume where you left off.

Context management - Give your agents the right context at the right time. Provide conversation history, retrieve data from your sources (APIs, databases, files), and add human-like working and semantic memory so your agents behave coherently.

Integrations - Bundle agents and workflows into existing React, Next.js, or Node.js apps, or ship them as standalone endpoints. When building UIs, integrate with agentic libraries like Vercel's AI SDK UI and CopilotKit to bring your AI assistant to life on the web.

MCP servers - Author Model Context Protocol servers, exposing agents, tools, and other structured resources via the MCP interface. These can then be accessed by any system or agent that supports the protocol.

Production essentials - Shipping reliable agents takes ongoing insight, evaluation, and iteration. With built-in evals and observability, Mastra gives you the tools to observe, measure, and refine continuously.

Get started

The recommended way to get started with Mastra is by running the command below:

npm create mastra@latest

Follow the Installation guide for step-by-step setup with the CLI or a manual install.

If you're new to AI agents, check out our templates, course, and YouTube videos to start building with Mastra today.

Documentation

Visit our official documentation.

Build with AI

Learn how to make your agent a Mastra expert by following the Build with AI guide.

Contributing

Looking to contribute? All types of help are appreciated, from coding to testing and feature specification. Read CONTRIBUTING.md for more details on how to get involved.

If you are a developer and would like to contribute with code, please open an issue to discuss before opening a Pull Request.

Information about the project setup can be found in the development documentation

Support

We have an open community Discord. Come and say hello and let us know if you have any questions or need any help getting things running.

It's also super helpful if you leave the project a star here at the top of the page

Licensing

This repository uses a dual-license model:

Apache License 2.0 — The core framework and the vast majority of this codebase is open source under Apache-2.0.

Mastra Enterprise License — Code in any directory named 
ee/
 (e.g., 
packages/core/src/auth/ee/
) is source-available under the Mastra Enterprise License. These features require a valid enterprise license for production use but can be freely used for development and testing.

See LICENSE.md for the full license mapping and ee/LICENSE for the enterprise license terms.

Security

We are committed to maintaining the security of this repo and of Mastra as a whole. If you discover a security finding we ask you to please responsibly disclose this to us at security@mastra.ai and we will get back to you.

About

 From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.
 

mastra.ai

Topics

 nodejs

 javascript

 typescript

 ai

 reactjs

 mcp

 nextjs

 tts

 chatbots

 workflows

 agents

 llm

 evals

Resources

 Readme

License

 View license
 

Code of conduct

 Code of conduct
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

22.8k
 stars

Watchers

90
 watching

Forks

1.9k
 forks

 Report repository

Releases
 77

April 7, 20206
 Latest

Apr 8, 2026

+ 76 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors
 401

+ 387 contributors

Languages

TypeScript99.3%

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
