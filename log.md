## 2026-04-10 — Recursive ingest 배치 (Pydantic AI / Deep Agents 세부 문서)
- **대상**: 공식 세부 문서 7개 (`pydantic.dev` 3개, `docs.langchain.com` 4개)
- **생성 페이지**:
  - `wiki/tooling/pydantic-ai-agent-core.md`
  - `wiki/tooling/pydantic-ai-mcp-overview.md`
  - `wiki/tooling/pydantic-ai-durable-execution-overview.md`
  - `wiki/tooling/deep-agents-quickstart.md`
  - `wiki/tooling/deep-agents-subagents.md`
  - `wiki/tooling/deep-agents-memory.md`
  - `wiki/tooling/deep-agents-production.md`
- **수행 내용**:
  - `raw/recursive-sources/2026-04-10-pydantic-deepagents/` 아래 원문 snapshot 저장
  - summary 페이지에 구조도 / 비교표 / 체크리스트를 추가해 심화 위키 수준으로 작성
  - parent entity(`pydantic-ai.md`, `deep-agents.md`)에 하위 문서 읽기 경로 추가

## 2026-04-10 — Recursive ingest 배치 (OpenAI Agents SDK / LangGraph 세부 문서)
- **대상**: 공식 세부 문서 7개 (`openai-agents-js` 4개, `docs.langchain.com` 3개)
- **생성 페이지**:
  - `wiki/tooling/openai-agents-sdk-quickstart.md`
  - `wiki/tooling/openai-agents-sdk-handoffs.md`
  - `wiki/tooling/openai-agents-sdk-sessions.md`
  - `wiki/tooling/openai-agents-sdk-model-context-protocol.md`
  - `wiki/tooling/langgraph-quickstart.md`
  - `wiki/tooling/langgraph-persistence.md`
  - `wiki/tooling/langgraph-durable-execution.md`
- **수행 내용**:
  - `raw/recursive-sources/2026-04-10-openai-langgraph/` 아래 원문 snapshot 저장
  - 각 summary 페이지를 표 / 구조도 / 읽기 경로 포함한 심화 위키 수준으로 작성
  - parent entity(`openai-agents-sdk.md`, `langgraph.md`)에 하위 문서 읽기 경로 추가

## 2026-04-10 — standalone 문서 심화 배치
- **대상**: 새로 승격된 standalone 문서 5개
- **수행 내용**:
  - 표 / 구조도 / 읽기 가이드를 추가해 summary와 paper의 학습 가치를 강화
- **대표 문서**:
  - `wiki/tooling/claude-agent-sdk-overview.md`
  - `wiki/tooling/mcp-specification-2025-11-25.md`
  - `wiki/agents/deep-research-agents-roadmap.md`
  - `wiki/papers/agentic-rl-survey-paper.md`
  - `wiki/concepts/the-lethal-trifecta-article.md`

## 2026-04-10 — 수동 고급 편집 배치
- **대상**: 상위 핵심 문서 6개
- **수행 내용**:
  - 비교표, 구조도, 읽기 순서 가이드를 추가해 심화 위키 수준으로 강화
- **대표 문서**:
  - `wiki/applications/ai-hot-topics-2026-04.md`
  - `wiki/concepts/context-engineering.md`
  - `wiki/tooling/model-context-protocol-mcp.md`
  - `wiki/tooling/long-running-agent-harnesses.md`
  - `wiki/agents/long-horizon-agent-benchmarks.md`
  - `wiki/tooling/gpt-5-4.md`

## 2026-04-10 — Recursive ingest 결과 흡수 (SDK/MCP 세부 문서)
- **대상**: `raw/recursive-sources/2026-04-10-sdk-mcp/` 아래 5개 문서
- **생성 페이지**:
  - `wiki/tooling/claude-agent-loop.md`
  - `wiki/tooling/claude-agent-sdk-quickstart.md`
  - `wiki/tooling/claude-agent-sessions.md`
  - `wiki/tooling/mcp-architecture.md`
  - `wiki/tooling/mcp-authorization-draft.md`

# Activity Log

## 2026-04-10 — Ingest 계속: sixth standalone promotion batch
- **대상**: 남은 source-specific 고가치 문서
- **생성 페이지**:
  - `summary` 3개
  - `paper` 1개
  - `concept summary` 1개
- **추가된 주요 페이지**:
  - `wiki/concepts/the-lethal-trifecta-article.md`
  - `wiki/applications/writing-about-agentic-engineering-patterns.md`
  - `wiki/papers/loop-paper.md`
  - `wiki/rag/context-rot-report.md`
  - `wiki/tooling/claude-opus-4-5-release-notes.md`

