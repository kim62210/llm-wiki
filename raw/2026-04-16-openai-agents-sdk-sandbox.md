# OpenAI Agents SDK: Sandbox Evolution

Sources:
- https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/
- https://thenewstack.io/openai-agents-sdk-sandboxes/
Fetched: 2026-04-16

## Overview

OpenAI announced a major update to its Agents SDK that transforms it from a bare-bones framework into a production-ready agent platform. The key innovation separates the agent orchestration layer (harness) from the compute environment (sandbox) where agents execute tasks.

## Architecture: Harness vs Compute

- **Harness layer**: Manages orchestration, decision-making, API interactions, instructions, tools, approvals, tracing, handoffs, resume bookkeeping
- **Compute layer**: Executes tool calls and code in unprivileged, isolated environments

Steve Coffey (tech lead for Responses API): "Now we have models that can kind of work for hours at a time or days or weeks."

## How Sandboxes Work

Sandboxes provide controlled workspaces where agents operate independently from the main application harness. Agents can operate in a single sandbox or spawn additional sandboxes. Sub-agents can run in isolated environments, enabling hierarchical architectures.

Sandboxes can be implemented as containers or virtual machines. Typical deployment:
- Agent harness as a Temporal job
- Agent compute in a Modal sandbox or Docker container
- Complete isolation between harness and execution environments

## Sandbox Provider Ecosystem

- Blaxel
- Cloudflare
- Daytona
- E2B
- Modal
- Runloop
- Vercel

Also introduces a Manifest abstraction for portable workspace descriptions.

## File System and Data Access

Sandboxes support mounted data sources:
- Local files
- AWS S3 buckets
- Google Cloud Storage
- Azure Blob Storage
- Cloudflare R2

Agents can work with text files, images, and PDFs. Container snapshotting and file system preservation across restarts supported.

## Security Model

- Sandboxes run unprivileged without API keys or secrets
- Network isolation prevents unauthorized egress
- De-approved environments ensure agents cannot access sensitive infrastructure
- Enterprise: strict isolation; Individual: fewer restrictions

## Key Details

- Python first, TypeScript support planned for later
- No additional cost for SDK itself--standard API pricing
- Pre-1.0 status but substantial maturation
- Configurable memory, file support, document handling included

Karan Sharma (OpenAI product): enables users to "go build these long-horizon agents using our harness and with whatever infrastructure they have."
