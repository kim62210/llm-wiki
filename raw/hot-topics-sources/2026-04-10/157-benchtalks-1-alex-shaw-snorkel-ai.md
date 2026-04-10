---
title: Benchtalks #1: Alex Shaw (Terminal-Bench, Harbor) – Building the Benchmark Factory | Snorkel AI
source_url: https://snorkel.ai/blog/benchtalks-alex-shaw-terminal-bench-harbor-building-the-benchmark-factory
final_url: https://snorkel.ai/blog/benchtalks-alex-shaw-terminal-bench-harbor-building-the-benchmark-factory/
status: 200
content_type: text/html; charset=UTF-8
topics: [Terminal-Bench 2.0]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:47.402025+00:00
---

# Benchtalks #1: Alex Shaw (Terminal-Bench, Harbor) – Building the Benchmark Factory | Snorkel AI

## 원본 URL

https://snorkel.ai/blog/benchtalks-alex-shaw-terminal-bench-harbor-building-the-benchmark-factory

## 추출 본문

Benchtalks #1: Alex Shaw (Terminal-Bench, Harbor) – Building the Benchmark Factory | Snorkel AI

 Capabilities 

 overview 

 Our technology 

 The engine powering our solutions 

 EXPERT DATA SERVICES 

 Overview 

 Expert-curated datasets for frontier AI 

 Use cases 

 From agentic systems to coding, explore  data applications 

 Join our expert community 

 Get paid to shape safer, smarter AI 

 Enterprise AI Solutions 

 Overview 

 Custom AI systems built to unlock ROI fast 

 Customer stories 

 Real-world results from enterprise deployments 

 Research 

 RESEARCH 

 Research hub 

 Leaderboards 

 Open Benchmarks Grants 

 featured benchmark 

 Introducing Agentic Coding 

 A benchmark for evaluating AI models on complex, real-world coding tasks that require multi-step reasoning, tool use, and autonomous problem-solving. 

See the benchmark

 Resources 

 RESOURCES 

 Resource library 

 Events 

 Reading Group 

 Blog 

 Docs 

 Featured blog 

 Terminal-Bench 2.0 is here. 

 Developed by Stanford and Laude Institute with contributions from Snorkel AI, it’s a major leap forward in evaluating AI coding agents. 

Read more

 Company 

 company 

 About 

 Careers 

 Press 

 Partners 

 Security 

 Contact us 

 Get started 

Get started

Get a demo

Search result for:

SearchSubmitClear

See all articles

Research

Benchtalks #1: Alex Shaw (Terminal-Bench, Harbor) – Building the Benchmark Factory

Vincent Sunn Chen

 Published: March 31, 2026 

To kick off our inaugural Benchtalks, a series dedicated to the researchers building these measurement toolkits, Snorkel AI co-founder Vincent Sunn Chen sat down with Alex Shaw, Founding MTS at Laude Institute and co-creator of Terminal-Bench and Harbor.

Highlights

Terminal-Bench is driving rapid progress at the frontier: Scores moved from roughly 20–30% in development to 40–45% at release and now around 75–80%, showing how quickly strong evaluations can push model performance forward. As Shaw puts it, “In school that still is a B-minus, so it’s not far enough.” At the same time, “these benchmarks are very hill-climbable these days,” Shaw notes.

Harbor and the shift to a “benchmark factory”: Running evaluations in sandboxed containers is slow, and RL post-training requires thousands of rollouts, pushing benchmarking toward systems that can continuously generate and test new tasks at pace; as Shaw notes, “the only real solution is to keep making new benchmarks quickly.”

Scaling benchmarks to match real-world complexity: Even strong benchmarks capture only a slice of real-world coding, which creates a clear push toward expanding task diversity and difficulty; as Shaw notes, “89 tasks aren’t going to cover all of it… we need a thousand times more benchmarks.”

Closing the gap between benchmark performance and real-world use: Frontier models can achieve high scores on structured tasks, yet still struggle with robustness and iteration in practice, pointing to a rich area for improving task design and evaluation signals; as Shaw notes, models can “introduce a ton of complexity” and have “a relatively hard time building off [their] own work.”

More on Terminal-Bench: See the leaderboard and the catalog of tasks at tbench.ai.

Explore Harbor: Learn how to scale your agent evaluations atharborframework.com.

Watch the full interview on YouTube

Episode Transcript

Rapid Progress in Terminal-Bench 2

