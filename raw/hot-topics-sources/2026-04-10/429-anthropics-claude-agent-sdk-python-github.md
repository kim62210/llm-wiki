---
title: GitHub - anthropics/claude-agent-sdk-python · GitHub
source_url: https://github.com/anthropics/claude-agent-sdk-python
final_url: https://github.com/anthropics/claude-agent-sdk-python
status: 200
content_type: text/html; charset=utf-8
topics: [Claude Agent SDK (Anthropic)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:26.987985+00:00
---

# GitHub - anthropics/claude-agent-sdk-python · GitHub

## 원본 URL

https://github.com/anthropics/claude-agent-sdk-python

## 추출 본문

GitHub - anthropics/claude-agent-sdk-python · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 anthropics
/claude-agent-sdk-pythonPublic

Notifications
You must be signed in to change notification settings

Fork
 870

 Star
6.2k

Code

Issues90

Pull requests110

Actions

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Security and quality

 Insights

anthropics/claude-agent-sdk-python

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
442 Commits

442 Commits

.claude

.claude

.github/workflows

.github/workflows

e2e-tests

e2e-tests

examples

examples

scripts

scripts

src/claude_agent_sdk

src/claude_agent_sdk

tests

tests

.dockerignore

.dockerignore

.gitignore

.gitignore

CHANGELOG.md

CHANGELOG.md

CLAUDE.md

CLAUDE.md

Dockerfile.test

Dockerfile.test

LICENSE

LICENSE

README.md

README.md

RELEASING.md

RELEASING.md

pyproject.toml

pyproject.toml

View all files

Repository files navigation

README

MIT license

Claude Agent SDK for Python

Python SDK for Claude Agent. See the Claude Agent SDK documentation for more information.

Installation

pip install claude-agent-sdk

Prerequisites:

Python 3.10+

Note: The Claude Code CLI is automatically bundled with the package - no separate installation required! The SDK will use the bundled CLI by default. If you prefer to use a system-wide installation or a specific version, you can:

Install Claude Code separately: 
curl -fsSL https://claude.ai/install.sh | bash

Specify a custom path: 
ClaudeAgentOptions(cli_path="/path/to/claude")

Quick Start

importanyiofromclaude_agent_sdkimportqueryasyncdefmain():
 asyncformessageinquery(prompt="What is 2 + 2?"):
 print(message)

anyio.run(main)

Basic Usage: query()

query()
 is an async function for querying Claude Code. It returns an 
AsyncIterator
 of response messages. See src/claude_agent_sdk/query.py.

fromclaude_agent_sdkimportquery, ClaudeAgentOptions, AssistantMessage, TextBlock# Simple queryasyncformessageinquery(prompt="Hello Claude"):
 ifisinstance(message, AssistantMessage):
 forblockinmessage.content:
 ifisinstance(block, TextBlock):
 print(block.text)

# With optionsoptions=ClaudeAgentOptions(
 system_prompt="You are a helpful assistant",
 max_turns=1
)

asyncformessageinquery(prompt="Tell me a joke", options=options):
 print(message)

Using Tools

By default, Claude has access to the full Claude Code toolset (Read, Write, Edit, Bash, and others). 
allowed_tools
 is a permission allowlist: listed tools are auto-approved, and unlisted tools fall through to 
permission_mode
 and 
can_use_tool
 for a decision. It does not remove tools from Claude's toolset. To block specific tools, use 
disallowed_tools
. See the permissions guide for the full evaluation order.

options=ClaudeAgentOptions(
 allowed_tools=["Read", "Write", "Bash"], # auto-approve these toolspermission_mode='acceptEdits'# auto-accept file edits
)

asyncformessageinquery(
 prompt="Create a hello.py file",
 options=options
):
 # Process tool use and resultspass

Working Directory

frompathlibimportPathoptions=ClaudeAgentOptions(
 cwd="/path/to/project"# or Path("/path/to/project")
)

ClaudeSDKClient

ClaudeSDKClient
 supports bidirectional, interactive conversations with Claude
Code. See src/claude_agent_sdk/client.py.

