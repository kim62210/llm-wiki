---
title: Tool Invocation - Phoenix
source_url: https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation
final_url: https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation
status: 200
content_type: text/html; charset=utf-8
topics: [Tool Selection & Tool Invocation Evaluators]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:59.256796+00:00
---

# Tool Invocation - Phoenix

## 원본 URL

https://arize.com/docs/phoenix/evaluation/pre-built-metrics/tool-invocation

## 추출 본문

Tool Invocation - Phoenix

Skip to main content

Phoenix home page

Search...

⌘KAsk AI

Phoenix Cloud

Phoenix Cloud

Search...

Navigation

Pre-Built Metrics

Tool Invocation

Documentation

Integrations

SDK & API Reference

Self-Hosting

Phoenix Cloud

Cookbooks

Release Notes

What is Arize Phoenix?

Get Started

Quick Start

Coding Agents

End to End Features Notebook

Phoenix Demo

Tracing

Tutorial

Overview: Tracing

How-to: Tracing

Evaluation

Tutorial

Overview

LLM as a Judge

Client-Side Evals (SDK)

Overview

LLM Evaluators

Code Evaluators

Batch Evaluations

Using Evals with Phoenix

Pre-Built Metrics

Overview

Faithfulness

Conciseness

Correctness

Document Relevance

Tool Selection

Tool Invocation

Tool Response Handling

Refusal

Exact Match

Matches Regex

Precision / Recall / F-Score

Legacy

Server-Side Evals (UI)

Datasets & Experiments

Tutorial

Overview: Datasets & Experiments

How-to: Datasets

How-to: Experiments

Prompts

Tutorial

Overview: Prompts

How to: Prompts

Settings

Access Control (RBAC)

API Keys

Data Retention

Custom AI Providers

Concepts

User Guide

Production Guide

Environments

Tracing

Prompts

Datasets & Experiments

Resources

Frequently Asked Questions

Contribute to Phoenix

Phoenix to Arize AX Migration

TypeScript SDK

Python SDK

Github

OpenInference

On this page

Overview

When to Use

Supported Levels

Input Requirements

Formatting Tips

Output Interpretation

Usage Examples

Using Input Mapping

Configuration

Viewing and Modifying the Prompt

Using with Phoenix

Evaluating Traces

Running Experiments

API Reference

Related

Pre-Built Metrics

Tool Invocation

Copy page

Evaluate whether LLM tool calls have correct arguments and formatting

Copy page

​

Overview
The Tool Invocation evaluator determines whether an LLM invoked a tool correctly with proper arguments, formatting, and safe content. This evaluator focuses on the how of tool calling - validating that the invocation itself is well-formed - rather than whether the right tool was selected.

​

When to Use
Use the Tool Invocation evaluator when you need to:
Validate tool call arguments - Ensure all required parameters are present with correct values

Check JSON formatting - Verify tool calls are properly structured

Detect hallucinated fields - Identify when the LLM invents parameters not in the schema

Audit for unsafe content - Check that arguments don’t contain PII or sensitive data

Evaluate multi-tool invocations - Validate when the LLM calls multiple tools at once

This evaluator validates tool invocation correctness, not tool selection. For evaluating whether the right tool was chosen, use the Tool Selection evaluator instead. The two evaluators are complementary — Tool Selection catches wrong-tool errors while Tool Invocation catches malformed-call errors — and are best run together for complete tool-calling coverage.

​

Supported Levels
The level of an evaluator determines the scope of the evaluation in OpenTelemetry terms. Some evaluations are applicable to individual spans, some to full traces or sessions, and some are applicable at multiple levels.

LevelSupportedNotesSpanYesFor LLM spans that contain tool calls. Evaluate individual tool-calling decisions.

Relevant span kinds: Tool spans or LLM spans with tool calls, particularly in agentic applications.

​

Input Requirements
The Tool Invocation evaluator requires three inputs:

FieldTypeDescription
input

string
The conversation context (can include multi-turn history)
available_tools

string
Tool schemas (JSON schema or human-readable format)
tool_selection

string
The LLM’s tool invocation(s) with arguments

In TypeScript, the fields use camelCase: 
availableTools
 and 
toolSelection
.

​

