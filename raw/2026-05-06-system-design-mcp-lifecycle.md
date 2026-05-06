---
source: modelcontextprotocol.io
url: https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle
title: "MCP Lifecycle & Capability Negotiation (2025-06-18)"
fetched: 2026-05-06
status: pending_ingest
---

# MCP Lifecycle - 2025-06-18 spec

## 3-Phase Lifecycle

> The Model Context Protocol (MCP) defines a rigorous lifecycle for client-server connections that ensures proper capability negotiation and state management.
> 1. Initialization: Capability negotiation and protocol version agreement
> 2. Operation: Normal protocol communication
> 3. Shutdown: Graceful termination of the connection

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
    Note over Client,Server: Connection closed
```

## Initialization 메시지 구조

### Request (Client → Server)

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

### Response (Server → Client)

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

### Initialized Notification

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

## Pre-Initialize 제약

> The client SHOULD NOT send requests other than pings before the server has responded to the initialize request.
> The server SHOULD NOT send requests other than pings and logging before receiving the initialized notification.

- initialize 응답 전: 클라이언트는 ping 외 금지
- initialized 알림 전: 서버는 ping/logging 외 금지

## Version Negotiation 규칙

원문:

> In the initialize request, the client MUST send a protocol version it supports. This SHOULD be the latest version supported by the client.
> If the server supports the requested protocol version, it MUST respond with the same version. Otherwise, the server MUST respond with another protocol version it supports. This SHOULD be the latest version supported by the server.
> If the client does not support the version in the server's response, it SHOULD disconnect.

요약:
1. 클라이언트는 자신의 최신 버전을 요청
2. 서버 동의 → 같은 버전 응답
3. 서버 미동의 → 자신의 최신 버전 응답
4. 클라이언트 미지원 → 연결 종료

HTTP 사용 시 `MCP-Protocol-Version` 헤더 필수.

## Capability Negotiation 표

| Category | Capability | 설명 |
|---|---|---|
| Client | `roots` | 파일시스템 root 제공 |
| Client | `sampling` | 서버의 LLM 샘플링 요청 처리 |
| Client | `elicitation` | 서버의 사용자 정보 요청 처리 |
| Client | `experimental` | 비표준 실험 기능 |
| Server | `prompts` | prompt 템플릿 제공 |
| Server | `resources` | 리소스 제공 |
| Server | `tools` | 도구 제공 |
| Server | `logging` | 구조화된 로그 |
| Server | `completions` | 인자 자동완성 |
| Server | `experimental` | 비표준 실험 기능 |

### 서브 Capability

- `listChanged`: 목록 변경 알림 지원 (prompts/resources/tools 공통)
- `subscribe`: 개별 항목 변경 구독 (resources 전용)

> Both parties MUST:
> - Respect the negotiated protocol version
> - Only use capabilities that were successfully negotiated

## Shutdown

> No specific shutdown messages are defined—instead, the underlying transport mechanism should be used to signal connection termination

### stdio 종료 절차

> 1. First, closing the input stream to the child process (the server)
> 2. Waiting for the server to exit, or sending SIGTERM if the server does not exit within a reasonable time
> 3. Sending SIGKILL if the server does not exit within a reasonable time after SIGTERM

### HTTP 종료

연관된 HTTP 연결을 닫는 것으로 종료 신호.

## Timeouts

> Implementations SHOULD establish timeouts for all sent requests, to prevent hung connections and resource exhaustion. When the request has not received a success or error response within the timeout period, the sender SHOULD issue a cancellation notification for that request and stop waiting for a response.
> SDKs and other middleware SHOULD allow these timeouts to be configured on a per-request basis.
> Implementations MAY choose to reset the timeout clock when receiving a progress notification corresponding to the request, as this implies that work is actually happening. However, implementations SHOULD always enforce a maximum timeout, regardless of progress notifications, to limit the impact of a misbehaving client or server.

핵심:
- per-request 타임아웃 권장
- 타임아웃 시 cancellation notification 발송
- progress notification으로 시계 reset 가능하나 max timeout은 항상 강제

## Error Handling

원문:

> Implementations SHOULD be prepared to handle these error cases:
> - Protocol version mismatch
> - Failure to negotiate required capabilities
> - Request timeouts

오류 코드 예 (JSON-RPC 표준 -32602 = Invalid params):

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

## 핵심 인사이트

1. **State machine 명확함**: 3-phase가 LSP에서 차용. 잘못된 phase에서의 메시지는 SHOULD NOT.
2. **Version mismatch는 단절**: spec이 disconnect를 명시하므로 graceful degrade 부담을 클라이언트에 위임.
3. **Capability는 양방향**: client → server뿐 아니라 server → client (sampling/roots/elicitation) 도 정의.
4. **Capability sub-fields는 선택**: `subscribe`, `listChanged` 등 미선언이면 미지원으로 간주.
5. **Shutdown은 transport-specific**: 통일된 shutdown RPC 없음 - transport 레벨에서 처리.

## 참고

- 본 페이지: https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle
- Transports: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
