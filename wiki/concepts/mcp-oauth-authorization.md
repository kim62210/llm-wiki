---
title: MCP OAuth Authorization (OAuth 2.1 + DCR + Resource Indicators)
category: concepts
page_type: concept
tags: [concepts, mcp, oauth, authorization, security, pkce, rfc8707, dcr]
sources: [raw/2026-05-06-system-design-mcp-authorization.md]
created: 2026-05-06
updated: 2026-05-06
---

# MCP OAuth Authorization (2025-06-18)

MCP HTTP transport용 OAuth 2.1 기반 인증 흐름을 정리한다. Authorization Server Discovery부터 PKCE, Resource Indicator(RFC 8707), DCR까지.

## 적용 범위

> The Model Context Protocol provides authorization capabilities at the transport level, enabling MCP clients to make requests to restricted MCP servers on behalf of resource owners. This specification defines the authorization flow for HTTP-based transports.

> Authorization is OPTIONAL for MCP implementations. When supported:
> - Implementations using an HTTP-based transport SHOULD conform to this specification.
> - Implementations using an STDIO transport SHOULD NOT follow this specification, and instead retrieve credentials from the environment.
> - Implementations using alternative transports MUST follow established security best practices for their protocol.

핵심:
- **HTTP transport에만 적용**
- stdio는 환경변수에서 자격증명 (이 spec 미적용)
- OPTIONAL이지만 지원 시 SHOULD 따라야 함

## 표준 준수 (2025-06-18 기준)

| RFC / 표준 | 역할 |
|---|---|
| OAuth 2.1 (draft-ietf-oauth-v2-1-13) | 기본 프레임워크 |
| RFC 8414 | Authorization Server Metadata 디스커버리 |
| RFC 7591 | Dynamic Client Registration (DCR) |
| RFC 9728 | Protected Resource Metadata |
| RFC 8707 | Resource Indicators (audience binding) |

## 3가지 역할

| 역할 | OAuth 매핑 |
|---|---|
| MCP Server | Resource Server |
| MCP Client | OAuth Client |
| 사용자 | Resource Owner |
| Authorization Server | 별도 또는 Resource Server와 통합 |

## 의무 (MUST 항목)

> 1. Authorization servers MUST implement OAuth 2.1 with appropriate security measures for both confidential and public clients.
> 2. Authorization servers and MCP clients SHOULD support the OAuth 2.0 Dynamic Client Registration Protocol (RFC7591).
> 3. MCP servers MUST implement OAuth 2.0 Protected Resource Metadata (RFC9728). MCP clients MUST use OAuth 2.0 Protected Resource Metadata for authorization server discovery.
> 4. Authorization servers MUST provide OAuth 2.0 Authorization Server Metadata (RFC8414). MCP clients MUST use the OAuth 2.0 Authorization Server Metadata.

## Authorization Server Discovery 흐름

```mermaid
sequenceDiagram
    participant C as Client
    participant M as MCP Server (Resource Server)
    participant A as Authorization Server

    C->>M: MCP request without token
    M-->>C: HTTP 401 Unauthorized with WWW-Authenticate header
    Note over C: Extract resource_metadata from WWW-Authenticate

    C->>M: GET /.well-known/oauth-protected-resource
    M-->>C: Resource metadata with authorization server URL
    Note over C: Validate RS metadata, build AS metadata URL

    C->>A: GET /.well-known/oauth-authorization-server
    A-->>C: Authorization server metadata

    Note over C,A: OAuth 2.1 authorization flow happens here

    C->>A: Token request
    A-->>C: Access token

    C->>M: MCP request with access token
    M-->>C: MCP response
```

> MCP servers MUST use the HTTP header `WWW-Authenticate` when returning a 401 Unauthorized to indicate the location of the resource server metadata URL as described in RFC9728 Section 5.1.

## Dynamic Client Registration (DCR)

> MCP clients and authorization servers SHOULD support the OAuth 2.0 Dynamic Client Registration Protocol (RFC7591) to allow MCP clients to obtain OAuth client IDs without user interaction.

DCR이 거의 의무에 가까운 SHOULD인 이유:
- 모르는 MCP 서버에 자동 연결을 위해 필수에 가까움
- 사용자 마찰 최소화
- 새 MCP 서버에 seamless connection
- 인증 서버는 자체 등록 정책 implement 가능

DCR 미지원 시 폴백:
1. 클라이언트별 hardcoded client ID (+ creds)
2. 사용자가 UI에서 직접 입력 (서버가 호스팅한 설정 인터페이스)

## 전체 Authorization Flow (PKCE + Resource Indicator)

```mermaid
sequenceDiagram
    participant B as User-Agent (Browser)
    participant C as Client
    participant M as MCP Server (Resource Server)
    participant A as Authorization Server

    C->>M: MCP request without token
    M->>C: HTTP 401 Unauthorized with WWW-Authenticate header

    C->>M: Request Protected Resource Metadata
    M->>C: Return metadata

    Note over C: Parse metadata and extract authorization server(s)

    C->>A: GET /.well-known/oauth-authorization-server
    A->>C: Authorization server metadata response

    alt Dynamic client registration
        C->>A: POST /register
        A->>C: Client Credentials
    end

    Note over C: Generate PKCE parameters, Include resource parameter
    C->>B: Open browser with authorization URL + code_challenge + resource
    B->>A: Authorization request with resource parameter
    Note over A: User authorizes
    A->>B: Redirect to callback with authorization code
    B->>C: Authorization code callback
    C->>A: Token request + code_verifier + resource
    A->>C: Access token (+ refresh token)
    C->>M: MCP request with access token
    M-->>C: MCP response
```

