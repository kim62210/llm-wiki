---
title: AI Development Study Wiki - Index
updated: 2026-04-09
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
> 아직 페이지 없음 - 소스 수집 필요

### Inference (추론/서빙)

**concept**
- [KV Cache](wiki/inference/kv-cache.md) — Key-Value 캐시 재사용으로 비용 90% 절감, stable prefix + variable suffix 설계 원칙

### RAG (검색 증강 생성)
> 아직 페이지 없음 - 소스 수집 필요

### Agents (에이전트)

**concept**
- [How Coding Agents Work](wiki/agents/how-coding-agents-work.md) — LLM 하네스, 시스템 프롬프트, 토큰 캐싱, 도구 호출 루프, reasoning 모드
- [Subagents](wiki/agents/subagents.md) — 컨텍스트 창 한계를 우회하는 하위 에이전트 패턴 (Explore, 병렬, 특화 서브에이전트)

**summary**
- [Evolution of Agentic Patterns (프롬프트에서 하네스까지)](wiki/agents/evolution-of-agentic-patterns.md) — 2022-2026 AI 에이전틱 패러다임 3 에라 연대기 + 부검 보고서

**project-internal · `oh-my-claudecode`**
- [OMC Agent Catalog](wiki/agents/omc-agent-catalog.md) — OMC의 19개 전문 에이전트 + 4개 레인 구조

### Applications (응용)

**summary**
- [Agentic Engineering Guide (Simon Willison)](wiki/applications/agentic-engineering-guide.md) — Simon Willison의 가이드 전체 맵 및 핵심 인사이트
- [Prompts Library (Simon Willison)](wiki/applications/prompts-library.md) — Artifacts, Proofreader, Alt text, Podcast highlights 프롬프트 모음
- [Stitch DESIGN.md 가이드 (Google)](wiki/applications/stitch-design-md-guide.md) — Google Stitch 공식 DESIGN.md 문서 3개 페이지(overview/format/usage) 한국어 요약

**concept**
- [Red/Green TDD](wiki/applications/red-green-tdd.md) — 네 단어로 에이전트에 TDD 규율을 전달하는 프롬프트 패턴
- [First Run the Tests](wiki/applications/first-run-the-tests.md) — 기존 코드베이스 온보딩을 위한 네 단어 프롬프트의 네 가지 효과
- [Agentic Manual Testing](wiki/applications/agentic-manual-testing.md) — Python/Web/브라우저 UI에 대해 에이전트가 수동 테스트를 수행하는 기법
- [Linear Walkthroughs](wiki/applications/linear-walkthroughs.md) — 에이전트가 코드베이스를 선형 설명 문서로 만드는 기법 (Showboat 활용)
- [Interactive Explanations](wiki/applications/interactive-explanations.md) — Cognitive debt를 갚는 인터랙티브 애니메이션 설명 기법

**case-study**
- [GIF Optimization Case Study](wiki/applications/gif-optimization-case-study.md) — Gifsicle → WASM 컴파일 실전 프롬프트 사례

**entity**
- [oh-my-claudecode (OMC)](wiki/applications/oh-my-claudecode.md) — Claude Code 멀티 에이전트 오케스트레이션 플러그인 프레임워크 (허브 페이지)

### Papers (논문)
> 아직 페이지 없음 - 소스 수집 필요

### Tooling (도구)

**entity**
- [Claude Code](wiki/tooling/claude-code.md) — Anthropic의 공식 코딩 에이전트. CLI, Desktop, Web, IDE 확장으로 배포
- [Google Stitch](wiki/tooling/google-stitch.md) — Google의 AI 기반 디자인 도구 (내부 코드네임 Nemo). DESIGN.md 포맷 정의자, Gemini 기반

**concept**
- [Git with Coding Agents](wiki/tooling/git-with-coding-agents.md) — Git을 에이전트의 시간 여행 도구로 활용하는 자연어 프롬프트 패턴
- [Browser Automation for Coding Agents](wiki/tooling/browser-automation-agents.md) — Playwright, agent-browser, Rodney, Showboat 비교와 통합 워크플로우

