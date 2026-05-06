---
source: modelcontextprotocol.io
url: https://modelcontextprotocol.io/specification/2025-06-18
title: "MCP Specification 2025-06-18 - Core Overview, Lifecycle, Transport"
fetched: 2026-05-06
status: pending_ingest
---

# MCP Specification 2025-06-18 - 핵심 개요

## 메타 정보

- 공식 spec 버전: **2025-06-18** (이전: 2025-03-26, 2024-11-05)
- 메시지 포맷: **JSON-RPC 2.0**, UTF-8 인코딩 필수
- 정의 스키마: TypeScript schema (`schema/2025-06-18/schema.ts` in modelcontextprotocol/specification 레포)

## 아키텍처: Host / Client / Server

원문 인용:

> The protocol uses JSON-RPC 2.0 messages to establish communication between:
> - **Hosts**: LLM applications that initiate connections
> - **Clients**: Connectors within the host application
> - **Servers**: Services that provide context and capabilities

한국어 요약:
- **Host**: LLM 애플리케이션 본체 (Claude Desktop, Claude Code, Cursor 등)
- **Client**: Host 안에서 단일 MCP 서버와 1:1 연결을 담당하는 커넥터
- **Server**: 컨텍스트/도구를 제공하는 외부 프로세스 또는 HTTP 엔드포인트

LSP (Language Server Protocol) 영감 — "표준화된 LSP가 IDE 생태계를 확장한 것처럼, MCP는 AI 애플리케이션 생태계를 확장한다."

## 서버가 클라이언트에게 제공하는 기능

> Servers offer any of the following features to clients:
> - Resources: Context and data, for the user or the AI model to use
> - Prompts: Templated messages and workflows for users
> - Tools: Functions for the AI model to execute

| Feature | 설명 | 한국어 요약 |
|---|---|---|
| Resources | URI로 식별되는 정적/동적 컨텍스트 | 파일 내용, DB row 등 모델/사용자가 읽는 데이터 |
| Prompts | 사용자가 호출할 수 있는 템플릿 메시지 | 미리 정의된 prompt slash command 같은 것 |
| Tools | 모델이 호출 가능한 함수 | 모델이 실행하는 액션 |

## 클라이언트가 서버에게 제공하는 기능

> Clients may offer the following features to servers:
> - Sampling: Server-initiated agentic behaviors and recursive LLM interactions
> - Roots: Server-initiated inquiries into uri or filesystem boundaries to operate in
> - Elicitation: Server-initiated requests for additional information from users

| Feature | 설명 |
|---|---|
| Sampling | 서버가 클라이언트의 LLM에 질의 (재귀적 LLM 호출) |
| Roots | 서버가 작업할 수 있는 파일시스템 경계 조회 |
| Elicitation | 서버가 사용자에게 추가 정보 요청 (2025-06-18 신규) |

## Lifecycle - 3단계

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Note over Client,Server: Initialization Phase
    Client->>+Server: initialize request
    Server-->>Client: initialize response
    Client--)Server: initialized notification

    Note over Client,Server: Operation Phase

    Note over Client,Server: Shutdown
    Client--)-Server: Disconnect
```

### 1. Initialization

클라이언트가 먼저 `initialize` 요청 전송:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-06-18",
    "capabilities": {
      "roots": { "listChanged": true },
      "sampling": {},
      "elicitation": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "title": "Example Client Display Name",
      "version": "1.0.0"
    }
  }
}
```

서버 응답:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-06-18",
    "capabilities": {
      "logging": {},
      "prompts": { "listChanged": true },
      "resources": { "subscribe": true, "listChanged": true },
      "tools": { "listChanged": true }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "title": "Example Server Display Name",
      "version": "1.0.0"
    },
    "instructions": "Optional instructions for the client"
  }
}
```

이후 클라이언트가 `notifications/initialized` 알림을 보내야 정상 운영 단계로 진입.

> The client SHOULD NOT send requests other than pings before the server has responded to the initialize request.
> The server SHOULD NOT send requests other than pings and logging before receiving the initialized notification.

### 2. Version Negotiation

> If the server supports the requested protocol version, it MUST respond with the same version. Otherwise, the server MUST respond with another protocol version it supports. This SHOULD be the latest version supported by the server.
> If the client does not support the version in the server's response, it SHOULD disconnect.

- 클라이언트는 자신이 지원하는 *최신* 버전 송신
- 서버가 미지원이면 자신이 지원하는 버전 (가능하면 최신) 회신
- 클라이언트가 서버 회신 버전을 지원 못하면 연결 끊는다

### 3. Capability Negotiation 표

| Category | Capability | 설명 |
|---|---|---|
| Client | `roots` | 파일시스템 root 제공 가능 |
| Client | `sampling` | LLM 샘플링 요청 처리 |
| Client | `elicitation` | 사용자 정보 요청 처리 |
| Client | `experimental` | 비표준 실험 기능 |
| Server | `prompts` | prompt 템플릿 제공 |
| Server | `resources` | 읽을 수 있는 리소스 제공 |
| Server | `tools` | 호출 가능한 tool 제공 |
| Server | `logging` | 구조화된 로그 발생 |
| Server | `completions` | 인자 자동완성 |
| Server | `experimental` | 비표준 실험 기능 |

서브 capability:
- `listChanged`: 목록 변경 알림 (prompts/resources/tools)
- `subscribe`: 개별 항목 변경 구독 (resources only)

### 4. Shutdown

명시적 shutdown 메시지 없이 transport 레벨에서 종료:
- **stdio**: 클라이언트가 stdin 닫고 → SIGTERM → SIGKILL 단계
- **HTTP**: HTTP 연결 종료

## Timeouts & Error Handling

> Implementations SHOULD establish timeouts for all sent requests. When the request has not received a success or error response within the timeout period, the sender SHOULD issue a cancellation notification.
> Implementations MAY choose to reset the timeout clock when receiving a progress notification ... However, implementations SHOULD always enforce a maximum timeout, regardless of progress notifications, to limit the impact of a misbehaving client or server.

오류 예시:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```

## Security & Trust 4대 원칙 (spec에서 직접 발췌)

1. **User Consent and Control**
   - 모든 데이터 접근/작업에 명시적 동의 필수
   - 사용자는 무엇이 공유되고 어떤 액션이 일어나는지 통제 가능해야 함

2. **Data Privacy**
   - Host는 사용자 데이터를 서버에 노출하기 전 명시적 동의를 받아야 함
   - 동의 없이 리소스 데이터를 외부로 전송 금지

3. **Tool Safety**
   > Tools represent arbitrary code execution and must be treated with appropriate caution.
   > In particular, descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server.
   - 도구 어노테이션은 신뢰되지 않는 서버에서는 untrusted
   - 모든 도구 호출 전 사용자 동의 필요

4. **LLM Sampling Controls**
   - 모든 sampling 요청은 사용자 명시적 승인
   - 사용자는 sampling 발생 여부, 실제 prompt, 서버가 받는 결과 모두 통제

## 추가 유틸리티

- Configuration
- Progress tracking
- Cancellation
- Error reporting
- Logging

## 참고 링크

- 전체 스펙: https://modelcontextprotocol.io/specification/2025-06-18
- TypeScript schema: https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-06-18/schema.ts
- llms.txt 인덱스: https://modelcontextprotocol.io/llms.txt