## 2026-04-10 — 비교 문서 배치
- **대상**: 이미 수집·승격된 모델/벤치마크 페이지를 가로지르는 summary 문서
- **생성 페이지**:
  - `wiki/applications/frontier-model-comparison-2026-04.md`
  - `wiki/applications/agent-benchmark-comparison-2026-04.md`

## 2026-04-10 — Ingest 계속: provenance merge batch
- **대상**: 남아 있던 duplicate fetched source 10개
- **수행 내용**:
  - 새 페이지를 더 만들지 않고, 대응하는 standalone 페이지의 `sources:`에 alternate raw path를 병합
- **결과**:
  - remaining fetched source: 0
  - broken wikilinks: 0
  - index missing-page: 0

## 2026-04-10 — Ingest 계속: recursive docs batch (SDK / MCP)
- **대상**: standalone page에서 파생된 2차 링크 중 MCP / Claude Agent SDK 핵심 문서
- **생성 페이지**:
  - `summary` 5개
- **추가된 주요 페이지**:
  - `wiki/tooling/claude-agent-sdk-quickstart.md`
  - `wiki/tooling/claude-agent-loop.md`
  - `wiki/tooling/claude-agent-sessions.md`
  - `wiki/tooling/mcp-architecture.md`
  - `wiki/tooling/mcp-authorization-draft.md`

## 2026-04-10 — Ingest 계속: standalone source pages 추가 승격
- **대상**: 이미 수집된 hot-topic raw source 중 고가치 공식 글/스펙/논문
- **생성 페이지**:
  - `summary` 4개
  - `entity` 1개
  - `paper` 1개
- **추가된 주요 페이지**:
  - `wiki/agents/anthropic-multi-agent-research-system.md`
  - `wiki/agents/agent-skills-specification.md`
  - `wiki/tooling/effective-harnesses-for-long-running-agents.md`
  - `wiki/tooling/model-context-protocol-mcp.md`
  - `wiki/tooling/writing-effective-tools-for-agents.md`
  - `wiki/papers/context-engineering-open-source-software-paper.md`

## 2026-04-10 — Ingest 계속: second standalone promotion batch
- **대상**: 남은 high-signal fetched source (논문 / 모델 / 인프라 글)
- **생성 페이지**:
  - `paper` 3개
  - `summary` 1개
  - `entity` 1개
- **추가된 주요 페이지**:
  - `wiki/papers/agentic-rl-survey-paper.md`
  - `wiki/papers/plan-and-act-paper.md`
  - `wiki/papers/are-gaia2-paper.md`
  - `wiki/tooling/scaling-managed-agents.md`
  - `wiki/tooling/claude-sonnet-4-5.md`

## 2026-04-10 — Ingest 계속: third standalone promotion batch
- **대상**: 남은 high-signal fetched source (deep research / MCP / context engineering)
- **생성 페이지**:
  - `paper` 1개
  - `summary` 3개
  - `entity` 1개

## 2026-04-10 — Ingest 계속: fourth standalone promotion batch
- **대상**: 남은 high-signal fetched source (agent RL / planning / MCP spec)
- **생성 페이지**:
  - `paper` 3개
  - `summary` 2개
- **추가된 주요 페이지**:
  - `wiki/papers/agentgym-rl-paper.md`
  - `wiki/papers/reveal-paper.md`
  - `wiki/papers/research-learning-to-reason-with-search-paper.md`
  - `wiki/agents/deep-research-agents-roadmap.md`
  - `wiki/tooling/mcp-specification-2025-11-25.md`

## 2026-04-10 — Ingest 계속: fifth standalone promotion batch
- **대상**: 구현 레퍼런스와 운영 노트 source
- **생성 페이지**:
  - `summary` 2개
  - `entity` 2개
  - `case-study` 1개
- **추가된 주요 페이지**:
  - `wiki/tooling/claude-agent-sdk-overview.md`
  - `wiki/tooling/claude-agent-sdk-typescript.md`
  - `wiki/tooling/claude-opus-4-5.md`
  - `wiki/tooling/mcp-roadmap-development.md`
  - `wiki/applications/openhands-swe-bench-scaling-notes.md`
