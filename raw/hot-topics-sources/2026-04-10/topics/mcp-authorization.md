---
title: MCP OAuth 2.1 + PKCE Authorization
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# MCP OAuth 2.1 + PKCE Authorization

## 기존 큐레이션 요약

- 정의: MCP 서버를 OAuth 2.1 리소스 서버로 다루는 PKCE·Resource Indicator 기반 인증 스펙.
- 왜 중요한가: 2025-11-25 MCP 스펙에서 remote MCP 서버는 OAuth 2.1 + PKCE + RFC 8707 Resource Indicator가 MUST가 됐고, Client ID Metadata Document·동적 등록·audience binding이 의무화되면서 2026년 1월 Anthropic Git MCP 서버에서 path traversal+argument injection이 RCE로 연결된 사건 이후 토큰 audience 검증이 필수 방어선으로 자리잡았다.

## 개별 원문 수집 스냅샷

### MCP Authorization Specification (draft)

- URL: https://modelcontextprotocol.io/specification/draft/basic/authorization
- raw snapshot: `raw/hot-topics-sources/2026-04-10/050-mcp-authorization-specification.md`
- 수집 제목: Authorization - Model Context Protocol

Authorization - Model Context Protocol Skip to main content Model Context Protocol home page Draft Search... ⌘K Blog GitHub Search... Navigation Base Protocol Authorization Documentation Extensions Specification Registry SEPs Community Specification Key Changes Architecture Base Protocol Overview Lifecycle Transports Authorization Utilities Client Features Roots Sampling Elicitation Server Features Overview Prompts Resources Tools Utilities Schema Reference On this page Introduction Purpose and Scope Protocol Requirements Standards Compliance Roles Overview Authorization Server Discovery Authorization Server Location Protected Resource Metadata Discovery Requirements Authorization Server Metadata Discovery Authorization Server Discovery Sequence Diagram Client Registration Approaches Autho

### MCP Specification 2025-11-25

- URL: https://modelcontextprotocol.io/specification/2025-11-25
- raw snapshot: `raw/hot-topics-sources/2026-04-10/047-mcp-specification-2025-11-25.md`
- 수집 제목: Specification - Model Context Protocol

Specification - Model Context Protocol Skip to main content Model Context Protocol home page Version 2025-11-25 (latest) Search... ⌘K Blog GitHub Search... Navigation Specification Documentation Extensions Specification Registry SEPs Community Specification Key Changes Architecture Base Protocol Overview Lifecycle Transports Authorization Utilities Client Features Roots Sampling Elicitation Server Features Overview Prompts Resources Tools Utilities Schema Reference On this page Overview Key Details Base Protocol Features Additional Utilities Security and Trust & Safety Key Principles Implementation Guidelines Learn More Specification Copy page Copy page Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and 

### The 2026 MCP Roadmap

- URL: https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap
- raw snapshot: `raw/hot-topics-sources/2026-04-10/045-the-2026-mcp-roadmap.md`
- 수집 제목: The 2026 MCP Roadmap | Model Context Protocol Blog

The 2026 MCP Roadmap | Model Context Protocol BlogSkip to content Model Context Protocol Blog Documentation Posts Archives Search Home » Posts The 2026 MCP Roadmap The updated Model Context Protocol roadmap for 2026: transport scalability, agent communication, governance maturation, and enterprise readiness, plus guidance on SEP prioritization and how to get involved. March 9, 2026 · 6 min · David Soria Parra (Lead Maintainer) Table of Contents From Releases to Working Groups The Priority Areas Transport Evolution and Scalability Agent Communication Governance Maturation Enterprise Readiness SEP Prioritization: What It Means for Contributors On the Horizon Get Involved MCP’s current spec release came out in November 2025. We haven’t cut a new version since, but the project hasn’t stood sti

### modelcontextprotocol/modelcontextprotocol (GitHub)

- URL: https://github.com/modelcontextprotocol/modelcontextprotocol
- raw snapshot: `raw/hot-topics-sources/2026-04-10/049-modelcontextprotocol-modelcontextprotocol.md`
- 수집 제목: GitHub - modelcontextprotocol/modelcontextprotocol: Specification and documentation for the Model Context Protocol · GitHub

GitHub - modelcontextprotocol/modelcontextprotocol: Specification and documentation for the Model Context Protocol · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZ

### MCP What is the Model Context Protocol?

- URL: https://modelcontextprotocol.io
- raw snapshot: `raw/hot-topics-sources/2026-04-10/048-mcp-what-is-the-model-context-protocol.md`
- 수집 제목: What is the Model Context Protocol (MCP)? - Model Context Protocol

What is the Model Context Protocol (MCP)? - Model Context Protocol Skip to main content Model Context Protocol home page Search... ⌘K Blog GitHub Search... Navigation Get started What is the Model Context Protocol (MCP)? Documentation Extensions Specification Registry SEPs Community Get started What is MCP? About MCP Architecture Servers Clients Versioning Develop with MCP Connect to local MCP servers Connect to remote MCP Servers Build with Agent Skills Build an MCP server Build an MCP client SDKs Security Developer tools MCP Inspector Debugging Examples Example Clients Example Servers On this page What can MCP enable? Why does MCP matter? Broad ecosystem support Start Building Learn more Get started What is the Model Context Protocol (MCP)? Copy page Copy page MCP (Model Context Protocol
