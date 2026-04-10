---
title: Quickstart - Docs by LangChain
source_url: https://docs.langchain.com/oss/python/deepagents/quickstart
final_url: https://docs.langchain.com/oss/python/deepagents/quickstart
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:33:35.036602+00:00
---

# Quickstart - Docs by LangChain

## 원본 URL

https://docs.langchain.com/oss/python/deepagents/quickstart

## 주요 헤딩

- Quickstart
- ​ Prerequisites
- ​ How does it work?
- ​ Examples
- ​ Streaming
- ​ Next steps

## 추출 본문

Quickstart - Docs by LangChain
Skip to main content
Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >
Docs by LangChain home page
Open source
Search...
⌘ K
Ask AI
GitHub
Try LangSmith
Try LangSmith
Search...
Navigation
Get started
Quickstart
Deep Agents
LangChain
LangGraph
Integrations
Learn
Reference
Contribute
Python
Overview
Get started
Quickstart
Customization
Comparison
Changelog
Deployment
Deploy with the CLI
Going to production
Core capabilities
Overview
Models
Context engineering
Backends
Subagents
Async subagents
Human-in-the-loop
Memory
Skills
Sandboxes
Streaming
Frontend
Overview
Patterns
Protocols
Agent Client Protocol (ACP)
Command line interface
Use the CLI
Model providers
Configuration
MCP Tools
On this page Prerequisites
Step 1: Install dependencies
Step 2: Set up your API keys
Step 3: Create a search tool
Step 4: Create a deep agent
Step 5: Run the agent
How does it work?
Examples
Streaming
Next steps
Get started
Quickstart
Copy page
Build your first deep agent in minutes
Copy page
This guide walks you through creating your first deep agent with planning, file system tools, and subagent capabilities. You’ll build a research agent that can conduct research and write reports.
Using an AI coding assistant?
Install the LangChain Docs MCP server to give your agent access to up-to-date LangChain documentation and examples.
Install LangChain Skills to improve your agent’s performance on LangChain ecosystem tasks.
​
Prerequisites
Before you begin, make sure you have an API key from a model provider (e.g., Anthropic, OpenAI).
Deep Agents require a model that supports tool calling . See customization for how to configure your model.
​
Step 1: Install dependencies
pip
uv
pip install deepagents tavily-python
This guide uses Tavily as an example search provider, but you can substitute any search API (e.g., DuckDuckGo, SerpAPI, Brave Search).
​
Step 2: Set up your API keys
Anthropic
OpenAI
Google
OpenRouter
Fireworks
Baseten
Ollama
Other
export ANTHROPIC_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
export OPENAI_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
export GOOGLE_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
export OPENROUTER_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
export FIREWORKS_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
export BASETEN_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
# Local: Ollama must be running on your machine
# Cloud: Set your Ollama API key for hosted inference
export OLLAMA_API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
# Set the API key for your provider
export < PROVIDER > _API_KEY = "your-api-key"
export TAVILY_API_KEY = "your-tavily-api-key"
Deep Agents work with any LangChain chat model . Set the API key for your provider.
​
Step 3: Create a search tool
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent
tavily_client = TavilyClient ( api_key = os . environ [ " TAVILY_API_KEY " ])
def internet_search (
query : str ,
max_results : int = 5 ,
topic : Literal [ " general " , " news " , " finance " ] = "general" ,
include_raw_content : bool = False ,
):
"""Run a web search"""
return tavily_client . search (
query ,
max_results = max_results ,
include_raw_content = include_raw_content ,
topic = topic ,
)
​
Step 4: Create a deep agent
# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.
You have access to an internet search tool as your primary means of gathering information.
## `internet_search`
Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""
Pass a model
string in provider:model
format, or an initialized model instance. Defaults to anthropic:claude-sonnet-4-6
. See supported models for all providers and suggested models for tested recommendations.
Anthropic
OpenAI
Google
OpenRouter
Fireworks
Baseten
Ollama
Other
agent = create_deep_agent (
model = "anthropic:claude-sonnet-4-6" ,
tools = [ internet_search ],
system_prompt = research_instructions ,
)
agent = create_deep_agent (
model = "openai:gpt-5.4" ,
