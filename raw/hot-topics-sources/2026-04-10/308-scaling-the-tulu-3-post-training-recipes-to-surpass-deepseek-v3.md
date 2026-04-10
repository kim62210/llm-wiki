---
title: Scaling the Tülu 3 post-training recipes to surpass the performance of DeepSeek V3  | Ai2
source_url: https://allenai.org/blog/tulu-3-405B
final_url: https://allenai.org/blog/tulu-3-405B
status: 200
content_type: text/html; charset=utf-8
topics: [Open Post-Training Recipes (Tülu 3 / OLMo 3)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:07.455132+00:00
---

# Scaling the Tülu 3 post-training recipes to surpass the performance of DeepSeek V3  | Ai2

## 원본 URL

https://allenai.org/blog/tulu-3-405B

## 추출 본문

Scaling the Tülu 3 post-training recipes to surpass the performance of DeepSeek V3 | Ai2

 Skip to main content ->

Ai2
Open models

Open models

Olmo

Tülu 3

Molmo

Playground

Language models

Multimodal models

Evaluation frameworks

Open data

Applications

AI for science

Asta

AstaBench

Research with Asta

Asta leaderboards

Semantic Scholar

All projects

AI for the planet

OlmoEarth

EarthRanger

Skylight

Climate Modeling

All projects

AI for robotics

Embodied AI

Research

Research

Latest

Papers

Research principles

News

Institute

Institute

About

Careers

Media center

Navigation Menu

Scaling the Tülu 3 post-training recipes to surpass the performance of DeepSeek V3

January 30, 2025

Ai2

Share

ModelsTech ReportDataCodeDemo

Following the success of our Tülu 3 release in November, we are thrilled to announce the launch of Tülu 3 405B—The first application of fully open post-training recipes to the largest open-weight models. With this release, we demonstrate the scalability and effectiveness of our post-training recipe applied at 405B parameter scale.

As outlined below, Tülu 3 405B achieves competitive or superior performance to both Deepseek v3 and GPT-4o, while surpassing prior open-weight post-trained models of the same size including Llama 3.1 405B Instruct and Nous Hermes 3 405B on many standard benchmarks. Interestingly, we found that our Reinforcement Learning from Verifiable Rewards (RLVR) framework improved the MATH performance more significantly at a larger scale, i.e., 405B compared to 70B and 8B, similar to the findings in the DeepSeek-R1 report. Overall, our results show a consistent edge over DeepSeek V3, especially with the inclusion of safety benchmarks.

A table mapping Tülu 3 405B performance compared to other current models across several evaluation benchmarks.

Scaling the Tülu 3 recipe

The primary objective of this release was to stress-test our novel RLVR approach and training infrastructure at large scales and extend the Tülu 3 recipe to the Llama-405B base model. Our training recipe for the 405B model followed very similarly to that of the 8B and 70B models introduced as part of Tulu 3 post-training recipe:

Careful data curation and synthesis targeting core skills

Supervised finetuning (SFT) on our carefully selected mix of prompts and their completions

Direct Preference Optimization (DPO) on both off- and on-policy preference data

RLVR, a new RL-based method to enhance specific skills with verifiable rewards

A standardized evaluation suite for development, decontamination, and final evaluation stage

RLVR training

In our post-training recipe, we leverage Reinforcement Learning with Verifiable Rewards (RLVR), a novel method we introduced for training language models on tasks with verifiable outcomes such as mathematical problem-solving and instruction following.

A diagram outlining the Reinforcement Learning with Verifiable Rewards (RLVR) process.

To scale RLVR at 405B scale, we deployed the model using vLLM with 16-way tensor parallelism, while utilizing the remaining 240 GPUs for training. After each RLVR iteration, the weights are synchronized to the vLLM engine using NCCL broadcast, which is made possible thanks to a recent fix suggestion by the vLLM team. In each RLVR iteration, the inference typically takes ~550 seconds, weight transfer takes ~25 seconds, and training takes ~1500 seconds. To reduce computational cost during the RLVR stage, we utilize an 8B value model. Future works can benefit from exploring larger value models or alternate value model-free RL algorithms such as GRPO.

We found that using MATH data exclusively—rather than a combination of GSM8k and IFEval data—yielded better results for larger models. This contrasts with findings when working with smaller models, which benefit from more diverse data. Our hypothesis is that larger models are better suited for complex tasks requiring specialized data.

In the figure below, we show the learning curves of verifiable rewards, KL divergence, and response length over episodes. Overall we are excited to find the verifiable rewards to go up like we have observed in the 8B and 70B settings. We mark the point with the final checkpoint with a star. We note that this was the last checkpoint saved – we intended to train longer but hit compute constraints. Since we did not observe that MATH performance had saturated during training, further training may further improve the performance.

Note that technically the metrics in MATH test split is accuracy, but here we multiply the accuracy by 10 to convert to verifiable rewards.

Technical Challenges

Scaling to 405B required several engineering efforts and posed a number of challenges:

Compute requirements: Training Tülu 3 405B demanded 32 nodes (256 GPUs) running in parallel. For inference, we deployed the model using vLLM with 16-way tensor parallelism, while utilizing the remaining 240 GPUs for training. While most of our codebase scaled well, we occasionally encountered NCCL timeout and synchronization issues that required meticulous monitoring and intervention.

Hyperparameter tuning challenges: Given the computational costs, hyperparameter tuning was limited. We followed the principle of “lower learning rates for larger models” consistent with prior practice with Llama models.

Despite these hurdles, our training pipeline proved robust, enabling us to release the largest model trained with a fully-open recipe to date. We’ve updated the paper with these 405B results and many details further explaining our evaluation results and methodology for all models in the Tülu 3 family.

Resources:

We’d love to know what you think – check out our paper, the Tülu 3 code, or try Tülu 3 405B in the Ai2 Playground.

Tülu 3 Recipe (paper)

Tülu 3 code

The Tülu 3 model family on Hugging Face

Tülu 3 405B in the Ai2 Playground

Discuss the release on alphaXiv!

Acknowledgements:

We thank the vLLM team (Kaichao You, Simon Mo, Woosuk Kwon, and Zhuohan Li) for their invaluable support in debugging NCCL weight transfer issues.

Tülu 3 405B is hosted on Google Cloud and will be available on Vertex.

Join us on Discord

Join Ai2's Discord server to talk about Tülu 3 405B or any of our open models, share your projects, and connect with other researchers and developers working on truly open AI.

Ai2 on Discord

•••

Follow us or share this post:

Ai2 on XAi2 on LinkedInShare on XShare on LinkedIn

Subscribe to receive monthly updates about the latest Ai2 news.

First Name

Last Name

Email

Sign up

Contact us

Questions about our work, or need support with one of our technologies?

Get in touch

Resources
Media center

Documentation

Careers

Team directory

Community
Discord

Reddit

X/Twitter

GitHub

Hugging Face

LinkedIn

Bluesky

Threads

Legal
Terms of use

Privacy policy

DMCA policy

Business code of conduct

Responsible use

© The Allen Institute for Artificial Intelligence - All Rights Reserved.