Formatting Tips
While you can pass full JSON representations for each field, human-readable formats typically produce more accurate evaluations.
input
 (conversation context adapted from input 
messages
):

User: I need to book a flight from New York to Los AngelesAssistant: I'd be happy to help you book a flight. When would you like to travel?User: Tomorrow morning, the earliest available

available_tools
 (tool descriptions adapted by JSON schemas):

book_flight: Book a flight between two cities - origin (required): Departure city code (e.g., "JFK", "LAX") - destination (required): Arrival city code - date (required): Flight date in YYYY-MM-DD format - time_preference (optional): "morning", "afternoon", or "evening"search_hotels: Search for hotel accommodations - city (required): City name or code - check_in (required): Check-in date in YYYY-MM-DD format - check_out (required): Check-out date in YYYY-MM-DD format

tool_selection
 (the LLM’s tool invocation adapted from 
tool_calls
 in the output):

book_flight(origin="JFK", destination="LAX", date="2024-01-15", time_preference="morning")

Additional tips:
Include full conversation context - The evaluator considers the entire conversation history to validate argument values

Multi-tool invocations are supported - If the LLM calls multiple tools, include all invocations in the 
tool_selection
 field

​

Output Interpretation
The evaluator returns a 
Score
 object with the following properties:

PropertyValueDescription
label

"correct"
 or 
"incorrect"
Classification result
score

1.0
 or 
0.0
Numeric score (1.0 = correct, 0.0 = incorrect)
explanation

string
LLM-generated reasoning for the classification
direction

"maximize"
Higher scores are better
metadata

object
Additional information such as the model name. When tracing is enabled, includes the 
trace_id
 for the evaluation.

​

Usage Examples

Python

TypeScript

from phoenix.evals import LLMfrom phoenix.evals.metrics import ToolInvocationEvaluator# Initialize the LLM clientllm = LLM(provider="openai", model="gpt-4o")# Create the evaluatortool_invocation_eval = ToolInvocationEvaluator(llm=llm)# Inspect the evaluator's requirementsprint(tool_invocation_eval.describe())# Evaluate a tool invocation using human-readable formateval_input = { "input": """User: I need to book a flight from New York to Los AngelesAssistant: I'd be happy to help you book a flight. When would you like to travel?User: Tomorrow morning, the earliest available""", "available_tools": """book_flight: Book a flight between two cities- origin (required): Departure city code (e.g., "JFK", "LAX")- destination (required): Arrival city code- date (required): Flight date in YYYY-MM-DD format- time_preference (optional): "morning", "afternoon", or "evening"search_hotels: Search for hotel accommodations- city (required): City name or code- check_in (required): Check-in date in YYYY-MM-DD format- check_out (required): Check-out date in YYYY-MM-DD format""", "tool_selection": 'book_flight(origin="JFK", destination="LAX", date="2024-01-15", time_preference="morning")'}scores = tool_invocation_eval.evaluate(eval_input)print(scores[0])# Score(name='tool_invocation', score=1.0, label='correct', ...)

import { createToolInvocationEvaluator } from "@arizeai/phoenix-evals";import { openai } from "@ai-sdk/openai";// Create the evaluatorconst toolInvocationEvaluator = createToolInvocationEvaluator({ model: openai("gpt-4o"),});// Evaluate a tool invocation using human-readable formatconst result = await toolInvocationEvaluator.evaluate({ input: `User: I need to book a flight from New York to Los AngelesAssistant: I'd be happy to help you book a flight. When would you like to travel?User: Tomorrow morning, the earliest available`, availableTools: `book_flight: Book a flight between two cities- origin (required): Departure city code (e.g., "JFK", "LAX")- destination (required): Arrival city code- date (required): Flight date in YYYY-MM-DD format- time_preference (optional): "morning", "afternoon", or "evening"search_hotels: Search for hotel accommodations- city (required): City name or code- check_in (required): Check-in date in YYYY-MM-DD format- check_out (required): Check-out date in YYYY-MM-DD format`, toolSelection: 'book_flight(origin="JFK", destination="LAX", date="2024-01-15", time_preference="morning")',});console.log(result);// { score: 1, label: "correct", explanation: "..." }

​

Using Input Mapping
When your data has different field names, use input mapping.

Python

TypeScript

