---
title: Aider (터미널 AI 페어 프로그래밍 도구)
category: tooling
page_type: entity
project: Aider
tags: [aider, coding-agent, terminal, git, pair-programming, cli, open-source, llm, repo-map, edit-format, udiff, architect-mode]
sources: [raw/2026-04-16-topic-queue-500.md, raw/2026-05-06-coding-harness-aider.md]
created: 2026-04-16
updated: 2026-05-06
---

# Aider

Paul Gauthier가 개발한 오픈소스 터미널 AI 페어 프로그래밍 도구. 터미널에서 LLM과 대화하며 코드를 편집하고, 변경 사항을 자동으로 Git에 커밋한다. VS Code 같은 IDE 없이 터미널과 텍스트 에디터만으로 AI 보조 개발을 가능하게 한다. SWE-bench 벤치마크에서 최고 수준의 성과를 지속적으로 기록하며 코딩 에이전트 분야의 기준 도구로 자리잡았다.

## 개요

| 항목 | 내용 |
|---|---|
| 이름 | Aider |
| 개발자 | Paul Gauthier |
| 라이선스 | Apache 2.0 |
| 저장소 | github.com/paul-gauthier/aider |
| 설치 | pip install aider-chat |
| 지원 모델 | Claude (Anthropic), GPT-4o (OpenAI), Gemini, 로컬 Ollama 등 |
| 운영 방식 | 터미널 REPL + Git 자동 커밋 |

## 핵심 워크플로우

```mermaid
flowchart TD
    Dev[개발자\n터미널에서 대화] --> Aider[Aider REPL]
    Aider --> Context[컨텍스트 구성\n관련 파일 자동 식별]
    Context --> LLM[LLM 호출\nClaude / GPT-4o 등]
    LLM --> Diff[편집 생성\nunified diff 또는 whole-file]
    Diff --> Apply[코드 변경 적용]
    Apply --> Git[Git 자동 커밋\n-m \"변경 내용 요약\"]
    Git --> Dev

    Apply --> Lint[린터/컴파일러 실행]
    Lint -- "오류 발생" --> LLM
```

## 설치와 시작

```bash
pip install aider-chat

# Claude 사용 (권장)
export ANTHROPIC_API_KEY=your-key
aider --model claude-sonnet-4-5

# OpenAI 사용
export OPENAI_API_KEY=your-key
aider --model gpt-4o

# 특정 파일과 함께 시작
aider src/auth.py tests/test_auth.py
```

## 주요 기능

### 리포지토리 맵 (Repo Map)

Aider의 핵심 기술 중 하나. 전체 코드베이스를 LLM 컨텍스트에 넣는 대신, 파일 간 의존성과 심볼 관계를 분석해 **현재 작업에 가장 관련 있는 코드 조각**만 동적으로 컨텍스트에 포함한다.

#### 알고리즘

> "analyzing the full repo map using a graph ranking algorithm, computed on a graph where each source file is a node and edges connect files which have dependencies."

(특정 알고리즘 이름은 docs 미명시. PageRank 변형으로 알려졌으나 [교차검증 필요])

#### Token budget

`--map-tokens` 기본 1k. "Aider adjusts the size of the repo map dynamically based on the state of the chat."

> "It will usually stay within that setting's value. But it does expand the repo map significantly at times, especially when no files have been added to the chat and aider needs to understand the entire repo as best as possible."

→ 사용자가 명시적으로 파일 추가 안 한 상황에서는 repo map을 확장해 전체 구조를 가능한 한 많이 노출.

#### 동작

```
repo map: 전체 리포지토리의 함수/클래스 시그니처 요약
         → 토큰 효율적이면서 전체 구조 파악 가능
```

### 인터랙티브 명령

```
# Aider REPL 내 명령어
/add src/new_feature.py      # 파일을 컨텍스트에 추가
/drop src/old_file.py        # 파일을 컨텍스트에서 제거
/ls                          # 현재 컨텍스트 파일 목록
/commit                      # 현재 변경사항 수동 커밋
/undo                        # 마지막 커밋 취소 (git reset)
/run pytest tests/           # 셸 명령 실행
/voice                       # 음성 입력 모드
```

