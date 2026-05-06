---
source: claude-code-official-docs
url: https://code.claude.com/docs/en/slash-commands
title: Slash Command System - Claude Code Skills (SKILL.md 표준)
fetched: 2026-05-06
status: pending_ingest
---

# Slash Command System / Skills

Claude Code의 slash command는 2026년에 **Skills** 라는 통합 명칭으로 재구성되었다. `.claude/commands/` legacy 형식과 `.claude/skills/<name>/SKILL.md` 신형식이 공존하지만, **양방향 invocation (사용자/모델)** 과 **dynamic context injection (`!command` 백틱)** 이 핵심 차별점이다. AgentSkills.io 오픈 표준을 채택.

## 1. Skill 핵심 개념

> "A skill is a markdown file with instructions that Claude loads into its context — either when you invoke it directly with /skill-name or automatically when it detects the skill is relevant to your task."

> "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way."

### 디렉토리 구조
```
my-skill/
├── SKILL.md           # 메인 instructions (필수)
├── template.md        # 템플릿
├── examples/sample.md # 예시 출력
└── scripts/validate.sh # 실행 스크립트
```

## 2. 저장 위치 (우선순위)

| Location | Path | Scope |
|----------|------|-------|
| Enterprise | managed settings | 조직 전체 |
| Personal | `~/.claude/skills/<name>/SKILL.md` | 모든 프로젝트 |
| Project | `.claude/skills/<name>/SKILL.md` | 해당 프로젝트만 |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | 플러그인 활성 시 |

> "Enterprise overrides personal, and personal overrides project. Plugin skills use a `plugin-name:skill-name` namespace, so they cannot conflict with other levels."

### Plugin namespace
플러그인 skill은 `plugin-name:skill-name` 형태로 호출하여 충돌 회피. 예: `/codex:rescue`, `/discord:access`.

### Live change detection
`~/.claude/skills/`, project `.claude/skills/`, `--add-dir` 디렉토리 내 변경을 세션 중 자동 감지. 새 디렉토리 생성은 재시작 필요.

### Monorepo: nested discovery
`packages/frontend/` 작업 시 `packages/frontend/.claude/skills/` 도 자동 감지.

## 3. Frontmatter Reference

```yaml
---
name: my-skill
description: What this skill does
disable-model-invocation: true
allowed-tools: Read Grep
---
```

| Field | Required | 설명 |
|-------|----------|------|
| `name` | No | 슬래시 커맨드명 (생략 시 디렉토리명, 영소문자/숫자/하이픈, 64자 max) |
| `description` | Recommended | 모델이 자동 invoke 결정에 사용. **첫 1,536자만** skill listing에 표시 |
| `when_to_use` | No | trigger phrase 추가 (description에 append) |
| `argument-hint` | No | 자동완성 힌트 (`[issue-number]`) |
| `arguments` | No | named positional arguments |
| `disable-model-invocation` | No | true 시 사용자만 invoke 가능 (`/commit`, `/deploy`) |
| `user-invocable` | No | false 시 Claude만 invoke (background knowledge) |
| `allowed-tools` | No | 이 skill 활성 시 권한 자동 grant |
| `model` | No | 임시 모델 override (turn 단위) |
| `effort` | No | `low|medium|high|xhigh|max` |
| `context` | No | `fork` 시 forked subagent에서 실행 |
| `agent` | No | `context: fork` 시 사용할 agent type |
| `hooks` | No | skill 라이프사이클 전용 hooks |
| `paths` | No | glob 패턴 매칭 시에만 자동 invoke |
| `shell` | No | `bash`(default) or `powershell` |

## 4. String Substitutions

| Variable | 설명 |
|----------|------|
| `$ARGUMENTS` | 전체 argument string (명령어 뒤 모든 텍스트) |
| `$ARGUMENTS[N]` | 0-based index 접근 |
| `$N` | `$ARGUMENTS[N]` 의 shorthand |
| `$<name>` | frontmatter `arguments` 에 선언된 named arg |
| `${CLAUDE_SESSION_ID}` | 세션 ID |
| `${CLAUDE_EFFORT}` | 현재 effort 레벨 |
| `${CLAUDE_SKILL_DIR}` | 이 SKILL.md 디렉토리 절대경로 |

> "Indexed arguments use shell-style quoting, so wrap multi-word values in quotes."

`/my-skill "hello world" second` → `$0` = `hello world`, `$1` = `second`

## 5. Dynamic Context Injection

### 인라인 명령
```yaml
---
name: summarize-changes
description: Summarizes uncommitted changes
---

## Current changes

!`git diff HEAD`

## Instructions
Summarize the changes above...
```

> "The `!`<command>`` syntax runs shell commands before the skill content is sent to Claude. The command output replaces the placeholder, so Claude receives actual data, not the command itself."

### 멀티라인 fenced block
````markdown
## Environment
```!
node --version
npm --version
git status --short
```
````

