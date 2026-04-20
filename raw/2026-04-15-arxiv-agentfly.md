---
source: arxiv
arxiv_id: "2508.16153"
title: "AgentFly: Fine-tuning LLM Agents without Fine-tuning LLMs"
authors: ["Huichi Zhou", "Yihang Chen", "Siyuan Guo", "Xue Yan", "Kin Hei Lee", "Zihan Wang", "Ka Yiu Lee", "Guchun Zhang", "Kun Shao", "Linyi Yang", "Jun Wang"]
date: 2025-08-22
url: "https://arxiv.org/abs/2508.16153"
fetched: 2026-04-15
status: pending_ingest
---

## Abstract

AgentFly introduces a novel learning framework for adaptive LLM agents that avoids fine-tuning underlying language models. The approach uses memory-based online reinforcement learning formalized as a Memory-augmented Markov Decision Process (M-MDP) with a neural case-selection policy. Past experiences are stored in episodic memory, enabling continual updates without gradient modifications to model parameters.

## Key Points

- Eliminates computational burden of fine-tuning LLMs by using memory-augmented RL
- Memory-augmented Markov Decision Process (M-MDP) with neural case-selection policy
- Top-1 on GAIA validation (87.88% Pass@3)
- Out-of-distribution robustness: +4.7% to 9.6% absolute improvement
- Enables generalist LLM agents with continuous, real-time learning without gradient updates
- 162 HuggingFace upvotes, highly discussed in community