### Git 자동 커밋

Aider는 모든 코드 변경 후 자동으로 Git 커밋을 생성한다. LLM이 커밋 메시지도 작성한다.

```bash
$ aider --model claude-sonnet-4-5 src/api.py

> JWT 기반 인증 미들웨어를 추가해줘

# Aider가 코드 변경 후 자동 실행:
# git add src/api.py
# git commit -m "feat: add JWT authentication middleware"
```

`--no-auto-commits` 옵션으로 자동 커밋을 끄고 수동 검토 후 커밋할 수 있다.

## Edit Format 6종 (공식 docs)

Aider는 모델 패밀리별 학습된 포맷 차이에 맞춰 6가지 edit format을 자동 선택한다.

| 포맷 | 동작 | 권장 모델 |
|---|---|---|
| `whole` | 전체 파일 fenced code block 반환 | 소규모 / 학습되지 않은 모델 |
| `diff` | SEARCH/REPLACE 블록 (`<<<<<<< SEARCH ... ======= ... >>>>>>> REPLACE`) | 중간 규모 |
| `diff-fenced` | 파일 경로를 fence 안쪽 | Gemini 패밀리 |
| `udiff` | Unified diff 변형 (line number 제거) | GPT-4 Turbo 패밀리 |
| `editor-diff` | architect mode 전용 diff 생성 | architect mode editor |
| `editor-whole` | architect mode 전용 whole 생성 | architect mode editor |

### Whole format

> "slow and costly because the LLM has to return the entire file"

### Diff (SEARCH/REPLACE)

```
mathweb/flask/app.py
<<<<<<< SEARCH
from flask import Flask
=======
import math
from flask import Flask
>>>>>>> REPLACE
```

### Udiff 혁신 (Aider의 핵심 기여)

> "GPT-4 Turbo family of models, because it reduced their lazy coding tendencies"

> "Aider tells GPT not to include line numbers, and just interprets each hunk from the unified diffs as a search and replace operation"

#### 4가지 설계 원칙

1. **FAMILIAR** — "Choose an edit format that GPT is already familiar with"
2. **SIMPLE** — "Choose a simple format that avoids escaping, syntactic overhead"
3. **HIGH LEVEL** — "Encourage GPT to structure edits as new versions of substantive code blocks"
4. **FLEXIBLE** — "Strive to be maximally flexible when interpreting GPT's edit instructions"

#### 메커니즘

> "With unified diffs, GPT acts more like it's writing textual data intended to be read by a program, not talking to a person. Diffs are usually consumed by the patch program, which is fairly rigid. This seems to encourage rigor, making GPT less likely to leave informal editing instructions."

#### 벤치마크 결과 (89개 python refactoring tasks)

| 모델 | SEARCH/REPLACE | Unified diff | 개선 |
|---|---|---|---|
| `gpt-4-1106-preview` | 20% (lazy 12개) | **61% (lazy 4개)** | 3배 |
| `gpt-4-0613` | 26% | **59%** | 2.3배 |

> "Aider's new unified diff editing format outperforms other solutions I evaluated by a wide margin."

#### Flexible patching 계층 (5단계)

1. Hunk 정규화: 의도된 버전 간 실제 unified diff 수행
2. Unmarked addition 발견: 원본 파일과 diff
3. "Relative leading white space"로 indentation 변동 처리
4. 큰 hunk를 overlap된 작은 hunk로 분할 후 독립 적용
5. Context window 크기 변동으로 localization

> "Experiments where flexible patching is disabled show a 9X increase in editing errors"

#### High-level diff 효과

> "Experiments without 'high level diff' prompting produce a 30-50% increase in editing errors, where diffs fail to apply or apply incorrectly and produce invalid code."

#### Folk remedy 검증 (반증)

> "It's worse to add a prompt that says the user is blind, has no hands, will tip $2000 and fears truncated code trauma. Widely circulated 'emotional appeal' folk remedies produced worse benchmark scores."

## Chat modes 4종

