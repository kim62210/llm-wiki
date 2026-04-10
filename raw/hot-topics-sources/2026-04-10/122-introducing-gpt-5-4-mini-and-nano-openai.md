---
title: Introducing GPT-5.4 mini and nano | OpenAI
source_url: https://openai.com/index/introducing-gpt-5-4-mini-and-nano
final_url: https://openai.com/index/introducing-gpt-5-4-mini-and-nano/
status: 200
content_type: text/html; charset=utf-8
topics: [GPT-5.4]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:41.223852+00:00
---

# Introducing GPT-5.4 mini and nano | OpenAI

## 원본 URL

https://openai.com/index/introducing-gpt-5-4-mini-and-nano

## 추출 본문

Introducing GPT-5.4 mini and nano | OpenAI

Skip to main content

Research

Products

Business

Developers

Company

Foundation(opens in a new window)

Log inTry ChatGPT(opens in a new window)

Research

Products

Business

Developers

Company

Foundation(opens in a new window)

Try ChatGPT(opens in a new window)Login

OpenAI

Table of contents

Coding

Computer use

Availability & pricing

March 17, 2026
CompanyProduct

Introducing GPT‑5.4 mini and nano

Fast and efficient models optimized for coding and subagents

Loading…

Share

Today we’re releasing GPT‑5.4 mini and nano, our most capable small models yet. They bring many of the strengths of GPT‑5.4 to faster, more efficient models designed for high-volume workloads.

GPT‑5.4 mini significantly improves over GPT‑5 mini across coding, reasoning, multimodal understanding, and tool use, while running more than 2x faster. It also approaches the performance of the larger GPT‑5.4 model on several evaluations, including SWE-Bench Pro and OSWorld-Verified.

GPT‑5.4 nano is the smallest, cheapest version of GPT‑5.4 for tasks where speed and cost matter most. It is also a significant upgrade over GPT‑5 nano. We recommend it for classification, data extraction, ranking, and coding subagents that handle simpler supporting tasks.

These models are built for the kinds of workloads where latency directly shapes the product experience: coding assistants that need to feel responsive, subagents that quickly complete supporting tasks, computer-using systems that capture and interpret screenshots, and multimodal applications that can reason over images in real-time. In these settings, the best model is often not the largest one—it’s the one that can respond quickly, use tools reliably, and still perform well on complex professional tasks. 

GPT-5.4 (xhigh)GPT-5.4 mini (xhigh)GPT-5.4 nano (xhigh)GPT-5 mini (high¹)SWE-Bench Pro (Public)57.7%54.4%52.4%45.7%Terminal-Bench 2.075.1%60.0%46.3%38.2%Toolathlon54.6%42.9%35.5%26.9%GPQA Diamond93.0%88.0%82.8%81.6%OSWorld-Verified75.0%72.1%39.0%42.0%

1 The highest reasoning_effort available for GPT‑5 mini is 'high'.

Here’s what our customers think after testing GPT‑5.4 mini and nano in their workflows:

HebbiaCodeRabbitMercorGitHubRoxNotionWhoopPerplexity

"GPT-5.4 mini delivers strong end-to-end performance for a model in this class. In our evaluations it matched or exceeded competitive models on several output tasks and citation recall at a much lower cost. It also achieved higher end-to-end pass rates and stronger source attribution than the larger GPT-5.4 model."

— Aabhas Sharma, CTO at Hebbia

Coding

GPT‑5.4 mini and nano are especially effective in coding workflows that benefit from fast iteration. The models handle targeted edits, codebase navigation, front-end generation, and debugging loops with low latency, making them a strong fit for coding tasks that need to be completed at faster speeds and lower costs.

In benchmarks, GPT‑5.4 mini consistently outperforms GPT‑5‑mini at similar latencies and approaches GPT‑5.4‑level pass rates while running much faster, delivering one of the strongest performance-per-latency tradeoffs for coding workflows.

We estimate latency by looking at the production behavior of our models, and simulating this offline. The latency estimate accounts for tool call duration (code execution time), sampled tokens, and input tokens. Real-world latency may vary substantially, and depends on many factors not captured in our simulation. Similarly, costs are estimated based on API pricing of these models at the time of writing. Costs may change in the future. Reasoning efforts were swept from low to xhigh.

Subagents

GPT‑5.4 mini is also a strong fit for systems that combine models of different sizes. In Codex, for example, a larger model like GPT‑5.4 can handle planning, coordination, and final judgment, while delegating to GPT‑5.4 mini subagents that handle narrower subtasks in parallel—like searching a codebase, reviewing a large file, or processing supporting documents. Learn how subagents work in Codex in the docs⁠(opens in a new window).

This pattern becomes more useful as smaller models get faster and more capable. Instead of using one model for everything, developers can compose systems where larger models decide what to do and smaller models execute quickly at scale. GPT‑5.4 mini is our strongest mini model yet for that style of workflow.

Computer use

