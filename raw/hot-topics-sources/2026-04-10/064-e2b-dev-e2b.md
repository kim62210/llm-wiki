---
title: GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub
source_url: https://github.com/e2b-dev/E2B
final_url: https://github.com/e2b-dev/E2B
status: 200
content_type: text/html; charset=utf-8
topics: [Firecracker/microVM Sandboxes for Agent Code Execution]
sections: [Harness Engineering]
fetched_at: 2026-04-10T01:43:33.962293+00:00
---

# GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub

## 원본 URL

https://github.com/e2b-dev/E2B

## 추출 본문

GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub

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

 e2b-dev
/E2BPublic

Notifications
You must be signed in to change notification settings

Fork
 835

 Star
11.6k

Code

Issues41

Pull requests25

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

e2b-dev/E2B

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
4,766 Commits

4,766 Commits

.changeset

.changeset

.github

.github

.vscode

.vscode

packages

packages

readme-assets

readme-assets

spec

spec

supabase

supabase

templates/base

templates/base

.editorconfig

.editorconfig

.eslintrc.cjs

.eslintrc.cjs

.gitattributes

.gitattributes

.gitignore

.gitignore

.npmrc

.npmrc

.prettierignore

.prettierignore

.prettierrc

.prettierrc

.tool-versions

.tool-versions

.vale.ini

.vale.ini

CLAUDE.md

CLAUDE.md

CODEOWNERS

CODEOWNERS

CONTRIBUTING.md

CONTRIBUTING.md

DEV.md

DEV.md

LICENSE

LICENSE

Makefile

Makefile

README.md

README.md

codegen.Dockerfile

codegen.Dockerfile

package.json

package.json

pnpm-lock.yaml

pnpm-lock.yaml

pnpm-workspace.yaml

pnpm-workspace.yaml

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

What is E2B?

E2B is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud. To start and control sandboxes, use our JavaScript SDK or Python SDK.

Run your first Sandbox

1. Install SDK

JavaScript / TypeScript

npm i e2b

Python

pip install e2b

2. Get your E2B API key

Sign up to E2B here.

Get your API key here.

Set environment variable with your API key

E2B_API_KEY=e2b_***

3. Start a sandbox and run commands

JavaScript / TypeScript

importSandboxfrom'e2b'constsandbox=awaitSandbox.create()constresult=awaitsandbox.commands.run('echo "Hello from E2B!"')console.log(result.stdout)// Hello from E2B!

Python

frome2bimportSandboxwithSandbox.create() assandbox:
 result=sandbox.commands.run('echo "Hello from E2B!"')
 print(result.stdout) # Hello from E2B!

4. Code execution with Code Interpreter

If you need to execute code with 
runCode()
/
run_code()
, install the Code Interpreter SDK:

npm i @e2b/code-interpreter # JavaScript/TypeScript
pip install e2b-code-interpreter # Python

import{Sandbox}from'@e2b/code-interpreter'constsandbox=awaitSandbox.create()constexecution=awaitsandbox.runCode('x = 1; x += 1; x')console.log(execution.text)// outputs 2

5. Check docs

Visit E2B documentation.

6. E2B cookbook

Visit our Cookbook to get inspired by examples with different LLMs and AI frameworks.

Self-hosting

Read the self-hosting guide to learn how to set up the E2B infrastructure on your own. The infrastructure is deployed using Terraform.

Supported cloud providers:

🟢 AWS

🟢 Google Cloud (GCP)

 Azure

 General Linux machine

About

 Open-source, secure environment with real-world tools for enterprise-grade agents.
 

e2b.dev/docs

Topics

 react

 javascript

 python

 agent

 development

 typescript

 ai

 nextjs

 devtools

 openai

 software

 gpt

 copilot

 ai-agents

 ai-agent

 gpt-4

 llm

 code-interpreter

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

11.6k
 stars

Watchers

69
 watching

Forks

835
 forks

 Report repository

Releases
 465

@e2b/python-sdk@2.20.0
 Latest

Apr 2, 2026

+ 464 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python56.4%

TypeScript42.3%

Go0.6%

Dockerfile0.3%

JavaScript0.2%

Handlebars0.1%

Other0.1%

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
