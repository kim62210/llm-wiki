---
title: MCP Protocol Deep Dive (Model Context Protocol 심층)
category: concepts
page_type: concept
tags: [mcp, model-context-protocol, json-rpc, streamable-http, stdio, session-management, transport]
sources: [raw/2026-05-06-harness-pattern-mcp-protocol.md]
created: 2026-05-06
updated: 2026-05-06
---

# MCP Protocol Deep Dive

Model Context Protocol(MCP)은 LLM 호스트와 외부 데이터 소스/도구 사이의 통합을 표준화하는 오픈 프로토콜이다. JSON-RPC 2.0 기반 + stateful connection + capability negotiation을 핵심으로 한다. 2025년에 Streamable HTTP transport가 도입되며 legacy SSE를 대체하고 있다.

> 기존 [[mcp]], [[mcp-architecture]], [[mcp-specification-2025-11-25]], [[what-is-mcp]] 와 차별화 — 이 페이지는 transport spec(stdio + Streamable HTTP), session management(Mcp-Session-Id), security model의 핵심 요건을 1차 source 인용 기반으로 정리한다.

## 1. 아키텍처 3-tier

- **Hosts**: LLM 애플리케이션 (Claude Desktop, Claude Code, IDE 등) — connection을 initiate
- **Clients**: Host 내부의 connector
- **Servers**: context/capability를 제공하는 서비스

> "MCP takes some inspiration from the Language Server Protocol, which standardizes how to add support for programming languages across a whole ecosystem of development tools."

## 2. Capabilities (3+3+utility)

```mermaid
flowchart LR
    Server[MCP Server] -->|Resources| Client
    Server -->|Prompts| Client
    Server -->|Tools| Client
    Client[MCP Client] -->|Sampling| Server
    Client -->|Roots| Server
    Client -->|Elicitation| Server
    Both[양쪽 모두] -.- Util[Utilities<br/>Configuration / Progress<br/>Cancellation / Logging]
```

### Server → Client 제공
| Capability | 설명 |
|------------|------|
| **Resources** | 사용자 또는 모델이 사용할 context/data |
| **Prompts** | 템플릿화된 메시지/워크플로우 |
| **Tools** | 모델이 실행할 함수 |

### Client → Server 제공
| Capability | 설명 |
|------------|------|
| **Sampling** | Server-initiated 에이전트 행동, recursive LLM 호출 |
| **Roots** | Server가 작동할 URI/filesystem 경계 조회 |
| **Elicitation** | Server가 사용자에게 추가 정보 요청 |

### Utilities
Configuration, Progress tracking, Cancellation, Error reporting, Logging.

## 3. Transport: stdio (권장)

> "Clients SHOULD support stdio whenever possible."

### 동작 방식
- Client가 server를 subprocess로 launch
- Server는 stdin에서 JSON-RPC 메시지 read, stdout으로 send
- Messages는 newline으로 구분, **embedded newline 금지**
- Server는 stderr에 UTF-8 로그 기록 가능
- Server는 stdout에 valid MCP 메시지 외 아무것도 쓰지 않아야 함

```mermaid
sequenceDiagram
    participant Client
    participant Server as Server Process
    Client->>+Server: Launch subprocess
    loop Message Exchange
        Client->>Server: Write to stdin
        Server->>Client: Write to stdout
        Server--)Client: Optional logs on stderr
    end
    Client->>Server: Close stdin, terminate subprocess
    deactivate Server
```

→ Local IDE/CLI 통합에 최적. latency 가장 낮음.

## 4. Transport: Streamable HTTP (2025-11+)

> "This replaces the HTTP+SSE transport from protocol version 2024-11-05."

### 핵심 사양
- 단일 HTTP endpoint (POST + GET 지원)
- POST: Client → Server 메시지 전송
- GET: SSE stream 열기 (Server → Client notification)
- Streaming은 SSE 기반 (옵셔널)

### POST 요청 규칙
1. Client는 `Accept: application/json, text/event-stream` 헤더 포함 필수
2. Body는 단일 JSON-RPC request/notification/response
3. **Notification/Response 입력 시**: 서버는 `202 Accepted` (no body), 거절 시 4xx
4. **Request 입력 시**: 서버는 `Content-Type: text/event-stream` (SSE) 또는 `application/json` (단일 응답) 중 선택

### GET 요청 (Server → Client 채널)
- Client가 SSE stream을 열기 위해 GET 요청
- 서버는 `text/event-stream` 또는 `405 Method Not Allowed`
- 서버는 GET stream에 client request에 대한 response를 보내지 않음 (resumability 제외)

### Resumability & Redelivery
- SSE event id 부여 → 연결 끊김 시 client는 GET + `Last-Event-ID` 헤더로 재연결
- 서버는 이전 stream에서만 replay (다른 stream 메시지는 replay 안 함)

### Multiple Connections
- Client는 동시에 여러 SSE stream에 연결 가능
- Server는 각 메시지를 **하나의 stream에서만** 송신 (broadcast 금지)

## 5. Session Management

### Mcp-Session-Id 헤더 라이프사이클

