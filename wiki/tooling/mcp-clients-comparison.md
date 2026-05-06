---
title: MCP Clients Comparison (Claude Desktop / Claude Code / Cursor)
category: tooling
page_type: concept
tags: [tooling, mcp, comparison, claude-desktop, claude-code, cursor, oauth]
sources: [raw/2026-05-06-system-design-mcp-clients-comparison.md]
created: 2026-05-06
updated: 2026-05-06
---

# MCP Clients Comparison

세 주요 MCP 클라이언트(Claude Desktop, Claude Code, Cursor)의 설정 방식, scope 모델, OAuth/transport 지원, plugin 통합 차이를 비교한다.

## 1. Claude Desktop

### 설정 파일 위치
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%AppData%\Claude\claude_desktop_config.json`

### 포맷
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

특징:
- stdio transport 위주 (subprocess 실행)
- 변경 후 재시작 필요
- absolute path 필수
- 별도 OAuth 통합은 connectors 기능에서 제공

## 2. Claude Code

### 설정 명령어 (CLI)

```bash
# stdio 서버 추가
claude mcp add --transport stdio --env KEY=value myserver -- python server.py --port 8080

# HTTP 서버 추가
claude mcp add --transport http stripe https://mcp.stripe.com

# 헤더로 인증
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer YOUR_GITHUB_PAT"

# JSON으로 추가
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

# 관리
claude mcp list
claude mcp get github
claude mcp remove github
```

> Important: All options (--transport, --env, --scope, --header) must come before the server name. The -- (double dash) then separates the server name from the command and arguments.

### 3가지 Scope

| Scope | 로드 범위 | 팀 공유 | 저장 위치 |
|---|---|---|---|
| Local (default) | 현재 프로젝트만 | No | `~/.claude.json` |
| Project | 현재 프로젝트만 | Yes (.mcp.json) | `.mcp.json` (프로젝트 루트) |
| User | 모든 프로젝트 | No | `~/.claude.json` |

Precedence: Local > Project > User > Plugin > claude.ai connectors

### `.mcp.json` 포맷 (Project scope)

```json
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

> For security reasons, Claude Code prompts for approval before using project-scoped servers from .mcp.json files. If you need to reset these approval choices, use the `claude mcp reset-project-choices` command.

### 환경 변수 expansion

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

문법:
- `${VAR}`: 환경변수
- `${VAR:-default}`: 미설정 시 기본값

### OAuth 흐름

> Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections.

```bash
# 서버 추가
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
# Claude Code 안에서 /mcp 명령으로 브라우저 로그인
```

OAuth 옵션:
- `--callback-port`: 고정 redirect URI port
- `--client-id` / `--client-secret`: 사전 등록 자격증명
- DCR (Dynamic Client Registration) 자동 시도, 실패 시 fallback

