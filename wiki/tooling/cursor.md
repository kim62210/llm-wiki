---
title: Cursor AI IDE
category: tooling
page_type: entity
project: Cursor
tags: [cursor, ai-ide, coding-agent, composer, multi-file, vscode, fork, agentic-coding]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---
# Cursor AI IDE

Anysphere가 개발한 AI 우선(AI-first) 코드 에디터. VS Code를 포크하여 빌드되었으며, 다중 파일 인식 에이전트 모드(Composer/Agent)를 핵심 기능으로 제공한다. 단순한 코드 자동완성을 넘어 **코드베이스 전체를 컨텍스트로 삼아 자율적으로 파일을 생성·수정·실행하는 에이전트 IDE**를 지향한다.

## 개요

| 항목 | 내용 |
|---|---|
| 이름 | Cursor |
| 개발사 | Anysphere |
| 기반 | VS Code 포크 |
| 유료 플랜 | Pro ($20/월), Business ($40/유저/월) |
| 지원 모델 | Claude (Anthropic), GPT-4o (OpenAI), Gemini, 커스텀 |
| 최신 버전 | 3.x (2026년 4월 기준) |

## 주요 기능 개요

```mermaid
flowchart TD
    Cursor[Cursor IDE] --> Tab[Tab 자동완성\n다음 편집 예측]
    Cursor --> Chat[Chat\n인라인 코드 질문]
    Cursor --> Composer[Agent 모드\n다중 파일 자율 편집]
    Cursor --> Worktree[/worktree\n병렬 에이전트]
    Cursor --> CloudAgent[Cloud Agent\nVM 기반 원격 에이전트]

    Composer --> FileOp[파일 생성/수정/삭제]
    Composer --> Terminal[터미널 명령 실행]
    Composer --> Linter[린트/빌드 오류 자동 수정]
```

## Composer / Agent 모드

Cursor의 핵심 차별점. `Cmd+I`(macOS)로 Agent 모드를 열면 [[coding-agent|코딩 에이전트]]가 활성화된다.

- **코드베이스 전체 인식**: 대형 리포지토리에서도 관련 파일을 자동으로 컨텍스트에 포함
- **다중 파일 편집**: 단일 요청으로 여러 파일을 동시에 생성·수정
- **터미널 실행**: 빌드, 테스트, 패키지 설치 명령을 직접 실행하고 결과를 피드백으로 활용
- **자동 오류 수정**: 린터, 타입 오류, 빌드 실패를 에이전트가 자동으로 수정 시도

```
User: "User 인증 기능을 JWT 기반으로 구현해줘.
       - src/auth/ 디렉토리에 생성
       - 미들웨어, 컨트롤러, 서비스 레이어 분리
       - Jest 테스트 포함"

Agent:
  1. src/auth/auth.service.ts 생성
  2. src/auth/auth.controller.ts 생성
  3. src/auth/auth.middleware.ts 생성
  4. src/auth/__tests__/auth.service.test.ts 생성
  5. npm test 실행 → 실패 시 자동 수정
```

## @기호 컨텍스트 시스템

Cursor는 `@` 기호로 다양한 컨텍스트를 명시적으로 참조한다.

| 컨텍스트 | 설명 |
|---|---|
| `@파일명` | 특정 파일 참조 |
| `@폴더명` | 폴더 전체 참조 |
| `@코드베이스` | 전체 리포지토리 시맨틱 검색 |
| `@웹` | 실시간 웹 검색 결과 |
| `@문서` | 커스텀 문서 임베딩 |
| `@Git` | Git 히스토리, diff 참조 |
| `@터미널` | 마지막 터미널 출력 |

## Cursor Rules (.cursorrules)

프로젝트별 에이전트 행동 규칙을 정의하는 파일. [[claude-code|Claude Code]]의 `CLAUDE.md`와 유사한 역할이다.

```markdown
# .cursorrules 예시
- TypeScript strict mode 사용
- 함수형 컴포넌트 + hooks 패턴
- 모든 비동기 작업은 error boundary 포함
- 테스트 파일은 __tests__ 디렉토리에 위치
- 커밋 메시지는 conventional commits 형식
```

Cursor 0.45 이후 `.cursorrules`는 `.cursor/rules/*.mdc` 형식으로 마이그레이션 중이다.

## Cursor 3.0: 병렬 에이전트

Cursor 3.0(2026년 4월)에서 추가된 병렬 멀티에이전트 기능이다. 상세 내용은 [[cursor-cloud-agents-and-parallel-worktree-agents|Cursor Cloud Agents & Parallel Worktree Agents]] 참조.

```mermaid
flowchart LR
    User --> Cursor3[Cursor 3.0]
    Cursor3 --> Worktree1[Worktree 에이전트 1\n기능 A 브랜치]
    Cursor3 --> Worktree2[Worktree 에이전트 2\n기능 B 브랜치]
    Cursor3 --> CloudVM[Cloud Agent\n회사 네트워크 VM]
    Cursor3 --> BestOfN[/best-of-n\n동일 작업 병렬 실행\n최선 결과 선택]
```

## VS Code 대비 추가 기능

| 기능 | VS Code | Cursor |
|---|---|---|
| AI 자동완성 | GitHub Copilot(별도) | 내장 Tab |
| 에이전트 편집 | 없음 | Composer/Agent |
| 코드베이스 검색 | 텍스트 검색 | 시맨틱 + 텍스트 |
| 멀티파일 에이전트 | 없음 | 기본 기능 |
| 병렬 워크트리 에이전트 | 없음 | Cursor 3.0 |
| 확장 호환성 | VS Code 확장 전체 | VS Code 확장 대부분 |

## Cursor vs Claude Code

[[claude-code|Claude Code]]는 터미널 기반 CLI 에이전트인 반면, Cursor는 GUI 기반 에디터다.

- **Cursor**: 비주얼 편집, 실시간 인라인 diff, 파일 트리 탐색 선호하는 개발자
- **Claude Code**: 터미널 중심 워크플로우, 스크립트 자동화, 서버 환경
- **혼합 사용**: Cursor로 대화형 개발 + Claude Code로 배치 작업

## 실무 관점

Cursor는 **GUI 환경에서 코드베이스 전체를 에이전트가 인식하며 개발**하는 경험을 제공한다. VS Code 생태계와 호환되므로 기존 확장과 설정을 그대로 사용할 수 있다. 에이전트 모드는 반복적인 보일러플레이트 생성, 리팩토링, 버그 수정에서 생산성을 크게 높인다. 다만 에이전트가 예상치 못한 파일을 수정하거나 터미널 명령을 실행할 수 있으므로, 민감한 프로덕션 환경에서는 에이전트 실행 전 변경사항을 항상 검토해야 한다.

## 관련 문서

- [[coding-agent|코딩 에이전트]]
- [[claude-code|Claude Code]]
- [[cursor-cloud-agents-and-parallel-worktree-agents|Cursor Cloud Agents & Parallel Worktree Agents]]
- [[vibe-coding-platforms|Vibe Coding 플랫폼]]
