---
source: modelcontextprotocol.io official spec
url:
  - https://modelcontextprotocol.io/specification/2025-06-18/server/tools
  - https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
title: MCP Capabilities & Authorization - Tools API + OAuth 2.1 보안 모델
fetched: 2026-05-06
status: pending_ingest
---

# MCP Capabilities & Authorization

MCP의 transport는 `mcp-protocol.md` 에서 다뤘다. 이 raw는 그 위에 얹히는 **(1) Tools/Resources/Prompts capabilities API spec** 과 **(2) OAuth 2.1 기반 authorization** 을 1차 소스에서 직접 인용한다. Production MCP server 구축 시 가장 중요한 보안 결정은 token audience validation과 PKCE 강제다.

## 1. Tools Capability

### Capability 선언
```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}
```

`listChanged: true` 는 도구 목록 변경 시 notification 발송 가능을 의미.

### tools/list (도구 목록 조회)
**Request**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {"cursor": "optional-cursor-value"}
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "title": "Weather Information Provider",
        "description": "Get current weather information for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "City name or zip code"}
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

페이지네이션은 cursor 기반.

### tools/call (도구 호출)
**Request**:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {"location": "New York"}
  }
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {"type": "text", "text": "Current weather in New York: ..."}
    ],
    "isError": false
  }
}
```

### Tool 정의 (Schema)
| 필드 | Required | 설명 |
|------|----------|------|
| `name` | Yes | 고유 식별자 |
| `title` | No | UI display name |
| `description` | Yes | 기능 설명 (모델이 이걸로 판단) |
| `inputSchema` | Yes | JSON Schema for arguments |
| `outputSchema` | No | JSON Schema for structured result |
| `annotations` | No | behavior 메타데이터 (untrusted!) |

### Tool Annotations (untrusted)
> "For trust & safety and security, clients MUST consider tool annotations to be untrusted unless they come from trusted servers."

| Annotation | 의미 |
|-----------|------|
| `title` | Display title |
| `readOnlyHint` | 읽기만 (side-effect 없음) |
| `destructiveHint` | 파괴적 (rm 등) |
| `idempotentHint` | 멱등 |
| `openWorldHint` | 열린 세계 (외부 영향) |

→ 이 hint를 신뢰하지 말 것. UI 표시에만 사용.

### Tool Result Content 종류
**텍스트**:
```json
{"type": "text", "text": "..."}
```

**이미지**:
```json
{
  "type": "image",
  "data": "base64-encoded-data",
  "mimeType": "image/png",
  "annotations": {"audience": ["user"], "priority": 0.9}
}
```

**오디오**:
```json
{"type": "audio", "data": "base64", "mimeType": "audio/wav"}
```

**Resource link** (URI만 반환):
```json
{
  "type": "resource_link",
  "uri": "file:///project/src/main.rs",
  "name": "main.rs",
  "description": "Primary application entry point",
  "mimeType": "text/x-rust"
}
```

**Embedded resource** (전체 임베드):
```json
{
  "type": "resource",
  "resource": {
    "uri": "file:///project/src/main.rs",
    "mimeType": "text/x-rust",
    "text": "fn main() {...}",
    "annotations": {"audience": ["user", "assistant"], "priority": 0.7}
  }
}
```

### Structured Content + outputSchema
출력이 JSON object일 때 schema 검증 가능:
```json
{
  "outputSchema": {
    "type": "object",
    "properties": {
      "temperature": {"type": "number"},
      "conditions": {"type": "string"}
    },
    "required": ["temperature", "conditions"]
  }
}
```

응답:
```json
{
  "result": {
    "content": [{"type": "text", "text": "{\"temperature\": 22.5, ...}"}],
    "structuredContent": {"temperature": 22.5, "conditions": "Partly cloudy"}
  }
}
```

> "For backwards compatibility, a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block."

### Error 두 종류
**A. Protocol Error** (JSON-RPC 표준):
```json
{
  "error": {"code": -32602, "message": "Unknown tool: invalid_tool_name"}
}
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

### Human-in-the-Loop 원칙
> "For trust & safety and security, there SHOULD always be a human in the loop with the ability to deny tool invocations."
>
> "Provide UI that makes clear which tools are being exposed to the AI model"
> "Insert clear visual indicators when tools are invoked"
> "Present confirmation prompts to the user for operations"

### Mermaid: Tool Call Flow
```mermaid
sequenceDiagram
    participant LLM
    participant Client
    participant Server

    Note over Client,Server: Discovery
    Client->>Server: tools/list
    Server-->>Client: List of tools

    Note over Client,LLM: Tool Selection
    LLM->>Client: Select tool to use

    Note over Client,Server: Invocation
    Client->>Server: tools/call
    Server-->>Client: Tool result
    Client->>LLM: Process result

    Note over Client,Server: Updates
    Server--)Client: tools/list_changed
    Client->>Server: tools/list
    Server-->>Client: Updated tools
```

## 2. Authorization (OAuth 2.1)

### 적용 범위
> "Authorization is OPTIONAL for MCP implementations."
> "Implementations using an HTTP-based transport SHOULD conform to this specification."
> "Implementations using an STDIO transport SHOULD NOT follow this specification, and instead retrieve credentials from the environment."

