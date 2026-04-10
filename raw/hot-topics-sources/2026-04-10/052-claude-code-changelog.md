---
title: Changelog - Claude Code Docs
source_url: https://code.claude.com/docs/en/changelog
final_url: https://code.claude.com/docs/en/changelog
status: 200
content_type: text/html; charset=utf-8
topics: [Claude Code Hooks System, Agent Skills (SKILL.md) Standard, Git Worktree Isolation for Parallel Coding Agents, Firecracker/microVM Sandboxes for Agent Code Execution]
sections: [Harness Engineering]
fetched_at: 2026-04-10T01:43:32.670544+00:00
---

# Changelog - Claude Code Docs

## 원본 URL

https://code.claude.com/docs/en/changelog

## 추출 본문

Changelog - Claude Code Docs

Skip to main content

Claude Code Docs home page

English

Search...

⌘KAsk AI

Claude Developer Platform

Claude Code on the Web

Claude Code on the Web

Search...

Navigation

Getting started

Changelog

Getting started

Build with Claude Code

Deployment

Administration

Configuration

Reference

Agent SDK

What's New

Resources

Getting started

Overview

Quickstart

Changelog

Core concepts

How Claude Code works

Extend Claude Code

Explore the .claude directory

Explore the context window

Use Claude Code

Store instructions and memories

Permission modes

Common workflows

Best practices

Platforms and integrations

Overview

Remote Control

Claude Code on the web

Claude Code on desktop

Chrome extension (beta)

Computer use (preview)

Visual Studio Code

JetBrains IDEs

Code review & CI/CD

Claude Code in Slack

On this page

2.1.98

2.1.97

2.1.96

2.1.94

2.1.92

2.1.91

2.1.90

2.1.89

2.1.87

2.1.86

2.1.85

2.1.84

2.1.83

2.1.81

2.1.80

2.1.79

2.1.78

2.1.77

2.1.76

2.1.75

2.1.74

2.1.73

2.1.72

2.1.71

2.1.70

2.1.69

2.1.68

2.1.66

2.1.63

2.1.62

2.1.61

2.1.59

2.1.58

2.1.56

2.1.55

2.1.53

2.1.52

2.1.51

2.1.50

2.1.49

2.1.47

2.1.46

2.1.45

2.1.44

2.1.43

2.1.42

2.1.41

2.1.39

2.1.38

2.1.37

2.1.36

2.1.34

2.1.33

2.1.32

2.1.31

2.1.30

2.1.29

2.1.27

2.1.25

2.1.23

2.1.22

2.1.21

2.1.20

2.1.19

2.1.18

2.1.17

2.1.16

2.1.15

2.1.14

2.1.12

2.1.11

2.1.10

2.1.9

2.1.7

2.1.6

2.1.5

2.1.4

2.1.3

2.1.2

2.1.0

2.0.76

2.0.75

2.0.74

2.0.73

2.0.72

2.0.71

2.0.70

2.0.69

2.0.68

2.0.67

2.0.65

2.0.64

2.0.62

2.0.61

2.0.60

2.0.59

2.0.58

2.0.57

2.0.56

2.0.55

2.0.54

2.0.52

2.0.51

2.0.50

2.0.49

2.0.47

2.0.46

2.0.45

2.0.43

2.0.42

2.0.41

2.0.37

2.0.36

2.0.35

2.0.34

2.0.33

2.0.32

2.0.31

2.0.30

2.0.28

2.0.27

2.0.25

2.0.24

2.0.22

2.0.21

2.0.20

2.0.19

2.0.17

2.0.15

2.0.14

2.0.13

2.0.12

2.0.11

2.0.10

2.0.9

2.0.8

2.0.5

2.0.1

2.0.0

1.0.126

1.0.124

1.0.123

1.0.120

1.0.119

1.0.117

1.0.115

1.0.113

1.0.112

1.0.111

1.0.110

1.0.109

1.0.106

1.0.97

1.0.94

1.0.93

1.0.90

1.0.88

1.0.86

1.0.85

1.0.84

1.0.83

1.0.82

1.0.81

1.0.80

1.0.77

1.0.73

1.0.72

1.0.71

1.0.70

1.0.69

1.0.68

1.0.65

1.0.64

1.0.63

1.0.62

1.0.61

1.0.60

1.0.59

1.0.58

1.0.57

1.0.56

1.0.55

1.0.54

1.0.53

1.0.52

1.0.51

1.0.48

1.0.45

1.0.44

1.0.43

1.0.42

1.0.41

1.0.40

1.0.39

1.0.38

1.0.37

1.0.36

1.0.35

1.0.34

1.0.33

1.0.32

1.0.31

1.0.30

1.0.29

1.0.28

1.0.27

1.0.25

1.0.24

1.0.23

1.0.22

1.0.21

1.0.18

1.0.17

1.0.11

1.0.10

1.0.8

1.0.7

1.0.6

1.0.4

1.0.1

1.0.0

0.2.125

0.2.117

0.2.108

0.2.107

0.2.106

0.2.105

0.2.102

0.2.100

0.2.98

0.2.96

0.2.93

0.2.82

0.2.75

0.2.74

0.2.72

0.2.70

0.2.69

0.2.67

0.2.66

0.2.63

0.2.61

0.2.59

0.2.54

0.2.53

0.2.50

0.2.49

0.2.47

0.2.44

0.2.41

0.2.37

0.2.36

0.2.34

0.2.32

0.2.31

0.2.30

0.2.26

0.2.21

Getting started

Changelog

Copy page

Release notes for Claude Code, including new features, improvements, and bug fixes by version.

Copy page

This page is generated from the CHANGELOG.md on GitHub.Run 
claude --version
 to check your installed version.

​

2.1.98

April 9, 2026

Added interactive Google Vertex AI setup wizard accessible from the login screen when selecting “3rd-party platform”, guiding you through GCP authentication, project and region configuration, credential verification, and model pinning

Added 
CLAUDE_CODE_PERFORCE_MODE
 env var: when set, Edit/Write/NotebookEdit fail on read-only files with a 
p4 edit
 hint instead of silently overwriting them

Added Monitor tool for streaming events from background scripts

Added subprocess sandboxing with PID namespace isolation on Linux when 
CLAUDE_CODE_SUBPROCESS_ENV_SCRUB
 is set, and 
CLAUDE_CODE_SCRIPT_CAPS
 env var to limit per-session script invocations

Added 
--exclude-dynamic-system-prompt-sections
 flag to print mode for improved cross-user prompt caching

Added 
workspace.git_worktree
 to the status line JSON input, set whenever the current directory is inside a linked git worktree

Added W3C 
TRACEPARENT
 env var to Bash tool subprocesses when OTEL tracing is enabled, so child-process spans correctly parent to Claude Code’s trace tree

LSP: Claude Code now identifies itself to language servers via 
clientInfo
 in the initialize request

Fixed a Bash tool permission bypass where a backslash-escaped flag could be auto-allowed as read-only and lead to arbitrary code execution

Fixed compound Bash commands bypassing forced permission prompts for safety checks and explicit ask rules in auto and bypass-permissions modes

Fixed read-only commands with env-var prefixes not prompting unless the var is known-safe (
LANG
, 
TZ
, 
NO_COLOR
, etc.)

Fixed redirects to 
/dev/tcp/...
 or 
