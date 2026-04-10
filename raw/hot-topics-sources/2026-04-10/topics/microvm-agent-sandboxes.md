---
title: Firecracker/microVM Sandboxes for Agent Code Execution
section: Harness Engineering
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Firecracker/microVM Sandboxes for Agent Code Execution

## 기존 큐레이션 요약

- 정의: Linux 컨테이너의 공유 커널 대신 KVM 기반 microVM으로 에이전트 생성 코드를 격리 실행하는 방식.
- 왜 중요한가: 2026년 들어 E2B가 자신의 샌드박스가 Firecracker microVM(≈125-150ms 부팅) 위에서 돈다고 공식화했고, Claude Code v2.1.98은 Linux에서 PID namespace 서브프로세스 sandboxing과 `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`를 추가하면서 "LLM 생성 코드 = 적대적 입력"이라는 하이퍼스케일러 컨센서스가 일반 개발자 환경까지 내려왔다.

## 개별 원문 수집 스냅샷

### E2B Documentation

- URL: https://e2b.dev/docs
- raw snapshot: `raw/hot-topics-sources/2026-04-10/062-e2b-documentation.md`
- 수집 제목: Documentation - E2B

Documentation - E2B Skip to main content E2B Docs home page Search... ⌘K Documentation SDK Reference API reference Getting started Home Quickstart API key Cookbook Need help? Billing Use cases Coding Agents Computer use GitHub Actions CI/CD Agents in sandbox Amp Claude Code Codex OpenClaw OpenCode Code interpreting Analyze data with AI Charts & visualizations Streaming Code contexts Supported languages Sandbox Lifecycle Lifecycle events API Lifecycle events webhooks Persistence Snapshots AutoResume Git integration Metrics Metadata Environment variables List sandboxes Connect to running sandbox Internet access Interactive terminal SSH access Connecting storage bucket Rate limits Secured access Proxy tunneling Custom domain Templates Quickstart How it works User and workdir Caching Base imag

### E2B Homepage

- URL: https://e2b.dev
- raw snapshot: `raw/hot-topics-sources/2026-04-10/063-e2b-homepage.md`
- 수집 제목: E2B | The Enterprise AI Agent Cloud

E2B | The Enterprise AI Agent Cloud CASE STUDY Perplexity shipped advanced data analysis in 1 week LEARN MORE → CASE STUDY How Manus Uses E2B to Provide Agents With Virtual Computers LEARN MORE → *** *** We raised $21M Series A Learn what’s next → *** *** Download logo (SVG/PNG) Product Pricing Resources Case Studies Startups Research Cookbook Blog Docs Case Studies ENTERPRISE Cookbook Blog Docs Startups Research Careers BOOK A CALL CAREERS Light/DARK SIGN UPSIGN IN NEW JOIN STARTUPS PROGRAM Deep Research Agents Computer Use Agents Automations Agents Background Agents Reinforcement Learning Secure MCPs Deep Research Agents AI Sandboxes for Open-source, secure environment with real-world tools for enterprise-grade agents. START FOR FREEVIEW DOCS TRUSTED BY How Perplexity implemented advance

### e2b-dev/E2B (GitHub)

- URL: https://github.com/e2b-dev/E2B
- raw snapshot: `raw/hot-topics-sources/2026-04-10/064-e2b-dev-e2b.md`
- 수집 제목: GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub

GitHub - e2b-dev/E2B: Open-source, secure environment with real-world tools for enterprise-grade agents. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterpri

### Claude Code Changelog

- URL: https://code.claude.com/docs/en/changelog
- raw snapshot: `raw/hot-topics-sources/2026-04-10/052-claude-code-changelog.md`
- 수집 제목: Changelog - Claude Code Docs

Changelog - Claude Code Docs Skip to main content Claude Code Docs home page English Search... ⌘KAsk AI Claude Developer Platform Claude Code on the Web Claude Code on the Web Search... Navigation Getting started Changelog Getting started Build with Claude Code Deployment Administration Configuration Reference Agent SDK What's New Resources Getting started Overview Quickstart Changelog Core concepts How Claude Code works Extend Claude Code Explore the .claude directory Explore the context window Use Claude Code Store instructions and memories Permission modes Common workflows Best practices Platforms and integrations Overview Remote Control Claude Code on the web Claude Code on desktop Chrome extension (beta) Computer use (preview) Visual Studio Code JetBrains IDEs Code review & CI/CD Clau

### Scaling Managed Agents: Decoupling the brain from the hands

- URL: https://www.anthropic.com/engineering/managed-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/042-scaling-managed-agents-decoupling-the-brain-from-the-hands.md`
- 수집 제목: Scaling Managed Agents: Decoupling the brain from the hands \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Scaling Managed Agents: Decoupling the brain from the hands Harnesses encode assumptions that go stale as models improve. Managed Agents—our hosted service for long-horizon agent work—is built around interfaces that stay stable as harnesses change. Get started with Claude Managed Agents by following our docs. A running topic on the Engineering Blog is how to build effective agents and design harnesses for long-running work. A common thread across this work is that harnesses encode assumptions about what Claude can’t do on its own. However, those assumptions need to be frequently questioned because they can go stale as models improve. As just one example, in prior work we 
