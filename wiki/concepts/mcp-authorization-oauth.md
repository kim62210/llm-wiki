---
title: MCP Authorization (OAuth 2.1 + PKCE + Resource Indicators)
category: concepts
page_type: concept
tags: [mcp, oauth, oauth-2.1, pkce, resource-indicators, rfc-8707, dynamic-client-registration, audience-validation]
sources: [raw/2026-05-06-harness-pattern-mcp-capabilities-auth.md]
created: 2026-05-06
updated: 2026-05-06
---

# MCP Authorization

MCP 서버를 OAuth 2.1 Resource Server로 다루는 인증 표준이다. Production MCP 배포에서 가장 중요한 보안 결정은 (1) PKCE 강제, (2) Resource Indicator (RFC 8707) 필수, (3) token audience validation, (4) token passthrough 금지의 4가지로 정리된다.

> 기존 [[mcp-authorization]], [[mcp-authorization-draft]] 와 차별화 — 이 페이지는 source-agnostic하게 OAuth 2.1 + PKCE + RFC 8707 + Audience Validation의 핵심 요건을 1차 source 인용 기반으로 정리하고, Tools API 보안과 함께 실무 체크리스트를 제공한다.

## 1. 적용 범위

> "Authorization is OPTIONAL for MCP implementations."
> "Implementations using an HTTP-based transport SHOULD conform to this specification."
> "Implementations using an STDIO transport SHOULD NOT follow this specification, and instead retrieve credentials from the environment."

| Transport | Authorization 적용 |
|-----------|---------------------|
| stdio | 환경변수 credential |
| HTTP-based ([[mcp-protocol-deep-dive\|Streamable HTTP]]) | OAuth 2.1 + PKCE 권장 |

## 2. 표준 문서 묶음

- **OAuth 2.1** IETF DRAFT (draft-ietf-oauth-v2-1-13)
- **RFC 8414**: Authorization Server Metadata
- **RFC 7591**: Dynamic Client Registration
- **RFC 9728**: Protected Resource Metadata
- **RFC 8707**: Resource Indicators (필수!)
- **PKCE**: RFC 7636 (필수)

## 3. 역할 매핑

```mermaid
flowchart LR
    Client[MCP Client<br/>= OAuth 2.1 Client] -->|1. token 요청| AS[Authorization Server<br/>토큰 발급]
    AS -->|2. access token| Client
    Client -->|3. Bearer token + 요청| Server[MCP Server<br/>= OAuth 2.1 Resource Server]
    Server -->|4. token audience 검증 후 응답| Client
```

- **MCP Server** = OAuth 2.1 Resource Server
- **MCP Client** = OAuth 2.1 Client
- **Authorization Server** = 토큰 발급 (별도 호스팅 가능)

## 4. Authorization Server Discovery 흐름

1. MCP server는 인증 안 된 요청에 `WWW-Authenticate` 헤더로 401 응답
2. Client는 헤더에서 `resource_metadata` URL 추출
3. Client는 Protected Resource Metadata 조회
4. Metadata에서 `authorization_servers` 필드 추출
5. AS Metadata Discovery (`/.well-known/oauth-authorization-server`)

```mermaid
sequenceDiagram
    participant B as Browser
    participant C as Client
    participant M as MCP Server
    participant A as Authorization Server

    C->>M: MCP request (no token)
    M->>C: 401 + WWW-Authenticate header
    C->>M: GET /.well-known/oauth-protected-resource
    M->>C: Resource metadata
    C->>A: GET /.well-known/oauth-authorization-server
    A->>C: Authorization server metadata

    alt Dynamic client registration
        C->>A: POST /register
        A->>C: Client Credentials
    end

    Note over C: Generate PKCE + resource param
    C->>B: Browser auth URL + code_challenge + resource
    B->>A: Authorization request
    Note over A: User authorizes
    A->>B: Redirect to callback (code)
    B->>C: Authorization code callback
    C->>A: Token request + code_verifier + resource
    A->>C: Access token
    C->>M: MCP request + Bearer token
    M-->>C: MCP response
```

## 5. Resource Parameter (RFC 8707) 필수

> "MCP clients MUST implement Resource Indicators for OAuth 2.0 as defined in RFC 8707."

```
&resource=https%3A%2F%2Fmcp.example.com
```

### Canonical URI 규칙
- Lowercase scheme/host 권장 (대문자도 interop 허용)
- Trailing slash 없는 형태 권장
- Fragment 금지

**유효**: `https://mcp.example.com/mcp`, `https://mcp.example.com:8443`
**무효**: `mcp.example.com` (scheme 누락), `https://mcp.example.com#fragment`

## 6. Token Usage