| Mode | Purpose | Model usage |
|---|---|---|
| **Code** (default) | 코드 변경 | 단일 main model |
| **Ask** | 토론, 질문 답변, 변경 X | 단일 main model |
| **Architect** | 2단계: 계획 → 편집 | architect + editor 두 모델 |
| **Help** | Aider 자체 사용법 | 단일 main model |

### Architect mode

```bash
# architect 모드: 강력한 모델이 계획, 경량 모델이 실행
aider --architect --model claude-opus-4-5 \
      --editor-model claude-sonnet-4-5
```

> "pairing an o1 architect with an editor model like GPT-4o or Sonnet will give the best results"

같은 모델을 architect와 editor 양쪽에 써도 OK. editor model의 edit format은 `--editor-edit-format`으로 별도 지정.

## Aider vs 경쟁 코딩 에이전트

| 항목 | Aider | [[claude-code|Claude Code]] | [[windsurf|Windsurf]] |
|---|---|---|---|
| 인터페이스 | 터미널 REPL | 터미널 CLI | GUI IDE |
| Git 통합 | 자동 커밋 내장 | Git 도구 사용 가능 | 내장 |
| 에디터 독립 | 완전 독립 | 완전 독립 | IDE 자체 |
| 멀티파일 편집 | 지원 | 지원 | 지원 |
| 오프라인/로컬 | Ollama로 가능 | 클라우드 API | 클라우드 API |
| 라이선스 | 오픈소스 | 유료 (Anthropic) | 유료 (Codeium) |
| SWE-bench 성과 | 최고 수준 | 높음 | [교차검증 필요] |

## .aider.conf.yml 설정

```yaml
# 프로젝트별 설정
model: claude-sonnet-4-5
auto-commits: true
auto-lint: true
lint-cmd: "ruff check --fix"
test-cmd: "pytest tests/ -x"
gitignore: true
```

## 실무 관점

Aider는 **터미널 중심 개발 워크플로우와 Git 자동 커밋을 원하는 개발자**에게 최적화되어 있다. IDE 없이 서버 환경에서도 동작하고, 오픈소스라 로컬 모델(Ollama)과 결합하면 API 비용 없이 운영할 수 있다. [[claude-code|Claude Code]]와 비교하면 Aider는 Git 통합이 더 강하고 다중 LLM 프로바이더를 지원하며, Claude Code는 파일 시스템 접근과 작업 범위 제어가 더 정교하다. 복잡한 GUI 인터페이스보다 키보드 중심 터미널 워크플로우를 선호하는 개발자에게 특히 생산성이 높다.

## FAQ technical details

### 컨텍스트 전달

> "It does this by analyzing your entire codebase in light of the current chat to build a compact repository map."

### 파일 추가 vs repo map

> "Adding a bunch of files that are mostly irrelevant to the task at hand will often distract or confuse the LLM."

→ 명시적 파일 추가는 수정 대상에 한정. 그 외는 repo map으로.

### Git 통합

> "Aider is tightly integrated with git so all of aider's code changes are committed to the repo with proper attribution."

### Conflict 처리

새 파일 추가가 필요해 사용자 승인되면 "it will re-submit the original request" — 원래 요청을 새로운 파일과 함께 재시도.

## 엔터프라이즈 / 프로덕션 관점

- **모델 무관성** — Claude/GPT/Gemini/Ollama 모두 지원. 모델별로 최적 edit format 자동 선택
- **Git-native** — 모든 변경이 commit으로 record → 감사 추적이 자연스럽게 수행
- **로컬 실행** — 별도 서버 / 클라우드 인프라 없음. 사용자 머신에서 동작
- **터미널 우선** — IDE 의존성 없어 SSH 환경, 컨테이너, CI에서도 활용 가능

## 관련 문서

- [[coding-agent|코딩 에이전트]] - AI 보조 개발 패턴과 도구 비교
- [[claude-code|Claude Code]] - Anthropic 공식 터미널 기반 코딩 에이전트
- [[windsurf|Windsurf]] - Cascade 에이전트 엔진을 탑재한 AI IDE
- [[swe-agent|SWE-agent]] - ACI 설계 원칙
- [[coding-harness-comparison|코딩 에이전트 하네스 횡단 비교]]
- [[parent-child-spawn-pattern|architect-editor 분업 패턴]]
