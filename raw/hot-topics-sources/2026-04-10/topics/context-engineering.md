---
title: Context Engineering for Long-Horizon Agents
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Context Engineering for Long-Horizon Agents

## 기존 큐레이션 요약

- 정의: 장기 실행 에이전트가 제한된 컨텍스트 윈도우에 어떤 토큰을 넣을지 의도적으로 큐레이션하는 기술.
- 왜 중요한가: 2025년 9월 Anthropic의 "Effective Context Engineering" 블로그 이후 프롬프트 엔지니어링을 대체하는 새로운 패러다임으로 자리잡았고, 2026년 4월 현재 ICLR 2026 ACE 논문, ACON, AgentFold 등 후속 연구가 쏟아지면서 컨텍스트 윈도우 크기 경쟁이 끝났다는 합의가 형성되고 있다.

## 개별 원문 수집 스냅샷

### Effective context engineering for AI agents (Anthropic)

- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- raw snapshot: `raw/hot-topics-sources/2026-04-10/001-effective-context-engineering-for-ai-agents.md`
- 수집 제목: Effective context engineering for AI agents \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic Effective context engineering for AI agents Published Sep 29, 2025 Context is a critical but finite resource for AI agents. In this post, we explore strategies for effectively curating and managing the context that powers them. After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: context engineering. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?" Context refers to the set of tokens included when sampling from a l

### ACON: Optimizing Context Compression for Long-horizon LLM Agents

- URL: https://arxiv.org/abs/2510.00615
- raw snapshot: `raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md`
- 수집 제목: [2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents

[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.00615 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2510.00615 (cs) [Submitted on 1 Oct 2025 (v1), last revised 17 Oct 2025 (this version, v2)] Title:ACON: Optimizing Context Compression for Long-horizon LLM Agents Authors:Minki Kang, Wei-Ning Chen, Dongge Han, Huseyin A. Inan, Lukas Wut

### Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (ICLR 2026)

- URL: https://arxiv.org/abs/2510.04618
- raw snapshot: `raw/hot-topics-sources/2026-04-10/003-agentic-context-engineering-evolving-contexts-for-self-improving-language-models.md`
- 수집 제목: [2510.04618] Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

[2510.04618] Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.04618 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2510.04618 (cs) [Submitted on 6 Oct 2025 (v1), last revised 29 Mar 2026 (this version, v3)] Title:Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models Authors:Qizheng Zhang, Changran Hu, Shubhangi 

### AgentFold: Long-Horizon Web Agents with Proactive Context Management

- URL: https://arxiv.org/abs/2510.24699
- raw snapshot: `raw/hot-topics-sources/2026-04-10/004-agentfold-long-horizon-web-agents-with-proactive-context-management.md`
- 수집 제목: [2510.24699] AgentFold: Long-Horizon Web Agents with Proactive Context Management

[2510.24699] AgentFold: Long-Horizon Web Agents with Proactive Context Management Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2510.24699 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2510.24699 (cs) [Submitted on 28 Oct 2025] Title:AgentFold: Long-Horizon Web Agents with Proactive Context Management Authors:Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen Zhang, Zile Qiao, Xinyu Wang, Pengjun Xie, Fei Huang, Siheng Chen, 

### Context Rot: How Increasing Input Tokens Impacts LLM Performance (Chroma Research)

- URL: https://www.trychroma.com/research/context-rot
- raw snapshot: `raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md`
- 수집 제목: Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma

Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma Products Products SyncDatabaseAgent DocsEnterprisePricingResearch Resources Resources ChangelogUpdatesCommunityGitHubPackage Search Log inSign up Chroma Technical Report July 14, 2025 Context Rot: How Increasing Input Tokens Impacts LLM Performance Kelly Hong Anton Troynikov Jeff Huber Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks. In this report, we evaluate 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Our
