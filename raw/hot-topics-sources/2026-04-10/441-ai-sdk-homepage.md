---
title: AI SDK
source_url: https://ai-sdk.dev
final_url: https://ai-sdk.dev
status: 200
content_type: text/html; charset=utf-8
topics: [Vercel AI SDK 6]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:28.487887+00:00
---

# AI SDK

## 원본 URL

https://ai-sdk.dev

## 추출 본문

AI SDK

Docs

Resources

AI GatewayGateway

Universal AI layer for building frameworks and agents

A unified TypeScript SDK for building AI apps with modern streaming, fallbacks, and multi-model support—powered by Vercel

For humans

For agents

$npm install ainpm install ai

Text GenerationImage GenerationSpeechTranscriptionVideo Generation

Run it with
AI GatewayProviderCustom

1
import{ generateText }from'ai';

2

3
const{ text }=awaitgenerateText({

4
 model:"anthropic/claude-sonnet-4.6",

5
 prompt:'Explain the concept of quantum entanglement.',

6
});

7

8
console.log(text);

Explain quantum entanglement in simple terms.

Quantum entanglement is when two particles become linked so that measuring one instantly affects the other, no matter the distance between them.

See allsupported LLM models

9.9MWeekly downloads

23.4KGitHub stars

614+Contributors

100+Models supported

The Framework Agnostic AI Toolkit

The open-source AI toolkit designed to help developers build AI-powered applications and agents with React, Next.js, Vue, Svelte, Node.js, and more.

Multi-provider support.Switch providers with one line of code.

Streaming that just works.Real-time responses without custom parsing.

Built-in fallbacks.
Reliable production behavior by default.

generate-text.ts

Run it with
AI GatewayProviderCustom

1
import{ generateText }from'ai';

2

3
const{ text }=awaitgenerateText({

4
 model:"openai/gpt-5.4",

5
 prompt:'Explain the concept of quantum entanglement.',

6
});

7

8
console.log(text);

Text GenerationSpeechTranscriptionImage GenerationVideo GenerationTool CallingError HandlingDevTools

AI SDK Core

A unified API for generating text, structured objects, tool calls, and building agents with LLMs.

AI SDK UI

A set of framework-agnostic hooks for quickly building chat and generative user interface.
Go to playground

Supports

+16 providers

Scale with confidence

Plug the AI SDK into an entire ecosystem designed for the way modern AI applications that scale.

Vercel AI Gateway

Access 100+ models with no markup or having to manage multiple API keys.

npm i ai

Vercel Sandbox

Run agent generated code securely and at scale.

npm i @vercel/sandbox

Workflows NEW

Build long running AI agents and apps that can suspend, resume, and survive function timeouts.

npm i workflow

AI Elements

A UI component library and custom registry built to build AI-native applications faster.

npx ai-elements

We built a full AI agent with 40+ tools, resumable streams, and multi-step reasoning on AI SDK. Every hard problem we'd solved with duct tape before, streaming, tool call repair, message management, tool based UI, they already had a clean API for. It feels like their team hit every wall we did, just before us.

Adir DuchanSenior AI Engineer

OpenCode uses AI SDK.

Dax RaadCEO & Founder

Build with our today

Get started with the AI SDK by using our cookbooks or templates.

Visit Documentation

npm i ai

Chatbot Starter Template

Learn how to build a full-featured AI chatbot with persistence, multi-modal chat, and more.

Copy install prompt

Build a Slackbot Agent

Learn how to build a Slackbot that responds to direct messages and mentions in channels.

Copy install prompt

Build a SQL Agent

Learn how to build an app that interacts with a PostgreSQL database using natural language.

Copy install prompt

Get Started

Templates

Supported frameworks

Marketplace

Domains

Build

Next.js on Vercel

Turborepo

v0

Scale

Content delivery network

Fluid compute

CI/CD

Observability

AI GatewayNew

Vercel AgentNew

Secure

Platform security

Web Application Firewall

Bot management

BotID

SandboxNew

Resources

Pricing

Customers

Enterprise

Articles

Startups

Solution partners

Learn

Docs

Blog

Changelog

Knowledge Base

Academy

Community

Frameworks

Next.js

Nuxt

Svelte

Nitro

Turbo

SDKs

AI SDK

Workflow DevKitNew

Flags SDK

Chat SDK

Streamdown AINew

Use Cases

Composable commerce

Multi-tenant platforms

Web apps

Marketing sites

Platform engineers

Design engineers

Company

About

Careers

Help

Press

Legal

Privacy Policy

Community

Open source program

Events

Shipped on Vercel

GitHub

LinkedIn

X

YouTube

© 2026 Vercel, Inc.
Select a display theme:systemlightdark
