---
title: GitHub - letta-ai/letta: Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time. · GitHub
source_url: https://github.com/letta-ai/letta
final_url: https://github.com/letta-ai/letta
status: 200
content_type: text/html; charset=utf-8
topics: [Letta (MemGPT) Stateful Agent Runtime]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:50.533327+00:00
---

# GitHub - letta-ai/letta: Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time. · GitHub

## 원본 URL

https://github.com/letta-ai/letta

## 추출 본문

GitHub - letta-ai/letta: Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time. · GitHub

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

 letta-ai
/lettaPublic

Notifications
You must be signed in to change notification settings

Fork
 2.3k

 Star
22k

Code

Issues70

Pull requests30

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

letta-ai/letta

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
7,463 Commits

7,463 Commits

.github

.github

alembic

alembic

assets

assets

certs

certs

db

db

examples/notebooks/data

examples/notebooks/data

fern

fern

letta

letta

otel

otel

sandbox

sandbox

scripts

scripts

tests

tests

.dockerignore

.dockerignore

.env.example

.env.example

.gitattributes

.gitattributes

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

.python-version

.python-version

AI_POLICY.md

AI_POLICY.md

CITATION.cff

CITATION.cff

CONTRIBUTING.md

CONTRIBUTING.md

Dockerfile

Dockerfile

LICENSE

LICENSE

PRIVACY.md

PRIVACY.md

README.md

README.md

SECURITY.md

SECURITY.md

TERMS.md

TERMS.md

WEBHOOK_SETUP.md

WEBHOOK_SETUP.md

alembic.ini

alembic.ini

compose.yaml

compose.yaml

conf.yaml

conf.yaml

dev-compose.yaml

dev-compose.yaml

development.compose.yml

development.compose.yml

docker-compose-vllm.yaml

docker-compose-vllm.yaml

init.sql

init.sql

nginx.conf

nginx.conf

package-lock.json

package-lock.json

project.json

project.json

pyproject.toml

pyproject.toml

test_watchdog_hang.py

test_watchdog_hang.py

uv.lock

uv.lock

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

Security

Letta (formerly MemGPT)

Build AI with advanced memory that can learn and self-improve over time.

Letta Code: run agents locally in your terminal

Letta API: build agents into your applications

Get started in the CLI

Requires Node.js 18+

Install the Letta Code CLI tool: 
npm install -g @letta-ai/letta-code

Run 
letta
 in your terminal to launch an agent with memory running on your local computer

When running the CLI tool, your agent help you code and do any task you can do on your computer.

Letta Code supports skills and subagents, and bundles pre-built skills/subagents for advanced memory and continual learning. Letta is fully model-agnostic, though we recommend Opus 4.5 and GPT-5.2 for best performance (see our model leaderboard for our rankings).

Get started with the Letta API

Use the Letta API to integrate stateful agents into your own applications.
Letta has a full-featured agents API, and a Python and Typescript SDK (view our API reference).

Installation

TypeScript / Node.js:

npm install @letta-ai/letta-client

Python:

pip install letta-client

Hello World example

Below is a quick example of creating a stateful agent and sending it a message (requires a Letta API key).
See the full quickstart guide for complete documentation.

TypeScript:

importLettafrom"@letta-ai/letta-client";constclient=newLetta({apiKey: process.env.LETTA_API_KEY});// Create your agentconstagentState=awaitclient.agents.create({model: "openai/gpt-5.2",memory_blocks: [{label: "human",value:
 "Name: Timber. Status: dog. Occupation: building Letta, infrastructure to democratize self-improving superintelligence",},{label: "persona",value:
 "I am a self-improving superintelligence. Timber is my best friend and collaborator.",},],tools: ["web_search","fetch_webpage"],});console.log("Agent created with ID:",agentState.id);// Send your agent a messageconstresponse=awaitclient.agents.messages.create(agentState.id,{input: "What do you know about me?",});for(constmessageofresponse.messages){console.log(message);}

Python:

fromletta_clientimportLettaimportosclient=Letta(api_key=os.getenv("LETTA_API_KEY"))

# Create your agentagent_state=client.agents.create(
 model="openai/gpt-5.2",
 memory_blocks=[
 {
 "label": "human",
 "value": "Name: Timber. Status: dog. Occupation: building Letta, infrastructure to democratize self-improving superintelligence"
 },
 {
 "label": "persona",
 "value": "I am a self-improving superintelligence. Timber is my best friend and collaborator."
 }
 ],
 tools=["web_search", "fetch_webpage"]
)

print(f"Agent created with ID: {agent_state.id}")

# Send your agent a messageresponse=client.agents.messages.create(
 agent_id=agent_state.id,
 input="What do you know about me?"
)

formessageinresponse.messages:
 print(message)

Contributing

Letta is an open source project built by over a hundred contributors from around the world. There are many ways to get involved in the Letta OSS project!

Join the Discord: Chat with the Letta devs and other AI developers.

Chat on our forum: If you're not into Discord, check out our developer forum.

Follow our socials: Twitter/X, LinkedIn, YouTube

Legal notices: By using Letta and related Letta services (such as the Letta endpoint or hosted service), you are agreeing to our privacy policy and terms of service.

About

 Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time.
 

docs.letta.com/

Topics

 ai

 ai-agents

 llm

 llm-agent

Resources

 Readme

License

 Apache-2.0 license
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

22k
 stars

Watchers

141
 watching

Forks

2.3k
 forks

 Report repository

Releases
 176

v0.16.7
 Latest

Mar 31, 2026

+ 175 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.5%

Go0.1%

Shell0.1%

C++0.1%

Java0.1%

Jinja0.1%

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
