# OpenHarness

Source: https://github.com/HKUDS/OpenHarness
Fetched: 2026-04-16

## Overview

OpenHarness is an open-source Python framework providing "core lightweight agent infrastructure: tool-use, skills, memory, and multi-agent coordination." The framework transforms LLMs into functional agents by supplying the execution layer--"hands, eyes, memory, and safety boundaries."

Alongside the core framework exists **ohmo**, a personal AI assistant built on OpenHarness that operates across communication platforms (Feishu, Slack, Telegram, Discord).

## 10-Subsystem Architecture

- **Engine**: Agent loop handling query streaming and tool-call cycles
- **Tools Registry**: 43+ integrated tools spanning file I/O, shell commands, web search, MCP
- **Skills System**: On-demand knowledge loading via Markdown files
- **Plugins**: Extensions including commands, hooks, and agents
- **Permissions**: Multi-level safety modes with path-level and command rules
- **Hooks**: PreToolUse/PostToolUse lifecycle events
- **Commands**: 54 built-in commands for workflow management
- **MCP Integration**: Model Context Protocol client support
- **Memory**: Persistent cross-session knowledge storage (CLAUDE.md discovery, MEMORY.md)
- **Coordinator**: Multi-agent spawning and team management

## Agent Loop Pattern

```
while True:
    response = await api.stream(messages, tools)
    if response.stop_reason != "tool_use":
        break
    for tool_call in response.tool_uses:
        result = await harness.execute_tool(tool_call)
    messages.append(tool_results)
```

## Permission Modes

| Mode | Behavior |
|------|----------|
| Default | Interactive approval for writes/execution |
| Auto | Allow everything (sandboxed environments) |
| Plan Mode | Block all writes (review-first workflows) |

## Provider Support

**Anthropic-Compatible**: Claude, Moonshot/Kimi, Zhipu/GLM, MiniMax
**OpenAI-Compatible**: OpenAI, OpenRouter, DeepSeek, SiliconFlow, GitHub Models, Groq, Ollama
**Subscription Bridges**: Claude CLI, Codex CLI, GitHub Copilot (OAuth)

## Skills Compatibility

Compatible with anthropics/skills markdown format. Stored in `~/.openharness/skills/`.

## Testing

114 unit+integration tests, 6 CLI E2E tests, 9 harness feature tests, 3 React TUI E2E tests, 12 real skills+plugins tests.

## License

MIT
