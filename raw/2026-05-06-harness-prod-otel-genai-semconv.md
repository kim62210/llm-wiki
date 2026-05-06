---
source: OpenTelemetry Specification
url: https://opentelemetry.io/docs/specs/semconv/gen-ai/
title: OpenTelemetry GenAI Semantic Conventions (gen_ai.* attributes)
fetched: 2026-05-06
status: pending_ingest
tags: [observability, opentelemetry, semantic-conventions, gen-ai, agent-trace, telemetry]
---

# OpenTelemetry GenAI Semantic Conventions

## 핵심 요약 (한국어)

OpenTelemetry 의 `gen_ai.*` semantic convention 은 LLM/Agent 관측의 **벤더 중립 표준**.
2026 년 5월 현재 status 는 **Development (experimental)** 이며 아직 stable 이 아니다.
4 가지 signal 카테고리 (Spans, Metrics, Events, Exceptions) 에 걸쳐 정의되며, span 은
다시 **client (model) span** 과 **agent framework span** 두 가지로 분리된다.

> "Existing GenAI instrumentations...SHOULD NOT change the version of the GenAI conventions
> that they emit by default" — 기존 instrumentation 은 default 버전 유지하고, 신버전은
> `OTEL_SEMCONV_STABILITY_OPT_IN` env var 로 opt-in.

```mermaid
flowchart TD
    Root[Agent Workflow] -->|invoke_workflow| WF[Workflow Span<br/>INTERNAL]
    WF -->|invoke_agent| Agent[Agent Span<br/>INTERNAL or CLIENT]
    Agent -->|chat/text_completion| Model[Client Span<br/>CLIENT]
    Agent -->|execute_tool| Tool[Tool Span]
    Agent -->|create_agent| Create[Create Agent Span<br/>CLIENT]
```

## Span 종류 (4 종)

### 1. Create Agent Span
- `gen_ai.operation.name` = `"create_agent"`
- span kind: `CLIENT`
- 용도: 원격 agent service 생성 (OpenAI Assistants API 등)
- span name 규칙: `"create_agent {gen_ai.agent.name}"`

### 2. Invoke Agent Client Span
- `gen_ai.operation.name` = `"invoke_agent"`
- span kind: `CLIENT`
- 용도: 원격 agent 호출 (OpenAI Assistants, AWS Bedrock Agents)

### 3. Invoke Agent Internal Span
- `gen_ai.operation.name` = `"invoke_agent"`
- span kind: `INTERNAL`
- 용도: in-process agent 실행 (LangChain, CrewAI)
- span name: `"invoke_agent {gen_ai.agent.name}"` (name 없으면 `"invoke_agent"`)

### 4. Invoke Workflow Span
- `gen_ai.operation.name` = `"invoke_workflow"`
- span kind: `INTERNAL`
- 용도: multi-agent coordinated execution
- span name: `"invoke_workflow {gen_ai.workflow.name}"`

## Required Attributes (모든 span)

| Attribute | Type | 설명 |
|---|---|---|
| `gen_ai.operation.name` | string | Operation 종류 (chat, generate_content, text_completion, create_agent, invoke_agent, invoke_workflow, embeddings 등) |
| `gen_ai.provider.name` | string | 제공자 식별 (`anthropic`, `openai`, `aws.bedrock`, `gcp.vertex_ai`, `azure.ai.openai`, `cohere`, `deepseek`, `gcp.gemini`, `groq`, `ibm.watsonx.ai`, `mistral_ai`, `perplexity`, `x_ai`) |

Create/client invoke span 추가:
- `error.type` (string, conditionally) — 에러 클래스

## Conditionally Required Attributes

### Agent attributes
| Attribute | 예시 |
|---|---|
| `gen_ai.agent.id` | `asst_5j66UpCpwteGg4YSxUnt7lPY` |
| `gen_ai.agent.name` | `Math Tutor`, `Fiction Writer` |
| `gen_ai.agent.description` | `Helps with math problems` |
| `gen_ai.agent.version` | `1.0.0`, `2025-05-01` |

### Request/Response
- `gen_ai.request.model` — 호출되는 모델명
- `gen_ai.conversation.id` — session/thread 식별자 (예: `conv_5j66UpCpwteGg4YSxUnt7lPY`)
- `gen_ai.output.type` — content type (`text`, `json`, `image`, `speech`)

### Server details
- `server.address`, `server.port`

## Recommended Attributes

### Request parameters
| Attribute | Type | 예시 |
|---|---|---|
| `gen_ai.request.max_tokens` | int | `100` |
| `gen_ai.request.temperature` | double | `0.0` |
| `gen_ai.request.top_p` | double | `1.0` |
| `gen_ai.request.top_k` | double | `1.0` |
| `gen_ai.request.frequency_penalty` | double | `0.1` |
| `gen_ai.request.presence_penalty` | double | `0.1` |
| `gen_ai.request.stop_sequences` | string[] | `["forest", "lived"]` |
| `gen_ai.request.seed` | int | `100` |
| `gen_ai.request.stream` | boolean | |
| `gen_ai.request.choice.count` | int | `3` |

### Token usage (가장 중요)
| Attribute | 설명 |
|---|---|
| `gen_ai.usage.input_tokens` | input prompt 토큰 수 |
| `gen_ai.usage.output_tokens` | response 토큰 수 |
| `gen_ai.usage.cache_creation.input_tokens` | provider-managed cache 에 쓰인 토큰 |
| `gen_ai.usage.cache_read.input_tokens` | cache 에서 읽은 토큰 |
| `gen_ai.usage.reasoning.output_tokens` | CoT/reasoning 출력 토큰 |
| `gen_ai.token.type` | `input` / `output` |

