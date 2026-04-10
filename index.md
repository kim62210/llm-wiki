---
title: AI Development Study Wiki - Index
updated: 2026-04-10
---

# AI Development Study Wiki

AI/ML 개발 학습 지식 베이스. 소스를 `raw/`에 넣으면 LLM이 구조화된 위키로 컴파일한다.

> **분류 체계**: 각 페이지는 **카테고리(주제)**와 **페이지 타입(성격)**의 두 축으로 분류된다. 카테고리별 섹션 안에서 타입별 서브섹션으로 구분. 상세 규칙은 `CLAUDE.md` 참조.
## 카테고리

### Foundations (기초)

> 아직 페이지 없음 - 소스 수집 필요

### Architectures (모델 구조)

> 아직 페이지 없음 - 소스 수집 필요

### Training (학습)

**concept**
- [Agentic RL (Tool-Integrated Reasoning 학습)](wiki/training/agentic-rl.md) — 이 페이지는 Agentic RL (Tool-Integrated Reasoning 학습)를 다룬다. 핵심은 도구 호출 궤적 전체를 RL로 최적화하는 에이전트 post-training 패러다임이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Corpus-Grounded Self-Play (SPICE 계열)](wiki/training/corpus-grounded-self-play.md) — 이 페이지는 Corpus-Grounded Self-Play (SPICE 계열)를 다룬다. 핵심은 외부 문서 코퍼스를 근거로 한 모델이 문제를 만들고 풀며 자기개선하는 RL이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)](wiki/training/dapo.md) — 이 페이지는 DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)를 다룬다. 핵심은 Clip-Higher, Dynamic Sampling 등 4가지 기법을 결합한 대규모 추론 RL 시스템이며, 2026년 4월 시점에 왜 다시 중
- [GRPO (Group Relative Policy Optimization)](wiki/training/grpo.md) — 이 페이지는 GRPO (Group Relative Policy Optimization)를 다룬다. 핵심은 크리틱 없이 그룹 내 보상 정규화로 어드밴티지를 계산하는 PPO 변형이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [On-Policy Distillation](wiki/training/on-policy-distillation.md) — 이 페이지는 On-Policy Distillation를 다룬다. 핵심은 학생이 직접 롤아웃한 궤적에 교사 모델이 토큰별 밀집 피드백을 주는 증류 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Process Reward Models (PRM) 재부상](wiki/training/process-reward-models.md) — 이 페이지는 Process Reward Models (PRM) 재부상를 다룬다. 핵심은 추론 과정의 각 단계를 평가해 보상을 주는 스텝-레벨 검증자 모델이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [RL Scaling Laws (ScaleRL)](wiki/training/rl-scaling-laws.md) — 이 페이지는 RL Scaling Laws (ScaleRL)를 다룬다. 핵심은 RL 컴퓨트 규모에 따른 성능을 예측 가능한 곡선으로 모델링하는 방법론이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [RLVR (Reinforcement Learning with Verifiable Rewards)](wiki/training/rlvr.md) — 이 페이지는 RLVR (Reinforcement Learning with Verifiable Rewards)를 다룬다. 핵심은 정답 검증 가능한 과제에서 보상 신호로 학습시키는 RL 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Test-Time Training & Self-Improvement](wiki/training/test-time-training-and-self-improvement.md) — title: Test-Time Training & Self-Improvement

**summary**
- [Open Post-Training Recipes (Tülu 3 / OLMo 3)](wiki/training/open-post-training-recipes.md) — 이 페이지는 Open Post-Training Recipes (Tülu 3 / OLMo 3)를 요약하고, 지금 시점에 왜 중요한지 빠르게 따라잡기 위한 페이지다. 핵심 범위는 SFT → DPO → RLVR 전체 파이프라인을 완전 공개한 오픈소스 post-training 레시피이다.

### Inference (추론/서빙)

**entity**
- [AMD ROCm as First-Class vLLM Platform](wiki/inference/vllm-rocm-platform.md) — title: AMD ROCm as First-Class vLLM Platform
- [FlashInfer Kernel Library for LLM Serving](wiki/inference/flashinfer.md) — title: FlashInfer Kernel Library for LLM Serving
- [llm-d & Gateway API Inference Extension](wiki/inference/llm-d.md) — title: llm-d & Gateway API Inference Extension
- [LMCache + Mooncake KV Cache Layer](wiki/inference/lmcache.md) — title: LMCache + Mooncake KV Cache Layer
- [LMCache-Based Distributed KV Cache Offloading](wiki/inference/lmcache-kv-cache-layer.md) — title: LMCache-Based Distributed KV Cache Offloading
- [NVIDIA Dynamo 1.0 Inference OS](wiki/inference/nvidia-dynamo.md) — title: NVIDIA Dynamo 1.0 Inference OS
- [SGLang on GB300 NVL72 with NVFP4](wiki/inference/sglang.md) — title: SGLang on GB300 NVL72 with NVFP4
- [TensorRT-LLM 1.3 with Day-0 Model Support](wiki/inference/tensorrt-llm.md) — title: TensorRT-LLM 1.3 with Day-0 Model Support
- [vLLM V1 Engine on Blackwell (GB200/GB300)](wiki/inference/vllm-v1-engine.md) — title: vLLM V1 Engine on Blackwell (GB200/GB300)
- [XGrammar-2 Constrained Decoding for Agentic LLMs](wiki/inference/xgrammar-2.md) — title: XGrammar-2 Constrained Decoding for Agentic LLMs

**concept**
- [Chunk-Semantic KV Cache Compression](wiki/inference/kv-cache-compression.md) — title: Chunk-Semantic KV Cache Compression
- [DeepSeek Sparse Attention (DSA) for Long Context](wiki/inference/deepseek-sparse-attention.md) — title: DeepSeek Sparse Attention (DSA) for Long Context
- [EAGLE-3 Speculative Decoding](wiki/inference/eagle-3-speculative-decoding.md) — 이 페이지는 EAGLE-3 Speculative Decoding를 다룬다. 핵심은 멀티레이어 피처 융합과 training-time test로 드래프트 헤드를 학습시키는 가속법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [FlashAttention-4 on Blackwell](wiki/inference/flashattention-4.md) — title: FlashAttention-4 on Blackwell
- [KV Cache (Key-Value 캐시)](wiki/inference/kv-cache.md) — KV Cache (Key-Value Cache)는 LLM 추론 과정에서 계산된 Transformer 어텐션의 Key와 Value 가중치를 저장하는 메커니즘이다. 프롬프트 접두사가 이전 요청과 일치하면 캐시를 재사용하여 토큰 재계산을 피할 수 있다.
- [NVFP4 Quantization for LLM Inference](wiki/inference/nvfp4-quantization.md) — title: NVFP4 Quantization for LLM Inference
- [Prefill/Decode Disaggregated Serving](wiki/inference/disaggregated-serving.md) — title: Prefill/Decode Disaggregated Serving
- [Wide Expert Parallelism (WideEP) for MoE](wiki/inference/wide-expert-parallelism.md) — title: Wide Expert Parallelism (WideEP) for MoE