- **추가된 주요 페이지**:
  - `wiki/papers/deep-research-agents-roadmap-paper.md`
  - `wiki/agents/skywork-deepresearchagent.md`
  - `wiki/concepts/effective-context-engineering-anthropic.md`
  - `wiki/tooling/the-2026-mcp-roadmap.md`
  - `wiki/tooling/what-is-mcp.md`

## 2026-04-10 — Ingest 확장: 핵심 논문 paper 페이지 생성
- **대상**: hot-topic 수집 raw 중 핵심 논문/서베이 10편
- **생성 페이지 수**: `paper` 10개
- **주요 목적**: 비어 있던 `papers` 카테고리를 채우고, 개념/엔티티 허브와 별도로 논문 자체의 기여·결과·한계를 읽을 수 있게 함
## 2026-04-10 — Deepen: hot-topic long-form expansion
- **대상**: hot-topic 파생 페이지 중 실제 본문 밀도가 낮은 페이지 전반
- **수행 내용**:
  - 97개 페이지에 `핵심 포인트 / source로 보면 / 실무 관점` 장문 섹션 추가
  - 기존 `source 기반 참고`는 유지
  - summary 허브(`wiki/applications/ai-hot-topics-2026-04.md`)에도 읽기 가이드와 해석 층위를 보강
- **결과**:
  - 장문 심화 적용 페이지: 97개
  - manifest 성공 상태 유지: 452 / 452
  - 깨진 위키링크: 0
  - index 누락 페이지: 0

## 2026-04-10 — Parallel deepening: hot-topic 장문 심화
- **대상**: hot-topic 파생 페이지 전반 (현재 98개 반영 페이지 기준)
- **수행 내용**:
  - agents / concepts / inference / rag / tooling / training 카테고리별 장문 설명 섹션 추가
  - entity 페이지는 `핵심 포인트` + `실무 관점` 보강
  - concept 페이지는 `핵심 메커니즘` + `실무 관점` 보강
  - source 기반 참고 섹션은 유지하고, 그 위에 해석 가능한 장문 본문을 덧대는 방식으로 확장

## 2026-04-10 — Deepen: hot-topic 파생 페이지 장문 확장
- **대상**: hot-topic 기반 topic packet 97개 / 반영 페이지 98개
- **수행 내용**:
  - inference / rag / tooling / training / agents / concepts 전반에 장문 해석 섹션 추가
  - `해석 포인트`, `실무 관점`, `2026년 4월 큐레이션 요약`, `source 기반 참고` 구조로 정렬
  - 얇은 허브형 문장을 운영/비교 관점 문단으로 확장
- **결과**:
  - hot-topic 관련 페이지 97개 갱신
  - manifest 수집 성공: 452 / 452 유지
  - 깨진 위키링크: 0
  - index 누락 페이지: 0

## 2026-04-10 — Enrich: hot-topic source synthesis 보강
- **대상**: `raw/2026-04-10-hot-ai-topics-100.md`에서 파생된 hot-topic 위키 페이지 전반
- **수행 내용**:
  - 실패 링크 3건을 대체 접근 경로로 복구
  - `raw/hot-topics-sources/2026-04-10/` 아래 개별 원문 snapshot 정리
  - hot-topic 관련 페이지 97개에 대해 `source 기반 참고` 섹션을 source 제목 + 짧은 메모 중심으로 재정리
  - 중복되던 `2026년 4월 핫토픽 ...` 보조 섹션을 `2026년 4월 큐레이션 요약`으로 통합
- **결과**:
  - manifest 수집 성공: 452 / 452
  - 깨진 위키링크: 0
  - index 누락 페이지: 0

## 2026-04-10 — Source Fetch: hot topics reference crawl
- **대상 raw**: `raw/2026-04-10-hot-ai-topics-100.md`
- **정규화된 URL 수**: 452개
- **수집 성공**: 452개
- **수집 실패**: 0개
- **snapshot 저장 위치**: `raw/hot-topics-sources/2026-04-10/`
- **topic packet 수**: 97개
- **위키 재-ingest**: 개별 topic packet을 각 위키 페이지의 `sources:`와 `## source 기반 참고` 섹션에 반영
- **후속 복구**:
  - OpenReview / TACL / Arize의 실패 링크 3건을 대체 URL로 재수집해 현재 실패 0건 상태로 정리
## 2026-04-10 — Lint: hot-topics ingest 정리
- **대상**: hot topics ingest 결과 + 위키 전역 링크/프론트매터 무결성
- **수행 내용**:
  - alias-aware 위키링크 점검
  - 누락 alias 보강
  - 누락 `sources` 프론트매터 2건 수정
  - 신규 보강 페이지 2개 추가: `wiki/concepts/lost-in-the-middle.md`, `wiki/tooling/tesseract-js.md`
  - `index.md`, `log.md` 정리
