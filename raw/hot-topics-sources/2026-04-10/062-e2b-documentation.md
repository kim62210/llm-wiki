---
title: Documentation - E2B
source_url: https://e2b.dev/docs
final_url: https://e2b.dev/docs
status: 200
content_type: text/html; charset=utf-8
topics: [Firecracker/microVM Sandboxes for Agent Code Execution]
sections: [Harness Engineering]
fetched_at: 2026-04-10T01:43:33.426676+00:00
---

# Documentation - E2B

## 원본 URL

https://e2b.dev/docs

## 추출 본문

Documentation - E2B

Skip to main content

E2B Docs home page

Search...

⌘K

Documentation

SDK Reference

API reference

Getting started

Home

Quickstart

API key

Cookbook

Need help?

Billing

Use cases

Coding Agents

Computer use

GitHub Actions CI/CD

Agents in sandbox

Amp

Claude Code

Codex

OpenClaw

OpenCode

Code interpreting

Analyze data with AI

Charts & visualizations

Streaming

Code contexts

Supported languages

Sandbox

Lifecycle

Lifecycle events API

Lifecycle events webhooks

Persistence

Snapshots

AutoResume

Git integration

Metrics

Metadata

Environment variables

List sandboxes

Connect to running sandbox

Internet access

Interactive terminal

SSH access

Connecting storage bucket

Rate limits

Secured access

Proxy tunneling

Custom domain

Templates

Quickstart

How it works

User and workdir

Caching

Base image

Private registries

Defining template

Start & ready commands

Build

Names

Tags & versioning

Logging

Error handling

Examples

V2 migration guide

Filesystem

Overview

Read & write

File & directory metadata

Watch directory for changes

Upload data

Download data

Volumes

Overview

Managing volumes

Mounting volumes

Read & write

File & directory metadata

Upload data

Download data

Commands

Overview

Streaming

Run commands in background

MCP gateway

Overview

Quickstart

Available servers

Custom templates

Custom servers

Examples

CLI

Installation

Authentication

List sandboxes

Create sandbox

Connect to sandbox

Execute commands in sandbox

Shutdown running sandboxes

Deployment

Bring Your Own Cloud

Migration

SDK v2 migration guide

Troubleshooting

Build authentication error

The sandbox is running but port is not open - 49999

pip install fails during template build

Dashboard

e2b-dev/e2b

E2B Docs home page

Search...

⌘KAsk AI

Dashboard

e2b-dev/e2b

e2b-dev/e2b

Search...

Navigation

Getting started

E2B Documentation

Getting started

E2B Documentation

Copy page

Copy page

​

What is E2B?
E2B provides isolated sandboxes that let agents safely execute code, process data, and run tools. Our SDKs make it easy to start and manage these environments.Start a sandbox and run code in a few lines:

JavaScript & TypeScript

Python

npm i e2b

JavaScript & TypeScript

Python

import { Sandbox } from 'e2b'const sandbox = await Sandbox.create() // Needs E2B_API_KEY environment variableconst result = await sandbox.commands.run('echo "Hello from E2B Sandbox!"')console.log(result.stdout)

​

E2B building blocks
A quick overview of the core building blocks you’ll interact with when using E2B.
Sandbox — A fast, secure Linux VM created on demand for your agent

Template — Defines what environment a sandbox starts with

​

How to use the docs
The documentation is split into three main sections:
Quickstart — Step-by-step tutorials that walk you through creating your first E2B sandboxes.

Examples — In-depth tutorials focused on specific use cases. Pick the topics that match what you’re building.

SDK Reference — A complete technical reference for every SDK method, parameter, and configuration option.

​

Quickstart

​

Examples

Computer Use

Build AI agents that see, understand, and control virtual Linux desktops using E2B Desktop sandboxes.

GitHub Actions CI/CD

Use E2B sandboxes in your GitHub Actions workflows to run testing, validation, and AI code reviews.

Was this page helpful?

YesNo

Suggest editsRaise issue

Running your first SandboxThis guide will show you how to start your first E2B Sandbox.

Next

⌘I

websitexdiscordlinkedin

Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform

On this page

What is E2B?

E2B building blocks

How to use the docs

Quickstart

Examples

Assistant

Responses are generated using AI and may contain mistakes.
