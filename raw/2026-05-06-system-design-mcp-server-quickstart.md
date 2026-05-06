---
source: modelcontextprotocol.io
url: https://modelcontextprotocol.io/quickstart/server
title: "MCP Server Quickstart - Python & TypeScript SDK"
fetched: 2026-05-06
status: pending_ingest
---

# MCP Server 개발 가이드

## 3가지 서버 능력

> MCP servers can provide three main types of capabilities:
> 1. Resources: File-like data that can be read by clients (like API responses or file contents)
> 2. Tools: Functions that can be called by the LLM (with user approval)
> 3. Prompts: Pre-written templates that help users accomplish specific tasks

## Python SDK (FastMCP) 패턴

### 환경 세팅

```bash
# uv 설치
curl -LsSf https://astral.sh/uv/install.sh | sh

# 프로젝트 초기화
uv init weather
cd weather
uv venv
source .venv/bin/activate

# MCP SDK + httpx 설치
uv add "mcp[cli]" httpx
```

요구 버전: **Python 3.10+, MCP Python SDK 1.2.0+**

### FastMCP 서버 정의

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")
```

> The FastMCP class uses Python type hints and docstrings to automatically generate tool definitions, making it easy to create and maintain MCP tools.

핵심: type hints + docstring → 자동으로 JSON Schema 생성.

### Tool 정의 (@mcp.tool 데코레이터)

```python
@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    ...
```

### 서버 실행

```python
def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
```

### Logging 주의사항 (stdio)

> For STDIO-based servers: Never write to stdout. Writing to stdout will corrupt the JSON-RPC messages and break your server. The print() function writes to stdout by default, but can be used safely with file=sys.stderr.

```python
import sys
import logging

# Bad (STDIO)
print("Processing request")

# Good (STDIO)
print("Processing request", file=sys.stderr)

# Good (STDIO)
logging.info("Processing request")
```

HTTP transport는 stdout 안전.

## TypeScript SDK 패턴

### 환경 세팅

```bash
mkdir weather
cd weather
npm init -y
npm install @modelcontextprotocol/sdk zod@3
npm install -D @types/node typescript
```

### Logging 주의

> For STDIO-based servers: Never use console.log(), as it writes to standard output (stdout) by default. Writing to stdout will corrupt the JSON-RPC messages and break your server.

```javascript
// Bad (STDIO)
console.log("Server started");

// Good (STDIO)
console.error("Server started"); // stderr is safe
```

## Claude Desktop 연결 설정

`~/Library/Application Support/Claude/claude_desktop_config.json`:

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

Windows:
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

핵심:
- `mcpServers` 키 안에 서버 이름별 entry
- `command` + `args`는 stdio subprocess 실행 명령
- 절대 경로 사용 (Claude Desktop은 cwd가 다름)
- 변경 후 Claude Desktop 재시작 필요

## 핵심 인사이트

1. **FastMCP가 추천 패턴**: 데코레이터 + type hints로 boilerplate 최소화
2. **stdout 오염 = 즉사**: stdio transport에서 무심코 print 한 줄로 서버 중단
3. **Resources / Tools / Prompts 분리**: 같은 데코레이터 패턴 (`@mcp.resource`, `@mcp.prompt`)
4. **transport는 mcp.run() 인자**: `stdio` 기본, HTTP도 가능
5. **Claude Desktop은 subprocess launcher**: 다른 클라이언트도 유사 (Cursor, Claude Code 등)

## 참고

- 본 페이지: https://modelcontextprotocol.io/quickstart/server
- Python 예제: https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python
- TypeScript 예제: https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript
- Server 개념 (Resources/Tools/Prompts): https://modelcontextprotocol.io/docs/learn/server-concepts
