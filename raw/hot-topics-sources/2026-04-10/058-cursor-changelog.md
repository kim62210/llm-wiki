---
title: Changelog · Cursor
source_url: https://cursor.com/changelog
final_url: https://cursor.com/changelog
status: 200
content_type: text/html; charset=utf-8
topics: [Cursor Cloud Agents & Parallel Worktree Agents]
sections: [Harness Engineering]
fetched_at: 2026-04-10T01:43:33.135514+00:00
---

# Changelog · Cursor

## 원본 URL

https://cursor.com/changelog

## 추출 본문

Changelog · Cursor

Skip to content
Cursor

Product↓

Agents

Code Review

Cloud ↗

Tab

CLI

Marketplace ↗

Enterprise

Pricing

Resources↓

Changelog

Blog

Docs

Community

Help ↗

Workshops

Forum ↗

Careers

Product →

Enterprise

Pricing

Resources →

Sign inContactContact salesDownload

Changelog

Apr 8, 2026 · Changelog

Bugbot Learned Rules and MCP Support

This release introduces updates to Bugbot including the ability to self-improve in real time, MCP support, improvements to Bugbot Autofix, and the highest resolution rate to date.

#Bugbot Learned Rules

Bugbot can now learn from feedback on pull requests and turn those signals into learned rules that improve future reviews.

It looks at reactions and replies to Bugbot comments and comments from human reviewers to create candidate rules. Bugbot automatically promotes the ones that accumulate signal and disables the ones that stop being useful.

Read more about learned rules in our announcement or manage learning in the Bugbot dashboard.

#Bugbot MCP Support

Give Bugbot access to MCP servers for additional context during code reviews. On Teams and Enterprise plans, you can add tools to Bugbot in the Bugbot dashboard.

Bugbot Improvements (6)↓↑

Bugbot's resolution rate is now 78%.

Added a "Fix All" action to apply multiple Bugbot fixes in one operation.

Redesigned Bugbot settings, and split personal and team settings into clearer sections.

Bugbot Autofix only runs when findings are substantial enough to warrant a fix.

Bugbot Autofix now uses only relevant rules, reducing noise in prompting.

Improved reliability of Bugbot Autofix CI checks on PRs.

Simplified Bugbot check progress messages in GitHub PRs.

Bugbot Bug Fixes (2)↓↑

Fixed a bug where stale privacy mode state from inactive teams could incorrectly block Bugbot Autofix.

Fixed infra issues that caused longer than expected Bugbot run times.

3.0Apr 2, 2026 · Changelog

New Cursor Interface

Cursor 3 is now available.

#Agents Window

The new Cursor interface allows you to run many agents in parallel across repos and environments: locally, in worktrees, in the cloud, and on remote SSH.

It's simpler, more powerful, and centered around agents, while keeping the depth of a development environment.

To try the Agents Window, upgrade Cursor and type 
Cmd+Shift+P -> Agents Window
.

You can switch back to the IDE anytime, or have both open simultaneously.

Read more in our announcement.

#Design Mode

In the Agents Window, you can use Design Mode to annotate and target UI elements directly in the browser.

This allows you to give more precise feedback and iterate faster by pointing the agent to exactly the part of the interface you're referring to.

Keyboard shortcuts include:

⌘ + Shift + D to toggle to Design Mode

Shift + drag to select an area

⌘ + L to add element to chat

⌥ + click to add element to input

#Agent Tabs in the Editor

Agent Tabs allow you to view multiple chats at once, side-by-side or in a grid.

Editor (4)↓↑

Added a new command 
/worktree
 that creates a separate git worktree so changes happen in isolation.

Added a new command 
/best-of-n
 that runs the same task in parallel across multiple models, each in its own isolated worktree, then compares outcomes.

Deprecated the previous worktree and best-of-n selection from the Editor.

Removed cloud agents from the Editor.

Plugins & MCP (2)↓↑

