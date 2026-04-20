---
source_url: https://ai-sdk.dev/docs/reference/ai-sdk-core/extract-json-middleware
captured: 2026-04-13
source_type: official-docs
project: Vercel AI SDK
---

# AI SDK Core: extractJsonMiddleware()

Source: Vercel AI SDK official documentation, v6 latest.

This source note was collected to resolve an empty/unlinked placeholder created from `/docs/reference/ai-sdk-core/extract-json-middleware` in the AI SDK docs navigation.

Key facts from the official page:

- `extractJsonMiddleware` is imported from the `ai` package.
- It is a language-model middleware used with `wrapLanguageModel`.
- The middleware extracts JSON from text content by removing markdown code fences and related formatting.
- The primary use case is structured output via `Output.object()` when a model wraps JSON in markdown code blocks such as fenced `json` blocks.
- The optional `transform?: (text: string) => string` parameter lets callers replace the default code-fence stripping with a custom text transformation.
- The return value is middleware that can process both streaming and non-streaming responses.
- For non-streaming `generateText`, it receives the complete model response, applies the transform, and returns cleaned text.
- For streaming `streamText`, it buffers the initial content to detect a markdown fence prefix, switches to streaming after detection, keeps a small suffix buffer for the closing fence, and strips trailing fence text at stream end.
- For custom transforms in streaming mode, it buffers all content and applies the transform at the end.

Local wiki ingest decision:

- category: tooling
- page_type: project-internal
- project: Vercel AI SDK
- Rationale: this is not a source-agnostic JSON extraction concept page; it is a specific API reference page for the AI SDK Core package.
