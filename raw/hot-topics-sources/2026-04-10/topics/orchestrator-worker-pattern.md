---
title: Orchestrator-Worker Multi-Agent Pattern
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Orchestrator-Worker Multi-Agent Pattern

## 기존 큐레이션 요약

- 정의: 리드 에이전트가 작업을 분해해 병렬 서브에이전트에게 위임하고 결과를 합성하는 분산형 에이전트 아키텍처.
- 왜 중요한가: Anthropic이 Claude의 Research 기능 백엔드로 공개한 이 패턴이 단일 Opus 4 대비 90.2% 향상을 보인 이후 사실상 표준이 되었고, 2026년 4월 8일 출시된 Claude Managed Agents는 이 패턴을 매니지드 인프라로 제품화했다.

## 개별 원문 수집 스냅샷

### How we built our multi-agent research system (Anthropic)

- URL: https://www.anthropic.com/engineering/multi-agent-research-system
- raw snapshot: `raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md`
- 수집 제목: How we built our multi-agent research system \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic How we built our multi-agent research system Published Jun 13, 2025 Our Research feature uses multiple Claude agents to explore complex topics more effectively. We share the engineering challenges and the lessons we learned from building this system. Claude now has Research capabilities that allow it to search across the web, Google Workspace, and any integrations to accomplish complex tasks. The journey of this multi-agent system from prototype to production taught us critical lessons about system architecture, tool design, and prompt engineering. A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together. Our Research fea

### Orchestrator-Workers Workflow Cookbook (Anthropic)

- URL: https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/orchestrator_workers.ipynb
- raw snapshot: `raw/hot-topics-sources/2026-04-10/007-orchestrator-workers-workflow-cookbook.md`
- 수집 제목: claude-cookbooks/patterns/agents/orchestrator_workers.ipynb at main · anthropics/claude-cookbooks · GitHub

claude-cookbooks/patterns/agents/orchestrator_workers.ipynb at main · anthropics/claude-cookbooks · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Sma

### Create custom subagents (Claude Code Docs)

- URL: https://code.claude.com/docs/en/sub-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/008-create-custom-subagents.md`
- 수집 제목: Create custom subagents - Claude Code Docs

Create custom subagents - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Agents Create custom subagents Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Agents Create custom subagents Run agent teams Tools and plugins Model Context Protocol (MCP) Discover and install prebuilt plugins Create plugins Extend Claude with skills Automation Automate with hooks Push external events to Claude Run prompts on a schedule Programmatic usage Troubleshooting Troubleshooting On this page Built-in subagents Quickstart: create your first subagent Configure subagents Use the /agents command Choose the 

### Building agents with the Claude Agent SDK

- URL: https://claude.com/blog/building-agents-with-the-claude-agent-sdk
- raw snapshot: `raw/hot-topics-sources/2026-04-10/009-building-agents-with-the-claude-agent-sdk.md`
- 수집 제목: Building agents with the Claude Agent SDK | Claude

Building agents with the Claude Agent SDK | Claude Meet Claude Products Claude Claude Code Claude Cowork Features Claude for Chrome Claude for Slack Claude for Excel Claude for PowerPoint Skills Models Opus Sonnet Haiku Platform Overview Developer docs Pricing Console login Solutions Use cases AI agents Coding Departments Security Industries Customer support Education Financial services Government Healthcare Life sciences Nonprofits Pricing Overview API Plans Pro Max Team Enterprise Resources Insights Blog Customer stories Anthropic news Learn Anthropic Academy Courses Tutorials Use cases Tools Connectors Plugins Connect Events Community Login Contact sales Contact salesContact sales Try Claude Try ClaudeTry Claude Contact sales Contact salesContact sales Try Claude Try ClaudeTry Claude Co

### The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

- URL: https://arxiv.org/abs/2509.02547
- raw snapshot: `raw/hot-topics-sources/2026-04-10/010-the-landscape-of-agentic-reinforcement-learning-for-llms-a-survey.md`
- 수집 제목: [2509.02547] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

[2509.02547] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2509.02547 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2509.02547 (cs) [Submitted on 2 Sep 2025 (v1), last revised 24 Jan 2026 (this version, v4)] Title:The Landscape of Agentic Reinforcement Learning for LLMs: A Survey Authors:Guibin Zhang, Hejia Geng, Xiaohang Yu, Zhenfei Yin, Zaibin Zh
