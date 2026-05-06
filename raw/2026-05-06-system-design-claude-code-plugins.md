---
source: code.claude.com
url: https://code.claude.com/docs/en/plugins
title: "Claude Code Plugins - Marketplace, plugin.json, Components"
fetched: 2026-05-06
status: pending_ingest
---

# Claude Code Plugins

## 출시 시점

- **2025-10**: Claude Code plugins 공개 베타
- **2026 현재**: 안정 단계, 마켓플레이스 다수

## Standalone vs Plugins

| 차원 | Standalone (`.claude/`) | Plugins |
|---|---|---|
| Skill 호출 | `/hello` | `/plugin-name:hello` |
| 적합 용도 | 개인/프로젝트 커스터마이징 | 팀/커뮤니티 공유, 버전 관리 |
| 분배 | 수동 복사 | marketplace로 install |
| 네임스페이스 | 없음 | plugin name으로 충돌 방지 |

## 디렉토리 구조

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # 매니페스트 (필수)
├── skills/                   # SKILL.md 디렉토리들
│   └── code-review/
│       └── SKILL.md
├── commands/                 # Flat Markdown 커맨드 (legacy)
├── agents/                   # 커스텀 서브에이전트
├── hooks/
│   └── hooks.json            # 이벤트 핸들러
├── .mcp.json                 # MCP 서버 번들
├── .lsp.json                 # LSP 서버 (코드 인텔리전스)
├── monitors/
│   └── monitors.json         # 백그라운드 모니터
├── bin/                      # 실행파일 (PATH 추가)
└── settings.json             # 기본 설정
```

> Common mistake: Don't put commands/, agents/, skills/, or hooks/ inside the .claude-plugin/ directory. Only plugin.json goes inside .claude-plugin/.

## plugin.json 매니페스트

```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

| 필드 | 용도 |
|---|---|
| `name` | 고유 식별자, skill namespace |
| `description` | 플러그인 매니저 표시 |
| `version` | 옵션. 미설정 시 git commit SHA가 버전 |
| `author` | 옵션 |

추가 필드: `homepage`, `repository`, `license`

## Skill 정의 (Plugin 안)

```yaml
---
description: Reviews code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage
```

호출: `/my-plugin:code-review`

> Run /reload-plugins to load the Skills

`$ARGUMENTS` placeholder로 사용자 입력 받기:
```markdown
---
description: Greet the user with a personalized message
---

Greet the user named "$ARGUMENTS" warmly...
```

## MCP Server Bundling (`.mcp.json`)

```json
{
  "mcpServers": {
    "database-tools": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": { "DB_URL": "${DB_URL}" }
    }
  }
}
```

또는 inline in `plugin.json`:
```json
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```

특수 변수:
- `${CLAUDE_PLUGIN_ROOT}`: 플러그인 디렉토리 절대경로
- `${CLAUDE_PLUGIN_DATA}`: 영구 상태 (업데이트 후 유지)

## LSP Server (`.lsp.json`)

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

## Background Monitors (`monitors/monitors.json`)

```json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]
```

각 stdout 라인이 알림으로 Claude에 전달.

## Hooks (`hooks/hooks.json`)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npm run lint:fix"
          }
        ]
      }
    ]
  }
}
```

stdin으로 hook input JSON 수신.

## 설정 (`settings.json`)

```json
{
  "agent": "security-reviewer"
}
```

지원 키: `agent`, `subagentStatusLine`

## 개발 워크플로우

```bash
# 로컬 테스트 (인스톨 없이)
claude --plugin-dir ./my-plugin

# 여러 플러그인 동시 로드
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two

