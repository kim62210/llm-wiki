---
title: GitHub - pydantic/pydantic-ai: AI Agent Framework, the Pydantic way · GitHub
source_url: https://github.com/pydantic/pydantic-ai
final_url: https://github.com/pydantic/pydantic-ai
status: 200
content_type: text/html; charset=utf-8
topics: [Pydantic AI (Type-Safe Python Agent Framework)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:25.764212+00:00
---

# GitHub - pydantic/pydantic-ai: AI Agent Framework, the Pydantic way · GitHub

## 원본 URL

https://github.com/pydantic/pydantic-ai

## 추출 본문

GitHub - pydantic/pydantic-ai: AI Agent Framework, the Pydantic way · GitHub

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

 pydantic
/pydantic-aiPublic

Notifications
You must be signed in to change notification settings

Fork
 1.9k

 Star
16.2k

Code

Issues384

Pull requests157

Actions

Projects

Security and quality2

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

pydantic/pydantic-ai

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
1,899 Commits

1,899 Commits

.claude

.claude

.gemini

.gemini

.github

.github

agent_docs

agent_docs

clai

clai

docs-site

docs-site

docs

docs

examples

examples

pydantic_ai_slim

pydantic_ai_slim

pydantic_evals

pydantic_evals

pydantic_graph

pydantic_graph

scripts

scripts

tests

tests

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

Makefile

Makefile

README.md

README.md

mkdocs.yml

mkdocs.yml

pyproject.toml

pyproject.toml

uv.lock

uv.lock

View all files

Repository files navigation

README

Contributing

MIT license

Security

GenAI Agent Framework, the Pydantic way

Documentation: ai.pydantic.dev

Pydantic AI is a Python agent framework designed to help you quickly, confidently, and painlessly build production grade applications and workflows with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic design, built on the foundation of Pydantic Validation and modern Python features like type hints.

Yet despite virtually every Python agent framework and LLM library using Pydantic Validation, when we began to use LLMs in Pydantic Logfire, we couldn't find anything that gave us the same feeling.

We built Pydantic AI with one simple aim: to bring that FastAPI feeling to GenAI app and agent development.

Why use Pydantic AI

Built by the Pydantic Team:
Pydantic Validation is the validation layer of the OpenAI SDK, the Google ADK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more. Why use the derivative when you can go straight to the source? 😃

Model-agnostic:
Supports virtually every model and provider: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, and Perplexity; Azure AI Foundry, Amazon Bedrock, Google Vertex AI, Ollama, LiteLLM, Groq, OpenRouter, Together AI, Fireworks AI, Cerebras, Hugging Face, GitHub, Heroku, Vercel, Nebius, OVHcloud, Alibaba Cloud, SambaNova, and Outlines. If your favorite model or provider is not listed, you can easily implement a custom model.

Seamless Observability:
Tightly integrates with Pydantic Logfire, our general-purpose OpenTelemetry observability platform, for real-time debugging, evals-based performance monitoring, and behavior, tracing, and cost tracking. If you already have an observability platform that supports OTel, you can use that too.

Fully Type-safe:
Designed to give your IDE or AI coding agent as much context as possible for auto-completion and type checking, moving entire classes of errors from runtime to write-time for a bit of that Rust "if it compiles, it works" feel.

Powerful Evals:
Enables you to systematically test and evaluate the performance and accuracy of the agentic systems you build, and monitor the performance over time in Pydantic Logfire.

Extensible by Design:
Build agents from composable capabilities that bundle tools, hooks, instructions, and model settings into reusable units. Use built-in capabilities for web search, thinking, and MCP, build your own, or install third-party capability packages. Define agents entirely in YAML/JSON — no code required.

MCP, A2A, and UI:
Integrates the Model Context Protocol, Agent2Agent, and various UI event stream standards to give your agent access to external tools and data, let it interoperate with other agents, and build interactive applications with streaming event-based communication.

Human-in-the-Loop Tool Approval:
Easily lets you flag that certain tool calls require approval before they can proceed, possibly depending on tool call arguments, conversation history, or user preferences.

Durable Execution:
Enables you to build durable agents that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability.

Streamed Outputs:
Provides the ability to stream structured output continuously, with immediate validation, ensuring real time access to generated data.

Graph Support:
Provides a powerful way to define graphs using type hints, for use in complex applications where standard control flow can degrade to spaghetti code.

Realistically though, no list is going to be as convincing as giving it a try and seeing how it makes you feel!

Hello World Example

Here's a minimal example of Pydantic AI:

frompydantic_aiimportAgent# Define a very simple agent including the model to use, you can also set the model when running the agent.agent=Agent(
 'anthropic:claude-sonnet-4-6',
 # Register static instructions using a keyword argument to the agent.# For more complex dynamically-generated instructions, see the example below.instructions='Be concise, reply with one sentence.',
)

