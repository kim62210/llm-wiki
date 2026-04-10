---
title: SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025
source_url: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
final_url: https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
status: 200
content_type: text/html; charset=utf-8
topics: [Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)]
sections: [Agent Architecture]
fetched_at: 2026-04-10T01:43:29.048085+00:00
---

# SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025

## 원본 URL

https://openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model

## 추출 본문

SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model | Nov 12, 2025

Product

Features

Terminal / CLI

Agentic power from the command line

Web GUI

Agentic development, made human.

SDK

Build agents your way.

Enterprise

Pricing

Benchmarks

Community

Resources

Learn

Docs

Manifesto

Blog

Company

Press

Careers

About

Contact

Build with SDK

Build with SDK

Try it live

Try it live

Menu

Close

← Back to Blog

SOTA on SWE-Bench Verified with Inference-Time Scaling and Critic Model

Written by

Xingyao Wang

Published on

April 17, 2025

We're thrilled to announce that OpenHands has reached a new milestone, achieving state-of-the-art results on SWE-Bench Verified!

SWE-Bench and OpenHands

 to verify they have appropriately scoped unit tests and well-specified issue descriptions.
Due to its realism and the potential vast benefits of AI agents that could autonomously solve real-world software development challenges, it is used widely throughout academia and industry as a gold-standard for measuring the abilities of AI coding agents.

 open-source software development agent, and its performance on this dataset is currently at 60.6% - not too shabby!
But we wondered, what happens if we really push the limits?

Inference-Time Scaling: More Compute, Better Results

Our approach leverages a simple but powerful idea: for challenging software engineering tasks, trying multiple solutions and picking the best one can lead to better outcomes. Here's how it works:

This method of inference-time scaling lets us achieve substantially better results without modifying the underlying agent model and scaffold.
We observe log-linear performance improvement from 60.6% on a single trajectory rollout to 66.4% with five attempts, which will make 

Building a Better Critic

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

We use veRL to finetune Qwen 2.5 Coder Instruct 32B as a critic model. During inference, we use a modified version of vLLM to serve this model for evaluation (fun fact: OpenHands agent itself wrote most of the functional code there).

We're making the critic model publicly available on huggingface for researchers who want to explore its capabilities or build upon our work.

Why We Built a Critic Model and Where It's Going

We chose to invest in a trained critic model for several reasons:

Genuine usefulness through generalization: While prompt-engineering-based reranker can help boost benchmark scores, real-world generalization is not easy to guarantee. We believe with sufficient data, a trained critic model could generalize to diverse software engineering scenarios beyond SWE-Bench. This makes it a valuable tool for solving real-world problems in everyday coding tasks.

: While our current implementation focuses on selecting the best complete solution from multiple trajectories, the intermediate rewards predicted throughout each trajectory opens up exciting possibilities for enhancing our agent's capabilities.
- 
).
- 

We're actively working on integrating these signals more deeply into the OpenHands agent experience, which could enable more efficient assistance even in scenarios where generating multiple complete solutions isn't practical.

Try OpenHands Today

Besides being state-of-the-art on SWE-Bench Verified, OpenHands is also a top-performing agent on LiveSWEBench, a contamination-free benchmark for AI software engineers. Additionally, OpenHands ranks first on Multi-SWE-Bench, a variant of SWE-Bench that evaluates across 8 different programming languages.

Overall, we feel confident in saying that OpenHands is the best agent out there for a wide variety of tasks!
If you'd like to try it out today you can:

We can't wait to see what you'll build with OpenHands!

Citation

The Software Agent Control Plane

EvoClaw: Evaluating AI Agents on Continuous Software Evolution

How to Evaluate Agent Skills (And Why You Should)

Get useful insights in our blog

Insights and updates from the OpenHands team

Sign up for our newsletter for updates, events, and community insights.

By submitting your email you agree to our Privacy Policy

Thank you for your submission!

Oops! Something went wrong while submitting the form.

Building the open standard for autonomous software development.

OpenHands is the foundation for secure, transparent, model-agnostic coding agents - empowering every software team to build faster with full control.

Build with SDK

Build with SDK

Try it live

Try it live

HomeProductEnterprisePricingAbout
ResourcesCommunityManifestoDocsBlogPressCareers
Contact

© 2025 OpenHands - All rights reserved
Privacy Policy
