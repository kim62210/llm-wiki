---
title: How to Evaluate Tool-Calling Agents - Arize AI
source_url: https://arize.com/blog/how-to-evaluate-tool-calling-agents
final_url: https://arize.com/blog/how-to-evaluate-tool-calling-agents/
status: 200
content_type: text/html; charset=UTF-8
topics: [Tool Selection & Tool Invocation Evaluators]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:01.164334+00:00
---

# How to Evaluate Tool-Calling Agents - Arize AI

## 원본 URL

https://arize.com/blog/how-to-evaluate-tool-calling-agents

## 추출 본문

How to Evaluate Tool-Calling Agents - Arize AI

Download logo as PNG

Download logo as SVG

Arize AX

Arize AX

AX - Generative
Enterprise AI Engineering Platform
AX - ML & CV
Enterprise ML Observability
Alyx
AI Engineering Agent

Arize Platform demoSee how it worksWatch video

Phoenix OSS

Pricing

Docs

Learn

Learn

Courses
Essential Arize-led courses
Prompt Learning
Essentials playbook
Paper readings
AI research insights
Agents hub
AI agent evaluation
LLM Evals Hub
LLM evaluation guide
AI Product Manager
AI PM learning

Insights

Blog
Get to know Arize
Community
Bring your questions
Events
AI networking events
Video tutorials
Hands-on video tutorials

Company

Company

About
We power the future of AI
Careers
Join a world class team
Partners
Partner with us
Customers
Built with Arize AX

Press
Updates from the newsroom
Security
We take your trust seriously

CustomersSee who is achieving better outcomes in production

Sign inBook a demoGet started

Arize AX
Back

Arize AX

AX - Generative
Enterprise AI Engineering Platform
AX - ML & CV
Enterprise ML Observability
Alyx
AI Engineering Agent
Arize Platform demo
See how it works

Phoenix OSS
Back

Pricing
Back

Docs
Back

Learn
Back

Learn

Courses
Essential Arize-led courses
Prompt Learning
Essentials playbook
Paper readings
AI research insights
Agents hub
AI agent evaluation
LLM Evals Hub
LLM evaluation guide
AI Product Manager
AI PM learning

Insights

Blog
Get to know Arize
Community
Bring your questions
Events
AI networking events
Video tutorials
Hands-on video tutorials

Company
Back

Company

About
We power the future of AI
Careers
Join a world class team
Partners
Partner with us
Customers
Built with Arize AX

Press
Updates from the newsroom
Security
We take your trust seriously

Book a demoSign inSign up

How to Evaluate Tool-Calling Agents

Published March 2, 2026

When you give an LLM access to tools, you introduce a new surface area for failure — and it breaks in two distinct ways:

The model selects the wrong tool (or calls a tool when it should have answered directly).

The model selects the right tool, but calls it incorrectly — wrong arguments, missing parameters, or hallucinated values.

These are different problems with different fixes. Catching them requires measuring them separately.

As tool use becomes central to production LLM systems, developers need a systematic way to measure tool calling behavior, understand where it fails, and iterate quickly.

Phoenix includes two prebuilt LLM-as-a-judge evaluators specifically for this — plus a full evaluation workflow in the UI that lets you write prompts, run experiments, add evaluators, and compare results without writing any code.

This tutorial walks through the full workflow using a travel assistant demo: what the evaluators measure, how to validate alignment, and how to use the results to improve both your assistant prompt and your evaluators. The exact dataset, prompts, and code to get started can be found in this notebook if you want to follow along.

The Demo: An AI Travel Assistant

To make this concrete, we’ll evaluate a travel planning assistant with access to six tools:

ToolDescription
search_flights
Search available flights between two cities on a given date
get_weather
Get current weather or forecast for a location
search_hotels
Find hotels in a city for given dates and guest count
get_directions
Get travel directions and estimated time between two locations
convert_currency
Convert an amount from one currency to another
search_restaurants
Find restaurants in a location by cuisine or criteria

Our evaluation dataset has 30 queries covering three scenarios:

PatternCountDescriptionSingle-tool18One tool needed; tests parameter extraction, implicit dates, ambiguous phrasingParallel (2 tools)10Two tools needed simultaneously; all 10 two-tool combinations representedNo tool needed2General travel knowledge questions the assistant should answer directly

The dataset is labeled — each query has an expected tool call (or an empty list, for no-tool cases). This lets us evaluate both with and without ground truth.

