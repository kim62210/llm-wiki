---
title: GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub
source_url: https://github.com/guidance-ai/llguidance
final_url: https://github.com/guidance-ai/llguidance
status: 200
content_type: text/html; charset=utf-8
topics: [XGrammar-2 Constrained Decoding for Agentic LLMs]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:40.517241+00:00
---

# GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub

## 원본 URL

https://github.com/guidance-ai/llguidance

## 추출 본문

GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub

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

 guidance-ai
/llguidancePublic

Notifications
You must be signed in to change notification settings

Fork
 61

 Star
729

Code

Issues34

Pull requests11

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

guidance-ai/llguidance

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
1,527 Commits

1,527 Commits

.config

.config

.github/workflows

.github/workflows

c_sample

c_sample

docs

docs

json_schema_test_suite

json_schema_test_suite

json_stats

json_stats

llg_test_utils

llg_test_utils

parser

parser

python

python

python_ext

python_ext

sample_parser

sample_parser

scripts

scripts

toktrie

toktrie

toktrie_hf_downloader

toktrie_hf_downloader

toktrie_hf_tokenizers

toktrie_hf_tokenizers

toktrie_tiktoken

toktrie_tiktoken

.gitignore

.gitignore

CHANGELOG.md

CHANGELOG.md

CODE_OF_CONDUCT.md

CODE_OF_CONDUCT.md

Cargo.lock

Cargo.lock

Cargo.toml

Cargo.toml

LICENSE

LICENSE

README.md

README.md

SECURITY.md

SECURITY.md

SUPPORT.md

SUPPORT.md

plan.md

plan.md

pyproject.toml

pyproject.toml

View all files

Repository files navigation

README

Code of conduct

MIT license

Security

Low-level Guidance (llguidance)

Performance results from MaskBench

2025-06-23 llguidance is now deemed v1.0.0

2025-06-11 Making Structured Outputs Go Brrr blog post released

2025-05-20 LLGuidance shipped in OpenAI for JSON Schema

2025-04-11 integration merged into Chromium

2025-03-25 integration merged into vLLM (v0.8.2)

2025-02-26 integration merged into SGLang (v0.4.4)

2025-02-01 integration merged into llama.cpp (b4613)

2025-01-21 JSONSchemaBench released, including paper and MaskBench

2025-01-07 Guidance v0.2.0 released, using llguidance as the grammar engine

About

This library implements constrained decoding (also called constrained sampling or
structured outputs) for Large Language Models (LLMs).
It can enforce arbitrary context-free grammar on the output of LLM
and is fast - on the order of 50μs of CPU time per token
(for 128k tokenizer) with negligible startup costs.

Following grammar formats are supported:

a large subset of JSON schemas

regular expressions

context-free grammars in a variation of Lark format;
with embedded JSON schemas and regular expressions

llguidance
 - internal (JSON-based) format;
slowly being deprecated in favor of the Lark-like format

The internal format is most powerful (though Lark-like format is catching up, and there are plans to convert the libraries to use it) and can be generated by the following libraries:

Guidance (Python)

guidance.ts (TypeScript)

hopefully more to come!

The library can be used from:

Rust, sample

C and C++, sample

Python

Integrations

The library is currently integrated in:

Guidance - library for interacting with LLMs

OpenAI models - LLGuidance powers Structured Output (JSON Schema only)

llama.cpp -
available via 
-DLLAMA_LLGUIDANCE=ON
 option for 
cmake
;
llama.cpp can be also used Guidance Python package

Chromium - merged,
to be used for JSON Schema enforcement for 
window.ai
 in Chromium-based browsers

SGLang -
use 
--grammar-backend llguidance
; when passing Lark grammar make
sure to prefix them with 
%llguidance {}
, just as in llama.cpp

vLLM - V0 PR and V1 PR

LLGTRT - OpenAI-compatible REST server using NVIDIA's TensorRT-LLM

mistral.rs

onnxruntime-genai

Technical details

See Making Structured Outputs Go Brrr for an overview of the library,
including the design decisions, performance, and how it compares to other approaches.

Given a context-free grammar, a tokenizer, and a prefix of tokens, llguidance computes a token mask - a set of tokens from the tokenizer - that, when added to the current token prefix, can lead to a valid string in the language defined by the grammar. Mask computation takes approximately 50μs of single-core CPU time for a tokenizer with 128k tokens. While this timing depends on the exact grammar, it holds, for example, for grammars derived from JSON schemas. There is no significant startup cost.

The library implements a context-free grammar parser using Earley’s algorithm on top of a lexer based on derivatives of regular expressions. Mask computation is achieved by traversing the prefix tree (trie) of all possible tokens, leveraging highly optimized code.

Grammars can be also used to speed up decode via fast-forward tokens.

Comparison and performance

See MaskBench in
JSON Schema Bench for detailed performance comparisons.

LM-format-enforcer and llama.cpp grammars are similar to llguidance in that they dynamically build token masks for every step of the decoding process. Both are significantly slower - the former due to clean Python code and the latter due to the lack of a lexer and use of a backtracking parser, which, while elegant, is inefficient.

Outlines builds an automaton from constraints and then pre-computes token masks for all automaton states, potentially making sampling fast but inherently limiting constraint complexity and introducing significant startup cost and memory overhead. Llguidance computes token masks on the fly and has essentially no startup cost. The lexer’s automata in llguidance are built lazily and are typically much smaller, as the context-free grammar imposes the top-level structure.

XGrammar follows an approach similar to llama.cpp (explicit stack-based, character-level parser) with additional pre-computation of certain token masks, similar to Outlines. The pre-computation often runs into seconds, and sometimes minutes. If the pre-computation works well for a given input, the masks are computed quickly (under 8μs in half of masks we tested), however if it doesn't fit the particular input,
the mask computation times can run to tens or hundreds of milliseconds.

In llguidance, the full mask computation for a typical JSON schema takes about 1.5ms (for 128k tokenizer).
However, very often the "slicer" optimization applies,
and thus the avarage mask computation in JSON Schema Bench
(2.5M tokens, 10k schemas) is under 50μs,
with less than 1% of masks taking longer than 1ms,
and 0.001% taking longer than 10ms (but still shorter than 30ms).
The optimization doesn't involve any significant pre-computation.

Thus, with 16 cores and a 10ms forward pass, llguidance can handle batch sizes up to 3200 without slowing down the model. (Note that a 10ms forward pass for small batch sizes typically increases to 20ms+ for batch sizes of 100-200.)

Building

install rust; 1.87 or later

If you just need the C or Rust library (
llguidance
),
check the parser directory.

For Python bindings:

install python 3.10 or later; very likely you'll need a virtual env/conda

run 
./scripts/install-deps.sh

to build and after any changes, run 
./scripts/test-guidance.sh

This builds the Python bindings for the library and runs the tests
(which mostly live in the Guidance repo - it will clone it).

Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the Microsoft Open Source Code of Conduct.
For more information see the Code of Conduct FAQ or
contact opencode@microsoft.com with any additional questions or comments.

Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
Microsoft's Trademark & Brand Guidelines.
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

About

 Super-fast Structured Outputs
 

Resources

 Readme

License

 MIT license
 

Code of conduct

 Code of conduct
 

Security policy

 Security policy
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

729
 stars

Watchers

7
 watching

Forks

61
 forks

 Report repository

Releases
91tags

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

Rust86.2%

Python9.4%

C1.9%

Shell1.3%

C++0.7%

JavaScript0.5%

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