Unlike 
query()
, 
ClaudeSDKClient
 additionally enables custom tools and hooks, both of which can be defined as Python functions.

Custom Tools (as In-Process SDK MCP Servers)

A custom tool is a Python function that you can offer to Claude, for Claude to invoke as needed.

Custom tools are implemented in-process MCP servers that run directly within your Python application, eliminating the need for separate processes that regular MCP servers require.

For an end-to-end example, see MCP Calculator.

Creating a Simple Tool

fromclaude_agent_sdkimporttool, create_sdk_mcp_server, ClaudeAgentOptions, ClaudeSDKClient# Define a tool using the @tool decorator@tool("greet", "Greet a user", {"name": str})asyncdefgreet_user(args):
 return {
 "content": [
 {"type": "text", "text": f"Hello, {args['name']}!"}
 ]
 }

# Create an SDK MCP serverserver=create_sdk_mcp_server(
 name="my-tools",
 version="1.0.0",
 tools=[greet_user]
)

# Use it with Claude. allowed_tools pre-approves the tool so it runs# without a permission prompt; it does not control tool availability.options=ClaudeAgentOptions(
 mcp_servers={"tools": server},
 allowed_tools=["mcp__tools__greet"]
)

asyncwithClaudeSDKClient(options=options) asclient:
 awaitclient.query("Greet Alice")

 # Extract and print responseasyncformsginclient.receive_response():
 print(msg)

Benefits Over External MCP Servers

No subprocess management - Runs in the same process as your application

Better performance - No IPC overhead for tool calls

Simpler deployment - Single Python process instead of multiple

Easier debugging - All code runs in the same process

Type safety - Direct Python function calls with type hints

Migration from External Servers

# BEFORE: External MCP server (separate process)options=ClaudeAgentOptions(
 mcp_servers={
 "calculator": {
 "type": "stdio",
 "command": "python",
 "args": ["-m", "calculator_server"]
 }
 }
)

# AFTER: SDK MCP server (in-process)frommy_toolsimportadd, subtract# Your tool functionscalculator=create_sdk_mcp_server(
 name="calculator",
 tools=[add, subtract]
)

options=ClaudeAgentOptions(
 mcp_servers={"calculator": calculator}
)

Mixed Server Support

You can use both SDK and external MCP servers together:

options=ClaudeAgentOptions(
 mcp_servers={
 "internal": sdk_server, # In-process SDK server"external": { # External subprocess server"type": "stdio",
 "command": "external-server"
 }
 }
)

Hooks

A hook is a Python function that the Claude Code application (not Claude) invokes at specific points of the Claude agent loop. Hooks can provide deterministic processing and automated feedback for Claude. Read more in Intercept and control agent behavior with hooks.

For more examples, see examples/hooks.py.

Example

fromclaude_agent_sdkimportClaudeAgentOptions, ClaudeSDKClient, HookMatcherasyncdefcheck_bash_command(input_data, tool_use_id, context):
 tool_name=input_data["tool_name"]
 tool_input=input_data["tool_input"]
 iftool_name!="Bash":
 return {}
 command=tool_input.get("command", "")
 block_patterns= ["foo.sh"]
 forpatterninblock_patterns:
 ifpatternincommand:
 return {
 "hookSpecificOutput": {
 "hookEventName": "PreToolUse",
 "permissionDecision": "deny",
 "permissionDecisionReason": f"Command contains invalid pattern: {pattern}",
 }
 }
 return {}

options=ClaudeAgentOptions(
 allowed_tools=["Bash"],
 hooks={
 "PreToolUse": [
 HookMatcher(matcher="Bash", hooks=[check_bash_command]),
 ],
 }
)

asyncwithClaudeSDKClient(options=options) asclient:
 # Test 1: Command with forbidden pattern (will be blocked)awaitclient.query("Run the bash command: ./foo.sh --help")
 asyncformsginclient.receive_response():
 print(msg)

 print("\n"+"="*50+"\n")

 # Test 2: Safe command that should workawaitclient.query("Run the bash command: echo 'Hello from hooks example!'")
 asyncformsginclient.receive_response():
 print(msg)

Types

