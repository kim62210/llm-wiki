# Claude Code Routines

Source: https://code.claude.com/docs/en/routines
Fetched: 2026-04-16

## Overview

A routine is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically. Routines execute on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed.

## Trigger Types

- **Scheduled**: run on a recurring cadence like hourly, nightly, or weekly
- **API**: trigger on demand by sending an HTTP POST to a per-routine endpoint with a bearer token
- **GitHub**: run automatically in response to repository events such as pull requests or releases

A single routine can combine triggers.

## Example Use Cases

- **Backlog maintenance**: Schedule trigger reads issues, applies labels, assigns owners, posts Slack summary
- **Alert triage**: API endpoint called by monitoring tool, correlates with recent commits, opens draft PR
- **Bespoke code review**: GitHub trigger on PR opened, applies team review checklist, leaves inline comments
- **Deploy verification**: API endpoint after production deploy, runs smoke checks, scans error logs
- **Docs drift**: Weekly schedule scans merged PRs, flags stale docs, opens update PRs
- **Library port**: GitHub trigger on merged PR, ports change to parallel SDK, opens matching PR

## Creation Methods

1. Web UI at claude.ai/code/routines
2. CLI with `/schedule` command
3. Desktop app via Schedule page > New remote task

## Configuration

- **Repositories**: Cloned at run start from default branch. Claude creates `claude/`-prefixed branches.
- **Environments**: Control network access, env vars, setup scripts
- **Connectors**: MCP connectors for external services (Slack, Linear, Google Drive)
- **Branch permissions**: Default limited to `claude/` prefix, configurable

## Trigger Details

### Schedule
- Presets: hourly, daily, weekdays, weekly
- Custom cron via `/schedule update` (minimum 1 hour)
- Times in local timezone, auto-converted

### API
- Per-routine HTTP endpoint with bearer token
- POST with optional `text` field for context
- Returns session ID and URL
- Beta header: `experimental-cc-routine-2026-04-01`

### GitHub
- Events: Pull request (opened, closed, assigned, labeled, etc.), Release
- PR filters: Author, Title, Body, Base/Head branch, Labels, Draft, Merged, Fork
- Each matching event starts a new session

## Availability

Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled.
Daily run cap per account. Extra usage available on metered overage.
