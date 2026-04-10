---
title: Agents: Overview
source_url: https://ai-sdk.dev/docs/agents/overview
final_url: https://ai-sdk.dev/docs/agents/overview
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:49:52.159699+00:00
---

# Agents: Overview

## 원본 URL

https://ai-sdk.dev/docs/agents/overview

## 주요 헤딩

- Agents
- ToolLoopAgent Class
- Why Use the ToolLoopAgent?
- Structured Workflows
- Next Steps
- Get Started
- Build
- Scale
- Secure
- Resources
- Learn
- Frameworks
- SDKs
- Use Cases

## 추출 본문

Agents: Overview
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
Coding Agents Overview
Copy markdown
Agents
Agents are large language models (LLMs) that use tools in a loop to accomplish tasks.
These components work together:
LLMs process input and decide the next action
Tools extend capabilities beyond text generation (reading files, calling APIs, writing to databases)
Loop orchestrates execution through:
Context management - Maintaining conversation history and deciding what the model sees (input) at each step
Stopping conditions - Determining when the loop (task) is complete
ToolLoopAgent Class
The ToolLoopAgent class handles these three components. Here's an agent that uses multiple tools in a loop to accomplish a task:
Gateway
Provider
Custom
Claude Sonnet 4.5
1 import { ToolLoopAgent , tool } from 'ai' ;
2 import { z } from 'zod' ;
3
4 const weatherAgent = new ToolLoopAgent ( {
5 model : "anthropic/claude-sonnet-4.5" ,
6 tools : {
7 weather : tool ( {
8 description : 'Get the weather in a location (in Fahrenheit)' ,
9 inputSchema : z . object ( {
10 location : z . string ( ) . describe ( 'The location to get the weather for' ) ,
11 } ) ,
12 execute : async ( { location } ) => ( {
13 location ,
14 temperature : 72 + Math . floor ( Math . random ( ) * 21 ) - 10 ,
15 } ) ,
16 } ) ,
17 convertFahrenheitToCelsius : tool ( {
18 description : 'Convert temperature from Fahrenheit to Celsius' ,
19 inputSchema : z . object ( {
20 temperature : z . number ( ) . describe ( 'Temperature in Fahrenheit' ) ,
21 } ) ,
22 execute : async ( { temperature } ) => {
23 const celsius = Math . round ( ( temperature - 32 ) * ( 5 / 9 ) ) ;
24 return { celsius } ;
25 } ,
26 } ) ,
27 } ,
28 } ) ;
29
30 const result = await weatherAgent . generate ( {
31 prompt : 'What is the weather in San Francisco in celsius?' ,
32 } ) ;
33
34 console . log ( result . text ) ; // agent's final answer
35 console . log ( result . steps ) ; // steps taken by the agent
The agent automatically:
Calls the weather
tool to get the temperature in Fahrenheit
Calls convertFahrenheitToCelsius
to convert it
Generates a final text response with the result
The ToolLoopAgent handles the loop, context management, and stopping conditions.
Why Use the ToolLoopAgent?
The ToolLoopAgent is the recommended approach for building agents with the AI SDK because it:
Reduces boilerplate - Manages loops and message arrays
Improves reusability - Define once, use throughout your application
Simplifies maintenance - Single place to update agent configuration
For most use cases, start with the ToolLoopAgent. Use core functions ( generateText
, streamText
) when you need explicit control over each step for complex structured workflows.
Structured Workflows
Agents are flexible and powerful, but non-deterministic. When you need reliable, repeatable outcomes with explicit control flow, use core functions with structured workflow patterns combining:
Conditional statements for explicit branching
Standard functions for reusable logic
Error handling for robustness
Explicit control flow for predictability
Explore workflow patterns to learn more about building structured, reliable systems.
Next Steps
Building Agents - Guide to creating agents with the ToolLoopAgent
Workflow Patterns - Structured patterns using core functions for complex workflows
Loop Control - Execution control with stopWhen and prepareStep
Previous Agents
Next Building Agents
On this page
Agents ToolLoopAgent Class
