---
title: How Instructor Patches LLM Clients - Instructor
source_url: https://python.useinstructor.com/concepts/patching/
final_url: https://python.useinstructor.com/concepts/patching/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T06:17:50.461242+00:00
---

# How Instructor Patches LLM Clients - Instructor

## 원본 URL

https://python.useinstructor.com/concepts/patching/

## 주요 헤딩

- Patching ¶
- What is Patching? ¶
- How Patching Works ¶
- Patching Modes ¶
- Default Modes by Provider ¶
- Manual Patching (Advanced) ¶
- What Gets Patched? ¶
- Provider-Specific Considerations ¶
- When to Use Manual Patching ¶
- Related Documentation ¶

## 추출 본문

Instructor
instructor
Introduction
Learning
Integrations
Cookbook
Concepts
Concepts Error Handling
Retrying
Fields
Models
Parallel Tools
Templating
Lists and Arrays
Prompting
Citations
Multimodal
Patching Patching Table of contents What is Patching?
How Patching Works
Patching Modes Tool Calling (TOOLS)
JSON Mode
Markdown JSON (MD_JSON)
Default Modes by Provider
Manual Patching (Advanced)
What Gets Patched? New Parameters
Enhanced Methods
Provider-Specific Considerations OpenAI
Anthropic
Google Gemini
Ollama (Local Models)
When to Use Manual Patching
Related Documentation
from_provider
Migration Guide
Mode Migration
Hooks
Types
TypedDicts
Validators
Usage Tokens
Missing
Stream Iterable
Stream Partial
Raw Response
FastAPI
Caching
Prompt Caching
Logging
Distillation
Dictionary Operations
Union
Unions
Validation
Semantic Validation
Alias
Enums
Type Adapter
Prompt Engineering
CLI Reference
Find Jobs (External)
Blog
Table of contents What is Patching?
How Patching Works
Patching Modes Tool Calling (TOOLS)
JSON Mode
Markdown JSON (MD_JSON)
Default Modes by Provider
Manual Patching (Advanced)
What Gets Patched? New Parameters
Enhanced Methods
Provider-Specific Considerations OpenAI
Anthropic
Google Gemini
Ollama (Local Models)
When to Use Manual Patching
Related Documentation
Patching ¶
Patching adds structured output features to LLM client libraries. This page explains how it works. For most users, from_provider
is simpler than manual patching.
Recommended Approach
Use from_provider
instead of manual patching. It works the same way across all providers. See the Migration Guide if you're using older patching patterns.
What is Patching? ¶
Patching adds new features to LLM client objects without changing their original code. When Instructor patches a client, it adds:
New parameters: response_model
, max_retries
, and context
to completion methods
Validation: Checks responses against Pydantic models
Retry logic: Retries when validation fails
Compatibility: The patched client still works with all original methods
How Patching Works ¶
When Instructor patches a client, it:
Wraps the completion method: Intercepts calls to create()
or chat.completions.create()
Converts schemas: Changes Pydantic models into provider-specific formats (JSON schema, tool definitions, etc.)
Validates responses: Checks LLM outputs against your Pydantic model
Handles retries: Retries with validation feedback if needed
Returns typed objects: Converts validated JSON into Pydantic model instances
Patching Modes ¶
Different providers support different modes for structured extraction. Instructor automatically selects the best mode for each provider, but you can override it:
Tool Calling (TOOLS) ¶
Uses the provider's function/tool calling API. This is the default for OpenAI.
Supported by: OpenAI, Anthropic (ANTHROPIC_TOOLS), Google (GENAI_TOOLS), Ollama (for supported models)
JSON Mode ¶
Instructs the model to return JSON directly. Works with most providers.
Supported by: OpenAI, Anthropic, Google, Ollama, and most providers
Markdown JSON (MD_JSON) ¶
Asks for JSON wrapped in markdown. Only use for specific providers like Databricks.
Supported by: Databricks, some vision models
Default Modes by Provider ¶
Each provider uses a recommended default mode:
OpenAI : Mode.TOOLS
(function calling)
Anthropic : Mode.TOOLS
(tool use)
Google : Mode.TOOLS
(function calling)
Ollama : Mode.TOOLS
(if model supports it) or Mode.JSON
Others : Provider-specific defaults
When using from_provider
, these defaults are applied automatically. You can override them with the mode
parameter.
Manual Patching (Advanced) ¶
If you need to patch a client manually (not recommended for most users):
import openai
import instructor
from pydantic import BaseModel
class YourModel ( BaseModel ):
message : str
# Create the base client
openai_client = openai . OpenAI ()
# Patch it manually
client = instructor . patch ( openai_client , mode = instructor . Mode . TOOLS )
# Now use it
response = client . chat . completions . create (
response_model = YourModel ,
messages = [{ "role" : "user" , "content" : "Say hello" }],
)
However, using from_provider
is simpler and recommended:
import instructor
from pydantic import BaseModel
# Simpler approach
class YourModel ( BaseModel ):
message : str
client = instructor . from_provider ( "openai/gpt-4o-mini" )
_response = client . create (
response_model = YourModel ,
messages = [{ "role" : "user" , "content" : "Say hello" }],
)
What Gets Patched? ¶
Instructor adds these features to patched clients:
New Parameters ¶
response_model
: A Pydantic model or type that defines the expected output structure
max_retries
: Number of retry attempts if validation fails (default: 0)
context
: Additional context for validation hooks
Enhanced Methods ¶
The patched client's create()
method: - Accepts response_model
parameter - Validates responses automatically - Retries on validation failures - Returns typed Pydantic objects instead of raw responses
Provider-Specific Considerations ¶
OpenAI ¶
Default mode: TOOLS
(function calling)
Supports streaming with structured outputs
Anthropic ¶
Default mode: ANTHROPIC_TOOLS
(tool use)
Uses Claude's native tool calling API
Google Gemini ¶
Default mode: GENAI_TOOLS
(function calling)
Requires jsonref
package for tool calling
Some limitations with strict validation and enums
