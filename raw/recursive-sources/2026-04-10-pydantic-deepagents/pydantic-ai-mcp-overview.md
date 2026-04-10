---
title: Overview | Pydantic Docs
source_url: https://pydantic.dev/docs/ai/mcp/overview/
final_url: https://pydantic.dev/docs/ai/mcp/overview/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:35:17.649428+00:00
---

# Overview | Pydantic Docs

## 원본 URL

https://pydantic.dev/docs/ai/mcp/overview/

## 주요 헤딩

- Overview
- What is MCP?

## 추출 본문

Overview
Pydantic AI supports Model Context Protocol (MCP) in multiple ways:
Agents can connect to MCP servers and use their tools using three different methods:
Pydantic AI can act as an MCP client and connect directly to local and remote MCP servers. Learn more about MCPServer
.
Pydantic AI can use the FastMCP Client to connect to local and remote MCP servers, whether or not they’re built using FastMCP Server . Learn more about FastMCPToolset
.
Some model providers can themselves connect to remote MCP servers using a “built-in tool”. Learn more about MCPServerTool
.
Agents can be used within MCP servers. Learn more
What is MCP?
The Model Context Protocol is a standardized protocol that allow AI applications (including programmatic agents like Pydantic AI, coding agents like cursor , and desktop applications like Claude Desktop ) to connect to external tools and services using a common interface.
As with other protocols, the dream of MCP is that a wide range of applications can speak to each other without the need for specific integrations.
There is a great list of MCP servers at github.com/modelcontextprotocol/servers .
Some examples of what this means:
Pydantic AI could use a web search service implemented as an MCP server to implement a deep research agent
Cursor could connect to the Pydantic Logfire MCP server to search logs, traces and metrics to gain context while fixing a bug
Pydantic AI, or any other MCP client could connect to our Run Python MCP server to run arbitrary Python code in a sandboxed environment
Was this page helpful?
Thanks for your feedback!
Previous
Testing Next
Client