→ HTTP transport에서만 적용. stdio는 환경변수로 credential 처리.

### 표준 준수
- **OAuth 2.1** IETF DRAFT (draft-ietf-oauth-v2-1-13)
- **RFC 8414**: Authorization Server Metadata
- **RFC 7591**: Dynamic Client Registration
- **RFC 9728**: Protected Resource Metadata
- **RFC 8707**: Resource Indicators (필수!)
- **PKCE**: 필수 (RFC 7636)

### 역할
- **MCP Server** = OAuth 2.1 Resource Server
- **MCP Client** = OAuth 2.1 Client
- **Authorization Server** = 토큰 발급 (별도 호스팅 가능)

### Authorization Server Discovery
1. MCP server는 `WWW-Authenticate` 헤더로 401 응답
2. Client는 헤더에서 `resource_metadata` URL 추출
3. Client는 Protected Resource Metadata 조회
4. Metadata에서 `authorization_servers` 필드 추출
5. AS Metadata Discovery (`/.well-known/oauth-authorization-server`)

### Mermaid: Auth Discovery + Flow
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

### Resource Parameter (RFC 8707) - 필수
> "MCP clients MUST implement Resource Indicators for OAuth 2.0 as defined in RFC 8707."

```
&resource=https%3A%2F%2Fmcp.example.com
```

#### Canonical URI 규칙
- Lowercase scheme/host 권장
- 대문자도 허용 (interop)
- Trailing slash 없는 형태 권장
- Fragment 금지

**유효**:
- `https://mcp.example.com/mcp`
- `https://mcp.example.com:8443`

**무효**:
- `mcp.example.com` (scheme 누락)
- `https://mcp.example.com#fragment`

### Token Usage
```http
GET /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**제약**:
1. 모든 HTTP 요청에 토큰 포함 (같은 세션이라도)
2. URI query string에 토큰 포함 금지

### Token Audience Validation (필수)
> "MCP servers MUST validate that access tokens were issued specifically for them as the intended audience."

토큰의 audience claim에 자신의 canonical URI 포함 여부 반드시 확인.

> "MCP servers MUST NOT pass through the token it received from the MCP client."

→ Token passthrough 절대 금지 (confused deputy 방지).

### Error Codes
| Code | 의미 |
|------|------|
| 401 Unauthorized | 인증 필요 또는 토큰 무효 |
| 403 Forbidden | scope 부족 또는 권한 없음 |
| 400 Bad Request | malformed 요청 |

### Dynamic Client Registration (RFC 7591)
> "MCP clients and authorization servers SHOULD support OAuth 2.0 Dynamic Client Registration Protocol."

이유:
- Client가 모든 MCP server를 사전에 알 수 없음
- 수동 등록은 user friction
- 새 server에 seamless 연결 가능

미지원 AS의 경우 hardcoded client ID 또는 UI 입력으로 대체.

## 3. 보안 모범 사례

### A. Communication Security
- **HTTPS 필수** (모든 AS endpoint)
- Redirect URI는 `localhost` 또는 HTTPS

### B. PKCE 강제
> "MCP clients MUST implement PKCE according to OAuth 2.1 Section 7.5.2."

Authorization code interception 방지.

### C. Token Theft 대응
- Short-lived access token 발급
- Refresh token rotation (public client)
- 안전한 토큰 저장

### D. Open Redirection
- Pre-registered redirect URI 정확 일치 검증
- `state` parameter 사용 + 검증

### E. Confused Deputy 방지
> "MCP proxy servers using static client IDs MUST obtain user consent for each dynamically registered client before forwarding to third-party authorization servers."

Static client ID로 dynamic 등록 시 매번 user consent.

### F. Token Privilege Restriction
1. **Audience validation**: 토큰이 자신을 대상으로 발급된 것인지 확인
2. **No passthrough**: client에서 받은 토큰을 upstream API에 그대로 전달 금지
3. Upstream API 호출 시 별도 토큰 사용

## 4. 엔터프라이즈 적용 관점

### Production 체크리스트
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

### Tool Design 권장사항
- description은 LLM이 routing에 사용 → 정확하고 구체적으로
- destructive/openWorld tool은 annotation에 표시 (UI 경고)
- `isError: true` 와 protocol error를 명확히 구분
- 큰 결과는 resource_link로 반환 (embedded 대신)
- structuredContent + outputSchema로 type-safe 결과

### Anti-pattern
- Tool annotation을 신뢰해서 destructive 자동 승인
- Token을 query string에 포함
- MCP server가 client token을 그대로 upstream에 전달
- Static client ID로 multi-user 환경 지원
- HTTPS 없는 production deployment
- PKCE 미구현 (CSRF/code interception 위험)

## 관련 문서 후보 (ingest 시)
- 기존 `wiki/tooling/mcp-authorization.md`, `mcp-authorization-draft.md` 갱신
- `wiki/tooling/mcp-tools-spec` (concept) - tools API 전용
- `wiki/tooling/oauth-2.1-resource-indicators` (concept)
