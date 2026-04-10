---
title: Claude Agent SDK Quickstart
source_url: https://code.claude.com/docs/en/agent-sdk/quickstart
fetched_via: r.jina.ai
fetched: 2026-04-10
---

# Claude Agent SDK Quickstart

Title: Quickstart - Claude Code Docs

URL Source: https://code.claude.com/docs/en/agent-sdk/quickstart

Markdown Content:
Use the Agent SDK to build an AI agent that reads your code, finds bugs, and fixes them, all without manual intervention.**What you’ll do:**

1.   Set up a project with the Agent SDK
2.   Create a file with some buggy code
3.   Run an agent that finds and fixes the bugs automatically

## Prerequisites

*   **Node.js 18+** or **Python 3.10+**
*   An **Anthropic account** ([sign up here](https://platform.claude.com/))

## Setup

1

2

3

## Create a buggy file

This quickstart walks you through building an agent that can find and fix bugs in code. First, you need a file with some intentional bugs for the agent to fix. Create `utils.py` in the `my-agent` directory and paste the following code:

```
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def get_user_name(user):
    return user["name"].upper()
```

This code has two bugs:

1.   `calculate_average([])` crashes with division by zero
2.   `get_user_name(None)` crashes with a TypeError

## Build an agent that finds and fixes bugs

Create `agent.py` if you’re using the Python SDK, or `agent.ts` for TypeScript:

This code has three main parts:

1.   **`query`**: the main entry point that creates the agentic loop. It returns an async iterator, so you use `async for` to stream messages as Claude works. See the full API in the [Python](https://code.claude.com/docs/en/agent-sdk/python#query) or [TypeScript](https://code.claude.com/docs/en/agent-sdk/typescript#query) SDK reference.
2.   **`prompt`**: what you want Claude to do. Claude figures out which tools to use based on the task.
3.   **`options`**: configuration for the agent. This example uses `allowedTools` to pre-approve `Read`, `Edit`, and `Glob`, and `permissionMode: "acceptEdits"` to auto-approve file changes. Other options include `systemPrompt`, `mcpServers`, and more. See all options for [Python](https://code.claude.com/docs/en/agent-sdk/python#claude-agent-options) or [TypeScript](https://code.claude.com/docs/en/agent-sdk/typescript#options).

The `async for` loop keeps running as Claude thinks, calls tools, observes results, and decides what to do next. Each iteration yields a message: Claude’s reasoning, a tool call, a tool result, or the final outcome. The SDK handles the orchestration (tool execution, context management, retries) so you just consume the stream. The loop ends when Claude finishes the task or hits an error.The message handling inside the loop filters for human-readable output. Without filtering, you’d see raw message objects including system initialization and internal state, which is useful for debugging but noisy otherwise.

### Run your agent

Your agent is ready. Run it with the following command:

*   Python

*   TypeScript

```
python3 agent.py
```

```
npx tsx agent.ts
```

After running, check `utils.py`. You’ll see defensive code handling empty lists and null users. Your agent autonomously:

1.   **Read**`utils.py` to understand the code
2.   **Analyzed** the logic and identified edge cases that would crash
3.   **Edited** the file to add proper error handling

This is what makes the Agent SDK different: Claude executes tools directly instead of asking you to implement them.

### Try other prompts

Now that your agent is set up, try some different prompts:

*   `"Add docstrings to all functions in utils.py"`
*   `"Add type hints to all functions in utils.py"`
*   `"Create a README.md documenting the functions in utils.py"`

### Customize your agent

You can modify your agent’s behavior by changing the options. Here are a few examples:**Add web search capability:**

**Give Claude a custom system prompt:**

**Run commands in the terminal:**

With `Bash` enabled, try: `"Write unit tests for utils.py, run them, and fix any failures"`

## Key concepts

**Tools** control what your agent can do:

| Tools | What the agent can do |
| --- | --- |
| `Read`, `Glob`, `Grep` | Read-only analysis |
| `Read`, `Edit`, `Glob` | Analyze and modify code |
| `Read`, `Edit`, `Bash`, `Glob`, `Grep` | Full automation |

**Permission modes** control how much human oversight you want:

| Mode | Behavior | Use case |
| --- | --- | --- |
| `acceptEdits` | Auto-approves file edits and common filesystem commands, asks for other actions | Trusted development workflows |
| `dontAsk` | Denies anything not in `allowedTools` | Locked-down headless agents |
| `auto` (TypeScript only) | A model classifier approves or denies each tool call | Autonomous agents with safety guardrails |
| `bypassPermissions` | Runs every tool without prompts | Sandboxed CI, fully trusted environments |
| `default` | Requires a `canUseTool` callback to handle approval | Custom approval flows |

The example above uses `acceptEdits` mode, which auto-approves file operations so the agent can run without interactive prompts. If you want to prompt users for approval, use `default` mode and provide a [`canUseTool` callback](https://code.claude.com/docs/en/agent-sdk/user-input) that collects user input. For more control, see [Permissions](https://code.claude.com/docs/en/agent-sdk/permissions).

## Next steps

Now that you’ve created your first agent, learn how to extend its capabilities and tailor it to your use case:

*   **[Permissions](https://code.claude.com/docs/en/agent-sdk/permissions)**: control what your agent can do and when it needs approval
*   **[Hooks](https://code.claude.com/docs/en/agent-sdk/hooks)**: run custom code before or after tool calls
*   **[Sessions](https://code.claude.com/docs/en/agent-sdk/sessions)**: build multi-turn agents that maintain context
*   **[MCP servers](https://code.claude.com/docs/en/agent-sdk/mcp)**: connect to databases, browsers, APIs, and other external systems
*   **[Hosting](https://code.claude.com/docs/en/agent-sdk/hosting)**: deploy agents to Docker, cloud, and CI/CD
*   **[Example agents](https://github.com/anthropics/claude-agent-sdk-demos)**: see complete examples: email assistant, research agent, and more

