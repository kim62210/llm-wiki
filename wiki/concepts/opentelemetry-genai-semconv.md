---
title: OpenTelemetry GenAI Semantic Conventions
category: concepts
page_type: entity
project: OpenTelemetry GenAI Semantic Conventions
tags: [concepts, entity, opentelemetry, genai, semconv]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/opentelemetry-genai-semconv.md, raw/hot-topics-sources/2026-04-10/247-opentelemetry-semantic-conventions-for-genai-systems.md, raw/hot-topics-sources/2026-04-10/248-openllmetry-github-repository.md, raw/hot-topics-sources/2026-04-10/249-langfuse-opentelemetry-integration.md, raw/hot-topics-sources/2026-04-10/250-langfuse-observability-overview.md, raw/hot-topics-sources/2026-04-10/251-opentelemetry-for-generative-ai.md]
created: 2026-04-10
updated: 2026-04-10
---
# OpenTelemetry GenAI Semantic Conventions

LLM·에이전트 텔레메트리를 위한 OTEL 표준 속성·스팬 규약.

## 왜 지금 중요한가

2026년 들어 Datadog·Grafana·Langfuse·Weave가 GenAI semconv를 네이티브 지원하기 시작하면서, 특정 플랫폼 lock-in 없이 에이전트 트레이스를 표준화하는 것이 관측성 스택의 가장 뜨거운 이슈다.

## 대표 레퍼런스

- [OpenTelemetry Semantic Conventions for GenAI Systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OpenLLMetry GitHub Repository (Traceloop)](https://github.com/traceloop/openllmetry)
- [Langfuse OpenTelemetry Integration](https://langfuse.com/integrations/native/opentelemetry)
- [Langfuse Observability Overview](https://langfuse.com/docs/observability/overview)
- [OpenTelemetry for Generative AI (OTel Blog)](https://opentelemetry.io/blog/2024/otel-generative-ai/)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: opentelemetry.io 2건, langfuse.com 2건, github.com 1건
- source 조합: 구현체

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/opentelemetry-genai-semconv.md`
- [Semantic conventions for generative AI systems | OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai) — `raw/hot-topics-sources/2026-04-10/247-opentelemetry-semantic-conventions-for-genai-systems.md`
  - 메모: --- title: Semantic conventions for generative AI systems | OpenTelemetry source_url: https://opentelemetry.io/docs/specs/semconv/gen-ai final_url: https://opentelemetry.io/docs/specs/semconv/gen-ai/ status: 200 content_type: text/html; charset=UTF-8 topics: [OpenTelemetry GenAI 
- [GitHub - traceloop/openllmetry: Open-source observability for your GenAI or LLM application, based on OpenTelemetry · GitHub](https://github.com/traceloop/openllmetry) — `raw/hot-topics-sources/2026-04-10/248-openllmetry-github-repository.md`
  - 메모: --- title: GitHub - traceloop/openllmetry: Open-source observability for your GenAI or LLM application, based on OpenTelemetry · GitHub source_url: https://github.com/traceloop/openllmetry final_url: https://github.com/traceloop/openllmetry status: 200 content_type: text/html; ch
- [Open Source LLM Observability via OpenTelemetry - Langfuse](https://langfuse.com/integrations/native/opentelemetry) — `raw/hot-topics-sources/2026-04-10/249-langfuse-opentelemetry-integration.md`
  - 메모: --- title: Open Source LLM Observability via OpenTelemetry - Langfuse source_url: https://langfuse.com/integrations/native/opentelemetry final_url: https://langfuse.com/integrations/native/opentelemetry status: 200 content_type: text/html; charset=utf-8 topics: [OpenTelemetry Gen
- [LLM Observability & Application Tracing (Open Source) - Langfuse](https://langfuse.com/docs/observability/overview) — `raw/hot-topics-sources/2026-04-10/250-langfuse-observability-overview.md`
  - 메모: --- title: LLM Observability & Application Tracing (Open Source) - Langfuse source_url: https://langfuse.com/docs/observability/overview final_url: https://langfuse.com/docs/observability/overview status: 200 content_type: text/html; charset=utf-8 topics: [OpenTelemetry GenAI Sem
- [OpenTelemetry for Generative AI | OpenTelemetry](https://opentelemetry.io/blog/2024/otel-generative-ai) — `raw/hot-topics-sources/2026-04-10/251-opentelemetry-for-generative-ai.md`
  - 메모: --- title: OpenTelemetry for Generative AI | OpenTelemetry source_url: https://opentelemetry.io/blog/2024/otel-generative-ai final_url: https://opentelemetry.io/blog/2024/otel-generative-ai/ status: 200 content_type: text/html; charset=UTF-8 topics: [OpenTelemetry GenAI Semantic 

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[pairwise-vs-pointwise-evals|Pairwise vs Pointwise Eval Protocol Bias]]
- [[synthetic-eval-data-generation|Synthetic Eval Data Generation]]
- [[context-engineering|Context Engineering]]
