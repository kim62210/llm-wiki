---
title: Playwright MCP (브라우저 자동화 MCP 서버)
category: tooling
page_type: entity
project: Playwright MCP
tags: [playwright, mcp, browser-automation, testing, accessibility-tree, microsoft]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Playwright MCP

Microsoft가 개발한 [[model-context-protocol|MCP]] 서버로, LLM이 웹 브라우저와 직접 상호작용할 수 있게 한다. 스크린샷이나 비전 모델 없이 브라우저의 접근성 트리(accessibility tree)를 활용하여 구조화된 방식으로 웹 페이지를 탐색하고 조작한다.

## 개요

Playwright MCP는 2025년 3월에 공개되었으며, [[browser-automation-agents|브라우저 자동화 에이전트]] 생태계에서 핵심 인프라로 자리잡았다. 기존 브라우저 자동화가 픽셀 기반 시각 입력이나 수동 스크립트에 의존했다면, Playwright MCP는 웹 페이지의 접근성 스냅샷이라는 구조화된 텍스트 표현을 사용한다. 이 접근은 비전 모델을 필요로 하지 않아 토큰 효율적이며, 결정론적(deterministic)인 제어가 가능하다.

위키의 깨진 wikilink 3회 참조로 확인된 고빈도 참조 엔티티다.

## 핵심 아키텍처

### 접근성 트리 기반 상호작용

웹 페이지의 DOM을 시각적으로 캡처하는 대신, 브라우저의 접근성 API가 제공하는 트리 구조를 활용한다. 이 트리에는 버튼, 링크, 입력 필드, 텍스트 등 인터랙티브 요소가 구조화된 형태로 포함되어 있어, LLM이 페이지 구조를 정확히 이해하고 조작할 수 있다.

### MCP 프로토콜 통합

[[model-context-protocol|MCP(Model Context Protocol)]] 표준을 따르며, stdio 기반 통신과 SSE(Server-Sent Events) 전송을 지원한다. CDP(Chrome DevTools Protocol) 엔드포인트에 직접 연결하는 것도 가능하다.

### 3가지 운영 모드

| 모드 | 설명 | 적합한 상황 |
|------|------|------------|
| 지속형 프로필 | 로그인 정보가 유지되는 영구 브라우저 프로필 | 인증이 필요한 반복 작업 |
| 격리 모드 | 각 세션이 독립적인 임시 컨텍스트 | 테스트, 보안이 중요한 작업 |
| 브라우저 확장 | 기존 실행 중인 브라우저 탭에 연결 | 디버깅, 기존 세션 활용 |

## 설치 및 설정

### 기본 설정

MCP 클라이언트(Claude Desktop, VS Code, Cursor 등)의 설정에 추가:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

### 주요 설정 옵션

| 옵션 | 설명 |
|------|------|
| `--browser` | Chrome, Firefox, WebKit 중 브라우저 선택 |
| `--headless` | 헤드리스 모드(UI 없이) 실행 |
| `--isolated` | 격리된 세션 모드 |
| `--user-data-dir` | 영구 프로필 저장 경로 |
| `--storage-state` | 초기 쿠키/로컬 스토리지 로드 |
| `--allowed-origins` | 허용 출처 제한 |

요구 사항: Node.js 18 이상.

## 제공 도구 (Tools)

Playwright MCP 서버가 LLM에 노출하는 주요 도구 카테고리:

- **네비게이션**: 페이지 이동, URL 접근, 뒤로/앞으로
- **상호작용**: 클릭, 텍스트 입력, 폼 제출, 드래그
- **접근성 스냅샷**: 페이지의 구조화된 표현 캡처
- **콘솔/네트워크 로그**: JavaScript 콘솔 메시지, 네트워크 요청 수집
- **코드 생성**: 수행한 작업을 TypeScript Playwright 스크립트로 변환
- **PDF 생성**: 페이지를 PDF로 출력

## 사용 사례

### E2E 테스트 자동화

LLM이 자연어로 기술된 테스트 시나리오를 접근성 트리 기반으로 실행한다. 셀렉터 변경에 강건한 "자가 복구(self-healing)" 테스트가 가능하다.

### 탐색적 자동화

에이전트가 웹 애플리케이션을 자율적으로 탐색하면서 기능을 검증하거나 데이터를 수집한다. 영구적 브라우저 상태 유지가 필요한 장기 실행 워크플로우에 적합하다.

### 폼 자동화 및 웹 스크래핑

복잡한 멀티스텝 폼 작성, 인증이 필요한 사이트 접근, 구조화된 데이터 추출 등에 활용된다.

## CLI vs MCP: 2026년 권장 사항

2026년 Microsoft는 코딩 에이전트용으로 Playwright CLI를 MCP보다 권장하고 있다. CLI 방식은 세션당 약 27,000 토큰을 소비하는 반면, MCP는 약 114,000 토큰을 소비하여 약 4배의 차이가 있다.

| 방식 | 토큰 효율 | 상태 유지 | 적합한 상황 |
|------|----------|----------|------------|
| CLI + Skills | 높음 (약 27K 토큰/세션) | 제한적 | 코딩 에이전트, 단발성 작업 |
| MCP 서버 | 낮음 (약 114K 토큰/세션) | 영구적 | 탐색적 자동화, 장기 워크플로우 |

단, MCP는 영구 상태 유지, 풍부한 인트로스펙션, 페이지 구조에 대한 반복 추론이 필요한 시나리오에서 여전히 가치가 있다.

## 지원 클라이언트

VS Code, Cursor, Claude Desktop, Windsurf, Cline, Cherry Studio 등 20개 이상의 MCP 호환 클라이언트를 지원한다.

## 관련 페이지

- [[model-context-protocol|MCP]] -- Playwright MCP가 구현하는 프로토콜
- [[browser-automation-agents|Browser Automation Agents]] -- 브라우저 자동화 도구 전체 개요
- [[claude-code|Claude Code]] -- MCP 서버를 활용하는 코딩 에이전트
- [[mcp-architecture|MCP 아키텍처]] -- MCP 서버/클라이언트 구조 상세
