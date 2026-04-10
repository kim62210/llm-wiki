---
title: DAPO
source_url: https://dapo-sia.github.io
final_url: https://dapo-sia.github.io
status: 200
content_type: text/html; charset=utf-8
topics: [DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:02.103857+00:00
---

# DAPO

## 원본 URL

https://dapo-sia.github.io

## 추출 본문

DAPO

 DAPO: an Open-Source LLM Reinforcement Learning
 System at Scale
 

1ByteDance Seed2Institute for AI Industry Research (AIR), Tsinghua University3The University of Hong Kong
4SIA-Lab of Tsinghua AIR and ByteDance Seed

*Full author list in Contributions

PaperCodeDataModel

Introducing DAPO

 We propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm. By making our work publicly available, we provide the broader research community and society with practical access to scalable reinforcement learning, enabling all to benefit from these advancements. Our system is based on the awesome verl framework. Thanks for their great work!
 Applying DAPO training to Qwen2.5-32B base model proves to outperform the previous state-of-the-art DeepSeek-R1-Zero-Qwen-32B on AIME 2024, achieving 50% accuracy with 50% less training steps. 
 

 AIME 2024 Performance
 

Fully Open-Source

 To benefit the broader research community, we fully open-source the recipe of our RL training, including algorithm details, dataset, verifiers, model weights and infrastructures. We utilize verl to perform DAPO training using the Qwen-32B-Base model from scratch with 128 H20 GPUs. Our open-source experiments were conducted on the Volcano Engine Machine Learning Platform. 
 We will provide a full reproduction guideline on the Volcano Engine platform 
 to help users replicate our experiments.
 

Datasets

 We provide training and validation datasets for DAPO training.
 

 Training: DAPO-Math-17k, an elaborately curated math dataset. 
 

 Validation: AIME 2024 dataset.
 

Verifier

 We adopt a simple but robust rule-based verifier relying on string normalization and matching.
 

Training Script

 We provide the out-of-the-box script for DAPO training reproduction.
 

Algorithm Insights

 We propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm, which includes several key techniques as below. Detailed analysis and insights can be found in our technical report.
 

Clip-Higher, which promotes the diversity of the system and avoids entropy collapse. We observe an entropy-collapsing phenomenon in our initial experiments. We propose increasing the upper clip range of the importance sampling ratio in policy gradient loss to mitigate this problem.
 

Dynamic Sampling, which improves training efficiency and stability. We propose a strategy that performs dynamic sampling and filters out prompt groups with the accuracy equal to 1 and 0, keeping a consistent number of prompts with effective gradients across batches.
 

Token-level Policy Gradient Loss, which is critical in long-CoT RL scenarios.
 

Overlong Reward Shaping, which reduces reward noise and stabilizes training.
 

 This website is adapted from Nerfies and licensed under a Creative
 Commons Attribution-ShareAlike 4.0 International License.