- **결과**:
  - alias-aware 깨진 위키링크: 34건 → 0건
  - `entity` / `project-internal`의 누락 `project` 필드: 0건
  - `index.md` 등록 누락 페이지: 0건

## 2026-04-10 — Ingest: 2026년 4월 AI 개발 핫토픽 100선
- **소스**: `raw/2026-04-10-hot-ai-topics-100.md`
- **결과 요약**:
  - 이번 raw가 반영된 전체 페이지: 98개
  - `entity`: 39개
  - `concept`: 53개
  - `summary`: 3개
  - `case-study`: 1개
  - `project-internal`: 2개
- **메모**:
  - 링크가 많은 큐레이션 문서였기 때문에, 개별 원문을 추가 수집한 것이 아니라 raw 내부 신호를 기준으로 허브/개념 페이지로 분해했다.
  - 후속 확장이 필요한 항목은 entity 허브에서 별도 source ingest로 깊이를 늘리는 방식이 적합하다.

## 2026-04-10 (오후) — Ingest: "프롬프트에서 하네스까지" AI 에이전틱 패턴 4년 연대기
- **소스**: https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html
- **성격**: 2022-2026 AI 에이전틱 개발 패러다임 3 에라(Prompt → Context → Harness Engineering) 연대기 + 부검 보고서
- **raw 파일**: `raw/2026-04-09-evolution-of-ai-agentic-patterns.md` (WebFetch로 한국어 본문 + 영어 원문 핵심 구절 보존)
- **생성 페이지 11개**:
  - **summary (1)**:
    - `wiki/agents/evolution-of-agentic-patterns.md` — 3 에라 전체 요약 + Mermaid 타임라인 다이어그램
  - **concept (10)**:
    - `wiki/concepts/relocating-rigor.md` — Chad Fowler의 메타 원칙 (엄밀함은 이동한다)
    - `wiki/concepts/prompt-engineering.md` — Era 1 (2022-2024) CoT/ReAct/Tree-of-Thought/Self-Refine/Ng 4 patterns
    - `wiki/concepts/context-engineering.md` — Era 2 (2025) Anthropic 4전략 + LLM OS 연결
    - `wiki/concepts/harness-engineering.md` — Era 3 (2026+) Agent = Model + Harness
    - `wiki/concepts/llm-as-os.md` — Karpathy OS 메타포 (Kernel/RAM/FS/syscall 대응)
    - `wiki/inference/kv-cache.md` — KV 캐시 구조 + stable prefix/variable suffix 설계 (category: inference, inference 디렉토리 신설)
    - `wiki/concepts/lethal-trifecta.md` — Simon Willison 3요소 + Meta Rule of Two 보안
    - `wiki/concepts/harness-quadrants.md` — Fowler/Böckeler 2×2 하네스 분류 (네 사분면)
    - `wiki/concepts/blind-prompting.md` — Mitchell Hashimoto의 프롬프트 안티패턴
    - `wiki/concepts/ralph-pattern.md` — Geoffrey Huntley의 클린 컨텍스트 반복 루프 패턴 (파일시스템을 진실의 원천으로)
- **갱신 페이지 2개 (concept 병합)**:
  - `wiki/concepts/vibe-coding.md` — 2025-09 Vibe Coding Hangover 사건, CodeRabbit 메트릭, Simon Willison 교정 인용 추가
  - `wiki/concepts/agentic-engineering.md` — 3 에라 연대기 관점에서의 위치 섹션 추가
- **Mermaid 다이어그램**: 10개 페이지 중 8개에 포함 (3 에라 타임라인, OS 메타포 대응, 4사분면 의사결정 트리, KV 캐시 히트/미스 흐름, harness-quadrants 2×2 결정 트리, prompt engineering ReAct 루프, context engineering 4전략 트리, harness engineering 3-Agent 아키텍처)
- **디렉토리 신설**: `wiki/inference/` (기존에 없었음. KV Cache가 첫 페이지)
- **분류 판단 메모**:
  - 소스는 에세이/연대기 성격이므로 기본 요약 페이지는 `summary`. 이를 `agents/` 카테고리에 배치 (에이전틱 패턴이 주제)
  - 3 에라(prompt/context/harness engineering)는 모두 source-agnostic한 일반 개념이므로 `concept`
  - KV Cache는 추론 최적화 기술이므로 `category: inference`. 디렉토리도 이에 맞춰 신설
  - Harness Quadrants는 이미 이번 작업 중 다른 버전이 작성되어 있음을 발견 (동등한 품질) — 그대로 유지
  - Lethal Trifecta와 Meta Rule of Two는 한 페이지에 묶음 (동일 주제)
