---
title: Context Folding & Sub-Trajectory Compression
category: agents
page_type: concept
tags: [agents, concept, context, folding]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/context-folding.md, raw/hot-topics-sources/2026-04-10/029-scaling-long-horizon-llm-agent-via-context-folding.md, raw/hot-topics-sources/2026-04-10/004-agentfold-long-horizon-web-agents-with-proactive-context-management.md, raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md, raw/hot-topics-sources/2026-04-10/001-effective-context-engineering-for-ai-agents.md, raw/hot-topics-sources/2026-04-10/005-context-rot-how-increasing-input-tokens-impacts-llm-performance.md]
created: 2026-04-10
updated: 2026-04-10
---
# Context Folding & Sub-Trajectory Compression

에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법.

## 왜 중요한가

2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.

## 대표 레퍼런스

- [Scaling Long-Horizon LLM Agent via Context-Folding (FoldGRPO)](https://arxiv.org/abs/2510.11967)
- [AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699)
- [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615)
- [Effective context engineering for AI agents (Anthropic)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)

## 해석 포인트

Context Folding & Sub-Trajectory Compression은 **성능만이 아니라 운영 설계까지 함께 봐야 하는 축** 으로 이해할 때 가장 명확하다. 이번 source 묶음이 `arxiv.org×3, anthropic.com×1, trychroma.com×1`처럼 분산돼 있다는 것은, 이 주제가 단일 주장보다 여러 층위의 검증을 거치고 있다는 뜻이다.

실무적으로는 개념 정의 자체보다 **어떤 병목을 해결하고 어떤 비용을 새로 만들까**를 묻는 편이 유익하다. 그래서 이 토픽은 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성를 기준으로 비교·실험하는 식으로 다루는 것이 좋다.

## 2026년 4월 큐레이션 요약

- 정의: 에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법.
- 왜 중요한가: 2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.
- 직접 수집 원문: 5개
- 주요 도메인: arxiv.org×3, anthropic.com×1, trychroma.com×1

## 핵심 구조

에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법. 에이전트 토픽은 보통 모델 자체보다 **루프 구조, 상태 관리, 작업 분해, 검증 방식**이 핵심이다. 이번 source 묶음도 `arxiv.org×3, anthropic.com×1, trychroma.com×1`를 오가며 설계 패턴과 구현 사례를 함께 보여 준다.

## 핵심 포인트

Context Folding & Sub-Trajectory Compression는 현재 시점의 핵심 개념을 정리한 페이지다. 출발점은 에이전트가 서브태스크 단위로 분기한 뒤 완료 시 그 구간을 요약으로 압축해 활성 컨텍스트를 10배 가까이 줄이는 기법.이며, 직접 수집한 source 5건은 이 개념이 연구·문서·구현으로 어떻게 확장되는지 보여준다.

## source로 보면

수집된 source는 arxiv.org×3, anthropic.com×1, trychroma.com×1로 분포한다. 연구 논문과 공식 문서가 함께 있어 원리와 제품화 흐름을 같이 읽을 수 있다.

## 실무 관점

실무에서는 장기 실행, 상태 관리, 실패 복구, 평가 루프를 함께 설계해야 이 토픽이 효과를 낸다. 즉 개별 아이디어보다 에이전트 시스템 전체의 제약 속에서 읽는 것이 중요하다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/context-folding.md`

### source별 핵심 신호

- **[2510.11967] Scaling Long-Horizon LLM Agent via Context-Folding** (`arxiv.org`): https://arxiv.org/abs/2510.11967
  - 메모: Large language model (LLM) agents are fundamentally constrained by context length on long-horizon tasks. We introduce Context-Folding, a framework that empowers agents to actively manage their working context.
- **[2510.24699] AgentFold: Long-Horizon Web Agents with Proactive Context Management** (`arxiv.org`): https://arxiv.org/abs/2510.24699
  - 메모: LLM-based web agents show immense promise for information seeking, yet their effectiveness on long-horizon tasks is hindered by a fundamental trade-off in context management.
- **[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents** (`arxiv.org`): https://arxiv.org/abs/2510.00615
  - 메모: Large language models (LLMs) are increasingly deployed as agents in dynamic, real-world environments, where success requires both reasoning and effective tool use.
- **Effective context engineering for AI agents \ Anthropic** (`anthropic.com`): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - 메모: Effective context engineering for AI agents
- **Context Rot: How Increasing Input Tokens Impacts LLM Performance·|·Chroma** (`trychroma.com`): https://www.trychroma.com/research/context-rot
  - 메모: Context Rot: How Increasing Input Tokens Impacts LLM Performance


## source 종합 해석

예를 들어 source note는 Large language model (LLM) agents are fundamentally constrained by context length on long-horizon tasks. We introduce Context-Folding, a framework that empowers agents to actively manage their working context.

또 다른 source는 LLM-based web agents show immense promise for information seeking, yet their effectiveness on long-horizon tasks is hindered by a fundamental trade-off in context management.

즉, 이 토픽이 중요한 이유는 `2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.`라는 한 문장보다, 여러 source가 같은 문제를 서로 다른 층위(개념·측정·구현)에서 지지한다는 데 있다.

함께 읽을 문서로는 2026년 4월 AI 개발 핫토픽 100선, Long-Horizon RL Training for Agents (Multi-Turn RLVR), Hierarchical Planning with Agent Trees가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- source note가 추상 개념/실험 결과/운영 사례 중 어디에 치우쳐 있는지 보면, 이 토픽을 실무에서 어떻게 다뤄야 하는지가 드러난다.
- `2025년 10월 ByteDance의 "Scaling Long-Horizon LLM Agent via Context-Folding"이 ReAct 베이스라인 대비 10배 작은 컨텍스트로 동등 성능을 보였고, 후속 AgentFold가 BrowseComp에서 OpenAI o4-mini를 능가하면서 단순 컨텍스트 확장이 아닌 능동적 압축이 long-horizon 에이전트의 핵심임이 확립되었다.`라는 중요도 설명은 보통 과장되기 쉬우므로, 구체적 수치·벤치마크·운영 사례를 같이 확인해야 한다.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[long-horizon-rl-training-for-agents|Long-Horizon RL Training for Agents (Multi-Turn RLVR)]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[subagents|Subagents]]
