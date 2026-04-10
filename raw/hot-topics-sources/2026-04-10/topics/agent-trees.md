---
title: Hierarchical Planning with Agent Trees
section: Agent Architecture
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Hierarchical Planning with Agent Trees

## 기존 큐레이션 요약

- 정의: 복잡한 목표를 동적으로 구성되는 에이전트 트리로 분해하고 제어 흐름 노드로 서브에이전트들을 조정하는 계획 방식.
- 왜 중요한가: AAMAS 2026에 채택된 ReAcTree가 Qwen 2.5 72B로 ReAct(31%) 대비 61% 성공률을 달성하며 트리 기반 분해의 우월성을 입증했고, Plan-and-Act, Plan-Then-Execute, 다층 메모리 계획기 등이 동시 등장하면서 평면적 ReAct 루프의 한계가 명확해졌다.

## 개별 원문 수집 스냅샷

### ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

- URL: https://arxiv.org/abs/2511.02424
- raw snapshot: `raw/hot-topics-sources/2026-04-10/030-reactree-hierarchical-llm-agent-trees-with-control-flow-for-long-horizon-task-pl.md`
- 수집 제목: [2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

[2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2511.02424 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2511.02424 (cs) [Submitted on 4 Nov 2025 (v1), last revised 10 Feb 2026 (this version, v2)] Title:ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning Authors:Jae-Woo Choi, Hyung

### Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks

- URL: https://arxiv.org/abs/2503.09572
- raw snapshot: `raw/hot-topics-sources/2026-04-10/031-plan-and-act-improving-planning-of-agents-for-long-horizon-tasks.md`
- 수집 제목: [2503.09572] Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks

[2503.09572] Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2503.09572 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2503.09572 (cs) [Submitted on 12 Mar 2025 (v1), last revised 22 Apr 2025 (this version, v3)] Title:Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks Authors:Lutfi Eren Erdogan, Nicholas Lee, Sehoon Kim, Suhong Moon, Hi

### Deep Research Agents: A Systematic Examination And Roadmap

- URL: https://arxiv.org/abs/2506.18096
- raw snapshot: `raw/hot-topics-sources/2026-04-10/032-deep-research-agents-a-systematic-examination-and-roadmap.md`
- 수집 제목: [2506.18096] Deep Research Agents: A Systematic Examination And Roadmap

[2506.18096] Deep Research Agents: A Systematic Examination And Roadmap Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2506.18096 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Artificial Intelligence arXiv:2506.18096 (cs) [Submitted on 22 Jun 2025 (v1), last revised 3 Sep 2025 (this version, v2)] Title:Deep Research Agents: A Systematic Examination And Roadmap Authors:Yuxuan Huang, Yihang Chen, Haozheng Zhang, Kang Li, Huichi Zhou, Meng Fang, L

### SkyworkAI/DeepResearchAgent (Hierarchical Multi-Agent System)

- URL: https://github.com/SkyworkAI/DeepResearchAgent
- raw snapshot: `raw/hot-topics-sources/2026-04-10/033-skyworkai-deepresearchagent.md`
- 수집 제목: GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains. · GitHub

GitHub - SkyworkAI/DeepResearchAgent: DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains. · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub CopilotWrite better code with AI GitHub SparkBuild and deploy intelligent apps GitHub ModelsManage and compare prompts MCP RegistryNewIntegrate external tools DEVELOPER WORKFLOWS ActionsAutomate any workflow CodespacesInstant dev environments IssuesPlan and track work Code ReviewManage code change

### How we built our multi-agent research system (Anthropic)

- URL: https://www.anthropic.com/engineering/multi-agent-research-system
- raw snapshot: `raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md`
- 수집 제목: How we built our multi-agent research system \ Anthropic

Skip to main contentSkip to footer Research Economic Futures Commitments Learn News Try Claude Engineering at Anthropic How we built our multi-agent research system Published Jun 13, 2025 Our Research feature uses multiple Claude agents to explore complex topics more effectively. We share the engineering challenges and the lessons we learned from building this system. Claude now has Research capabilities that allow it to search across the web, Google Workspace, and any integrations to accomplish complex tasks. The journey of this multi-agent system from prototype to production taught us critical lessons about system architecture, tool design, and prompt engineering. A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together. Our Research fea