/dev/udp/...
 not prompting instead of auto-allowing

Fixed stalled streaming responses timing out instead of falling back to non-streaming mode

Fixed 429 retries burning all attempts in ~13s when the server returns a small 
Retry-After
 — exponential backoff now applies as a minimum

Fixed MCP OAuth 
oauth.authServerMetadataUrl
 config override not being honored on token refresh after restart, affecting ADFS and similar IdPs

Fixed capital letters being dropped to lowercase on xterm and VS Code integrated terminal when the kitty keyboard protocol is active

Fixed macOS text replacements deleting the trigger word instead of inserting the substitution

Fixed 
--dangerously-skip-permissions
 being silently downgraded to accept-edits mode after approving a write to a protected path via Bash

Fixed managed-settings allow rules remaining active after an admin removed them, until process restart

Fixed 
permissions.additionalDirectories
 changes not applying mid-session — removed directories lose access immediately and added ones work without restart

Fixed removing a directory from 
additionalDirectories
 revoking access to the same directory passed via 
--add-dir

Fixed 
Bash(cmd:*)
 and 
Bash(git commit *)
 wildcard permission rules failing to match commands with extra spaces or tabs

Fixed 
Bash(...)
 deny rules being downgraded to a prompt for piped commands that mix 
cd
 with other segments

Fixed false Bash permission prompts for 
cut -d /
, 
paste -d /
, 
column -s /
, 
awk '{print $1}' file
, and filenames containing 
%

Fixed permission rules with names matching JavaScript prototype properties (e.g. 
toString
) causing 
settings.json
 to be silently ignored

Fixed agent team members not inheriting the leader’s permission mode when using 
--dangerously-skip-permissions

Fixed a crash in fullscreen mode when hovering over MCP tool results

Fixed copying wrapped URLs in fullscreen mode inserting spaces at line breaks

Fixed file-edit diffs disappearing from the UI on 
--resume
 when the edited file was larger than 10KB

Fixed several 
/resume
 picker issues: 
--resume <name>
 opening uneditable, filter reload wiping search state, empty list swallowing arrow keys, cross-project staleness, and transient task-status text replacing conversation summaries

Fixed 
/export
 not honoring absolute paths and 
~
, and silently rewriting user-supplied extensions to 
.txt

Fixed 
/effort max
 being denied for unknown or future model IDs

Fixed slash command picker breaking when a plugin’s frontmatter 
name
 is a YAML boolean keyword

Fixed rate-limit upsell text being hidden after message remounts

Fixed MCP tools with 
_meta["anthropic/maxResultSizeChars"]
 not bypassing the token-based persist layer

Fixed voice mode leaking dozens of space characters into the input when re-holding the push-to-talk key while the previous transcript is still processing

Fixed 
DISABLE_AUTOUPDATER
 not fully suppressing the npm registry version check and symlink modification on npm-based installs

Fixed a memory leak where Remote Control permission handler entries were retained for the lifetime of the session

Fixed background subagents that fail with an error not reporting partial progress to the parent agent

Fixed prompt-type Stop/SubagentStop hooks failing on long sessions, and hook evaluator API errors showing “JSON validation failed” instead of the real message

Fixed feedback survey rendering when dismissed

Fixed Bash 
grep -f FILE
 / 
rg -f FILE
 not prompting when reading a pattern file outside the working directory

Fixed stale subagent worktree cleanup removing worktrees that contain untracked files

Fixed 
sandbox.network.allowMachLookup
 not taking effect on macOS

Improved 
/resume
 filter hint labels and added project/worktree/branch names in the filter indicator

Improved footer indicators (Focus, notifications) to stay on the mode-indicator row instead of wrapping at narrow terminal widths

Improved 
/agents
 with a tabbed layout: a Running tab shows live subagents, and the Library tab adds Run agent and View running instance actions

Improved 
/reload-plugins
 to pick up plugin-provided skills without requiring a restart

Improved Accept Edits mode to auto-approve filesystem commands prefixed with safe env vars or process wrappers

Improved Vim mode: 
j
/
k
 in NORMAL mode now navigate history and select the footer pill at the input boundary

Improved hook errors in the transcript to include the first line of stderr for self-diagnosis without 
--debug

Improved OTEL tracing: interaction spans now correctly wrap full turns under concurrent SDK calls, and headless turns end spans per-turn

Improved transcript entries to carry final token usage instead of streaming placeholders

Updated the 
/claude-api
 skill to cover Managed Agents alongside Claude API

[VSCode] Fixed false-positive “requires git-bash” error on Windows when 
CLAUDE_CODE_GIT_BASH_PATH
 is set or Git is installed at a default location

Fixed 
CLAUDE_CODE_MAX_CONTEXT_TOKENS
 to honor 
DISABLE_COMPACT
 when it is set.

Dropped 
/compact
 hints when 
DISABLE_COMPACT
 is set.

​

2.1.97

April 8, 2026

Added focus view toggle (
Ctrl+O
) in 
NO_FLICKER
 mode showing prompt, one-line tool summary with edit diffstats, and final response

Added 
refreshInterval
 status line setting to re-run the status line command every N seconds

Added 
workspace.git_worktree
 to the status line JSON input, set when the current directory is inside a linked git worktree

Added 
● N running
 indicator in 
/agents
 next to agent types with live subagent instances

Added syntax highlighting for Cedar policy files (
.cedar
, 
.cedarpolicy
)

Fixed 
--dangerously-skip-permissions
 being silently downgraded to accept-edits mode after approving a write to a protected path

Fixed and hardened Bash tool permissions, tightening checks around env-var prefixes and network redirects, and reducing false prompts on common commands

Fixed permission rules with names matching JavaScript prototype properties (e.g. 
toString
) causing 
settings.json
 to be silently ignored

Fixed managed-settings allow rules remaining active after an admin removed them until process restart

Fixed 
permissions.additionalDirectories
 changes in settings not applying mid-session

Fixed removing a directory from 
settings.permissions.additionalDirectories
 revoking access to the same directory passed via 
--add-dir

Fixed MCP HTTP/SSE connections accumulating ~50 MB/hr of unreleased buffers when servers reconnect

Fixed MCP OAuth 
oauth.authServerMetadataUrl
 not being honored on token refresh after restart, fixing ADFS and similar IdPs

Fixed 429 retries burning all attempts in ~13 seconds when the server returns a small 
Retry-After
 — exponential backoff now applies as a minimum

Fixed rate-limit upgrade options disappearing after context compaction

Fixed several 
/resume
 picker issues: 
--resume <name>
 opening uneditable, Ctrl+A reload wiping search, empty list swallowing navigation, task-status text replacing conversation summary, and cross-project staleness

Fixed file-edit diffs disappearing on 
--resume
 when the edited file was larger than 10KB

Fixed 
--resume
 cache misses and lost mid-turn input from attachment messages not being saved to the transcript

Fixed messages typed while Claude is working not being persisted to the transcript

Fixed prompt-type 
Stop
/
SubagentStop
 hooks failing on long sessions, and hook evaluator API errors displaying “JSON validation failed” instead of the actual message

Fixed subagents with worktree isolation or 
cwd:
 override leaking their working directory back to the parent session’s Bash tool

Fixed compaction writing duplicate multi-MB subagent transcript files on prompt-too-long retries

Fixed 
claude plugin update
 reporting “already at the latest version” for git-based marketplace plugins when the remote had newer commits

