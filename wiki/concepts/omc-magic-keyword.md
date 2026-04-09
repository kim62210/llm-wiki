---
title: OMC Magic Keyword
aliases: ["OMC Magic Keyword", "매직 키워드", "Magic Keyword"]
category: concepts
page_type: project-internal
project: oh-my-claudecode
tags: [omc, keyword-detection, user-prompt, hook]
sources: [raw/2026-04-09-omc-HOOKS.md, raw/2026-04-09-omc-AGENTS.md, raw/2026-04-09-omc-ARCHITECTURE.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC Magic Keyword

> 자연어 입력에 특정 단어가 포함되면 해당 스킬/모드를 자동 활성화하는 OMC의 핵심 UX.

## 정의

**매직 키워드(Magic Keyword)**는 사용자 메시지에 포함된 특정 단어를 감지해, 해당 스킬을 슬래시 명령 없이도 자동 실행하는 메커니즘이다. OMC가 "Zero learning curve"를 달성하는 주 수단이다.

예시:
```
"autopilot build me a todo app"     → autopilot 스킬 활성
"ralph: refactor the auth module"   → ralph 스킬 활성
"ulw implement user auth"           → ultrawork 스킬 활성
"cancelomc"                         → cancel 스킬 활성
```

슬래시 명령은 여전히 사용 가능: `/oh-my-claudecode:autopilot ...`

## 동작 구조

매직 키워드 감지는 `keyword-detector` 훅이 `UserPromptSubmit` 이벤트에서 처리한다.

```
사용자 프롬프트 제출
    │
    ▼
UserPromptSubmit 이벤트 발생
    │
    ▼
keyword-detector.mjs 실행 (timeout 5s)
    │
    ├─ 1. 프롬프트 sanitize
    │     (코드블록, XML 태그, URL, 파일경로 제거 → false positive 방지)
    │
    ├─ 2. 키워드 패턴 매칭
    │
    ├─ 3. 우선순위 충돌 해소
    │
    └─ 4. `<system-reminder>`로 스킬 호출 지시 주입
```

출력은 `hookSpecificOutput.additionalContext`를 통해 Claude에게 전달된다:

```
[MAGIC KEYWORD: autopilot detected]
→ Read ~/.agents/skills/autopilot/SKILL.md and execute the autonomous pipeline
```

## 키워드 카탈로그

### 실행 모드 키워드 (스킬 호출 + 상태 파일 생성)

| 키워드 | 스킬 | 설명 |
|---|---|---|
| `cancelomc`, `stopomc` | cancel | 모든 활성 모드 취소 (최우선) |
| `ralph`, `don't stop`, `must complete`, `until done` | ralph | 검증 완료까지 지속 실행 |
| `autopilot`, `build me`, `I want a`, `handle it all`, `end to end`, `fullsend`, `e2e this` | autopilot | 완전 자율 실행 |
| `ultrawork`, `ulw`, `uw` | ultrawork | 최대 병렬 실행 |
| `ccg`, `claude-codex-gemini` | ccg | Claude+Codex+Gemini 삼중 자문 |
| `ralplan` | ralplan | 컨센서스 기반 반복 기획 |
| `deep interview`, `ouroboros` | deep-interview | Socratic 질문 인터뷰 |

### AI Slop Cleanup 키워드

두 가지 패턴:

**단독 활성**: `ai-slop`, `anti-slop`, `deslop`, `de-slop`

**조합 활성** (액션 키워드 + 스멜 키워드):
- 액션: `cleanup`, `refactor`, `simplify`, `dedupe`, `prune`
- 스멜: `slop`, `duplicate`, `dead code`, `unused code`, `over-abstraction`, `wrapper layers`, `needless abstractions`, `ai-generated`, `tech debt`

예: `"cleanup the duplicate code"` → ai-slop-cleaner 활성

### 에이전트 숏컷 키워드

슬래시 명령 없이 에이전트 모드 활성:

| 키워드 | 효과 |
|---|---|
| `tdd`, `test first`, `red green` | TDD 모드 (test-first 강제) |
| `code review`, `review code` | 종합 코드 리뷰 모드 |
| `security review`, `review security` | 보안 리뷰 모드 |

이들은 스킬을 호출하지 않고 **인라인 모드 메시지**만 주입한다.

### 추론 강화 키워드

| 키워드 | 효과 |
|---|---|
| `ultrathink`, `think hard`, `think deeply` | 확장 추론 모드 |
| `deepsearch`, `search the codebase`, `find in codebase` | 코드베이스 집중 검색 |
| `deepanalyze`, `deep-analyze` | 심층 분석 모드 |

## 우선순위 및 충돌 해소

여러 키워드가 동시에 매칭되면 다음 순서로 해소:

```
cancel  (배타적 최우선)
  → ralph
    → autopilot
      → ultrawork
        → ccg
          → ralplan
            → deep-interview
              → ai-slop-cleaner
                → tdd
                  → code-review
                    → security-review
                      → ultrathink
                        → deepsearch
                          → analyze
```

- `cancel`은 **배타적**: 다른 모든 매칭 무시
- 그 외는 공존 가능, 우선순위 순으로 처리

## 안전장치

- **Sanitization**: 코드블록·URL·파일경로 안의 키워드는 무시 → LLM에 코드 보여주다가 오발 방지
- **Team worker 보호**: `OMC_TEAM_WORKER` 환경변수 설정 시 비활성 (무한 spawning 방지)
- **Case insensitive**: 대소문자 구분 없음
- **가장 긴 매칭 우선**: 겹치는 패턴 중 specific한 것을 선택
- **명시 호출 우선**: `$name` 또는 `/name`이 있으면 키워드 감지 무시
- **비활성화**: `DISABLE_OMC=1` 또는 `OMC_SKIP_HOOKS=keyword-detector`

## 커스터마이징 가능 범위

`config.jsonc`의 `magicKeywords` 섹션에서 **4개 카테고리만** 커스터마이즈 가능:

```jsonc
{
  "magicKeywords": {
    "ultrawork": ["ultrawork", "ulw", "uw", "parallel"],
    "search": ["search", "find", "locate", "grep"],
    "analyze": ["analyze", "investigate", "examine"],
    "ultrathink": ["ultrathink", "think", "reason"]
  }
}
```

`autopilot`, `ralph`, `ccg`, `ralplan`, `deep-interview` 등은 **훅에 하드코딩**되어 있어 설정 파일로 변경 불가.

## Team 키워드는 제외된다

`team` 키워드는 자동 감지 **대상이 아니다**. 팀 모드 안에서 또 팀을 스폰하는 무한 재귀를 막기 위해 반드시 명시 슬래시 호출만 허용:

```bash
/oh-my-claudecode:team 3:executor "build a fullstack todo app"
```

## Ralph 특수 게이트

Ralph가 활성 상태일 때는 **ralplan-first** 게이트가 적용된다:
- `.omc/plans/prd-*.md`와 `.omc/plans/test-spec-*.md`가 모두 존재해야 구현 시작 허용
- 없으면 planning 단계에서 먼저 생성

## 관련 문서

- [[oh-my-claudecode (OMC)]]
- [[OMC Hook System]]
- [[OMC Execution Modes]]
- [[OMC Ralph Mode]]
- [[OMC Autopilot]]
