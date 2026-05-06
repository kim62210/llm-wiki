---
source: anthropic.com + platform.claude.com
url: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
title: "Anthropic Agent Skills - Open Standard, Packaging, Distribution"
fetched: 2026-05-06
status: pending_ingest
---

# Anthropic Agent Skills

## 출시 타임라인

- **2025-10-16**: 최초 발표 (Equipping agents for the real world with Agent Skills)
- **2025-12-18**: Open Standard으로 spec 공개 + 엔터프라이즈 기능 + OpenAI Codex CLI/ChatGPT가 동일 포맷 채택

## Skill 정의

> Agent Skills are organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks.

> Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

비유: "an onboarding guide for a new hire" (신입사원에게 주는 온보딩 가이드).

## SKILL.md 포맷

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

# PDF Processing
## Quick start
...
```

### Frontmatter 필수 필드

| 필드 | 제한 |
|---|---|
| `name` | 최대 64자, lowercase letters/numbers/hyphens, "anthropic"/"claude" 금지, XML 태그 금지 |
| `description` | non-empty, 최대 1024자, XML 태그 금지 |

> The description should include both what the Skill does and when Claude should use it.

## Progressive Disclosure - 3-Level 로딩

| Level | 로딩 시점 | 토큰 비용 | 내용 |
|---|---|---|---|
| Level 1: Metadata | 항상 (startup) | ~100 토큰/skill | YAML frontmatter (name, description) |
| Level 2: Instructions | Skill 트리거될 때 | < 5K 토큰 | SKILL.md 본문 |
| Level 3+: Resources | 필요 시 | 사실상 무제한 | 번들된 파일, bash로 실행 |

> Progressive disclosure ensures only relevant content occupies the context window at any given time.

### Level 3 예시 구조

```
pdf-skill/
├── SKILL.md (main instructions)
├── FORMS.md (form-filling guide)
├── REFERENCE.md (detailed API reference)
└── scripts/
    └── fill_form.py (utility script)
