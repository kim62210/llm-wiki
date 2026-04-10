---
title: AI SDK Core: Overview
source_url: https://ai-sdk.dev/docs/ai-sdk-core/overview
final_url: https://ai-sdk.dev/docs/ai-sdk-core/overview
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:49:51.957846+00:00
---

# AI SDK Core: Overview

## 원본 URL

https://ai-sdk.dev/docs/ai-sdk-core/overview

## 주요 헤딩

- AI SDK Core
- AI SDK Core Functions
- API Reference
- Get Started
- Build
- Scale
- Secure
- Resources
- Learn
- Frameworks
- SDKs
- Use Cases
- Company
- Community

## 추출 본문

AI SDK Core: Overview
Docs
Resources
AI Gateway Gateway
Menu
v6 (Latest)
AI SDK 6.x
AI SDK by Vercel
Foundations
Overview
Providers and Models
Prompts
Tools
Streaming
Provider Options
Getting Started
Choosing a Provider
Navigating the Library
Next.js App Router
Next.js Pages Router
Svelte
Vue.js (Nuxt)
Node.js
Expo
TanStack Start
Coding Agents
Agents
Overview
Building Agents
Workflow Patterns
Loop Control
Configuring Call Options
Memory
Subagents
AI SDK Core
Overview
Generating Text
Generating Structured Data
Tool Calling
Model Context Protocol (MCP)
Prompt Engineering
Settings
Embeddings
Reranking
Image Generation
Transcription
Speech
Video Generation
Language Model Middleware
Provider & Model Management
Error Handling
Testing
Telemetry
DevTools
Event Callbacks
AI SDK UI
Overview
Chatbot
Chatbot Message Persistence
Chatbot Resume Streams
Chatbot Tool Usage
Generative User Interfaces
Completion
Object Generation
Streaming Custom Data
Error Handling
Transport
Reading UIMessage Streams
Message Metadata
Stream Protocols
AI SDK RSC
Advanced
Reference
AI SDK Core
AI SDK UI
AI SDK RSC
AI SDK Errors
Migration Guides
Troubleshooting
AI SDK Core Overview
Copy markdown
AI SDK Core
Large Language Models (LLMs) are advanced programs that can understand, create, and engage with human language on a large scale.
They are trained on vast amounts of written material to recognize patterns in language and predict what might come next in a given piece of text.
AI SDK Core simplifies working with LLMs by offering a standardized way of integrating them into your app - so you can focus on building great AI applications for your users, not waste time on technical details.
For example, here’s how you can generate text with various models using the AI SDK:
Gateway
Provider
Custom
Claude Sonnet 4.5
1 import { generateText } from "ai" ;
2
3 const { text } = await generateText ( {
4 model : "anthropic/claude-sonnet-4.5" ,
5 prompt : "What is love?" ,
6 } ) ;
Love is a complex and multifaceted emotion that can be felt and expressed in many different ways. It involves deep affection, care, compassion, and connection towards another person or thing.
AI SDK Core Functions
AI SDK Core has various functions designed for text generation , structured data generation , and tool usage .
These functions take a standardized approach to setting up prompts and settings , making it easier to work with different models.
generateText
: Generates text and tool calls .
This function is ideal for non-interactive use cases such as automation tasks where you need to write text (e.g. drafting email or summarizing web pages) and for agents that use tools.
streamText
: Stream text and tool calls.
You can use the streamText
function for interactive use cases such as chat bots and content streaming .
Both generateText
and streamText
support structured output via the output
property (e.g. Output.object()
, Output.array()
), allowing you to generate typed, schema-validated data for information extraction, synthetic data generation, classification tasks, and streaming generated UIs .
API Reference
Please check out the AI SDK Core API Reference for more details on each function.
Previous AI SDK Core
Next Generating Text
On this page
AI SDK Core AI SDK Core Functions
API Reference
Deploy and Scale AI Apps with Vercel Deliver AI experiences globally with one push.
Trusted by industry leaders: OpenAI
Photoroom
Sign Up
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
AI Gateway New
Vercel Agent New
Secure
Platform security
Web Application Firewall
Bot management
BotID
Sandbox New
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
