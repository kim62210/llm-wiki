# Running Gemma 4 as a Local Model in Codex CLI

Sources:
- https://medium.com/google-cloud/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4
- https://news.ycombinator.com/item?id=47744255
- https://ollama.com/library/gemma4
Fetched: 2026-04-16

## Overview

Google's Gemma 4 (April 2026) is the first open-weights model family where local tool calling works well enough to drive the Codex CLI harness end to end. The flagship 31B Dense scores 86.4% on tau2-bench--up from Gemma 3's 6.6%.

## Setup Approaches

### 1. llama.cpp (Recommended for Apple Silicon)
Use `codex --oss -m gemma4:31b`. On NVIDIA GB10, Ollama v0.20.5 was the first path that worked reliably.

### 2. Ollama (with limitations)
As of April 2026, Ollama's Gemma 4 tool-call parser is unreliable. Streaming drops tool calls--in streaming mode, tool call content gets incorrectly routed into the reasoning field rather than the tool_calls array.

## Configuration Gotchas

- Set `stream_idle_timeout_ms` to at least 1,800,000 in provider config
- Benchmarks taken with ggml 0.9.11 (Homebrew build 8680)
- 3.3x regression between build b8680 and later master builds: M4 generation dropped from ~27 tok/s to ~8 tok/s on base M4

## Model Variants

- **31B Dense**: Full capability, requires more VRAM
- **26B MoE** (sweet spot for local dev): Only 3.8B active parameters, runs on 32GB Apple Silicon Mac via Metal offloading, delivers 97% of 31B Dense's agentic capability

## Key Insights

- First open-weight model viable for agentic harness use
- Cost and privacy advantages over cloud alternatives
- Local tool calling maturity is the key breakthrough
- MoE variant makes consumer hardware viable