**project-internal · `vLLM`**
- [vLLM Semantic Router](wiki/inference/vllm-semantic-router.md) — 이 페이지는 vLLM 내부에서 vLLM Semantic Router이 어떤 역할을 하는지 정리한 프로젝트 스냅샷이다. 핵심 범위는 mmBERT 기반 신경 분류기로 요청을 적절한 모델에 라우팅하는 시스템 레벨 Mixture-of-Models이다.

### RAG (검색 증강 생성)

**entity**
- [Letta (MemGPT) Stateful Agent Runtime](wiki/rag/letta-stateful-agent-runtime.md) — title: Letta (MemGPT) Stateful Agent Runtime
- [Mem0 Universal Memory Layer](wiki/rag/mem0-universal-memory-layer.md) — title: Mem0 Universal Memory Layer
- [Serverless Object-Storage Vector DBs (Turbopuffer 등)](wiki/rag/serverless-vector-dbs.md) — title: Serverless Object-Storage Vector DBs (Turbopuffer 등)

**concept**
- [Adaptive Context Compression for Long-Running Agents](wiki/rag/adaptive-context-compression.md) — title: Adaptive Context Compression for Long-Running Agents
- [Agentic RAG with Hierarchical Retrieval Interfaces](wiki/rag/agentic-rag.md) — title: Agentic RAG with Hierarchical Retrieval Interfaces
- [Context Rot & Effective Context Window](wiki/rag/context-rot.md) — title: Context Rot & Effective Context Window
- [Contextual Retrieval (Anthropic)](wiki/rag/contextual-retrieval.md) — 이 페이지는 Contextual Retrieval (Anthropic)를 다룬다. 핵심은 청크마다 문서 맥락을 LLM으로 사전 주입한 뒤 임베딩·BM25를 계산하는 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [GraphRAG / LightRAG / LazyGraphRAG in Production](wiki/rag/graphrag-in-production.md) — title: GraphRAG / LightRAG / LazyGraphRAG in Production
- [Zep / Graphiti Temporal Knowledge Graph Memory](wiki/rag/temporal-knowledge-graph-memory.md) — title: Zep / Graphiti Temporal Knowledge Graph Memory

**summary**
- [Context Rot Report (Chroma)](wiki/rag/context-rot-report.md) — context window 크기와 실제 유효 컨텍스트 사이의 차이를 강조한 Chroma 기술 보고서 요약

**case-study**
- [Qwen3 / Voyage-4 Embedding Leaderboard Shakeup](wiki/rag/embedding-leaderboard-shakeup-2026.md) — title: Qwen3 / Voyage-4 Embedding Leaderboard Shakeup

### Agents (에이전트)

**concept**
- [Agent Memory Systems (Episodic / Semantic / Working)](wiki/agents/agent-memory-systems.md) — 이 페이지는 Agent Memory Systems (Episodic / Semantic / Working)를 다룬다. 핵심은 에이전트가 세션을 넘어 경험·사실·작업 상태를 store/retrieve/update/summarize/discard 연산으로 관리하는 메모리 계층이며, 2026
- [Agent Skills](wiki/agents/agent-skills.md) — title: Agent Skills
- [Context Folding & Sub-Trajectory Compression](wiki/agents/context-folding.md) — title: Context Folding & Sub-Trajectory Compression
- [Hierarchical Planning with Agent Trees](wiki/agents/agent-trees.md) — title: Hierarchical Planning with Agent Trees
- [How Coding Agents Work](wiki/agents/how-coding-agents-work.md) — Simon Willison이 agentic engineering guide Section 2에서 설명하는 코딩 에이전트의 내부 구조.
- [Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)](wiki/agents/long-horizon-agent-benchmarks.md) — 이 페이지는 Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)를 다룬다. 핵심은 수십~수백 단계, 수십 파일에 걸친 실세계 과제로 에이전트의 지속 추론·도구 사용·환경 상호작용을 평가하는 벤치마크 세대이며, 2026년 4
- [Long-Horizon RL Training for Agents (Multi-Turn RLVR)](wiki/agents/long-horizon-rl-training-for-agents.md) — title: Long-Horizon RL Training for Agents (Multi-Turn RLVR)
- [Orchestrator-Worker Multi-Agent Pattern](wiki/agents/orchestrator-worker-pattern.md) — title: Orchestrator-Worker Multi-Agent Pattern
- [Subagents](wiki/agents/subagents.md) — Simon Willison이 agentic engineering guide Section 2에서 설명하는 핵심 패턴.

**summary**
- [Agent Skills Specification](wiki/agents/agent-skills-specification.md) — Agent Skills 포맷의 디렉토리 구조와 SKILL.md 스펙을 정리한 공식 specification 요약
- [Anthropic Multi-Agent Research System](wiki/agents/anthropic-multi-agent-research-system.md) — Claude Research 백엔드에 적용된 orchestrator-worker 멀티 에이전트 시스템의 구조와 교훈 요약
- [Deep Research Agents Roadmap](wiki/agents/deep-research-agents-roadmap.md) — deep research agent의 구성 요소, 한계, 향후 연구 로드맵을 체계적으로 정리한 문서 요약
- [Effective Context Engineering for AI Agents (Anthropic)](wiki/concepts/effective-context-engineering-anthropic.md) — Anthropic이 context engineering을 Write / Select / Compress / Isolate 전략으로 정리한 대표 글 요약
- ["프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록"](wiki/agents/evolution-of-agentic-patterns.md) — 이 글의 중심 명제는 Chad Fowler의 "relocating rigor" 원칙이다:
- [Anthropic Harness Design for Long-Running Apps (Prithvi Rajasekaran, 2026-03)](wiki/agents/anthropic-harness-design.md) — 저자: Prithvi Rajasekaran (Anthropic Labs) · 발행: 2026-03-24 · 출처: anthropic.com/engineering/harness-design-long-running-apps

**entity**
- [SkyworkAI DeepResearchAgent](wiki/agents/skywork-deepresearchagent.md) — deep research workflow를 오픈소스로 구현한 공개 레퍼런스 프로젝트 허브

**project-internal · `oh-my-claudecode`**
- [OMC Agent Catalog](wiki/agents/omc-agent-catalog.md) — > OMC의 19개 전문 에이전트를 4개 레인(Build/Analysis, Review, Domain, Coordination)으로 분류.

### Applications (응용)

