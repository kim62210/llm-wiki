---
title: Leaf Quality Web Research Notes
captured: 2026-04-13
source_type: web-research-notes
---

# Leaf Quality Web Research Notes

This note records the web/official-documentation checks used during the 2026-04-13 leaf-node quality repair pass. It is an audit/support source rather than a source for a single wiki concept page.

Checked official/current documentation URLs:

- BAML official documentation: https://docs.boundaryml.com/guide/introduction/what-is-baml
- Mastra documentation entrypoint checked via existing raw source family: https://mastra.ai/docs
- Vercel AI SDK Agents overview: https://ai-sdk.dev/docs/agents/overview
- Vercel AI SDK Core overview: https://ai-sdk.dev/docs/ai-sdk-core/overview
- Vercel AI SDK Tool Calling: https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling
- Vercel AI SDK MCP Tools: https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools
- Pydantic AI Agent core concepts: https://pydantic.dev/docs/ai/core-concepts/agent/
- LangGraph durable execution was searched as an official-docs validation target for the existing LangGraph raw snapshot family.

Local ingest decision:

- This file should not be added to every page's `sources:` list because it is a pass-level audit note, not the original source for each page.
- Individual wiki pages continue to cite their existing raw snapshots, which preserve the concrete official/blog/paper source used for that page.
- The web research pass confirmed that the repeated low-quality sections should be replaced by source-specific notes tied to each page's own raw source paths and URLs.
