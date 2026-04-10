---
title: AI SDK Core: Tool Calling
source_url: https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling
final_url: https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:49:52.360363+00:00
---

# AI SDK Core: Tool Calling

## 원본 URL

https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling

## 주요 헤딩

- Tool Calling
- Strict Mode
- Input Examples
- Tool Execution Approval
- Multi-Step Calls (using stopWhen)
- Response Messages
- Dynamic Tools
- Preliminary Tool Results
- Tool Choice
- Tool Execution Options
- Tool Input Lifecycle Hooks
- Types
- Handling Errors
- Tool Call Repair

## 추출 본문

AI SDK Core: Tool Calling
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
AI SDK Core Tool Calling
Copy markdown
Tool Calling
As covered under Foundations, tools are objects that can be called by the model to perform a specific task.
AI SDK Core tools contain several core elements:
description
: An optional description of the tool that can influence when the tool is picked.
inputSchema
: A Zod schema or a JSON schema that defines the input parameters. The schema is consumed by the LLM, and also used to validate the LLM tool calls.
execute
: An optional async function that is called with the inputs from the tool call. It produces a value of type RESULT
(generic type). It is optional because you might want to forward tool calls to the client or to a queue instead of executing them in the same process.
strict
: (optional, boolean) Enables strict tool calling when supported by the provider
You can use the tool
helper function to
infer the types of the execute
parameters.
The tools
parameter of generateText
and streamText
is an object that has the tool names as keys and the tools as values:
Gateway
Provider
Custom
Claude Sonnet 4.5
1 import { z } from 'zod' ;
2 import { generateText , tool , stepCountIs } from 'ai' ;
3
4 const result = await generateText ( {
5 model : "anthropic/claude-sonnet-4.5" ,
6 tools : {
7 weather : tool ( {
8 description : 'Get the weather in a location' ,
9 inputSchema : z . object ( {
10 location : z . string ( ) . describe ( 'The location to get the weather for' ) ,
11 } ) ,
12 execute : async ( { location } ) => ( {
13 location ,
14 temperature : 72 + Math . floor ( Math . random ( ) * 21 ) - 10 ,
15 } ) ,
16 } ) ,
17 } ,
18 stopWhen : stepCountIs ( 5 ) ,
19 prompt : 'What is the weather in San Francisco?' ,
20 } ) ;
When a model uses a tool, it is called a "tool call" and the output of the
tool is called a "tool result".
Tool calling is not restricted to only text generation.
You can also use it to render user interfaces (Generative UI).
Strict Mode
When enabled, language model providers that support strict tool calling will only generate tool calls that are valid according to your defined inputSchema
.
This increases the reliability of tool calling.
However, not all schemas may be supported in strict mode, and what is supported depends on the specific provider.
By default, strict mode is disabled. You can enable it per-tool by setting strict: true
:
1 tool ( {
2 description : 'Get the weather in a location' ,
3 inputSchema : z . object ( {
4 location : z . string ( ) ,
5 } ) ,
6 strict : true , // Enable strict validation for this tool
7 execute : async ( { location } ) => ( {
8 // ...
9 } ) ,
10 } ) ;
Not all providers or models support strict mode. For those that do not, this
option is ignored.
Input Examples
You can specify example inputs for your tools to help guide the model on how input data should be structured.
When supported by providers, input examples can help when JSON schema itself does not fully specify the intended
usage or when there are optional values.
1 tool ( {
2 description : 'Get the weather in a location' ,
3 inputSchema : z . object ( {
4 location : z . string ( ) . describe ( 'The location to get the weather for' ) ,
5 } ) ,
6 inputExamples : [
7 { input : { location : 'San Francisco' } } ,
8 { input : { location : 'London' } } ,