**entity**
- [oh-my-claudecode (OMC)](wiki/applications/oh-my-claudecode.md) — > "Don't learn Claude Code. Just use OMC."

**concept**
- ["First Run the Tests"](wiki/applications/first-run-the-tests.md) — Simon Willison이 agentic engineering guide Section 3에서 제안하는 네 단어 프롬프트.
- [Agentic Manual Testing](wiki/applications/agentic-manual-testing.md) — Simon Willison이 agentic engineering guide Section 3에서 다루는 수동 테스트 자동화 패턴.
- [Interactive Explanations](wiki/applications/interactive-explanations.md) — Simon Willison이 agentic engineering guide Section 4에서 제시하는 인지 부채 상환 기법.
- [Linear Walkthroughs](wiki/applications/linear-walkthroughs.md) — Simon Willison이 agentic engineering guide Section 4에서 소개하는 "에이전트가 코드를 설명하게 만드는 기법".
- [Red/Green TDD with Coding Agents](wiki/applications/red-green-tdd.md) — Simon Willison이 agentic engineering guide Section 3의 핵심 프롬프트 패턴으로 소개한 기법.

**summary**
- ["Google Stitch DESIGN.md 가이드 (요약)"](wiki/applications/stitch-design-md-guide.md) — Google Stitch 공식 문서의 DESIGN.MD 섹션 3개 페이지(overview/format/usage)를 한국어로 요약한 문서. 원본은 raw/2026-04-09-stitch-design-md.md에 보존.
- [2026년 4월 Frontier Model 비교](wiki/applications/frontier-model-comparison-2026-04.md) — 주요 frontier 모델을 성능 수치보다 작업 적합성과 운영 관점으로 비교한 summary
- [2026년 4월 에이전트 벤치마크 비교](wiki/applications/agent-benchmark-comparison-2026-04.md) — SWE-bench / Terminal-Bench / ARC-AGI / METR의 측정 대상을 비교한 summary
- [Writing about Agentic Engineering Patterns](wiki/applications/writing-about-agentic-engineering-patterns.md) — Simon Willison이 Agentic Engineering Patterns 프로젝트를 왜 시작했는지 설명한 글 요약
- ["Simon Willison's Prompts Library"](wiki/applications/prompts-library.md) — Simon Willison이 agentic engineering guide 부록 "Prompts I use"에 모아둔, 본인이 상시 사용하는 프롬프트 모음. 지속적으로 업데이트되는 섹션이다.
- [2026년 4월 AI 개발 핫토픽 100선](wiki/applications/ai-hot-topics-2026-04.md) — title: 2026년 4월 AI 개발 핫토픽 100선
- [2026년 4월 핫토픽 corpus coverage audit](wiki/applications/hot-topics-corpus-coverage-audit-2026-04.md) — 원본 500개 링크가 deduplication, raw snapshot 저장, wiki 참조까지 모두 완료됐는지 검증한 감사 문서
- [Agentic Engineering Patterns 가이드 (Simon Willison)](wiki/applications/agentic-engineering-guide.md) — Simon Willison이 2026-02-23에 시작한 가이드 시리즈. 코딩 에이전트(Claude Code, OpenAI Codex, Gemini CLI 등)를 사용하는 프로페셔널 소프트웨어 엔지니어를 위한 패턴 모음이다. 1994년 GoF *Design Patterns* 책에서 영감

**case-study**
- ["GIF Optimization with WebAssembly — Case Study"](wiki/applications/gif-optimization-case-study.md) — Simon Willison이 agentic engineering guide Section 5 "Annotated Prompts"에 실은 실전 사례. Claude Code에게 Gifsicle을 WebAssembly로 컴파일하고 브라우저 인터페이스를 만들게 하는 과정을 주석 달린 프롬프트로
- [Anthropic Full-Stack Harness Case Study (Game Maker + DAW)](wiki/applications/anthropic-app-harness-case-study.md) — Anthropic의 Prithvi Rajasekaran이 Harness Design for Long-Running Application Development에서 공개한 두 개의 풀 스택 빌드 케이스. Retro Game Maker (Opus 4.5) 와 Digital Audio Work
- [OpenHands SWE-Bench Scaling Notes](wiki/applications/openhands-swe-bench-scaling-notes.md) — inference-time scaling과 critic model이 coding agent benchmark 성능을 어떻게 바꾸는지 보여주는 사례 정리

### Papers (논문)

**paper**
- [ACON: Optimizing Context Compression for Long-horizon LLM Agents](wiki/papers/acon-context-compression-paper.md) — 장기 실행 에이전트의 문맥 압축을 단순 요약 문제가 아니라 **실패 원인 기반 최적화 문제**로 다룬 논문이다.
- [ARE: Scaling Up Agent Environments and Evaluations](wiki/papers/are-gaia2-paper.md) — 에이전트 평가를 환경·도구·시간 제약을 포함한 실행 문제로 끌어올린 ARE / Gaia2 논문이다.
- [AgentFold: Long-Horizon Web Agents with Proactive Context Management](wiki/papers/agentfold-paper.md) — 웹 에이전트가 단순히 로그를 누적하는 대신, 히스토리를 능동적으로 접어 넣는 **proactive context management** 패러다임을 제안한다.
- [AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning](wiki/papers/agentgym-rl-paper.md) — 장기 의사결정 에이전트를 multi-turn RL로 훈련시키는 프레임워크 논문이다.
- [Deep Research Agents: A Systematic Examination and Roadmap](wiki/papers/deep-research-agents-roadmap-paper.md) — deep research agent를 planning / retrieval / synthesis / verification 문제로 정리한 로드맵형 논문이다.
- [Context Engineering for AI Agents in Open-Source Software](wiki/papers/context-engineering-open-source-software-paper.md) — 오픈소스 소프트웨어 작업에서 context engineering을 저장소·문서·작업 이력 설계 문제로 분석한 논문이다.
- [Memory in the Age of AI Agents](wiki/papers/memory-in-the-age-of-ai-agents-paper.md) — 에이전트 메모리 연구를 token-level, parametric, latent memory와 factual / experiential / working memory 축으로 재정리한 대형 서베이다.
- [Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](wiki/papers/plan-and-act-paper.md) — 장기 과제에서 계획과 실행을 분리하는 접근을 제안한 planning 논문이다.
- [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](wiki/papers/research-learning-to-reason-with-search-paper.md) — search policy와 reasoning policy를 함께 RL로 최적화하는 논문이다.
- [ReVeal: Self-Evolving Code Agents via Reliable Self-Verification](wiki/papers/reveal-paper.md) — reliable self-verification으로 코드 에이전트를 진화시키는 구조를 제안한 논문이다.
- [Scaling Long-Horizon LLM Agent via Context-Folding](wiki/papers/context-folding-paper.md) — 서브태스크를 branch한 뒤 fold하여 요약으로 되돌리는 **Context-Folding**을 RL 프레임워크로 학습시킨 논문이다.
- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](wiki/papers/agentic-rl-survey-paper.md) — LLM 에이전트 강화학습의 문제 설정·알고리즘·평가 지형을 정리한 서베이다.
- [ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning](wiki/papers/reactree-paper.md) — 단일 trajectory 대신 agent tree와 control flow node를 도입해 장기 계획 문제를 푸는 hierarchical planning 논문이다.
- [SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios](wiki/papers/swe-evo-paper.md) — 코딩 에이전트를 단일 버그 수정이 아니라 release-note 기반의 다단계 진화 과제로 평가하는 long-horizon benchmark 논문이다.
- [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](wiki/papers/flashattention-4-paper.md) — Blackwell GPU의 비대칭 하드웨어 스케일링에 맞춰 attention kernel을 다시 설계한 FlashAttention-4 논문이다.
- [ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](wiki/papers/chunkkv-paper.md) — 토큰 단위 중요도 대신 의미 청크를 보존 단위로 삼아 KV cache를 압축하는 기법을 제안한 논문이다.
- [Lost in the Middle: How Language Models Use Long Contexts](wiki/papers/lost-in-the-middle-paper.md) — 긴 컨텍스트에서 관련 정보가 중간에 있을 때 LLM 성능이 크게 저하된다는 고전적이면서도 여전히 중요한 논문이다.
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](wiki/papers/deepseek-r1-paper.md) — 인간 라벨 reasoning trace 없이도 pure RL만으로 reasoning 패턴이 출현할 수 있음을 강하게 보여준 전환점 논문이다.
- [Reinforcement Learning for Long-Horizon Interactive LLM Agents](wiki/papers/loop-paper.md) — 장기 상호작용 에이전트를 RL 문제로 정식화한 초기 핵심 논문이다.