- **기존 concept 병합 규칙 준수**: vibe-coding과 agentic-engineering 페이지에 덮어쓰기 없이 새 섹션만 추가, `sources:` 배열에 raw 파일 추가
- **언어 규칙 준수**: 모든 본문 한국어, 영어 원문은 blockquote 인용으로만 보존 (Mitchell Hashimoto, Simon Willison 핵심 문장)
- **발견된 지식 갭** (index.md TODO에 반영):
  - Mitchell Hashimoto의 두 블로그 포스트 (Blind Prompting, My AI Adoption Journey) 원문
  - Tobi Lütke의 2025-06-19 context engineering 원본 트윗
  - Karpathy의 Software 3.0 원본
  - Anthropic 3-Agent 아키텍처 상세
  - OpenAI Codex 5개월 실험 원본
  - CoT/ReAct/ToT/Self-Refine/Reflexion/Lost-in-Middle 원본 논문 (paper 타입 후보 6개)
  - Fowler/Böckeler 4사분면 원본 아티클
  - Simon Willison Lethal Trifecta 원문
  - Meta Rule of Two 공식 문서
  - Andrew Ng "Four Agentic Design Patterns" 원본
  - Chad Fowler "Relocating Rigor" (Honeycomb) 원문

## 2026-04-10 — Ingest: Google Stitch DESIGN.md 문서
- **소스**: Google Stitch 공식 문서 DESIGN.MD 섹션 3개 페이지
  - https://stitch.withgoogle.com/docs/design-md/overview/
  - https://stitch.withgoogle.com/docs/design-md/format/
  - https://stitch.withgoogle.com/docs/design-md/usage/
- **수집 방법**: Stitch는 인증이 필요한 SPA(iframe 내부)라 WebFetch로는 JavaScript만 잡힘. **chrome-devtools MCP**로 실제 렌더링 후 a11y 스냅샷으로 전체 텍스트 추출
- **raw 파일**: `raw/2026-04-09-stitch-design-md.md` (3개 페이지 한국어 번역 + 영어 원문 핵심 구절 blockquote 보존)
- **생성 페이지 5개**:
  - **summary (1)**:
    - `wiki/applications/stitch-design-md-guide.md` — 3개 페이지 통합 요약 + Mermaid 구조 다이어그램
  - **entity (1)** [project: Google Stitch]:
    - `wiki/tooling/google-stitch.md` — Stitch 제품 개요, 아키텍처 다이어그램, MCP/SDK/Learn 섹션 네비게이션
  - **concept (3)**:
    - `wiki/concepts/design-md-format.md` — 6개 섹션(Overview/Colors/Typography/Elevation/Components/Do's and Don'ts) 명세와 철학
    - `wiki/concepts/ai-readable-design-system.md` — README/AGENTS/DESIGN 세 파일 체계, "living artifact" 원칙, 기계 가독성 요건
    - `wiki/concepts/design-tokens.md` — 3-tier 모델(primitive/semantic/component) + Mermaid 계층도, AI 에이전트 관점
- **Mermaid 다이어그램**: 5개 페이지 중 4개에 포함 (summary 1개, entity 1개, concept 2개)
- **언어 규칙 준수**: 모든 본문 한국어. 영어 원문 인용은 blockquote로만 보존. 기술 용어는 괄호 병기
- **분류 판단 주의점**:
  - "dual representation" (markdown + structured tokens)은 Stitch 고유 메커니즘 → `design-md-format` concept 페이지에서는 간단히만 언급하고 상세는 `google-stitch` entity로 미루기
  - DESIGN.md 포맷 자체는 source-agnostic (Claude Code 등 다른 에이전트도 읽을 수 있음) → concept로 분류
  - Stitch 제품 고유 기능(Design System 패널, export)은 entity/project-internal 영역
- **발견된 지식 갭**:
  - Google Stitch의 나머지 docs 섹션 (Learn/MCP/SDK/Prompting/Device Types/Design Modes/Variants/Controls)
  - AGENTS.md 관례의 역사 (OpenAI/Cursor/Claude Code 생태계)
  - Design Tokens Community Group (W3C) 공식 JSON 표준
  - Style Dictionary, Tokens Studio 같은 도구들
  - Material Design color role 체계 상세
  - WCAG 접근성 가이드라인

