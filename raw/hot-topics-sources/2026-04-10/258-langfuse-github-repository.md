---
title: GitHub - langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 · GitHub
source_url: https://github.com/langfuse/langfuse
final_url: https://github.com/langfuse/langfuse
status: 200
content_type: text/html; charset=utf-8
topics: [Production Observability Platforms Convergence]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:01.744000+00:00
---

# GitHub - langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 · GitHub

## 원본 URL

https://github.com/langfuse/langfuse

## 추출 본문

GitHub - langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 · GitHub

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

 langfuse
/langfusePublic

Notifications
You must be signed in to change notification settings

Fork
 2.5k

 Star
24.6k

Code

Issues335

Pull requests285

Discussions

Actions

Security and quality3

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Security and quality

 Insights

langfuse/langfuse

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
6,725 Commits

6,725 Commits

.agents

.agents

.devcontainer

.devcontainer

.github

.github

.husky

.husky

.vscode

.vscode

ee

ee

fern

fern

packages

packages

patches

patches

scripts

scripts

specs

specs

web

web

worker

worker

.codespellrc

.codespellrc

.dockerignore

.dockerignore

.env.dev-azure.example

.env.dev-azure.example

.env.dev-redis-cluster.example

.env.dev-redis-cluster.example

.env.dev.example

.env.dev.example

.env.prod.example

.env.prod.example

.env.test.example

.env.test.example

.gitignore

.gitignore

.npmrc

.npmrc

.nvmrc

.nvmrc

.prettierignore

.prettierignore

AGENTS.md

AGENTS.md

CLAUDE.md

CLAUDE.md

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

README.cn.md

README.cn.md

README.ja.md

README.ja.md

README.kr.md

README.kr.md

README.md

README.md

SECURITY.md

SECURITY.md

docker-compose.build.yml

docker-compose.build.yml

docker-compose.dev-azure.yml

docker-compose.dev-azure.yml

docker-compose.dev-redis-cluster.yml

docker-compose.dev-redis-cluster.yml

docker-compose.dev.yml

docker-compose.dev.yml

docker-compose.yml

docker-compose.yml

package.json

package.json

pnpm-lock.yaml

pnpm-lock.yaml

pnpm-workspace.yaml

pnpm-workspace.yaml

prettier.config.cjs

prettier.config.cjs

turbo.json

turbo.json

vitest.workspace.ts

vitest.workspace.ts

View all files

Repository files navigation

README

Contributing

License

Security

Langfuse Is Doubling Down On Open Source

Langfuse Cloud · 
 Self Host · 
 Demo

Docs ·
 Report Bug ·
 Feature Request ·
 Changelog ·
 Roadmap ·
 

Langfuse uses GitHub Discussions for Support and Feature Requests.
We're hiring.Join us in product engineering and technical go-to-market roles.

Proudly made with ClickHouse open source database

Langfuse is an open source LLM engineering platform. It helps teams collaboratively
develop, monitor, evaluate, and debug AI applications. Langfuse can be self-hosted in minutes and is battle-tested.

✨ Core Features

LLM Application Observability: Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions. Try the interactive demo to see this in action.

Prompt Management helps you centrally manage, version control, and collaboratively iterate on your prompts. Thanks to strong caching on server and client side, you can iterate on prompts without adding latency to your application.

Evaluations are key to the LLM application development workflow, and Langfuse adapts to your needs. It supports LLM-as-a-judge, user feedback collection, manual labeling, and custom evaluation pipelines via APIs/SDKs.

Datasets enable test sets and benchmarks for evaluating your LLM application. They support continuous improvement, pre-deployment testing, structured experiments, flexible evaluation, and seamless integration with frameworks like LangChain and LlamaIndex.

LLM Playground is a tool for testing and iterating on your prompts and model configurations, shortening the feedback loop and accelerating development. When you see a bad result in tracing, you can directly jump to the playground to iterate on it.

Comprehensive API: Langfuse is frequently used to power bespoke LLMOps workflows while using the building blocks provided by Langfuse via the API. OpenAPI spec, Postman collection, and typed SDKs for Python, JS/TS are available.

📦 Deploy Langfuse

Langfuse Cloud

Managed deployment by the Langfuse team, generous free-tier, no credit card required.

Self-Host Langfuse

Run Langfuse on your own infrastructure:

Local (docker compose): Run Langfuse on your own machine in 5 minutes using Docker Compose.

# Get a copy of the latest Langfuse repository
git clone https://github.com/langfuse/langfuse.git
cd langfuse

# Run the langfuse docker compose
docker compose up

VM: Run Langfuse on a single Virtual Machine using Docker Compose.

Kubernetes (Helm): Run Langfuse on a Kubernetes cluster using Helm. This is the preferred production deployment.

Terraform Templates: AWS, Azure, GCP

