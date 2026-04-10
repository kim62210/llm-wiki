---
title: GitHub - 567-labs/instructor: structured outputs for llms · GitHub
source_url: https://github.com/567-labs/instructor
final_url: https://github.com/567-labs/instructor
status: 200
content_type: text/html; charset=utf-8
topics: [Instructor (Multi-Language Structured Outputs)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:30.041305+00:00
---

# GitHub - 567-labs/instructor: structured outputs for llms · GitHub

## 원본 URL

https://github.com/567-labs/instructor

## 추출 본문

GitHub - 567-labs/instructor: structured outputs for llms · GitHub

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

 567-labs
/instructorPublic

 Uh oh!

There was an error while loading. Please reload this page.

Notifications
You must be signed in to change notification settings

Fork
 1k

 Star
12.7k

Code

Issues10

Pull requests16

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

567-labs/instructor

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
1,546 Commits

1,546 Commits

.cursor/rules

.cursor/rules

.github

.github

.grit

.grit

docs

docs

examples

examples

instructor

instructor

scripts

scripts

tests

tests

.coveragerc

.coveragerc

.cursorignore

.cursorignore

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

.ruff.toml

.ruff.toml

AGENT.md

AGENT.md

CHANGELOG.md

CHANGELOG.md

CLAUDE.md

CLAUDE.md

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

NEW_PROVIDER_AGENT_INSTRUCTIONS.md

NEW_PROVIDER_AGENT_INSTRUCTIONS.md

README.md

README.md

build_mkdocs.sh

build_mkdocs.sh

cross_link_mapping.yaml

cross_link_mapping.yaml

ellipsis.yaml

ellipsis.yaml

github_issue.md

github_issue.md

mkdocs.yml

mkdocs.yml

pyproject.toml

pyproject.toml

requirements-doc.txt

requirements-doc.txt

requirements-examples.txt

requirements-examples.txt

requirements.txt

requirements.txt

sitemap.yaml

sitemap.yaml

ty-tests.toml

ty-tests.toml

ty.toml

ty.toml

uv.lock

uv.lock

View all files

Repository files navigation

README

Contributing

MIT license

Instructor: Structured Outputs for LLMs

Get reliable JSON from any LLM. Built on Pydantic for validation, type safety, and IDE support.

importinstructorfrompydanticimportBaseModel# Define what you wantclassUser(BaseModel):
 name: strage: int# Extract it from natural languageclient=instructor.from_provider("openai/gpt-4o-mini")
user=client.chat.completions.create(
 response_model=User,
 messages=[{"role": "user", "content": "John is 25 years old"}],
)

print(user) # User(name='John', age=25)

That's it. No JSON parsing, no error handling, no retries. Just define a model and get structured data.

Use Instructor for fast extraction, reach for PydanticAI when you need agents. Instructor keeps schema-first flows simple and cheap. If your app needs richer agent runs, built-in observability, or shareable traces, try PydanticAI. PydanticAI is the official agent runtime from the Pydantic team, adding typed tools, replayable datasets, evals, and production dashboards while using the same Pydantic models. Dive into the PydanticAI docs to see how it extends Instructor-style workflows.

Why Instructor?

Getting structured data from LLMs is hard. You need to:

Write complex JSON schemas

Handle validation errors

Retry failed extractions

Parse unstructured responses

Deal with different provider APIs

Instructor handles all of this with one simple interface:
Without InstructorWith Instructor

response=openai.chat.completions.create(
 model="gpt-4",
 messages=[{"role": "user", "content": "..."}],
 tools=[
 {
 "type": "function",
 "function": {
 "name": "extract_user",
 "parameters": {
 "type": "object",
 "properties": {
 "name": {"type": "string"},
 "age": {"type": "integer"},
 },
 },
 },
 }
 ],
)

# Parse responsetool_call=response.choices[0].message.tool_calls[0]
user_data=json.loads(tool_call.function.arguments)

# Validate manuallyif"name"notinuser_data:
 # Handle error...pass

client=instructor.from_provider("openai/gpt-4")

user=client.chat.completions.create(
 response_model=User,
 messages=[{"role": "user", "content": "..."}],
)

# That's it! user is validated and typed

Install in seconds

pip install instructor

Or with your package manager:

uv add instructor
poetry add instructor

Works with every major provider

Use the same code with any LLM provider:

# OpenAIclient=instructor.from_provider("openai/gpt-4o")

# Anthropicclient=instructor.from_provider("anthropic/claude-3-5-sonnet")

# Googleclient=instructor.from_provider("google/gemini-pro")

# Ollama (local)client=instructor.from_provider("ollama/llama3.2")

# With API keys directly (no environment variables needed)client=instructor.from_provider("openai/gpt-4o", api_key="sk-...")
client=instructor.from_provider("anthropic/claude-3-5-sonnet", api_key="sk-ant-...")
client=instructor.from_provider("groq/llama-3.1-8b-instant", api_key="gsk_...")

# All use the same API!user=client.chat.completions.create(
 response_model=User,
 messages=[{"role": "user", "content": "..."}],
)