## 2026-04-09 (새벽) — Obsidian Vault 연결 + GitHub remote 설정
- **GitHub remote 연결**: `git@github-personal:kim62210/llm-wiki.git`을 `origin`으로 추가. 원격 저장소는 비어 있어 push만 하면 됨 (아직 push 전, 사용자 승인 대기).
- **Obsidian 호환성 확보**: 파일명은 kebab-case(`agentic-engineering-guide.md`)지만 본문 위키링크는 공백형(`[[agentic engineering guide]]`)이라 Obsidian 기본 파일명 해결로는 링크가 깨진다. 해결책으로 **38개 페이지 전체에 `aliases:` frontmatter 필드 추가**. 각 페이지가 실제로 참조되는 모든 wikilink 텍스트를 alias로 포함.
- **특수 케이스 처리**:
  - `browser-automation-agents.md` — Playwright, Rodney, Showboat, agent-browser 4개 별칭 통합 (현재 dedicated 페이지 없음)
  - `omc-hook-system.md` — "Hooks" 별칭
  - `omc-skill-layering.md` — "Skills" 별칭
  - `omc-state-management.md` — "State Management" 별칭
  - `omc-agent-catalog.md` — "Agents" 별칭
  - `omc-magic-keyword.md` — "매직 키워드" (한글) 별칭
  - `oh-my-claudecode.md` — "OMC", "oh-my-claudecode" 등 축약형 별칭
- **미해결 wikilink (knowledge gap)**:
  - `[[Tesseract.js]]` — dedicated 페이지 없음. Obsidian에서 unresolved link로 표시되어 자연스러운 knowledge gap marker 역할
- **`.gitignore` 갱신**: Obsidian workspace 파일(`.obsidian/workspace*`, `cache`, `graph.json`), 플러그인 local data, `.omx/`, `.omc/state/` 등 user-specific/민감 파일 제외
- **`README.md` 신규 생성**: 저장소 루트에 README 작성 — 디렉토리 구조, 두 축 분류 모델, Obsidian vault 열기 가이드, 권장 설정, 위키링크 해결 방식, Mermaid/Graph view 사용법, 새 페이지 추가 스킬 안내
- **검증**: 38/38 wiki 페이지에 `aliases:` 필드 정상 삽입 확인

## 2026-04-09 (심야) — 시스템 개선: Mermaid 다이어그램 도입
- **배경**: 구조·흐름·관계 설명을 글과 ASCII art로만 처리하면 가독성과 유지보수성이 떨어짐. Mermaid는 GitHub/Obsidian/VS Code가 기본 지원하므로 텍스트 기반 diff 추적과 렌더링을 모두 얻을 수 있음.
- **`CLAUDE.md` 갱신**: 작성 스타일 섹션 아래에 "다이어그램 작성 규칙 (Mermaid)" 섹션 신설:
  - 언제 Mermaid를 쓰는가 / 쓰지 않는가
  - 다이얼렉트 선택 가이드 (flowchart / sequenceDiagram / stateDiagram-v2 / classDiagram)
  - 7가지 작성 규칙 (ASCII 금지, 간결성, 한글 레이블 OK, 코드 펜스, 렌더링 확인, 설명 병기, 스타일 지시 자제)
  - 타입별 적용 힌트 (concept/entity/project-internal/case-study/summary/paper)
- **`~/.claude/skills/wiki-ingest/SKILL.md` 갱신**: 실행 절차에 Section 7 "다이어그램화 판단 (Mermaid)" 추가. ASCII art 금지, Mermaid 우선 규칙 명시. 섹션 번호 재조정 (7→11).
- **기존 페이지 8개에 Mermaid 추가/대체**:
  - **신규 추가 (4)**:
    - `wiki/agents/how-coding-agents-work.md` — 에이전트 루프 flowchart
    - `wiki/agents/subagents.md` — parent/child spawn 구조 flowchart
    - `wiki/concepts/omc-model-routing.md` — task → tier → agent 의사결정 트리
    - `wiki/applications/red-green-tdd.md` — TDD Red/Green/Refactor stateDiagram
  - **ASCII → Mermaid 리팩토링 (4)**:
    - `wiki/concepts/multi-agent-orchestration.md` — orchestrator→에이전트 flowchart
    - `wiki/concepts/omc-hook-system.md` — 컨텍스트 보존 전략 flowchart (컴팩션 루프 포함)
    - `wiki/tooling/omc-autopilot.md` — 5-Phase 파이프라인 flowchart (validation 피드백 루프 포함)
    - `wiki/tooling/omc-team-mode.md` — 5-Stage 파이프라인 stateDiagram