from phoenix.evals import LLMfrom phoenix.evals.metrics import ToolInvocationEvaluatorllm = LLM(provider="openai", model="gpt-4o")tool_invocation_eval = ToolInvocationEvaluator(llm=llm)eval_input = { "conversation": """User: Search for hotels in ParisAssistant: I can help you find hotels. What are your check-in and check-out dates?User: March 15th to March 20th""", "tools_schema": """search_hotels: Search for hotel accommodations- city (required): City name or code- check_in (required): Check-in date in YYYY-MM-DD format- check_out (required): Check-out date in YYYY-MM-DD format""", "llm_tool_call": 'search_hotels(city="Paris", check_in="2024-03-15", check_out="2024-03-20")'}input_mapping = { "input": "conversation", "available_tools": "tools_schema", "tool_selection": "llm_tool_call"}scores = tool_invocation_eval.evaluate(eval_input, input_mapping)

For more details on input mapping options, see Input Mapping.

import { bindEvaluator, createToolInvocationEvaluator } from "@arizeai/phoenix-evals";import { openai } from "@ai-sdk/openai";const toolInvocationEvaluator = createToolInvocationEvaluator({ model: openai("gpt-4o"),});const boundEvaluator = bindEvaluator(toolInvocationEvaluator, { inputMapping: { input: "conversation", availableTools: "toolsSchema", toolSelection: "llmToolCall", },});const result = await boundEvaluator.evaluate({ conversation: `User: Search for hotels in ParisAssistant: I can help you find hotels. What are your check-in and check-out dates?User: March 15th to March 20th`, toolsSchema: `search_hotels: Search for hotel accommodations- city (required): City name or code- check_in (required): Check-in date in YYYY-MM-DD format- check_out (required): Check-out date in YYYY-MM-DD format`, llmToolCall: 'search_hotels(city="Paris", check_in="2024-03-15", check_out="2024-03-20")',});

For more details on input mapping options, see Input Mapping.

​

Configuration
For LLM client configuration options, see Configuring the LLM.

​

Viewing and Modifying the Prompt
You can view the latest versions of our prompt templates on GitHub. The evaluators are designed to work well in a variety of contexts, but we highly recommend modifying the prompt to be more specific to your use case. Feel free to adapt them.

Python

TypeScript

from phoenix.evals.metrics import ToolInvocationEvaluatorfrom phoenix.evals import LLM, ClassificationEvaluatorllm = LLM(provider="openai", model="gpt-4o")evaluator = ToolInvocationEvaluator(llm=llm)# View the prompt templateprint(evaluator.prompt_template)# Create a custom evaluator based on the built-in templatecustom_evaluator = ClassificationEvaluator( name="tool_invocation", prompt_template=evaluator.prompt_template, # Modify as needed llm=llm, choices={"correct": 1.0, "incorrect": 0.0}, direction="maximize",)

import { TOOL_INVOCATION_CLASSIFICATION_EVALUATOR_CONFIG, createToolInvocationEvaluator } from "@arizeai/phoenix-evals";import { openai } from "@ai-sdk/openai";// View the prompt templateconsole.log(TOOL_INVOCATION_CLASSIFICATION_EVALUATOR_CONFIG.template);// Create a custom evaluator with a modified templateconst customEvaluator = createToolInvocationEvaluator({ model: openai("gpt-4o"), promptTemplate: TOOL_INVOCATION_CLASSIFICATION_EVALUATOR_CONFIG.template, // Modify as needed});

​

Using with Phoenix

​

Evaluating Traces
Run evaluations on traces collected in Phoenix and log results as annotations:
Evaluating Phoenix Traces

Logging LLM Evaluations

​

Running Experiments
Use the Tool Invocation evaluator in Phoenix experiments:
Using Evaluators in Experiments

​

API Reference

Python: ToolInvocationEvaluator

TypeScript: createToolInvocationEvaluator

​

Related

Tool Selection Evaluator - For evaluating whether the right tool was chosen

Correctness Evaluator - For evaluating factual accuracy

Was this page helpful?

YesNo

Suggest editsRaise issue

Tool SelectionTool Response Handling

⌘I

Phoenix home page

English日本語 (Japanese)中文 (Chinese)

Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform

Assistant

Responses are generated using AI and may contain mistakes.
