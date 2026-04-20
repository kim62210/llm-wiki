---
title: Aider (터미널 AI 페어 프로그래밍 도구)
category: tooling
page_type: entity
project: Aider
tags: [aider, coding-agent, terminal, git, pair-programming, cli, open-source, llm]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
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

## 편집 모드

| 모드 | 설명 | 적합 상황 |
|---|---|---|
| `whole` | 전체 파일 재출력 | 소규모 파일 |
| `diff` | unified diff 형식 | 중간 규모 파일 |
| `udiff` | 컨텍스트 포함 diff | 기본값, 대부분의 상황 |
| `architect` | 계획 → 실행 2단계 | 복잡한 구조적 변경 |

```bash
# architect 모드: 강력한 모델이 계획, 경량 모델이 실행
aider --architect --model claude-opus-4-5 \
      --editor-model claude-sonnet-4-5
```

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

## 관련 문서

- [[coding-agent|코딩 에이전트]] - AI 보조 개발 패턴과 도구 비교
- [[claude-code|Claude Code]] - Anthropic 공식 터미널 기반 코딩 에이전트
- [[windsurf|Windsurf]] - Cascade 에이전트 엔진을 탑재한 AI IDE