### 정책으로 비활성화
`"disableSkillShellExecution": true` 설정 시 모든 shell 실행이 `[shell command execution disabled by policy]` 로 대체. 단 bundled/managed skill은 영향 안 받음.

## 6. Invocation 제어 매트릭스

| Frontmatter | 사용자 invoke | Claude invoke | Description in context |
|-------------|--------------|---------------|------------------------|
| (default) | Yes | Yes | Always |
| `disable-model-invocation: true` | Yes | No | Not in context (전체 skill만 사용자 invoke 시 로드) |
| `user-invocable: false` | No | Yes | Always |

### Description 캐릭터 budget
- 모든 skill 이름은 항상 포함
- description은 동적 budget (context window의 1%, fallback 8,000 chars)
- 각 entry는 1,536자 cap
- `SLASH_COMMAND_TOOL_CHAR_BUDGET` 환경변수로 조정

## 7. Skill Content Lifecycle

> "When you or Claude invoke a skill, the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session. Claude Code does not re-read the skill file on later turns."

### Auto-compaction 동작
> "Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens. Claude Code fills this budget starting from the most recently invoked skill, so older skills can be dropped entirely after compaction."

- 가장 최근 invocation만 재첨부
- 각 skill 5K 토큰 보존
- 25K 토큰 공동 budget
- 최근 invoke 부터 채움 → 오래된 것은 drop

## 8. context: fork 패턴 (Subagent 위임)

```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:
1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

| 접근법 | System prompt | Task | Also loads |
|--------|---------------|------|------------|
| Skill `context: fork` | agent type (Explore/Plan) | SKILL.md 본문 | CLAUDE.md |
| Subagent `skills:` field | subagent body | delegation message | preloaded skills + CLAUDE.md |

## 9. Permission 통합

### `allowed-tools`
```yaml
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)
```
> "Grants permission for the listed tools while the skill is active. It does not restrict which tools are available."

### Skill 차단
```text
# permissions deny rules:
Skill                  # 모든 skill 차단
Skill(commit)          # 정확히 commit만 허용
Skill(review-pr *)     # prefix 매치 허용
```

## 10. SKILL.md 작성 모범 사례

### Reference content (지식 type)
```yaml
---
name: api-conventions
description: API design patterns for this codebase
---

When writing API endpoints:
- Use RESTful naming conventions
- Return consistent error formats
```

### Task content (행동 type)
```yaml
---
name: deploy
description: Deploy to production
context: fork
disable-model-invocation: true
---

Deploy:
1. Run tests
2. Build
3. Push
4. Verify
```

> "Keep the body itself concise. Once a skill loads, its content stays in context across turns, so every line is a recurring token cost."
> "Keep SKILL.md under 500 lines. Move detailed reference material to separate files."

## 11. AgentSkills.io 오픈 표준

> "Claude Code skills follow the AgentSkills open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection."

표준 핵심:
- SKILL.md + frontmatter
- `description` 기반 자동 라우팅
- 디렉토리 packaging

Claude Code 확장:
- `disable-model-invocation`
- `context: fork`
- `!command` injection

## 12. Mermaid: Skill Lifecycle

```mermaid
flowchart TD
    User[User: /skill-name args] --> Resolve[Resolve skill from precedence]
    Resolve --> Inject[Inject !command outputs]
    Inject --> Sub[Substitute $ARGUMENTS, $N, ${VAR}]
    Sub --> Decide{context: fork?}
    Decide -->|No| Inline[Inline 메시지로 대화에 추가]
    Decide -->|Yes| Spawn[Subagent spawn with agent type]
    Inline --> Conv[Stay in context across turns]
    Spawn --> Result[Subagent result returns to parent]
    Conv -->|Auto-compact| Reattach[최근 invocation 5K tokens 재첨부]
```

## 13. 엔터프라이즈 적용 관점

### Skill을 만들 시점
> "Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than a fact."

### 보안 모델
- Project skill은 git 트래킹되어 review 대상이어야 함
- `allowed-tools` 는 trust dialog 후 적용
- `disableSkillShellExecution: true` 로 organization 단위 차단 가능
- Plugin skill의 namespace는 conflict 방지

### 분배 채널
- **Project skills**: `.claude/skills/` git 커밋
- **Plugins**: `skills/` 디렉토리 포함
- **Managed**: 조직 단위 settings 배포

### Anti-pattern
- description을 너무 짧게 → 자동 invoke 안 됨
- description에 키워드 부족 → 모델이 다른 방향으로 진행
- SKILL.md 500줄 초과 → context 비용 누적
- description 작성 시 1,536자 cap 무시 → 끝부분 잘림

## 관련 문서 후보 (ingest 시)
- `wiki/agents/slash-commands-skills` (concept)
- `wiki/agents/agent-skills-standard` (entity, AgentSkills.io)
- `wiki/agents/dynamic-context-injection` (concept)