`authServerMetadataUrl` 오버라이드 (v2.1.64+):
```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

`oauth.scopes` 제한:
```json
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "oauth": {
        "scopes": "channels:read chat:write search:read"
      }
    }
  }
}
```

### Dynamic Headers (non-OAuth 인증)

```json
{
  "mcpServers": {
    "internal-api": {
      "type": "http",
      "url": "https://mcp.internal.example.com",
      "headersHelper": "/opt/bin/get-mcp-auth-headers.sh"
    }
  }
}
```

> The command must write a JSON object of string key-value pairs to stdout. The command runs in a shell with a 10-second timeout. Dynamic headers override any static headers with the same name.

환경변수 주입:
- `CLAUDE_CODE_MCP_SERVER_NAME`
- `CLAUDE_CODE_MCP_SERVER_URL`

### Reconnection / Resilience

> If an HTTP or SSE server disconnects mid-session, Claude Code automatically reconnects with exponential backoff: up to five attempts, starting at a one-second delay and doubling each time.

> As of v2.1.121, Claude Code retries the initial connection up to three times on transient errors such as a 5xx response, a connection refused, or a timeout.

> Stdio servers are local processes and are not reconnected automatically.

### Output Token Limit

> Claude Code will display a warning when MCP tool output exceeds 10,000 tokens. To increase this limit, set the MAX_MCP_OUTPUT_TOKENS environment variable (for example, MAX_MCP_OUTPUT_TOKENS=50000)

`MCP_TIMEOUT` (env): 서버 startup timeout

### Plugin-provided MCP Servers

Plugins can bundle MCP servers via `.mcp.json` at plugin root:

```json
{
  "mcpServers": {
    "database-tools": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": { "DB_URL": "${DB_URL}" }
    }
  }
}
```

특수 변수:
- `${CLAUDE_PLUGIN_ROOT}`: 플러그인 루트
- `${CLAUDE_PLUGIN_DATA}`: 영구 상태 디렉토리 (업데이트 후에도 유지)

## 3. Cursor

### 설정 파일 위치
- 프로젝트: `.cursor/mcp.json`
- 글로벌: `~/.cursor/mcp.json`

### Local stdio
```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "mcp-server"],
      "env": { "API_KEY": "value" }
    }
  }
}
```

### Remote HTTP
```json
{
  "mcpServers": {
    "server-name": {
      "url": "http://localhost:3000/mcp",
      "headers": { "API_KEY": "value" }
    }
  }
}
```

### 변수 interpolation
- `${env:NAME}`: 환경변수
- `${workspaceFolder}`: 프로젝트 루트
- `${userHome}`: 홈 디렉토리

### Tool Approval
> Agent displays available MCP tools and requests approval before execution by default.
> Users can: view tool arguments, enable auto-run in settings, pre-configure auto-run via ~/.cursor/permissions.json

### 지원 transport
- stdio (로컬)
- SSE (deprecated since 2025-03-26 spec, 호환용 유지)
- Streamable HTTP (권장)

## 클라이언트 비교 표

| 기능 | Claude Desktop | Claude Code | Cursor |
|---|---|---|---|
| 설정 파일 | `claude_desktop_config.json` | `~/.claude.json` + `.mcp.json` | `.cursor/mcp.json` |
| Scope | 단일 | Local/Project/User | Project/Global |
| 팀 공유 | No | Yes (.mcp.json checkin) | Yes (.cursor/mcp.json checkin) |
| stdio | Yes | Yes | Yes |
| Streamable HTTP | Yes (connectors) | Yes | Yes |
| OAuth (DCR/PKCE) | Yes (connectors) | Yes (자동) | 부분적 |
| Dynamic headers | No (제한적) | Yes (`headersHelper`) | No (정적 headers만) |
| Plugin 통합 | No | Yes (.claude-plugin) | No (플러그인 시스템 별도) |
| Auto reconnect (HTTP) | - | Yes (exp backoff x5) | - |
| Output limit | - | 10K (환경변수로 조정) | - |
| 변수 expansion | - | `${VAR}`, `${VAR:-default}` | `${env:NAME}`, `${workspaceFolder}` |
| Approval flow | UI prompt | UI prompt + `/mcp` panel | UI prompt + auto-run setting |

## 핵심 인사이트

1. **Claude Code가 가장 풍부**: scope hierarchy, env expansion, dynamic headers, plugin 통합, 자동 reconnect
2. **Cursor는 워크스페이스 변수 강함**: `${workspaceFolder}` 등 IDE 변수 통합
3. **Claude Desktop은 단순함**: subprocess launcher 중심, 변경 시 재시작
4. **모두 stdio + HTTP 지원**: SSE는 deprecated 중
5. **OAuth는 Claude Code가 가장 성숙**: DCR + 사전등록 자격증명 + scope pinning
6. **Project-scoped consent 필요**: Claude Code는 .mcp.json checkin된 서버에 추가 approval 요구

## 관련 문서

- [[mcp-specification-deep-dive]] — 전체 spec 개요
- [[mcp-transport-protocols]] — stdio / Streamable HTTP
- [[mcp-oauth-authorization]] — OAuth 2.1 흐름
- [[mcp-server-development-guide]] — 서버 SDK 패턴
- [[claude-code-plugins-marketplace]] — Claude Code plugin 통합
- [[claude-code]] — Claude Code 메인 페이지
- [[cursor-mcp]] — Cursor MCP 통합 (있다면)

## 참고

- Claude Code MCP: https://code.claude.com/docs/en/mcp
- Cursor MCP: https://cursor.com/docs/context/mcp
- Claude Desktop: https://modelcontextprotocol.io/quickstart/user
- MCP Spec transport: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
