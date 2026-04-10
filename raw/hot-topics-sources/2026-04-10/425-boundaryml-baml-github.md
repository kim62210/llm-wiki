---
title: GitHub - BoundaryML/baml: The AI framework that adds the engineering to prompt engineering (Python/TS/Ruby/Java/C#/Rust/Go compatible) · GitHub
source_url: https://github.com/BoundaryML/baml
final_url: https://github.com/BoundaryML/baml
status: 200
content_type: text/html; charset=utf-8
topics: [BAML (Boundary ML) — Prompts as Typed Functions]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:26.744267+00:00
---

# GitHub - BoundaryML/baml: The AI framework that adds the engineering to prompt engineering (Python/TS/Ruby/Java/C#/Rust/Go compatible) · GitHub

## 원본 URL

https://github.com/BoundaryML/baml

## 추출 본문

GitHub - BoundaryML/baml: The AI framework that adds the engineering to prompt engineering (Python/TS/Ruby/Java/C#/Rust/Go compatible) · GitHub

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

 BoundaryML
/bamlPublic

Notifications
You must be signed in to change notification settings

Fork
 406

 Star
7.9k

Code

Issues180

Pull requests67

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

BoundaryML/baml

canary

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
2,958 Commits

2,958 Commits

.cursor/rules

.cursor/rules

.devcontainer

.devcontainer

.github

.github

.vscode

.vscode

baml-cli

baml-cli

baml

baml

baml_language

baml_language

beps

beps

ci

ci

docs

docs

engine

engine

fern

fern

integ-tests

integ-tests

jetbrains

jetbrains

jobs

jobs

languages

languages

patches

patches

release

release

scripts

scripts

tools

tools

typescript

typescript

typescript2

typescript2

.actrc

.actrc

.dockerignore

.dockerignore

.envrc

.envrc

.gitattributes

.gitattributes

.gitconfig

.gitconfig

.gitignore

.gitignore

.infisical.json

.infisical.json

.pre-commit-config.yaml

.pre-commit-config.yaml

CHANGELOG.md

CHANGELOG.md

CITATION.cff

CITATION.cff

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

README-DEV.md

README-DEV.md

README.md

README.md

baml_language.code-workspace

baml_language.code-workspace

biome.json

biome.json

cliff.toml

cliff.toml

codecov.yml

codecov.yml

flake.lock

flake.lock

flake.nix

flake.nix

go.mod

go.mod

go.sum

go.sum

justfile

justfile

mise.toml

mise.toml

package.json

package.json

pnpm-lock.yaml

pnpm-lock.yaml

pnpm-workspace.yaml

pnpm-workspace.yaml

root-wasm32.code-workspace

root-wasm32.code-workspace

root.code-workspace

root.code-workspace

rust-toolchain.toml

rust-toolchain.toml

test_git_date.txt

test_git_date.txt

thoughts

thoughts

turbo.json

turbo.json

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

BAML: Basically a Made-up Language

Homepage | Docs | BAML AI Chat | Discord

BAML is a simple prompting language for building reliable AI workflows and agents.

BAML makes prompt engineering easy by turning it into schema engineering -- where you mostly focus on the models of your prompt -- to get more reliable outputs.
You don't need to write your whole app in BAML, only the prompts! You can wire-up your LLM Functions in any language of your choice! See our quickstarts for Python, TypeScript, Ruby and Go, and more.

BAML comes with all batteries included -- with full typesafety, streaming, retries, wide model support, even when they don't support native tool-calling APIs

Try BAML: Prompt Fiddle • Interactive App Examples

The core BAML principle: LLM Prompts are functions

The fundamental building block in BAML is a function. Every prompt is a function that takes in parameters and returns a type.

function ChatAgent(message:Message[], tone:"happy" | "sad") -> string

Every function additionally defines which models it uses and what its prompt is.

function ChatAgent(message:Message[], tone:"happy" | "sad") -> StopTool | ReplyTool{
 client "openai/gpt-4o-mini"

 prompt #" Be a {{ tone }} bot. {{ ctx.output_format }} {% for m in message %} {{ _.role(m.role) }} {{ m.content }} {% endfor %} "#
}

class Message{
 role string
 content string
}

class ReplyTool{
 response string
}

class StopTool{
 action "stop" @description(#" when it might be a good time to end the conversation "#)}

BAML Functions can be called from any language

Below we call the ChatAgent function we defined in BAML through Python. BAML's Rust compiler generates a "baml_client" to access and call them.

frombaml_clientimportbfrombaml_client.typesimportMessage, StopToolmessages= [Message(role="assistant", content="How can I help?")]

whileTrue:
 print(messages[-1].content)
 user_reply=input()
 messages.append(Message(role="user", content=user_reply))
 tool=b.ChatAgent(messages, "happy")
 ifisinstance(tool, StopTool):
 print("Goodbye!")
 breakelse:
 messages.append(Message(role="assistant", content=tool.response))

You can write any kind of agent or workflow using chained BAML functions. An agent is a while loop that calls a Chat BAML Function with some state.

And if you need to stream, add a couple more lines:

stream=b.stream.ChatAgent(messages, "happy")
# partial is a Partial type with all Optional fieldsfortoolinstream:
 ifisinstance(tool, StopTool):
 ...
 
final=stream.get_final_response()

And get fully type-safe outputs for each chunk in the stream.

Test prompts 10x faster, right in your IDE

BAML comes with native tooling for VS Code and JetBrains IDEs, with support for other editors continuing to expand.

Visualize full prompt (including any multi-modal assets), and the API request. BAML gives you full transparency and control of the prompt.

Using AI is all about iteration speed.

If testing your pipeline takes 2 minutes, you can only test 10 ideas in 20 minutes.

If you reduce it to 5 seconds, you can test 240 ideas in the same amount of time.

The playground also allows you to run tests in parallel -- for even faster iteration speeds 🚀.

No need to login to websites, and no need to manually define json schemas.

Enable reliable tool-calling with any model

BAML works even when the models don't support native tool-calling APIs. We created the SAP (schema-aligned parsing) algorithm to support the flexible outputs LLMs can provide, like markdown within a JSON blob or chain-of-thought prior to answering. Read more about SAP

With BAML, your structured outputs work in Day-1 of a model release. No need to figure out whether a model supports parallel tool calls, or whether it supports recursive schemas, or 
anyOf
 or 
oneOf
 etc.

See it in action with: Deepseek-R1 and OpenAI O1.

Switch from 100s of models in a couple lines

function Extract() -> Resume {
+ client openai/o3-mini
 prompt #"
 ....
 "#
}

Retry policies • fallbacks • model rotations. All statically defined.

Want to do pick models at runtime? Check out the Client Registry.

We support: OpenAI • Anthropic • Gemini • Vertex • Bedrock • Azure OpenAI • Anything OpenAI Compatible (Ollama, OpenRouter, VLLM, LMStudio, TogetherAI, and more)

Build beautiful streaming UIs

BAML generates a ton of utilities for NextJS, Python (and any language) to make streaming UIs easy.

BAML's streaming interfaces are fully type-safe. Check out the Streaming Docs, and our React hooks

Fully Open-Source, and offline

100% open-source (Apache 2)

100% private. AGI will not require an internet connection, neither will BAML

No network requests beyond model calls you explicitly set

Not stored or used for any training data

BAML files can be saved locally on your machine and checked into Github for easy diffs.

Built in Rust. So fast, you can't even tell it's there.

BAML's Design Philosophy

Everything is fair game when making new syntax. If you can code it, it can be yours. This is our design philosophy to help restrict ideas:

1: Avoid invention when possible

Yes, prompts need versioning — we have a great versioning tool: git

Yes, you need to save prompts — we have a great storage tool: filesystems

2: Any file editor and any terminal should be enough to use it

3: Be fast

4: A first year university student should be able to understand it

Why a new programming language

We used to write websites like this:

defhome():
 return"<button onclick=\"() => alert(\\\"hello!\\\")\">Click</button>"

And now we do this:

functionHome(){return<buttononClick={()=>setCount(prev=>prev+1)}>{count} clicks!
 </button>}

New syntax can be incredible at expressing new ideas. Plus the idea of maintaining hundreds of f-strings for prompts kind of disgusts us 🤮. Strings are bad for maintainable codebases. We prefer structured strings.

The goal of BAML is to give you the expressiveness of English, but the structure of code.

Full blog post by us.

Conclusion

As models get better, we'll continue expecting even more out of them. But what will never change is that we'll want a way to write maintainable code that uses those models. The current way we all just assemble strings is very reminiscent of the early days PHP/HTML soup in web development. We hope some of the ideas we shared today can make a tiny dent in helping us all shape the way we all code tomorrow.

FAQ

Do I need to write my whole app in BAML?Nope, only the prompts! BAML translates definitions into the language of your choice! Python, TypeScript, Ruby and more.Is BAML stable?Yes, many companies use it in production! We ship updates weekly!Why a new language?Jump to section

Contributing

Checkout our guide on getting started

Citation

You can cite the BAML repo as follows:

@software{baml,
 author = {Boundary ML},
 title = {BAML},
 url = {https://github.com/boundaryml/baml},
 year = {2024}
}

Made with ❤️ by Boundary

HQ in Seattle, WA

P.S. We're hiring for software engineers that love rust. Email us or reach out on discord!

About

 The AI framework that adds the engineering to prompt engineering (Python/TS/Ruby/Java/C#/Rust/Go compatible)
 

docs.boundaryml.com

Topics

 playground

 vscode

 prompt

 structured-data

 structured-output

 baml

 guardrails

 llm

 llm-playground

 boundaryml

 structured-generation

 prompt-config

 prompt-templates

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

7.9k
 stars

Watchers

31
 watching

Forks

406
 forks

 Report repository

Releases
 316

0.220.0
 Latest

Mar 11, 2026

+ 315 releases

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

Rust67.4%

TypeScript15.2%

Python4.3%

MDX3.8%

JavaScript3.3%

Go2.3%

Other3.7%

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