Vincent Chen: Welcome, Alex, to Benchtalks.

Alex Shaw: Thank you for having me.

Vincent Chen: Yeah, we’re super excited to have you here. So I guess first of all, four months ago we talked a bit about TB2 and Harbor after it launched. It’s had a ton of momentum since then. What has been most surprising in the last four months?

Alex Shaw: It’s a good question. I think two things have been pretty surprising.

First is how quickly the model developers have hill-climbed Terminal-Bench 2. When we were building it, while it was still in development, the scores we were seeing were around 20% to 30%. By the time we actually released it, the better models were scoring up to around 40% or 45%. And now the most recent submissions from OpenAI are around 75%. If you really build a custom harness around it, people have even gotten up to 80%.

I guess in school that still is a B-minus, so it’s not far enough. And we’ve actually seen that every single task in Terminal-Bench 2 has been solved at least one time by one agent–model combination over the course of the benchmark. So in theory, that means 100% is possible.

So there’s still 20% room to go. But yeah, we’re actively working on Terminal-Bench 3 because of this very reason. These benchmarks are very hill-climbable these days, which is good for users of agents—they get better agents because of it. But yeah, that was surprising.

And then the other surprising thing is how quickly Harbor was adopted. We put it out there as an experimental “hey, people seem to want this, we’ll see if they pick it up.” And yeah, people seem to like it.

What Fast Progress Says About Models

Vincent Chen: That’s awesome. On the first point, what do you think that says about either the benchmark or the models—that they’re hill-climbing so quickly? Any lessons or hot takes on that phenomenon?

Alex Shaw: It’s a little bit confusing, to be honest. The Terminal-Bench 2 tasks are very high quality. Terminal-Bench 3 will be even higher quality, so I’m excited about that.

But I think it’s a relatively difficult benchmark to reward-hack. So I do think the models are actually getting better at those specific types of tasks. But when I use Claude Code myself—I use it all the time when I’m coding—I still see a lot of shortcomings.

At 80% on Terminal-Bench, you’d think it would be solving every problem instantly. But it introduces a ton of complexity. It still has a relatively hard time building off its own work and producing robust and secure code.

That has me thinking a lot about how we encode more of these shortcomings into tasks in Terminal-Bench 3 or other benchmarks.

I think maybe the lesson is that coding is an extremely broad domain. Eighty-nine tasks aren’t going to cover all of it—we need a thousand times more benchmarks than we have right now.

Vincent Chen: Yeah, that’s a big part of our philosophy. It’s not just about evaluating models and snapshotting progress—it’s also about shaping where models are going and how they’re actually used in practice.

Capturing what I’m doing day-to-day that isn’t in benchmarks is really important for closing that gap. So very much agreed.

Why Terminal-Bench 2 Took Off

Vincent Chen: At a high level, what do you think made Terminal-Bench 2 stick and have the impact it did? You’re in all the recent model cards with Claude and Codex—even today, I think there’s a new one out. What made it stick?

Alex Shaw: I think we got a little bit lucky. And by that, I mean there are a few things you need for a benchmark to become a standard.

One is quality—tasks people care about, and tasks that aren’t easily reward-hackable.

Two, it needs to be easy to adopt. This is something we agonized over. What is the fewest number of characters someone can type to start running Terminal-Bench 2? In theory, if you have Docker, you can run it in a single line. That was a big one.

And then the last thing—something you have less control over—is making the right bet on a capability people care about that isn’t already being measured.

For us, that was the terminal as a tool for general computer use—not just coding, but arbitrary tasks.

And I have to credit Andy Konwinski and Ludwig Schmidt for a lot of the initial thinking there. They recognized that it’s a powerful text-based tool, and I think we executed well on that and expanded the vision.

Vincent Chen: I love that framing. Going deeper on the terminal—why is it the right abstraction? It feels broader than just CLI agents. Why is it such a strong foundational layer?

Why the Terminal Is the Right Abstraction

Alex Shaw: Before UI existed, it was just terminals. That’s how people interacted with computers.

So it makes sense that most things you do through a UI were originally done—or still can be done—through a terminal.

Also, these are language models. They’re better at text-based domains than vision-based ones. Most UIs are vision-heavy, so models naturally excel at writing commands, scripts, and code in the terminal.

And people underestimate how much you can do with a terminal.

