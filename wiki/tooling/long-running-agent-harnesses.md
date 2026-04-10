---
title: Agent Harnesses for Long-Running Coding Sessions
category: tooling
page_type: concept
tags: [tooling, concept, long, running, agent, harnesses]
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Agent Harnesses for Long-Running Coding Sessions

컨텍스트 윈도우를 넘어 몇 시간 동안 자율적으로 코딩을 이어가게 하는 에이전트 실행 구조.

## 왜 중요한가

Anthropic이 2025년 11월 "Effective harnesses for long-running agents"에서 initializer + coding agent 2단 구조와 claude-progress.txt 기반 세션 이어받기 패턴을 공개했고, 2026년 3월에는 generator-evaluator 3-agent 구조로 확장한 후속편을 내며 "harness engineering"을 공식 카테고리로 띄웠다.

## 대표 레퍼런스

- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [anthropics/claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[model-context-protocol|MCP 2026 Roadmap & Enterprise Readiness]]