```

> When instructions mention executable scripts, Claude runs them via bash and receives only the output (the script code itself never enters context).

## 디스커버리 메커니즘

> At startup, the agent pre-loads the name and description of every installed skill into its system prompt.

> When a Skill is triggered, Claude uses bash to read SKILL.md from the filesystem, bringing its instructions into the context window. If those instructions reference other files (like FORMS.md or a database schema), Claude reads those files too using additional bash commands.

흐름:
1. Startup: `name` + `description` 메타가 system prompt에 주입
2. User request: "Extract the text from this PDF and summarize it"
3. Claude invokes: `bash: read pdf-skill/SKILL.md` → Instructions 로드
4. Claude determines: Form filling 불필요 → FORMS.md 미로드
5. Claude executes: SKILL.md 지시에 따라 task 수행

핵심: Claude는 **bash로 파일을 읽음** (특수 도구 없이) → 일반 파일시스템 모델.

## 배포 모델 (Surface별)

### Claude API
- Pre-built (`pptx`, `xlsx`, `docx`, `pdf`) + Custom 모두 지원
- `skill_id`를 `container` 파라미터에 명시
- 필요 beta 헤더:
  - `code-execution-2025-08-25`
  - `skills-2025-10-02`
  - `files-api-2025-04-14`
- Workspace-wide 공유

### Claude Code
- Custom Skills만 지원
- 필터 베이스 (filesystem-based, API 업로드 불필요)
- 두 위치:
  - Personal: `~/.claude/skills/`
  - Project: `.claude/skills/`
- Plugin marketplace로 공유 가능

### Claude.ai
- Pre-built + Custom 모두 지원
- Custom: Settings > Features에서 zip 업로드
- Pro/Max/Team/Enterprise plan에서 code execution 활성화 시
- **Individual user only** (조직 공유 안 됨)

## Cross-Surface 제약

> Custom Skills do not sync across surfaces:
> - Skills uploaded to Claude.ai must be separately uploaded to the API
> - Skills uploaded via the API are not available on Claude.ai
> - Claude Code Skills are filesystem-based and separate from both Claude.ai and API

| Surface | 공유 범위 |
|---|---|
| Claude.ai | Individual user only |
| Claude API | Workspace-wide |
| Claude Code | Personal (`~/.claude/skills/`) 또는 project (`.claude/skills/`), Plugins로 확장 가능 |

## Runtime 제약

| Surface | 네트워크 | 패키지 설치 |
|---|---|---|
| Claude.ai | varying (사용자/관리자 설정) | pre-installed only |
| Claude API | None | pre-installed only |
| Claude Code | Full (사용자 머신과 동일) | local install 권장 (global 비권장) |

## Pre-built Agent Skills (Anthropic 공식)

- `pptx`: PowerPoint
- `xlsx`: Excel
- `docx`: Word
- `pdf`: PDF
- Open-source: `claude-api` (8개 언어 SDK 레퍼런스)

오픈소스 레포: https://github.com/anthropics/skills

## Open Standard (2025-12-18)

> Anthropic released its Agent Skills specification as an open standard, expanding the ability for Claude users to create, deploy, share and discover new skills for agentic AI.

> OpenAI adopted the same format for Codex CLI and ChatGPT (December 2025).

엔터프라이즈 추가 기능 (Team / Enterprise plan):
- Organization-wide skill 관리
- Workspace-wide deployment
- 자동 업데이트
- 중앙 관리 (admin)
- Partner skills (Canva, Notion, Figma, Atlassian)

## 보안 고려사항

> We strongly recommend using Skills only from trusted sources.

> If you must use a Skill from an untrusted or unknown source, exercise extreme caution and thoroughly audit it before use. Depending on what access Claude has when executing the Skill, malicious Skills could lead to data exfiltration, unauthorized system access, or other security risks.

핵심 위험:
- **Audit thoroughly**: SKILL.md, scripts, images, 모든 번들 파일 검토
- **External sources are risky**: 외부 URL fetch가 위험 (의존성 변경 가능)
- **Tool misuse**: file ops, bash, code execution을 악용
- **Data exposure**: 민감 데이터 외부 유출
- **Treat like installing software**

## Skills vs MCP vs Plugins 비교

| 차원 | Agent Skills | MCP Server | Claude Code Plugin |
|---|---|---|---|
| 단위 | 디렉토리 (SKILL.md + 리소스) | 서버 프로세스/HTTP | 플러그인 디렉토리 (.claude-plugin/plugin.json) |
| 디스커버리 | system prompt에 metadata | tools/list, prompts/list | manifest |
| 실행 | Claude가 bash로 파일 read + script 실행 | JSON-RPC tool call | skill/agent/hook/MCP 묶음 |
| 토큰 효율 | progressive disclosure | tool description은 항상 로드 | progressive (skill 내부) |
| 배포 | filesystem / zip / API skill_id | binary / npm / docker / HTTP URL | plugin marketplace |
| 신뢰 모델 | 설치 시 신뢰 결정 | tools/list 어노테이션 untrusted | marketplace + 명시적 install |

## 핵심 인사이트

1. **Filesystem-native**: Claude는 특수 API 없이 bash로 SKILL.md를 read - 표준 도구 활용
2. **Progressive disclosure가 핵심**: 100토큰/skill로 수십 개 설치 가능, 본문은 트리거 시에만
3. **Skills는 procedural, MCP는 functional**: skill = 워크플로우/노하우, MCP = 도구/데이터 접근
4. **Open Standard로 확산**: OpenAI도 동일 포맷 채택 (2025-12)
5. **신뢰 모델은 software install과 동일**: code execution + filesystem access를 받음
6. **Surface 간 미동기화**: surface별로 별도 관리 (Claude.ai / API / Claude Code)

## 참고

- Anthropic 엔지니어링 블로그: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Skills cookbook: https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction
- Open-source Skills 레포: https://github.com/anthropics/skills
- Complete Guide PDF: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