For example, when I shop for groceries, I might use an app like Paprika, pick recipes, build a list, and export it to Reminders—all through a UI.

But I tried asking Claude Code if it could access the app. It found the SQLite database, read my recipes, generated a grocery list, and exported it to Reminders using Apple scripting libraries.

So you can do almost anything on a computer through the terminal.

How to Build High-Quality Benchmarks

Vincent Chen: On quality—what contributes to that? How do you maintain high quality at scale?

Alex Shaw: At first, there was no scale. It was just me and Mike making tasks. We quickly realized we couldn’t create enough high-quality tasks ourselves.

So we moved to a crowdsourced approach.

The biggest factor is having expert contributors who can recreate hard problems they’ve solved in their careers. Someone like Nicholas Carlini contributed a lot early on.

We also gave contributors tools—rubrics, LLM judges—to help validate their tasks.

And then there’s QA. Once tasks are created, we test them thoroughly: are they brittle? Reward-hackable? Should they be included?

All of that together led to a high-quality benchmark.

Vincent Chen: That resonates a lot. Generation isn’t the bottleneck—verification and quality control are. Tight feedback loops and early checks make a huge difference.

You’ve also had people try to game the leaderboard. How do you maintain integrity as it scales?

Preventing Cheating and Maintaining Integrity

Alex Shaw: Initially, people emailed results and we manually added them. That didn’t scale.

So we moved to a Hugging Face repo with automatic validation—checking configs, number of runs, etc.

But the biggest layer is transparency. All submissions are public. The community can inspect them.

There was a case where a contributor caught someone bundling gold trajectories into their agent. That’s what keeps integrity high.

That said, there are things we can’t detect—like whether a model was fine-tuned on our solutions. So the only real solution is to keep making new benchmarks quickly.

That’s what Harbor is about: building a benchmark factory, not just individual benchmarks.

Harbor: Vision and Growth

Vincent Chen: Let’s talk about Harbor. What’s the vision, and how has it evolved?

Alex Shaw: Initially, it was experimental—just to see if our infrastructure was useful.

We focused on usability: how simple is it to define tasks and run evaluations at scale?

The goal was always to support many benchmarks and let people create their own.

Now we’re seeing lots of usage—everything from SWE-bench to things like RuneBench (agents playing RuneScape).

We’ve adapted dozens of benchmarks, and now we’re expanding beyond coding into finance, law, and general automation tasks.

What Harbor Does Better

Vincent Chen: What gap does Harbor fill?

Alex Shaw: I was inspired by tools like Next.js—great developer experience.

We wanted to make something equally simple and usable.

There were already frameworks for running evaluations, but none were simple, flexible, and user-friendly at the same time.

Harbor abstracts most complexity while keeping flexibility. That’s what we got right.

Why Harbor Matters for Agents

Vincent Chen: Why should people building agents care?

Alex Shaw: Model and agent development are both highly empirical.

You need tools to measure performance and understand whether changes help or hurt.

Tasks also serve as a shared language—they define what capabilities matter. They’re like your product spec or roadmap.

Having a unified format and framework helps solve coordination across teams and organizations.

What Won’t Change in Evals

Vincent Chen: What are the long-term invariants?

Alex Shaw: There’s a lot of discussion about online learning, but I think offline workflows will remain critical.

We need to take real-world workflows and encode them into tasks for training and evaluation.

That’s going to remain central for years.

Also, companies are going to increasingly care about data and evaluations. They’ll turn workflows into tasks and optimize against them.

Demand for this will explode.

The Need for Verifier Benchmarks

Vincent Chen: What benchmarks do you want to see that don’t exist yet?

Alex Shaw: A meta-benchmark: measuring an agent’s ability to write verifiers.

Verification is often the hardest part of task creation.

If we could automate that, we could generate tasks at scale.

But we don’t currently have a good way to measure how well agents can create verifiers. That’s a big gap.

The Ideal Agent Development Loop

Vincent Chen: What does the ideal loop look like?

Alex Shaw: You take real workflows from production systems—like GitHub PRs in SWE-bench.

Use those to generate environments and instructions.

Then synthesize verifiers, with humans helping in the final step.

Once you have tasks, they become training signals. Then you deploy, collect traces, turn those into new tasks—and repeat.

That’s the flywheel.

Surprising Realities of Benchmarking

Vincent Chen: What surprises people about building benchmarks?

Alex Shaw: Creating tasks is more fun than people expect—especially if it’s based on a hard problem you’ve solved.