MCP Apps now support structured content, enabling richer tool outputs.

Third-party plugin imports now default to off for Enterprises when unset, while preserving explicit Admin overrides.

Enterprise & Teams (3)↓↑

Added the directory group name so audit logs are human-readable without looking up IDs.

Added a team-level Admin setting for cloud agents that restricts creating, editing, and deleting team secrets to Admins.

Added an Enterprise Admin control for disabling "Made with Cursor" code attribution for the entire team. Per-user settings still exist via Cursor Settings > Agent > Attribution.

Other Improvements (10)↓↑

Large-file diff rendering is now much faster, smoother, and less memory-heavy.

Agents are now better at monitoring long-running jobs.

Added an 
Await
 tool that lets agents wait for background shell commands and subagents to complete, or wait for specific output such as "Ready" or "Error".

Reduced the browser automation tool surface and tightened the subagent to use browser tools only, helping it stay more focused on the task. Also improved the browser instructions to reduce error loops, and added screenshot-based coordinate clicking as a fallback when DOM interactions are unreliable.

Plans are now included in shared chats alongside the transcript.

Added caching to improve Explorer subagents startup time.

Past chat transcripts are now surfaced directly in at-mention search results.

Added a "scroll to bottom" button in the agent panel that appears when content overflows.

Tab bar can now span the full available width in maximized chat layouts.

Consolidated the Early Access release track behind Nightly.

Bug Fixes (8)↓↑

Fixed text area behavior for Network Access Controls so pressing 
Enter
 can reliably add a newline at the end of the input.

Fixed hooks loading so multi-root workspaces read project hook files from all workspace folders instead of only the first one.

Fixed a markdown parsing bug where parenthesized HTTP(S) links could be misread as citations.

Fixed todo card visibility to prevent them from disappearing after all todos complete.

Fixed Agent queued prompts that were not resuming automatically after editing operations.

Fixed picker behavior for models that are disabled but selectable by removing misleading "not allowed" styling and auto-enabling a model when the user selects it.

Fixed a bug where expanding/collapsing thinking blocks didn't work while streaming was still in progress.

Fixed a bug where Shift+Enter line breaks weren't treated as multiline content, so the prompt input field could stay in an incorrect state.

Mar 25, 2026 · Changelog

Self-hosted Cloud Agents

Cursor now supports self-hosted cloud agents that keep your code and tool execution entirely in your own network.

Your codebase, build outputs, and secrets all stay on internal machines running in your infrastructure, while the agent handles tool calls locally.

Self-hosted cloud agents offer the same capabilities as Cursor-hosted cloud agents, including isolated VMs, full development environments, multi-model harnesses, plugins, and more.

Try it out today by enabling self-hosted cloud agents in your Cursor Dashboard. Read more in our announcement.

Mar 19, 2026 · Changelog

Composer 2

Composer 2 is now available in Cursor: frontier-level coding performance with strong results on challenging coding tasks.

Standard: $0.50/M input, $2.50/M output tokens

Fast (default): $1.50/M input, $7.50/M output tokens

Read more in our announcement.

Mar 11, 2026 · Changelog

New Plugins on the Cursor Marketplace

We've added more than 30 new plugins from partners such as Atlassian, Datadog, GitLab, Glean, Hugging Face, monday.com, and PlanetScale. Cursor can now read from, write to, and take actions across more of your stack.

Most plugins contain MCPs that cloud agents can use when kicked off manually or triggered automatically through automations.

Try out the new plugins at cursor.com/marketplace, or read more in our announcement.

Next →Older posts

Product

Agents

Enterprise

Pricing

Code Review

Tab

CLI

Cloud Agents

Marketplace ↗

Resources

Download

Changelog

Docs

Learn ↗

Forum ↗

Help ↗

Workshops

Status ↗

Company

Careers

Blog

Community

Students

Brand

Future

Anysphere ↗

Legal

Terms of Service

