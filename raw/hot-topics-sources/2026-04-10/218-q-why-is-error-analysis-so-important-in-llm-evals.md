---
title: Q: Why is “error analysis” so important in LLM evals, and how is it performed? – Hamel's Blog - Hamel Husain
source_url: https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html
final_url: https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html
status: 200
content_type: text/html; charset=utf-8
topics: [Error Analysis as the Eval Foundation]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:43:56.197968+00:00
---

# Q: Why is “error analysis” so important in LLM evals, and how is it performed? – Hamel's Blog - Hamel Husain

## 원본 URL

https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html

## 추출 본문

Q: Why is “error analysis” so important in LLM evals, and how is it performed? – Hamel's Blog - Hamel Husain

Blog

Notes

Hire Me

OSS

Teaching

On this page

1. Creating a Dataset

2. Open Coding

3. Axial Coding

4. Iterative Refinement

Subscribe To My Newsletter

Q: Why is “error analysis” so important in LLM evals, and how is it performed?

LLMs

evals

faq

faq-individual

Published

August 15, 2025

Error analysis is the most important activity in evals. Error analysis helps you decide what evals to write in the first place. It allows you to identify failure modes unique to your application and data. The process involves:

1. Creating a Dataset

Gathering representative traces of user interactions with the LLM. If you do not have any data, you can generate synthetic data to get started.

2. Open Coding

Human annotator(s) (ideally a benevolent dictator) review and write open-ended notes about traces, noting any issues. This process is akin to “journaling” and is adapted from qualitative research methodologies. When beginning, it is recommended to focus on noting the first failure observed in a trace, as upstream errors can cause downstream issues, though you can also tag all independent failures if feasible. A domain expert should be performing this step.

3. Axial Coding

Categorize the open-ended notes into a “failure taxonomy.”. In other words, group similar failures into distinct categories. This is the most important step. At the end, count the number of failures in each category. You can use a LLM to help with this step.

4. Iterative Refinement

Keep iterating on more traces until you reach theoretical saturation, meaning new traces do not seem to reveal new failure modes or information to you. As a rule of thumb, you should aim to review at least 100 traces.

You should frequently revisit this process. There are advanced ways to sample data more efficiently, like clustering, sorting by user feedback, and sorting by high probability failure patterns. Over time, you’ll develop a “nose” for where to look for failures in your data.

Do not skip error analysis. It ensures that the evaluation metrics you develop are supported by real application behaviors instead of counter-productive generic metrics (which most platforms nudge you to use). For examples of how error analysis can be helpful, see this video, or this blog post.

Here is a visualization of the error analysis process by one of our students, Pawel Huryn - including how it fits into the overall evaluation process:

↩︎ Back to main FAQ

This article is part of our AI Evals FAQ, a collection of common questions (and answers) about LLM evaluation. View all FAQs or return to the homepage.
