---
title: GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub
source_url: https://github.com/lancedb/lancedb
final_url: https://github.com/lancedb/lancedb
status: 200
content_type: text/html; charset=utf-8
topics: [Serverless Object-Storage Vector DBs (Turbopuffer 등)]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:55.273526+00:00
---

# GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub

## 원본 URL

https://github.com/lancedb/lancedb

## 추출 본문

GitHub - lancedb/lancedb: Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less. · GitHub

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

 lancedb
/lancedbPublic

Notifications
You must be signed in to change notification settings

Fork
 827

 Star
9.9k

Code

Issues548

Pull requests87

Discussions

Actions

Projects

Wiki

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Discussions

 Actions

 Projects

 Wiki

 Security and quality

 Insights

lancedb/lancedb

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
2,423 Commits

2,423 Commits

.cargo

.cargo

.github

.github

ci

ci

dockerfiles

dockerfiles

docs

docs

java

java

nodejs

nodejs

python

python

rust

rust

.bumpversion.toml

.bumpversion.toml

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

Cargo.lock

Cargo.lock

Cargo.toml

Cargo.toml

LICENSE

LICENSE

Makefile

Makefile

README.md

README.md

RUST_THIRD_PARTY_LICENSES.html

RUST_THIRD_PARTY_LICENSES.html

about.hbs

about.hbs

about.toml

about.toml

docker-compose.yml

docker-compose.yml

pyright_report.csv

pyright_report.csv

release_process.md

release_process.md

rust-toolchain.toml

rust-toolchain.toml

View all files

Repository files navigation

README

Contributing

Apache-2.0 license

The Multimodal AI Lakehouse

How to Install ✦ Detailed Documentation ✦ Tutorials and Recipes ✦ Contributors

The ultimate multimodal data platform for AI/ML applications.

LanceDB is designed for fast, scalable, and production-ready vector search. It is built on top of the Lance columnar format. You can store, index, and search over petabytes of multimodal data and vectors with ease.
LanceDB is a central location where developers can build, train and analyze their AI workloads.

Demo: Multimodal Search by Keyword, Vector or with SQL

Star LanceDB to get updates!

⭐ Click here ⭐ to see how fast we're growing!

Key Features:

Fast Vector Search: Search billions of vectors in milliseconds with state-of-the-art indexing.

Comprehensive Search: Support for vector similarity search, full-text search and SQL.

Multimodal Support: Store, query and filter vectors, metadata and multimodal data (text, images, videos, point clouds, and more).

Advanced Features: Zero-copy, automatic versioning, manage versions of your data without needing extra infrastructure. GPU support in building vector index.

Products:

Open Source & Local: 100% open source, runs locally or in your cloud. No vendor lock-in.

Cloud and Enterprise: Production-scale vector search with no servers to manage. Complete data sovereignty and security.

Ecosystem:

Columnar Storage: Built on the Lance columnar format for efficient storage and analytics.

Seamless Integration: Python, Node.js, Rust, and REST APIs for easy integration. Native Python and Javascript/Typescript support.

Rich Ecosystem: Integrations with LangChain 🦜️🔗, LlamaIndex 🦙, Apache-Arrow, Pandas, Polars, DuckDB and more on the way.

How to Install:

Follow the Quickstart doc to set up LanceDB locally.

API & SDK: We also support Python, Typescript and Rust SDKs
InterfaceDocumentationPython SDKhttps://lancedb.github.io/lancedb/python/python/Typescript SDKhttps://lancedb.github.io/lancedb/js/globals/Rust SDKhttps://docs.rs/lancedb/latest/lancedb/index.htmlREST APIhttps://docs.lancedb.com/api-reference/rest

Join Us and Contribute

We welcome contributions from everyone! Whether you're a developer, researcher, or just someone who wants to help out.

If you have any suggestions or feature requests, please feel free to open an issue on GitHub or discuss it on our Discord server.

Check out the GitHub Issues if you would like to work on the features that are planned for the future. If you have any suggestions or feature requests, please feel free to open an issue on GitHub.

Contributors

Stay in Touch With Us

About

 Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less.
 

lancedb.com/docs

Topics

 search-engine

 nearest-neighbor-search

 image-search

 recommender-system

 approximate-nearest-neighbor-search

 semantic-search

 similarity-search

 vector-database

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

9.9k
 stars

Watchers

49
 watching

Forks

827
 forks

 Report repository

Releases
 406

Python LanceDB v0.31.0-beta.1
 Latest

Apr 5, 2026

+ 405 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors
 188

+ 174 contributors

Languages

HTML40.6%

Rust28.4%

Python23.2%

TypeScript7.4%

Shell0.3%

Java0.1%

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