GPT‑5.4 mini is also strong on multimodal tasks, particularly those related to computer use. The model can quickly interpret screenshots of dense user interfaces to complete computer use tasks with speed. On OSWorld-Verified, GPT‑5.4 mini approaches GPT‑5.4 while substantially outperforming GPT‑5 mini.

Availability & pricing

GPT‑5.4 mini is available today in the API, Codex, and ChatGPT.

In the API, GPT‑5.4 mini supports text and image inputs, tool use, function calling, web search, file search, computer use, and skills. It has a 400k context window and costs $0.75 per 1M input tokens and $4.50 per 1M output tokens. 

In Codex, GPT‑5.4 mini is available across the Codex app, CLI, IDE extension and web. It uses only 30% of the GPT‑5.4 quota, letting developers quickly handle simpler coding tasks in Codex for about one-third the cost. Codex can also delegate to GPT‑5.4 mini subagents so that less reasoning-intensive work runs on the cheaper model.

In ChatGPT, GPT‑5.4 mini is available to Free and Go users via the “Thinking” feature in the + menu. For all other users, GPT‑5.4 mini is available as a rate limit fallback for GPT‑5.4 Thinking.

GPT‑5.4 nano is only available in the API and costs $0.20 per 1M input tokens and $1.25 per 1M output tokens.

For more information on the models’ safeguards, please check out the System Card addendum on our Deployment Safety Hub⁠(opens in a new window).

Coding

GPT-5.4 (xhigh)GPT-5.4 mini (xhigh)GPT-5.4 nano (xhigh)GPT-5 mini (high¹)SWE-bench Pro (Public)57.7%54.4%52.4%45.7%Terminal-Bench 2.075.1%60.0%46.3%38.2%

Tool-calling

GPT-5.4 (xhigh)GPT-5.4 mini (xhigh)GPT-5.4 nano (xhigh)GPT-5 mini (high¹)MCP Atlas67.2%57.7%56.1%47.6%Toolathlon54.6%42.9%35.5%26.9%τ2-bench (telecom)98.9%93.4%92.5%74.1%

Intelligence

GPT-5.4 (xhigh)GPT-5.4 mini (xhigh)GPT-5.4 nano (xhigh)GPT-5 mini (high¹)GPQA Diamond93.0%88.0%82.8%81.6%HLE w/ tool52.1%41.5%37.7%31.6%HLE w/o tools39.8%28.2%24.3%18.3%

MM / Vision / CUA

GPT-5.4 (xhigh)GPT-5.4 mini (xhigh)GPT-5.4 nano (xhigh)GPT-5 mini (high¹)OSWorld-Verified75.0%72.1%39.0%42.0%MMMUPro w/ Python81.5%78.0%69.5%74.1%MMMUPro81.2%76.6%66.1%67.5%OmniDocBench 1.5 (no tools)² — lower is better0.1090.12630.24190.1791

Long context

GPT-5.4 (xhigh)GPT-5.4 mini (xhigh)GPT-5.4 nano (xhigh)GPT-5 mini (high¹)OpenAI MRCR v2 8-needle 64K–128K86.0%47.7%44.2%35.1%OpenAI MRCR v2 8-needle 128K–256K79.3%33.6%33.1%19.4%Graphwalks BFS 0K–128K93.1%76.3%73.4%73.4%Graphwalks parents 0–128K (accuracy)89.8%71.5%50.8%64.3%

1 The highest reasoning_effort available for GPT‑5 mini is 'high'.

2 Overall Edit Distance. OmniDocBench was run with reasoning_effort set to 'none' to reflect low-cost, low-latency performance.

2026

Author

OpenAI

Keep reading

View all

The next phase of enterprise AI

CompanyApr 8, 2026

OpenAI acquires TBPN

CompanyApr 2, 2026

Codex now offers pay-as-you-go pricing for teams

ProductApr 2, 2026

Our Research
Research Index

Research Overview

Research Residency

OpenAI for Science

Economic Research

Latest Advancements
GPT-5.3 Instant

GPT-5.3-Codex

GPT-5

Codex

Safety
Safety Approach

Security & Privacy

Trust & Transparency

ChatGPT
Explore ChatGPT(opens in a new window)

Business

Enterprise

Education

Pricing(opens in a new window)

Download(opens in a new window)

Sora
Sora Overview

Features

Pricing

Sora log in(opens in a new window)

API Platform
Platform Overview

Pricing

API log in(opens in a new window)

Documentation(opens in a new window)

Developer Forum(opens in a new window)

For Business
Business Overview

Solutions

Contact Sales

Company
About Us

Our Charter

Foundation(opens in a new window)

Careers

Brand

Support
Help Center(opens in a new window)

More
News

Stories

Livestreams

Podcast

RSS

Terms & Policies
Terms of Use

Privacy Policy

Other Policies 

(opens in a new window)(opens in a new window)(opens in a new window)(opens in a new window)(opens in a new window)(opens in a new window)(opens in a new window)

OpenAI © 2015–2026Manage Cookies

EnglishUnited States