See self-hosting documentation to learn more about architecture and configuration options.

🔌 Integrations

Main Integrations:

IntegrationSupportsDescriptionSDKPython, JS/TSManual instrumentation using the SDKs for full flexibility.OpenAIPython, JS/TSAutomated instrumentation using drop-in replacement of OpenAI SDK.LangchainPython, JS/TSAutomated instrumentation by passing callback handler to Langchain application.LlamaIndexPythonAutomated instrumentation via LlamaIndex callback system.HaystackPythonAutomated instrumentation via Haystack content tracing system.LiteLLMPython, JS/TS (proxy only)Use any LLM as a drop in replacement for GPT. Use Azure, OpenAI, Cohere, Anthropic, Ollama, VLLM, Sagemaker, HuggingFace, Replicate (100+ LLMs).Vercel AI SDKJS/TSTypeScript toolkit designed to help developers build AI-powered applications with React, Next.js, Vue, Svelte, Node.js.MastraJS/TSOpen source framework for building AI agents and multi-agent systems.APIDirectly call the public API. OpenAPI spec available.

Packages integrated with Langfuse:

NameTypeDescriptionInstructorLibraryLibrary to get structured LLM outputs (JSON, Pydantic)DSPyLibraryFramework that systematically optimizes language model prompts and weightsMirascopeLibraryPython toolkit for building LLM applications.OllamaModel (local)Easily run open source LLMs on your own machine.Amazon BedrockModelRun foundation and fine-tuned models on AWS.AutoGenAgent FrameworkOpen source LLM platform for building distributed agents.FlowiseChat/Agent UIJS/TS no-code builder for customized LLM flows.LangflowChat/Agent UIPython-based UI for LangChain, designed with react-flow to provide an effortless way to experiment and prototype flows.DifyChat/Agent UIOpen source LLM app development platform with no-code builder.OpenWebUIChat/Agent UISelf-hosted LLM Chat web ui supporting various LLM runners including self-hosted and local models.PromptfooToolOpen source LLM testing platform.LobeChatChat/Agent UIOpen source chatbot platform.VapiPlatformOpen source voice AI platform.InferableAgentsOpen source LLM platform for building distributed agents.GradioChat/Agent UIOpen source Python library to build web interfaces like Chat UI.GooseAgentsOpen source LLM platform for building distributed agents.smolagentsAgentsOpen source AI agents framework.CrewAIAgentsMulti agent framework for agent collaboration and tool use.

🚀 Quickstart

Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions.

1️⃣ Create new project

Create Langfuse account or self-host

Create a new project

Create new API credentials in the project settings

2️⃣ Log your first LLM call

The 
@observe()
 decorator makes it easy to trace any Python LLM application. In this quickstart we also use the Langfuse OpenAI integration to automatically capture all model parameters.

Tip

Not using OpenAI? Visit our documentation to learn how to log other models and frameworks.

pip install langfuse openai

LANGFUSE_SECRET_KEY="sk-lf-..."
LANGFUSE_PUBLIC_KEY="pk-lf-..."
LANGFUSE_BASE_URL="https://cloud.langfuse.com"# 🇪🇺 EU region# LANGFUSE_BASE_URL="https://us.cloud.langfuse.com" # 🇺🇸 US region

fromlangfuseimportobservefromlangfuse.openaiimportopenai# OpenAI integration@observe()defstory():
 returnopenai.chat.completions.create(
 model="gpt-4o",
 messages=[{"role": "user", "content": "What is Langfuse?"}],
 ).choices[0].message.content@observe()defmain():
 returnstory()

main()

3️⃣ See traces in Langfuse

See your language model calls and other application logic in Langfuse.

Public example trace in Langfuse

Tip

Learn more about tracing in Langfuse or play with the interactive demo.

⭐️ Star Us

💭 Support

Finding an answer to your question:

Our documentation is the best place to start looking for answers. It is comprehensive, and we invest significant time into maintaining it. You can also suggest edits to the docs via GitHub.

Langfuse FAQs where the most common questions are answered.

Use "Ask AI" to get instant answers to your questions.

Support Channels:

Ask any question in our public Q&A on GitHub Discussions. Please include as much detail as possible (e.g. code snippets, screenshots, background information) to help us understand your question.

Request a feature on GitHub Discussions.

Report a Bug on GitHub Issues.

For time-sensitive queries, ping us via the in-app chat widget.

🤝 Contributing

Your contributions are welcome!

Vote on Ideas in GitHub Discussions.

Raise and comment on Issues.

Open a PR - see CONTRIBUTING.md for details on how to setup a development environment.

🥇 License

This repository is MIT licensed, except for the 
ee
 folders. See LICENSE and docs for more details.

Dependencies

We deploy this code base in Docker containers based on the Linux Alpine Image (source). You may find the Dockerfiles in web/Dockerfile and worker/Dockerfile.

