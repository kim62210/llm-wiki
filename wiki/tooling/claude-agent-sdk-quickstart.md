---
title: Claude Agent SDK Quickstart
category: tooling
page_type: summary
tags: [tooling, summary, claude-[[coding-agent|agent]]-sdk, quickstart, onboarding]
sources: [raw/recursive-sources/2026-04-10-sdk-mcp/claude-agent-sdk-quickstart.md]
created: 2026-04-10
updated: 2026-04-13
---
# Claude Agent SDK Quickstart

Claude Agent SDK의 quickstart 문서 요약이다. SDK를 처음 연결할 때 어떤 순서로 개념과 실행 흐름을 이해해야 하는지에 초점을 맞춘다.

## 핵심 내용

- SDK를 시작하는 최소 단계와 초기 실행 흐름을 설명한다.
- overview보다 더 실전적인 시작 지점이다.
- 세션 / 입력 / agent loop를 실제 코드로 붙이는 첫 단계 역할을 한다.

## 왜 중요한가

개념 overview만으로는 시작이 어렵다. quickstart는 입문자가 실제로 손을 움직이게 만드는 문서라는 점에서 가치가 있다.

## 실무 적용 관점

새 도구를 팀에 도입할 때 가장 중요한 것은 “첫 성공 경험”이다. quickstart는 그 역할을 하는 문서다.

## 원문이 다루는 흐름

원문은 대체로 `Prerequisites` → `Setup` → `Create a buggy file` → `Build an agent that finds and fixes bugs` → `Run your agent` 순서로 전개된다. 따라서 `Claude Agent SDK Quickstart` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: Prerequisites, Setup, Create a buggy file, Build an agent that finds and fixes bugs, Run your agent
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## source 메모

- **Claude Agent SDK Quickstart** — snapshot: `raw/recursive-sources/2026-04-10-sdk-mcp/claude-agent-sdk-quickstart.md` · source: https://code.claude.com/docs/en/agent-sdk/quickstart · 볼 섹션: Prerequisites, Setup, Create a buggy file, Build an agent that finds and fixes bugs

## quickstart가 가르치는 최소 객체

| 객체 | quickstart에서 맡는 역할 | 왜 중요하나 |
|---|---|---|
| `prompt` | 에이전트에게 수행 목표를 준다 | SDK는 도구를 제공하지만, 실제 작업 분해는 프롬프트 품질에 크게 좌우된다 |
| `query` | agentic loop를 시작하고 메시지 스트림을 돌려준다 | 단발 completion API가 아니라 **turn-based agent loop**를 직접 다루는 진입점이다 |
| `allowedTools` | `Read`, `Edit`, `Glob` 등 승인된 행위를 제한한다 | 빠른 성공 경험과 안전한 권한 경계를 동시에 잡아준다 |
| `permissionMode` | `acceptEdits` 같은 모드로 승인 정책을 정한다 | headless 자동화와 human-in-the-loop 사이의 운영 모델을 결정한다 |

## 추천 읽기 순서

1. 이 quickstart로 **첫 성공 경험**을 만든다.
2. 바로 [[claude-agent-loop|How the Agent Loop Works]]로 넘어가 메시지 유형과 turn 개념을 이해한다.
3. 그다음 [[claude-agent-sessions|Claude Agent SDK Sessions]]에서 multi-turn continuity를 본다.
4. 마지막으로 MCP/permissions/hooks 문서로 확장하면, quickstart 예제가 실제 제품 하네스로 이어진다.

## 관련 문서

- [[claude-agent-sdk-overview|Claude Agent SDK Overview]]
- [[claude-agent-sdk|Claude Agent SDK]]
- [[claude-agent-sdk-typescript|Claude Agent SDK TypeScript]]