**project-internal · `oh-my-claudecode`**
- [OMC Execution Modes](wiki/tooling/omc-execution-modes.md) — OMC 6+가지 실행 모드 개요 (Team, Autopilot, Ralph, Ultrawork, CCG, Ralplan 등)
- [OMC Autopilot](wiki/tooling/omc-autopilot.md) — 아이디어→동작 코드 5-Phase 자율 실행 파이프라인
- [OMC Ralph Mode](wiki/tooling/omc-ralph-mode.md) — 검증 완료까지 중단하지 않는 persistence 모드
- [OMC Ultrawork](wiki/tooling/omc-ultrawork.md) — 최대 병렬성의 non-team 버스트 실행 (최대 6개 동시 에이전트)
- [OMC Team Mode](wiki/tooling/omc-team-mode.md) — 5-stage staged 파이프라인 기반 canonical 오케스트레이션
- [OMC CCG](wiki/tooling/omc-ccg.md) — Claude-Codex-Gemini 삼중 자문 합성 스킬
- [OMC Ralplan](wiki/tooling/omc-ralplan.md) — Planner+Architect+Critic 컨센서스 반복 기획
- [OMC Deep Interview](wiki/tooling/omc-deep-interview.md) — Socratic 질문 + 수학적 ambiguity gating 요구사항 정제

### Concepts (개념)

**concept — 에이전틱 패러다임 3 에라**
- [Relocating Rigor (엄밀함의 이동)](wiki/concepts/relocating-rigor.md) — Chad Fowler의 메타 원칙. 엔지니어링 엄밀함은 사라지지 않고 이동할 뿐이다
- [Prompt Engineering (프롬프트 엔지니어링)](wiki/concepts/prompt-engineering.md) — 2022-2024 지배적 패러다임. CoT, ReAct, Andrew Ng의 4 patterns
- [Context Engineering (컨텍스트 엔지니어링)](wiki/concepts/context-engineering.md) — 2025 중반 패러다임. Anthropic Write/Select/Compress/Isolate 4전략
- [Harness Engineering (하네스 엔지니어링)](wiki/concepts/harness-engineering.md) — 2026+ 패러다임. Agent = Model + Harness
- [LLM as OS (운영체제로서의 LLM)](wiki/concepts/llm-as-os.md) — Karpathy의 OS 메타포. Kernel/RAM/FS/syscall 대응
- [Harness Quadrants (하네스 4사분면)](wiki/concepts/harness-quadrants.md) — Fowler/Böckeler의 2×2 하네스 분류 (Guides/Computational/System prompts/Inferential)
- [Lethal Trifecta (치명적 3요소)](wiki/concepts/lethal-trifecta.md) — Simon Willison의 보안 원칙 + Meta Rule of Two
- [Blind Prompting (맹목적 프롬프팅)](wiki/concepts/blind-prompting.md) — Mitchell Hashimoto의 프롬프트 안티패턴 지적
- [Ralph Pattern (랠프 패턴)](wiki/concepts/ralph-pattern.md) — Geoffrey Huntley의 클린 컨텍스트 반복 루프. 파일시스템을 진실의 원천으로 사용하는 에이전트 실행 패턴

**concept — 에이전틱 엔지니어링 기본**
- [Agentic Engineering](wiki/concepts/agentic-engineering.md) — 코딩 에이전트의 도움을 받는 프로페셔널 소프트웨어 개발의 정의
- [Vibe Coding](wiki/concepts/vibe-coding.md) — Karpathy가 만든 용어. 리뷰 없이 LLM으로 프로토타입 코드를 얻는 방식 + 2025-09 Hangover 사례
- [Coding Agent](wiki/concepts/coding-agent.md) — 코드를 작성하고 실행할 수 있는 에이전트의 정의와 예시
- [Writing Code is Cheap Now](wiki/concepts/code-is-cheap.md) — 코드 작성 비용 하락이 만드는 새로운 트레이드오프
- [Hoard Things You Know How To Do](wiki/concepts/hoard-things-you-know-how-to-do.md) — 작동하는 예제를 축적해 에이전트와 재조합하는 원칙
- [Better Code With Agents](wiki/concepts/better-code-with-agents.md) — 에이전트로 *더 나은* 코드를 쓰는 것은 선택의 문제
- [Anti-patterns in Agentic Engineering](wiki/concepts/anti-patterns.md) — 리뷰 안 한 에이전트 코드를 동료에게 떠넘기는 안티패턴
- [Cognitive Debt](wiki/concepts/cognitive-debt.md) — 에이전트 코드를 이해하지 못할 때 쌓이는 인지 부채

**concept — 디자인 시스템**
- [DESIGN.md 포맷](wiki/concepts/design-md-format.md) — AI 디자인 에이전트가 읽는 평문 디자인 시스템 포맷 (6개 섹션 고정 순서, portable)
- [AI 친화적 디자인 시스템 문서화](wiki/concepts/ai-readable-design-system.md) — README/AGENTS/DESIGN 세 파일 체계와 "living artifact" 원칙
- [디자인 토큰](wiki/concepts/design-tokens.md) — 3-tier 토큰 모델 (primitive → semantic → component)과 AI 에이전트 관점