- **검증**: 8/8 파일에 `mermaid` 코드 펜스 정상 삽입 확인
- **남은 작업 (TODO)**:
  - `omc-execution-modes.md`, `oh-my-claudecode.md` 전체 아키텍처 다이어그램
  - `omc-delegation-categories.md` 카테고리 판정 트리
  - `agentic-manual-testing.md` 수동 테스트 워크플로우
  - `interactive-explanations.md` cognitive debt 상환 플로우

## 2026-04-09 (밤) — 시스템 개선: 페이지 타입 축 도입
- **배경**: OMC 관련 페이지들이 `concepts/` 카테고리에 섞여 있어 Karpathy의 source-agnostic concept 노드 원칙과 충돌. "카테고리 축 하나"만으로는 일반 개념과 프로젝트 내부 디테일을 구분할 수 없음을 발견.
- **변경 사항**: 카테고리(주제) 축과 독립된 **페이지 타입(성격)** 축 도입. 타입 6종 정의:
  - `concept` — source-agnostic 일반 개념 (여러 소스에서 누적)
  - `entity` — 특정 프로젝트/도구/인물 허브
  - `project-internal` — 특정 프로젝트 내부 구현/기능 디테일
  - `case-study` — "어떻게 만들었나" narrative
  - `summary` — 특정 소스의 압축 요약
  - `paper` — 논문 요약
- **`CLAUDE.md` 갱신**: 두 축 분류 모델, 페이지 타입 정의, 타입별 편집 규범, 타입 간 교차참조 규칙 표, 프론트매터 템플릿(page_type/project 필드 추가) 전면 재작성
- **기존 페이지 프론트매터 마이그레이션 (38개)**:
  - `concept` (19): agentic-engineering, vibe-coding, coding-agent, code-is-cheap, hoard-things-you-know-how-to-do, better-code-with-agents, anti-patterns, cognitive-debt, how-coding-agents-work, subagents, red-green-tdd, first-run-the-tests, agentic-manual-testing, linear-walkthroughs, interactive-explanations, git-with-coding-agents, browser-automation-agents
  - `entity` (2): claude-code (project: Claude Code), oh-my-claudecode (project: oh-my-claudecode)
  - `project-internal` (16, project: oh-my-claudecode): omc-agent-catalog, multi-agent-orchestration, omc-delegation-categories, omc-hook-system, omc-magic-keyword, omc-model-routing, omc-skill-layering, omc-state-management, omc-execution-modes, omc-autopilot, omc-ralph-mode, omc-ultrawork, omc-team-mode, omc-ccg, omc-ralplan, omc-deep-interview
  - `summary` (2): agentic-engineering-guide, prompts-library
  - `case-study` (1): gif-optimization-case-study
- **`index.md` 재구성**: 카테고리 섹션 내에서 **타입별 서브섹션**으로 분리. 일반 개념/도구와 특정 프로젝트(oh-my-claudecode) 그룹이 시각적으로 구분됨.
- **`~/.claude/skills/wiki-ingest/SKILL.md` 갱신**: 실행 절차에 "페이지 계획 (타입 판단 필수 단계)" 추가. concept 오염 방지 규칙, 타입별 편집 가이드, index/log 타입별 분류 절차 명시.
- **신규 TODO**:
  - `concepts/multi-agent-orchestration.md`가 내용 70% OMC 특화 상태 → 향후 순수 concept판과 project-internal판으로 분리 필요

## 2026-04-09 (저녁)
- **Ingest**: `yeachan-heo/oh-my-claudecode` GitHub 프로젝트 전체 구조 위키화
  - 소스 URL: https://github.com/yeachan-heo/oh-my-claudecode
  - 수집 범위: README.md, AGENTS.md, CLAUDE.md, docs/ARCHITECTURE.md, docs/FEATURES.md, docs/HOOKS.md, docs/GETTING-STARTED.md, docs/REFERENCE.md, docs/TOOLS.md
  - raw 파일 9개:
    - `raw/2026-04-09-omc-README.md`
    - `raw/2026-04-09-omc-AGENTS.md`
    - `raw/2026-04-09-omc-CLAUDE.md`
    - `raw/2026-04-09-omc-ARCHITECTURE.md`
    - `raw/2026-04-09-omc-FEATURES.md`
    - `raw/2026-04-09-omc-HOOKS.md`
    - `raw/2026-04-09-omc-GETTING-STARTED.md`
    - `raw/2026-04-09-omc-REFERENCE.md`
    - `raw/2026-04-09-omc-TOOLS.md`