⭐️ Star History

❤️ Open Source Projects Using Langfuse

Top open-source Python projects that use Langfuse, ranked by stars (Source):
RepositoryStarslangflow-ai / langflow116251open-webui / open-webui109642abi / screenshot-to-code70877lobehub / lobe-chat65454infiniflow / ragflow64118firecrawl / firecrawl56713run-llama / llama_index44203FlowiseAI / Flowise43547QuivrHQ / quivr38415microsoft / ai-agents-for-beginners38012chatchat-space / Langchain-Chatchat36071mindsdb / mindsdb35669danny-avila / LibreChat33142BerriAI / litellm28726onlook-dev / onlook22447NixOS / nixpkgs21748kortix-ai / suna17976anthropics / courses17057mastra-ai / mastra16484langfuse / langfuse16054Canner / WrenAI11868promptfoo / promptfoo8350The-Pocket / PocketFlow8313OpenPipe / ART7093topoteretes / cognee7011awslabs / agent-squad6785BasedHardware / omi6231hatchet-dev / hatchet6019zenml-io / zenml4873refly-ai / refly4654coleam00 / ottomator-agents4165JoshuaC215 / agent-service-toolkit3557colanode / colanode3517VoltAgent / voltagent3210bragai / bRAG-langchain3010pingcap / autoflow2651sourcebot-dev / sourcebot2570open-webui / pipelines2055YFGaia / dify-plus1734TheSpaghettiDetective / obico-server1687MLSysOps / MLE-agent1387TIGER-AI-Lab / TheoremExplainAgent1385trailofbits / buttercup1223wassim249 / fastapi-langgraph-agent-production-ready-template1200alishobeiri / thread1098dmayboroda / minima1010zstar1003 / ragflow-plus993openops-cloud / openops939dynamiq-ai / dynamiq927xataio / agent857plastic-labs / tutor-gpt845trendy-design / llmchat829hotovo / aider-desk781opslane / opslane719wrtnlabs / autoview688andysingal / llm-course643theopenconversationkit / tock587sentient-engineering / agent-q487NicholasGoh / fastapi-mcp-langgraph-template481i-am-alice / 3rd-devs472AIDotNet / koala-ai470phospho-app / text-analytics-legacy439inferablehq / inferable403duoyang666 / ai_novel397strands-agents / samples385FranciscoMoretti / sparka380RobotecAI / rai373ElectricCodeGuy / SupabaseAuthWithSSR370souzatharsis / tamingLLMs323aws-samples / aws-ai-ml-workshop-kr295weizxfree / KnowFlow285zenml-io / zenml-projects276wxai-space / LightAgent275Ozamatash / deep-research-mcp269sql-agi / DB-GPT241guyernest / advanced-rag238bklieger-groq / mathtutor-on-groq233plastic-labs / honcho224OVINC-CN / OpenWebUI202zhutoutoutousan / worldquant-miner202iceener / ai186giselles-ai / giselle181ai-shifu / ai-shifu181aws-samples / sample-serverless-mcp-servers175celerforge / freenote171babelcloud / LLM-RGB1648090-inc / xrx-sample-apps163deepset-ai / haystack-core-integrations163codecentric / c4-genai-suite152XSpoonAi / spoon-core150chatchat-space / LangGraph-Chatchat144langfuse / langfuse-docs139piyushgarg-dev / genai-cohort135i-dot-ai / redbox132bmd1905 / ChatOpsLLM127Fintech-Dreamer / FinSynth121kenshiro-o / nagato-ai119

🔒 Security & Privacy

We take data security and privacy seriously. Please refer to our Security and Privacy page for more information.

Telemetry

By default, Langfuse automatically reports basic usage statistics of self-hosted instances to a centralized server (PostHog).

This helps us to:

Understand how Langfuse is used and improve the most relevant features.

Track overall usage for internal and external (e.g. fundraising) reporting.

The telemetry does not include raw traces, prompts, observations, scores, or dataset contents. We document the exact fields that are collected, where they are sent, and the implementation reference in our telemetry docs.

For Langfuse OSS, you can opt out by setting 
TELEMETRY_ENABLED=false
.

About

 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 
 

langfuse.com/docs

Topics

 open-source

 playground

 monitoring

 analytics

 evaluation

 self-hosted

 ycombinator

 openai

 observability

 autogen

 large-language-models

 llm

 prompt-engineering

 langchain

 llmops

 llama-index

 prompt-management

 llm-evaluation

 llm-observability

Resources

 Readme

License

 View license
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

24.6k
 stars

Watchers

70
 watching

Forks

2.5k
 forks

 Report repository

Releases
 548

v3.167.0
 Latest

Apr 9, 2026

+ 547 releases

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

TypeScript99.0%

Other1.0%

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