### Tooling (도구)

**entity**
- [ARC-AGI-2](wiki/tooling/arc-agi-2.md) — 이 페이지는 ARC-AGI-2를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 ARC Prize가 운영하는 추상 추론/유동지능(fluid intelligence) 벤치마크 2세대이기 때문이다.
- [BAML](wiki/tooling/baml.md) — 이 페이지는 BAML를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL이기 때문이다.
- [Claude Agent SDK](wiki/tooling/claude-agent-sdk.md) — 이 페이지는 Claude Agent SDK를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Claude Code의 에이전트 루프·툴·컨텍스트 관리를 라이브러리화한 Anthropic SDK이기 때문이다.
- [Claude Agent SDK TypeScript](wiki/tooling/claude-agent-sdk-typescript.md) — Claude Agent SDK의 TypeScript 구현 저장소를 추적하는 허브 페이지.
- [Claude Code](wiki/tooling/claude-code.md) — Anthropic이 제공하는 공식 coding agent. Simon Willison이 agentic engineering guide 전반에 걸쳐 가장 많이 레퍼런스하는 도구다.
- [Claude Agent SDK TypeScript](wiki/tooling/claude-agent-sdk-typescript.md) — Claude Agent SDK의 TypeScript 구현 저장소를 추적하는 허브 페이지.
- [Claude Opus 4.5](wiki/tooling/claude-opus-4-5.md) — 장기 자율 작업과 고난도 coding workflow를 겨냥한 Anthropic high-end frontier 모델 허브.
- [Claude Opus 4.6](wiki/tooling/claude-opus-4-6.md) — 이 페이지는 Claude Opus 4.6를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 2월 Anthropic이 공개한 플래그십 모델 (1M 컨텍스트)이기 때문이다.
- [Claude Opus 4.5](wiki/tooling/claude-opus-4-5.md) — 장기 자율 작업과 고난도 coding workflow를 겨냥한 Anthropic high-end frontier 모델 허브.
- [Claude Sonnet 4.5](wiki/tooling/claude-sonnet-4-5.md) — agentic coding, computer use, 장시간 작업 유지력 측면에서 중요한 Anthropic frontier 모델 허브.
- [Cursor Cloud Agents & Parallel Worktree Agents](wiki/tooling/cursor-cloud-agents-and-parallel-worktree-agents.md) — title: Cursor Cloud Agents & Parallel Worktree Agents
- [Deep Agents](wiki/tooling/deep-agents.md) — 이 페이지는 Deep Agents를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 플래너·파일시스템·서브에이전트를 기본 탑재한 LangGraph 기반 딥 에이전트 하네스이기 때문이다.
- [DSPy + GEPA optimize_anything](wiki/tooling/dspy-gepa.md) — title: DSPy + GEPA optimize_anything
- [Gemini 3.1 Pro](wiki/tooling/gemini-3-1-pro.md) — 이 페이지는 Gemini 3.1 Pro를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 2월 Google DeepMind가 출시한 Gemini 3 시리즈 point-version이기 때문이다.
- [GLM-5.1](wiki/tooling/glm-5-1.md) — 이 페이지는 GLM-5.1를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 4월 Z.ai(구 Zhipu)가 공개한 754B MoE 오픈소스 에이전틱 엔지니어링 모델이기 때문이다.
- [Google Stitch](wiki/tooling/google-stitch.md) — Google의 AI 기반 디자인 도구. "Stitch - Design with AI"라는 태그라인으로 제공되며, 내부 코드네임은 Nemo. Gemini 모델 계열(gemini-2.5-flash-native-audio-preview-12-2025 등)을 기반으로 UI를 생성한다.
- [GPT-5.4](wiki/tooling/gpt-5-4.md) — 이 페이지는 GPT-5.4를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 3월 OpenAI가 공개한 네이티브 컴퓨터 사용 플래그십이기 때문이다.
- [Instructor](wiki/tooling/instructor.md) — 이 페이지는 Instructor를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Pydantic 기반 구조화 출력·검증·재시도를 캡슐화한 다언어 LLM 라이브러리이기 때문이다.
- [Kimi K2.5](wiki/tooling/kimi-k2-5.md) — 이 페이지는 Kimi K2.5를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 1월 Moonshot AI가 공개한 1T 파라미터 오픈소스 네이티브 멀티모달 에이전트 모델이기 때문이다.
- [LangGraph 1.0 / 2.0 (Agent Orchestration Framework)](wiki/tooling/langgraph.md) — title: LangGraph 1.0 / 2.0 (Agent Orchestration Framework)
- [Mastra](wiki/tooling/mastra.md) — 이 페이지는 Mastra를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Gatsby 팀이 만든 TypeScript 풀스택 에이전트·워크플로우 프레임워크이기 때문이다.
- [MCP 2026 Roadmap & Enterprise Readiness](wiki/tooling/model-context-protocol.md) — title: MCP 2026 Roadmap & Enterprise Readiness
- [MCP OAuth 2.1 + PKCE Authorization](wiki/tooling/mcp-authorization.md) — title: MCP OAuth 2.1 + PKCE Authorization
- [MiniMax M2.5](wiki/tooling/minimax-m2-5.md) — 이 페이지는 MiniMax M2.5를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 2월 공개된 230B/10B MoE 오픈 웨이트 프론티어 근접 모델이기 때문이다.
- [Model Context Protocol (MCP)](wiki/tooling/model-context-protocol-mcp.md) — LLM 앱과 외부 데이터/도구 연결을 표준화하는 개방형 프로토콜 자체를 다루는 허브 페이지.
- [OpenAI Agents SDK](wiki/tooling/openai-agents-sdk.md) — 이 페이지는 OpenAI Agents SDK를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Swarm의 후속 프로덕션 버전인 OpenAI 공식 에이전트 오케스트레이션 SDK이기 때문이다.
- [Pydantic AI](wiki/tooling/pydantic-ai.md) — 이 페이지는 Pydantic AI를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 FastAPI식 개발 경험을 가진 타입 안전 Python 에이전트 프레임워크이기 때문이다.
- [Qwen3.6-Plus](wiki/tooling/qwen3-6-plus.md) — 이 페이지는 Qwen3.6-Plus를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 2026년 4월 Alibaba가 공개한 Qwen 플래그십 (1M 컨텍스트, 항상 reasoning)이기 때문이다.
- [SWE-bench Pro](wiki/tooling/swe-bench-pro.md) — 이 페이지는 SWE-bench Pro를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Scale AI가 구축한 장기 호흡(long-horizon) 소프트웨어 엔지니어링 벤치마크이기 때문이다.
- [Terminal-Bench 2.0](wiki/tooling/terminal-bench-2-0.md) — 이 페이지는 Terminal-Bench 2.0를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Stanford-Laude Institute가 만든 터미널 환경 에이전트 평가 벤치마크이기 때문이다.
- [Tesseract.js](wiki/tooling/tesseract-js.md) — 브라우저와 Node.js에서 동작하는 OCR 라이브러리. 에이전트가 이미지·스크린샷에서 텍스트를 읽는 실험에 자주 등장한다.
- [Vercel AI SDK 6](wiki/tooling/vercel-ai-sdk.md) — title: Vercel AI SDK 6