Fixed slash command picker breaking when a plugin’s frontmatter 
name
 is a YAML boolean keyword

Fixed copying wrapped URLs in 
NO_FLICKER
 mode inserting spaces at line breaks

Fixed scroll rendering artifacts in 
NO_FLICKER
 mode when running inside zellij

Fixed a crash in 
NO_FLICKER
 mode when hovering over MCP tool results

Fixed a 
NO_FLICKER
 mode memory leak where API retries left stale streaming state

Fixed slow mouse-wheel scrolling in 
NO_FLICKER
 mode on Windows Terminal

Fixed custom status line not displaying in 
NO_FLICKER
 mode on terminals shorter than 24 rows

Fixed Shift+Enter and Alt/Cmd+arrow shortcuts not working in Warp with 
NO_FLICKER
 mode

Fixed Korean/Japanese/Unicode text becoming garbled when copied in no-flicker mode on Windows

Fixed Bedrock SigV4 authentication failing when 
AWS_BEARER_TOKEN_BEDROCK
 or 
ANTHROPIC_BEDROCK_BASE_URL
 are set to empty strings (as GitHub Actions does for unset inputs)

Improved Accept Edits mode to auto-approve filesystem commands prefixed with safe env vars or process wrappers (e.g. 
LANG=C rm foo
, 
timeout 5 mkdir out
)

Improved auto mode and bypass-permissions mode to auto-approve sandbox network access prompts

Improved sandbox: 
sandbox.network.allowMachLookup
 now takes effect on macOS

Improved image handling: pasted and attached images are now compressed to the same token budget as images read via the Read tool

Improved slash command and 
@
-mention completion to trigger after CJK sentence punctuation, so Japanese/Chinese input no longer requires a space before 
/
 or 
@

Improved Bridge sessions to show the local git repo, branch, and working directory on the claude.ai session card

Improved footer layout: indicators (Focus, notifications) now stay on the mode-indicator row instead of wrapping below

Improved context-low warning to show as a transient footer notification instead of a persistent row

Improved markdown blockquotes to show a continuous left bar across wrapped lines

Improved session transcript size by skipping empty hook entries and capping stored pre-edit file copies

Improved transcript accuracy: per-block entries now carry the final token usage instead of the streaming placeholder

Improved Bash tool OTEL tracing: subprocesses now inherit a W3C 
TRACEPARENT
 env var when tracing is enabled

Updated 
/claude-api
 skill to cover Managed Agents alongside the Claude API

​

2.1.96

April 8, 2026

Fixed Bedrock requests failing with 
403 "Authorization header is missing"
 when using 
AWS_BEARER_TOKEN_BEDROCK
 or 
CLAUDE_CODE_SKIP_BEDROCK_AUTH
 (regression in 2.1.94)

​

2.1.94

April 7, 2026

Added support for Amazon Bedrock powered by Mantle, set 
CLAUDE_CODE_USE_MANTLE=1

Changed default effort level from medium to high for API-key, Bedrock/Vertex/Foundry, Team, and Enterprise users (control this with 
/effort
)

Added compact 
Slacked #channel
 header with a clickable channel link for Slack MCP send-message tool calls

Added 
keep-coding-instructions
 frontmatter field support for plugin output styles

Added 
hookSpecificOutput.sessionTitle
 to 
UserPromptSubmit
 hooks for setting the session title

Plugin skills declared via 
"skills": ["./"]
 now use the skill’s frontmatter 
name
 for the invocation name instead of the directory basename, giving a stable name across install methods

Fixed agents appearing stuck after a 429 rate-limit response with a long Retry-After header — the error now surfaces immediately instead of silently waiting

Fixed Console login on macOS silently failing with “Not logged in” when the login keychain is locked or its password is out of sync — the error is now surfaced and 
claude doctor
 diagnoses the fix

Fixed plugin skill hooks defined in YAML frontmatter being silently ignored

Fixed plugin hooks failing with “No such file or directory” when 
CLAUDE_PLUGIN_ROOT
 was not set

Fixed 
${CLAUDE_PLUGIN_ROOT}
 resolving to the marketplace source directory instead of the installed cache for local-marketplace plugins on startup

Fixed scrollback showing the same diff repeated and blank pages in long-running sessions

Fixed multiline user prompts in the transcript indenting wrapped lines under the 
❯
 caret instead of under the text

Fixed Shift+Space inserting the literal word “space” instead of a space character in search inputs

Fixed hyperlinks opening two browser tabs when clicked inside tmux running in an xterm.js-based terminal (VS Code, Hyper, Tabby)

Fixed an alt-screen rendering bug where content height changes mid-scroll could leave compounding ghost lines

Fixed 
FORCE_HYPERLINK
 environment variable being ignored when set via 
settings.json

env

Fixed native terminal cursor not tracking the selected tab in dialogs, so screen readers and magnifiers can follow tab navigation

Fixed Bedrock invocation of Sonnet 3.5 v2 by using the 
us.
 inference profile ID

Fixed SDK/print mode not preserving the partial assistant response in conversation history when interrupted mid-stream

Improved 
--resume
 to resume sessions from other worktrees of the same repo directly instead of printing a 
cd
 command

Fixed CJK and other multibyte text being corrupted with U+FFFD in stream-json input/output when chunk boundaries split a UTF-8 sequence

[VSCode] Reduced cold-open subprocess work on starting a session

[VSCode] Fixed dropdown menus selecting the wrong item when the mouse was over the list while typing or using arrow keys

[VSCode] Added a warning banner when 
settings.json
 files fail to parse, so users know their permission rules are not being applied

​

2.1.92

April 4, 2026

Added 
forceRemoteSettingsRefresh
 policy setting: when set, the CLI blocks startup until remote managed settings are freshly fetched, and exits if the fetch fails (fail-closed)

Added interactive Bedrock setup wizard accessible from the login screen when selecting “3rd-party platform” — guides you through AWS authentication, region configuration, credential verification, and model pinning

Added per-model and cache-hit breakdown to 
/cost
 for subscription users

/release-notes
 is now an interactive version picker

Remote Control session names now use your hostname as the default prefix (e.g. 
myhost-graceful-unicorn
), overridable with 
--remote-control-session-name-prefix

Pro users now see a footer hint when returning to a session after the prompt cache has expired, showing roughly how many tokens the next turn will send uncached

Fixed subagent spawning permanently failing with “Could not determine pane count” after tmux windows are killed or renumbered during a long-running session

Fixed prompt-type Stop hooks incorrectly failing when the small fast model returns 
ok:false
, and restored 
preventContinuation:true
 semantics for non-Stop prompt-type hooks

Fixed tool input validation failures when streaming emits array/object fields as JSON-encoded strings

Fixed an API 400 error that could occur when extended thinking produced a whitespace-only text block alongside real content

Fixed accidental feedback survey submissions from auto-pilot keypresses and consecutive-prompt digit collisions

Fixed misleading “esc to interrupt” hint appearing alongside “esc to clear” when a text selection exists in fullscreen mode during processing

Fixed Homebrew install update prompts to use the cask’s release channel (
claude-code
 → stable, 
claude-code@latest
 → latest)

Fixed 
ctrl+e
 jumping to the end of the next line when already at end of line in multiline prompts

