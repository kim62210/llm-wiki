---
title: Vercel AI SDK 6
section: Dev Tooling & Frameworks
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Vercel AI SDK 6

## 기존 큐레이션 요약

- 정의: Next.js·React 친화의 TypeScript LLM·에이전트 SDK.
- 왜 중요한가: 2025년 12월 AI SDK 6 릴리스로 ToolLoopAgent·needsApproval HITL·MCP OAuth·DevTools·이미지 편집·리랭킹까지 탑재되며 풀스택 TS 에이전트의 첫 선택지로 자리잡았고, streamText·generateText 위에 얇은 Agent 추상화를 더한 점진적 업그레이드 경로가 강점이다.

## 개별 원문 수집 스냅샷

### AI SDK 6 Release Blog (Vercel)

- URL: https://vercel.com/blog/ai-sdk-6
- raw snapshot: `raw/hot-topics-sources/2026-04-10/438-ai-sdk-6-release-blog.md`
- 수집 제목: AI SDK 6 - Vercel

AI SDK 6 - Vercel Skip to content Products AI Cloud v0 Build applications with AI AI SDK The AI Toolkit for TypeScript AI Gateway One endpoint, all your models Vercel Agent An agent that knows your stack Sandbox AI workflows in live environments Core Platform CI/CD Helping teams ship 6× faster Content Delivery Fast, scalable, and reliable Fluid Compute Servers, in serverless form Observability Trace every step Security Bot Management Scalable bot protection BotID Invisible CAPTCHA Platform Security DDoS Protection, Firewall Web Application Firewall Granular, custom protection Resources Company Customers Trusted by the best teams Blog The latest posts and changes Changelog See what shipped Press Read the latest news Events Join us at an event Learn Docs Vercel documentation Academy Linear c

### AI SDK Official Docs

- URL: https://ai-sdk.dev/docs/introduction
- raw snapshot: `raw/hot-topics-sources/2026-04-10/439-ai-sdk-official-docs.md`

# AI SDK The AI SDK is the TypeScript toolkit designed to help developers build AI-powered applications and agents with React, Next.js, Vue, Svelte, Node.js, and more. ## Why use the AI SDK? Integrating large language models (LLMs) into applications is complicated and heavily dependent on the specific model provider you use. The AI SDK standardizes integrating artificial intelligence (AI) models across [supported providers](/docs/foundations/providers-and-models). This enables developers to focus on building great AI applications, not waste time on technical details. For example, here’s how you can generate text with various models using the AI SDK: <PreviewSwitchProviders /> The AI SDK has two main libraries: - **[AI SDK Core](/docs/ai-sdk-core):** A unified API for generating text, struc

### vercel/ai GitHub Releases

- URL: https://github.com/vercel/ai/releases
- raw snapshot: `raw/hot-topics-sources/2026-04-10/440-vercel-ai-github-releases.md`
- 수집 제목: Releases · vercel/ai · GitHub

Releases · vercel/ai · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code changes APPLICATION SECURITY GitHub Advanced SecurityFind and fix vulnerabilities Code securitySecure your code as you build Secret protectionStop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecO

### AI SDK Homepage

- URL: https://ai-sdk.dev
- raw snapshot: `raw/hot-topics-sources/2026-04-10/441-ai-sdk-homepage.md`
- 수집 제목: AI SDK

AI SDK Docs Resources AI GatewayGateway Universal AI layer for building frameworks and agents A unified TypeScript SDK for building AI apps with modern streaming, fallbacks, and multi-model support—powered by Vercel For humans For agents $npm install ainpm install ai Text GenerationImage GenerationSpeechTranscriptionVideo Generation Run it with AI GatewayProviderCustom 1 import{ generateText }from'ai'; 2 3 const{ text }=awaitgenerateText({ 4 model:"anthropic/claude-sonnet-4.6", 5 prompt:'Explain the concept of quantum entanglement.', 6 }); 7 8 console.log(text); Explain quantum entanglement in simple terms. Quantum entanglement is when two particles become linked so that measuring one instantly affects the other, no matter the distance between them. See allsupported LLM models 9.9MWeekly d

### Vercel AI SDK Product Page

- URL: https://vercel.com/docs/ai-sdk
- raw snapshot: `raw/hot-topics-sources/2026-04-10/442-vercel-ai-sdk-product-page.md`

--- title: AI SDK product: ai-sdk url: /docs/ai-sdk type: integration prerequisites: [] related: [] summary: TypeScript toolkit for building AI-powered applications with React, Next.js, Vue, Svelte and Node.js install_vercel_plugin: npx plugins add vercel/vercel-plugin --- # AI SDK The [AI SDK](https://sdk.vercel.ai) is the TypeScript toolkit designed to help developers build AI-powered applications with [Next.js](https://sdk.vercel.ai/docs/getting-started/nextjs-app-router), [Vue](https://sdk.vercel.ai/docs/getting-started/nuxt), [Svelte](https://sdk.vercel.ai/docs/getting-started/svelte), [Node.js](https://sdk.vercel.ai/docs/getting-started/nodejs), and more. Integrating LLMs into applications is complicated and heavily dependent on the specific model provider you use. The AI SDK abstrac
