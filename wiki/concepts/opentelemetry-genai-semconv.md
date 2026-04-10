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

## 해석 포인트

OpenTelemetry GenAI Semantic Conventions은 단순한 제품 소개보다 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `opentelemetry.io×2, langfuse.com×2, github.com×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: LLM·에이전트 텔레메트리를 위한 OTEL 표준 속성·스팬 규약.
- 왜 중요한가: 2026년 들어 Datadog·Grafana·Langfuse·Weave가 GenAI semconv를 네이티브 지원하기 시작하면서, 특정 플랫폼 lock-in 없이 에이전트 트레이스를 표준화하는 것이 관측성 스택의 가장 뜨거운 이슈다.
- 직접 수집 원문: 5개
- 주요 도메인: opentelemetry.io×2, langfuse.com×2, github.com×1

## 핵심 포인트

OpenTelemetry GenAI Semantic Conventions는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 LLM·에이전트 텔레메트리를 위한 OTEL 표준 속성·스팬 규약.이며, 직접 수집한 source 5건은 langfuse.com×2, opentelemetry.io×2, github.com×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 langfuse.com×2, opentelemetry.io×2, github.com×1로 분포한다. 구현 저장소 비중이 높아 실제 사용·통합 관점이 두드러진다.

## 실무 관점

개념 페이지는 용어 정의에서 끝나지 않고, 어떤 시스템 설계 문제를 해결하려고 등장했는지와 어디까지가 적용 범위인지까지 함께 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/opentelemetry-genai-semconv.md`

### source별 핵심 신호

- **Semantic conventions for generative AI systems | OpenTelemetry** (`opentelemetry.io`): https://opentelemetry.io/docs/specs/semconv/gen-ai/
  - 메모: System semantic conventions: instrumentation design philosophy
- **GitHub - traceloop/openllmetry: Open-source observability for your GenAI or LLM application, based on OpenTelemetry · GitHub** (`github.com`): https://github.com/traceloop/openllmetry
  - 메모: To see all available qualifiers, see our documentation.
- **Open Source LLM Observability via OpenTelemetry - Langfuse** (`langfuse.com`): https://langfuse.com/integrations/native/opentelemetry
  - 메모: (OTLP) endpoint.
- **LLM Observability & Application Tracing (Open Source) - Langfuse** (`langfuse.com`): https://langfuse.com/docs/observability/overview
  - 메모: The core of this is application tracing — structured logs of every request that capture the exact prompt sent, the model's response, token usage, latency, and any tools or retrieval steps in between.
- **OpenTelemetry for Generative AI | OpenTelemetry** (`opentelemetry.io`): https://opentelemetry.io/blog/2024/otel-generative-ai/
  - 메모: View Markdown View page source Edit this page Create child page Create documentation issue

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[pairwise-vs-pointwise-evals|Pairwise vs Pointwise Eval Protocol Bias]]
- [[synthetic-eval-data-generation|Synthetic Eval Data Generation]]
- [[context-engineering|Context Engineering]]