# Run the agent synchronously, conducting a conversation with the LLM.result=agent.run_sync('Where does "hello world" come from?')
print(result.output)
"""The first known use of "hello, world" was in a 1974 textbook about the C programming language."""

(This example is complete, it can be run "as is", assuming you've installed the 
pydantic_ai
 package)

The exchange will be very short: Pydantic AI will send the instructions and the user prompt to the LLM, and the model will return a text response.

Not very interesting yet, but we can easily add tools, dynamic instructions, structured outputs, or composable capabilities to build more powerful agents.

Here's the same agent with thinking and web search capabilities:

frompydantic_aiimportAgentfrompydantic_ai.capabilitiesimportThinking, WebSearchagent=Agent(
 'anthropic:claude-sonnet-4-6',
 instructions='Be concise, reply with one sentence.',
 capabilities=[Thinking(), WebSearch()],
)

result=agent.run_sync('What was the mass of the largest meteorite found this year?')
print(result.output)

Tools & Dependency Injection Example

Here is a concise example using Pydantic AI to build a support agent for a bank:

(Better documented example in the docs)

fromdataclassesimportdataclassfrompydanticimportBaseModel, Fieldfrompydantic_aiimportAgent, RunContextfrombank_databaseimportDatabaseConn# SupportDependencies is used to pass data, connections, and logic into the model that will be needed when running# instructions and tool functions. Dependency injection provides a type-safe way to customise the behavior of your agents.@dataclassclassSupportDependencies:
 customer_id: intdb: DatabaseConn# This Pydantic model defines the structure of the output returned by the agent.classSupportOutput(BaseModel):
 support_advice: str=Field(description='Advice returned to the customer')
 block_card: bool=Field(description="Whether to block the customer's card")
 risk: int=Field(description='Risk level of query', ge=0, le=10)

# This agent will act as first-tier support in a bank.# Agents are generic in the type of dependencies they accept and the type of output they return.# In this case, the support agent has type `Agent[SupportDependencies, SupportOutput]`.support_agent=Agent(
 'openai:gpt-5.2',
 deps_type=SupportDependencies,
 # The response from the agent will, be guaranteed to be a SupportOutput,# if validation fails the agent is prompted to try again.output_type=SupportOutput,
 instructions=(
 'You are a support agent in our bank, give the ''customer support and judge the risk level of their query.'
 ),
)

# Dynamic instructions can make use of dependency injection.# Dependencies are carried via the `RunContext` argument, which is parameterized with the `deps_type` from above.# If the type annotation here is wrong, static type checkers will catch it.@support_agent.instructionsasyncdefadd_customer_name(ctx: RunContext[SupportDependencies]) ->str:
 customer_name=awaitctx.deps.db.customer_name(id=ctx.deps.customer_id)
 returnf"The customer's name is {customer_name!r}"# The `tool` decorator let you register functions which the LLM may call while responding to a user.# Again, dependencies are carried via `RunContext`, any other arguments become the tool schema passed to the LLM.# Pydantic is used to validate these arguments, and errors are passed back to the LLM so it can retry.@support_agent.toolasyncdefcustomer_balance(
 ctx: RunContext[SupportDependencies], include_pending: bool
) ->float:
 """Returns the customer's current account balance."""# The docstring of a tool is also passed to the LLM as the description of the tool.# Parameter descriptions are extracted from the docstring and added to the parameter schema sent to the LLM.balance=awaitctx.deps.db.customer_balance(
 id=ctx.deps.customer_id,
 include_pending=include_pending,
 )
 returnbalance

... # In a real use case, you'd add more tools and a longer system promptasyncdefmain():
 deps=SupportDependencies(customer_id=123, db=DatabaseConn())
 # Run the agent asynchronously, conducting a conversation with the LLM until a final response is reached.# Even in this fairly simple case, the agent will exchange multiple messages with the LLM as tools are called to retrieve an output.result=awaitsupport_agent.run('What is my balance?', deps=deps)
 # The `result.output` will be validated with Pydantic to guarantee it is a `SupportOutput`. Since the agent is generic,# it'll also be typed as a `SupportOutput` to aid with static type checking.print(result.output)
 """ support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1 """result=awaitsupport_agent.run('I just lost my card!', deps=deps)
 print(result.output)
 """ support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8 """

Next Steps

To try Pydantic AI for yourself, install it and follow the instructions in the examples.

Read the docs to learn more about building applications with Pydantic AI.

Read the API Reference to understand Pydantic AI's interface.

Join Slack or file an issue on GitHub if you have any questions.

About

 AI Agent Framework, the Pydantic way
 

ai.pydantic.dev

Topics

 python

 pydantic

 agent-framework

 llm

 genai

Resources

 Readme

License

 MIT license
 

Contributing

 Contributing
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

16.2k
 stars

Watchers

101
 watching

Forks

1.9k
 forks

 Report repository

Releases
 228

v1.79.0 (2026-04-09)
 Latest

Apr 10, 2026

+ 227 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.7%

Other0.3%

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
