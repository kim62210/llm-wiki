---
title: What is BAML? | Boundary Documentation
source_url: https://docs.boundaryml.com/guide/introduction/what-is-baml
final_url: https://docs.boundaryml.com/guide/introduction/what-is-baml
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:49:51.282017+00:00
---

# What is BAML? | Boundary Documentation

## 원본 URL

https://docs.boundaryml.com/guide/introduction/what-is-baml

## 주요 헤딩

- What is BAML?

## 추출 본문

Home Guide Examples BAML Reference Playground Agents.md Changelog
Introduction
What is BAML?
Why BAML?
What's the baml_src folder
What's baml_client
Installation: Editors
VSCode Extension
Cursor Extension
JetBrains IDEs
Zed
Claude Code
Others
Installation: Language
Python
Typescript
Go
Ruby
Rust
REST API (other languages)
Elixir
Framework Integration
React/Next.js
Development
Environment Variables
Terminal Logs
Upgrade BAML versions
Deploying
BAML Basics
Prompting with BAML
Switching LLMs
Testing functions
Streaming
Multi-Modal (Images / Audio)
Error Handling
Configuring Timeouts
Concurrent Calls
AbortSignal / Cancellation
BAML Advanced
Collector (track tokens)
LLM Client Registry
Dynamic Types
Reusing Prompt Snippets
Prompt Caching / Message Role Metadata
Checks and Asserts
Modular API
Prompt Optimization
Boundary Cloud
Observability
Comparisons
BAML vs Langchain
BAML vs Marvin
BAML vs Ai-SDK
BAML vs OpenAI SDK
BAML vs Pydantic
Contact
Help on Discord
Light
On this page
Demo video
Examples
High-level Developer Flow
Introduction
What is BAML?
Copy page
The best way to understand BAML and its developer experience is to see it live in a demo (see below).
Demo video
Here we write a BAML function definition, and then call it from a Python script.
Examples
Interactive NextJS app with streaming
Starter boilerplates for Python, Typescript, Ruby, etc.
High-level Developer Flow
1 Write a BAML function definition
main.baml
1 class WeatherAPI { 2 city string @description("the user's city") 3 timeOfDay string @description("As an ISO8601 timestamp") 4 } 5 6 function UseTool(user_message: string) -> WeatherAPI { 7 client "openai-responses/gpt-5-mini" 8 prompt #" 9 Extract.... {# we will explain the rest in the guides #} 10 "# 11 }
Here you can run tests in the VSCode Playground.
2 Generate baml_client
from those .baml files.
This is auto-generated code with all boilerplate to call the LLM endpoint, parse the output, fix broken JSON, and handle errors.
3 Call your function in any language
with type-safety, autocomplete, retry-logic, robust JSON parsing, etc..
Python TypeScript Go Ruby Other Languages
1 import asyncio 2 from baml_client import b 3 from baml_client.types import WeatherAPI 4 5 def main(): 6 weather_info = b.UseTool("What's the weather like in San Francisco?") 7 print(weather_info) 8 assert isinstance(weather_info, WeatherAPI) 9 print(f"City: {weather_info.city}") 10 print(f"Time of Day: {weather_info.timeOfDay}") 11 12 if __name__ == '__main__': 13 main()
Continue on to the Installation Guides for your language to setup BAML in a few minutes!
You don’t need to migrate 100% of your LLM code to BAML in one go! It works along-side any existing LLM framework.
Was this page helpful? Yes No
Edit this page
Why BAML?
Next Built with