Fixed an issue where the same message could appear at two positions when scrolling up in fullscreen mode (iTerm2, Ghostty, and other terminals with DEC 2026 support)

Fixed idle-return “/clear to save X tokens” hint showing cumulative session tokens instead of current context size

Fixed plugin MCP servers stuck “connecting” on session start when they duplicate a claude.ai connector that is unauthenticated

Improved Write tool diff computation speed for large files (60% faster on files with tabs/
&
/
$
)

Removed 
/tag
 command

Removed 
/vim
 command (toggle vim mode via 
/config
 → Editor mode)

Linux sandbox now ships the 
apply-seccomp
 helper in both npm and native builds, restoring unix-socket blocking for sandboxed commands

​

2.1.91

April 2, 2026

Added MCP tool result persistence override via 
_meta["anthropic/maxResultSizeChars"]
 annotation (up to 500K), allowing larger results like DB schemas to pass through without truncation

Added 
disableSkillShellExecution
 setting to disable inline shell execution in skills, custom slash commands, and plugin commands

Added support for multi-line prompts in 
claude-cli://open?q=
 deep links (encoded newlines 
%0A
 no longer rejected)

Plugins can now ship executables under 
bin/
 and invoke them as bare commands from the Bash tool

Fixed transcript chain breaks on 
--resume
 that could lose conversation history when async transcript writes fail silently

Fixed 
cmd+delete
 not deleting to start of line on iTerm2, kitty, WezTerm, Ghostty, and Windows Terminal

Fixed plan mode in remote sessions losing track of the plan file after a container restart, which caused permission prompts on plan edits and an empty plan-approval modal

Fixed JSON schema validation for 
permissions.defaultMode: "auto"
 in settings.json

Fixed Windows version cleanup not protecting the active version’s rollback copy

/feedback
 now explains why it’s unavailable instead of disappearing from the slash menu

Improved 
/claude-api
 skill guidance for agent design patterns including tool surface decisions, context management, and caching strategy

Improved performance: faster 
stripAnsi
 on Bun by routing through 
Bun.stripANSI

Edit tool now uses shorter 
old_string
 anchors, reducing output tokens

​

2.1.90

April 1, 2026

Added 
/powerup
 — interactive lessons teaching Claude Code features with animated demos

Added 
CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE
 env var to keep the existing marketplace cache when 
git pull
 fails, useful in offline environments

Added 
.husky
 to protected directories (acceptEdits mode)

Fixed an infinite loop where the rate-limit options dialog would repeatedly auto-open after hitting your usage limit, eventually crashing the session

Fixed 
--resume
 causing a full prompt-cache miss on the first request for users with deferred tools, MCP servers, or custom agents (regression since v2.1.69)

Fixed 
Edit
/
Write
 failing with “File content has changed” when a PostToolUse format-on-save hook rewrites the file between consecutive edits

Fixed 
PreToolUse
 hooks that emit JSON to stdout and exit with code 2 not correctly blocking the tool call

Fixed collapsed search/read summary badge appearing multiple times in fullscreen scrollback when a CLAUDE.md file auto-loads during a tool call

Fixed auto mode not respecting explicit user boundaries (“don’t push”, “wait for X before Y”) even when the action would otherwise be allowed

Fixed click-to-expand hover text being nearly invisible on light terminal themes

Fixed UI crash when malformed tool input reached the permission dialog

Fixed headers disappearing when scrolling 
/model
, 
/config
, and other selection screens

Hardened PowerShell tool permission checks: fixed trailing 
&
 background job bypass, 
-ErrorAction Break
 debugger hang, archive-extraction TOCTOU, and parse-fail fallback deny-rule degradation

Improved performance: eliminated per-turn JSON.stringify of MCP tool schemas on cache-key lookup

Improved performance: SSE transport now handles large streamed frames in linear time (was quadratic)

Improved performance: SDK sessions with long conversations no longer slow down quadratically on transcript writes

Improved 
/resume
 all-projects view to load project sessions in parallel, improving load times for users with many projects

Changed 
--resume
 picker to no longer show sessions created by 
claude -p
 or SDK invocations

Removed 
Get-DnsClientCache
 and 
ipconfig /displaydns
 from auto-allow (DNS cache privacy)

​

2.1.89

April 1, 2026

Added 
"defer"
 permission decision to 
PreToolUse
 hooks — headless sessions can pause at a tool call and resume with 
-p --resume
 to have the hook re-evaluate

Added 
CLAUDE_CODE_NO_FLICKER=1
 environment variable to opt into flicker-free alt-screen rendering with virtualized scrollback

Added 
PermissionDenied
 hook that fires after auto mode classifier denials — return 
{retry: true}
 to tell the model it can retry

Added named subagents to 
@
 mention typeahead suggestions

Added 
MCP_CONNECTION_NONBLOCKING=true
 for 
-p
 mode to skip the MCP connection wait entirely, and bounded 
--mcp-config
 server connections at 5s instead of blocking on the slowest server

Auto mode: denied commands now show a notification and appear in 
/permissions
 → Recent tab where you can retry with 
r