**concept**
- [Agent Harnesses for Long-Running Coding Sessions](wiki/tooling/long-running-agent-harnesses.md) — title: Agent Harnesses for Long-Running Coding Sessions
- [Browser Automation for Coding Agents](wiki/tooling/browser-automation-agents.md) — Simon Willison이 agentic engineering guide Section 3 (agentic manual testing)에서 언급하는 브라우저 자동화 도구 모음. 웹 UI를 에이전트가 직접 조작·검증하게 하기 위한 기반.
- [Firecracker/microVM Sandboxes for Agent Code Execution](wiki/tooling/microvm-agent-sandboxes.md) — title: Firecracker/microVM Sandboxes for Agent Code Execution
- [Git with Coding Agents](wiki/tooling/git-with-coding-agents.md) — Simon Willison이 agentic engineering guide Section 2에서 다루는 주제. Git을 코딩 에이전트의 "시간 여행 도구"로 활용하는 법.
- [Git Worktree Isolation for Parallel Coding Agents](wiki/tooling/git-worktree-isolation.md) — title: Git Worktree Isolation for Parallel Coding Agents
- [Tool Contracts & Writing Tools for Agents](wiki/tooling/tool-contracts-for-agents.md) — title: Tool Contracts & Writing Tools for Agents

**summary**
- [Claude Agent SDK Overview](wiki/tooling/claude-agent-sdk-overview.md) — Claude Agent SDK의 세션, agent loop, streaming, approval 개념을 한 번에 훑는 공식 개요 요약
- [Claude Agent SDK Quickstart](wiki/tooling/claude-agent-sdk-quickstart.md) — Claude Agent SDK를 실제로 시작하기 위한 최소 실행 경로 요약
- [Claude Agent Loop](wiki/tooling/claude-agent-loop.md) — SDK 내부 실행 루프와 tool routing 흐름을 설명하는 문서 요약
- [Claude Agent Sessions](wiki/tooling/claude-agent-sessions.md) — 장기 실행 에이전트에서 세션이 상태 단위로 어떻게 작동하는지 설명하는 문서 요약
- [Effective Harnesses for Long-Running Agents](wiki/tooling/effective-harnesses-for-long-running-agents.md) — initializer agent와 coding agent를 분리해 장기 실행 에이전트의 세션 연속성을 확보하는 하네스 설계 글 요약
- [Claude Opus 4.5 Release Notes](wiki/tooling/claude-opus-4-5-release-notes.md) — Claude Opus 4.5 출시 글에서 모델 성능과 제품군 방향성을 함께 요약한 문서
- [MCP Specification 2025-11-25](wiki/tooling/mcp-specification-2025-11-25.md) — MCP의 architecture, protocol, authorization, client/server features를 정의하는 공식 스펙 요약
- [MCP Architecture](wiki/tooling/mcp-architecture.md) — host / client / server 구조를 중심으로 MCP를 시스템 관점에서 설명하는 문서 요약
- [MCP Authorization Draft](wiki/tooling/mcp-authorization-draft.md) — MCP authorization draft를 security boundary와 운영 관점에서 읽는 문서 요약
- [MCP Roadmap (Development)](wiki/tooling/mcp-roadmap-development.md) — workstream, working group, governance, SEP 흐름을 중심으로 정리한 MCP development roadmap 요약
- [Scaling Managed Agents](wiki/tooling/scaling-managed-agents.md) — brain / hands / session을 분리하는 managed agent 인프라 설계 글 요약
- [The 2026 MCP Roadmap](wiki/tooling/the-2026-mcp-roadmap.md) — MCP의 우선순위가 transport, agent communication, governance, enterprise readiness로 이동했음을 설명하는 공식 로드맵 요약
- [What is the Model Context Protocol (MCP)?](wiki/tooling/what-is-mcp.md) — MCP의 기본 개념과 host / client / server 구조를 빠르게 이해하기 위한 입문 요약
- [Writing Effective Tools for Agents](wiki/tooling/writing-effective-tools-for-agents.md) — 에이전트용 도구를 deterministic API가 아니라 agent-friendly interface로 설계하는 원칙 요약

