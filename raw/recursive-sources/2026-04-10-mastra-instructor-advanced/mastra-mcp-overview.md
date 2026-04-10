---
title: MCP overview | MCP | Mastra Docs
source_url: https://mastra.ai/docs/mcp/overview
final_url: https://mastra.ai/docs/mcp/overview
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T06:17:49.100508+00:00
---

# MCP overview | MCP | Mastra Docs

## 원본 URL

https://mastra.ai/docs/mcp/overview

## 주요 헤딩

- MCP overview
- Get started Direct link to Get started
- Configuring MCPClient Direct link to configuring-mcpclient
- Using MCPClient with an agent Direct link to using-mcpclient-with-an-agent
- Configuring MCPServer Direct link to configuring-mcpserver
- Registering an MCPServer Direct link to registering-an-mcpserver
- Static and dynamic tools Direct link to Static and dynamic tools
- Connecting to an MCP registry Direct link to Connecting to an MCP registry
- Related Direct link to Related

## 추출 본문

MCP Overview
On this page
MCP overview
Mastra supports the Model Context Protocol (MCP) , an open standard for connecting AI agents to external tools and resources. It serves as a universal plugin system, enabling agents to call tools regardless of language or hosting environment.
Mastra can also be used to author MCP servers, exposing agents, tools, and other structured resources via the MCP interface. These can then be accessed by any system or agent that supports the protocol.
Mastra currently supports two MCP classes:
MCPClient
: Connects to one or many MCP servers to access their tools, resources, prompts, and handle elicitation requests.
MCPServer
: Exposes Mastra tools, agents, workflows, prompts, and resources to MCP-compatible clients.
Get started Direct link to Get started
To use MCP, install the required dependency:
npm pnpm Yarn Bun npm install @mastra/mcp@latest
pnpm add @mastra/mcp@latest
yarn add @mastra/mcp@latest
bun add @mastra/mcp@latest
Configuring MCPClient
Direct link to configuring-mcpclient
The MCPClient
connects Mastra primitives to external MCP servers, which can be local packages (invoked using npx
) or remote HTTP(S) endpoints. Each server must be configured with either a command
or a url
, depending on how it's hosted.
src/mastra/mcp/test-mcp-client.ts
import { MCPClient } from '@mastra/mcp'
export const testMcpClient = new MCPClient ( {
id : 'test-mcp-client' ,
servers : {
wikipedia : {
command : 'npx' ,
args : [ '-y' , 'wikipedia-mcp' ] ,
} ,
weather : {
url : new URL (
` https://server.smithery.ai/@smithery-ai/national-weather-service/mcp?api_key= ${ process . env . SMITHERY_API_KEY } ` ,
) ,
} ,
} ,
} )
info
Visit MCPClient for a full list of configuration options.
Authentication
For connecting to OAuth-protected MCP servers, see the OAuth Authentication section.
Using MCPClient
with an agent Direct link to using-mcpclient-with-an-agent
To use tools from an MCP server in an agent, import your MCPClient
and call .listTools()
in the tools
parameter. This loads from the defined MCP servers, making them available to the agent.
src/mastra/agents/test-agent.ts
import { Agent } from '@mastra/core/agent'
import { testMcpClient } from '../mcp/test-mcp-client'
export const testAgent = new Agent ( {
id : 'test-agent' ,
name : 'Test Agent' ,
description : 'You are a helpful AI assistant' ,
instructions : `
You are a helpful assistant that has access to the following MCP Servers.
- Wikipedia MCP Server
- US National Weather Service
Answer questions using the information you find using the MCP Servers. ` ,
model : 'openai/gpt-5.4' ,
tools : await testMcpClient . listTools ( ) ,
} )
info
Visit Agent Class for a full list of configuration options.
Configuring MCPServer
Direct link to configuring-mcpserver
To expose agents, tools, and workflows from your Mastra application to external systems over HTTP(S) use the MCPServer
class. This makes them accessible to any system or agent that supports the protocol.
src/mastra/mcp/test-mcp-server.ts
import { MCPServer } from '@mastra/mcp'
import { testAgent } from '../agents/test-agent'
import { testWorkflow } from '../workflows/test-workflow'
import { testTool } from '../tools/test-tool'
export const testMcpServer = new MCPServer ( {
id : 'test-mcp-server' ,
name : 'Test Server' ,
version : '1.0.0' ,
agents : { testAgent } ,
tools : { testTool } ,
workflows : { testWorkflow } ,
} )
info
Visit MCPServer for a full list of configuration options.
Authentication
To protect your MCP server with OAuth, see the OAuth Protection section.
Registering an MCPServer
Direct link to registering-an-mcpserver
To make an MCP server available to other systems or agents that support the protocol, register it in the main Mastra
instance using mcpServers
.
src/mastra/index.ts
import { Mastra } from '@mastra/core/mastra'
import { testMcpServer } from './mcp/test-mcp-server'
export const mastra = new Mastra ( {
mcpServers : { testMcpServer } ,
} )
Static and dynamic tools Direct link to Static and dynamic tools
MCPClient
offers two approaches to retrieving tools from connected servers, suitable for different application architectures:
Feature Static Configuration ( await mcp.listTools()
) Dynamic Configuration ( await mcp.listToolsets()
) Use Case Single-user, static config (e.g., CLI tool) Multi-user, dynamic config (e.g., SaaS app) Configuration Fixed at agent initialization Per-request, dynamic Credentials Shared across all uses Can vary per user/request Agent Setup Tools added in Agent
constructor Tools passed in .generate()
or .stream()
options
Static tools Direct link to Static tools
Use the .listTools()
method to fetch tools from all configured MCP servers. This is suitable when configuration (such as API keys) is static and consistent across users or requests. Call it once and pass the result to the tools
property when defining your agent.
info
Visit listTools() for more information.
src/mastra/agents/test-agent.ts
import { Agent } from '@mastra/core/agent'
import { testMcpClient } from '../mcp/test-mcp-client'
export const testAgent = new Agent ( {
id : 'test-agent' ,
tools : await testMcpClient . listTools ( ) ,
} )
Dynamic tools Direct link to Dynamic tools
Use the .listToolsets()
method when tool configuration may vary by request or user, such as in a multi-tenant system where each user provides their own API key. This method returns toolsets that can be passed to the toolsets
option in the agent's .generate()
or .stream()
calls.
import { MCPClient } from '@mastra/mcp'
import { mastra } from './mastra'
async function handleRequest ( userPrompt : string , userApiKey : string ) {
const userMcp = new MCPClient ( {
servers : {
weather : {
url : new URL ( 'http://localhost:8080/mcp' ) ,
requestInit : {
headers : {
Authorization : ` Bearer ${ userApiKey } ` ,
} ,
} ,
} ,
} ,
} )
const agent = mastra . getAgent ( 'testAgent' )
const response = await agent . generate ( userPrompt , {
toolsets : await userMcp . listToolsets ( ) ,
} )
await userMcp . disconnect ( )
return Response . json ( {
data : response . text ,
} )
}
info
Visit listToolsets() for more information.
Connecting to an MCP registry Direct link to Connecting to an MCP registry
MCP servers can be discovered through registries. Here's how to connect to some popular ones using MCPClient
:
Klavis AI mcp.run Composio.dev Smithery.ai Ampersand Klavis AI provides hosted, enterprise-authenticated, high-quality MCP servers. import { MCPClient } from '@mastra/mcp'
const mcp = new MCPClient ( {
servers : {
salesforce : {
url : new URL (
'https://salesforce-mcp-server.klavis.ai/mcp/?instance_id={private-instance-id}' ,
) ,
} ,
hubspot : {
url : new URL ( 'https://hubspot-mcp-server.klavis.ai/mcp/?instance_id={private-instance-id}' ) ,
} ,
} ,
} )
Klavis AI offers enterprise-grade authentication and security for production deployments. For more details on how to integrate Mastra with Klavis, check out their documentation .
mcp.run provides pre-authenticated, managed MCP servers. Tools are grouped into Profiles, each with a unique, signed URL. import { MCPClient } from '@mastra/mcp'
const mcp = new MCPClient ( {
servers : {
marketing : {
// Example profile name
url : new URL ( process . env . MCP_RUN_SSE_URL ! ) , // Get URL from mcp.run profile
} ,
} ,
} )
Important: Treat the mcp.run SSE URL like a password. Store it securely, for example, in an environment variable.
.env
