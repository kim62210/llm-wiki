---
source: blog
url: https://claude.com/blog/building-agents-with-the-claude-agent-sdk
title: Building agents with the Claude Agent SDK
author: Thariq Shihipar (Anthropic) - with notes from Molly Vorwerck, Suzanne Wang, Alex Isken, Cat Wu, Keir Bradwell, Alexander Bricken, Ashwin Bhat
date: 2025-09-29
fetched: 2026-05-06
status: pending_ingest
tags: [claude-agent-sdk, claude-code, agent-loop, gather-context, take-action, verify-iterate, anthropic-engineering]
---

# Building agents with the Claude Agent SDK (Anthropic Engineering)

## 핵심 디자인 원칙

> "Give your agents a computer."

Anthropic은 Claude Code SDK를 **Claude Agent SDK**로 리네이밍. Claude Code의 agent harness가 코딩 외 다양한 에이전트 use case도 powering 가능함을 인정.

> "Over the past several months, Claude Code has become far more than a coding tool—we've used it for deep research, video creation, and note-taking, among countless other non-coding applications."

## Agent Loop 4-단계 프레임워크

### 1. Gather Context (컨텍스트 수집)
- **Agentic search**: filesystem 도구 (grep, tail)
- **Semantic search** (선택적)
- **Subagent parallelization**: 격리된 컨텍스트로 병렬 작업
- **Conversation compaction**

### 2. Take Action (행동)
- 커스텀 도구
- Bash 스크립트
- Code generation
- **MCP integrations**

### 3. Verify Work (검증)
- Rules-based feedback (linting)
- Visual feedback (screenshots)
- LLM-as-judge 평가

### 4. Iterate (반복)
- 테스트와 정제로 지속 개선

## Use Case 예시

- **Finance agents**: 포트폴리오 분석
- **Personal assistants**: 캘린더/여행 관리
- **Customer support agents**: 복잡 요청 처리
- **Deep research agents**: 정보 종합

## 기술 능력

- **Bash/Scripts**: 파일 작업, PDF 변환, 웹 검색
- **Code Generation**: Excel/PowerPoint/Word 생성용 Python
- **MCPs**: 사전 빌드 통합 (Slack, GitHub, Asana, Google Drive)
- **Subagents**: 격리된 컨텍스트로 병렬 작업

## 핵심 원칙

> "Evaluating agents through concrete feedback mechanisms rather than relying solely on fuzzy judgment criteria."

명확한 검증 → 도구가 잘 동작하는지 객관 측정.

## Claude Agent SDK 컴포넌트

- 커스텀 시스템 프롬프트
- Slash commands
- Hooks (deterministic 자동 실행)
- Subagents (격리된 컨텍스트)
- Tools (MCP, Bash, custom)
- Skills (도메인 지식 패키지)

## 메모

- 게시일: 2025년 9월 29일
- 카테고리: Claude Code, Agents
- Claude Agent SDK는 Claude Code SDK의 리네이밍 - 코딩 외 일반 에이전트로 확장
- 핵심 메시지: "Claude Code의 agent loop가 거의 모든 Anthropic 내부 에이전트를 powering"
- npm: `@anthropic-ai/claude-agent-sdk`, Python: `claude-agent-sdk-python`