See src/claude_agent_sdk/types.py for complete type definitions:

ClaudeAgentOptions
 - Configuration options

AssistantMessage
, 
UserMessage
, 
SystemMessage
, 
ResultMessage
 - Message types

TextBlock
, 
ToolUseBlock
, 
ToolResultBlock
 - Content blocks

Error Handling

fromclaude_agent_sdkimport (
 ClaudeSDKError, # Base errorCLINotFoundError, # Claude Code not installedCLIConnectionError, # Connection issuesProcessError, # Process failedCLIJSONDecodeError, # JSON parsing issues
)

try:
 asyncformessageinquery(prompt="Hello"):
 passexceptCLINotFoundError:
 print("Please install Claude Code")
exceptProcessErrorase:
 print(f"Process failed with exit code: {e.exit_code}")
exceptCLIJSONDecodeErrorase:
 print(f"Failed to parse response: {e}")

See src/claude_agent_sdk/_errors.py for all error types.

Available Tools

See the Claude Code documentation for a complete list of available tools.

Examples

See examples/quick_start.py for a complete working example.

See examples/streaming_mode.py for comprehensive examples involving 
ClaudeSDKClient
. You can even run interactive examples in IPython from examples/streaming_mode_ipython.py.

Migrating from Claude Code SDK

If you're upgrading from the Claude Code SDK (versions < 0.1.0), please see the CHANGELOG.md for details on breaking changes and new features, including:

ClaudeCodeOptions
 → 
ClaudeAgentOptions
 rename

Merged system prompt configuration

Settings isolation and explicit control

New programmatic subagents and session forking features

Development

If you're contributing to this project, run the initial setup script to install git hooks:

./scripts/initial-setup.sh

This installs a pre-push hook that runs lint checks before pushing, matching the CI workflow. To skip the hook temporarily, use 
git push --no-verify
.

Building Wheels Locally

To build wheels with the bundled Claude Code CLI:

# Install build dependencies
pip install build twine

# Build wheel with bundled CLI
python scripts/build_wheel.py

# Build with specific version
python scripts/build_wheel.py --version 0.1.4

# Build with specific CLI version
python scripts/build_wheel.py --cli-version 2.0.0

# Clean bundled CLI after building
python scripts/build_wheel.py --clean

# Skip CLI download (use existing)
python scripts/build_wheel.py --skip-download

The build script:

Downloads Claude Code CLI for your platform

Bundles it in the wheel

Builds both wheel and source distribution

Checks the package with twine

See 
python scripts/build_wheel.py --help
 for all options.

Release Workflow

The package is published to PyPI via the GitHub Actions workflow in 
.github/workflows/publish.yml
. To create a new release:

Trigger the workflow manually from the Actions tab with two inputs:

version
: The package version to publish (e.g., 
0.1.5
)

claude_code_version
: The Claude Code CLI version to bundle (e.g., 
2.0.0
 or 
latest
)

The workflow will:

Build platform-specific wheels for macOS, Linux, and Windows

Bundle the specified Claude Code CLI version in each wheel

Build a source distribution

Publish all artifacts to PyPI

Create a release branch with version updates

Open a PR to main with:

Updated 
pyproject.toml
 version

Updated 
src/claude_agent_sdk/_version.py

Updated 
src/claude_agent_sdk/_cli_version.py
 with bundled CLI version

Auto-generated 
CHANGELOG.md
 entry

Review and merge the release PR to update main with the new version information

The workflow tracks both the package version and the bundled CLI version separately, allowing you to release a new package version with an updated CLI without code changes.

License and terms

Use of this SDK is governed by Anthropic's Commercial Terms of Service, including when you use it to power products and services that you make available to your own customers and end users, except to the extent a specific component or dependency is covered by a different license as indicated in that component's LICENSE file.

About

 No description, website, or topics provided.
 

Resources

 Readme

License

 MIT license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

6.2k
 stars

Watchers

45
 watching

Forks

870
 forks

 Report repository

Releases
 65

v0.1.58
 Latest

Apr 9, 2026

+ 64 releases

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python99.5%

Shell0.5%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.