- [LangGraph Quickstart](wiki/tooling/langgraph-quickstart.md) — LangGraph의 상태·노드·도구·종료 조건을 가장 짧은 계산기 예제로 설명하는 공식 quickstart 요약
- [LangGraph Persistence](wiki/tooling/langgraph-persistence.md) — thread, checkpoint, super-step, replay를 통해 LangGraph 상태 저장 구조를 설명하는 문서 요약
- [LangGraph Durable Execution](wiki/tooling/langgraph-durable-execution.md) — checkpointer와 task wrapping으로 장기 실행 그래프를 재개 가능하게 만드는 가이드 요약
- [OpenAI Agents SDK Quickstart](wiki/tooling/openai-agents-sdk-quickstart.md) — 단일 agent에서 tool·handoff orchestration으로 확장하는 가장 짧은 공식 입문 경로
- [OpenAI Agents SDK Handoffs](wiki/tooling/openai-agents-sdk-handoffs.md) — specialist agent handoff, inputType, history filtering을 설명하는 공식 가이드 요약
- [OpenAI Agents SDK Sessions](wiki/tooling/openai-agents-sdk-sessions.md) — Session 인터페이스, Conversations/Memory 세션, compaction을 설명하는 공식 가이드 요약
- [OpenAI Agents SDK MCP](wiki/tooling/openai-agents-sdk-model-context-protocol.md) — hosted MCP tools, streamable HTTP, stdio 연결 방식을 정리한 공식 가이드 요약

- [Pydantic AI Agent Core Concepts](wiki/tooling/pydantic-ai-agent-core.md) — Agent를 타입 계약과 실행 표면 중심으로 설명하는 Pydantic AI 핵심 개념 요약
- [Pydantic AI MCP Overview](wiki/tooling/pydantic-ai-mcp-overview.md) — Pydantic AI가 MCP client / FastMCP / built-in MCP tool을 지원하는 방식을 정리한 문서 요약
- [Pydantic AI Durable Execution Overview](wiki/tooling/pydantic-ai-durable-execution-overview.md) — Temporal·DBOS·Prefect와의 durable execution 통합 전략 요약
- [Deep Agents Quickstart](wiki/tooling/deep-agents-quickstart.md) — planning·filesystem·subagents를 갖춘 deep agent를 빠르게 실행하는 공식 입문 경로
- [Deep Agents Subagents](wiki/tooling/deep-agents-subagents.md) — context isolation 중심의 subagent 설계와 best practices 요약
- [Deep Agents Memory](wiki/tooling/deep-agents-memory.md) — scoped memory와 forgetting 정책을 설명하는 문서 요약
- [Deep Agents Going to Production](wiki/tooling/deep-agents-production.md) — memory·sandbox·guardrails·frontend를 포함한 운영 전환 가이드 요약

- [Mastra Get Started](wiki/tooling/mastra-get-started.md) — Mastra의 quickstart와 프레임워크 통합 출발점을 설명하는 공식 docs 요약
- [What is BAML?](wiki/tooling/baml-what-is-baml.md) — BAML을 structured output용 DSL과 생성된 클라이언트 관점에서 설명하는 공식 문서 요약
- [Instructor Overview](wiki/tooling/instructor-overview.md) — validation·retry·schema 중심의 structured output 라이브러리 입문 요약
- [AI SDK Core Overview](wiki/tooling/vercel-ai-sdk-core-overview.md) — Vercel AI SDK Core primitives를 정리하는 공식 overview
- [Vercel AI SDK Agents Overview](wiki/tooling/vercel-ai-sdk-agents-overview.md) — ToolLoopAgent 중심의 agent 레이어 설계 요약
- [Vercel AI SDK Tool Calling](wiki/tooling/vercel-ai-sdk-tool-calling.md) — strict mode, approval, multi-step calls를 정리한 공식 문서 요약
- [Vercel AI SDK MCP Tools](wiki/tooling/vercel-ai-sdk-mcp-tools.md) — MCP client와 tools/resources/prompts 통합을 다루는 공식 문서 요약

**project-internal · `Claude Code`**
- [Claude Code Hooks System](wiki/tooling/claude-code-hooks-system.md) — 이 페이지는 Claude Code 내부에서 Claude Code Hooks System이 어떤 역할을 하는지 정리한 프로젝트 스냅샷이다. 핵심 범위는 툴 호출 전후·세션 이벤트에 사용자 정의 스크립트를 끼워 넣는 settings.json 기반 확장 훅이다.

**project-internal · `oh-my-claudecode`**
- [OMC Autopilot](wiki/tooling/omc-autopilot.md) — > 아이디어 한 줄에서 검증된 동작 코드까지. 5-Phase 자율 실행 파이프라인.
- [OMC CCG](wiki/tooling/omc-ccg.md) — > 한 요청을 Codex와 Gemini에 동시 질의하고 Claude가 결과를 합성하는 삼중 자문 스킬.
- [OMC Deep Interview](wiki/tooling/omc-deep-interview.md) — > Socratic 질문과 수학적 모호성 측정으로 요구사항을 명확화하는 스킬. Ouroboros에서 영감.
- [OMC Execution Modes](wiki/tooling/omc-execution-modes.md) — > OMC가 제공하는 여러 실행 전략 한눈에 보기. Team부터 Ultrawork까지 6가지 모드가 있으며, 각기 다른 상황을 겨냥한다.
- [OMC Ralph Mode](wiki/tooling/omc-ralph-mode.md) — > "The boulder never stops." 검증이 완료될 때까지 중단하지 않는 지속 실행 모드.
- [OMC Ralplan](wiki/tooling/omc-ralplan.md) — > Planner + Architect + Critic의 반복 루프로 컨센서스 기획에 도달하는 스킬. Ralph 모드의 기획 게이트 역할도 함께 수행.
- [OMC Team Mode](wiki/tooling/omc-team-mode.md) — > OMC v4.1.7부터의 canonical 오케스트레이션 표면. swarm 키워드를 대체한 공식 다중 에이전트 표준.
- [OMC Ultrawork](wiki/tooling/omc-ultrawork.md) — > 최대 병렬성으로 독립 태스크를 한꺼번에 해치우는 버스트 모드.

### Concepts (개념)

**entity**
- [METR Time Horizon Benchmark](wiki/concepts/metr-time-horizon-benchmark.md) — title: METR Time Horizon Benchmark
- [OpenTelemetry GenAI Semantic Conventions](wiki/concepts/opentelemetry-genai-semconv.md) — title: OpenTelemetry GenAI Semantic Conventions
- [Production Observability Platforms Convergence](wiki/concepts/llm-observability-platforms.md) — title: Production Observability Platforms Convergence

