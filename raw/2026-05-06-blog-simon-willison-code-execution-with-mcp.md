---
source: blog
url: https://simonwillison.net/2025/Nov/4/code-execution-with-mcp/
title: "Code execution with MCP: Building more efficient agents"
author: Simon Willison (linkpost on Anthropic engineering article)
date: 2025-11-04
fetched: 2026-05-06
status: pending_ingest
tags: [mcp, code-execution, simon-willison, agent-efficiency, token-savings]
---

# Code execution with MCP (Simon Willison linkpost)

## 개요

Simon이 Anthropic의 새 엔지니어링 글 "Code execution with MCP"를 소개. 핵심 제안: **MCP 도구를 LLM이 코드로 wire 하는 방식**으로 효율화.

## MCP의 두 가지 핵심 문제

### 1. Context Token Overhead
> "Tool descriptions take up a lot of valuable real estate in the agent context even before you start using them."

MCP는 모든 도구 메타데이터를 세션 시작 시 로드 → 컨텍스트 윈도우 대량 점유.

### 2. Chaining Inefficiency
여러 MCP 도구를 연결하려면 응답을 LLM 컨텍스트로 통과시켜야 함:
- 추가 토큰 소비
- 에러 전파 가능성

## 제안: MCP Tools as Code Functions

도구 메타데이터를 컨텍스트로 전달하는 대신, **TypeScript 파일로 디스크에 저장**. 도구는 on-demand로 발견되어 0 토큰 소비.

### 함수 구조 예시
```typescript
interface GetDocumentInput {
  documentId: string;
}
interface GetDocumentResponse {
  content: string;
}
export async function getDocument(input: GetDocumentInput): 
Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>
  ('google_drive__get_document', input);
}
```

### Agent-Generated Code Chaining
에이전트가 코드를 생성해서 도구를 wire:

```typescript
const transcript = (await gdrive.getDocument({ 
  documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

## 핵심 이점

> "This avoids round-tripping the response from the gdrive call through the model"

→ 결과:
- 속도 향상
- 신뢰성 증가
- 토큰 절감
- 민감 데이터 노출 감소

## Simon의 평가

> "A sensible way to take advantage of the strengths of coding agents and address some of the major drawbacks of MCP as it is usually implemented today."

## 한계

Anthropic이 **구현 코드를 제공하지 않음** - 제안은 개념적 단계에 머무름.

## 메모

- 게시일: 2025년 11월 4일
- 원본 Anthropic 글: engineering/code-execution-with-mcp
- Simon은 이전부터 MCP 사용을 줄이고 CLI 도구 + Playwright Python 라이브러리를 선호한다고 언급
- Skills + MCP-as-code = Anthropic 측 에이전트 도구 사용 패러다임의 진화