**project-internal · `oh-my-claudecode`**
- [Multi-Agent Orchestration (OMC 관점)](wiki/concepts/multi-agent-orchestration.md) — OMC 기준 멀티 에이전트 오케스트레이션 설계 (※ 향후 source-agnostic concept로 분리 필요)
- [OMC Magic Keyword](wiki/concepts/omc-magic-keyword.md) — 자연어 입력의 키워드 기반 자동 스킬/모드 활성화
- [OMC Skill Layering](wiki/concepts/omc-skill-layering.md) — 스킬이 에이전트를 교체하지 않고 행동을 주입하는 구조
- [OMC Model Routing](wiki/concepts/omc-model-routing.md) — Haiku/Sonnet/Opus 3-tier 자동 라우팅으로 비용 최적화
- [OMC Hook System](wiki/concepts/omc-hook-system.md) — Claude Code 라이프사이클 이벤트 기반 훅 시스템
- [OMC State Management](wiki/concepts/omc-state-management.md) — `.omc/` 기반 지속 상태, compaction 극복
- [OMC Delegation Categories](wiki/concepts/omc-delegation-categories.md) — 태스크 자동 분류 → 모델 티어 + temperature + thinking budget 결정

## 지식 갭 / TODO

### 일반 개념 수집 필요
- [ ] Max Woolf의 원본 글 "An AI agent coding skeptic tries AI agent coding, in excessive detail"
- [ ] Every의 "Compound Engineering Loop" 원본 방법론
- [ ] Karpathy의 "vibe coding" 원본 트윗/글
- [ ] Karpathy의 "Software 3.0" 원본 (Latent Space 인터뷰)
- [ ] Shopify Tobi Lütke의 2025-06-19 "context engineering" 원본 트윗
- [ ] Mitchell Hashimoto "Prompt Engineering vs Blind Prompting" 원문
- [ ] Mitchell Hashimoto "My AI Adoption Journey" (2026-02) 원문
- [ ] Martin Fowler / Birgitta Böckeler 하네스 4사분면 원본 아티클
- [ ] Simon Willison의 Lethal Trifecta 원본 블로그 포스트
- [ ] Meta의 "Rule of Two" 공식 문서
- [ ] Andrew Ng "Four Agentic Design Patterns" (2024) 원본
- [ ] Chad Fowler의 "Relocating Rigor" (Honeycomb) 원문

### 논문 수집 필요 (paper 페이지 후보)
- [ ] Wei et al. 2022 — Chain-of-Thought Prompting (arXiv:2201.11903)
- [ ] Yao et al. 2022 — ReAct: Synergizing Reasoning and Acting (arXiv:2210.03629)
- [ ] Yao et al. 2023 — Tree-of-Thought (arXiv:2305.10601)
- [ ] Madaan et al. 2023 — Self-Refine (arXiv:2303.17651)
- [ ] Shinn et al. 2023 — Reflexion (arXiv:2303.11366)
- [ ] Liu et al. 2023 — Lost in the Middle (arXiv:2307.03172)

### 케이스 스터디 수집 필요
- [ ] Anthropic 3-Agent 아키텍처 상세 (Planner/Generator/Evaluator)
- [ ] OpenAI Codex 5개월 실험 원본 (100만 라인 / 1500 PR)

### Tooling 확장
- [ ] Showboat, Rodney 각각에 대한 별도 entity 페이지 (현재는 browser-automation-agents에 통합)
- [ ] OpenAI Codex, Gemini CLI/Jules 개별 entity 페이지
- [ ] Tesseract.js, PDF.js 같은 언급된 도구들 개별 페이지
- [ ] Google Stitch 나머지 섹션 (Learn, MCP, SDK, Prompting, Device Types, Design Modes, Variants, Controls & Hotkeys)

### Design 관련 추가 수집
- [ ] AGENTS.md 관례의 역사와 상세 (OpenAI/Cursor/Claude Code 생태계)
- [ ] Design Tokens Community Group (W3C) 공식 JSON 표준
- [ ] Style Dictionary, Tokens Studio 같은 토큰 도구 개별 페이지
- [ ] Material Design color role 체계 상세
- [ ] WCAG 접근성 가이드라인 (DESIGN.md의 "Do's" 참조처)

### 리팩토링 필요
- [ ] `concepts/multi-agent-orchestration.md` — 현재 OMC 중심 내용. source-agnostic한 `concept`판(`multi-agent-orchestration`)과 OMC 전용 `project-internal`판(`omc-orchestration-model`)으로 분리
- [ ] OMC 관련 추가 수집: Learner/Skill 학습 시스템, Notepad Wisdom, MCP 툴 카탈로그, Ecomode, Ultraqa, Visual-Verdict, Web-Clone, autoresearch runtime, HUD statusline, Notification 통합 (Telegram/Discord/Slack/OpenClaw)