Production-ready features

Automatic retries

Failed validations are automatically retried with the error message:

frompydanticimportBaseModel, field_validatorclassUser(BaseModel):
 name: strage: int@field_validator('age')defvalidate_age(cls, v):
 ifv<0:
 raiseValueError('Age must be positive')
 returnv# Instructor automatically retries when validation failsuser=client.chat.completions.create(
 response_model=User,
 messages=[{"role": "user", "content": "..."}],
 max_retries=3,
)

Streaming support

Stream partial objects as they're generated:

frominstructorimportPartialforpartial_userinclient.chat.completions.create(
 response_model=Partial[User],
 messages=[{"role": "user", "content": "..."}],
 stream=True,
):
 print(partial_user)
 # User(name=None, age=None)# User(name="John", age=None)# User(name="John", age=25)

Nested objects

Extract complex, nested data structures:

fromtypingimportListclassAddress(BaseModel):
 street: strcity: strcountry: strclassUser(BaseModel):
 name: strage: intaddresses: List[Address]

# Instructor handles nested objects automaticallyuser=client.chat.completions.create(
 response_model=User,
 messages=[{"role": "user", "content": "..."}],
)

Used in production by

Trusted by over 100,000 developers and companies building AI applications:

3M+ monthly downloads

10K+ GitHub stars

1000+ community contributors

Companies using Instructor include teams at OpenAI, Google, Microsoft, AWS, and many YC startups.

Get started

Basic extraction

Extract structured data from any text:

frompydanticimportBaseModelimportinstructorclient=instructor.from_provider("openai/gpt-4o-mini")

classProduct(BaseModel):
 name: strprice: floatin_stock: boolproduct=client.chat.completions.create(
 response_model=Product,
 messages=[{"role": "user", "content": "iPhone 15 Pro, $999, available now"}],
)

print(product)
# Product(name='iPhone 15 Pro', price=999.0, in_stock=True)

Multiple languages

Instructor's simple API is available in many languages:

Python - The original

TypeScript - Full TypeScript support

Ruby - Ruby implementation

Go - Go implementation

Elixir - Elixir implementation

Rust - Rust implementation

Learn more

Documentation - Comprehensive guides

Examples - Copy-paste recipes

Blog - Tutorials and best practices

Discord - Get help from the community

Why use Instructor over alternatives?

vs Raw JSON mode: Instructor provides automatic validation, retries, streaming, and nested object support. No manual schema writing.

vs LangChain/LlamaIndex: Instructor is focused on one thing - structured extraction. It's lighter, faster, and easier to debug.

vs Custom solutions: Battle-tested by thousands of developers. Handles edge cases you haven't thought of yet.

Contributing

We welcome contributions! Check out our good first issues to get started.

License

MIT License - see LICENSE for details.

Built by the Instructor community. Special thanks to Jason Liu and all contributors.

About

 structured outputs for llms 
 

python.useinstructor.com/

Topics

 python

 validation

 openai

 openai-functions

 pydantic-v2

 openai-function-calli

Resources

 Readme

License

 MIT license
 

Contributing

 Contributing
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

12.7k
 stars

Watchers

53
 watching

Forks

1k
 forks

 Report repository

Releases
 108

v1.15.1
 Latest

Apr 3, 2026

+ 107 releases

Sponsor this project

 Sponsor

 Uh oh!

There was an error while loading. Please reload this page.

Learn more about GitHub Sponsors

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

Python100.0%

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
