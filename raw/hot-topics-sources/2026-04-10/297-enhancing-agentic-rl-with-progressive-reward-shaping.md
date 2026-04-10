---
title: [2512.07478] Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization
source_url: https://arxiv.org/abs/2512.07478
final_url: https://arxiv.org/abs/2512.07478
status: 200
content_type: text/html; charset=utf-8
topics: [Agentic RL (Tool-Integrated Reasoning 학습)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.620448+00:00
---

# [2512.07478] Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization

## 원본 URL

https://arxiv.org/abs/2512.07478

## 추출 본문

[2512.07478] Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization
Skip to main content

Learn about arXiv becoming an independent nonprofit.

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate

>cs> arXiv:2512.07478
 

Help | Advanced Search

All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text

Search

GO

quick links

Login

Help Pages

About

Computer Science > Computation and Language

arXiv:2512.07478 (cs)
 

 [Submitted on 8 Dec 2025 (v1), last revised 20 Jan 2026 (this version, v2)]

Title:Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization

Authors:Jianghao Su, Xia Zeng, Luhui Liu, Chao Luo, Ye Chen, Zhuoran Zhuang

View a PDF of the paper titled Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization, by Jianghao Su and 5 other authors
View PDFHTML (experimental)
Abstract:Large Language Models (LLMs) empowered with Tool-Integrated Reasoning (TIR) can iteratively plan, call external tools, and integrate returned information to solve complex, long-horizon reasoning tasks. Agentic Reinforcement Learning (Agentic RL) optimizes such models over full tool-interaction trajectories, but two key challenges hinder effectiveness: (1) Sparse, non-instructive rewards, such as binary 0-1 verifiable signals, provide limited guidance for intermediate steps and slow convergence; (2) Gradient degradation in Group Relative Policy Optimization (GRPO), where identical rewards within a rollout group yield zero advantage, which reducing sample efficiency. To address these challenges, we propose two complementary techniques: Progressive Reward Shaping (PRS) and Value-based Sampling Policy Optimization (VSPO). PRS is a curriculum-inspired reward design that introduces dense, stage-wise feedback - encouraging models to first master parseable and properly formatted tool calls, then optimize for factual correctness and answer quality. We instantiate PRS for short-form QA (with a length-aware BLEU to fairly score concise answers) and long-form QA (with LLM-as-a-Judge scoring to prevent reward hacking). VSPO is an enhanced GRPO variant that replaces zero advantages samples with prompts selected by a task-value metric balancing difficulty and uncertainty, and applies value-smoothing clipping to stabilize gradient updates. Experiments on multiple short-form and long-form QA benchmarks show that PRS consistently outperforms traditional binary rewards, and VSPO achieves superior stability, faster convergence, and higher final performance compared to SFT, PPO and GRPO baselines. Together, PRS and VSPO yield LLM-based TIR agents that generalize better across domains.
 

Subjects:Computation and Language (cs.CL)Cite as:arXiv:2512.07478 [cs.CL](or arXiv:2512.07478v2 [cs.CL] for this version)
 https://doi.org/10.48550/arXiv.2512.07478
Focus to learn more
 arXiv-issued DOI via DataCite

Submission history
 From: Xia Zeng [view email] 
[v1]
 Mon, 8 Dec 2025 11:59:25 UTC (4,126 KB)
[v2]
 Tue, 20 Jan 2026 12:16:48 UTC (4,259 KB)

Full-text links:
Access Paper:

View a PDF of the paper titled Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization, by Jianghao Su and 5 other authors

View PDF

HTML (experimental)

TeX Source
 

view license

 Current browse context: 
cs.CL

< prev  |  next >

new | recent | 2025-12

 Change to browse by:
 
cs

References & Citations

NASA ADS

Google Scholar

Semantic Scholar

export BibTeX citationLoading...

BibTeX formatted citation
×

loading...

Data provided by: 

Bookmark

Bibliographic Tools

Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer(What is the Explorer?)

Connected Papers Toggle

Connected Papers(What is Connected Papers?)

Litmaps Toggle

Litmaps(What is Litmaps?)

scite.ai Toggle

scite Smart Citations(What are Smart Citations?)

Code, Data, Media

Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv(What is alphaXiv?)

Links to Code Toggle

CatalyzeX Code Finder for Papers(What is CatalyzeX?)

DagsHub Toggle

DagsHub(What is DagsHub?)

GotitPub Toggle

Gotit.pub(What is GotitPub?)

Huggingface Toggle

Hugging Face(What is Huggingface?)

Links to Code Toggle

Papers with Code(What is Papers with Code?)

ScienceCast Toggle

ScienceCast(What is ScienceCast?)

Demos

Demos

Replicate Toggle

Replicate(What is Replicate?)

Spaces Toggle

Hugging Face Spaces(What is Spaces?)

Spaces Toggle

TXYZ.AI(What is TXYZ.AI?)

Related Papers

Recommenders and Search Tools

Link to Influence Flower

Influence Flower(What are Influence Flowers?)

Core recommender toggle

CORE Recommender(What is CORE?)

Author

Venue

Institution

Topic

 About arXivLabs
 

arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)
 

About

Help

 Contact

 Subscribe

Copyright

Privacy Policy

Web Accessibility Assistance

arXiv Operational Status