### Response
- `gen_ai.response.id` — `chatcmpl-123`
- `gen_ai.response.model` — 실제 응답 모델 (예: `gpt-4-0613` ≠ request.model)
- `gen_ai.response.finish_reasons` — `["stop"]`, `["stop", "length"]`
- `gen_ai.response.time_to_first_chunk` — streaming TTFB (seconds)

## Opt-In Attributes (민감 콘텐츠)

기본적으로 **수집 안 함**. 명시적 opt-in 필요:

| Attribute | 설명 |
|---|---|
| `gen_ai.input.messages` | 모델에 보낸 chat history (구조화 JSON, schema 존재) |
| `gen_ai.output.messages` | 모델 응답 메시지 |
| `gen_ai.system_instructions` | system prompt |
| `gen_ai.tool.definitions` | agent 가 사용 가능한 tool 정의 목록 |

> JSON schema 가 명세에 함께 정의되어 있어 (gen-ai-input-messages.json,
> gen-ai-output-messages.json, gen-ai-system-instructions.json, gen-ai-tool-definitions.json)
> exporter 호환성 보장.

## Tool Operation Attributes

| Attribute | 예시 |
|---|---|
| `gen_ai.tool.name` | `Flights` |
| `gen_ai.tool.description` | `Multiply two numbers` |
| `gen_ai.tool.type` | `function`, `extension`, `datastore` |
| `gen_ai.tool.call.id` | `call_mszuSIzqtI65i1wAUOE8w5H4` |
| `gen_ai.tool.call.arguments` | `{"location": "San Francisco"}` |
| `gen_ai.tool.call.result` | `{"temperature_range": {"high": 75, "low": 60}}` |

## Retrieval/RAG attributes

- `gen_ai.retrieval.query.text` — retrieval query
- `gen_ai.retrieval.documents` — 검색된 문서 (구조화 JSON)
- `gen_ai.data_source.id` — 데이터 소스 ID
- `gen_ai.embeddings.dimension.count` — embedding 차원

## Evaluation attributes (eval-in-loop)

| Attribute | 예시 |
|---|---|
| `gen_ai.evaluation.name` | `Relevance`, `IntentResolution` |
| `gen_ai.evaluation.score.value` | `4.0` (double) |
| `gen_ai.evaluation.score.label` | `relevant`, `not_relevant`, `correct`, `incorrect` |
| `gen_ai.evaluation.explanation` | free-form 설명 |

## Workflow & Prompt management

- `gen_ai.workflow.name` — `multi_agent_rag`, `customer_support_pipeline`
- `gen_ai.prompt.name` — `analyze-code`

## Deprecated Attributes (참고)

| Old | New |
|---|---|
| `gen_ai.completion` | Event API (제거됨) |
| `gen_ai.prompt` | Event API (제거됨) |
| `gen_ai.system` | `gen_ai.provider.name` |
| `gen_ai.usage.completion_tokens` | `gen_ai.usage.output_tokens` |
| `gen_ai.usage.prompt_tokens` | `gen_ai.usage.input_tokens` |
| `gen_ai.openai.request.response_format` | `gen_ai.output.type` |
| `gen_ai.openai.*` | `openai.*` (provider-specific namespace 분리) |

## MCP (Model Context Protocol) 통합

> "Additionally, the spec includes conventions for the Model Context Protocol (MCP)."

MCP 호출 추적용 별도 convention 이 spec 에 포함되어 있어 Claude/MCP 생태계와 호환.

## 운영 관점 — Stability & Migration

- **OTEL_SEMCONV_STABILITY_OPT_IN** env var 로 새 spec 버전 점진 채택
- 같은 instrumentation 이 legacy 와 experimental 두 버전 attribute 동시 emit 가능
- v1.36.0 이전 attribute 와의 호환성 layer 제공

## 실무 적용 — Agent Trace 표준화

```python
# 의사 코드 예시
with tracer.start_as_current_span(
    f"invoke_agent {agent_name}",
    kind=SpanKind.INTERNAL,
    attributes={
        "gen_ai.operation.name": "invoke_agent",
        "gen_ai.provider.name": "anthropic",
        "gen_ai.agent.name": agent_name,
        "gen_ai.agent.id": agent_id,
        "gen_ai.conversation.id": conv_id,
    }
) as agent_span:
    with tracer.start_as_current_span(
        "chat claude-sonnet-4-6",
        kind=SpanKind.CLIENT,
        attributes={
            "gen_ai.operation.name": "chat",
            "gen_ai.provider.name": "anthropic",
            "gen_ai.request.model": "claude-sonnet-4-6",
            "gen_ai.request.max_tokens": 1024,
            "gen_ai.request.temperature": 0.7,
        }
    ) as model_span:
        response = client.messages.create(...)
        model_span.set_attribute("gen_ai.usage.input_tokens", response.usage.input_tokens)
        model_span.set_attribute("gen_ai.usage.output_tokens", response.usage.output_tokens)
        model_span.set_attribute("gen_ai.usage.cache_read.input_tokens",
                                  response.usage.cache_read_input_tokens)
        model_span.set_attribute("gen_ai.response.id", response.id)
        model_span.set_attribute("gen_ai.response.finish_reasons", [response.stop_reason])
```

## 관련 명세

- [Agent spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/)
- [Client spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/)
- [Metrics](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/)
- [Events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/)
- [Attribute registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- GitHub repo: https://github.com/open-telemetry/semantic-conventions
- Issue #2664 (Agentic Systems): https://github.com/open-telemetry/semantic-conventions/issues/2664