Fixed 
Edit(//path/**)
 and 
Read(//path/**)
 allow rules to check the resolved symlink target, not just the requested path

Fixed voice push-to-talk not activating for some modifier-combo bindings, and voice mode on Windows failing with “WebSocket upgrade rejected with HTTP 101”

Fixed Edit/Write tools doubling CRLF on Windows and stripping Markdown hard line breaks (two trailing spaces)

Fixed 
StructuredOutput
 schema cache bug causing ~50% failure rate when using multiple schemas

Fixed memory leak where large JSON inputs were retained as LRU cache keys in long-running sessions

Fixed a crash when removing a message from very large session files (over 50MB)

Fixed LSP server zombie state after crash — server now restarts on next request instead of failing until session restart

Fixed prompt history entries containing CJK or emoji being silently dropped when they fall on a 4KB boundary in 
~/.claude/history.jsonl

Fixed 
/stats
 undercounting tokens by excluding subagent usage, and losing historical data beyond 30 days when the stats cache format changes

Fixed 
-p --resume
 hangs when the deferred tool input exceeds 64KB or no deferred marker exists, and 
-p --continue
 not resuming deferred tools

Fixed 
claude-cli://
 deep links not opening on macOS

Fixed MCP tool errors truncating to only the first content block when the server returns multi-element error content

Fixed skill reminders and other system context being dropped when sending messages with images via the SDK

Fixed PreToolUse/PostToolUse hooks to receive 
file_path
 as an absolute path for Write/Edit/Read tools, matching the documented behavior

Fixed autocompact thrash loop — now detects when context refills to the limit immediately after compacting three times in a row and stops with an actionable error instead of burning API calls

Fixed prompt cache misses in long sessions caused by tool schema bytes changing mid-session

Fixed nested CLAUDE.md files being re-injected dozens of times in long sessions that read many files

Fixed 
--resume
 crash when transcript contains a tool result from an older CLI version or interrupted write

Fixed misleading “Rate limit reached” message when the API returned an entitlement error — now shows the actual error with actionable hints

Fixed hooks 
if
 condition filtering not matching compound commands (
ls && git push
) or commands with env-var prefixes (
FOO=bar git push
)

Fixed collapsed search/read group badges duplicating in terminal scrollback during heavy parallel tool use

Fixed notification 
invalidates
 not clearing the currently-displayed notification immediately

Fixed prompt briefly disappearing after submit when background messages arrived during processing

Fixed Devanagari and other combining-mark text being truncated in assistant output

Fixed rendering artifacts on main-screen terminals after layout shifts

Fixed voice mode failing to request microphone permission on macOS Apple Silicon

Fixed Shift+Enter submitting instead of inserting a newline on Windows Terminal Preview 1.25

Fixed periodic UI jitter during streaming in iTerm2 when running inside tmux

Fixed PowerShell tool incorrectly reporting failures when commands like 
git push
 wrote progress to stderr on Windows PowerShell 5.1

Fixed a potential out-of-memory crash when the Edit tool was used on very large files (>1 GiB)

Improved collapsed tool summary to show “Listed N directories” for 
ls
/
tree
/
du
 instead of “Read N files”

Improved Bash tool to warn when a formatter/linter command modifies files you have previously read, preventing stale-edit errors

Improved 
@
-mention typeahead to rank source files above MCP resources with similar names

Improved PowerShell tool prompt with version-appropriate syntax guidance (5.1 vs 7+)

Changed 
Edit
 to work on files viewed via 
Bash
 with 
sed -n
 or 
cat
, without requiring a separate 
Read
 call first

Changed hook output over 50K characters to be saved to disk with a file path + preview instead of being injected directly into context

Changed 
cleanupPeriodDays: 0
 in settings.json to be rejected with a validation error — it previously silently disabled transcript persistence

Changed thinking summaries to no longer be generated by default in interactive sessions — set 
showThinkingSummaries: true
 in settings.json to restore

Documented 
TaskCreated
 hook event and its blocking behavior

Preserved task notifications when backgrounding a running command with Ctrl+B

PowerShell tool on Windows: external-command arguments containing both a double-quote and whitespace now prompt instead of auto-allowing (PS 5.1 argument-splitting hardening)

/env
 now applies to PowerShell tool commands (previously only affected Bash)

/usage
 now hides redundant “Current week (Sonnet only)” bar for Pro and Enterprise plans

Image paste no longer inserts a trailing space

Pasting 
!command
 into an empty prompt now enters bash mode, matching typed 
!
 behavior

/buddy
 is here for April 1st — hatch a small creature that watches you code

​

2.1.87

March 29, 2026

Fixed messages in Cowork Dispatch not getting delivered

​

2.1.86

March 27, 2026

Added 
X-Claude-Code-Session-Id
 header to API requests so proxies can aggregate requests by session without parsing the body

Added 
.jj
 and 
.sl
 to VCS directory exclusion lists so Grep and file autocomplete don’t descend into Jujutsu or Sapling metadata

Fixed 
--resume
 failing with “tool_use ids were found without tool_result blocks” on sessions created before v2.1.85

Fixed Write/Edit/Read failing on files outside the project root (e.g., 
~/.claude/CLAUDE.md
) when conditional skills or rules are configured

Fixed unnecessary config disk writes on every skill invocation that could cause performance issues and config corruption on Windows

Fixed potential out-of-memory crash when using 
/feedback
 on very long sessions with large transcript files

Fixed 
--bare
 mode dropping MCP tools in interactive sessions and silently discarding messages enqueued mid-turn

Fixed the 
c
 shortcut copying only ~20 characters of the OAuth login URL instead of the full URL

Fixed masked input (e.g., OAuth code paste) leaking the start of the token when wrapping across multiple lines on narrow terminals

Fixed official marketplace plugin scripts failing with “Permission denied” on macOS/Linux since v2.1.83

Fixed statusline showing another session’s model when running multiple Claude Code instances and using 
/model
 in one of them

Fixed scroll not following new messages after wheel scroll or click-to-select at the bottom of a long conversation

Fixed 
/plugin
 uninstall dialog: pressing 
n
 now correctly uninstalls the plugin while preserving its data directory

Fixed a regression where pressing Enter after clicking could leave the transcript blank until the response arrived

Fixed 
ultrathink
 hint lingering after deleting the keyword

Fixed memory growth in long sessions from markdown/highlight render caches retaining full content strings

Reduced startup event-loop stalls when many claude.ai MCP connectors are configured (macOS keychain cache extended from 5s to 30s)

Reduced token overhead when mentioning files with 
@
 — raw string content no longer JSON-escaped

Improved prompt cache hit rate for Bedrock, Vertex, and Foundry users by removing dynamic content from tool descriptions

Memory filenames in the “Saved N memories” notice now highlight on hover and open on click

Skill descriptions in the 
/skills
 listing are now capped at 250 characters to reduce context usage

Changed 
/skills
 menu to sort alphabetically for easier scanning

Auto mode now shows “unavailable for your plan” when disabled by plan restrictions (was “temporarily unavailable”)

[VSCode] Fixed extension incorrectly showing “Not responding” during long-running operations

[VSCode] Fixed extension defaulting Max plan users to Sonnet after the OAuth token refreshes (8 hours after login)

Read tool now uses compact line-number format and deduplicates unchanged re-reads, reducing token usage

​

2.1.85

March 26, 2026

Added 
CLAUDE_CODE_MCP_SERVER_NAME
 and 
CLAUDE_CODE_MCP_SERVER_URL
 environment variables to MCP 
headersHelper
 scripts, allowing one helper to serve multiple servers

Added conditional 
if
 field for hooks using permission rule syntax (e.g., 
Bash(git *)
) to filter when they run, reducing process spawning overhead

Added timestamp markers in transcripts when scheduled tasks (
/loop
, 
CronCreate
) fire

Added trailing space after 
[Image #N]
 placeholder when pasting images

Deep link queries (
claude-cli://open?q=…
) now support up to 5,000 characters, with a “scroll to review” warning for long pre-filled prompts

MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find the authorization server

Plugins blocked by organization policy (
managed-settings.json
) can no longer be installed or enabled, and are hidden from marketplace views

PreToolUse hooks can now satisfy 
AskUserQuestion
 by returning 
updatedInput
 alongside 
permissionDecision: "allow"
, enabling headless integrations that collect answers via their own UI

tool_parameters
 in OpenTelemetry tool_result events are now gated behind 
OTEL_LOG_TOOL_DETAILS=1

Fixed 
/compact
 failing with “context exceeded” when the conversation has grown too large for the compact request itself to fit

Fixed 
/plugin enable
 and 
/plugin disable
 failing when a plugin’s install location differs from where it’s declared in settings

Fixed 
--worktree
 exiting with an error in non-git repositories before the 
WorktreeCreate
 hook could run

Fixed 
deniedMcpServers
 setting not blocking claude.ai MCP servers

Fixed 
switch_display
 in the computer-use tool returning “not available in this session” on multi-monitor setups

Fixed crash when 
OTEL_LOGS_EXPORTER
, 
OTEL_METRICS_EXPORTER
, or 
OTEL_TRACES_EXPORTER
 is set to 
none

Fixed diff syntax highlighting not working in non-native builds

Fixed MCP step-up authorization failing when a refresh token exists — servers requesting elevated scopes via 
403 insufficient_scope
 now correctly trigger the re-authorization flow

Fixed memory leak in remote sessions when a streaming response is interrupted

Fixed persistent ECONNRESET errors during edge connection churn by using a fresh TCP connection on retry

Fixed prompts getting stuck in the queue after running certain slash commands, with up-arrow unable to retrieve them

Fixed Python Agent SDK: 
type:'sdk'
 MCP servers passed via 
--mcp-config
 are no longer dropped during startup

Fixed raw key sequences appearing in the prompt when running over SSH or in the VS Code integrated terminal

Fixed Remote Control session status staying stuck on “Requires Action” after a permission is resolved

Fixed shift+enter and meta+enter being intercepted by typeahead suggestions instead of inserting newlines

Fixed stale content bleeding through when scrolling up during streaming

Fixed terminal left in enhanced keyboard mode after exit in Ghostty, Kitty, WezTerm, and other terminals supporting the Kitty keyboard protocol — Ctrl+C and Ctrl+D now work correctly after quitting

Improved @-mention file autocomplete performance on large repositories

Improved PowerShell dangerous command detection

Improved scroll performance with large transcripts by replacing WASM yoga-layout with a pure TypeScript implementation

Reduced UI stutter when compaction triggers on large sessions

​

2.1.84

March 26, 2026

Added PowerShell tool for Windows as an opt-in preview. Learn more at https://code.claude.com/docs/en/tools-reference#powershell-tool

Added 
ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS
 env vars to override effort/thinking capability detection for pinned default models for 3p (Bedrock, Vertex, Foundry), and 
_MODEL_NAME
/
_DESCRIPTION
 to customize the 
/model
 picker label

Added 
CLAUDE_STREAM_IDLE_TIMEOUT_MS
 env var to configure the streaming idle watchdog threshold (default 90s)

Added 
TaskCreated
 hook that fires when a task is created via 
TaskCreate

Added 
WorktreeCreate
 hook support for 
type: "http"
 — return the created worktree path via 
hookSpecificOutput.worktreePath
 in the response JSON

Added 
allowedChannelPlugins
 managed setting for team/enterprise admins to define a channel plugin allowlist

Added 
x-client-request-id
 header to API requests for debugging timeouts

Added idle-return prompt that nudges users returning after 75+ minutes to 
/clear
, reducing unnecessary token re-caching on stale sessions

Deep links (
claude-cli://
) now open in your preferred terminal instead of whichever terminal happens to be first in the detection list

Rules and skills 
paths:
 frontmatter now accepts a YAML list of globs

MCP tool descriptions and server instructions are now capped at 2KB to prevent OpenAPI-generated servers from bloating context

MCP servers configured both locally and via claude.ai connectors are now deduplicated — the local config wins

Background bash tasks that appear stuck on an interactive prompt now surface a notification after ~45 seconds

Token counts ≥1M now display as “1.5m” instead of “1512.6k”

Global system-prompt caching now works when 
ToolSearch
 is enabled, including for users with MCP tools configured

Fixed voice push-to-talk: holding the voice key no longer leaks characters into the text input, and transcripts now insert at the correct position

Fixed up/down arrow keys being unresponsive when a footer item is focused

Fixed 
Ctrl+U
 (kill-to-line-start) being a no-op at line boundaries in multiline input, so repeated 
Ctrl+U
 now clears across lines

Fixed null-unbinding a default chord binding (e.g. 
"ctrl+x ctrl+k": null
) still entering chord-wait mode instead of freeing the prefix key

Fixed mouse events inserting literal “mouse” text into transcript search input

Fixed workflow subagents failing with API 400 when the outer session uses 
--json-schema
 and the subagent also specifies a schema

Fixed missing background color behind certain emoji in user message bubbles on some terminals

Fixed the “allow Claude to edit its own settings for this session” permission option not sticking for users with 
Edit(.claude)
 allow rules

Fixed a hang when generating attachment snippets for large edited files

Fixed MCP tool/resource cache leak on server reconnect

Fixed a startup performance issue where partial clone repositories (Scalar/GVFS) triggered mass blob downloads

Fixed native terminal cursor not tracking the text input caret, so IME composition (CJK input) now renders inline and screen readers can follow the input position

Fixed spurious “Not logged in” errors on macOS caused by transient keychain read failures

Fixed cold-start race where core tools could be deferred without their bypass active, causing Edit/Write to fail with InputValidationError on typed parameters

Improved detection for dangerous removals of Windows drive roots (
C:\
, 
C:\Windows
, etc.)

Improved interactive startup by ~30ms by running 
setup()
 in parallel with slash command and agent loading

Improved startup for 
claude "prompt"
 with MCP servers — the REPL now renders immediately instead of blocking until all servers connect

Improved Remote Control to show a specific reason when blocked instead of a generic “not yet enabled” message

Improved p90 prompt cache rate

Reduced scroll-to-top resets in long sessions by making the message window immune to compaction and grouping changes

Reduced terminal flickering when animated tool progress scrolls above the viewport

Changed issue/PR references to only become clickable links when written as 
owner/repo#123
 — bare 
#123
 is no longer auto-linked

Slash commands unavailable for the current auth setup (
/voice
, 
/mobile
, 
/chrome
, 
/upgrade
, etc.) are now hidden instead of shown

[VSCode] Added rate limit warning banner with usage percentage and reset time

Stats screenshot (Ctrl+S in /stats) now works in all builds and is 16× faster

​

2.1.83

March 25, 2026

Added 
managed-settings.d/
 drop-in directory alongside 
managed-settings.json
, letting separate teams deploy independent policy fragments that merge alphabetically

Added 
CwdChanged
 and 
FileChanged
 hook events for reactive environment management (e.g., direnv)

Added 
sandbox.failIfUnavailable
 setting to exit with an error when sandbox is enabled but cannot start, instead of running unsandboxed

Added 
disableDeepLinkRegistration
 setting to prevent 
claude-cli://
 protocol handler registration

Added 
CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1
 to strip Anthropic and cloud provider credentials from subprocess environments (Bash tool, hooks, MCP stdio servers)

Added transcript search — press 
/
 in transcript mode (
Ctrl+O
) to search, 
n
/
N
 to step through matches

Added 
Ctrl+X Ctrl+E
 as an alias for opening the external editor (readline-native binding; 
Ctrl+G
 still works)

Pasted images now insert an 
[Image #N]
 chip at the cursor so you can reference them positionally in your prompt

Agents can now declare 
initialPrompt
 in frontmatter to auto-submit a first turn

chat:killAgents
 and 
chat:fastMode
 are now rebindable via 
~/.claude/keybindings.json

Fixed mouse tracking escape sequences leaking to shell prompt after exit

Fixed Claude Code hanging on exit on macOS

Fixed screen flashing blank after being idle for a few seconds

Fixed a hang when diffing very large files with few common lines — diffs now time out after 5 seconds and fall back gracefully

Fixed a 1–8 second UI freeze on startup when voice input was enabled, caused by eagerly loading the native audio module

Fixed a startup regression where Claude Code would wait ~3s for claude.ai MCP config fetch before proceeding

Fixed 
--mcp-config
 CLI flag bypassing 
allowedMcpServers
/
deniedMcpServers
 managed policy enforcement

Fixed claude.ai MCP connectors (Slack, Gmail, etc.) not being available in single-turn 
--print
 mode

Fixed 
caffeinate
 process not properly terminating when Claude Code exits, preventing Mac from sleeping

Fixed bash mode not activating when tab-accepting 
!
-prefixed command suggestions

Fixed stale slash command selection showing wrong highlighted command after navigating suggestions

Fixed 
/config
 menu showing both the search cursor and list selection at the same time

Fixed background subagents becoming invisible after context compaction, which could cause duplicate agents to be spawned

Fixed background agent tasks staying stuck in “running” state when git or API calls hang during cleanup

Fixed 
--channels
 showing “Channels are not currently available” on first launch after upgrade

Fixed uninstalled plugin hooks continuing to fire until the next session

Fixed queued commands flickering during streaming responses

Fixed slash commands being sent to the model as text when submitted while a message is processing

Fixed scrollback jumping when collapsed read/search groups finish after scrolling offscreen

Fixed scrollback jumping to top when the model starts or stops thinking

Fixed SDK session history loss on resume caused by hook progress/attachment messages forking the parentUuid chain

Fixed copy-on-select not firing when you release the mouse outside the terminal window

Fixed ghost characters appearing in height-constrained lists when items overflow

Fixed 
Ctrl+B
 interfering with readline backward-char at an idle prompt — it now only fires when a foreground task can be backgrounded

Fixed tool result files never being cleaned up, ignoring the 
cleanupPeriodDays
 setting

Fixed space key being swallowed for up to 3 seconds after releasing voice hold-to-talk

Fixed ALSA library errors corrupting the terminal UI when using voice mode on Linux without audio hardware (Docker, headless, WSL1)

Fixed voice mode SoX detection on Termux/Android where spawning 
which
 is kernel-restricted

Fixed Remote Control sessions showing as Idle in the web session list while actively running

Fixed footer navigation selecting an invisible Remote Control pill in config-driven mode

Fixed memory leak in remote sessions where tool use IDs accumulate indefinitely

Improved Bedrock SDK cold-start latency by overlapping profile fetch with other boot work

Improved 
--resume
 memory usage and startup latency on large sessions

Improved plugin startup — commands, skills, and agents now load from disk cache without re-fetching

Improved Remote Control session titles: AI-generated titles now appear within seconds of the first message

Improved 
WebFetch
 to identify as 
Claude-User
 so site operators can recognize and allowlist Claude Code traffic via 
robots.txt

Reduced 
WebFetch
 peak memory usage for large pages

Reduced scrollback resets in long sessions from once per turn to once per ~50 messages

Faster 
claude -p
 startup with unauthenticated HTTP/SSE MCP servers (~600ms saved)

Bash ghost-text suggestions now include just-submitted commands immediately

Increased non-streaming fallback token cap (21k → 64k) and timeout (120s → 300s local) so fallback requests are less likely to be truncated

Interrupting a prompt before any response now automatically restores your input so you can edit and resubmit

/status
 now works while Claude is responding, instead of being queued until the turn finishes

Plugin MCP servers that duplicate an org-managed connector are now suppressed instead of running a second connection

Linux: respect 
XDG_DATA_HOME
 when registering the 
claude-cli://
 protocol handler

Changed “stop all background agents” keybinding from 
Ctrl+F
 to 
Ctrl+X Ctrl+K
 to stop shadowing readline forward-char

Deprecated 
TaskOutput
 tool in favor of using 
Read
 on the background task’s output file path

Added 
CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK
 env var to disable the non-streaming fallback when streaming fails

Plugin options (
manifest.userConfig
) now available externally — plugins can prompt for configuration at enable time, with 
sensitive: true
 values stored in keychain (macOS) or protected credentials file (other platforms)

Claude can now reference the on-disk path of clipboard-pasted images for file operations

Ctrl+L
 now clears the screen and forces a full redraw — use this to recover when Cmd+K leaves the UI partially blank. Use 
Ctrl+U
 or double-Esc to clear prompt input.

--bare -p
 (SDK pattern) is ~14% faster to the API request

Memory: 
MEMORY.md
 index now truncates at 25KB as well as 200 lines

Disabled 
AskUserQuestion
 and plan-mode tools when 
--channels
 is active

Fixed API 400 error when a pasted image was queued during a failing tool call

Fixed MCP tool calls hanging indefinitely when an SSE connection drops mid-call and exhausts its reconnection attempts

Fixed Remote Control session titles showing raw XML when a background agent completed before the first user message

Fixed remote sessions forgetting conversation history after a container restart due to progress-message gaps in the resumed transcript chain

Fixed remote sessions requiring re-login on transient auth errors instead of retrying automatically

Fixed 
rg ... | wc -l
 and similar piped commands hanging and returning 
0
 in sandbox mode on Linux

Fixed voice input hold-to-talk not activating when a CJK IME inserts a full-width space

Fixed 
--worktree
 hanging silently when the worktree name contained a forward slash

[VSCode] Spinner now turns red with “Not responding” when the backend hasn’t responded for 60 seconds

[VSCode] Fixed session history not loading correctly when reopening a session via URL or after restart

[VSCode] Added Esc-twice (or 
/rewind
) to open a keyboard-navigable rewind picker

[VSCode] Fixed “Fork conversation from here” and rewind actions failing silently after the session cache goes stale

​

2.1.81

March 20, 2026

Added 
--bare
 flag for scripted 
-p
 calls — skips hooks, LSP, plugin sync, and skill directory walks; requires 
ANTHROPIC_API_KEY
 or an 
apiKeyHelper
 via 
--settings
 (OAuth and keychain auth disabled); auto-memory fully disabled

Added 
--channels
 permission relay — channel servers that declare the permission capability can forward tool approval prompts to your phone

Fixed multiple concurrent Claude Code sessions requiring repeated re-authentication when one session refreshes its OAuth token

Fixed voice mode silently swallowing retry failures and showing a misleading “check your network” message instead of the actual error

Fixed voice mode audio not recovering when the server silently drops the WebSocket connection

Fixed 
CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS
 not suppressing the structured-outputs beta header, causing 400 errors on proxy gateways forwarding to Vertex/Bedrock

Fixed 
--channels
 bypass for Team/Enterprise orgs with no other managed settings configured

Fixed a crash on Node.js 18

Fixed unnecessary permission prompts for Bash commands containing dashes in strings

Fixed plugin hooks blocking prompt submission when the plugin directory is deleted mid-session

Fixed a race condition where background agent task output could hang indefinitely when the task completed between polling intervals

Resuming a session that was in a worktree now switches back to that worktree

Fixed 
/btw
 not including pasted text when used during an active response

Fixed a race where fast Cmd+Tab followed by paste could beat the clipboard copy under tmux

Fixed terminal tab title not updating with an auto-generated session description

Fixed invisible hook attachments inflating the message count in transcript mode

Fixed Remote Control sessions showing a generic title instead of deriving from the first prompt

Fixed 
/rename
 not syncing the title for Remote Control sessions

Fixed Remote Control 
/exit
 not reliably archiving the session

Improved MCP read/search tool calls to collapse into a single “Queried 
{server}
” line (expand with Ctrl+O)

Improved 
!
 bash mode discoverability — Claude now suggests it when you need to run an interactive command

Improved plugin freshness — ref-tracked plugins now re-clone on every load to pick up upstream changes

Improved Remote Control session titles to refresh after your third message

Updated MCP OAuth to support Client ID Metadata Document (CIMD / SEP-991) for servers without Dynamic Client Registration

Changed plan mode to hide the “clear context” option by default (restore with 
"showClearContextOnPlanAccept": true
)

Disabled line-by-line response streaming on Windows (including WSL in Windows Terminal) due to rendering issues

[VSCode] Fixed Windows PATH inheritance for Bash tool when using Git Bash (regression in v2.1.78)

​

2.1.80

March 19, 2026

Added 
rate_limits
 field to statusline scripts for displaying Claude.ai rate limit usage (5-hour and 7-day windows with 
used_percentage
 and 
resets_at
)

Added 
source: 'settings'
 plugin marketplace source — declare plugin entries inline in settings.json

Added CLI tool usage detection to plugin tips, in addition to file pattern matching

Added 
effort
 frontmatter support for skills and slash commands to override the model effort level when invoked

Added 
--channels
 (research preview) — allow MCP servers to push messages into your session

Fixed 
--resume
 dropping parallel tool results — sessions with parallel tool calls now restore all tool_use/tool_result pairs instead of showing 
[Tool result missing]
 placeholders

Fixed voice mode WebSocket failures caused by Cloudflare bot detection on non-browser TLS fingerprints

Fixed 400 errors when using fine-grained tool streaming through API proxies, Bedrock, or Vertex

Fixed 
/remote-control
 appearing for gateway and third-party provider deployments where it cannot function

Fixed 
/sandbox
 tab switching not responding to Tab or arrow keys

Improved responsiveness of 
@
 file autocomplete in large git repositories

Improved 
/effort
 to show what auto currently resolves to, matching the status bar indicator

Improved 
/permissions
 — Tab and arrow keys now switch tabs from within a list

Improved background tasks panel — left arrow now closes from the list view

Simplified plugin install tips to use a single 
/plugin install
 command instead of a two-step flow

Reduced memory usage on startup in large repositories (~80 MB saved on 250k-file repos)

Fixed managed settings (
enabledPlugins
, 
permissions.defaultMode
, policy-set env vars) not being applied at startup when 
remote-settings.json
 was cached from a prior session

​

2.1.79

March 18, 2026

Added 
--console
 flag to 
claude auth login
 for Anthropic Console (API billing) authentication

Added “Show turn duration” toggle to the 
/config
 menu

Fixed 
claude -p
 hanging when spawned as a subprocess without explicit stdin (e.g. Python 
subprocess.run
)

Fixed Ctrl+C not working in 
-p
 (print) mode

Fixed 
/btw
 returning the main agent’s output instead of answering the side question when triggered during streaming

Fixed voice mode not activating correctly on startup when 
voiceEnabled: true
 is set

Fixed left/right arrow tab navigation in 
/permissions

Fixed 
CLAUDE_CODE_DISABLE_TERMINAL_TITLE
 not preventing terminal title from being set on startup

Fixed custom status line showing nothing when workspace trust is blocking it

Fixed enterprise users being unable to retry on rate limit (429) errors

Fixed 
SessionEnd
 hooks not firing when using interactive 
/resume
 to switch sessions

Improved startup memory usage by ~18MB across all scenarios

Improved non-streaming API fallback with a 2-minute per-attempt timeout, preventing sessions from hanging indefinitely

CLAUDE_CODE_PLUGIN_SEED_DIR
 now supports multiple seed directories separated by the platform path delimiter (
:
 on Unix, 
;
 on Windows)

[VSCode] Added 
/remote-control
 — bridge your session to claude.ai/code to continue from a browser or phone

[VSCode] Session tabs now get AI-generated titles based on your first message

[VSCode] Fixed the thinking pill showing “Thinking” instead of “Thought for Ns” after a response completes

[VSCode] Fixed missing session diff button when opening sessions from the left sidebar

​

2.1.78

March 17, 2026

Added 
StopFailure
 hook event that fires when the turn ends due to an API error (rate limit, auth failure, etc.)

Added 
${CLAUDE_PLUGIN_DATA}
 variable for plugin persistent state that survives plugin updates; 
/plugin uninstall
 prompts before deleting it

Added 
effort
, 
maxTurns
, and 
disallowedTools
 frontmatter support for plugin-shipped agents

Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach the outer terminal when running inside tmux with 
set -g allow-passthrough on

Response text now streams line-by-line as it’s generated

Fixed 
git log HEAD
 failing with “ambiguous argument” inside sandboxed Bash on Linux, and stub files polluting 
git status
 in the working directory

Fixed 
cc log
 and 
--resume
 silently truncating conversation history on large sessions (>5 MB) that used subagents

Fixed infinite loop when API errors triggered stop hooks that re-fed blocking errors to the model

Fixed 
deny: ["mcp__servername"]
 permission rules not removing MCP server tools before sending to the model, allowing it to see and attempt blocked tools

Fixed 
sandbox.filesystem.allowWrite
 not working with absolute paths (previously required 
//
 prefix)

Fixed 
/sandbox
 Dependencies tab showing Linux prerequisites on macOS instead of macOS-specific info

Security: Fixed silent sandbox disable when 
sandbox.enabled: true
 is set but dependencies are missing — now shows a visible startup warning

Fixed 
.git
, 
.claude
, and other protected directories being writable without a prompt in 
bypassPermissions
 mode

Fixed ctrl+u in normal mode scrolling instead of readline kill-line (ctrl+u/ctrl+d half-page scroll moved to transcript mode only)

Fixed voice mode modifier-combo push-to-talk keybindings (e.g. ctrl+k) requiring a hold instead of activating immediately

Fixed voice mode not working on WSL2 with WSLg (Windows 11); WSL1/Win10 users now get a clear error

Fixed 
--worktree
 flag not loading skills and hooks from the worktree directory

Fixed 
CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS
 and 
includeGitInstructions
 setting not suppressing the git status section in the system prompt

Fixed Bash tool not finding Homebrew and other PATH-dependent binaries when VS Code is launched from Dock/Spotlight

Fixed washed-out Claude orange color in VS Code/Cursor/code-server terminals that don’t advertise truecolor support

Added 
ANTHROPIC_CUSTOM_MODEL_OPTION
 env var to add a custom entry to the 
/model
 picker, with optional 
_NAME
 and 
_DESCRIPTION
 suffixed vars for display

Fixed 
ANTHROPIC_BETAS
 environment variable being silently ignored when using Haiku models

Fixed queued prompts being concatenated without a newline separator

Improved memory usage and startup time when resuming large sessions

[VSCode] Fixed a brief flash of the login screen when opening the sidebar while already authenticated

[VSCode] Fixed “API Error: Rate limit reached” when selecting Opus — model dropdown no longer offers 1M context variant to subscribers whose plan tier is unknown

​

2.1.77

March 17, 2026

Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens, and the upper bound for Opus 4.6 and Sonnet 4.6 models to 128k tokens

Added 
allowRead
 sandbox filesystem setting to re-allow read access within 
denyRead
 regions

/copy
 now accepts an optional index: 
/copy N
 copies the Nth-latest assistant response

Fixed “Always Allow” on compound bash commands (e.g. 
cd src && npm test
) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts

Fixed auto-updater starting overlapping binary downloads when the slash-command overlay repeatedly opened and closed, accumulating tens of gigabytes of memory

Fixed 
--resume
 silently truncating recent conversation history due to a race between memory-extraction writes and the main transcript

Fixed PreToolUse hooks returning 
"allow"
 bypassing 
deny
 permission rules, including enterprise managed settings

Fixed Write tool silently converting line endings when overwriting CRLF files or creating files in CRLF directories

Fixed memory growth in long-running sessions from progress messages surviving compaction

Fixed cost and to