But reviewing tasks is much harder than people expect. It’s a grind to understand and evaluate someone else’s task.

So creation is exciting, but review is painful.

Terminal-Bench 3 and Call for Contributors

Vincent Chen: Anything else you want to share?

Alex Shaw: We’re working on Terminal-Bench 3, and this is probably the best opportunity for people to influence model development.

If we can get top contributors to submit their hardest problems, we can build the best benchmark yet—one that shapes the field.

We’re looking for contributions from people solving difficult, high-value problems.

Closing

Vincent Chen: Love it. If you want to shape AI, contribute to Terminal-Bench 3.

Thanks so much, Alex.

Alex Shaw: Thank you so much.

Vincent Chen: We’ll have you back soon. Thanks.

Share this article

Vincent Sunn Chen

Vincent Sunn Chen is a Research Fellow on the founding team at Snorkel AI. His work centers on systems for high quality AI evaluation & data development with experts in the loop. He currently leads the Open Benchmarks Grants, a $3M commitment to funding benchmarks and infrastructure for frontier agents. Prior to Snorkel, Vincent was a researcher at the Stanford AI Lab, where he studied the foundations of data-centric AI systems.

Recommended 
 articles

See all articles

Research

Benchmarks should shape the frontier, not just measure it

Since launching the Open Benchmarks Grants, we’ve received more than 100 applications from academic groups and industry labs spanning a wide range of domains and capabilities. As the best benchmarks drive how the field allocates research effort, the bar for benchmarks has risen as well. Here, we share what’s now table stakes for useful benchmarks, and what separates the ones…

Vincent Sunn Chen

 April 7, 2026 

Research

Building FinQA: An Open RL Environment for Financial Reasoning Agents

TL;DR: We built FinQA — a financial question-answering environment with 290 expert-curated questions across 22 public companies, now available on OpenEnv. Agents use MCP tools to discover schemas, write constrained SQL queries, and answer multi-step questions from real SEC 10-K filings. Most open-source models struggle with this kind of multi-step tool use, and even frontier closed-source models, while more accurate,…

Bhavishya Pohani

 March 30, 2026 

Research

How Tool Discipline Let a 4B Model Outsmart a 235B Giant on Financial Tasks

The Snorkel research team collaborated with the rLLM team at UC Berkeley on the Agentica project, using their open-source rLLM framework to fine-tune Qwen3-4B-Instruct-2507, delivering a model that beats Qwen3-235B-A22B on Snorkel AI’s expert-curated financial benchmarks – at 1/60th the size. A full breakdown of the results are published in the rLLM blog here. The key insight? Just focus on…

Chris Glaze

 February 18, 2026 

Join our newsletter for expert advice, the latest research, and exclusive events.

By submitting this form, I acknowledge I will receive email updates from Snorkel AI, and I agree to the Terms of Use and acknowledge that my information will be used in accordance with the Privacy Policy.

CONNECT WITH US

How do you want to work  with Snorkel?

AI data development services

Accelerate the development of frontier AI models with expert-curated, enterprise-grade data.

Learn how Snorkel’s Data-as-a-Service helps teams label, refine, and evaluate high-quality, domain-specific datasets for your projects.

Talk to a data researcher

AI solutions engineering

Explore how Snorkel can collaborate with your product and development teams to build and deploy custom AI and agentic systems.

Solutions undergo rigorous testing based on your business criteria to ensure positive ROI, faster.

Talk to a strategist

Become an expert contributor

Join the Snorkel Expert Contributor community and help shape the future of AI with your expertise. 

Contribute to groundbreaking projects, share domain-specific insights, and get rewarded for your impact.

Join now

Capabilities

Overview

Our technology

Enterprise AI solutions

Overview

Customer stories

Expert data services

Overview

Use cases

Join our expert community

Solutions

Industries

Banking & finance

Healthcare

Insurance

Public sector

Resources

Resource library

Events

Blog

Docs

AI Primers

Data-centric AI

Data labeling

Generative AI

Large language models

LLM evaluation

Research

Research hub

Leaderboards

Open Benchmarks Grants

Company

About

Careers

Press

Partners

Security

Contact us

Contact

Get started

Apply to join the expert network

Become a Data Development Partner

Compliance

Copyright © 2026 Snorkel AI, Inc. All rights reserved.

Terms of UsePrivacyCookie Policy