```http
GET /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**제약**:
1. 모든 HTTP 요청에 토큰 포함 (같은 세션이라도)
2. URI query string에 토큰 포함 금지

## 7. Token Audience Validation (필수)

> "MCP servers MUST validate that access tokens were issued specifically for them as the intended audience."

토큰의 audience claim에 자신의 canonical URI 포함 여부 반드시 확인.

> "MCP servers MUST NOT pass through the token it received from the MCP client."

→ Token passthrough 절대 금지 (confused deputy 방지). MCP server가 upstream API를 호출할 때는 별도 토큰 사용.

## 8. PKCE 필수

> "MCP clients MUST implement PKCE according to OAuth 2.1 Section 7.5.2."

Authorization code interception 방지. PKCE 미구현 시 CSRF / authorization code interception 위험.

## 9. Dynamic Client Registration (RFC 7591)

> "MCP clients and authorization servers SHOULD support OAuth 2.0 Dynamic Client Registration Protocol."

이유:
- Client가 모든 MCP server를 사전에 알 수 없음
- 수동 등록은 user friction
- 새 server에 seamless 연결 가능

미지원 AS의 경우 hardcoded client ID 또는 UI 입력으로 대체.

## 10. Error Codes

| Code | 의미 |
|------|------|
| 401 Unauthorized | 인증 필요 또는 토큰 무효 |
| 403 Forbidden | scope 부족 또는 권한 없음 |
| 400 Bad Request | malformed 요청 |

## 11. 보안 모범 사례

### A. Communication Security
- HTTPS 필수 (모든 AS endpoint)
- Redirect URI는 `localhost` 또는 HTTPS

### B. Token Theft 대응
- Short-lived access token 발급 (1시간 이내 권장)
- Refresh token rotation (public client)
- 안전한 토큰 저장

### C. Open Redirection 방지
- Pre-registered redirect URI 정확 일치 검증
- `state` parameter 사용 + 검증

### D. Confused Deputy 방지
> "MCP proxy servers using static client IDs MUST obtain user consent for each dynamically registered client before forwarding to third-party authorization servers."

Static client ID로 dynamic 등록 시 매번 user consent.

### E. Token Privilege Restriction
1. **Audience validation**: 토큰이 자신을 대상으로 발급된 것인지 확인
2. **No passthrough**: client에서 받은 토큰을 upstream API에 그대로 전달 금지
3. Upstream API 호출 시 별도 토큰 사용

## 12. Tools API 보안 측면 (관련)

### Tool Annotations untrusted

> "For trust & safety and security, clients MUST consider tool annotations to be untrusted unless they come from trusted servers."

| Annotation | 의미 |
|-----------|------|
| `title` | Display title |
| `readOnlyHint` | 읽기만 (side-effect 없음) |
| `destructiveHint` | 파괴적 (rm 등) |
| `idempotentHint` | 멱등 |
| `openWorldHint` | 열린 세계 (외부 영향) |

→ 이 hint를 신뢰하지 말 것. UI 표시에만 사용.

### Human-in-the-Loop 원칙

> "For trust & safety and security, there SHOULD always be a human in the loop with the ability to deny tool invocations."
> "Provide UI that makes clear which tools are being exposed to the AI model"
> "Insert clear visual indicators when tools are invoked"
> "Present confirmation prompts to the user for operations"

### Error 두 종류

**A. Protocol Error** (JSON-RPC 표준):
```json
{"error": {"code": -32602, "message": "Unknown tool: invalid_tool_name"}}
```

**B. Tool Execution Error** (`isError: true`):
```json
{
  "result": {
    "content": [{"type": "text", "text": "API rate limit exceeded"}],
    "isError": true
  }
}
```

→ Business logic 오류는 `isError: true`, 프로토콜/스키마 위반은 JSON-RPC error.

## 13. Production 체크리스트

- [ ] HTTP transport: OAuth 2.1 + PKCE 강제
- [ ] stdio transport: 환경변수 credential 사용
- [ ] Resource indicator (`resource` param) 모든 요청에 포함
- [ ] Token audience 검증
- [ ] Token passthrough 금지 (separate token for upstream)
- [ ] HTTPS only (localhost callback 예외)
- [ ] Short-lived access token (1시간 이내 권장)
- [ ] Refresh token rotation
- [ ] Tool annotation을 untrusted로 처리 (UI display 한정)
- [ ] Tool 호출 confirmation UI

## 14. Anti-pattern

- Tool annotation을 신뢰해서 destructive 자동 승인
- Token을 query string에 포함
- MCP server가 client token을 그대로 upstream에 전달
- Static client ID로 multi-user 환경 지원
- HTTPS 없는 production deployment
- PKCE 미구현 (CSRF/code interception 위험)
- Audience validation 누락 → confused deputy 공격

## 관련 문서

- [[mcp-authorization]] — MCP OAuth 일반 entity
- [[mcp-protocol-deep-dive]] — Transport spec과 함께 적용
- [[mcp-specification-2025-11-25]] — 2025-11-25 스펙 요약
- [[mcp-architecture]] — MCP 아키텍처
- [[claude-code-mcp-security-reckoning]] — Production 사고 사례
- [[mcp-rce-vulnerability-2026]] — 2026 RCE 사건
- [[ai-agent-security]] — 에이전트 보안 일반