# 변경 후 재로드 (재시작 없이)
/reload-plugins
```

> When a --plugin-dir plugin has the same name as an installed marketplace plugin, the local copy takes precedence for that session.

## Marketplace 분배

> Once your plugin is in a marketplace, others can install it using the instructions in Discover and install plugins. To keep a plugin internal to your team, host the marketplace in a private repository.

공식 마켓플레이스 제출:
- claude.ai: https://claude.ai/settings/plugins/submit
- Console: https://platform.claude.com/plugins/submit

## 커뮤니티 마켓플레이스 (2025-2026 생태계)

핵심 통계 (2026-05 시점):
- 4,200+ skills
- 770+ MCP servers
- 2,500+ marketplaces
- 120,000+ monthly visitors

### 주요 마켓플레이스/디렉토리

| 이름 | 특징 |
|---|---|
| claudemarketplaces.com | Skills/MCP/Marketplace 종합 디렉토리 |
| awesome-skills.com | Curated skills 모음 |
| tonsofskills.com (claude-code-plugins) | 340개+ 패키지, ccpi CLI 패키지 매니저 |
| awesome-claude-code-toolkit (rohitg00) | 135 agents, 35 skills (+400K via SkillKit), 42 commands, 176+ plugins |
| awesome-claude-plugins (ComposioHQ) | Curated plugins list |
| awesome-claude-plugins (Chat2AnyLLM) | Curated marketplaces |
| skillsmp.com | Multi-agent (Claude/Codex/ChatGPT) skills marketplace |

### oh-my-claudecode 사례

> oh-my-claudecode is a multi-AI orchestration plugin for Claude Code that coordinates Claude, Gemini, and Codex with 19 specialized agents, 36 skills, and MCP-powered tools.

설치 경로:
- Claude Code plugin marketplace
- npm package 직접
- 사이트: yeachan-heo.github.io/oh-my-claudecode-website/

## 마이그레이션 (`.claude/` → plugin)

```bash
mkdir -p my-plugin/.claude-plugin
# manifest 작성
# 기존 파일 복사
cp -r .claude/commands my-plugin/
cp -r .claude/agents my-plugin/
cp -r .claude/skills my-plugin/
# hooks: settings.json의 hooks 객체를 hooks/hooks.json으로 옮김
# 테스트
claude --plugin-dir ./my-plugin
```

## Plugin이 통합하는 컴포넌트 카탈로그

| 컴포넌트 | 정의 위치 | 호출 방식 |
|---|---|---|
| Skill | `skills/<name>/SKILL.md` | `/plugin:skill` 또는 모델 자동 invocation |
| Subagent | `agents/<name>.md` | `/agents` 메뉴 |
| Hook | `hooks/hooks.json` | 이벤트 (PostToolUse 등) |
| MCP server | `.mcp.json` 또는 inline | tool calls |
| LSP server | `.lsp.json` | 코드 인텔리전스 자동 |
| Monitor | `monitors/monitors.json` | 백그라운드 stdout 알림 |
| Bin | `bin/` | PATH에 자동 추가 |
| Settings | `settings.json` | 기본 agent / statusline |

## 핵심 인사이트

1. **Plugin = "skills + agents + hooks + MCP" 번들**: 단일 단위로 설치/삭제
2. **Namespace 강제**: `/plugin-name:skill-name` 형식 - 충돌 방지가 첫째 가치
3. **Marketplace 생태계 폭발적 성장**: 2025 후반-2026에 수천 개 플러그인
4. **Migration friendly**: `.claude/` 표준 구조와 동일 → 그대로 복사
5. **Versioning**: 명시적 `version` 미설정 시 git commit SHA = 매 커밋이 새 버전
6. **Local development**: `--plugin-dir`로 인스톨 없이 테스트
7. **MCP 통합 자연스러움**: plugin이 MCP server 번들 → install 시 자동 시작

## 참고

- Plugins 가이드: https://code.claude.com/docs/en/plugins
- Plugins reference: https://code.claude.com/docs/en/plugins-reference
- Discover & install: https://code.claude.com/docs/en/discover-plugins
- Plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- 공식 마켓플레이스: https://claude.ai/settings/plugins/submit
