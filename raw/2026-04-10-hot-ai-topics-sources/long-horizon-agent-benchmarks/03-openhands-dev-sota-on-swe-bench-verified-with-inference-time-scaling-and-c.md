---
title: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model
source_url: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
fetched_via: reader
origin_topic: Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)
origin_section: Agent Architecture
origin_ref_label: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model (OpenHands)
fetched: 2026-04-10
---

# SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model

- 원본 URL: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
- 수집 경로: reader
- 연결된 토픽: Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)

## 요약 메모

# SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025 * [Product](https://openhands.dev/product) Features * [Terminal / CLI Agentic power from the command line](https://openhands.dev/product/cli) * [Web GUI Agentic development, made human.](https://openhands.dev/product/gui) * [SDK Build agents your way.](https://openhands.dev/product/sdk) * [Enterprise](https://openhands.dev/enterp

## 원문 추출

Title: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model

URL Source: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model

Published Time: 2026-01-13T16:38:03.983Z

Markdown Content:
# SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025

[![Image 1](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/6903891b9597f86d920507d1_Logo.svg)](https://openhands.dev/)

*   [Product](https://openhands.dev/product)

Features 
    *   [Terminal / CLI Agentic power from the command line](https://openhands.dev/product/cli)
    *   [Web GUI Agentic development, made human.](https://openhands.dev/product/gui)
    *   [SDK Build agents your way.](https://openhands.dev/product/sdk)

*   [Enterprise](https://openhands.dev/enterprise)
*   [Pricing](https://openhands.dev/pricing)
*   [Benchmarks](https://index.openhands.dev/home)
*   [Community](https://openhands.dev/community)
*   Resources  

Learn 
    *   [Docs](https://docs.openhands.dev/)
    *   [Manifesto](https://openhands.dev/manifesto)
    *   [Blog](https://openhands.dev/blog)

Company

    *   [Press](https://openhands.dev/press)
    *   [Careers](https://jobs.ashbyhq.com/OpenHands)
    *   [About](https://openhands.dev/about)
    *   [Contact](https://openhands.dev/contact)

[](https://github.com/OpenHands/OpenHands)

Build with SDK

[Build with SDK](https://docs.openhands.dev/sdk)

Try it live

[Try it live](https://app.all-hands.dev/)

Menu

Close

[← Back to Blog](https://openhands.dev/blog)
# SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model

![Image 2: OpenHands Inference-Time Scaling Result](https://cdn.prod.website-files.com/68ff4058b35616cdd47d5b59/6914ea781d6d5cf27100d131_6914ea769e3520100138ff4d_inference-time-scaling-fig.png)

Written by

Xingyao Wang

Published on

April 17, 2025

We're thrilled to announce that OpenHands has reached a new milestone, achieving state-of-the-art results on SWE-Bench Verified!

![Image 3: OpenHands Performance on Leaderboard](https://cdn.prod.website-files.com/68ff4058b35616cdd47d5b59/6914ea781d6d5cf27100d134_6914ea75cd16ddd77c06e4c5_leaderboard.png)

## SWE-Bench and OpenHands

to verify they have appropriately scoped unit tests and well-specified issue descriptions.

Due to its realism and the potential vast benefits of AI agents that could autonomously solve real-world software development challenges, it is used widely throughout academia and industry as a gold-standard for measuring the abilities of AI coding agents.

open-source software development agent, and its performance on this dataset is currently at 60.6% - not too shabby!

But we wondered, what happens if we really push the limits?

## Inference-Time Scaling: More Compute, Better Results

Our approach leverages a simple but powerful idea: for challenging software engineering tasks, trying multiple solutions and picking the best one can lead to better outcomes. Here's how it works:

This method of inference-time scaling lets us achieve substantially better results without modifying the underlying agent model and scaffold.

We observe log-linear performance improvement from 60.6% on a single trajectory rollout to 66.4% with five attempts, which will make

![Image 4: OpenHands Inference-Time Scaling Result](https://cdn.prod.website-files.com/68ff4058b35616cdd47d5b59/6914ea781d6d5cf27100d131_6914ea769e3520100138ff4d_inference-time-scaling-fig.png)

## Building a Better Critic

This idea of using choosing the best of multiple solutions has been tried by other SWE-bench submissions, but these strategies were generally based on prompting an existing model like Claude.

Rather than using this prompt-based reranking strategy, we trained a dedicated critic model, which we found provided more effective results.

For the training process, we:

- Roll out agent trajectories from 

 to avoid data leakage

- Implement a temporal difference (TD) learning objective to propagate trajectory-level success signals from unit test execution backward through each trajectory

- Add a regression head on top of the last layer to predict reward values

The TD learning objective is particularly powerful because it helps the model understand which actions contributed to the final outcome:

$$

r_t = \gamma r_{t+1}

$$

Where $r_t$ is the reward at time step $t$ (i.e., the t-th action produced by agent), $\gamma$ is the discount factor. The process starts with the final reward $r_T$ which is determined by running the unit tests on the completed solution - 1 for passing all tests and 0 for failing. This terminal reward is then propagated backwards through the trajectory, with each previous step discounted by $\gamma$. We use $\gamma=0.99$.

We use [veRL](https://github.com/volcengine/verl) to finetune [Qwen 2.5 Coder Instruct 32B](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) as a critic model. During inference, we use a [modified version of vLLM](https://github.com/xingyaoww/vllm/tree/add-token-classification-support) to serve this model for evaluation (fun fact: OpenHands agent itself wrote most of the functional [code](https://github.com/vllm-project/vllm/compare/main...xingyaoww:vllm:add-token-classification-support) there).

We're making the critic model [publicly available on huggingface](https://huggingface.co/all-hands/openhands-critic-32b-exp-20250417) for researchers who want to explore its capabilities or build upon our work.

## Why We Built a Critic Model and Where It's Going

We chose to invest in a trained critic model for several reasons:

**Genuine usefulness through generalization**: While prompt-engineering-based reranker can help boost benchmark scores, real-world generalization is not easy to guarantee. We believe with sufficient data, a trained critic model could generalize to diverse software engineering scenarios beyond SWE-Bench. This makes it a valuable tool for solving real-world problems in everyday coding tasks.

: While our current implementation focuses on selecting the best complete solution from multiple trajectories, the intermediate rewards predicted throughout each trajectory opens up exciting possibilities for enhancing our agent's capabilities.

- 

).

-

We're actively working on integrating these signals more deeply into the OpenHands agent experience, which could enable more efficient assistance even in scenarios where generating multiple complete solutions isn't practical.

## Try OpenHands Today

Besides being state-of-the-art on SWE-Bench Verified, OpenHands is also a top-performing agent on [LiveSWEBench](https://liveswebench.github.io/), a contamination-free benchmark for AI software engineers. Additionally, OpenHands ranks first on [Multi-SWE-Bench](https://multi-swe-bench.github.io/), a variant of SWE-Bench that evaluates across 8 different programming languages.

Overall, we feel confident in saying that OpenHands is the best agent out there for a wide variety of tasks!

If you'd like to try it out today you can:

We can't wait to see what you'll build with OpenHands!

Citation

![Image 5](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/690bb402fa20bacff3bb5938_Chevron%20Down.svg)

![Image 6](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/690bb44a27a9ac4d3ee54ba6_Copy.svg)

[![Image 7: The Software Agent Control Plane cover image](https://cdn.prod.website-files.com/68ff4058b35616cdd47d5b59/69d016ebf9996dd034605e68_cover.png) The Software Agent Control Plane](https://openhands.dev/blog/agent-control-plane)

[![Image 8](https://cdn.prod.website-files.com/68ff4058b35616cdd47d5b59/69c2a00864acdcfca728ebfc_202603-evoblog-1.webp) EvoClaw: Evaluating AI Agents on Continuous Software Evolution](https://openhands.dev/blog/evoclaw-benchmark)

[![Image 9](https://cdn.prod.website-files.com/68ff4058b35616cdd47d5b59/69ba745d32c2335c32230444_69ba7450d61c3bdd05ee50d5_evaluating-agent-skills-cover.png) How to Evaluate Agent Skills (And Why You Should)](https://openhands.dev/blog/evaluating-agent-skills)

# Get useful insights in our blog

Insights and updates from the OpenHands team

Sign up for our newsletter for updates, events, and community insights.

By submitting your email you agree to our [Privacy Policy](https://openhands.dev/privacy)

### Thank you for your submission!

Oops! Something went wrong while submitting the form.

Building the open standard for autonomous software development.

OpenHands is the foundation for secure, transparent, model-agnostic coding agents - empowering every software team to build faster with full control.

Build with SDK

[Build with SDK](https://docs.openhands.dev/sdk)

Try it live

[Try it live](https://app.all-hands.dev/)

[![Image 10](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/6908d21b2270590dedae7f30_Frame%2048095725.svg)](https://openhands.dev/joinslack)

[![Image 11](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/6908d21bd2a1305f4f77161b_Frame%2048095723.svg)](https://x.com/OpenHandsDev)

[![Image 12](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/6908d21a36dee3e7147b3d21_Frame%2048095724.svg)](https://github.com/OpenHands/OpenHands)

[Home](https://openhands.dev/)[Product](https://openhands.dev/product)[Enterprise](https://openhands.dev/enterprise)[Pricing](https://openhands.dev/pricing)[About](https://openhands.dev/about)

[Resources](https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model#)[Community](https://openhands.dev/community)[Manifesto](https://openhands.dev/manifesto)[Docs](https://docs.openhands.dev/)[Blog](https://openhands.dev/blog)[Press](https://openhands.dev/press)[Careers](https://jobs.ashbyhq.com/OpenHands)

[Contact](https://openhands.dev/contact)

©2025 OpenHands - All rights reserved

[Privacy Policy](https://openhands.dev/privacy)

![Image 13](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/6908d2235830415ac045d25d_openhands_logo_black.svg)

![Image 14](https://cdn.prod.website-files.com/68ff4057b35616cdd47d5ac7/6908d170831c19b2b6976323_ascii-art%20(16)%201.svg)