Example queries:

“I need to get from Narita Airport to my hotel in Shinjuku — what’s the best transit route?” → 
get_directions

“I’m planning a trip to Lisbon in September — find me hotels from the 8th to the 12th and check the weather on the 8th.” → 
search_hotels
 + 
get_weather

“What’s the best way to handle tipping in Japan?” → no tool needed

The Evaluation Workflow

The overall loop looks like this:

Upload dataset and prompt to Phoenix (done via setup notebook)

Run an experiment using the assistant prompt in the Phoenix playground

Add evaluators from prebuilt templates or write your own

Inspect failures at the example level with per-example explanations

Iterate — update the assistant prompt or evaluator prompt, rerun, and compare

Steps 2–5 all happen directly in the Phoenix UI.

Two Prebuilt, Reference-Free Tool Evaluators

Phoenix ships with two LLM-as-a-judge evaluators designed specifically for tool calling. Both are reference-free — they reason from conversational context rather than comparing against labeled ground truth, which means you can run them on any tool-calling LLM without a labeled dataset.

https://arize.com/wp-content/uploads/2026/03/add-evaluators.mp4

1. Tool Selection Evaluator

Answers: Did the model choose the correct tool — or correctly choose no tool?

The evaluator looks at:

The user query

The list of available tools

The model’s output, including any tool calls

It handles single tool calls, parallel tool calls, and cases where no tool should be called. The template includes formatting logic that transforms the structured experiment output into a readable format for the judge — in most cases you don’t need to modify it.

What it returns: A correct / incorrect label and an explanation.

Example explanation for a failure:

“The model called search_flights with the correct origin and destination, but used 2023 dates rather than the current year, making the selection contextually incorrect.”

The only configuration step is mapping your dataset’s input column (e.g., 
input.query
) so the template pulls the right field.

2. Tool Invocation Evaluator

Tool selection is only half the story. Even when the right tool is chosen, arguments can be wrong.

Answers: Was the tool called correctly?

This evaluator checks:

Are all required parameters present?

Were any arguments hallucinated or inconsistent with user intent?

Do argument values match what the user actually said?

Critically, it evaluates invocation independently of selection — a useful separation when you want to distinguish “wrong tool” failures from “right tool, bad arguments” failures.

You can preview the template with example data filled in to verify the mappings before running.

Adding A Custom Evaluator

Reference-free evaluators are broadly useful, but if you have labeled data, you can go further.

Our travel assistant dataset includes expected tool calls for every query. Rather than a simple string-match code evaluator, we use a custom LLM evaluator that:

Compares actual tool calls to expected tool calls

Ignores argument ordering differences

Reasons about semantic equivalence

An LLM judge is the right tool here because tool call arguments don’t lend themselves to exact matching — values like “CDG Airport” and “Charles De Gaulle Airport” are equivalent in ways that string comparison can’t capture.

The custom evaluator prompt asks the judge to compare the output tool calls to the reference calls and return correct or incorrect with an explanation.

First Results: Reading the Experiment

After the first experiment run, here’s what the scores looked like:

Tool Selection: 100% — the model consistently chose the right tool(s)

Tool Invocation: Lower — some arguments were wrong or hallucinated

Matches Expected: 0.36 — only 36% of calls matched the ground truth

A 36% ground truth match sounds alarming, but the per-example explanations tell a more nuanced story.

https://arize.com/wp-content/uploads/2026/03/explanation-shot.mp4

Iteration: What the Failures Revealed

The real value of evaluation is in the failure cases. Three distinct patterns emerged.

Failure 1: The year bug (prompt issue → fix the system prompt)

For a flight search query, the judge flagged a mismatch:

“The expected tool calls use 2025 dates, but the model called search_flights with dates in 2023.”

The model was defaulting to a year embedded in its training data rather than the current year. The fix: add one line to the system prompt:

“Assume the current year is 2025 for all searches that require dates.”

Since the base Tool Invocation evaluator didn’t catch that the year was wrong, we also updated it’s prompt template to explicitly check for this: adding a line specifying that date arguments should use 2025. This is an example of customizing a prebuilt template to enforce use-case-specific constraints.

Failure 2: CDG Airport vs. Paris (evaluator calibration issue → loosen the evaluator)

