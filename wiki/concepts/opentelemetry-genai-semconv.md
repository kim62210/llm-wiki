---
title: OpenTelemetry GenAI Semantic Conventions
category: concepts
page_type: entity
project: OpenTelemetry GenAI Semantic Conventions
tags: [concepts, entity, opentelemetry, genai, semconv]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/2026-04-14-ai-hot-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/opentelemetry-genai-semconv.md, raw/hot-topics-sources/2026-04-10/247-opentelemetry-semantic-conventions-for-genai-systems.md, raw/hot-topics-sources/2026-04-10/248-openllmetry-github-repository.md, raw/hot-topics-sources/2026-04-10/249-langfuse-opentelemetry-integration.md, raw/hot-topics-sources/2026-04-10/250-langfuse-[[llm-observability-platforms|observability]]-overview.md, raw/hot-topics-sources/2026-04-10/251-opentelemetry-for-generative-ai.md]
created: 2026-04-10
updated: 2026-04-14
---
# OpenTelemetry GenAI Semantic Conventions

[[context-engineering|LLM]]·에이전트 텔레메트리를 위한 OTEL 표준 속성·스팬 규약.

## 왜 지금 중요한가

2026년 들어 Datadog·Grafana·Langfuse·Weave가 GenAI semconv를 네이티브 지원하기 시작하면서, 특정 플랫폼 lock-in 없이 에이전트 트레이스를 표준화하는 것이 관측성 스택의 가장 뜨거운 이슈다.

## 대표 레퍼런스

- [OpenTelemetry Semantic Conventions for GenAI Systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OpenLLMetry GitHub Repository (Traceloop)](https://github.com/traceloop/openllmetry)
- [Langfuse OpenTelemetry Integration](https://langfuse.com/integrations/native/opentelemetry)
- [Langfuse Observability Overview](https://langfuse.com/docs/observability/overview)
- [OpenTelemetry for Generative AI (OTel Blog)](https://opentelemetry.io/blog/2024/otel-generative-ai/)


### 프로바이더 무관 표준화

OpenAI, Anthropic, Amazon Bedrock 등 복수 벤더의 성능을 표준화된 필드 브레이크다운(모델/프로바이더별)으로 비교할 수 있다. 한 번 OTel로 계측하면 플랫폼별 병렬 계측 경로를 유지할 필요가 없다.

### 에이전트 태스크/액션/아티팩트 트레이싱 확장

`gen_ai.operation.name` 속성이 `tool_call`, `agent_run` 등의 값을 지원하면서, 멀티 에이전트 및 도구 기반 워크플로의 엔드투엔드 트레이싱이 가능해졌다. 오케스트레이션된 AI 시스템 내에서 에이전트와 도구 흐름을 완전히 추적할 수 있다.

### 거버넌스 통합

OpenTelemetry Collector 프로세서를 통해 편집(redaction), 샘플링, 보강(enrichment), 라우팅이 수행되어 텔레메트리 데이터가 네트워크를 떠나기 전에 데이터 정책이 적용된다.

### 2026-04-14 추가 소스

- [Datadog: LLM OTel Semantic Convention](https://www.datadoghq.com/blog/llm-otel-semantic-convention/)
- [Uptrace: OpenTelemetry AI Systems](https://uptrace.dev/blog/opentelemetry-ai-systems)
- [GitHub Issue: Agent Tracing Extension Proposal](https://github.com/open-telemetry/semantic-conventions/issues/2664)

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[pairwise-vs-pointwise-evals|Pairwise vs Pointwise Eval Protocol Bias]]
- [[synthetic-eval-data-generation|Synthetic Eval Data Generation]]
- [[context-engineering|Context Engineering]]
- [[llm-observability-platforms|LLM Observability Platforms]]
- [[agentic-ai-production|Agentic AI 프로덕션 배포 패턴]]
