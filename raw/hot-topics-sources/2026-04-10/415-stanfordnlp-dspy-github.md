---
title: GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models · GitHub
source_url: https://github.com/stanfordnlp/dspy
final_url: https://github.com/stanfordnlp/dspy
status: 200
content_type: text/html; charset=utf-8
topics: [DSPy + GEPA optimize_anything]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:24.674817+00:00
---

# GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models · GitHub

## 원본 URL

https://github.com/stanfordnlp/dspy

## 추출 본문

GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models · GitHub

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

 stanfordnlp
/dspyPublic

Notifications
You must be signed in to change notification settings

Fork
 2.8k

 Star
33.6k

Code

Issues296

Pull requests182

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

stanfordnlp/dspy

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
4,438 Commits

4,438 Commits

.github

.github

docs

docs

dspy

dspy

tests

tests

.gitignore

.gitignore

.pre-commit-config.yaml

.pre-commit-config.yaml

CONTRIBUTING.md

CONTRIBUTING.md

LICENSE

LICENSE

README.md

README.md

SECURITY.md

SECURITY.md

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

DSPy: Programming—not prompting—Foundation Models

Documentation:DSPy Docs

DSPy is the framework for programming—rather than prompting—language models. It allows you to iterate fast on building modular AI systems and offers algorithms for optimizing their prompts and weights, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops.

DSPy stands for Declarative Self-improving Python. Instead of brittle prompts, you write compositional Python code and use DSPy to teach your LM to deliver high-quality outputs. Learn more via our official documentation site or meet the community, seek help, or start contributing via this GitHub repo and our Discord server.

Documentation: dspy.ai

Please go to the DSPy Docs at dspy.ai

Installation

pip install dspy

To install the very latest from 
main
:

pip install git+https://github.com/stanfordnlp/dspy.git

📜 Citation & Reading More

If you're looking to understand the framework, please go to the DSPy Docs at dspy.ai.

If you're looking to understand the underlying research, this is a set of our papers:

[Jul'25] GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
[Jun'24] Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs
[Oct'23] DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

[Jul'24] Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together

[Jun'24] Prompts as Auto-Optimized Training Hyperparameters

[Feb'24] Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models

[Jan'24] In-Context Learning for Extreme Multi-Label Classification

[Dec'23] DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines

[Dec'22] Demonstrate-Search-Predict: Composing Retrieval & Language Models for Knowledge-Intensive NLP

To stay up to date or learn more, follow @DSPyOSS on Twitter or the DSPy page on LinkedIn.

The DSPy logo is designed by Chuyi Zhang.

If you use DSPy or DSP in a research paper, please cite our work as follows:

@inproceedings{khattab2024dspy,
 title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
 author={Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and Vardhamanan, Sri and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas T. and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher},
 journal={The Twelfth International Conference on Learning Representations},
 year={2024}
}
@article{khattab2022demonstrate,
 title={Demonstrate-Search-Predict: Composing Retrieval and Language Models for Knowledge-Intensive {NLP}},
 author={Khattab, Omar and Santhanam, Keshav and Li, Xiang Lisa and Hall, David and Liang, Percy and Potts, Christopher and Zaharia, Matei},
 journal={arXiv preprint arXiv:2212.14024},
 year={2022}
}

About

 DSPy: The framework for programming—not prompting—language models
 

dspy.ai

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

33.6k
 stars

Watchers

195
 watching

Forks

2.8k
 forks

 Report repository

Releases
 106

3.1.3
 Latest

Feb 5, 2026

+ 105 releases

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.3%

JavaScript0.7%

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
