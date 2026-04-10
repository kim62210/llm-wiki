---
title: Context Folding & Sub-Trajectory Compression
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Context Folding & Sub-Trajectory Compression

## 기존 큐레이션 요약

- 정의: 에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법.
- 왜 중요한가: 2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.

## 개별 원문 수집 스냅샷

### Scaling Long-Horizon LLM Agent via Context-Folding (FoldGRPO)

- URL: https://arxiv.org/abs/2510.11967
- raw snapshot: `raw/hot-topics-sources/2026-04-10/029-scaling-long-horizon-llm-agent-via-context-folding.md`
- 수집 제목: [2510.11967] Scaling Long-Horizon LLM Agent via Context-Folding

[2510.11967] Scaling Long-Horizon LLM Agent via Context-Folding Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.11967 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2510.11967 (cs) [Submitted on 13 Oct 2025] Title:Scaling Long-Horizon LLM Agent via Context-Folding Authors:Weiwei Sun, Miao Lu, Zhan Ling, Kang Liu, Xuesong Yao, Yiming Yang, Jiecao Chen View a PDF of the paper titled Scaling Long-Horizon LLM Agent

### AgentFold: Long-Horizon Web Agents with Proactive Context Management

- URL: https://arxiv.org/abs/2510.24699
- raw snapshot: `raw/hot-topics-sources/2026-04-10/004-agentfold-long-horizon-web-agents-with-proactive-context-management.md`
- 수집 제목: [2510.24699] AgentFold: Long-Horizon Web Agents with Proactive Context Management

[2510.24699] AgentFold: Long-Horizon Web Agents with Proactive Context Management Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.24699 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2510.24699 (cs) [Submitted on 28 Oct 2025] Title:AgentFold: Long-Horizon Web Agents with Proactive Context Management Authors:Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen Zhang, Zile Qiao, Xinyu Wang, Pengjun Xie, Fei Huang, Siheng Chen, 

### ACON: Optimizing Context Compression for Long-horizon LLM Agents

- URL: https://arxiv.org/abs/2510.00615
- raw snapshot: `raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md`
- 수집 제목: [2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents

[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.00615 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2510.00615 (cs) [Submitted on 1 Oct 2025 (v1), last revised 17 Oct 2025 (this version, v2)] Title:ACON: Optimizing Context Compression for Long-horizon LLM Agents Authors:Minki Kang, Wei-Ning Chen, Dongge Han, Huseyin A. Inan, Lukas Wut

### Effective context engineering for AI agents (Anthropic)

- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/001-effective-context-engineering-for-ai-agents.md`
- 수집 제목: Effective context engineering for AI agents \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Effective context engineering for AI agents Published Sep 29, 2025 Context is a critical but finite resource for AI agents. In this post, we explore strategies for effectively curating and managing the context that powers them. After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: context engineering. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?" Context refers to the set of tokens included when sampling from a l

### Context Rot: How Increasing Input Tokens Impacts LLM Performance

- URL: https://www.trychroma.com/research/context-rot
- raw snapshot: `raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md`
- 수집 제목: Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma

Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma Products Products SyncDatabaseAgent DocsEnterprisePricingResearch Resources Resources ChangelogUpdatesCommunityGitHubPackage Search Log inSign up Chroma Technical Report July 14, 2025 Context Rot: How Increasing Input Tokens Impacts LLM Performance Kelly Hong Anton Troynikov Jeff Huber Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks. In this report, we evaluate 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Our