Privacy Policy

Data Use

Security

Connect

X ↗

LinkedIn ↗

YouTube ↗

© 2026Anysphere, Inc.🛡SOC 2 Certified

🌐English↓

English✓

简体中文

日本語

繁體中文

Español

Français

Português

한국어

Deutsch

Skip to content
Cursor

Product↓

Agents

Code Review

Cloud ↗

Tab

CLI

Marketplace ↗

Enterprise

Pricing

Resources↓

Changelog

Blog

Docs

Community

Help ↗

Workshops

Forum ↗

Careers

Product →

Enterprise

Pricing

Resources →

Sign inContactContact salesDownload

Changelog

Apr 8, 2026 · Changelog

Bugbot Learned Rules and MCP Support

This release introduces updates to Bugbot including the ability to self-improve in real time, MCP support, improvements to Bugbot Autofix, and the highest resolution rate to date.

#Bugbot Learned Rules

Bugbot can now learn from feedback on pull requests and turn those signals into learned rules that improve future reviews.

It looks at reactions and replies to Bugbot comments and comments from human reviewers to create candidate rules. Bugbot automatically promotes the ones that accumulate signal and disables the ones that stop being useful.

Read more about learned rules in our announcement or manage learning in the Bugbot dashboard.

#Bugbot MCP Support

Give Bugbot access to MCP servers for additional context during code reviews. On Teams and Enterprise plans, you can add tools to Bugbot in the Bugbot dashboard.

Bugbot Improvements (6)↓↑

Bugbot's resolution rate is now 78%.

Added a "Fix All" action to apply multiple Bugbot fixes in one operation.

Redesigned Bugbot settings, and split personal and team settings into clearer sections.

Bugbot Autofix only runs when findings are substantial enough to warrant a fix.

Bugbot Autofix now uses only relevant rules, reducing noise in prompting.

Improved reliability of Bugbot Autofix CI checks on PRs.

Simplified Bugbot check progress messages in GitHub PRs.

Bugbot Bug Fixes (2)↓↑

Fixed a bug where stale privacy mode state from inactive teams could incorrectly block Bugbot Autofix.

Fixed infra issues that caused longer than expected Bugbot run times.

3.0Apr 2, 2026 · Changelog

New Cursor Interface

Cursor 3 is now available.

#Agents Window

The new Cursor interface allows you to run many agents in parallel across repos and environments: locally, in worktrees, in the cloud, and on remote SSH.

It's simpler, more powerful, and centered around agents, while keeping the depth of a development environment.

To try the Agents Window, upgrade Cursor and type 
Cmd+Shift+P -> Agents Window
.

You can switch back to the IDE anytime, or have both open simultaneously.

Read more in our announcement.

#Design Mode

In the Agents Window, you can use Design Mode to annotate and target UI elements directly in the browser.

This allows you to give more precise feedback and iterate faster by pointing the agent to exactly the part of the interface you're referring to.

Keyboard shortcuts include:

⌘ + Shift + D to toggle to Design Mode

Shift + drag to select an area

⌘ + L to add element to chat

⌥ + click to add element to input

#Agent Tabs in the Editor

Agent Tabs allow you to view multiple chats at once, side-by-side or in a grid.

Editor (4)↓↑

Added a new command 
/worktree
 that creates a separate git worktree so changes happen in isolation.

Added a new command 
/best-of-n
 that runs the same task in parallel across multiple models, each in its own isolated worktree, then compares outcomes.

Deprecated the previous worktree and best-of-n selection from the Editor.

Removed cloud agents from the Editor.

Plugins & MCP (2)↓↑

MCP Apps now support structured content, enabling richer tool outputs.

Third-party plugin imports now default to off for Enterprises when unset, while preserving explicit Admin overrides.

Enterprise & Teams (3)↓↑

Added the directory group name so audit logs are human-readable without looking up IDs.