For the query “I’m staying near the Eiffel Tower and need to find my way to CDG Airport — also find hotels near the airport,” the ground truth expected 
city: "Paris"
 for the hotel search. The model used 
city: "CDG Airport"
.

The judge flagged this as a mismatch. But looking at it: the user explicitly asked for hotels near the airport. CDG Airport is arguably a more faithful interpretation of the request than just Paris.

This is a case where the evaluator was being too strict, not the model. The right fix isn’t to change the assistant — it’s to adjust the custom evaluator prompt to allow for reasonable semantic equivalence in location arguments.

This is a common pattern: early experiment results reveal where your evaluators need calibration, not just where your model needs improvement.

Failure 3: “This weekend” (capability gap → add a tool)

For queries like “I need a hotel in Kyoto for this weekend,” the Tool Invocation evaluator flagged the date arguments as incorrect:

“The model assumed specific dates for ‘this weekend’ without knowing the current date. This is an ungrounded assumption.”

The model isn’t wrong to try — it just doesn’t have the information it needs. The fix isn’t to change the prompt; it’s to add a 
get_current_date
 tool to the assistant so it can make accurate date calculations when users say things like “this weekend” or “next Friday.” This would also fix the first failure we observed, where the LLM didn’t know the current year.

After Iteration: Comparing Experiments

After updating the system prompt (year fix) and the tool invocation evaluator (year check), we reran the experiment and compared results side by side in Phoenix.

https://arize.com/wp-content/uploads/2026/03/experiment-compare.mp4

What changed:

Matches Expected improved — the year fix resolved the most common failure case

Tool Invocation scores decreased slightly — but this is expected and correct. By making the evaluator more specific about date validation, it now catches cases it previously missed. The decrease reflects better measurement, not worse performance.

Side-by-side experiment comparison makes these changes visible and interpretable — you can see exactly which examples improved, which regressed, and why.

When to Customize the Templates

The prebuilt evaluators are designed to be general-purpose. They’ll catch most tool calling issues without modification. But high-quality systems often need evaluators that understand your domain.

Common reasons to customize:

Use-case specific constraints: e.g., “all date searches should use the current year”

Looser semantic equivalence: allow “CDG Airport” and “Charles De Gaulle Airport” to match

Stricter parameter validation: require a specific field format or value range

Because the built-in templates are fully editable, you can adapt them while preserving the underlying structure. The workflow is: duplicate the template, add your constraints, and rerun.

Before (default Tool Invocation evaluator): Evaluates whether required parameters are present and values are grounded in user intent.

After (customized for this use case): Same evaluation, plus: “Assume the current year is 2025. Flag any date arguments that use a different year as incorrect.”

Wrapping Up

This tutorial covered the main building blocks for evaluating tool-calling behavior in Phoenix: the two prebuilt evaluators (tool selection and tool invocation), how to add a custom ground-truth evaluator when you have labeled data, and how to use the results to iterate on both your assistant prompt and your evaluators.

The prebuilt templates are designed to be general-purpose starting points — they’ll work out of the box for most tool-calling setups, but they’re straightforward to customize when your use case has specific requirements.

The dataset and prompts from this demo are available in this notebook if you want to run through it yourself or use them as a starting point for your own evaluation setup.

 Elizabeth Hutton 
 Senior AI Engineer 

Copied

 Sign up for our newsletter, The Evaluator — and stay in the know with updates and new resources:
 

Platform

Arize AX - Generative

Arize AX - ML & CV

Docs

Pricing

Phoenix Open Source

Learn

Blog

AI Agents & Assistants Handbook

Evaluating AI Agents course

AI Research Papers

Topics

Agent Evaluation

AI Agent: Useful Case Study

AI Product Manager

LLM Tracing

LLM Hallucination Examples

Prompt Optimization Techniques

LLM as a Judge

Company

About

Careers

Press

Security

Partners

Customers

Get started

Book a Demo

Sign In

Contact

AX Platform Status

Privacy Policy

Arize - LLMs.txt

Linkedin

Twitter

 Copyright © 2026 Arize AI, Inc
 Privacy Policy

Subscribe to The Evaluator

We’ll send you the latest news, expertise, and product updates from Arize. Your inbox is sacred, so we’ll only curate and send the best stuff.

*We're committed to your privacy. Arize uses the information you provide to contact you about relevant content, products, and services. You may unsubscribe from these communications at any time. For more information, check out our privacy policy.
