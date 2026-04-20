---
title: oh-my-claudecode (OMC)
aliases: [oh-my-claudecode, OMC, oh-my-claudecode (OMC)]
category: applications
page_type: entity
project: oh-my-claudecode
tags: [claude-code, multi-agent, orchestration, plugin, framework]
sources: [raw/2026-04-09-omc-README.md, raw/2026-04-09-omc-AGENTS.md, raw/2026-04-09-omc-ARCHITECTURE.md, raw/2026-04-09-omc-FEATURES.md, raw/2026-04-09-omc-HOOKS.md, raw/2026-04-09-omc-GETTING-STARTED.md, raw/2026-04-09-omc-REFERENCE.md, raw/2026-04-09-omc-CLAUDE.md]
created: 2026-04-09
updated: 2026-04-13
---
# oh-my-claudecode (OMC)

> **"Don't learn Claude Code. Just use OMC."**
> Claude Code용 멀티 에이전트 오케스트레이션 프레임워크. Zero learning curve.

## 개요

**oh-my-claudecode** (OMC)는 [Claude Code](https://docs.anthropic.com/claude-code) 위에서 동작하는 **멀티 에이전트 오케스트레이션 레이어**다. 사용자는 슬래시 명령을 외울 필요 없이 자연어로 작업을 요청하면, OMC가 적절한 전문 에이전트를 선정·위임·검증하는 전체 파이프라인을 자동 수행한다.

- **Creator**: Yeachan Heo ([@Yeachan-Heo](https://github.com/Yeachan-Heo))
- **Repository**: `github.com/Yeachan-Heo/oh-my-claudecode`
- **License**: MIT
- **npm 패키지명**: `oh-my-claude-sisyphus` (브랜드명과 다름)
- **Stars**: 26k+ (2026-04 기준)

## 왜 중요한가

Claude Code는 단일 에이전트 루프가 기본이다. 복잡한 작업(다중 파일 리팩터링, 아키텍처 설계, 병렬 처리, 장기 실행)은 수동으로 작업을 쪼개고 적절한 프롬프트를 공급해야 한다. OMC는 이 수고를 **자동 위임 + 검증 루프 + 상태 지속성**으로 해결한다.

핵심 가치:
- **Zero-config**: 설치 후 바로 사용. 기본값만으로 실전 투입 가능
- **자연어 인터페이스**: `autopilot`, `ralph`, `ulw` 같은 [[omc-magic-keyword]]가 포함된 메시지를 보내면 해당 모드가 자동 활성화
- **자동 병렬화**: 복잡한 작업을 최대 6개 동시 child agent로 분산
- **끈질긴 실행**: 검증될 때까지 멈추지 않음 (`persistent-mode` 훅이 Stop 이벤트를 가로채 재진입 유도)
- **비용 최적화**: Haiku/Sonnet/Opus 3-tier 모델 라우팅으로 30~50% 토큰 절감
- **경험 학습**: 세션에서 나온 문제 해결 패턴을 재사용 가능한 스킬로 자동 추출

## 4대 구성 요소

OMC는 네 개의 상호 연결된 시스템으로 구성된다.

```
User Input → Hooks (이벤트 감지) → Skills (행동 주입)
         → Agents (작업 실행) → State (진행 추적)
```

| 구성 요소 | 역할 | 수 |
|---|---|---|
| [[claude-code-hooks-system]] | Claude Code 라이프사이클 이벤트에 반응, 키워드 감지/검증/주입 | 20+ |
| [[agent-skills]] | 오케스트레이터 행동을 수정하는 주입 가능한 워크플로우 | 31+ |
| [[agentic-ai-foundation]] | 특정 역할(아키텍트·실행자·리뷰어 등)에 특화된 하위 에이전트 | 19 |
| [[omc-state-management]] | `.omc/` 디렉토리 기반 지속 상태 + 컴팩션 방지 메모 | - |

## 설치

OMC v4.x 이후 **Claude Code 플러그인 방식만 공식 지원**한다. npm/bun 직접 설치는 더 이상 권장되지 않음.

```bash
# 1. 마켓플레이스 등록
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode

# 2. 플러그인 설치
/plugin install oh-my-claudecode

# 3. 설정 (세션 내부 또는 터미널)
/setup
# 또는
omc setup
```

설정 후 진단:

```bash
/oh-my-claudecode:omc-doctor
```

## 실행 모드 한눈에 보기

| 모드 | 용도 | 링크 |
|---|---|---|
| **Team** (권장) | 5-stage 파이프라인으로 여러 Claude 에이전트 조율 | [[omc-team-mode]] |
| **Autopilot** | 아이디어→동작 코드 자동 완성 (5-phase) | [[omc-autopilot]] |
| **Ralph** | 검증 통과할 때까지 반복 | [[omc-ralph-mode]] |
| **Ultrawork** | 최대 병렬성 (non-team) | [[omc-ultrawork]] |
| **CCG** | Claude + Codex + Gemini 삼중 자문 | [[omc-ccg]] |
| **Ralplan** | Planner + Architect + Critic 컨센서스 기획 | [[omc-ralplan]] |
| **Deep Interview** | Socratic 질문으로 요구사항 정제 | [[omc-deep-interview]] |

전체 개요는 [[omc-execution-modes]] 참조.

## 에이전트 카탈로그

19개의 전문 에이전트가 4개 레인(Build/Analysis, Review, Domain, Coordination)으로 분류된다. 각 에이전트는 기본 모델 티어가 지정되어 있으며 [[omc-model-routing]] 규칙에 따라 자동 선택된다.

- 전체 목록: [[omc-agent-catalog]]
- 모델 라우팅 정책: [[omc-model-routing]]

## 주요 개념

- [[multi-agent-orchestration]] — 오케스트레이션 기본 원리
- [[omc-magic-keyword]] — 자연어 키워드 트리거 시스템
- [[omc-skill-layering]] — Guarantee/Enhancement/Execution 3-레이어 조합
- [[omc-hook-system]] — Claude Code 11개 라이프사이클 이벤트 + 20개 훅
- [[omc-state-management]] — Control Plane/Data Plane 분리와 컴팩션 생존 전략
- [[omc-delegation-categories]] — 태스크 → 모델 티어·temperature·thinking budget 매핑

## 인프라 요구사항

- Claude Code CLI
- Claude Max/Pro 구독 또는 `ANTHROPIC_API_KEY`
- **tmux** (team CLI, rate-limit 감지 기능용)
  - macOS: `brew install tmux`
  - Windows: WSL2 권장 또는 [psmux](https://github.com/marlocarlo/psmux)
- (선택) Gemini CLI, Codex CLI — 멀티 프로바이더 오케스트레이션

## 관련 프로젝트

- **oh-my-codex**: OMC의 OpenAI Codex CLI 버전
- **Inspired by**: oh-my-opencode, claude-hud, Superpowers, everything-claude-code, Ouroboros

## 관련 문서

- [[omc-agent-catalog]]
- [[omc-execution-modes]]
- [[omc-magic-keyword]]
- [[omc-hook-system]]
- [[omc-state-management]]
- [[omc-skill-layering]]
- [[omc-model-routing]]
- [[multi-agent-orchestration]]
- [[omc-mcp-tools|OMC MCP Tools]] — OMC 내부 MCP 도구군 스냅샷