## Resource Parameter (RFC 8707)

> MCP clients MUST implement Resource Indicators for OAuth 2.0 as defined in RFC 8707 to explicitly specify the target resource for which the token is being requested. The resource parameter:
> 1. MUST be included in both authorization requests and token requests.
> 2. MUST identify the MCP server that the client intends to use the token with.
> 3. MUST use the canonical URI of the MCP server as defined in RFC 8707 Section 2.

### Canonical Server URI

유효:
- `https://mcp.example.com/mcp`
- `https://mcp.example.com`
- `https://mcp.example.com:8443`
- `https://mcp.example.com/server/mcp`

무효:
- `mcp.example.com` (스킴 없음)
- `https://mcp.example.com#fragment` (프래그먼트 포함)

> While both `https://mcp.example.com/` (with trailing slash) and `https://mcp.example.com` (without trailing slash) are technically valid, implementations SHOULD consistently use the form without the trailing slash.

예시:
```
&resource=https%3A%2F%2Fmcp.example.com
```

## Access Token 사용

```http
GET /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

> Access tokens MUST NOT be included in the URI query string
> authorization MUST be included in every HTTP request from client to server, even if they are part of the same logical session.

## Token Validation

> MCP servers MUST validate that access tokens were issued specifically for them as the intended audience, according to RFC 8707 Section 2.
> MCP clients MUST NOT send tokens to the MCP server other than ones issued by the MCP server's authorization server.
> Authorization servers MUST only accept tokens that are valid for use with their own resources.
> MCP servers MUST NOT accept or transit any other tokens.

## HTTP 오류 코드

| Status | 설명 | 사용 |
|---|---|---|
| 401 | Unauthorized | 인증 필요 또는 토큰 무효 |
| 403 | Forbidden | 스코프 부족 또는 권한 없음 |
| 400 | Bad Request | 잘못된 인증 요청 |

## Security Considerations - 핵심 위협 모델

### 1. Token Theft

> Clients and servers MUST implement secure token storage and follow OAuth best practices.
> Authorization servers SHOULD issue short-lived access tokens to reduce the impact of leaked tokens.
> For public clients, authorization servers MUST rotate refresh tokens.

### 2. Communication Security

> 1. All authorization server endpoints MUST be served over HTTPS.
> 2. All redirect URIs MUST be either localhost or use HTTPS.

### 3. Authorization Code Protection — PKCE 의무

> MCP clients MUST implement PKCE according to OAuth 2.1 Section 7.5.2.
> PKCE helps prevent authorization code interception and injection attacks by requiring clients to create a secret verifier-challenge pair.

### 4. Open Redirection

> MCP clients MUST have redirect URIs registered with the authorization server.
> Authorization servers MUST validate exact redirect URIs against pre-registered values.
> MCP clients SHOULD use and verify state parameters in the authorization code flow.

### 5. Confused Deputy

> MCP proxy servers using static client IDs MUST obtain user consent for each dynamically registered client before forwarding to third-party authorization servers.

[[mcp-security-model]]에서 confused deputy 공격 시나리오 + mitigation 상세.

### 6. Access Token Privilege Restriction (Token Passthrough 금지)

> MCP servers MUST validate access tokens before processing the request, ensuring the access token is issued specifically for the MCP server.
> If the MCP server makes requests to upstream APIs, it may act as an OAuth client to them. The access token used at the upstream API is a separate token, issued by the upstream authorization server. The MCP server MUST NOT pass through the token it received from the MCP client.
> MCP clients MUST implement and use the resource parameter as defined in RFC 8707 to explicitly specify the target resource.

## 구현 체크리스트

- [ ] Authorization Server: OAuth 2.1 (draft-13) + RFC 8414 metadata
- [ ] MCP Server: RFC 9728 Protected Resource Metadata + WWW-Authenticate 헤더
- [ ] MCP Client: PKCE + RFC 8707 resource parameter + DCR 지원
- [ ] HTTPS 강제 (localhost 예외 가능)
- [ ] Bearer 토큰 (헤더 only, query string 금지)
- [ ] 토큰 audience validation (passthrough 금지)
- [ ] Refresh token rotation (public clients)

## 핵심 인사이트

1. **DCR이 거의 의무에 가까운 SHOULD**: 모르는 MCP 서버에 자동 연결을 위해 필수에 가까움
2. **Resource Indicators(RFC 8707)가 MUST**: 토큰의 audience를 강제 → cross-server 토큰 도용 방지
3. **Token passthrough는 명시적 금지**: 업스트림 API 호출 시 별도 토큰 발급 필수
4. **stdio transport는 ENV로 처리**: 이 spec에서 제외
5. **PKCE 필수**: public client뿐 아니라 모든 MCP client

## 관련 문서

- [[mcp-specification-deep-dive]] — 전체 spec 개요
- [[mcp-transport-protocols]] — HTTP transport 흐름
- [[mcp-security-model]] — 6대 공격 벡터 + mitigation
- [[mcp-authorization]] — 이전 버전 entity 페이지
- [[mcp-authorization-draft]] — 초기 draft
- [[claude-code-mcp-security-reckoning]] — 실제 사고 사례

## 참고

- 본 페이지: https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
- OAuth 2.1 draft: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13
- RFC 9728 Protected Resource Metadata: https://datatracker.ietf.org/doc/html/rfc9728
- RFC 7591 DCR: https://datatracker.ietf.org/doc/html/rfc7591
- RFC 8707 Resource Indicators: https://www.rfc-editor.org/rfc/rfc8707.html
