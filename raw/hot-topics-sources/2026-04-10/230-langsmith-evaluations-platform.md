---
title: LangSmith - LLM & AI Agent Evals Platform: Continuously improve agents
source_url: https://www.langchain.com/langsmith/evaluation
final_url: https://www.langchain.com/langsmith/evaluation
status: 200
content_type: text/html; charset=utf-8
topics: [Multi-Turn Agent Evaluation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:57.991275+00:00
---

# LangSmith - LLM & AI Agent Evals Platform: Continuously improve agents

## 원본 URL

https://www.langchain.com/langsmith/evaluation

## 추출 본문

LangSmith - LLM & AI Agent Evals Platform: Continuously improve agents

Products

LangSmith Platform

Observability

See exactly what your agents are doing

Evaluation

Score and improve agent performance

Deployment

Ship and scale agents in production

Fleet

Agents for the whole company

Open Source Frameworks

deepagents

Build long-running agents for complex tasks

langchain

Quick start agents with any model provider

langgraph

Build reliable agents with low-level control

Learn

Resources

Blog

Customer Stories

Guides

How-To

LangChain Academy

YouTube

Documentation

Community

LangSmith for Startups

Events

Community

Docs

Company

About

Careers

Partners

Pricing

Try LangSmith

Get a demo

Try LangSmith

Get a demo

LangSmith Evaluations: LLM & AI Agent Evaluation Platform

Continuously improve agent quality

Run evals before and after shipping, gather expert feedback on agent performance, and iterate on prompts with your team.

Start building

Get a demo

Helping top teams ship great agents

Use cases in production

Evals

Human feedback

Prompt optimization

Offline & online evals

Evaluate your agent’s performance

Run evaluations on curated datasets during development to compare agent versions, benchmark performance, and catch regressions before users do. 

Monitor performance in production with online evals that score user interactions with your agent in real-time to detect issues and measure quality.

Calibrate llm-as-judge evals with human feedback

Conversation evals

Multi-modal evals

Learn about eval techniques

Human feedback

Gather expert feedback

Equip subject-matter experts to assess response quality or review specific attributes of your agent. Automatically assign runs for review, and annotate any part of your agent workflow to capture precise feedback.

Embedded renderings of UI in review flow

Auto send interesting traces for human review

Shared scoring criteria to standardize reviewer feedback

Streamline human feedback

Prompt optimization

Iterate & collaborate on prompts

Experiment with prompts in the Playground, and compare outputs across different prompt versions or model providers. Use our AI Agent Polly to auto improve prompts. Scale spot checking by running an evaluation of the prompt on a larger dataset, all from the UI.

Create and test a prompt

Resources for LangSmith Evaluation

guide

Evals guidebook

docs

Evals concepts

course

Foundational course

FAQs for LangSmith Evaluation

What kind of evaluators does LangSmith support?

LangSmith's evaluation framework supports multiple evaluator types: human evaluation through annotation queues, heuristic checks (like validating outputs or checking if code compiles), LLM-as-judge evaluators that score against criteria you define, and pairwise comparisons. You can also write custom evaluators in Python or TypeScript with any business logic you need, from correctness and ground truth matching to hallucination detection and guardrails validation.

How does human feedback and annotation work?

LangSmith makes it easy for AI teams to collect expert feedback through annotation queues. Flag runs for review, assign them to subject-matter experts, and use that feedback to calibrate automated evaluation, improve prompts, or augment datasets with high-quality test cases.

How reliable is LLM-as-judge, and how do I audit it?

LLM-as-judge evaluators don't always get it right. LangSmith lets you route samples to human reviewers who flag disagreements, helping you identify failure modes and edge cases. This feedback loop lets you iterate on and calibrate your automated evaluation metrics over time.

What's the difference between offline and online evaluation?

Offline evaluation runs against curated datasets during development to catch regressions before deployment. They act as unit tests for your LLM application. Online evaluation scores real-world production traffic in real-time to detect quality drift. LangSmith supports both as part of an end-to-end evaluation lifecycle.

Can I use LangSmith Evaluation without LangSmith Observability?

Yes. You can use LangSmith Evaluation with or without Observability. For all plan types, you'll get access to both and only pay for what you use.

How does LangSmith evaluate AI agents and multi-turn workflows?

Agent evaluation in LangSmith captures the full trajectory of steps, tool calls, and reasoning your agent took. Define evaluators that score intermediate decisions and agent behavior to debug complex agent workflows and pinpoint where things went wrong.

Can I run evaluations in my CI/CD pipeline?

Yes. LangSmith integrates with pytest, Vitest, and GitHub workflows so you can run evals on every PR or nightly build. Set thresholds on evaluation metrics and fail pipelines automatically when scores drop, bringing the same rigor as deterministic unit tests to your AI development process.

How do I benchmark across prompts, models, or agent versions?

LangSmith's comparison view dashboards show results side-by-side across experiments. Run the same dataset against different prompt versions, model providers, or agent systems to visualize what's working and optimize performance with real benchmarks.

How does LangSmith evaluate RAG systems?

RAG evaluation separates retrieval quality from generation quality. LangSmith supports metrics like context precision (did you retrieve relevant documents?) and faithfulness (does the answer match the retrieved context?) helping you catch hallucinations and improve your retrieval pipelines independently.

Do I have to use LangChain or LangGraph to use LangSmith?

No. LangSmith is framework-agnostic. Evaluate AI applications built with LangGraph, custom Python, or any other framework. Use the SDK or API to send traces from whatever stack your team runs.

How do I get started if I don't have a labeled dataset?

Start by capturing production traces with LangSmith, then sample interesting or problematic runs into a dataset. Use LLM-as-judge evaluators to bootstrap initial labels, then refine with human annotation.

Will LangSmith add latency to my application?

No. The LangSmith SDK uses an async callback handler that sends traces to a distributed collector. Your application performance is never impacted. If LangSmith experiences an incident, your agent keeps running normally.

Can I self-host LangSmith? Where is my data stored?

LangSmith instances hosted at smith.langchain.com stores data in GCP us-central-1 or europe-west4. For enterprise-grade requirements, LangSmith can run on your Kubernetes cluster in AWS, GCP, or Azure so its fully self-hosted and data never leaves your environment. We will not train on your data. See our documentation for details.

Will you train on the data that I send LangSmith?

We will not train on your data, and you own all rights to your data. See LangSmith Terms of Service for more information.

How much does LangSmith cost?

LangSmith has a free tier for development and small-scale production. Paid plans scale with trace volume. See our pricing page for details, or contact us for enterprise pricing.

Ready to build better agents through continuous evaluation?

‍

Start building

Get a demo

Products
LangSmith PlatformLangSmith ObservabilityLangSmith EvaluationLangSmith DeploymentLangSmith FleetDeep AgentsLangChainLangGraph

Resources
BlogCustomer StoriesGuidesLangChain AcademyCommunityEventsChangelogDocsSupport

Company
AboutCareersPartnersTrust CenterMarketing Assets

Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

All systems operational

Privacy policyTerms of service
