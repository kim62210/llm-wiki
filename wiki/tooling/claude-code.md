---
title: Claude Code
aliases: ["Claude Code"]
category: tooling
page_type: entity
project: Claude Code
tags: [claude-code, anthropic, coding-agent, cli]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Claude Code

Anthropic이 제공하는 공식 [[coding agent]]. Simon Willison이 [[agentic engineering guide]] 전반에 걸쳐 가장 많이 레퍼런스하는 도구다.

## 개요

Claude Code는 Claude 모델(대표적으로 Opus 4.6, Sonnet 4.6 등)을 감싼 [[how coding agents work|에이전트 하네스]]. 코드 읽기/쓰기/실행 능력을 갖춘다.

## 배포 형태

Simon Willison의 가이드와 CLI 환경에서 언급되는 형태:

- **Terminal CLI**: 기본 개발자 워크플로우
- **Desktop 앱** (Mac/Windows)
- **Web 앱** (claude.ai/code, "Claude Code for web")
- **IDE 확장** (VS Code, JetBrains)

Simon은 [[linear walkthroughs]] 사례에서 "Claude Code for web"을 GitHub 저장소 분석에 활용했다.

## Simon의 사용 사례

가이드에 등장하는 대표 활용:

| 사례 | 기법 | 참조 |
|------|------|------|
| SwiftUI 슬라이드 앱 Present를 vibe coded | 즉석 생성 | [[linear walkthroughs]] |
| GIF 최적화 도구 (Gifsicle→WASM) | 긴 시행착오 컴파일 | [[gif optimization case study]] |
| Word cloud Rust CLI + 애니메이션 설명 | 비동기 연구 + Opus 4.6 | [[interactive explanations]] |
| 디프 뷰 문자 단위 강조 | Explore subagent | [[subagents]] |

## 주요 기능

가이드에서 암시되거나 명시되는 특징:

### 1. Explore Subagent (기본 패턴)
새 저장소에서 작업 시작 시 자동으로 Explore 서브에이전트를 발사해 코드베이스를 매핑. 부모 에이전트의 컨텍스트 창을 보존. 자세한 것은 [[subagents]] 참조.

### 2. 병렬 서브에이전트
여러 서브에이전트를 동시에 실행 가능. 독립 파일 편집, 대량 탐색, 병렬 리팩토링에 유리.

### 3. 브라우저 자동화 통합
`uvx rodney --help`, `uvx showboat --help` 같은 외부 CLI를 자동 설치·활용 가능. [[agentic manual testing]] 참조.

### 4. Git 통합
"Use git bisect to find when this bug was introduced"처럼 자연어 Git 지시를 이해. [[git with coding agents]] 참조.

### 5. 리즈닝 모델 활용
Opus 4.6 같은 reasoning-enabled 모델로 복잡한 디버깅에 유리.

## 효과적 사용 패턴

Simon이 권장하는 세션 시작 패턴:

```
1. First run the tests
2. Use red/green TDD
3. Use subagents where independent work can parallelize
4. Use rodney/playwright for browser testing
5. Write a walkthrough with showboat when done
```

## 대체제

가이드에 언급된 다른 [[coding agent|코딩 에이전트]]들:
- OpenAI Codex (비동기 작업에 유리)
- Gemini CLI
- Gemini Jules (비동기 리팩토링 워커)

## 관련 문서

- [[coding agent]]
- [[how coding agents work]]
- [[subagents]]
- [[first run the tests]]
- [[red-green TDD]]
- [[agentic manual testing]]
- [[git with coding agents]]
- [[agentic engineering guide]]