- **생성된 페이지 (16개)**:
  - 메인 허브: `wiki/applications/oh-my-claudecode.md`
  - Concepts (7개):
    - `wiki/concepts/multi-agent-orchestration.md`
    - `wiki/concepts/omc-magic-keyword.md`
    - `wiki/concepts/omc-skill-layering.md`
    - `wiki/concepts/omc-model-routing.md`
    - `wiki/concepts/omc-hook-system.md`
    - `wiki/concepts/omc-state-management.md`
    - `wiki/concepts/omc-delegation-categories.md`
  - Agents (1개):
    - `wiki/agents/omc-agent-catalog.md` (19개 에이전트, 4개 레인)
  - Tooling (8개):
    - `wiki/tooling/omc-execution-modes.md`
    - `wiki/tooling/omc-autopilot.md`
    - `wiki/tooling/omc-ralph-mode.md`
    - `wiki/tooling/omc-ultrawork.md`
    - `wiki/tooling/omc-team-mode.md`
    - `wiki/tooling/omc-ccg.md`
    - `wiki/tooling/omc-ralplan.md`
    - `wiki/tooling/omc-deep-interview.md`
- **갱신된 페이지**:
  - `index.md` — Tooling 섹션에 OMC 8개 페이지 추가
- **발견된 지식 갭**:
  - OMC Learner / Skill 학습 시스템 별도 페이지
  - OMC Notepad Wisdom System 상세
  - OMC MCP 툴 카탈로그
  - OMC Ecomode / Ultraqa / Visual-Verdict / Web-Clone 개별 페이지
  - OMC autoresearch runtime 상세
  - OMC HUD statusline / Notification 통합 (Telegram/Discord/Slack/OpenClaw)

## 2026-04-09
- **Ingest**: Simon Willison의 "Agentic Engineering Patterns" 가이드 전체 수집 및 컴파일
  - 소스 URL: https://simonwillison.net/guides/agentic-engineering-patterns
  - 수집 범위: 메인 가이드 + 모든 서브 챕터 14개 + 2026-02-23 소개 포스트
  - raw 파일: `raw/2026-04-09-simon-willison-agentic-engineering-patterns.md`
- **생성된 페이지 (18개)**:
  - `wiki/applications/agentic-engineering-guide.md` (가이드 전체 맵)
  - `wiki/concepts/agentic-engineering.md`
  - `wiki/concepts/vibe-coding.md`
  - `wiki/concepts/coding-agent.md`
  - `wiki/concepts/code-is-cheap.md`
  - `wiki/concepts/hoard-things-you-know-how-to-do.md`
  - `wiki/concepts/better-code-with-agents.md`
  - `wiki/concepts/anti-patterns.md`
  - `wiki/concepts/cognitive-debt.md`
  - `wiki/agents/how-coding-agents-work.md`
  - `wiki/agents/subagents.md`
  - `wiki/applications/red-green-tdd.md`
  - `wiki/applications/first-run-the-tests.md`
  - `wiki/applications/agentic-manual-testing.md`
  - `wiki/applications/linear-walkthroughs.md`
  - `wiki/applications/interactive-explanations.md`
  - `wiki/applications/gif-optimization-case-study.md`
  - `wiki/applications/prompts-library.md`
  - `wiki/tooling/claude-code.md`
  - `wiki/tooling/git-with-coding-agents.md`
  - `wiki/tooling/browser-automation-agents.md`
- **갱신된 페이지**:
  - `index.md` — agents, applications, tooling, concepts 카테고리 전면 갱신, TODO 섹션 추가
- **발견된 지식 갭**:
  - Max Woolf 원본 글 (word cloud 프롬프트 출처)
  - Every의 Compound Engineering Loop 원본 방법론
  - Karpathy의 "vibe coding" 원본 정의
  - OpenAI Codex, Gemini CLI/Jules 개별 페이지

## 2026-04-06
- 위키 초기 구조 생성 (CLAUDE.md, index.md, log.md)
- 카테고리 10개 정의: foundations, architectures, training, inference, rag, agents, applications, papers, tooling, concepts
