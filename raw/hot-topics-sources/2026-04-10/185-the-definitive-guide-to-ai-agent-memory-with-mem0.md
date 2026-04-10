---
title: Overview - Mem0
source_url: https://docs.mem0.ai/components/llms/overview
final_url: https://docs.mem0.ai/components/llms/overview
status: 200
content_type: text/html; charset=utf-8
topics: [Mem0 Universal Memory Layer]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:52.130372+00:00
---

# Overview - Mem0

## 원본 URL

https://docs.mem0.ai/components/llms/overview

## 추출 본문

Overview - Mem0

Skip to main content

Mem0 home page

Search...

⌘KAsk AI

Your Dashboard

Your Dashboard

Search...

Navigation

LLMs

Overview

Welcome

Mem0 Platform

OpenClaw

Open Source

Cookbooks

Integrations

Agent Plugins

API Reference

Documentation

Getting Started

Overview

Vibecoding

Python SDK Quickstart

Node SDK Quickstart

Self-Hosting Features

Overview

Graph Memory

Enhanced Metadata Filtering

Reranker-Enhanced Search

Async Memory

Multimodal Support

Custom Fact Extraction Prompt

Custom Update Memory Prompt

REST API Server

OpenAI Compatibility

Configuration

Configure the OSS Stack

LLMs

Overview

Configurations

Supported LLMs

Vector Databases

Embedding Models

Rerankers

Community & Support

Development

Documentation

On this page

Usage

Supported LLMs

Structured vs Unstructured Outputs

Structured Outputs

Unstructured Outputs

LLMs

Overview

Copy page

Overview of all supported LLM providers in Mem0, including OpenAI, Anthropic, Groq, Ollama, and more.

Copy page

Mem0 includes built-in support for various popular large language models. Memory can utilize the LLM provided by the user, ensuring efficient use for specific needs.

​

Usage
To use a llm, you must provide a configuration to customize its usage. If no configuration is supplied, a default configuration will be applied, and 
OpenAI
 will be used as the llm.For a comprehensive list of available parameters for llm configuration, please refer to Config.

​

Supported LLMs
See the list of supported LLMs below.

All LLMs are supported in Python. The following LLMs are also supported in TypeScript: OpenAI, Anthropic, and Groq.

OpenAI

Ollama

Azure OpenAI

Anthropic

Together

Groq

Litellm

Mistral AI

Google AI

AWS bedrock

DeepSeek

MiniMax

xAI

Sarvam AI

LM Studio

Langchain

​

Structured vs Unstructured Outputs
Mem0 supports two types of OpenAI LLM formats, each with its own strengths and use cases:

​

Structured Outputs
Structured outputs are LLMs that align with OpenAI’s structured outputs model:
Optimized for: Returning structured responses (e.g., JSON objects)

Benefits: Precise, easily parseable data

Ideal for: Data extraction, form filling, API responses

Learn more:OpenAI Structured Outputs Guide

​

Unstructured Outputs
Unstructured outputs correspond to OpenAI’s standard, free-form text model:
Flexibility: Returns open-ended, natural language responses

Customization: Use the 
response_format
 parameter to guide output

Trade-off: Less efficient than structured outputs for specific data needs

Best for: Creative writing, explanations, general conversation
Choose the format that best suits your application’s requirements for optimal performance and usability.

Was this page helpful?

YesNo

Suggest editsRaise issue

Configure the OSS Stack

Previous

Configurations

Next

⌘I

discordxgithublinkedin

Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform

Assistant

Responses are generated using AI and may contain mistakes.

Contact support