1. Server가 initialize 응답에 `Mcp-Session-Id` 헤더로 세션 ID 부여 (옵션)
2. Session ID는 globally unique + cryptographically secure (UUID, JWT, hash)
3. 가시 ASCII 문자(0x21-0x7E)만 사용
4. Client는 이후 모든 요청에 `Mcp-Session-Id` 헤더 포함 필수
5. 서버가 세션 종료 시 → 해당 ID 요청에 `404 Not Found`
6. Client가 `404` 받으면 → 새 InitializeRequest로 새 세션 시작
7. Client가 명시 종료 → `DELETE /mcp` + `Mcp-Session-Id`

```mermaid
sequenceDiagram
    participant Client
    participant Server

    note over Client, Server: initialization
    Client->>+Server: POST InitializeRequest
    Server->>-Client: InitializeResponse<br/>Mcp-Session-Id: 1868a90c...

    Client->>+Server: POST InitializedNotification
    Server->>-Client: 202 Accepted

    note over Client, Server: client request (sync)
    Client->>+Server: POST request + Mcp-Session-Id
    Server->>-Client: 200 + JSON response

    note over Client, Server: client request (streaming)
    Client->>+Server: POST request + Mcp-Session-Id
    loop SSE stream
        Server-)Client: SSE messages
    end
    Server-)Client: SSE event response
    deactivate Server

    note over Client, Server: server-initiated channel
    Client->>+Server: GET /mcp + Mcp-Session-Id
    loop SSE stream
        Server-)Client: server requests/notifications
    end
    deactivate Server
```

## 6. Protocol Version Negotiation

```
MCP-Protocol-Version: 2025-06-18
```

- Client는 모든 후속 요청에 protocol version 헤더 포함
- Initialization 단계에서 negotiate된 버전 사용
- 헤더 없으면 server는 `2025-03-26` 가정 (backwards compat)
- 서버는 unsupported version 시 `400 Bad Request`

## 7. Security Model 4가지 핵심 원칙

### A. User Consent and Control
> "Users must explicitly consent to and understand all data access and operations."

### B. Data Privacy
> "Hosts must obtain explicit user consent before exposing user data to servers."
> "Hosts must not transmit resource data elsewhere without user consent."

### C. Tool Safety
> "Tools represent arbitrary code execution and must be treated with appropriate caution."
> "Descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server."

### D. LLM Sampling Controls
> "Users must explicitly approve any LLM sampling requests."
> "The protocol intentionally limits server visibility into prompts."

## 8. Streamable HTTP 전용 보안 hardening

> "Servers MUST validate the Origin header on all incoming connections to prevent DNS rebinding attacks."
> "When running locally, servers SHOULD bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)."
> "Servers SHOULD implement proper authentication for all connections."

3가지 hardening:
1. `Origin` 헤더 검증 (DNS rebinding 차단)
2. localhost(127.0.0.1) 바인딩 (개발)
3. 인증 구현 (production)

## 9. Backwards Compatibility (HTTP+SSE → Streamable HTTP)

### Server side
신/구 endpoint를 동시 호스팅 (legacy SSE + new MCP endpoint).

### Client side
1. URL 받은 후 InitializeRequest를 POST 시도
2. 성공 → Streamable HTTP server
3. 실패 (4xx) → GET으로 SSE stream 열기 → `endpoint` event 받으면 legacy HTTP+SSE server로 인식

## 10. JSON-RPC 메시지 포맷

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search",
    "arguments": {"query": "MCP spec"}
  }
}
```

- UTF-8 encoded
- Stateful connection 유지
- Capability negotiation은 initialization phase에서

## 11. Transport 선택 가이드

| 시나리오 | 권장 Transport |
|----------|---------------|
| Local IDE/CLI 통합 | stdio |
| Cloud-hosted MCP server | Streamable HTTP |
| 다중 클라이언트 동시 접속 | Streamable HTTP |
| Latency-critical | stdio (subprocess 직접) |
| Browser-based MCP client | Streamable HTTP |

## 12. Production 보안 체크리스트

- [ ] Origin 헤더 검증 활성화
- [ ] localhost-only binding (development)
- [ ] OAuth 2.1 또는 JWT 인증 (production) — 자세한 내용은 [[mcp-authorization-oauth]]
- [ ] User consent UI 구현
- [ ] Tool annotation을 untrusted로 처리 (sandbox)
- [ ] Sampling 호출에 사용자 승인 게이트

## 13. Session ID 운영

- UUID v7 또는 ULID로 정렬 가능 + 보안성
- 세션 만료 시 클라이언트가 자동 재초기화
- DELETE 미지원 시 405 응답 → TTL 기반 cleanup

## 관련 문서

- [[mcp]] — MCP 일반 개념
- [[mcp-architecture]] — 아키텍처 개요
- [[mcp-specification-2025-11-25]] — 2025-11-25 스펙 요약
- [[mcp-authorization-oauth]] — OAuth 2.1 + PKCE 인증
- [[what-is-mcp]] — 기초 입문
- [[hook-system-patterns]] — MCP tool hook 통합
- [[tool-orchestration-patterns]] — MCP 다중 서버에서 tool search
- [[claude-code-mcp-security-reckoning]] — production 보안 사고 사례