**concept**
- ["AI 친화적 디자인 시스템 문서화"](wiki/concepts/ai-readable-design-system.md) — AI 에이전트가 UI를 생성하는 시대에, 디자인 시스템은 사람뿐 아니라 에이전트도 읽을 수 있는 형태여야 한다는 관점. Google Stitch가 DESIGN.md 포맷을 제안하면서 구체화된 개념이지만, 원리 자체는 source-agnostic하다.
- ["DESIGN.md 포맷"](wiki/concepts/design-md-format.md) — AI 디자인 에이전트가 읽을 수 있는 평문 디자인 시스템 문서 포맷. Google Stitch가 정의했지만 포맷 자체는 portable하며 다른 AI 에이전트(예: Claude Code)도 읽고 활용할 수 있다.
- ["Writing Code is Cheap Now"](wiki/concepts/code-is-cheap.md) — Simon Willison이 agentic engineering guide Section 1에서 제시한 핵심 원칙.
- ["디자인 토큰"](wiki/concepts/design-tokens.md) — 디자인 시스템의 원자적 값을 이름이 붙은 토큰으로 관리하는 패턴. 색상 hex, 폰트 패밀리, spacing 단위, corner radius 등을 직접 하드코딩하지 않고 의미 있는 이름으로 추상화해 참조한다.
- [Agent Prompt Injection Defense & Trustworthy Agents](wiki/concepts/agent-prompt-injection-defense.md) — 이 페이지는 Agent Prompt Injection Defense & Trustworthy Agents를 다룬다. 핵심은 에이전트 브라우징/툴 사용 시 악성 지시 주입을 차단하는 계층적 방어 프레임워크이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Agent Trajectory Evaluation](wiki/concepts/agent-trajectory-evaluation.md) — 이 페이지는 Agent Trajectory Evaluation를 다룬다. 핵심은 최종 출력이 아닌 에이전트의 중간 도구 호출 경로를 평가이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Agentic Engineering](wiki/concepts/agentic-engineering.md) — Agentic Engineering = "코딩 에이전트(coding agent)의 도움을 받아 소프트웨어를 개발하는 실천"
- [Alignment Faking in LLMs](wiki/concepts/alignment-faking.md) — title: Alignment Faking in LLMs
- [Anti-patterns in Agentic Engineering](wiki/concepts/anti-patterns.md) — Simon Willison이 agentic engineering guide Section 1에서 경고하는 "하지 말아야 할 행동들".
- [Better Code With Agents](wiki/concepts/better-code-with-agents.md) — Simon Willison이 agentic engineering guide에서 제시하는 원칙: 코딩 에이전트를 도입한다고 해서 코드 품질이 반드시 하락하는 것은 아니다. 오히려 *더 나은* 코드를 쓸 기회다.
- [Blind Prompting (맹목적 프롬프팅)](wiki/concepts/blind-prompting.md) — Blind Prompting은 Mitchell Hashimoto가 지적한 안티패턴이다:
- [Chain-of-Thought Monitorability](wiki/concepts/cot-monitorability.md) — title: Chain-of-Thought Monitorability
- [Circuit Tracing & Attribution Graphs](wiki/concepts/circuit-tracing.md) — title: Circuit Tracing & Attribution Graphs
- [Coding Agent](wiki/concepts/coding-agent.md) — Coding agent는 코드를 *작성*하고 *실행*할 수 있는 에이전트다. Simon Willison은 이를 LLM을 감싼 하네스(harness)로 설명한다.
- [Cognitive Debt](wiki/concepts/cognitive-debt.md) — Simon Willison이 agentic engineering guide에서 소개한 개념. 기술 부채(technical debt)와 쌍을 이루는 새로운 용어.
- [Constitutional Classifiers++ (Jailbreak Defense)](wiki/concepts/constitutional-classifiers.md) — title: Constitutional Classifiers++ (Jailbreak Defense)
- [Context Anxiety (컨텍스트 불안)](wiki/concepts/context-anxiety.md) — Context Anxiety는 LLM이 실제로는 컨텍스트 창에 여유가 있을 때에도 스스로 한계에 가까워졌다고 "믿고" 작업을 조기에 마무리 짓는 실패 모드다. Anthropic의 Prithvi Rajasekaran이 2026-03 글에서 Claude Sonnet 4.5에서 관찰한 특정 
- [Context Engineering (컨텍스트 엔지니어링)](wiki/concepts/context-engineering.md) — Context Engineering은 2025년 중반에 등장한 AI 개발 패러다임이다. 핵심 질문은 "모델의 컨텍스트 창에 어떤 정보를 주입해야 작업이 해결될까?"다. 엄밀함의 위치는 프롬프트 텍스트에서 컨텍스트 창 구성으로 이동했다.
- [Deliberative Alignment & Anti-Scheming Training](wiki/concepts/deliberative-alignment.md) — title: Deliberative Alignment & Anti-Scheming Training
- [Error Analysis as the Eval Foundation](wiki/concepts/error-analysis-for-evals.md) — title: Error Analysis as the Eval Foundation
- [Generator-Evaluator Architecture (생성자-평가자 아키텍처)](wiki/concepts/generator-evaluator-architecture.md) — Generator-Evaluator Architecture는 *작업을 생성하는 에이전트*와 *작업을 평가하는 에이전트*를 구조적으로 분리하는 하네스 패턴이다. GAN(Generative Adversarial Networks)의 generator/discriminator 분리에서 영감을 
- [Harness Engineering (하네스 엔지니어링)](wiki/concepts/harness-engineering.md) — Harness Engineering은 2026년 초부터 지배적이 된 AI 개발 패러다임이다. 핵심 질문은 "모델을 감싸는 어떤 시스템을 구축해야 원하는 동작이 나올까?"다. 엄밀함의 위치는 컨텍스트 창 구성에서 시스템 아키텍처로 이동했다.
- [Harness Quadrants (하네스 4사분면)](wiki/concepts/harness-quadrants.md) — Harness Quadrants는 Martin Fowler와 Birgitta Böckeler(ThoughtWorks)가 2026년 2월에 제시한 하네스 구성요소의 2×2 분류 체계다. harness engineering에서 "모델을 제외한 모든 것"에 해당하는 하네스를 네 영역으로 쪼개
- [Hoard Things You Know How To Do](wiki/concepts/hoard-things-you-know-how-to-do.md) — Simon Willison이 agentic engineering guide에서 제시하는 핵심 프로페셔널 스킬. "할 줄 아는 것을 축적하라."
- [Lethal Trifecta (치명적 3요소)](wiki/concepts/lethal-trifecta.md) — Lethal Trifecta는 Simon Willison이 정리한 AI 에이전트 보안 원칙이다. 에이전트가 다음 세 가지 능력을 동시에 갖추면 보안 사고는 불가피하다:
- [The Lethal Trifecta for AI Agents](wiki/concepts/the-lethal-trifecta-article.md) — Simon Willison이 lethal trifecta를 직접 설명하며 왜 이 규칙이 agent 보안 설계의 출발점이어야 하는지 경고한 원문 글 요약
- [LLM as OS (운영체제로서의 LLM)](wiki/concepts/llm-as-os.md) — LLM as OS는 Andrej Karpathy가 제안한 메타포로, LLM 시스템을 운영체제(Operating System) 에 빗대어 이해하는 멘탈 모델이다. 이 비유는 context engineering 시대의 표준 프레임워크가 되었다.
- [LLM-as-Judge Calibration & Reliability](wiki/concepts/llm-as-judge-calibration.md) — title: LLM-as-Judge Calibration & Reliability
- [Load-Bearing Harness (하네스 load-bearing 테스트)](wiki/concepts/load-bearing-harness.md) — Load-Bearing Harness는 하네스 엔지니어링의 메타 원칙이다: 하네스의 어떤 컴포넌트가 정말로 성능을 떠받치고 있는지는 오직 그것을 제거해봐야 알 수 있다. 그리고 그 답은 모델 버전이 바뀔 때마다 달라진다.
- [Lost in the Middle](wiki/concepts/lost-in-the-middle.md) — 긴 컨텍스트에서 중간에 놓인 정보의 회수 성능이 앞·뒤보다 떨어지는 현상. long-context 설계와 검색 전략의 핵심 제약이다.
- [Model Welfare & Formal Welfare Assessments](wiki/concepts/model-welfare.md) — 이 페이지는 Model Welfare & Formal Welfare Assessments를 다룬다. 핵심은 모델의 의식 가능성과 심리적 안녕을 평가·보호하는 연구 프로그램이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Multi-Turn Agent Evaluation](wiki/concepts/multi-turn-agent-evaluation.md) — 이 페이지는 Multi-Turn Agent Evaluation를 다룬다. 핵심은 대화 전체 세션 단위로 사용자 목표 달성 여부를 채점이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Natural Emergent Misalignment from Reward Hacking](wiki/concepts/emergent-misalignment.md) — title: Natural Emergent Misalignment from Reward Hacking
- [Pairwise vs Pointwise Eval Protocol Bias](wiki/concepts/pairwise-vs-pointwise-evals.md) — title: Pairwise vs Pointwise Eval Protocol Bias
- [Prompt Engineering (프롬프트 엔지니어링)](wiki/concepts/prompt-engineering.md) — Prompt Engineering은 2022-2024년 사이 AI 개발의 지배적 패러다임이었다. 핵심 질문은 "모델에게 무엇을 말해야 원하는 결과를 얻을까?"였다. 엄밀함의 위치는 프롬프트 텍스트 자체였다.
- [Ralph Pattern (랠프 패턴)](wiki/concepts/ralph-pattern.md) — Ralph Pattern은 Geoffrey Huntley가 제시한 에이전트 실행 패턴이다. PRD(Product Requirements Document)가 완료될 때까지 AI 코딩 도구를 반복 루프에서 실행하되, 매 이터레이션마다 컨텍스트를 완전히 초기화하는 방식을 뜻한다.
- [Relocating Rigor (엄밀함의 이동)](wiki/concepts/relocating-rigor.md) — Relocating Rigor는 Chad Fowler가 제시한 엔지니어링 원칙이다:
- [Rubric-Based Evaluation Frameworks](wiki/concepts/rubric-based-evals.md) — title: Rubric-Based Evaluation Frameworks
- [Self-Evaluation Bias (자기평가 편향)](wiki/concepts/self-evaluation-bias.md) — Self-Evaluation Bias는 LLM이 자기 작업을 자기 자신이 평가할 때 체계적으로 과도하게 관대해지는 경향이다. 출력 품질이 평범하거나 심지어 잘못되었을 때조차 모델은 자신 있게 자기 작업을 칭찬하는 패턴을 보인다.
- [Sprint Contracts (스프린트 계약)](wiki/concepts/sprint-contracts.md) — Sprint Contract는 구현을 시작하기 전에 Generator와 Evaluator가 "이 sprint에서 무엇을 만들고, 어떻게 성공을 검증할지" 를 명시적으로 협상해 문서화하는 pre-coding 합의다. Anthropic의 Prithvi Rajasekaran이 Harness 
- [Synthetic Eval Data Generation](wiki/concepts/synthetic-eval-data-generation.md) — 이 페이지는 Synthetic Eval Data Generation를 다룬다. 핵심은 LLM으로 자동 생성한 테스트 케이스로 평가 데이터셋을 확장이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.
- [Tool Selection & Tool Invocation Evaluators](wiki/concepts/tool-invocation-evaluators.md) — title: Tool Selection & Tool Invocation Evaluators
- [Vibe Coding](wiki/concepts/vibe-coding.md) — Vibe coding은 Andrej Karpathy가 2025년 2월에 만든 용어로, LLM에 프롬프트를 던져 리뷰하지 않은 프로토타입 수준의 코드를 얻는 방식을 가리킨다.

