# Gemini CLI Subagents

Source: https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/
Fetched: 2026-04-16

## What Subagents Are

Subagents function as "specialized, expert agents that operate alongside your primary Gemini CLI session." They handle delegated tasks while maintaining isolated execution environments, preventing context pollution in the main agent's workflow.

## Architectural Design

**Isolation Model:**
Each subagent operates within its own ecosystem featuring:
- Separate context windows
- Custom system instructions
- Curated tool sets
- Independent MCP server access

The orchestration model treats the primary agent as a "strategic orchestrator" that delegates sub-tasks to relevant specialists. Subagent execution--potentially involving dozens of tool calls or test runs--collapses into single consolidated responses returned to the main agent.

## Configuration and Usage

**Definition Format:**
Subagents use Markdown files with YAML frontmatter, deployable at:
- Personal level: `~/.gemini/agents`
- Project level: `.gemini/agents`
- Extension bundles: `agents/` directory

**Invocation Syntax:**
Users employ the `@agent` notation: `"@frontend-specialist Can you review our app?"`

The `/agents` command displays all configured subagents.

## Built-in Subagents

Google provides three default options:
- **generalist:** Universal task handler with full tool access
- **cli_help:** Gemini CLI documentation specialist
- **codebase_investigator:** Architectural mapping and bug analysis expert

## Parallel Execution

The system supports simultaneous subagent deployment through explicit requests like "Run the frontend-specialist on each package in parallel," reducing total completion time for multi-component tasks. However, parallel execution risks code conflicts during simultaneous edits and accelerates usage limit consumption.

## Notable Limitations

"multiple agents editing code at the same time can lead to conflicts and agents overwriting one another."