Added a team-level Admin setting for cloud agents that restricts creating, editing, and deleting team secrets to Admins.

Added an Enterprise Admin control for disabling "Made with Cursor" code attribution for the entire team. Per-user settings still exist via Cursor Settings > Agent > Attribution.

Other Improvements (10)↓↑

Large-file diff rendering is now much faster, smoother, and less memory-heavy.

Agents are now better at monitoring long-running jobs.

Added an 
Await
 tool that lets agents wait for background shell commands and subagents to complete, or wait for specific output such as "Ready" or "Error".

Reduced the browser automation tool surface and tightened the subagent to use browser tools only, helping it stay more focused on the task. Also improved the browser instructions to reduce error loops, and added screenshot-based coordinate clicking as a fallback when DOM interactions are unreliable.

Plans are now included in shared chats alongside the transcript.

Added caching to improve Explorer subagents startup time.

Past chat transcripts are now surfaced directly in at-mention search results.

Added a "scroll to bottom" button in the agent panel that appears when content overflows.

Tab bar can now span the full available width in maximized chat layouts.

Consolidated the Early Access release track behind Nightly.

Bug Fixes (8)↓↑

Fixed text area behavior for Network Access Controls so pressing 
Enter
 can reliably add a newline at the end of the input.

Fixed hooks loading so multi-root workspaces read project hook files from all workspace folders instead of only the first one.

Fixed a markdown parsing bug where parenthesized HTTP(S) links could be misread as citations.

Fixed todo card visibility to prevent them from disappearing after all todos complete.

Fixed Agent queued prompts that were not resuming automatically after editing operations.

Fixed picker behavior for models that are disabled but selectable by removing misleading "not allowed" styling and auto-enabling a model when the user selects it.

Fixed a bug where expanding/collapsing thinking blocks didn't work while streaming was still in progress.

Fixed a bug where Shift+Enter line breaks weren't treated as multiline content, so the prompt input field could stay in an incorrect state.

Mar 25, 2026 · Changelog

Self-hosted Cloud Agents

Cursor now supports self-hosted cloud agents that keep your code and tool execution entirely in your own network.

Your codebase, build outputs, and secrets all stay on internal machines running in your infrastructure, while the agent handles tool calls locally.

Self-hosted cloud agents offer the same capabilities as Cursor-hosted cloud agents, including isolated VMs, full development environments, multi-model harnesses, plugins, and more.

Try it out today by enabling self-hosted cloud agents in your Cursor Dashboard. Read more in our announcement.

Mar 19, 2026 · Changelog

Composer 2

Composer 2 is now available in Cursor: frontier-level coding performance with strong results on challenging coding tasks.

Standard: $0.50/M input, $2.50/M output tokens

Fast (default): $1.50/M input, $7.50/M output tokens

Read more in our announcement.

Mar 11, 2026 · Changelog

New Plugins on the Cursor Marketplace

We've added more than 30 new plugins from partners such as Atlassian, Datadog, GitLab, Glean, Hugging Face, monday.com, and PlanetScale. Cursor can now read from, write to, and take actions across more of your stack.

Most plugins contain MCPs that cloud agents can use when kicked off manually or triggered automatically through automations.

Try out the new plugins at cursor.com/marketplace, or read more in our announcement.

Next →Older posts

Product

Agents

Enterprise

Pricing

Code Review

Tab

CLI

Cloud Agents

Marketplace ↗

Resources

Download

Changelog

Docs

Learn ↗

Forum ↗

Help ↗

Workshops

Status ↗

Company

Careers

Blog

Community

Students

Brand

Future

Anysphere ↗

Legal

Terms of Service

Privacy Policy

Data Use

Security

Connect

X ↗

LinkedIn ↗

YouTube ↗

© 2026Anysphere, Inc.🛡SOC 2 Certified

🌐English↓

English✓

简体中文

日本語

繁體中文

Español

Français

Português

한국어

Deutsch