**summary**
- [Responsible Scaling Policy v3 & Frontier Safety Roadmap](wiki/concepts/responsible-scaling-policy-v3.md) — 이 페이지는 Responsible Scaling Policy v3 & Frontier Safety Roadmap를 요약하고, 지금 시점에 왜 중요한지 빠르게 따라잡기 위한 페이지다. 핵심 범위는 역량 임계치별 위험 완화를 명문화하고 공개 로드맵으로 진척도를 투명화하는 거버넌스이다.

**project-internal · `oh-my-claudecode`**
- [Multi-Agent Orchestration](wiki/concepts/multi-agent-orchestration.md) — > 단일 LLM 에이전트를 여러 전문 에이전트의 협업 시스템으로 확장하는 패턴.
- [OMC Delegation Categories](wiki/concepts/omc-delegation-categories.md) — > 태스크 프롬프트를 자동 분류해 모델 티어 + temperature + thinking budget을 한 번에 결정하는 시스템.
- [OMC Hook System](wiki/concepts/omc-hook-system.md) — > Claude Code의 라이프사이클 이벤트에 Node.js 스크립트를 붙여 오케스트레이션, 상태 관리, 키워드 감지를 구현.
- [OMC Magic Keyword](wiki/concepts/omc-magic-keyword.md) — > 자연어 입력에 특정 단어가 포함되면 해당 스킬/모드를 자동 활성화하는 OMC의 핵심 UX.
- [OMC Model Routing](wiki/concepts/omc-model-routing.md) — > 태스크 복잡도에 맞춰 Haiku/Sonnet/Opus 중 하나를 자동 선택. 비용 30~50% 절감의 핵심.
- [OMC Skill Layering](wiki/concepts/omc-skill-layering.md) — > 스킬은 에이전트를 교체하는 게 아니라 행동을 주입(behavior injection) 한다.
- [OMC State Management](wiki/concepts/omc-state-management.md) — > .omc/ 디렉토리 기반 지속 상태 시스템. 컨텍스트 컴팩션을 이겨내고 장기 작업을 재개할 수 있게 한다.
