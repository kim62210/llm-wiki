---
title: AI SDK Core: Model Context Protocol (MCP)
source_url: https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools
final_url: https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:49:52.550427+00:00
---

# AI SDK Core: Model Context Protocol (MCP)

## 원본 URL

https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools

## 주요 헤딩

- Model Context Protocol (MCP)
- Initializing an MCP Client
- Using MCP Tools
- Using MCP Resources
- Using MCP Prompts
- Handling Elicitation Requests
- Examples
- Get Started
- Build
- Scale
- Secure
- Resources
- Learn
- Frameworks

## 추출 본문

AI SDK Core: Model Context Protocol (MCP)
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
AI SDK Core Model Context Protocol (MCP)
Copy markdown
Model Context Protocol (MCP)
The AI SDK supports connecting to Model Context Protocol (MCP) servers to access their tools, resources, and prompts.
This enables your AI applications to discover and use capabilities across various services through a standardized interface.
If you're using OpenAI's Responses API, you can also use the built-in
openai.tools.mcp
tool, which provides direct MCP server integration without
needing to convert tools. See the OpenAI provider
documentation for details.
Initializing an MCP Client
We recommend using HTTP transport (like StreamableHTTPClientTransport
) for production deployments. The stdio transport should only be used for connecting to local servers as it cannot be deployed to production environments.
Create an MCP client using one of the following transport options:
HTTP transport (Recommended) : Either configure HTTP directly via the client using transport: { type: 'http', ... }
, or use MCP's official TypeScript SDK StreamableHTTPClientTransport
SSE (Server-Sent Events): An alternative HTTP-based transport
stdio
: For local development only. Uses standard input/output streams for local MCP servers
HTTP Transport (Recommended)
For production deployments, we recommend using the HTTP transport. You can configure it directly on the client:
1 import { createMCPClient } from '@ai-sdk/mcp' ;
2
3 const mcpClient = await createMCPClient ( {
4 transport : {
5 type : 'http' ,
6 url : 'https://your-server.com/mcp' ,
7
8 // optional: configure HTTP headers
9 headers : { Authorization : 'Bearer my-api-key' } ,
10
11 // optional: provide an OAuth client provider for automatic authorization
12 authProvider : myOAuthClientProvider ,
13
14 // optional: reject redirect responses to prevent SSRF
15 redirect : 'error' ,
16 } ,
17 } ) ;
Alternatively, you can use StreamableHTTPClientTransport
from MCP's official TypeScript SDK:
1 import { createMCPClient } from '@ai-sdk/mcp' ;
2 import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js' ;
3
4 const url = new URL ( 'https://your-server.com/mcp' ) ;
5 const mcpClient = await createMCPClient ( {
6 transport : new StreamableHTTPClientTransport ( url , {
7 sessionId : 'session_123' ,
8 } ) ,
9 } ) ;
SSE Transport
SSE provides an alternative HTTP-based transport option. Configure it with a type
and url
property. You can also provide an authProvider
for OAuth:
1 import { createMCPClient } from '@ai-sdk/mcp' ;
2
3 const mcpClient = await createMCPClient ( {
4 transport : {
5 type : 'sse' ,
6 url : 'https://my-server.com/sse' ,
7
8 // optional: configure HTTP headers
9 headers : { Authorization : 'Bearer my-api-key' } ,
10
11 // optional: provide an OAuth client provider for automatic authorization
12 authProvider : myOAuthClientProvider ,
13
14 // optional: reject redirect responses to prevent SSRF
15 redirect : 'error' ,
16 } ,
17 } ) ;
Stdio Transport (Local Servers)
The stdio transport should only be used for local servers.
The Stdio transport can be imported from either the MCP SDK or the AI SDK:
1 import { createMCPClient } from '@ai-sdk/mcp' ;
2 import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js' ;
3 // Or use the AI SDK's stdio transport:
4 // import { Experimental_StdioMCPTransport as StdioClientTransport } from '@ai-sdk/mcp/mcp-stdio';
5
6 const mcpClient = await createMCPClient ( {
7 transport : new StdioClientTransport ( {
