---
source_url: https://ai-sdk.dev/docs/troubleshooting/typescript-cannot-find-namespace-jsx
captured: 2026-04-13
source_type: official-docs
project: Vercel AI SDK
---

# AI SDK Troubleshooting: TypeScript error "Cannot find namespace 'JSX'"

Source: Vercel AI SDK official documentation, v6 latest.

This source note was collected to resolve an empty/unlinked placeholder created from `/docs/troubleshooting/typescript-cannot-find-namespace-jsx` in the AI SDK docs navigation.

Key facts from the official page:

- The documented issue is TypeScript error TS2503: `Cannot find namespace 'JSX'`.
- The example environment is a non-React project that uses the AI SDK, for example an Hono server.
- The background given by the official page is that the AI SDK has a dependency on `@types/react`, which defines the `JSX` namespace.
- The page notes that this dependency is intended to be removed in the next major version of the AI SDK.
- The documented solution is to install `@types/react` as a dependency.
- The package-manager example is `npm install @types/react`.

Local wiki ingest decision:

- category: tooling
- page_type: project-internal
- project: Vercel AI SDK
- Rationale: this is a product-specific troubleshooting note for AI SDK TypeScript dependency behavior, not a general TypeScript concept page.
