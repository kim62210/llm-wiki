---
title: LangSmith Evaluation - Docs by LangChain
source_url: https://docs.langchain.com/langsmith/evaluation
final_url: https://docs.langchain.com/langsmith/evaluation
status: 200
content_type: text/html; charset=utf-8
topics: [Multi-Turn Agent Evaluation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:57.797287+00:00
---

# LangSmith Evaluation - Docs by LangChain

## 원본 URL

https://docs.langchain.com/langsmith/evaluation

## 추출 본문

LangSmith Evaluation - Docs by LangChain

Skip to main content

Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. Buy tickets >

Docs by LangChain home page

LangSmith

Search...

⌘K

Ask AI

GitHub

Try LangSmith

Try LangSmith

Search...

Navigation

LangSmith Evaluation

Get started

Observability

Evaluation

Prompt engineering

Agent deployment

Platform setup

Reference

Overview

Quickstart

Concepts

Evaluation approaches

Polly AI assistant

Datasets

Create a dataset

Manage datasets

Custom output rendering

Set up evaluations

Run an evaluation

Evaluation types

Frameworks & integrations

Evaluation techniques

Improve evaluators

Tutorials

Analyze experiment results

Analyze an experiment

Compare experiment results

Filter experiments in the UI

Fetch performance metrics for an experiment

Upload experiments run outside of LangSmith

Annotation & human feedback

Use annotation queues

Manage feedback & annotation queues
SDK

Set up feedback criteria

Annotate traces and runs inline

Audit evaluator scores

Common data types

Example data format

Dataset prebuilt JSON schema types

Dataset transformations

LangSmith Evaluation

Copy page

Copy page

LangSmith supports two types of evaluations based on when and where they run:

Offline Evaluation

Test before you shipRun evaluations on curated datasets during development to compare versions, benchmark performance, and catch regressions.

Online Evaluation

Monitor in productionEvaluate real user interactions in real-time to detect issues and measure quality on live traffic.

​

Evaluation workflow

Offline evaluation flow

Online evaluation flow

1

Create a dataset

Create a dataset with examples from manually curated test cases, historical production traces, or synthetic data generation.

2

Define evaluators

Create evaluators to score performance:
Human review

Code rules

LLM-as-judge

Pairwise comparison

3

Run an experiment

Execute your application on the dataset to create an experiment. Configure repetitions, concurrency, and caching to optimize runs.

4

Analyze results

Compare experiments for benchmarking, unit tests, regression tests, or backtesting.

1

Deploy your application

Each interaction creates a run without reference outputs.

2

Configure online evaluators

Set up evaluators to run automatically on production traces: safety checks, format validation, quality heuristics, and reference-free LLM-as-judge. Apply filters and sampling rates to control costs.

3

Monitor in real-time

Evaluators run automatically on runs or threads, providing real-time monitoring, anomaly detection, and alerting.

4

Establish a feedback loop

Add failing production traces to your dataset, create targeted evaluators, validate fixes with offline experiments, and redeploy.

For more on the differences between offline and online evaluation, refer to the Evaluation concepts page.

​

Get started

Evaluation quickstart

Get started with offline evaluation.

Manage datasets

Create and manage datasets for evaluation through the UI or SDK.

Run offline evaluations

Explore evaluation types, techniques, and frameworks for comprehensive testing.

Analyze results

View and analyze evaluation results, compare experiments, filter data, and export findings.

Run online evaluations

Monitor production quality in real-time from the Observability tab.

Follow tutorials

Learn by following step-by-step tutorials, from simple chatbots to complex agent evaluations.

To set up a LangSmith instance, visit the Platform setup section to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.

Edit this page on GitHub or file an issue.

Connect these docs to Claude, VSCode, and more via MCP for real-time answers.

Was this page helpful?

YesNo

Evaluation quickstart

Next

⌘I

Docs by LangChain home page
githubxlinkedinyoutube

Resources
ForumChangelogLangChain AcademyTrust Center

Company
HomeAboutCareersBlog

githubxlinkedinyoutube
