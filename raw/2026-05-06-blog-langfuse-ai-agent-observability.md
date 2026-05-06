---
source: blog
url: https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse
title: "AI Agent Observability, Tracing & Evaluation with Langfuse"
author: Jannik (Langfuse)
date: 2025-03-16
fetched: 2026-05-06
status: pending_ingest
tags: [langfuse, agent-observability, opentelemetry, llm-tracing, evaluation, multi-agent]
---

# AI Agent Observability, Tracing & Evaluation with Langfuse

## 핵심 개념

**AI Agent Observability** = 에이전트의 성능, 행동, 인터랙션을 tracking·analyzing.
- 실시간 LLM 호출 모니터링
- Control flow 추적
- 의사결정 추적
- Output 추적

## 주요 프레임워크 통합

- **LangGraph**: "complex, stateful, multi-agent applications" - 내장 persistence
- **Pydantic AI**: "type safety and ergonomic developer experience" + native OpenTelemetry instrumentation
- **OpenAI Agents SDK**: "detailed traces of agent execution, including planning, function calls, and multi-agent handoffs"
- **smolagents**: "agent interactions are traced using OpenTelemetry"
- **CrewAI**: "role-based collaboration among multiple agents"
- AutoGen, Strands Agents, Semantic Kernel

## OpenTelemetry 채택

> "OpenTelemetry as a standard for collecting agent telemetry data, preventing vendor lock-in"

업계가 OTEL 표준에 수렴 중. Pydantic AI, smolagents 등이 native 지원.

## 평가 접근법

Langfuse가 지원하는 3가지 상호 보완적 전략:

1. **Final Response (Black-Box)**: 사용자 입력과 최종 응답만
2. **Trajectory (Glass-Box)**: "full sequence of tool calls, reasoning steps, and decisions"
3. **Single Step (White-Box)**: 개별 실행 단계

3단계 평가 phase: 수동 추적 → 온라인 평가 → 대규모 오프라인 평가

## 핵심 기능

- 실시간 비용 추적 + 토큰 모니터링
- 사용자 피드백 메커니즘
- LLM-as-a-Judge evaluators
- Benchmark 데이터셋 생성
- 자동화 실험
- 엣지 케이스 식별

## 메모

- 게시일: 2025년 3월 16일 (지속 업데이트)
- Langfuse는 open-source LLM 엔지니어링 플랫폼 (YC W23)
- Self-hostable, ClickHouse 기반 high-volume storage
- 최근 강화: OpenTelemetry-native SDK, full execution tracing 기반 LLM-as-Judge
- vLLM/SGLang multi-tenant 환경에서 강한 선택지로 평가됨
