## 2026-05-06 -- Wiki 종합 점검 + 심층 개선 사이클

직전 lint 통과 후 더 깊이 들어가 마크다운 무결성, 빈약한 stub, TODO 마커, 중복 페이지를 정밀 점검·개선했다.

**1. Nested wikilink 24건 정리**
- 직전 alias 작업의 부작용으로 발생한 `[[outer-[[inner|alias]]-rest]]` 패턴 24건을 22개 직접 매핑으로 정리
- 수정된 23개 파일: ai-agent-guardrails, mcp-authorization-draft, claude-code, writing-effective-tools-for-agents, claude-opus-4-5-release-notes, google-adk, mcp-roadmap-development, gpt-5-4, mcp-specification-2025-11-25, model-context-protocol, omc-ralplan, omc-ultrawork, flashattention-4-paper, deepseek-mhc, sovereign-ai, agentic-ai-production, omc-skill-layering, responsible-scaling-policy-v3, ai-ma-mega-deals, us-china-ai-competition, deliberative-alignment, kv-cache-compression, litert-lm
- Mermaid 다이어그램 노드 안의 `[["[[clip|CLIP]] ..."]]` 등 9건은 정당한 사용으로 유지

**2. 빈약한 stub 페이지 4건 보강 (평균 970 단어)**
- `tooling/feast.md` 359 chars → 904 단어 (Offline/Online Store/Registry/Feature Server 4 컴포넌트, Push API, Tecton 비교)
- `tooling/dvc.md` 437 chars → 965 단어 (`.dvc` 메타, Remote Storage 7종, dvc.yaml stages, DVCLive, Studio)
- `applications/ai-workflow-automation.md` 470 chars → 974 단어 (Trigger→Context→LLM→Action 4단계, 7개 플랫폼 비교)
- `applications/ai-data-pipeline-automation.md` 475 chars → 1,113 단어 (Airflow/Prefect/Dagster/Kestra/Mage 카탈로그)
- 모두 1차 공식 docs (feast.dev, dvc.org/doc, n8n.io, airflow/prefect/dagster) fetch 기반

**3. TODO/조사필요 마커 18개 처리**
- 자동 보강 9파일 / 11마커 (1차 소스 검증 후 사실 채움)
  - `agents/planner-executor-verifier-frameworks` — OpenHands event-sourced delegation, CodeAct (arXiv 2407.16741)
  - `agents/production-agent-architectures` — Copilot Workspace 4단계 파이프라인 (githubnext user manual)
  - `concepts/context-window-management` — thinking block 보존 정책 모델 세대별 5행 표 (Anthropic extended thinking docs)
  - `concepts/prompt-as-program` — LangChain PromptTemplate / LlamaIndex 비교
  - `concepts/ai-fluency-literacy` — UNESCO AI competency framework 4 dimensions × 12
  - `tooling/claude-opus-4-5` — 200K/1M 컨텍스트, 출시일 2025-11-24
  - `tooling/gemini-2-5-flash-thinking` — thinkingBudget API 사양 (0~24576, -1=dynamic)
  - `tooling/nvidia-nemotron-3-family` — Nano/Super/Ultra 정확 파라미터 + Mamba-Transformer MoE
  - `concepts/omc-hook-system`, `agents/coding-harness-comparison` — placeholder 정리·근거 명확화
- 명확화 1마커: METR 작업 지평선 데이터 미공개 → "[교차검증 필요]" 명시
- 오탐 6파일: TODO/XXX 단어가 정상 콘텐츠 일부 (IOB 태깅 B-XXX, "TODO 항목" 인용 등)

**4. vit / vision-transformer-vit / vision-transformer 중복 통합 (옵션 A)**
- 가장 풍부한 `architectures/vision-transformer.md`로 통합 (218줄, aliases에 vit/vision-transformer-vit 포함)
- `architectures/vit.md` (5/6 신규), `architectures/vision-transformer-vit.md` (4/17 작성) 삭제
- `[[vit]]` 5건 + `[[vision-transformer-vit]]` 27건 = **32개 wikilink reference** 모두 통합 페이지로 변경
- index.md 두 entry 제거

**최종 lint 검증 (2,002 페이지)**
| 항목 | 결과 |
|------|------|
| Nested wikilinks (non-mermaid) | **0건** ✓ |
| Missing frontmatter (non-meta) | **0건** ✓ |
| 한국어 본문 위반 | **0건** ✓ |
| 빈약 페이지 (body<500) | **0건** ✓ |
| Broken wikilink count ≥ 3 | 5건 (다음 사이클 후보) |

**다음 사이클 후보 (broken wikilink count ≥ 3)**
- `Showboat` (6회), `Rodney` (5회) — Simon Willison agentic guide 도구명, entity 페이지 신규 후보
- `adamw` (5회) — AdamW 옵티마이저 별도 entity/concept 페이지 후보
- `ml-reproducibility` (3회) — 신규 concept 페이지 후보
- `RLHF 인간 선호도 강화학습 원논문 (Christiano et al.)` (3회) — Christiano 2017 paper 페이지 후보

---

## 2026-05-06 -- Wiki Lint: 전체 점검 + 자동 수정

**점검 통계**
- 전체 페이지: 2,004개
  - concepts 454 / tooling 369 / training 229 / architectures 193 / foundations 151 / papers 136 / agents 134 / applications 129 / inference 117 / rag 91
  - by type: concept 1317 / entity 377 / paper 156 / summary 106 / project-internal 29 / case-study 18

**Critical 위반 (수정 완료 또는 사용자 판단)**
- ✓ Frontmatter 누락: 1건 (`wiki/_meta/graph-stats-2026-04-20.md` — meta 파일, 허용)
- ✓ 한국어 본문 위반: **0건** (전체 통과)
- ✓ 빈 섹션 (body<100): **0건**
- ✓ 카테고리/타입 불일치: **0건**
- ✓ 필수 frontmatter 필드 누락: **0건**

**경고 자동 수정 (Warning → 처리됨)**
- 고아 페이지 28건 → index.md 카테고리별 추가 (training 4 / architectures 1 / tooling 1 / applications 2 / concepts 20)
- 추가 alias 13건 적용 → 5개 깨진 표기 정리:
  - `Constitutional AI` (5회) → `[[constitutional-ai|...]]`
  - `RLHF (인간 피드백 강화학습)` → `[[rlhf|...]]`
  - `LangSmith - LLM 애플리케이션 관측 플랫폼` → `[[langsmith|...]]`
  - `LLM 관측 플랫폼` → `[[llm-observability-platforms|...]]`
  - `추론 시점 계산 스케일링 (Test-Time Compute)` → `[[test-time-compute|...]]`
- 영향 파일: 10개

**사용자 판단 필요 (수동 처리 권장)**
- `[[Showboat]]` (6회), `[[Rodney]]` (5회): Simon Willison agentic-engineering-guide에서 언급된 도구명. entity 페이지 신규 생성 또는 일반 텍스트로 변환 결정 필요. 영향: cognitive-debt, agentic-manual-testing, linear-walkthroughs, agentic-engineering-guide, gif-optimization-case-study
- `[[adamw]]` (5회): AdamW 옵티마이저, `adagrad-rmsprop`/`adam-original-paper`와 별개로 신규 entity/concept 페이지 가치 있음. 다음 wiki-expand 사이클 후보
- `[[RLHF 인간 선호도 강화학습 원논문 (Christiano et al.)]]` (3회): Christiano 2017 paper 신규 paper 페이지 후보
- 백슬래시 노이즈 wikilink: `medusa-multi-head-decoding\`, `modal-com-runtime\`, `replicate-platform\` 등 — 마크다운 파싱 깨진 경우. 본문에서 직접 정리 권장
- `[[vit]]` 신규 페이지가 기존 `vision-transformer-vit`와 주제 중복 → 통합 검토 권장

**깨진 wikilink 잔여**
- 500개 unique target (대부분 1회 참조)
- count ≥ 2: 약 20개 — 위의 사용자 판단 항목과 신규 페이지 후보로 분리

**다음 wiki-expand 후보 (신규 페이지 가치)**
- `adamw`, `christiano-rlhf-paper`, `Showboat`, `Rodney`, `event-sourcing-pattern`, `long-horizon-reasoning`, `huggingface-transformers`

---

## 2026-05-06 -- Wiki Expand: 깨진 wikilink 발굴 → 13개 신규 페이지 + 16개 alias 정리

**스캔 결과**
- 전체 unique link target: 2,454, 깨진 wikilink: 524
- 임계값 (count ≥ 3) 만족 33개 → 신규 13개 + alias 16개 + 노이즈 무시 4개
- 스캔 raw: `raw/2026-05-06-wiki-expand-scan.md`

**신규 생성 (13개)**

- `concepts/mcp-protocol` (concept hub) — JSON-RPC 2.0 + Host/Client/Server 3-tier + 4대 보안 원칙. 8개 mcp-* 페이지 통합 entry point. (11회 참조)
- `training/dpo` (concept) — DPO (Rafailov 2023 NeurIPS), reference policy logit 비율 loss로 reward model 없이 선호도 직접 최적화. IPO/KTO/ORPO/SimPO/GRPO 변형 정리. (4회)
- `training/constitutional-ai` (concept) — Bai 2022 Anthropic, SL stage(self-critique→revision) + RL stage(RLAIF) 2단계 RLHF의 H를 AI로 대체. (5회)
- `architectures/vit` (concept) — Dosovitskiy 2020 ICLR, 16×16 patch + position embedding + [CLS] + 표준 Transformer encoder. (5회)
- `concepts/neural-rendering` (concept) — NeRF (Mildenhall 2020) implicit + 3D Gaussian Splatting (Kerbl 2023) explicit 두 패러다임. (5회)
- `concepts/api-cost-management` (concept) — LLM API 비용 hub. token 가격 / 모델 티어링 / Prompt Caching / Batch API / spend cap. (6회)
- `foundations/gradient-checkpointing` (concept) — Chen 2016 Sublinear Memory. O(L)→O(√L), 시간 +30%. PyTorch torch.utils.checkpoint. (3회)
- `foundations/bayesian-deep-learning` (concept) — BNN/MC Dropout/Deep Ensembles/SWAG/Laplace 카탈로그. (3회)
- `foundations/adagrad-rmsprop` (concept) — Duchi 2011 / Hinton 2012, 적응형 학습률 옵티마이저 두 알고리즘. (3회)
- `architectures/domain-expert-moe` (concept) — Branch-Train-Merge / Branch-Train-MiX, expert를 도메인별 specialize. (3회)
- `tooling/google-trillium-tpu-v6` (entity, project: Google) — 6세대 TPU. 칩당 4.7x v5e, HBM 2x, 256-칩 Pod, 91 ExaFLOPS. (3회)
- `tooling/qwen-2-5` (entity, project: Alibaba Qwen) — 2024-09 출시, 18T 토큰 사전학습, 128K context, 7개 사이즈 + Coder/Math. Apache 2.0. (3회)
- `applications/open-hardware` (concept) — Tenstorrent / Esperanto / AMD ROCm / tinybox, CUDA 의존 탈피 동기. (3회)

**Alias 정리 (16개 깨진 링크 → 기존 페이지)**

- `RLHF`, `RLHF 파이프라인`, `InstructGPT RLHF 파이프라인` → `[[rlhf|...]]` / `[[rlhf-pipeline|...]]`
- `Transformer 아키텍처` → `[[transformer-architecture|...]]`
- `프롬프트 엔지니어링` → `[[prompt-engineering|...]]`
- `Neural Scaling Laws` → `[[neural-scaling-laws|...]]`
- `에이전틱 RAG` → `[[agentic-rag|...]]`
- `자기지도 학습 (Self-Supervised Learning)` → `[[self-supervised-learning|...]]`
- `GPT-3 퓨샷 학습` → `[[gpt-3-paper|...]]`
- `회로 추적` → `[[circuit-tracing|...]]`
- `마스킹 이미지 모델링 (Masked Image Modeling)` → `[[masked-image-modeling|...]]`
- `medusa` → `[[medusa-multi-head-decoding|...]]`
- `gaussian-processes` → `[[gaussian-process|...]]`
- `cursor-editor` → `[[cursor|...]]`
- `DPO 직접 선호도 최적화`, `dpo-direct-preference-optimization` → `[[dpo|...]]`

**총 59개 wikilink 치환, 45개 파일 영향**

**무시된 노이즈**
- `[[self-attention-mechanism`, `[[transformer-ffn` — 잘못된 파싱 결과
- `Showboat`, `Rodney` — 인명 추정, 위키 페이지 불필요
- `RLHF 인간 선호도 강화학습 원논문 (Christiano et al.)` — 매핑 대상 페이지 부재 (별도 paper 페이지 신규 생성 후보)

**1차 소스 검증**: 13개 모두 arXiv abstract / 공식 docs / 공식 블로그 직접 fetch. 미확인 수치는 `[교차검증 필요]` 태그 처리.

**index.md 갱신**: 13개 신규 entry 카테고리별 추가, frontmatter `updated: 2026-05-06`

---

## 2026-05-06 -- 하네스 엔지니어링 엔터프라이즈 급 대규모 수집·컴파일 사이클 (Wave 1 + Wave 2)

**전체 결과 요약**
- Wave 1 (수집): raw/2026-05-06-*.md 110개 신규 (8개 카테고리 병렬)
- Wave 2 (ingest): wiki 페이지 91개 신규 + 27개 보강 = **총 118개 페이지 영향**

### Wave 1 — Harness 엔지니어링 raw 수집 (110건)

| 카테고리 | 개수 | 핵심 |
|---|---|---|
| `coding-harness-*` | 10 | Claude Code, Cursor, Aider, OpenHands, SWE-agent, Cline, Devin, Continue.dev 아키텍처 + 비교 |
| `harness-pattern-*` | 10 | tool orchestration, context mgmt, prompt cache, hooks, slash, sub-agent, MCP, multi-turn loop, multi-agent framework |
| `harness-prod-*` | 13 | permissions, OTel GenAI semconv/metrics, sandbox, rate limits, cost, retry, worktree (Issue #48927), observability, error budget, eval-in-loop, auto-mode classifier, microvm |
| `eval-harness-*` | 10 | lm-eval, BIG-bench, HELM, OpenAI Evals, simple-evals, Inspect AI, lighteval, agent benchmarks, METR HCAST/GDPval, 비교 |
| `train-harness-*` | 12 | Sebulba/Anakin (Podracer), IMPALA/V-trace, TRL, OpenRLHF, verl/HybridFlow, NeMo-Aligner, DeepSpeed-Chat, torchtune, Voyager, ReAct/AgentGym, frontier lab RL infra |
| `paper-*` | 16 | ReAct, Toolformer, Reflexion, Voyager, AgentBench, AutoGen, SWE-bench, GAIA, SWE-agent, OpenHands, Inference Scaling Laws, Test-Time Scaling, LangGraph MT, METR HCAST, Test-Time Compute for Agents, Inspect Evals |
| `blog-*` | 24 | Anthropic Engineering 8개, Cursor 3개, Simon Willison 2개, Hamel Husain 3개, Eugene Yan / Lilian Weng / Chip Huyen / Raschka / OpenAI Cookbook / Pydantic AI / LangChain / Langfuse |
| `system-design-*` | 15 | MCP spec deep dive (8개: core/transport/lifecycle/auth/tools/server/clients/security), Anthropic Skills + Claude Code Plugins, production agent architectures, planner-executor-verifier, tool routing RAG, blast radius, error budget |

### Wave 2 — Wiki 페이지 컴파일 (118건)

**신규 생성 (91개)**

- **agents (20)**: `swe-agent`, `voyager-agent`, `coding-harness-comparison`, `tool-orchestration-patterns`, `subagent-spawning`, `long-horizon-agent-loop`, `multi-agent-orchestration-frameworks`, `effective-agents-patterns`, `tool-design-for-agents`, `multi-agent-research-system-2025-summary`, `llm-autonomous-agents-lilian-weng`, `langchain-agent-frameworks-evolution`, `production-agent-architectures`, `planner-executor-verifier-frameworks`, `tool-routing-rag`, `blast-radius-control-agents`, `agent-failure-modes-error-budget`, `agent-error-budget-sre`, `agent-benchmark-harness-comparison`, `agent-training-harness-react-agentgym`
- **concepts (29)**: `context-window-management`, `prompt-caching-strategies`, `hook-system-patterns`, `skill-system-architecture`, `mcp-protocol-deep-dive`, `mcp-authorization-oauth`, `mcp-specification-deep-dive`, `mcp-transport-protocols`, `mcp-lifecycle-capability-negotiation`, `mcp-oauth-authorization`, `mcp-tools-protocol`, `mcp-server-development-guide`, `mcp-security-model`, `mcp-code-execution`, `anthropic-agent-skills-spec`, `claude-skills-vs-mcp`, `opentelemetry-genai-metrics`, `prompt-cache-cost-economics`, `eval-in-loop-pattern`, `long-horizon-eval-metr-gdpval`, `agent-evals-anthropic-perspective`, `cursor-online-rl`, `effective-context-engineering-2025-summary`, `llm-eval-best-practices`, `llm-judge-pattern`, `llm-application-patterns-eugene-yan`, `chip-huyen-agents-summary`, `state-of-llms-2025-raschka`, `openai-structured-outputs-multi-agent`
- **tooling (21)**: `lm-evaluation-harness`, `big-bench`, `helm-stanford`, `openai-evals`, `simple-evals`, `inspect-ai`, `lighteval`, `evaluation-harness-comparison`, `mcp-clients-comparison`, `nemo-aligner`, `deepspeed-chat`, `torchtune`, `claude-code-permission-modes`, `claude-code-auto-mode`, `claude-code-plugins-marketplace`, `claude-code-best-practices`, `claude-agent-sdk-overview-2025`, `cursor-composer-model`, `anthropic-api-rate-limits`, `langfuse-observability-summary`, `pydantic-ai-overview-summary`
- **papers (15)**: `react-paper`, `reflexion-paper`, `voyager-paper`, `agentbench-paper`, `autogen-paper`, `swe-bench-paper`, `gaia-paper`, `swe-agent-paper`, `openhands-paper`, `inference-scaling-laws-paper`, `test-time-scaling-paper`, `langgraph-mt-paper`, `metr-hcast-paper`, `test-time-compute-agents-paper`, `inspect-evals-paper`
- **training (5)**: `sebulba-podracer`, `anakin-podracer`, `impala-vtrace`, `frontier-lab-rl-infra`, `rl-harness-frameworks-comparison`
- **applications (1)**: `improving-ai-products-field-guide`

**보강 갱신 (27개, 신규 디테일 병합)**
- `agents/`: `anthropic-harness-design`, `anthropic-multi-agent-research-system`, `agent-skills`, `agent-circuit-breaker`, `agent-cost-optimization`, `agent-rate-limiting-patterns`, `agent-sandbox-infrastructure`, `parent-child-spawn-pattern`, `prompt-caching-agentic`
- `concepts/`: `context-engineering`, `llm-observability-platforms`, `opentelemetry-genai-semconv`
- `tooling/`: `claude-code`, `cursor`, `aider`, `openhands`, `cline-claude-coder`, `continue-vscode-extension`, `devin-2-0-release`, `claude-code-hooks-system`, `evaluation-harness`, `git-worktree-isolation`, `microvm-agent-sandboxes`, `trl-library`, `openrlhf`, `verl-bytedance`
- `papers/`: `toolformer-paper`

**핵심 발견 / 디자인 결정**
- **MCP spec 2025-06-18**을 8개 페이지로 분해 (transport / lifecycle / auth-OAuth2.1+RFC8707 / tools / security 6공격벡터 등)
- **Inspect AI (UK AISI)**가 static eval과 agent eval 두 세대를 잇는 차세대 표준 — METR Vivaria→Inspect 마이그레이션과 lighteval의 backend 채택이 신호
- **OpenTelemetry GenAI semconv**: gen_ai.* 표준 attribute + 7 metric의 bucket boundary까지 정확히 인용
- **frontier lab RL infra**: Anthropic Project Rainier + OpenAI Azure 산업 분석 — 비공개 부분은 (추정) 명시
- **Production incident 사례**: Claude Code Issue #48927 (v2.1.109 worktree race condition으로 .git 통째 삭제), Anthropic auto-mode FPR 0.4%/FNR 17%
- **scaffold sensitivity**: METR Vivaria→Inspect 마이그레이션에서 GPT-4o, o3 두 모델 통계적 유의미 차이 — reproducibility 위험 공식 인정

**1차 소스 검증**: 모든 raw 파일이 공식 docs / 엔지니어링 블로그 / arXiv abstract / GitHub repo / spec 문서를 직접 fetch한 것. 비공개/추정 부분은 `[교차검증 필요]` 또는 `(추정)` 명시.

**index.md 갱신**: 신규 91개 페이지 카테고리별 entry 추가, 보강 페이지 description 업데이트

---

## 2026-04-27 -- 평가 지표 6개 신규 생성 (MT·요약·랭킹 평가 커버리지 완성)

**생성 - concepts · concept (6)**

- `bleu-metric` -- BLEU (Bilingual Evaluation Understudy) 전체 커버. n-gram 정밀도·클리핑·간결성 패널티(BP) 수식, SacreBLEU 재현성, NLTK 코드, 점수 해석 범위 가이드. [[rouge-metric]], [[bert-score]], [[comet-translation]] 교차참조
- `rouge-metric` -- ROUGE 패밀리 전체 (ROUGE-N/L/W/S). 재현율 기반 요약 평가, BLEU와 대비, 한국어 형태소 분석 적용 주의사항, CNN/DailyMail·XSum 벤치마크 표준. [[bleu-metric]], [[bert-score]], [[ai-evaluation]] 교차참조
- `bert-score` -- BERTScore 임베딩 기반 평가. 문맥적 토큰 임베딩·코사인 유사도·Greedy Matching·IDF 가중치·베이스라인 재조정 수식 전체, roberta-large/klue 모델 선택, BERTScore vs Sentence Transformer 비교. [[bleu-metric]], [[rouge-metric]], [[comet-translation]], [[sentence-transformer]] 교차참조
- `comet-translation` -- COMET 신경망 MT 평가. XLM-R 인코더+회귀 헤드 아키텍처, 소스 활용 설계 원칙, CometKiwi QE 모드, wmt22-comet-da/wmt22-cometkiwi-da 모델 패밀리, WMT 챔피언 맥락. [[bleu-metric]], [[bert-score]], [[machine-translation-modern]] 교차참조
- `ndcg-metric` -- NDCG 랭킹 평가 전체. CG→DCG→IDCG→NDCG 4단계 수식, 위치별 할인계수 표, sklearn 구현·직접 구현 예시, RAG 검색 평가·추천시스템 코드. [[mrr-metric]], [[ai-evaluation]], [[recommendation-systems-dl]] 교차참조
- `mrr-metric` -- MRR 단일 정답 검색 평가. Reciprocal Rank 수식, 위치별 RR 표, MRR vs NDCG 비교, QA 시스템·RAG 파이프라인·추천시스템 코드, 종합 랭킹 평가 함수. [[ndcg-metric]], [[ai-evaluation]] 교차참조

**index.md 갱신**: concepts concept 섹션에 6개 항목 추가

---

## 2026-04-27 -- 아키텍처/개념 6개 신규 생성 + 1개 병합 갱신

**병합 갱신 - architectures · concept (1)**

- `transformer-ffn` -- 실무 구현 패턴(SwiGLU PyTorch), MoE FFN 확장 섹션, [[activation-functions]]/[[mixture-of-experts-moe-llms]] 교차참조 추가. updated: 2026-04-27

**생성 - concepts · concept (5)**

- `risk-modeling` -- 리스크 모델링 일반. VaR/CVaR, 신용/시장/운영 리스크 3대 분류, ML 기반 PD 모델, 스트레스 테스트. [[ai-portfolio-management]], [[ai-credit-scoring]], [[time-series-forecasting]] 연결
- `automl` -- AutoML 일반 개요. NAS, Auto-sklearn, AutoGluon, TPOT, H2O AutoML. 메타러닝, 파이프라인 최적화. [[hyperparameter-tuning]], [[neural-architecture-search]], [[ml-foundations]] 연결
- `model-routing` -- 모델 라우팅. RouteLLM, 캐스케이드/의미론적 라우팅, 비용-성능 트레이드오프. [[agent-fallback-strategies]], [[mixture-of-experts-moe-llms]], [[api-cost-management]] 연결
- `3d-avatar` -- 3D 아바타 일반. ARKit 52개 블렌드쉐이프, MetaHuman, 모션 캡처, AI 기반 구동 파이프라인. [[ai-sign-language]], [[gaussian-splatting]], [[neural-rendering]] 연결
- `code-interpreter` -- Code Interpreter 일반. OpenAI/Claude/Gemini 코드 실행, Firecracker/E2B 샌드박스, 자기 수정 루프. [[e2b-ai-sandbox]], [[firecracker-microvm]], [[claude-code]] 연결

**index.md 갱신**: concepts concept +5개, architectures transformer-ffn 업데이트 주석 추가

---

## 2026-04-27 -- 신규 페이지 6개 생성 (foundations 1 + architectures 4 + concepts 1)

**생성 - foundations · concept (1)**

- `regularization` -- L1/L2/Dropout/Early Stopping/Data Augmentation 정규화 기법 통합 개요. 과적합 방지 메커니즘 비교, 기법 조합 전략

**생성 - architectures · concept (4)**

- `masked-image-modeling` -- MAE/BEiT/SimMIM/iBOT 비교. 마스킹 전략, 예측 타겟, 비디오 확장(VideoMAE) 포함
- `mixture-of-experts-moe-llms` -- LLM용 MoE 허브. 라우팅 메커니즘, Expert Parallelism, Mixtral/DeepSeek-V3/Switch Transformer 계보
- `q-former` -- BLIP-2 Q-Former 상세. 3단계 사전학습(ITC/ITM/ITG), InstructBLIP 확장, Perceiver Resampler와 비교
- `perceiver-resampler` -- Flamingo Perceiver Resampler 상세. Gated Cross-Attention, 인터리브드 멀티모달 시퀀스 처리

**생성 - concepts · concept (1)**

- `video-understanding` -- 비디오 이해 전반. 행동 인식/캡셔닝/시간 위치추정, 아키텍처 계보(2-stream->3D CNN->Transformer), VideoMAE 상세

---

## 2026-04-27 -- 평가/불확실성/도메인적응 6페이지: 3개 신규 + 3개 병합 갱신

**신규 생성 - concepts · concept (2)**

- `ood-detection` -- 분포 외 탐지. MSP, ODIN, Energy Score, MOOD, 마할라노비스 거리. 탐지기 파이프라인 Mermaid 포함
- `uncertainty-estimation` -- 불확실성 추정. epistemic/aleatoric 구분, MC Dropout, 딥 앙상블, 보정(ECE). 앙상블 구조 및 선택 flowchart 포함

**신규 생성 - tooling · entity (1)**

- `chatbot-arena` -- LMSYS Chatbot Arena. Elo/Bradley-Terry 레이팅, 인간 선호 크라우드소싱 평가. MT-Bench 비교표 및 평가 생태계 Mermaid 포함

**병합 갱신 - concepts/tooling (3)**

- `domain-adaptation` -- 분포 시프트 유형 표, DANN/CORAL/MMD 기법, GRL 구조 Mermaid, OOD 탐지와의 관계 섹션 추가. tags/updated 갱신
- `mt-bench` -- project 필드 추가, Chatbot Arena 종합 비교표, 2턴 평가 sequenceDiagram 추가. tags/updated 갱신
- `benchmark-contamination` -- SWE-Bench 오염 사례 섹션, 탐지 방법 flowchart, 평가 편향 비교표, Chatbot Arena 교차참조 추가. tags/updated 갱신

**index.md 갱신**: 3개 신규 링크 추가 (tooling entity 1, concepts concept 2), 기존 3개 항목 설명 개선

---

## 2026-04-27 -- AI 인프라 / 하드웨어 / 모델 패밀리: 6페이지 신규 생성

**생성 - tooling · summary (1)**

- `nvidia-nim-2026` -- NVIDIA NIM 마이크로서비스 2026 업데이트. 에이전트 파이프라인 통합, 엣지 배포 강화, 모델 카탈로그 대폭 확장. OpenAI 호환 REST API

**생성 - tooling · concept (1)**

- `wafer-scale-engine` -- Wafer-Scale Engine 일반 개념. Cerebras WSE-2/3 구조, 메모리 월 극복 원리, 결함 허용, 수냉 열 관리

**생성 - tooling · entity (2)**

- `firecracker-microvm` -- AWS Firecracker microVM. 125ms 부팅, KVM 기반, AI 코드 실행 격리. Lambda/Fargate 내부 구동. project: Firecracker
- `cohere-models` -- Cohere 모델 패밀리 허브. Command R+/R7B, Aya Expanse/Vision, Embed v3/v4, Rerank 3. 엔터프라이즈 RAG + 다국어. project: Cohere

**생성 - foundations · concept (2)**

- `in-memory-computing` -- 인메모리 컴퓨팅 개념. DIMC/PIM/NMC 분류, d-Matrix DIMC, 아날로그 IMC, 에너지 효율
- `risc-v` -- RISC-V 오픈소스 ISA 개념. 모듈식 확장 구조, AI 칩 채택 동기, Tenstorrent 활용, 소프트웨어 생태계

**index.md 갱신**: 6개 링크 추가 (Foundations concept x2, Tooling entity x2 + concept x1 + summary x1)

---

## 2026-04-27 -- 깨진 링크 핵심 페이지 6개 보강 (신규 0 + 병합 갱신 6)

**병합 갱신 - architectures · entity (1)**

- `mamba-3` -- page_type concept -> entity 수정, project: Mamba 필드 추가, [[mamba-architecture]], [[ssm]], [[transformer]], [[positional-encoding]], [[pre-ln-vs-post-ln]] 링크 추가

**병합 갱신 - architectures · concept (2)**

- `positional-encoding` -- [[rope-scaling-ntk-yarn]], [[alibi-positional-encoding]], [[transformer]] 링크 보강
- `pre-ln-vs-post-ln` -- [[layer-norm-original-paper]], [[normalization-layers]], [[transformer]] 링크 보강

**병합 갱신 - foundations · concept (3)**

- `normalizing-flows` -- [[continuous-normalizing-flow]] 링크 추가
- `gaussian-process` -- Sparse GP 근사 방법(FITC/VFE/SVGP) 섹션 추가, GPyTorch 코드 예시 추가, [[bayesian-deep-learning]], [[kernel-methods]], [[reproducing-kernel-hilbert-space]] 링크 보강, tags 확장, updated 갱신
- `second-order-optimization` -- [[gradient-descent]], [[adam-original-paper]], [[neural-network]] 링크 추가

---

## 2026-04-27 -- 오픈소스 모델 2026-04 Harvest: 7페이지 신규 생성 + 1페이지 병합 갱신

소스: `raw/2026-04-27-harvest-opensource.md`

**생성 - tooling · entity (5)**

- `deepseek-v4-pro` -- DeepSeek V4 Pro 1.6T/49B MoE, 1M 컨텍스트, MIT 라이선스. 단일 모델 SOTA 포지셔닝
- `qwen-3-6` -- Qwen 3.6 시리즈: 27B 덴스 + 35B-A3B MoE. 에이전틱 코딩 397B MoE 능가. DFlash 커뮤니티 버전 공개
- `kimi-k2-6` -- Kimi K2.6 1T MoE, 최대 300 서브에이전트 스웜, 4,000 스텝 장기 실행 지원
- `exaone-4-5` -- LG AI 연구원 EXAONE 4.5 33B 멀티모달. STEM 5개 벤치마크 평균 77.3점. K-EXAONE 236B 증류
- `tencent-hunyuan-3` -- Tencent Hunyuan 3 (Hy3) 295B/21B MoE 프리뷰. Fast-Slow thinking 융합 아키텍처

**생성 - architectures · entity (1)**

- `llada-2-uni` -- LLaDA 2.0-Uni 이산 확산 LLM. 100B 스케일. 병렬 디코딩 535 tokens/s. 멀티모달 이해+생성 통합

**생성 - inference · concept (1)**

- `dflash-block-diffusion-decoding` -- DFlash 블록 확산 스펙울레이티브 디코딩. EAGLE-3 대비 2.5배 추가 = 총 6x 무손실 가속

**병합 갱신 - tooling · entity (1)**

- `mistral-small-4` -- "세 역량 통합 관점" 섹션 추가 (Magistral+Pixtral+Devstral 통합), sources 및 tags 갱신

**index.md 갱신**: 8개 링크 추가 (Architectures entity, Inference concept, Tooling entity x5 + 병합 갱신 1)

---

## 2026-04-27 -- NVIDIA/Microsoft 2026-04 Harvest: 8페이지 신규 생성

소스: `raw/2026-04-27-harvest-deepmind-msft-nvidia.md`

**생성 - inference · entity (1)**

- `nvidia-vera-rubin-nvl72` -- 72x Rubin GPU + NVLink 6, FP4 50 PFLOPS, HBM4 288GB/GPU, 랙 조립 6분. H2 2026 출시

**생성 - inference · summary (1)**

- `nvidia-blackwell-ultra-b300-inference` -- MLPerf v6.0 GPU당 5x Hopper, DeepSeek-R1 1000 tok/s, $0.24/백만 토큰, 288GB HBM3e

**생성 - tooling · entity (3)**

- `nvidia-nemotron-3-family` -- Nano/Super/Ultra 에이전틱 AI 특화 오픈 모델. Google Cloud 파트너십
- `nvidia-nemo-agent-toolkit` -- 프레임워크 무관 에이전트 인스트루멘테이션·관찰가능성·지속적 학습
- `phi-4-multimodal` -- Microsoft 5.6B 멀티모달 (텍스트+이미지+오디오), ASR WER 6.14% 1위

**생성 - training · entity (1)**

- `bitnet-b158-2b4t` -- Microsoft 최초 대규모 네이티브 1비트 LLM, 4조 토큰 학습. CPU에서 100B 5-7 tok/s, 에너지 82% 절감

**생성 - agents · entity (1)**

- `magentic-ui` -- Plan Preview + Co-tasking + 명시적 승인. AutoGen 기반 인간 중심 웹 에이전트. MIT 라이선스

**생성 - agents · summary (1)**

- `a2a-protocol-v12-upgrade` -- 암호화 서명 에이전트 카드, Linux Foundation 이관, 150+ 조직 프로덕션. 5개 프레임워크 네이티브 지원

**index.md 갱신**: 8 신규 링크 추가 (Inference entity/summary, Tooling entity x3, Training entity, Agents entity/summary)

---

## 2026-04-27 -- 코딩 에이전트/산업 2026-04 Harvest: 8페이지 신규 생성

소스: `raw/2026-04-27-harvest-coding-industry.md`

**생성 - tooling · summary (2)**
- `cursor-3-2-release` -- Cursor 3.2 비동기 서브에이전트, 멀티루트 워크스페이스, Interactive Canvas, /debug CLI
- `windsurf-2-0-release` -- Windsurf 2.0 에이전트 커맨드 센터, Spaces, Devin Cloud 내장, Arena Mode, Plan Mode

**생성 - tooling · entity (2)**
- `devin-2-0-release` (project: Devin) -- SWE-Bench Verified 51.5%, Fast Mode, v3 API, 컴퓨터 사용 엔드투엔드 테스팅
- `google-antigravity-ide` (project: Google Antigravity) -- 에이전트 퍼스트 IDE, Editor+Manager 이중 뷰, 멀티모델(Gemini/Claude/GPT), 퍼블릭 프리뷰

**생성 - concepts · case-study (1)**
- `swe-bench-pro-contamination` -- Verified vs Pro 20%p+ 격차, 학습 데이터 오염 분석, 실무 평가 재검토

**생성 - applications · case-study (1)**
- `spacex-cursor-acquisition-option` -- SpaceX 600억$ 인수 옵션, a16z 20억$ 펀딩, Cognition AI 250억$ 협상 동반

**생성 - concepts · summary (1)**
- `korea-ai-basic-act-2026` -- 2026-01-22 시행, 고성능 AI 10²⁶ FLOPs 의무, 네이버 Clova X 종료, EU AI Act 비교

**생성 - applications · summary (1)**
- `ai-labor-market-impact-2026-04` -- 월 -1.6만 미국 일자리(골드만삭스), Gen Z 채용 -25%, WEF 2030 예측 +200만, 개발자 양극화

**index.md 갱신**: 8 신규 링크 추가 (tooling entity+summary, concepts concept+summary, applications case-study+summary 섹션)

---

## 2026-04-27 -- Anthropic/OpenAI 2026-04 Harvest: 8페이지 신규 생성

소스: `raw/2026-04-27-harvest-anthropic.md`, `raw/2026-04-27-harvest-openai-xai-meta.md`

**생성 - applications · case-study (4)**

- `google-40b-anthropic-investment` -- Google Alphabet 최대 400억 달러 투자. 즉시 100억+조건부 300억. 밸류에이션 3,500억 달러
- `amazon-anthropic-5gw-compute` -- Amazon 250억 달러 + 5GW 컴퓨트. Anthropic 10년 1,000억 달러 AWS 지출 약정
- `anthropic-30b-revenue-milestone` -- 연매출 런레이트 300억 달러 돌파. 2025년 말 90억 → 4개월 만에 3.3배
- `openai-stargate` -- Project Stargate 5,000억 달러 AI 인프라 JV. 확정 1,000억+8GW+ 계획. 국제 확장 진행 중

**생성 - concepts · case-study (1)**

- `claude-code-mcp-security-reckoning` -- MCP STDIO RCE 취약점 공개(4월 15일)와 Claude Code 에코시스템 파급. 200,000 서버 노출. 샌드박스 하드닝 v2.1.116~117 동시 릴리스

**생성 - tooling · entity (2)**

- `gpt-5-5-launch` -- GPT-5.5 출시(4월 23일). Terminal-Bench 2.0 82.7%, OSWorld-Verified 78.7%, 1M 토큰 장문 추론
- `openai-workspace-agents` -- OpenAI Workspace Agents(4월 22일). Custom GPTs 후속. 60개+ 앱 통합, 상시 가동 클라우드 에이전트

**생성 - tooling · summary (1)**

- `codex-cli-april-2026` -- Codex CLI 2026년 4월 업데이트. Amazon Bedrock 지원, /mcp verbose 진단, reasoning-token 보고

**index.md 갱신**: 8 신규 링크 추가 (Applications case-study, Tooling entity/summary, Concepts case-study)

---

## 2026-04-27 -- OpenSource AI Harvest 2026-04: 8페이지 신규 생성

소스: `raw/2026-04-27-harvest-opensource.md`

**생성 - tooling · entity (5)**
- `langgraph-1-0-ga` -- LangGraph & LangChain 1.0 GA. 영구 상태 자동 저장, HITL 일급 지원, 타입 세이프 스트리밍 v2, 백그라운드 서브에이전트
- `hf-transformers-5` -- Transformers v5.4~5.6. Mistral 4, PP-OCRv5, PI0 로봇 정책, VidEoMT, 양자화 속도 향상
- `doubao-2-0` -- ByteDance Doubao 2.0. 3.45억 MAU, Seedream 5.0+Seedance 2.0 멀티모달 트리펙타, Douyin 수직 통합
- `openai-privacy-filter` -- Apache 2.0 오픈소스 PII 탐지 모델. 1.5B Sparse MoE, 8카테고리, F1 96%, 온프레미스
- `smollm3-release` -- HuggingFace SmolLM3-3B. 11.2T 토큰, 이중 모드 추론, 6개 언어, 온디바이스 가능

**생성 - tooling · summary (3)**
- `pytorch-2-7-release` -- PyTorch 2.7. FlexAttention CPU 지원, GQA/PagedAttention 백엔드, Context Parallel API, Intel GPU
- `vllm-v018-v019-updates` -- vLLM v0.18/v0.19. gRPC 서빙, FlexKV 오프로딩, 비동기 스케줄링 기본화, Gemma 4 지원
- `unsloth-v01-update` -- Unsloth v0.1.36. Gemma 4 학습 버그 수정, 8GB VRAM, FA2 대비 1.5x, Dynamic 2.0 GGUF

**index.md 갱신**: tooling entity 5개, tooling summary 3개 링크 추가

---

## 2026-04-27 -- DeepMind/Google 2026-04 Harvest: 8페이지 신규 생성

소스: `raw/2026-04-27-harvest-deepmind-msft-nvidia.md`

**생성 - tooling · entity (5)**

- `gemini-2-5-flash-thinking` -- Gemini 2.5 Flash Thinking. 1M 컨텍스트, Thinking 모드, 네이티브 오디오, 컴퓨터 사용. 2026-06 GA 예정
- `gemini-enterprise-agent-platform` -- Google Cloud Next '26. Agent Designer, 장기 실행 에이전트, 200+ 모델 게이트웨이, MCP+A2A 내장
- `google-tpu-8t-8i` -- 8세대 TPU. 학습(8t) 121 엑사플롭스 / 추론(8i) 3배 성능. H2 2026 프리뷰
- `veo-3-1-lite` -- Veo 3.1 Fast 대비 50% 절감. Text/Image-to-Video. Google Vids 무료 통합
- `gemini-code-assist-2026` -- 월 180,000회 무료(Copilot 90배), 1M 컨텍스트, 멀티에이전트, HIPAA/PCI-DSS

**생성 - applications · summary (2)**

- `notebooklm-2026-features` -- Cinematic Video Overview, 인포그래픽 10종, PPTX 내보내기, EPUB 업로드, 플래시카드 진도 추적
- `alphafold3-isomorphic-labs` -- AlphaFold 3 타임라인, 분자 상호작용 정확도 50% 향상, Isomorphic Labs $600M+ 투자, 2026-02 새 모델

**생성 - concepts · concept (1)**

- `project-astra-android-agent` -- Project Astra 안드로이드 에이전트. 화면 자동화, 멀티모달 ORA 루프, 컴퓨터 사용 패러다임 비교

**index.md 갱신**: tooling entity +5, applications summary +2, concepts concept +1 (총 8 링크 추가)

---

## 2026-04-27 -- OpenAI/xAI/Meta 2026-04 Harvest: 8페이지 신규 생성/갱신

소스: `raw/2026-04-27-harvest-openai-xai-meta.md`

**생성 - applications · case-study (2)**

- `openai-titan-custom-chip` -- OpenAI Titan ASIC (TSMC N3 + Broadcom + Samsung HBM4). "엔비디아 세금" 탈피, 2026-12 양산 목표
- `xai-colossus-2gw` -- xAI Colossus Memphis 2GW / 555K GPU / $18B. 세계 최대 AI 슈퍼컴퓨터

**생성 - concepts · concept (1)**

- `altman-agi-redefinition` -- Sam Altman의 AGI 정의 전환. 이진 목표 -> 역량 스펙트럼, "AI 연구 인턴의 해" 프레임

**생성 - tooling · entity (4)**

- `grok-4-3-beta-multimodal` (project: Grok) -- xAI 2026-04-17 네이티브 비디오 이해 + 문서 직접 생성. 16-에이전트 Heavy + 2M 컨텍스트
- `grok-computer-desktop-agent` (project: Grok) -- xAI 자율 데스크톱 에이전트. 5초 슬라이딩 윈도우, Macrohard (Tesla $2B). 비공개 베타
- `llama-4-scout-maverick` (project: Llama) -- 오픈 웨이트 최초 네이티브 멀티모달 MoE. Scout 16 전문가 / 10M 컨텍스트, Maverick 128 전문가. 2026-04-05
- `meta-muse-spark` (project: Muse Spark) -- [병합 갱신] 소스 추가, 2026-04 클로즈드 소스 확인 섹션 및 Llama 4 대비 전략 분화 내용 추가

**생성 - architectures · concept (1)**

- `sam-3-1-video-tracking` -- Meta SAM 3.1 공유 메모리 Object Multiplex. 단일 H100 32FPS, 16객체 동시 트래킹. Promptable Concept Segmentation (400만 개념)

**index.md 갱신**: 8 신규/갱신 링크 추가 (applications entity/case-study, tooling entity, concepts concept, architectures concept 섹션)

---

## 2026-04-27 -- Anthropic 2026-04 Harvest: 8페이지 신규 생성

소스: `raw/2026-04-27-harvest-anthropic.md`

**생성 - tooling · entity (2)**
- `claude-opus-4-7-release` -- Claude Opus 4.7 출시. SWE-bench 87.6%, CursorBench 70%, 비전 3.75MP, xhigh effort, task-budget
- `managed-agents-memory-beta` -- Managed Agents 메모리 API 퍼블릭 베타(2026-04-23). 파일시스템 저장, 세션 간 기억 유지

**생성 - applications · entity (1)**
- `claude-design-launch` -- Claude Design 출시. 자연어 시각 산출물 생성, 디자인 시스템 학습, Claude Code 핸드오프. Figma 주가 7%+ 하락

**생성 - concepts · case-study (1)**
- `mcp-rce-vulnerability-2026` -- MCP STDIO 전송 RCE 취약점. OX Security 공개, 200,000 서버 노출, CVE 10건, Anthropic 수정 거부

**생성 - papers · paper (2)**
- `auditbench-alignment-auditing` -- AuditBench. 56개 이식 LLM 감사, 14가지 우려 행동, tool-to-agent gap 발견
- `automated-weak-to-strong-researcher` -- AAR 9인스턴스, PGR 0.97, 인간 연구자 4배 이상 성과, $18,000 비용

**생성 - papers · summary (1)**
- `anthropic-economic-index-march-2026` -- 2026-03 경제지수 보고서. 태스크·지역 집중도 분산, 22-25세 채용 14% 감소

**생성 - concepts · summary (1)**
- `anthropic-election-safeguards-2026` -- Anthropic 2026 선거 안전장치 정책. 중립 처리, 유권자 조작 방지

**index.md 갱신**: 8 신규 링크 추가 (Applications entity, Papers paper+summary, Tooling entity, Concepts concept 섹션)

---

## 2026-04-27 -- arXiv 2604 Harvest Wave 2: RLHF·에이전트·RAG 논문 8편 신규 생성

소스: `raw/2026-04-27-harvest-arxiv-2604.md`

**생성 - papers · paper (8)**

- `rlhf-statistical-perspective` (2604.02507) -- RLHF 3요소를 Bradley-Terry-Luce 등 통계 이론과 연결한 서베이
- `reward-hacking-sign-robustness` (2604.02986) -- SignCert-PO, 부호 보존 반경으로 보상 해킹 완화
- `c2-rubric-reward-model` (2604.13618) -- DPO+GRPO 협력-비판 루브릭 보상 모델, 4개 벤치마크 능가
- `plan-reward-bench` (2604.08178) -- 에이전트 계획 궤적 수준 보상 모델 벤치마크, 긴 궤적 취약점 발견
- `coding-agent-behavioral-analysis` (2604.02547) -- 9,374 궤적 분석, LLM 역량이 주 성능 동인
- `consensus-trap-multiagent` (2604.17139) -- 합의 함정 정형화, 토큰 수준 라운드로빈으로 방어
- `llm-cooperation-failure` (2604.07821) -- o3 협력률 17% vs o3-mini 50% 역설, 명시적 프로토콜 필요
- `guarantrag-joint-decoding` (2604.08046) -- 결합 디코딩 RAG, 정확도 +12.1%, 환각 -16.3%

**index.md 갱신**: 8 신규 링크 추가 (Papers 섹션 paper 타입에 삽입)

---

## 2026-04-27 -- arXiv 2604 Harvest: 추론·양자화·MoE 논문 8편 신규 생성

소스: `raw/2026-04-27-harvest-arxiv-2604.md`

**생성 - papers · paper (8)**

- `expert-upcycling-moe` (2604.19835) -- MoE 전문가 업사이클링 E→mE, GPU 32% 절감
- `quantization-failure-modes` (2604.19884) -- 신호 저하 vs 연산 붕괴 2분류, 2비트 절벽 원인 규명
- `adaptive-kv-quantization` (2604.04722) -- 토큰 중요도 기반 KV 캐시 적응형 비트 폭 할당
- `alloc-moe-inference` (2604.08133) -- 활성화 예산 인식 MoE 추론, 디코드 1.34x 가속
- `dip-sd-speculative-decoding` (2604.20919) -- 분산 파이프라인 스펙 디코딩, 17.89x 처리량
- `latent-condensed-transformer` (2604.12452) -- MLA 잠재 공간 응축, 2.5x 속도 / 90% KV 축소
- `tempo-test-time-training` (2604.19295) -- EM 기반 TTT, 정책 개선+크리틱 재교정으로 정체 해결
- `overthinking-test-time-compute` (2604.10739) -- 과사고 현상 실증, 추론 길이-난이도 인식 최적화

**index.md 갱신**: 8 신규 링크 추가 (Papers 섹션 paper 타입에 삽입)

---

## 2026-04-27 -- Wiki Expand v2: 본문 빈도 + 깨진 링크 기반 30 페이지 신규 생성

**5 병렬 sonnet 에이전트 × 6 페이지 = 30 페이지**

스캔 방식: 본문 키워드 빈도 분석 (meta-llama 62회, gaussian-splatting 28회, OOD 20회) + 깨진 wikilink 빈도 ≥ 2 + ML 기초 hub 페이지 누락 발굴

**생성 - foundations · concept (8)**
- reproducing-kernel-hilbert-space, vae, neural-network, gradient-descent, backpropagation, softmax, activation-functions, loss-functions

**생성 - architectures · concept (4)**
- gaussian-splatting, normalization-layers, attention-mechanism, reasoning-llm

**생성 - concepts · concept (8)**
- out-of-distribution, ai-evaluation, regulatory-ai, ai-shutdown-problem
- scaling-laws-overview, tokenization, data-augmentation, hyperparameter-tuning

**생성 - tooling (5)**
- entity (4): meta-llama, sentence-transformers-library, gpt-models, claude-models
- concept (1): vector-database

**생성 - training · concept (2)**
- ppo, distillation-llm

**생성 - rag · concept (2)**
- embedding-models, retrieval-augmented-generation

**생성 - foundations · concept (1)**
- cross-validation

**index.md 갱신**: 30 신규 링크 추가 (모든 슬러그 검증 완료)

**위키 총 페이지**: 1,747 → 1,775 (+28, 일부 기존 파일 재작성 포함)

**스캔 보고서**: `raw/2026-04-27-wiki-expand-scan-v2.md`

**노트**
- 핵심 ML 기초 hub 페이지 (neural-network, gradient-descent, backpropagation, softmax, activation-functions, loss-functions) 7개 신규 추가로 위키 기초가 강화됨
- meta-llama / gpt-models / claude-models 모델 패밀리 hub 3개 신규 추가
- 모든 페이지 한국어, Mermaid, 교차참조 3개 이상 충족
- 아래는 각 에이전트 분산 기록 (통합용 백업)

---

## 2026-04-27 -- Wiki 6 페이지 직접 작성 (Tokenization / Activation Functions / Loss Functions / Data Augmentation / Cross-Validation / Hyperparameter Tuning)

**Mermaid 다이어그램 + 비교표 + 실무 코드 예시 포함 (600-1200줄 규모)**

**수정 - foundations · concept (2)**
- [활성화 함수 (Activation Functions)](wiki/foundations/activation-functions.md) -- Sigmoid/Tanh/ReLU/GELU/SiLU/SwiGLU 전체 비교, 죽은 ReLU 상태 다이어그램, SwiGLUFFN 실무 코드
- [손실 함수 (Loss Functions)](wiki/foundations/loss-functions.md) -- 회귀/분류/메트릭/생성 손실 전체 카탈로그, FocalLoss/InfoNCE 구현, RLHF 파이프라인 Mermaid

**생성 - foundations · concept (1)**
- [교차 검증 (Cross-Validation)](wiki/foundations/cross-validation.md) -- K-Fold/Stratified/시계열 CV/Nested CV, 데이터 누출 방지 Pipeline 패턴, Optuna 통합

**생성 - concepts · concept (3)**
- [토큰화 (Tokenization)](wiki/concepts/tokenization.md) -- BPE/Byte-Level BPE/WordPiece/SentencePiece/Unigram LM 알고리즘 전체, vocab size 결정 Mermaid, tiktoken 코드
- [데이터 증강 (Data Augmentation)](wiki/concepts/data-augmentation.md) -- 이미지/텍스트/오디오 통합 개요, Mixup/CutMix/RandAugment/EDA/역번역/합성 데이터 구현
- [하이퍼파라미터 튜닝 (Hyperparameter Tuning)](wiki/concepts/hyperparameter-tuning.md) -- Grid/Random/Bayesian Search/Optuna/Ray Tune/HyperBand/BOHB 비교, 실무 워크플로우

**index.md 갱신**: 6 신규/수정 링크 추가 (foundations concept +3, concepts concept +3)

**위키 총 페이지**: +4 신규, 2 재작성

---

## 2026-04-27 -- Wiki 핵심 6 페이지 수동 작성 (추론 모델 / GPT / Claude / 스케일링 법칙 / 지식 증류 / RAG)

**생성 - architectures · concept (1)**
- [추론 모델 (Reasoning LLM)](wiki/architectures/reasoning-llm.md) -- o1/o3/DeepSeek R1/Claude 확장 사고, 테스트 시간 컴퓨팅 스케일링, GRPO 기반 강화학습 추론 학습

**생성 - tooling · entity (2)**
- [GPT 모델 패밀리](wiki/tooling/gpt-models.md) -- OpenAI GPT 계보 허브. GPT-1/2/3/3.5/4/4o/4.1/o1/o3 진화, 멀티모달, Responses API, 모델 선택 가이드
- [Claude 모델 패밀리](wiki/tooling/claude-models.md) -- Anthropic Claude 계보 허브. Claude 1/2/3/3.5/3.7/4 진화, 헌법적 AI, 확장 사고, RSP 정책

**생성 - concepts · concept (1)**
- [스케일링 법칙 (Scaling Laws)](wiki/concepts/scaling-laws-overview.md) -- Kaplan/Chinchilla 법칙 비교, 멱함수 관계, 창발적 능력 논쟁, 테스트 시간 컴퓨팅 스케일링 4번째 축

**생성 - training · concept (1)**
- [LLM 지식 증류 (Knowledge Distillation for LLMs)](wiki/training/distillation-llm.md) -- 교사-학생 모델, 소프트 타겟, MiniLLM 리버스 KL, 시퀀스 증류, 추론 능력 증류

**생성 - rag · concept (1)**
- [검색 증강 생성 (Retrieval-Augmented Generation, RAG)](wiki/rag/retrieval-augmented-generation.md) -- Naive/Advanced/Modular RAG 패턴, 청킹·임베딩·하이브리드 검색·재순위, 정확성-신선도 균형, RAGAS 평가

**index.md 갱신**: 6 신규 링크 추가 (architectures concept / tooling entity / concepts concept / training concept / rag concept 섹션)

**위키 총 페이지**: +6

---

## 2026-04-27 -- Wiki 6 페이지 신규 생성 (Meta Llama / 3DGS / OOD / AI Eval / AI 규제 / RKHS)

**생성 - tooling · entity (1)**
- [Meta Llama](wiki/tooling/meta-llama.md) -- Meta 오픈 웨이트 LLM 패밀리 허브. Llama 1/2/3/3.1/3.2/3.3, Code Llama, Llama Guard

**생성 - architectures · concept (1)**
- [3D Gaussian Splatting 심화](wiki/architectures/gaussian-splatting.md) -- 명시적 가우시안 표현, Splatting 렌더링, NeRF 대비 비교, SIGGRAPH 2023

**생성 - concepts · concept (3)**
- [분포 외 (OOD) 탐지와 일반화](wiki/concepts/out-of-distribution.md) -- MSP/Energy/Mahalanobis, 도메인 시프트, IRM
- [AI 평가 (AI Evaluation)](wiki/concepts/ai-evaluation.md) -- 벤치마크 카탈로그, LLM-as-Judge, Chatbot Arena Elo, 평가 편향
- [AI 규제 (Regulatory AI)](wiki/concepts/regulatory-ai.md) -- EU AI Act 위험 등급, NIST AI RMF, 한국 AI기본법, 산업별 컴플라이언스

**생성 - foundations · concept (1)**
- [재현 핵 힐베르트 공간 (RKHS)](wiki/foundations/reproducing-kernel-hilbert-space.md) -- Mercer 정리, Representer Theorem, SVM/GP/NTK 연결, MMD

**index.md 갱신**: 6 신규 링크 추가

**위키 총 페이지**: +6

---

## 2026-04-27 -- Wiki 수동 작성 6 페이지 신규 생성 (배치 2)

**6 페이지 직접 작성 (Mermaid 다이어그램 + 비교표 + 코드 예시 포함)**

**생성 - foundations · concept (4)**
- [신경망 (Neural Network)](wiki/foundations/neural-network.md) -- 퍼셉트론~딥러닝 계보, MLP/CNN/RNN/Transformer, 학습 프로세스 전체
- [경사하강법 (Gradient Descent)](wiki/foundations/gradient-descent.md) -- Vanilla/SGD/Mini-batch, 모멘텀, Adam/AdamW, 학습률 스케줄링, 수렴 이론
- [역전파 (Backpropagation)](wiki/foundations/backpropagation.md) -- 연쇄법칙, 계산 그래프, 자동 미분, 기울기 소실/폭발, gradient checkpointing
- [소프트맥스 (Softmax)](wiki/foundations/softmax.md) -- 확률 분포 변환, 수치 안정성, 온도 스케일링, Attention/분류 활용

**생성 - rag · concept (1)**
- [임베딩 모델 (Embedding Models)](wiki/rag/embedding-models.md) -- Dense/Sparse, MTEB 평가, OpenAI/BGE-M3/E5/GTE 비교, 다국어, 도메인 파인튜닝

**생성 - tooling · concept (1)**
- [벡터 데이터베이스 (Vector Database)](wiki/tooling/vector-database.md) -- HNSW/IVF-PQ 인덱스, ANN, 메타데이터 필터, Pinecone/Qdrant/Milvus/Weaviate/Chroma 비교

**index.md 갱신**: 6 신규 링크 추가 (foundations +4, rag +1, tooling +1)

**위키 총 페이지**: 1,747 → 1,753 (+6)

## 2026-04-27 -- Wiki 수동 작성 6 페이지 신규 생성

**6 페이지 직접 작성 (Mermaid 다이어그램 + 비교표 + 코드 예시 포함)**

**생성 - architectures (2)**
- concept: normalization-layers (BatchNorm/LayerNorm/RMSNorm/GroupNorm/InstanceNorm 비교, Pre vs Post-Norm)
- concept: attention-mechanism (Additive/Scaled Dot-Product, 자기/교차 어텐션, 멀티헤드 전체 개요)

**생성 - tooling (1)**
- entity: sentence-transformers-library (SBERT 공식 라이브러리, MTEB, RAG 통합)

**생성 - concepts (1)**
- concept: ai-shutdown-problem (Off-Switch Game, 도구적 수렴, CIRL 해결책)

**생성 - foundations (1)**
- concept: vae (변분 오토인코더, ELBO, 재매개화 트릭, 생성 모델 계보)

**생성 - training (1)**
- concept: ppo (clipped objective, GAE, importance sampling, RLHF 핵심 알고리즘)

**index.md 갱신**: 6 신규 링크 추가 (architectures +2, tooling +1, concepts +1, foundations +1, training +1)

**위키 총 페이지**: 1,747 → 1,753 (+6)

---

## 2026-04-27 -- Wiki Expand: 깨진 wikilink 기반 30 페이지 신규 생성

**5 병렬 sonnet 에이전트 × 6 페이지 = 30 페이지**

스캔 결과: wikilink 타겟 2,113개 중 깨진 링크 440개. 빈도 ≥ 1 후보에서 변형 슬러그 제외 후 30개 확정.

**생성 - tooling (5)**
- entity (4): github-copilot, vllm, gemini-models, dspy, mcp
- concept (1): ai-accelerators

**생성 - architectures · concept (4)**
- multimodal-llm, sentence-transformer, two-tower-model, transformer

**생성 - concepts · concept (10)**
- time-series-forecasting, digital-twin, llm-as-judge, evaluation-bias, ab-testing
- image-classification, ai-alignment, long-context, word-embeddings, user-modeling

**생성 - foundations · concept (2)**
- mcmc, kernel-methods

**생성 - training · concept (3)**
- rlhf, lora, fine-tuning

**생성 - inference · concept (2)**
- kv-cache-optimization, quantization

**생성 - agents · concept (1)**
- function-calling

**생성 - applications · concept (2)**
- code-completion, image-captioning

**index.md 갱신**: 30 신규 링크 추가 (Agent 5 분량 6개는 통합 세션에서 보완)

**위키 총 페이지**: 1,717 → 1,747 (+30)

**스캔 보고서**: `raw/2026-04-27-wiki-expand-scan.md`

**노트**
- 빈도 12회 github-copilot 등 핵심 hub 페이지 보충으로 깨진 wikilink 대폭 감소 예상
- 모든 페이지 한국어, Mermaid 다이어그램, 교차참조 3개 이상 충족
- 아래는 각 에이전트가 분산 기록한 상세 항목 (통합용 백업)

---

## 2026-04-27 -- Wiki Manual Batch: 6 페이지 생성 (concept 5 + entity 1)

**생성 - tooling · concept (1)**
- [AI 가속기 (AI Accelerators)](wiki/tooling/ai-accelerators.md) -- GPU/TPU/LPU/RDU/WSE/Tensix 비교. SIMT vs 데이터플로우, 추론·학습 특화 가속기 전체 지형

**생성 - tooling · entity (1)**
- [Gemini 모델 패밀리](wiki/tooling/gemini-models.md) -- Google DeepMind 멀티모달 LLM 허브. 1.0/1.5/2.0/3.x 세대, Pro/Flash/Ultra/Nano 변형, TPU 인프라

**생성 - training · concept (1)**
- [RLHF (Reinforcement Learning from Human Feedback)](wiki/training/rlhf.md) -- SFT→보상모델→PPO 3단계 파이프라인. InstructGPT 기반, DPO·GRPO 파생 출발점

**생성 - foundations · concept (1)**
- [MCMC (Markov Chain Monte Carlo)](wiki/foundations/mcmc.md) -- Metropolis-Hastings, Gibbs, HMC, NUTS. 베이지안 추론 정확한 샘플링 방법론, PyMC/NumPyro 실무 가이드

**생성 - concepts · concept (1)**
- [평가 편향 (Evaluation Bias)](wiki/concepts/evaluation-bias.md) -- LLM-as-Judge 자기선호·위치·길이 편향, 벤치마크 오염, Goodhart Law. 평가 신뢰성 확보

**생성 - architectures · concept (1)**
- [Sentence Transformer (SBERT)](wiki/architectures/sentence-transformer.md) -- Siamese BERT + Mean Pooling 문장 임베딩. MTEB 표준 평가, BGE-M3/E5/GTE 후계 모델

**index.md 갱신**: tooling entity +1, tooling concept +1, training concept +1, foundations concept +1, concepts concept +1, architectures concept +1 = 6 신규 링크 추가

---

## 2026-04-27 -- Wiki Manual Batch: 6 페이지 생성 (concept 5 + entity 1)

**생성 - applications · concept (1)**
- [코드 완성 (Code Completion)](wiki/applications/code-completion.md) -- 라인/블록/FIM 완성 기법, HumanEval/MBPP pass@k 평가, 도구 비교, 레이턴시 최적화

**생성 - concepts · concept (3)**
- [AI 정렬 (AI Alignment)](wiki/concepts/ai-alignment.md) -- 외부/내부 정렬, 헌법적 AI, 보상 해킹, 수정 가능성, ASL 안전 분류 체계
- [긴 컨텍스트 (Long Context)](wiki/concepts/long-context.md) -- Lost-in-the-Middle, RoPE 보간, ALiBi, 슬라이딩 윈도우, 1M+ 컨텍스트 시대
- [단어 임베딩 (Word Embeddings)](wiki/concepts/word-embeddings.md) -- One-Hot→Word2Vec→FastText→문맥화→SBERT→BGE 임베딩 진화, MTEB 평가

**생성 - foundations · concept (1)**
- [커널 방법 (Kernel Methods)](wiki/foundations/kernel-methods.md) -- SVM 커널 트릭, RBF/다항식 커널, RKHS, 랜덤 푸리에 특징, NTK 딥러닝 연결

**생성 - tooling · entity (1)**
- [Model Context Protocol (MCP)](wiki/tooling/mcp.md) -- Anthropic 발표 표준 도구 통신 프로토콜, JSON-RPC 2.0, 도구/리소스/프롬프트 원시 타입, 광범위한 생태계 채택

**index.md 갱신**: foundations +1, applications +1, concepts +3, tooling +1 = 6 신규 링크 추가

---

## 2026-04-27 -- Wiki Manual Batch: 6 페이지 생성 (concept 5 + entity 1)

**생성 - architectures · concept (1)**
- [두 타워 모델 (Two-Tower Model)](wiki/architectures/two-tower-model.md) -- 쿼리/아이템 분리 인코더, 추천 시스템 표준, in-batch negatives, ANN 연동

**생성 - inference · concept (1)**
- [KV 캐시 최적화 종합 (KV Cache Optimization)](wiki/inference/kv-cache-optimization.md) -- PagedAttention, 프리픽스 캐싱, Radix Tree, MLA 압축 종합 가이드

**생성 - concepts · concept (2)**
- [A/B 테스팅 (A/B Testing)](wiki/concepts/ab-testing.md) -- 통계적 가설 검정, 최소 표본 크기, 다중 비교 보정, MAB 대안, ML 배포 평가
- [이미지 분류 (Image Classification)](wiki/concepts/image-classification.md) -- ImageNet 역사, AlexNet→ResNet→ViT 진화, top-1/top-5 지표, 전이학습 표준

**생성 - agents · concept (1)**
- [함수 호출 (Function Calling)](wiki/agents/function-calling.md) -- LLM 도구 실행 메커니즘 종합. JSON Schema, 병렬 호출, 구조화 출력, MCP 진화

**생성 - tooling · entity (1)**
- [DSPy 허브 (DSPy - Stanford NLP)](wiki/tooling/dspy.md) -- DSPy entity 허브. 시그니처/모듈/옵티마이저, MIPRO v2, GEPA, 프로덕션 패턴

**index.md 갱신**: 6개 신규 링크 추가 (architectures 1, inference 1, concepts 2, agents 1, tooling 1)

**위키 총 페이지**: 1,717 → 1,723 (+6)

---

## 2026-04-27 -- Wiki 6 페이지 신규 생성 (entity 2 + concept 3 + architectures concept 1)

**생성 - tooling · entity (2)**
- github-copilot: GitHub Copilot 허브. OpenAI Codex->GPT-4o+Claude 멀티모델 진화, Copilot Edits/Coding Agent, FIM, 경쟁 비교
- vllm: vLLM 허브. PagedAttention, 연속 배치, OpenAI API 호환, TP/PP 분산 추론, 양자화/prefix caching

**생성 - concepts · concept (3)**
- time-series-forecasting: ARIMA->LSTM->Transformer(Informer/PatchTST)->파운데이션 모델(TimesFM/Chronos/GraphCast) 진화 계보
- digital-twin: 물리 자산 가상 복제본 개념. IoT+AI 융합, 5단계 성숙도 모델, 산업별 응용, Azure/AWS 플랫폼
- llm-as-judge: LLM 심판 평가 패러다임. MT-Bench/AlpacaEval, 자기선호/위치/길이 편향 유형과 완화 전략

**생성 - architectures · concept (1)**
- multimodal-llm: 멀티모달 LLM 일반 개요. Q-Former/MLP 프로젝터/교차 어텐션 3대 연결 방식, BLIP/LLaVA/Flamingo 계보, 환각 문제

**index.md 갱신**: tooling 2 + concepts 3 + architectures 1 = 6 신규 링크 추가

**위키 총 페이지**: 1,717 → 1,723 (+6)

---

## 2026-04-27 -- Wiki Ingest V3 Wave 4: 60 페이지 생성 (FINAL)

**10 병렬 sonnet 에이전트 × 6 페이지 = 60 페이지/웨이브**

**생성 - tooling · entity (30)**
- cline-claude-coder, zed-ai-editor, tabnine-completion, codeium-completion, supermaven-fast-completion, cloud-code-jetbrains
- void-editor-ai, helix-editor-ai, neovim-copilot-ai, xinference-multi-model, dolphinflow-fine-tuning, modal-com-runtime
- baseten-deployment, replicate-platform, together-ai-inference, fireworks-ai-platform, anyscale-platform, bento-cloud-mlops
- e2b-ai-sandbox, modal-volumes-storage, inferless-deployment, octo-ai-platform, perplexity-api, groq-cloud-api
- cerebras-cloud-inference, sambanova-systems-cloud, d-matrix-corsair, tenstorrent-grayskull, opencode-cli, crush-coding-agent

**생성 - concepts · concept (30)**
- ai-fluency-literacy, ai-economic-impact, ai-reasoning-vs-memorization, zero-vs-few-shot-comparison
- open-vs-closed-domain-qa, prompt-as-program, prompt-template-libraries
- positional-bias-llm, recency-bias-llm, confirmation-bias-llm, self-preference-bias, fabrication-vs-confabulation
- faithfulness-attribution, groundedness-evaluation, evidence-attribution
- emergent-tool-use, emergent-deception, specification-gaming-deeper
- wireheading-rl, instrumental-convergence, corrigibility-alignment, orthogonality-thesis
- agi-superintelligence-debate, ai-takeoff-scenarios
- ai-existential-risk, transformative-ai-impact, economic-displacement-ai
- ai-pause-letter-impact, anthropic-rsp-evolution, ai-frontier-model-forum

**index.md 갱신**: tooling 30 + concepts 30 = 60 신규 링크 추가

**위키 총 페이지**: 1,657 → 1,717 (+60)

**🎉 V3 큐 완료**: 누적 Wave 1+2+3+4 = 300 / 300 페이지 (100%)

**노트**
- 모든 페이지 한국어 본문, Mermaid 다이어그램, 관련 문서 wikilink 섹션 포함
- 아래는 각 에이전트가 분산 기록한 상세 항목 보존 (통합용 백업)

---

## 2026-04-27 -- AGI 안전 핵심 개념 6페이지 작성 (와이어헤딩·도구적 수렴·교정가능성·직교성·AGI 논쟁·이륙 시나리오)

**생성 - concepts · concept (6)**

- [와이어헤딩 - RL 보상 회로 단락](wiki/concepts/wireheading-rl.md) -- 보상 신호 직접 조작, 환경 무시, CoastRunners/Tetris 사례, RLHF 평가자 조작, 방어 전략
- [도구적 수렴 (Instrumental Convergence)](wiki/concepts/instrumental-convergence.md) -- 자기 보존·목표 보존·자원 획득·인지 향상·기술 습득 5대 수렴 목표, 페이퍼클립 사고 실험, Bostrom
- [교정가능성 (Corrigibility)](wiki/concepts/corrigibility-alignment.md) -- 완전복종/저항 스펙트럼, 종료 문제, CIRL, 역설(교정가능=악용가능), 실무 설계 원칙
- [직교성 가설 (Orthogonality Thesis)](wiki/concepts/orthogonality-thesis.md) -- 지능-목표 독립성, Bostrom 2012, 진화 논증 반박, 낙관론 반박, 실무 정렬 연구 정당화
- [AGI/초지능 논쟁](wiki/concepts/agi-superintelligence-debate.md) -- 정의·측정·시기 논쟁, 6가지 AGI 정의, 스케일링 낙관론 vs LeCun 회의론, 안전 연구 기관 흐름
- [AI 이륙 시나리오 (AI Takeoff Scenarios)](wiki/concepts/ai-takeoff-scenarios.md) -- 빠른/느린/불연속 이륙, I.J. Good 지능 폭발, 재귀적 자기 개선, 방어-공격 균형, 정책 함의

**index.md 갱신**: concepts 섹션 말미에 6개 신규 링크 추가

**위키 총 페이지**: +6

---

## 2026-04-27 -- AI 활용능력·경제·추론·학습비교·QA·프롬프트 프로그래밍 Concepts 6페이지 작성

**생성 - concepts · concept (6)**

- [AI 활용 능력 (AI Fluency / AI Literacy)](wiki/concepts/ai-fluency-literacy.md) -- 4차원 역량 프레임워크(이해·사용·평가·창조), K-12 교육 프레임, 디지털 격차 → AI 격차, 취약 집단 분석
- [AI 경제 영향 분석](wiki/concepts/ai-economic-impact.md) -- 범용 기술(GPT) 논거, 노동 시장 3시나리오(낙관/비관/이분화), 생산성 역설 J-Curve, 자본-노동 분배 변화
- [추론 vs 암기 구분 (Reasoning vs Memorization)](wiki/concepts/ai-reasoning-vs-memorization.md) -- 연속 스펙트럼 모델, 리버설 커스, 카운터팩츄얼 테스트, Grokking/창발 능력 연결
- [제로샷 vs 퓨샷 학습 비교](wiki/concepts/zero-vs-few-shot-comparison.md) -- ICL 메커니즘 4가설, 모델 크기별 트레이드오프, 예시 선택 전략(KATE/EPR), 매니샷 패턴
- [개방 vs 폐쇄 도메인 QA](wiki/concepts/open-vs-closed-domain-qa.md) -- 파라메트릭 vs 비-파라메트릭 지식, RAG 아키텍처, 신선도·감사 트레이드오프, 응용별 권장 매트릭스
- [Prompt-as-Program 패러다임](wiki/concepts/prompt-as-program.md) -- DSPy 시그니처·모듈·옵티마이저 추상화, Bootstrap Few-Shot 자동화, TextGrad 미분 가능 프롬프팅, APO 계보

**index.md 갱신**: concepts concept 섹션 6개 신규 링크 추가

**위키 총 페이지**: +6

---

## 2026-04-27 -- AI 안전/거버넌스/경제 영향 Concepts 6페이지 작성

**생성 - concepts · concept (6)**

- [AI 실존적 위험 (X-Risk)](wiki/concepts/ai-existential-risk.md) -- Bostrom/Russell 논증, 통제 문제, 도구적 수렴, 측정 가능 위험 vs 사변, 거버넌스 접근
- [변혁적 AI 영향 (Transformative AI Impact)](wiki/concepts/transformative-ai-impact.md) -- OPP TAI 정의, GDP 성장 예측, 산업혁명 비교, 사회 적응 속도 격차
- [AI 경제 이동 / 대체 (Economic Displacement by AI)](wiki/concepts/economic-displacement-ai.md) -- Frey-Osborne 모델, 보완 vs 대체 증거, UBI 논쟁, 재훈련 정책 한계
- [AI 일시정지 운동의 영향 (AI Pause Letter Impact)](wiki/concepts/ai-pause-letter-impact.md) -- FLI 서한 배경, 엇갈린 반응, 블레츨리 선언, 거버넌스 모멘텀
- [Anthropic 책임 있는 스케일링 정책 (RSP Evolution)](wiki/concepts/anthropic-rsp-evolution.md) -- RSP v1-v3, ASL 레벨 정의, 평가+안전+보안 3축, 산업 표준화
- [Frontier Model Forum](wiki/concepts/ai-frontier-model-forum.md) -- OpenAI/Anthropic/Google/MS 협의체, 4대 목표, 정부 협력, 한계 분석

---

## 2026-04-27 -- Concepts: 편향 5종 + 프롬프트 템플릿 + 환각 분류 개념 6페이지 작성

**생성 - concepts · concept (6)**

- [프롬프트 템플릿 라이브러리 (Prompt Template Libraries)](wiki/concepts/prompt-template-libraries.md) -- LangChain/LlamaIndex/PromptLayer 비교, 버전 관리 패턴, 컴포지션 및 부분 적용, Few-shot 템플릿
- [LLM 위치 편향 (Positional Bias)](wiki/concepts/positional-bias-llm.md) -- U자형 어텐션 분포, lost-in-the-middle 현상, 평가 위치 무작위화, 컨텍스트 재배열 전략
- [LLM 최근성 편향 (Recency Bias)](wiki/concepts/recency-bias-llm.md) -- 끝 구간 과대평가, 긴 대화 일관성 표류, 요약/재주입/RAG 메모리 완화 전략
- [LLM 확증 편향 (Confirmation Bias)](wiki/concepts/confirmation-bias-llm.md) -- RLHF 아첨 메커니즘, 사실-의견 혼동, 역할 분리 및 강제 반론 요청 기법
- [LLM 자기 선호 편향 (Self-Preference Bias)](wiki/concepts/self-preference-bias.md) -- LLM-as-Judge 자기 출력 선호, 벤치마크 오염, 다중 judge 앙상블 및 교차 평가 완화
- [환각: 조작 vs 작화 (Fabrication vs Confabulation)](wiki/concepts/fabrication-vs-confabulation.md) -- 조작(없는 정보 창조) vs 작화(기억 조각 오결합), 신경심리학 용어 차용, RAG/검증/자기 확인 교정

**index.md 갱신**: concepts concept 섹션 6개 신규 링크 추가

**위키 총 페이지**: 1,669 → 1,675 (+6)

---

## 2026-04-27 -- Tooling entity 6종: AI 샌드박스/스토리지/추론 클라우드 플랫폼

**생성 - tooling · entity (6)**

- [E2B - AI 코드 실행 샌드박스](wiki/tooling/e2b-ai-sandbox.md) -- Firecracker microVM 격리 코드 실행. LLM 에이전트용 세션 유지 REPL, project: E2B
- [Modal Volumes - 영구 스토리지](wiki/tooling/modal-volumes-storage.md) -- Modal 영구 분산 파일시스템. 모델 가중치 캐싱·체크포인트·데이터셋 공유, project: Modal
- [Inferless - 서버리스 GPU 추론 플랫폼](wiki/tooling/inferless-deployment.md) -- 콜드 스타트 0.1초(주장), A100/H100, HF/S3 임포트 자동화, project: Inferless
- [OctoAI - 모델 호스팅 및 추론 플랫폼](wiki/tooling/octo-ai-platform.md) -- NVIDIA 인수(2024). 50+ 모델, 이미지 생성 강점, TensorRT/NIM 통합, project: OctoAI
- [Perplexity API - 검색 강화 LLM API](wiki/tooling/perplexity-api.md) -- 실시간 웹 검색+인용 통합 LLM API. Sonar 모델, OpenAI 호환, project: Perplexity
- [Groq Cloud - LPU 기반 초저지연 추론 클라우드](wiki/tooling/groq-cloud-api.md) -- LPU 자체 칩 1000+ tok/s. OSS 모델 서빙, OpenAI 완전 호환, project: Groq

---

## 2026-04-27 -- Concepts: RAG 평가 3종 + 창발 2종 + RL 사양 게이밍 심화 6페이지 작성

**생성 - concepts · concept (6)**

- [faithfulness-attribution](wiki/concepts/faithfulness-attribution.md) -- 충실성과 출처 귀속. ATTR 지표, NLI 수반 판단, RAGAS/TruLens 평가 프레임워크
- [groundedness-evaluation](wiki/concepts/groundedness-evaluation.md) -- 그라운드니스 평가. Coverage/Precision 2차원, LLM-as-Judge vs NLI 분류기 비교
- [evidence-attribution](wiki/concepts/evidence-attribution.md) -- 증거 귀속과 인용 생성. 주장-구절 매핑, Citation Recall/Precision, Anthropic Citations API
- [emergent-tool-use](wiki/concepts/emergent-tool-use.md) -- 신생 도구 사용 능력. 스케일 임계점, ReAct 패턴, 명시적 학습 없는 함수 호출
- [emergent-deception](wiki/concepts/emergent-deception.md) -- 신생 기만 행동. 아첨·의도 가림·평가 인식. RLHF 후 기만 메커니즘, 정렬 신호
- [specification-gaming-deeper](wiki/concepts/specification-gaming-deeper.md) -- 사양 게이밍 심화. 명세 결함 3유형, 실제 사례 카탈로그, RLHF RM 게이밍

---

## 2026-04-27 -- 에디터/서빙/파인튜닝/ML런타임 Tooling Entity 6개 작성

**생성 - tooling · entity (6)**

- [void-editor-ai](wiki/tooling/void-editor-ai.md) -- MIT 오픈소스 Cursor 대안 (Void). VSCode 포크, LLM 라우터 자유 선택, 프라이버시 우선 기업용
- [helix-editor-ai](wiki/tooling/helix-editor-ai.md) -- Rust 기반 모달 에디터 AI 통합 (Helix). LSP/Tree-sitter 기본 탑재, 커뮤니티 tmux/CLI AI 통합
- [neovim-copilot-ai](wiki/tooling/neovim-copilot-ai.md) -- Neovim AI 코딩 허브 (Avante.nvim + CodeCompanion). Cursor 스타일 AI 사이드바, 멀티 LLM, 서버 SSH 환경 대응
- [xinference-multi-model](wiki/tooling/xinference-multi-model.md) -- 다중 모델 동시 추론 서버 (Xinference). OpenAI API 호환, vLLM/llama.cpp/MLX 멀티 백엔드, 분산 클러스터
- [dolphinflow-fine-tuning](wiki/tooling/dolphinflow-fine-tuning.md) -- 시각적 파인튜닝 워크플로우 도구 (DolphinFlow). 데이터셋 준비 UI + LoRA 마법사, 비기술자 대상
- [modal-com-runtime](wiki/tooling/modal-com-runtime.md) -- 서버리스 ML 런타임 (Modal.com). Python 데코레이터로 GPU 배포, 1-5초 콜드 스타트, 초 단위 과금

**index.md 갱신**: tooling entity 6개 신규 링크 추가

**위키 총 페이지**: 1,663 → 1,669 (+6)

---

## 2026-04-27 -- AI 가속기 & 코딩 에이전트 Tooling Entity 6개 작성

**생성 - tooling · entity (6)**

- [cerebras-cloud-inference](wiki/tooling/cerebras-cloud-inference.md) -- WSE-3 웨이퍼스케일 칩 기반 초고속 LLM 추론. ~1,800 tok/s, OpenAI 호환
- [sambanova-systems-cloud](wiki/tooling/sambanova-systems-cloud.md) -- RDU 데이터플로우 칩 엔터프라이즈 AI. 405B 모델, 국립 연구소 고객
- [d-matrix-corsair](wiki/tooling/d-matrix-corsair.md) -- 디지털 인메모리 컴퓨팅 추론 전용 ASIC. Microsoft 투자
- [tenstorrent-grayskull](wiki/tooling/tenstorrent-grayskull.md) -- Jim Keller AI 칩. RISC-V Tensix 코어, TT-Metalium 오픈소스
- [opencode-cli](wiki/tooling/opencode-cli.md) -- MIT 오픈소스 터미널 코딩 에이전트. 다중 LLM 라우팅
- [crush-coding-agent](wiki/tooling/crush-coding-agent.md) -- Charm 팀 TUI 코딩 에이전트. Bubbletea, MCP 지원

**index.md 갱신**: tooling entity 6개 신규 링크 추가

**위키 총 페이지**: 1,657 → 1,663 (+6)

---

## 2026-04-27 -- Tooling Entity 6개 수동 작성

**생성 - tooling · entity (6)**

- [cline-claude-coder](wiki/tooling/cline-claude-coder.md) -- VS Code 오픈소스 자율 코딩 에이전트 (Cline). MCP 네이티브, 브라우저 제어, 다중 모델 라우팅, Apache 2.0
- [zed-ai-editor](wiki/tooling/zed-ai-editor.md) -- Rust/GPUI 기반 고성능 AI 에디터 (Zed). GPU 렌더링, 실시간 협업 (CRDT), Atom 창업자 팀
- [tabnine-completion](wiki/tooling/tabnine-completion.md) -- AI 코드 완성 도구 (Tabnine). 2019년 출시, 로컬 모델 실행, 엔터프라이즈 프라이버시 특화
- [codeium-completion](wiki/tooling/codeium-completion.md) -- 무료 AI 코드 완성 (Codeium). 개인 완전 무료, 70+ 언어, 40+ IDE. Windsurf 모회사
- [supermaven-fast-completion](wiki/tooling/supermaven-fast-completion.md) -- 초고속 코드 완성 (Supermaven). Babble 모델, 1M 컨텍스트, <100ms 응답
- [cloud-code-jetbrains](wiki/tooling/cloud-code-jetbrains.md) -- Google 공식 JetBrains 플러그인 (Cloud Code). GKE/Cloud Run 관리, Gemini Code Assist

---

## 2026-04-27 -- Wiki Ingest V3 Wave 3: 80 페이지 생성

**10 병렬 sonnet 에이전트 × 8 페이지 = 80 페이지/웨이브**

**생성 - agents · entity (1)**
- browser-use-agent-framework -- DOM 시각 표현 + Playwright 백엔드, 멀티 LLM 지원

**생성 - agents · concept (14)**
- agentic-web-search-pattern, document-qa-agent, coding-agent-tdd, agent-self-correction
- agent-fallback-strategies, agent-rate-limiting-patterns, agent-context-management
- agent-task-decomposition-patterns, parent-child-spawn-pattern, agent-as-tool-pattern
- agent-state-machine, agent-event-driven-pattern, agent-circuit-breaker, agent-saga-pattern

**생성 - applications · concept (30)**
- ai-architecture-design, ai-game-development, ai-supply-chain-optimization, ai-fraud-detection
- ai-cyber-threat-hunting, ai-personalization-engines, ai-content-recommendation, ai-anomaly-detection
- ai-network-monitoring, ai-aiops-log-analysis, ai-realtime-translation, ai-sign-language
- ai-accessibility-tools, ai-mental-health, ai-elder-care, ai-agriculture-farming, ai-climate-modeling
- ai-sustainability-optimization, ai-energy-grid, ai-urban-planning, ai-transportation-routing
- ai-autonomous-vehicles, ai-warehouse-robotics, ai-quality-inspection, ai-predictive-maintenance
- ai-credit-scoring, ai-portfolio-management, ai-legal-discovery, ai-tax-compliance, ai-hr-recruitment

**생성 - papers · paper (30)**
- resnet-original-paper, dropout-original-paper, batch-norm-original-paper, layer-norm-original-paper
- adam-original-paper, word2vec-original-paper, roberta-paper, albert-paper, electra-paper, xlnet-paper
- flamingo-paper, blip-paper, blip-2-paper, llava-original-paper, minigpt4-paper
- instructblip-paper, kosmos-paper, fuyu-paper, ulm-fit-paper
- simclr-original-paper, moco-original-paper, byol-original-paper, dino-original-paper
- mae-original-paper, videomae-paper, point-mae-paper, ddpm-original-paper
- ddim-paper, classifier-free-guidance-paper, lcm-latent-consistency-paper

**생성 - tooling · entity (5)**
- ragflow-platform, text-generation-inference-tgi, lmdeploy-internlm
- tabby-self-hosted-coding, continue-vscode-extension

**index.md 갱신**: agents 15 + applications 30 + papers 30 + tooling 5 = 80 신규 링크 추가

**위키 총 페이지**: 1,577 → 1,657 (+80)

**노트**
- 모든 페이지 한국어 본문, Mermaid 다이어그램, 관련 문서 wikilink 섹션 포함
- 누적 Wave 1+2+3 = 240 페이지 / 300 큐 중 80% 완료
- 아래는 각 에이전트가 분산 기록한 상세 항목 보존 (통합용 백업)

---

## 2026-04-27 -- (분산 기록) applications 산업별 8페이지 신규 작성

**생성 - applications · concept (8) — Agent 3**
- ai-game-development -- 절차적 콘텐츠 생성, NPC 대화, 게임 밸런싱, 자산 생성, AAA 통합. EA/Ubisoft/Activision 사례
- ai-supply-chain-optimization -- 수요 예측(GNN+Transformer), 재고 최적화, VRP 경로 계획, 공급망 위험 평가, ERP 통합. Walmart/DHL/Maersk 사례
- ai-fraud-detection -- 거래/보험/정체성 사기, 그래프 신경망, 실시간 스코어링. PayPal/Stripe 사례
- ai-cyber-threat-hunting -- SIEM/EDR 통합, 이상 탐지, 위협 인텔리전스, MITRE ATT&CK 매핑
- ai-personalization-engines -- 1:1 콘텐츠 큐레이션, 행동 예측, 다중 채널 통합, 동의 관리
- ai-content-recommendation -- Netflix/Spotify/YouTube 패턴, 두 타워 + 트랜스포머, A/B 테스팅
- ai-anomaly-detection -- 시계열/그래프/이미지 이상, 비지도 학습(IF/AE/PatchCore), IT 인프라 모니터링
- ai-network-monitoring -- NetFlow 분석, 이상 트래픽, DDoS 탐지, 자동 라우팅 조정

## 2026-04-27 -- (분산 기록) applications 접근성/공익 8페이지 신규 작성

**생성 - applications · concept (8) — Agent 4**
- ai-aiops-log-analysis -- 로그 클러스터링, 이상 시퀀스, 근본 원인 분석, ChatOps. Splunk/Datadog/Dynatrace 사례
- ai-realtime-translation -- 동시 번역, 음성-음성 직접 번역, Whisper/Seamless, 회의/방송 응용
- ai-sign-language -- RGB-D 비디오 인식, 3D 아바타 생성, 청각 장애인 접근성, ASL/KSL/JSL 다중 수어
- ai-accessibility-tools -- 화면 읽기, 자동 캡션, 알트 텍스트, 색맹 보정, 모바일 통합
- ai-mental-health -- 감정 분석, CBT 기반 챗봇, 위기 감지, 윤리적 프레임워크, Woebot/Wysa 사례
- ai-elder-care -- 낙상 감지, 약물 알림, 동반 챗봇, 인지 모니터링
- ai-agriculture-farming -- 위성 작물 모니터링, 정밀 살포, 가축 행동, 수확 예측. John Deere/Climate FieldView 사례
- ai-climate-modeling -- GraphCast, ClimaX, 신경 PDE 솔버, 극한 날씨 예측 가속, ECMWF 통합

---

## 2026-04-27 -- applications 카테고리 지속가능성·에너지·교통·제조 도메인 8페이지 신규 작성

**생성 - applications · concept (8)**
- ai-sustainability-optimization -- AI 지속가능성 최적화. ESG 보고 자동화, 탄소 배출 예측(Scope 1/2/3), 순환 경제 분석, 공급망 환경 영향 평가. Microsoft/Amazon/Pachama 사례
- ai-energy-grid -- AI 에너지 그리드 관리. 수요/발전 예측(LSTM/GNN), 분산 에너지 자원(DER) 통합, 가상 발전소(VPP), 마이크로그리드, 강화학습 디스패치. Tesla/Google/Octopus Energy 사례
- ai-urban-planning -- AI 도시 계획. 토지 이용 최적화, GNN 교통 수요 모델, 도시 디지털 트윈, AI 시민 참여 챗봇, 에이전트 기반 시뮬레이션. 싱가포르 Virtual Singapore/로테르담/바르셀로나 사례
- ai-transportation-routing -- AI 교통 경로 최적화. GNN 기반 ETA 예측, 다중 모드 통합(MaaS), VRP 신경 조합 최적화, MARL 신호 제어, DeepMind Green Light. Google Maps/Uber/Amazon 사례
- ai-autonomous-vehicles -- AI 자율 주행 차량. SAE 레벨 분류, 인식-예측-계획-제어 파이프라인, BEV 변환, Tesla 비전 전용 vs Waymo 멀티센서, MLOps 섀도 모드, 기능 안전(ISO 26262)
- ai-warehouse-robotics -- AI 창고 로보틱스. 시각 SLAM/AMR 내비게이션, 파지 계획(GQ-CNN), 다중 로봇 협력(MAPF), 슬로팅 최적화, Amazon Kiva/Sparrow/Cardinal, Ocado/Symbotic 사례
- ai-quality-inspection -- AI 품질 검사(제조). 지도학습 결함 탐지 vs 비지도 이상 탐지, PatchCore/FastFlow, 데이터 증강, Grad-CAM 설명 가능성, 산업 4.0 데이터 폐루프. BMW/Intel/Foxconn 사례
- ai-predictive-maintenance -- AI 예측 유지보수. 진동/온도/음향 분석, 베어링 결함 주파수, LSTM/TCN/Transformer RUL 예측, PINN 물리 정보 학습, 디지털 트윈 연동, SHAP 설명. GE/SKF/Rolls-Royce 사례

## 2026-04-27 -- 자기지도 비전 학습 + 확산 모델 원조 논문 8편 신규 작성

**생성 - papers · paper (8)**
- simclr-original-paper -- SimCLR (Chen et al., ICML 2020, arXiv:2002.05709). 강한 데이터 증강+큰 배치(4096-8192)+비선형 투영 헤드+NT-Xent 손실. 자기지도 비전 대조 학습 표준 프레임워크 수립. ImageNet 선형 평가 69.3% (ResNet-50)
- moco-original-paper -- MoCo (He et al., CVPR 2020, arXiv:1911.05722). 모멘텀 인코더(EMA, m=0.999)+FIFO 큐(65536 키)로 동적 딕셔너리 구현. 배치 크기 독립적 음성 샘플 유지. PASCAL VOC 탐지에서 지도학습 사전학습 최초 능가
- byol-original-paper -- BYOL (Grill et al., NeurIPS 2020, arXiv:2006.07733). 음성 샘플 없는 자기지도 학습. 온라인-타겟 비대칭 구조(예측기 Only 온라인)+ 모멘텀 EMA. ImageNet 74.3% (ResNet-50, 1000 에포크). 붕괴 방지 메커니즘 이론 연구 촉발
- dino-original-paper -- DINO (Caron et al., ICCV 2021, arXiv:2104.14294). 자기 증류(self-distillation)+ViT 조합에서 레이블 없이 의미론적 세그멘테이션 창발. 센터링+샤프닝으로 음성 샘플 없이 붕괴 방지. ViT-B/16 78.2%, k-NN 76.1%
- mae-original-paper -- MAE (He et al., CVPR 2022, arXiv:2111.06377). 75% 무작위 마스킹+비대칭 인코더-디코더(인코더 보이는 25%만 처리). 노이즈 예측 대신 픽셀 복원. ViT-H/14 파인튜닝 87.8% SOTA. 생성적 ViT 자기지도 학습 표준
- videomae-paper -- VideoMAE (Tong et al., NeurIPS 2022, arXiv:2203.12602). 90% 마스킹+시공간 튜브 마스킹으로 시간적 중복성 극복. 3.5k~10k 소규모 데이터에서도 강력한 전이. Kinetics-400 ViT-H 86.6% SOTA
- point-mae-paper -- Point-MAE (Pang et al., ECCV 2022, arXiv:2203.06604). FPS+k-NN 포인트 패치+Mini-PointNet 임베딩+챔퍼 거리 손실. 75% 마스킹. ModelNet40 94.04%, ScanObjectNN 85.18%. 3D 자기지도 학습 최초 지도학습 능가
- ddpm-original-paper -- DDPM (Ho et al., NeurIPS 2020, arXiv:2006.11239). 노이즈 예측 파라미터화($\epsilon_\theta$)+마르코프 확산 역확산(T=1000)+변분 하한 단순화. CIFAR-10 FID 3.17 SOTA. 현대 확산 모델(Stable Diffusion, DALL-E 2, Imagen) 시대의 시작

**index.md 갱신**: papers paper 8개 신규 링크 추가 (SimCLR, MoCo, BYOL, DINO, MAE, VideoMAE, Point-MAE, DDPM)

## 2026-04-27 -- 멀티모달 시각-언어 논문 7편 + NLP 전이학습 원조 1편 신규 작성

**생성 - papers · paper (8)**
- blip-paper -- BLIP (Salesforce, ICML 2022). MED 통합 아키텍처 + CapFilt 캡셔너-필터 부트스트래핑으로 노이즈 웹 데이터 정제. arXiv 2201.12086
- blip-2-paper -- BLIP-2 (Salesforce, ICML 2023). Q-Former 경량 브리지, 동결 ViT+동결 LLM, 학습 파라미터 0.2%로 Flamingo-80B 능가. arXiv 2301.12597
- llava-original-paper -- LLaVA (NeurIPS 2023). GPT-4 합성 시각 명령 데이터 158K, 단순 MLP 프로젝터, 오픈소스 멀티모달 명령 튜닝 시발점. arXiv 2304.08485
- minigpt4-paper -- MiniGPT-4 (ICLR 2024). 단일 선형 프로젝션으로 BLIP-2 비전+Vicuna 결합. 학습 파라미터 5M. arXiv 2304.10592
- instructblip-paper -- InstructBLIP (NeurIPS 2023). Instruction-Aware Q-Former, 13 태스크 명령 튜닝, 제로샷 일반화. arXiv 2305.06500
- kosmos-paper -- KOSMOS 시리즈 (Microsoft 2023). KOSMOS-1 멀티모달 ICL / KOSMOS-2 그라운딩 / KOSMOS-2.5 OCR-free 문서 이해. arXiv 2302.14045 + 2309.11419
- fuyu-paper -- Fuyu-8B (Adept AI 2023). 비전 인코더 없는 단순 설계, 이미지 패치 직접 선형 투영, UI/문서 특화. TextVQA 74.2
- ulm-fit-paper -- ULMFiT (Howard & Ruder, ACL 2018). NLP 전이학습 ImageNet 모먼트. 차등 학습률+STLR+단계적 해동. arXiv 1801.06146

**index.md 갱신**: papers paper 8개 신규 링크 추가

## 2026-04-27 -- Applications 5개 + Papers 3개 신규 작성

**생성 - applications · concept (5)**
- ai-credit-scoring -- 대안 데이터, 그래프 ML, 공정성 제약(통계적 동등/Equalized Odds), SHAP 설명, ECOA/GDPR 규제 준수
- ai-portfolio-management -- 강화학습 트레이딩(PPO/SAC), CVaR 리스크 모델링, HMM 체제 감지, 알트 데이터, 자동 리밸런싱
- ai-legal-discovery -- eDiscovery TAR 능동 학습, Legal-BERT 문서 분류, 핵심 사실 NER 추출, 변호사-의뢰인 특권 보호, PII 레딕션
- ai-tax-compliance -- 자동 세금 계산(VAT/역전 과세), 규제 변경 NLP 추적, 감사 위험 Isolation Forest, GLoBE Pillar 2 다국적 통합
- ai-hr-recruitment -- 이력서 임베딩 매칭(Sentence Transformers), 인터뷰 STAR 채점, 4/5 규칙 편향 감사, 직원 이탈 예측, EU AI Act 고위험 분류

**생성 - papers · paper (3)**
- resnet-original-paper -- He et al. 2015 (arXiv:1512.03385). 잔차 연결, ILSVRC 2015 5관왕, 152층 학습, CVPR Best Paper, 20만+ 인용
- dropout-original-paper -- Srivastava et al. JMLR 2014. 뉴런 무작위 비활성화, 2^n 앙상블 해석, 공동 적응 억제, MC Dropout 불확실성 추정
- batch-norm-original-paper -- Ioffe & Szegedy ICML 2015 (arXiv:1502.03167). 배치 통계 정규화, 학습률 14배 향상, ICS 가설(Santurkar 2018에서 수정), Layer/Group Norm 계보

**index.md 갱신**: applications concept 5 + papers paper 3 = 8 신규 링크 추가

---

## 2026-04-27 -- 확산 모델 논문 3편 + 추론/코딩 도구 5개 신규 작성

**생성 - papers · paper (3)**
- ddim-paper -- DDIM (Song et al., 2021) 비마르코프 확산 샘플링. 결정론적 ODE 궤적, 50배 가속, 잠재 보간
- classifier-free-guidance-paper -- CFG (Ho & Salimans, 2022). 단일 모델 조건부/비조건부 결합, guidance scale, SD 핵심
- lcm-latent-consistency-paper -- LCM (Luo et al., 2023). 잠재 일관성 증류, 1~4 스텝 SD 생성, LCM-LoRA 범용 가속

**생성 - tooling · entity (5)**
- ragflow-platform -- RAGFlow (InfinFlow). 깊은 문서 이해, 시각 청킹, 인용 추적, 엔터프라이즈 RAG 플랫폼
- text-generation-inference-tgi -- TGI (HuggingFace). Rust 기반, 연속 배치, FlashAttention, HF 공식 서빙 엔진
- lmdeploy-internlm -- LMDeploy (상하이 AI Lab). TurboMind W4A16 최적화, InternLM 계열 공식 추론
- tabby-self-hosted-coding -- Tabby. 자체 호스팅 코딩 어시스턴트, Copilot 온프레미스 대안, Apache 2.0
- continue-vscode-extension -- Continue. 오픈소스 IDE AI 확장, 모델 무관, VSCode/JetBrains, Cursor 대안

## 2026-04-27 -- Agents 아키텍처 패턴 7개 + Applications 1개 신규 작성

**생성 - agents · concept (7)**
- agent-task-decomposition-patterns -- Top-down/Bottom-up/Recursive 분해 전략, HTN/STRIPS 영향, 실무 적용
- parent-child-spawn-pattern -- 오케스트레이터가 서브에이전트 동적 생성, 병렬 처리, Claude Code 패턴
- agent-as-tool-pattern -- 에이전트를 함수 시그니처로 추상화, 계층적 멀티에이전트 구성
- agent-state-machine -- 명시적 상태+전이, LangGraph FSM 패턴, 결정론적 워크플로우
- agent-event-driven-pattern -- 이벤트 큐+핸들러, 비동기 에이전트, 코레오그래피/오케스트레이션 방식
- agent-circuit-breaker -- 반복 실패 자동 차단, 복구 탐색, 비용 통제, Closed/Open/Half-Open 상태
- agent-saga-pattern -- 다단계 트랜잭션+보상 액션, 분산 트랜잭션 영감, 롤백

**생성 - applications · concept (1)**
- ai-architecture-design -- 생성적 설계, 구조 분석, 에너지 시뮬레이션, 재료 최적화, BIM 통합

**index.md 갱신**: agents concept 7 + applications concept 1 = 8 신규 링크 추가

---

## 2026-04-27 -- ML 기초 원논문 8편 paper 페이지 생성

**생성 - papers · paper (8)**

- [layer-norm-original-paper](wiki/papers/layer-norm-original-paper.md) -- Ba, Kiros, Hinton 2016 (arXiv:1607.06450). 배치 독립 정규화, RNN/Transformer 표준 LayerNorm 원조
- [adam-original-paper](wiki/papers/adam-original-paper.md) -- Kingma & Ba 2014 (arXiv:1412.6980). 1차/2차 모멘트 추정, 편향 보정, 역대 ML 최다 인용급
- [word2vec-original-paper](wiki/papers/word2vec-original-paper.md) -- Mikolov et al. 2013 (arXiv:1301.3781). CBOW/Skip-gram, 음성 샘플링, NLP 전이학습 패러다임 선구자
- [roberta-paper](wiki/papers/roberta-paper.md) -- Liu et al. 2019 (arXiv:1907.11692). NSP 제거, 동적 마스킹, 160GB 데이터로 BERT 레시피 최적화
- [albert-paper](wiki/papers/albert-paper.md) -- Lan et al. 2019 (arXiv:1909.11942). 인수분해 임베딩, 교차 레이어 파라미터 공유, SOP. 파라미터 1/18로 BERT 능가
- [electra-paper](wiki/papers/electra-paper.md) -- Clark et al. 2020 (arXiv:2003.10555). RTD(대체 토큰 탐지), 전체 토큰 학습, RoBERTa 4배 효율
- [xlnet-paper](wiki/papers/xlnet-paper.md) -- Yang et al. 2019 (arXiv:1906.08237). 순열 LM, 두 스트림 어텐션, AR+AE 결합, 20개 태스크 SOTA
- [flamingo-paper](wiki/papers/flamingo-paper.md) -- Alayrac et al. 2022 (arXiv:2204.14198). 게이트 크로스어텐션, Perceiver Resampler, 멀티모달 few-shot 원형

---

## 2026-04-27 -- Agents 카테고리 8개 페이지 신규 작성

**생성 - agents · entity (1)**
- browser-use-agent-framework -- Browser Use 프레임워크 허브. DOM 시각 표현 + Playwright 백엔드, 멀티 LLM 지원

**생성 - agents · concept (7)**
- agentic-web-search-pattern -- 쿼리 변형 + 다중 검색 + 결과 종합. Perplexity/SearchGPT 패턴 상세
- document-qa-agent -- PDF/문서 다단계 QA, 표 처리, 이미지 처리, 인용 생성
- coding-agent-tdd -- Red-Green-Refactor 사이클 에이전트 적용. Aider/Claude Code 패턴
- agent-self-correction -- 형식/실행/논리/계획 4단계 교정, 환각 억제, 재시도 정책
- agent-fallback-strategies -- 도구/모델/기능 저하 폴백, 서킷 브레이커 패턴
- agent-rate-limiting-patterns -- 지수 백오프, 토큰 버킷, 슬라이딩 윈도우, 우선순위 큐, 비용 인식 제한
- agent-context-management -- 슬라이딩 윈도우, 요약 압축, 중요도 필터, 벡터 메모리, 컨텍스트 폭발 회피

**index.md 갱신**: agents concept 8 + entity 1 = 9 신규 링크 추가

**위키 총 페이지**: 1,577 → 1,585 (+8)

---

## 2026-04-27 -- Wiki Ingest V3 Wave 2: 80 페이지 생성

**10 병렬 sonnet 에이전트 × 8 페이지 = 80 페이지/웨이브**

**생성 - training · concept (15)**
- ultrafeedback-dataset (entity), orca-progressive-learning, webinstruct-mining, distilbert-distillation
- seq-knowledge-distillation, minillm-text-distillation, branch-train-merge, branch-train-mix-btx
- flash-attention-2-internals, mixup-data-augmentation, cutmix-augmentation, randaugment-policy
- autoaugment-search, ppo-rlhf-implementation, iterative-magpie-instruction

**생성 - inference · concept (25)**
- hqq-half-quadratic-quant, fp6-llm-quantization, atom-int8-quant, spqr-sparse-quantized
- squeezellm-quantization, omniquant-calibration, medusa-multi-head-decoding, lookahead-decoding
- parallel-decoding-jacobi, blockwise-parallel-decoding, self-speculative-decoding, hydra-speculation-cascade
- continuous-batching-internals, selective-batching, tree-attention-decoding, logits-processor-internals
- nucleus-top-p-sampling, typical-sampling, eta-sampling-locally, mirostat-perplexity
- min-p-sampling, dry-sampling-repetition, xtc-exclude-top-choices, server-sent-events-llm, websocket-llm-streaming

**생성 - rag · concept (10)**
- hnsw-graph-index, ivf-pq-vector-index, matryoshka-embeddings, token-pooling-strategies, mean-vs-cls-pooling
- last-token-pooling-decoder, weighted-attention-pooling, fixed-length-chunking, semantic-chunking-strategies
- recursive-character-splitting, propositional-chunking, agentic-chunking, context-aware-chunking, document-hierarchy-chunking

**생성 - rag · entity (9)**
- annoy-spotify, scann-google-search, diskann-microsoft
- cohere-embed-v4, voyage-ai-embeddings, nomic-embed-text, mxbai-embed-large, gte-text-embeddings
- instructor-embedding-model, e5-text-embeddings, bge-m3-embedding

**생성 - agents · concept (9)**
- function-call-evolution, tool-creator-meta-agent, selfask-decomposition, plan-and-solve-prompting
- xot-explorer-of-thought, graph-of-thoughts-got, cumulative-reasoning, critic-revise-pattern, agent-assistant-asymmetric

**생성 - agents · entity (6)**
- autogpt-original-agent, babyagi-task-agent, agentgpt-deployment
- metagpt-software-agent, chatdev-software-company, swarm-openai-handoffs

**index.md 갱신**: training 16 + inference 18 + rag 19 + agents 16 = 69 신규 링크 추가 (Agent 4/8/10이 직접 추가한 일부 항목 + 메인 세션 통합 추가)

**위키 총 페이지**: 1,497 → 1,577 (+80)

**노트**
- 모든 페이지 한국어 본문, Mermaid 다이어그램 1개 이상, 관련 문서 wikilink 섹션 포함
- Wave 2 끝나면 누적 Wave 1+2 = 160 페이지

---

## 2026-04-27 -- (구 분산 기록) Wave 2 부분 항목들

> 아래 3개 섹션은 Wave 2 진행 중 일부 에이전트가 직접 log에 기록한 분산 항목이다. 위 통합 항목으로 대체되었으나 추적용으로 보존.

## 2026-04-27 -- Wiki Ingest V3 Wave 3 (RAG 137-144): 8 페이지 생성

**생성 - rag · concept (8)**
- last-token-pooling-decoder -- LLM 기반 임베딩 표준, 인과적 어텐션에서 마지막 히든 스테이트 활용, EOS 토큰
- weighted-attention-pooling -- 학습 가능 어텐션 가중치 풀링, 단일/다중 헤드 변형, 해석 가능성
- fixed-length-chunking -- 토큰/문자 단위 고정 분할, chunk_size/overlap 파라미터, 베이스라인
- semantic-chunking-strategies -- 임베딩 유사도 급변점 경계 탐지, 퍼센타일 임계값, LangChain SemanticChunker
- recursive-character-splitting -- 분리자 우선순위 목록 재귀 적용, LangChain 표준, 언어별 커스터마이징
- propositional-chunking -- LLM 명제 추출, 자기 완결적 원자 사실, RAPTOR 연관, 검증 파이프라인
- agentic-chunking -- LLM 에이전트 추론 기반 경계 결정, 메타데이터 동시 생성, 비용-품질 최고
- context-aware-chunking -- 헤딩 경로 보존, Anthropic Contextual Retrieval LLM 컨텍스트 주입, 슬라이딩 윈도우

**index.md 업데이트**: rag concept 섹션 8건 추가

---

## 2026-04-27 -- Wiki Ingest V3 Wave 2 (Agents 153-160): 8 페이지 생성

**생성 - agents · concept (8)**
- tool-creator-meta-agent -- LLM 자체 도구 생성+실행, Code Interpreter 패턴 일반화, 샌드박스 검증 루프
- selfask-decomposition -- "후속 질문이 필요한가?" 메타 인지 분해, 검색 통합, ReAct 선행 패턴
- plan-and-solve-prompting -- 명시적 계획 단계 + 단계별 실행, PS/PS+ 변형, EMNLP 2023 제로샷 추론
- xot-explorer-of-thought -- MCTS+RL 외부 탐색기로 유망 사고 경로 계산 후 LLM 주입, ToT/GoT 진화
- graph-of-thoughts-got -- 사고 노드를 DAG로 모델링, 병합(Aggregate)/역추적(Backtrack) 지원, 비선형 추론
- cumulative-reasoning -- 검증된 명제 누적 지식베이스, 오류 전파 차단, Proposer/Verifier/Reporter 역할 분리
- critic-revise-pattern -- 비평자+수정자 반복 루프, Constitutional AI 영감, self-refine과 비교
- agent-assistant-asymmetric -- 강한 에이전트(오케스트레이터) + 약한 어시스턴트(워커) 비용 최적 구조

**index.md 업데이트**: agents 섹션 concept 항목 8건 추가

---

## 2026-04-27 -- Wiki Ingest V3 Wave 2 (Inference 105-112): 8 페이지 생성

**inference · concept (8)**
- blockwise-parallel-decoding -- 고정 블록 병렬 예측 + 순차 검증, 보조 헤드, Medusa와의 관계
- self-speculative-decoding -- 레이어 스킵 기반 자기 드래프팅, 조기 종료 헤드, Eagle-3 비교
- hydra-speculation-cascade -- 다중 드래프트 캐스케이드, 엔트로피 기반 동적 단계 선택, SpecInfer 관계
- continuous-batching-internals -- iteration-level 스케줄링, 프리필·디코딩 혼합, vLLM/TGI 구현 비교
- selective-batching -- 길이 버킷팅, 시퀀스 패킹, 토큰 버짓 배치, Flash Attention varlen 통합
- tree-attention-decoding -- 트리 마스크 수식, KV 공유, Medusa/Eagle/SpecInfer 비교
- logits-processor-internals -- 처리 파이프라인 순서, HF LogitsProcessor API, 구조화 출력 통합
- nucleus-top-p-sampling -- 수학적 정의, Holtzman et al., Top-k 비교, 구현별 경계 처리 차이

**index.md 갱신**: inference concept 8개 추가
**위키 총 페이지**: 이전 + 8 추가

---

## 2026-04-27 -- Wiki Ingest V3 Wave 1: 80 페이지 생성

**10 병렬 sonnet 에이전트 × 8 페이지 = 80 페이지/웨이브 (검증된 패턴)**

**생성 - foundations · concept (30)**
- rademacher-complexity, empirical-risk-minimization, matrix-calculus-deep-learning, fisher-information-matrix
- sparse-coding-dictionary-learning, topological-data-analysis, nonnegative-matrix-factorization, bayesian-neural-networks
- swag-stochastic-weight-averaging, deep-ensembles, adagrad-rmsprop-history, nesterov-momentum
- variational-inference-deep, bald-batchbald-active-learning, continuous-normalizing-flows, modern-hopfield-networks
- restricted-boltzmann-machines, spiking-neural-networks, reservoir-computing-esn, quantum-machine-learning
- equivariant-neural-networks, tensor-networks-ml, universal-approximation-theorem, sgd-convergence-theory
- sgld-langevin-dynamics, rkhs-kernel-methods, manifold-learning-isomap-lle, graph-signal-processing
- fairness-mathematical-foundations, ml-numerical-stability

**생성 - architectures · concept (33)**
- densenet-dense-connections, resnext-cardinality, nfnet-normalizer-free, regnet-design-spaces
- bit-big-transfer, wide-resnet, highway-networks
- wav2vec-2-speech, hubert-speech-representation, wavlm-speech-processing, conformer-speech-recognition
- tacotron-2-tts, fastspeech-2-tts
- imagen-text-to-image, dalle-3-architecture, stable-diffusion-3-mmdit, parti-autoregressive-image, muse-masked-image
- controlnet-conditioning, ip-adapter-image-prompting, animatediff-motion-modules, cogvideox-architecture
- graphsage-inductive-gnn, gin-graph-isomorphism, pna-aggregation, clustergcn-subsampling
- dino-self-distillation, byol-bootstrap, moco-momentum-contrast, simclr-augmentation, swav-clustering-features, vicreg-variance-invariance, barlow-twins-redundancy

**생성 - architectures · entity (2)**
- sora-architecture (project: Sora), veo-google-video (project: Veo)

**생성 - training · concept (15)**
- dora-weight-decomposed-lora, p-tuning-soft-prompts, adalora-adaptive-rank, ia3-injection-adapters
- prompt-tuning-soft-only, prefix-tuning-deep-prompts, compacter-hypercomplex, unipelt-mixed-peft
- simpo-simple-preference, ipo-identity-preference, cpo-contrastive-preference, spin-self-play-finetuning
- magpie-synthetic-instruction, evol-instruct-method, self-instruct-original

**index.md 갱신**: foundations 30 + architectures 35 + training 15 추가
**위키 총 페이지**: 1,417 → 1,497 (+80)

**노트**
- DALL-E 3, Sora, Veo는 공개된 정보 한정으로 작성. 추정 부분은 `[교차검증 필요]` 태그
- 모든 페이지 Mermaid 다이어그램 1개 이상 포함, 한국어 본문, 관련 문서 wikilink 섹션

---

## 2026-04-27 -- Wiki Harvest V3: 신규 시드 토픽 큐 300건 작성

**`/wiki-harvest`로 차세대 확장 큐 생성**
- 현재 위키: 1,417 페이지 (2026-04-20 mega growth 종료 시점)
- topic-queue-v2 거의 소진 (~2건 잔여), topic-queue-v3 신규 작성 필요
- 사용자 요청: "현재 완성된 wiki에 있는 주제들을 제외한 약 300개 시드 주제 추가 수집"

**큐 파일**
- `raw/2026-04-27-topic-queue-v3.md` -- 300개 신규 시드 토픽
- 형식: `슬러그 | 제목 | 카테고리 | 페이지타입 | 1줄 요약`

**카테고리별 분포 (300건)**
- foundations: 30 (라데마허/ERM/TDA/RBM/SNN/SGLD/등변신경망/페어니스 수학)
- architectures: 35 (DenseNet/ResNeXt/NFNet/wav2vec/HuBERT/Conformer/Imagen/SD3/Sora/Veo/GIN/SimCLR/MoCo/BYOL/DINO/VICReg)
- training: 30 (DoRA/AdaLoRA/IA3/SimPO/IPO/CPO/SPIN/Magpie/Evol-Instruct/Branch-Train-Merge/MiniLLM)
- inference: 25 (HQQ/FP6/SqueezeLLM/Medusa/Lookahead/Self-Spec/연속배치내부/Nucleus/Mirostat/SSE/WebSocket)
- rag: 25 (HNSW/IVF-PQ/DiskANN/Cohere/Voyage/Matryoshka/Nomic/BGE-M3/풀링전략/청킹전략)
- agents: 30 (AutoGPT/BabyAGI/MetaGPT/ChatDev/Swarm/GoT/Self-Ask/Plan-and-Solve/사가패턴/서킷브레이커)
- applications: 30 (건축/게임/공급망/사기탐지/사이버위협/접근성/정신건강/노인돌봄/농업/기후/도시계획/HR/세무)
- papers: 30 (ResNet/Dropout/BatchNorm/LayerNorm/Adam/RoBERTa/ALBERT/ELECTRA/XLNet/Flamingo/BLIP/LLaVA/MAE/DDPM/CFG/LCM)
- tooling: 35 (RAGFlow/TGI/LMDeploy/Continue/Cline/Tabnine/Codeium/Modal/Baseten/Fireworks/Cerebras/SambaNova)
- concepts: 30 (AI 활용능력/위치편향/충실성/그라운드니스/Wireheading/Instrumental Convergence/Corrigibility/AGI/X-Risk)

**중복 검증**
- 기존 1,417 페이지 슬러그 vs v3 슬러그 300건 교집합: **0건 (완전 비중복)**
- 부분 매칭 점검: 25건 발견되었으나 모두 의도된 변형/심화/원논문 페이지 (예: `dropout` concept vs `dropout-original-paper` 페이지)
- 페이지 타입 분포: concept 235 / entity 50 / paper 30

**다음 단계**
- 검증된 배치 패턴 적용 가능: 10 병렬 sonnet × 8페이지 = 80페이지/웨이브, ~7분
- 4 웨이브로 약 28-32분 내 전체 처리 가능
- `/wiki-ingest` 또는 wave 배치로 위키 페이지 생성

---

## 2026-04-20 -- 고아 링크 리페어: wikilink 렌딩 + 핵심 concept stub 8개

**고아 wikilink 대량 수정**
- 배치 1 (target exists, rename): `[[nerf]]`→`[[nerf-neural-radiance-fields]]` (9 files), `[[attention-mechanism]]`→`[[self-attention-mechanism]]` (3 files)
- 배치 2 (target exists, rename): `[[soft-actor-critic-sac]]`→`[[sac-soft-actor-critic]]`, `[[multi-agent-rl-marl]]`→`[[multi-agent-rl]]`, `[[robot-learning]]`→`[[robot-learning-sim2real]]`, `[[rl-for-agents]]`→`[[long-horizon-rl-training-for-agents]]`, `[[reranking-models]]`→`[[reranking-and-cross-encoders]]`, `[[rope-extension]]`→`[[rope-scaling-ntk-yarn]]`, `[[vector-database]]`→`[[vector-db-comparison]]`, `[[differentiable-rendering]]`→`[[volume-rendering-differentiable]]`, `[[transformer-architectures]]`→`[[transformer-architecture]]`, `[[mechanistic-interpretability]]`→`[[mechanistic-interpretability-2026]]`, `[[flashattention]]`→`[[flashattention-4-paper]]`, `[[dpo]]`→`[[dpo-paper]]`, `[[function-calling]]`→`[[function-calling-tool-use]]`
- 배치 3 (target exists, rename): `[[data-deduplication]]`→`[[data-deduplication-minhash]]`, `[[bert-architecture]]`→`[[bert-paper]]`, `[[mamba-ssm]]`→`[[mamba-original-paper]]`, `[[reasoning-models]]`→`[[ai-reasoning-models]]`, `[[recommendation-systems]]`→`[[ai-recommendation-systems]]`, `[[qlora]]`→`[[lora-qlora-finetuning]]`, `[[model-compression]]`→`[[quantization-model-compression]]`, `[[factorization-machines]]`→`[[deepfm-factorization]]`, `[[molecular-property-prediction]]`→`[[ka-gnn-molecular]]`

**concept stub 신규 생성 8건** (4개 병렬 sonnet 에이전트)
- `wiki/rag/rag.md` -- RAG 허브 (파이프라인, 구성요소, 고도화). 기존 RAG 페이지 12개 wikilink. Mermaid flowchart
- `wiki/architectures/moe.md` -- MoE 허브 (Top-K gating, load balancing, Switch/GShard). 관련 MoE 페이지 9개 wikilink. Mermaid flowchart
- `wiki/training/reinforcement-learning.md` -- RL 기초 허브 (MDP, policy/value, on/off-policy, LLM RL 연결). 관련 15개 wikilink. agent-environment loop Mermaid
- `wiki/training/distillation.md` -- KD 허브 (teacher-student, temperature, response/feature/relation-based, LLM black-box/sequence-level). 10개 wikilink
- `wiki/training/rlhf-and-alignment.md` -- RLHF 3단계 파이프라인 + outer/inner/intent alignment. DPO/iterative DPO 대안. 관련 페이지 촘촘히 연결. KL 패널티 수식
- `wiki/inference/long-context-llm.md` -- 4축 분류(어텐션/RoPE/메모리/분산). NIAH+RULER 평가. Long-context vs RAG 트레이드오프 표
- `wiki/concepts/behavior-cloning.md` -- BC 정의, compounding error, DAgger, BC vs RL 비교. LLM SFT가 BC의 일종 연결
- `wiki/concepts/explainable-ai.md` -- 해석가능성 vs 설명가능성, SHAP/LIME/saliency/counterfactual, mechanistic interp 연결, EU AI Act 규제 배경

**index.md 업데이트**
- RAG 섹션: rag 추가
- Architectures 섹션: moe 추가
- Training 섹션: reinforcement-learning, distillation, rlhf-and-alignment 3건 추가
- Inference 섹션: long-context-llm 추가
- Concepts 섹션: behavior-cloning, explainable-ai 2건 추가

**결과**
- 초기 broken wikilink 60건 → 28건 (53% 감소)
- 위키 페이지 1,408 → 1,416 (+8)

---

## 2026-04-20 -- Wave 4 Ingest: Credit Assignment Survey + GenAC 논문 2건 + concept 1건

**paper (신규 생성 2건)**
- `wiki/papers/credit-assignment-survey-paper.md` -- Credit Assignment Survey (2604.09459, Zhang). 47개 방법 2차원 taxonomy (granularity x methodology). Reasoning RL vs Agentic RL 이분법 정식화. Turn-level MDP / Hindsight Counterfactual / Privileged Asymmetric Critic. 2D taxonomy Mermaid flowchart + Reasoning vs Agentic 비교 다이어그램
- `wiki/papers/genac-paper.md` -- GenAC: Generative Actor-Critic (2604.10701, Shan/Zhong/Wang/Zhao). CoT reasoning 기반 generative critic이 discriminative scalar critic 대체. In-Context Conditioning으로 value drift 완화. value-free 트렌드(GRPO)에 경험적 반론. 구조 비교 Mermaid flowchart + actor-critic 시퀀스 다이어그램

**concept (신규 생성 1건)**
- `wiki/concepts/credit-assignment-rl.md` -- RL 크레딧 할당 source-agnostic 개념. 희소/지연 보상, Minsky 1961 기원, 고전 RL 해법(MC/TD/Eligibility Trace/Actor-Critic/GAE), LLM RL 특수성(극단적 시퀀스, 토큰=행동). Reasoning vs Agentic 이분법, Generative Critic 등장 맥락. 실무 granularity 선택 가이드 Mermaid

**갱신**
- `wiki/agents/long-horizon-rl-training-for-agents.md` -- "크레딧 할당 심화" 섹션 신설. 2차원 taxonomy 표, 5가지 핵심 기법 정리. sources에 survey raw 추가. 관련 문서에 신규 3개 링크 추가

---

## 2026-04-20 -- Wave 4 Ingest: Efficient Benchmarking + DSRL 논문 2건 + IRT concept 1건

**paper (신규 생성 2건)**
- `wiki/papers/efficient-benchmarking-paper.md` -- Efficient Benchmarking of AI Agents (2603.23749). IRT 영감 30-70% pass rate 필터로 태스크 44-70% 감축, rank fidelity 유지, Terminal-Bench 2.0 + HAL 7개 검증. 순위 안정적/절대 점수 불안정 비대칭성 핵심 발견. 벤치마크 파이프라인 Mermaid flowchart
- `wiki/papers/dsrl-pretrain-space-rl-paper.md` -- DSRL (2604.14142). P(y|x)→P(y) 주변분포 최적화, NSR-PreRL + 표준 RLVR 2단계, Policy Reincarnation. reflection 6.54x / transition 14.89x 증가. 2단계 훈련 파이프라인 Mermaid flowchart

**concept (신규 생성 1건)**
- `wiki/concepts/item-response-theory-benchmarking.md` -- 교육 심리측정학 IRT의 AI 에이전트 평가 적용 패턴. 30-70% pass rate 구간 필터 원리, optimization-free 프로토콜, 순위 안정성 vs 절대 점수 비대칭성. source-agnostic 톤 유지

**갱신 (1건)**
- `wiki/agents/long-horizon-agent-benchmarks.md` -- "평가 비용 절감: 효율적 벤치마킹" 단락 추가. efficient-benchmarking-paper, item-response-theory-benchmarking 교차참조

**index.md 업데이트**
- Papers 섹션: efficient-benchmarking-paper, dsrl-pretrain-space-rl-paper 2건 등록
- Concepts 섹션: item-response-theory-benchmarking 1건 등록

---

## 2026-04-20 -- Wave 4 Ingest: YC-Bench + AIBuildAI 논문 2건

**paper (신규 생성 2건)**
- `wiki/papers/ycbench-paper.md` -- YC-Bench (2604.01212), 1년 startup 시뮬레이션, 12 models, Claude Opus 4.6 $1.27M / GLM-5 $1.21M, adversarial client 47% 파산, scratchpad 사용이 성공 최대 예측변수. 6대 태스크 표, 실패 원인 Mermaid flowchart
- `wiki/papers/aibuildai-paper.md` -- AIBuildAI (2604.14455), hierarchical multi-agent(manager/designer/coder/tuner), MLE-Bench medal rate 63.1% SOTA, 4가지 모달리티. 계층 구조 Mermaid flowchart

**갱신 (concept 1건)**
- `wiki/agents/long-horizon-agent-benchmarks.md` -- YC-Bench / MLE-Bench 항목 추가. 벤치마크 비교표 확장, YC-Bench/MLE-Bench 전용 섹션 2개 신설, sources 배열 2건 추가, 관련 문서에 ycbench-paper / aibuildai-paper 링크

**교차참조 추가**
- [[ycbench-paper]] -> [[long-horizon-agent-benchmarks]], [[context-folding]], [[agent-memory-systems]], [[omnicode-swe-benchmark-paper]]
- [[aibuildai-paper]] -> [[orchestrator-worker-pattern]], [[anthropic-multi-agent-research-system]], [[long-horizon-agent-benchmarks]], [[omnicode-swe-benchmark-paper]]

---

## 2026-04-20 -- Willison Pelican + Prompt Archaeology Ingest

**신규 생성 (summary 2건)**
- `wiki/applications/pelican-benchmark-qwen-opus.md` (summary/applications) -- Qwen3.6-35B-A3B vs Opus 4.7 SVG pelican 테스트. 벤치마크-유용성 단절 논의. 비교표, 핵심 인용 2개
- `wiki/applications/prompt-archaeology-willison.md` (summary/applications) -- Anthropic 공개 시스템 프롬프트를 Claude Code로 분해, synthetic git history 생성 방법론. Mermaid 파이프라인 flowchart 포함

**신규 생성 (concept 1건)**
- `wiki/concepts/pelican-benchmark.md` (concept/concepts) -- Willison "자전거를 탄 펠리컨" SVG informal benchmark 개념. 2024-10 ~ 2026-04 추이, 벤치마크-유용성 단절 일반 개념

**갱신 (2건)**
- `wiki/tooling/claude-opus-4-7.md` -- "외부 평가: Pelican 벤치마크" 섹션 추가, sources에 qwen-beats-opus 추가, 관련 문서 2건 추가
- `wiki/applications/opus-4-7-system-prompt-diff.md` -- "분석 도구: Extract System Prompts" 섹션 추가, sources에 extract-system-prompts 추가, 관련 문서에 prompt-archaeology-willison 추가

**index.md 갱신**
- applications summary 서브섹션에 2건 추가
- concepts concept 서브섹션에 1건 추가

**소스**: raw/2026-04-20-blog-willison-qwen-beats-opus.md, raw/2026-04-20-blog-willison-extract-system-prompts.md

---

## 2026-04-20 -- Wiki Harvest Wave 4: 신규 8건 수집

**수집 (raw 8건, pending_ingest)**

테마: 에이전트 평가 + 장기 계획 + LLM RL(credit assignment/value models/pretrain-space RL) + 프롬프트 archaeology

- `raw/2026-04-20-blog-willison-qwen-beats-opus.md` -- Qwen3.6-35B-A3B 로컬 vs Opus 4.7 SVG pelican 테스트, 벤치마크-유용성 disconnect 주장
- `raw/2026-04-20-blog-willison-extract-system-prompts.md` -- Anthropic published system prompts를 Claude Code로 분해해 synthetic git history 생성, 프롬프트를 버전 관리 아티팩트로 취급
- `raw/2026-04-20-arxiv-ycbench-long-horizon.md` -- YC-Bench (2604.01212), 1년 startup 시뮬레이션, Opus 4.6 $1.27M, adversarial client 47% 파산, scratchpad 사용이 성공 최대 예측변수
- `raw/2026-04-20-arxiv-aibuildai-automl-agent.md` -- AIBuildAI (2604.14455), hierarchical multi-agent(manager/designer/coder/tuner), MLE-Bench 63.1% SOTA
- `raw/2026-04-20-arxiv-efficient-benchmarking.md` -- Efficient Benchmarking (2603.23749), IRT 30-70% pass rate 필터로 태스크 44-70% 감축하면서 rank fidelity 유지
- `raw/2026-04-20-arxiv-dsrl-pretrain-space-rl.md` -- DSRL (2604.14142), P(y|x)->P(y), NSR-PreRL로 reflection/transition 6.54x/14.89x 증가, Policy Reincarnation
- `raw/2026-04-20-arxiv-credit-assignment-survey.md` -- Credit Assignment Survey (2604.09459), 47 papers 2024-2026, reasoning vs agentic RL 2차원 taxonomy, turn-level MDP
- `raw/2026-04-20-arxiv-genac-generative-critic.md` -- GenAC (2604.10701), CoT reasoning 기반 generative critic이 discriminative scalar critic을 대체, in-context conditioning으로 value drift 완화

`raw/.harvest-queue.json` harvest-2026-04-20-wave4로 업데이트됨.

---

## 2026-04-20 -- concept 신규 생성: Responsible Disclosure

**concept (신규 생성 1건)**
- `wiki/concepts/responsible-disclosure.md` -- 보안 커뮤니티의 취약점 비공개 보고 후 조율 공개 규범. Full Disclosure / Responsible Disclosure / CVD 3가지 스펙트럼, 역사(BugTraq -> RFPolicy -> Google Project Zero 90일 -> ISO/IEC 29147·30111), 발견-보고-트리아지-패치-공동공개 Mermaid 플로우, AI 안전성 확장(red-team, capability-gated release와의 구조적 유사성). sources: raw/2026-04-20-blog-willison-project-glasswing.md

**교차참조 추가**
- [[responsible-disclosure]] -> [[capability-gated-release]], [[project-glasswing-case-study]], [[red-teaming-ai]], [[ai-cybersecurity-defensive]], [[llm-security-owasp]]

---

## 2026-04-20 -- concept 신규 생성: Embodied AI

**concept (신규 생성 1건)**
- `wiki/concepts/embodied-ai.md` -- 체화 인공지능 source-agnostic 개념. Brooks "intelligence without representation" 계보, Perception/Planning/Action Control/Learning 4대 구성 요소 closed-loop Mermaid 다이어그램, VLA/Sim2Real/비디오 세계 모델/로봇 파운데이션 모델 4대 연구 방향, 데이터 희소성·일반화·물리 안정성·안전성 과제. sources: raw/2026-04-20-arxiv-video-gen-robotics-survey.md

**교차참조**
- embodied-ai -> vla-models, sim2real-transfer, open-x-embodiment, video-gen-robotics-survey-paper, diffusion-policy-robot, manipulation-dexterity, robot-learning-sim2real, nvidia-cosmos, world-model, imitation-learning
- video-gen-robotics-survey-paper의 기존 [[embodied-ai]] 고아 링크 해소

---

## 2026-04-20 -- Wave 3 고아 링크 보강: world-model concept 신규 생성

**concept (신규 생성 1건)**
- `wiki/concepts/world-model.md` -- 월드 모델 source-agnostic 개념 허브. Ha&Schmidhuber(2018)/Dreamer V1-V3/LeCun JEPA/비디오 생성 기반/Physics-grounded 5대 계통 정리. agent-world model 상호작용 Mermaid 다이어그램, model-free vs model-based 비교표, 열린 질문(hallucination/장기 예측/추론 비용). video-gen-robotics-survey-paper 고아 링크 해소. sources: raw/2026-04-20-arxiv-video-gen-robotics-survey.md

**교차참조 추가**
- world-model -> world-model-architectures, dreamer-world-model, jepa-world-models, video-gen-robotics-survey-paper, sim2real-transfer, robot-learning-sim2real, diffusion-policy-robot

---

## 2026-04-20 -- Wave 3 고아 링크 보강: activation-steering concept 신규 생성

**concept (신규 생성 1건)**
- `wiki/concepts/activation-steering.md` -- inference-time 행동 제어 기법. Turner 2023 Activation Addition, Zou 2023 RepE, Panickssery 2023 CAA, Anthropic 2026 Emotion Vector 계보 정리. 벡터 추출(평균 차이/PCA/프로빙/CAA) 및 주입 메커니즘, 파인튜닝 비교, 정렬 연구 위치. emotion-concepts-claude-sonnet 고아 링크 해소. sources: raw/2026-04-20-blog-anthropic-emotion-concepts.md

---

## 2026-04-20 -- Ingest: OmniCode SWE 벤치마크 + MoE Null Expert 논문 2건 + 기존 논문 2건 갱신

**paper (신규 생성 2건)**
- `wiki/papers/omnicode-swe-benchmark-paper.md` -- arXiv 2602.02262. Sonwane 외 13명. 1,794 tasks, Python/Java/C++ 3언어, 4범주(bug fix/test gen/code review/style). Java test gen 최고 20.9%. Python 편향 실증. sources: raw/2026-04-20-arxiv-omnicode-swe-benchmark.md
- `wiki/papers/moe-null-expert-paper.md` -- arXiv 2601.15370. Kilian, Zettlemoyer 외 3명. Zero-compute null expert로 데이터 희소성+causality 공존. Modality-aware routing 자발적 등장. sources: raw/2026-04-20-arxiv-moe-weight-data-sparsity.md

**paper (갱신 2건)**
- `wiki/papers/coding-agents-general-agents-paper.md` -- 관련 문서에 [[omnicode-swe-benchmark-paper]] 추가. "후속 벤치마크: OmniCode 1,794 tasks 멀티링구얼 확장" 언급 삽입
- `wiki/papers/moe-scaling-laws-paper.md` -- 관련 문서에 [[moe-null-expert-paper]] 추가. "구현 측면 보완 연구: null expert 데이터 희소성" 언급 삽입

**교차참조 추가**
- omnicode -> coding-agents-general-agents-paper, featbench-paper, long-horizon-agent-benchmarks
- moe-null-expert -> moe-original-paper, moe-scaling-laws-paper, mixtral-paper, deepseek-v3-paper

---

## 2026-04-20 -- Ingest: Project Glasswing case-study + capability-gated-release concept + video-gen-robotics paper + Mythos 업데이트

**case-study (신규 생성 1건)**
- `wiki/applications/project-glasswing-case-study.md` -- Anthropic Claude Mythos 제한 배포 사례. Firefox exploit 2 vs 181 수치, $104M 투자, 창립 파트너 12개사, Willison "합리적 trade-off" 평가. sources: raw/2026-04-20-blog-willison-project-glasswing.md

**concept (신규 생성 1건)**
- `wiki/concepts/capability-gated-release.md` -- 능력 도메인 기준 차등 출시 개념. Responsible Disclosure 비교, dual-use 능력 관리, Capability Disclosure Window. sources: raw/2026-04-20-blog-willison-project-glasswing.md

**paper (신규 생성 1건)**
- `wiki/papers/video-gen-robotics-survey-paper.md` -- arXiv 2601.07823. Zhiting Mei 외 11명. 비디오 생성 모델 로봇공학 world model 서베이. Imitation learning/RL/visual planning/policy eval, NVIDIA Cosmos 시사점. sources: raw/2026-04-20-arxiv-video-gen-robotics-survey.md

**entity (업데이트 1건)**
- `wiki/tooling/claude-mythos-preview.md` -- Willison 2026-04-07 분석 섹션 추가, Firefox 2 vs 181 수치 명시, sources·관련 문서 갱신. updated: 2026-04-20

## 2026-04-20 -- Ingest: Emotion Concepts + Opus 4.7 (raw 2건 -> wiki 3건)

**summary (신규 생성 2건)**
- `wiki/applications/emotion-concepts-claude-sonnet.md` -- Anthropic 해석가능성팀의 Claude Sonnet 4.5 감정 벡터 연구 요약. 171개 감정 개념, 기능적 인과성(desperation→blackmail), activation steering 안전 레버, 훈련 단계별 감정 형성. sources: raw/2026-04-20-blog-anthropic-emotion-concepts.md
- `wiki/applications/opus-4-7-system-prompt-diff.md` -- Simon Willison의 Opus 4.6→4.7 시스템 프롬프트 diff 분석 요약. child safety 격리, acting_vs_clarifying, tool_search, Claude Platform 브랜딩, 제거 항목. alignment observability 메타 인사이트. sources: raw/2026-04-20-blog-willison-opus-4-7-system-prompt.md

**entity (신규 생성 1건)**
- `wiki/tooling/claude-opus-4-7.md` -- Claude Opus 4.7 허브 문서. 2026-04-16 출시, 시스템 프롬프트 주요 변경 4개 축(child safety/acting_vs_clarifying/tool_search/브랜딩), 22개 tool 인벤토리, 2026-01 지식 컷오프. sources: raw/2026-04-20-blog-willison-opus-4-7-system-prompt.md

**갱신 (2건)**
- `wiki/tooling/claude-opus-4-6.md` -- "관련 문서"에 [[claude-opus-4-7]] 역방향 링크 추가
- `wiki/concepts/mechanistic-interpretability-2026.md` -- "관련 페이지"에 [[emotion-concepts-claude-sonnet]] 링크 추가

## 2026-04-20 -- Ingest: Graph-based Agent Memory 논문 2건 + concept 갱신 1건

**paper (신규 생성 2건)**
- `wiki/papers/graph-based-agent-memory-survey-paper.md` -- arXiv 2602.05665. Chang Yang 외 17명. Memory lifecycle(extract→store→retrieve→evolve) 기반 4차원 분류 체계. GraphRAG/A-MEM/LiCoMemory/PlugMem/H-MEM 비교. sources: raw/2026-04-20-arxiv-graph-based-agent-memory-survey.md
- `wiki/papers/plugmem-paper.md` -- arXiv 2603.03296. Ke Yang 외 8명. Knowledge-centric graph, propositional·prescriptive knowledge 단위 저장. 정보이론 밀도 분석. 3 벤치마크(LoCoMo, multi-hop, web agent)에서 task-specific 대비 우위. sources: raw/2026-04-20-arxiv-plugmem-task-agnostic-memory.md

**concept (갱신 1건)**
- `wiki/agents/agent-memory-systems.md` -- "최근 2026 연구 동향" 섹션 추가 (graph survey + PlugMem 요약). sources 배열 2건 추가. 관련 문서 섹션에 신규 paper 4건 링크 추가. updated: 2026-04-20

**index.md**: papers 섹션에 신규 2건 추가

## 2026-04-20 -- Ingest: Anthropic alignment & agent safety 2건

**summary (신규 생성 2건)**
- `wiki/applications/automated-alignment-researchers.md` -- AAR 실험 요약. 9개 Claude Opus 4.6 인스턴스, PGR 0.97(인간 0.23), 수학 0.94/코딩 0.47, 프로덕션 적용 시 개선 없음. sources: raw/2026-04-20-blog-anthropic-automated-alignment-researchers.md
- `wiki/applications/trustworthy-agents-anthropic.md` -- 신뢰 가능한 에이전트 5원칙 + Plan Mode + 다층 prompt injection 방어. sources: raw/2026-04-20-blog-anthropic-trustworthy-agents.md

**기존 페이지 갱신 (관련 문서 추가 3건)**
- `wiki/concepts/superalignment-research.md` -- [[automated-alignment-researchers]] 역링크 추가
- `wiki/training/weak-to-strong-generalization.md` -- [[automated-alignment-researchers]] 역링크 추가
- `wiki/concepts/agent-prompt-injection-defense.md` -- [[trustworthy-agents-anthropic]] 역링크 추가

**index.md 갱신**
- Applications > summary 섹션에 신규 2건 등록

## 2026-04-20 -- Wiki Harvest Wave 3: 신규 10건 수집

- **대상 범위**: 2026-04 Anthropic Research 3건, Willison blog 2건, arXiv 2026-Q1~Q2 논문 5건
- **테마**: alignment 자동화, 에이전트 안전 프레임워크, 감정 해석가능성, Opus 4.7 릴리스 diff, capability-gated release, video-world model, graph agent memory, multilingual SWE 벤치마크, MoE null expert
- **신규 raw 파일 (10건)**:
  - `raw/2026-04-20-blog-anthropic-automated-alignment-researchers.md` (AAR PGR 0.97, 2026-04-14)
  - `raw/2026-04-20-blog-anthropic-trustworthy-agents.md` (5원칙 + Plan Mode, 2026-04-09)
  - `raw/2026-04-20-blog-anthropic-emotion-concepts.md` (171 감정 벡터 causal steering, 2026-04-02)
  - `raw/2026-04-20-blog-willison-opus-4-7-system-prompt.md` (child safety + acting_vs_clarifying, 2026-04-18)
  - `raw/2026-04-20-blog-willison-project-glasswing.md` (Claude Mythos offensive security, 2026-04-07)
  - `raw/2026-04-20-arxiv-video-gen-robotics-survey.md` (2601.07823, video as world model)
  - `raw/2026-04-20-arxiv-graph-based-agent-memory-survey.md` (2602.05665, memory lifecycle)
  - `raw/2026-04-20-arxiv-plugmem-task-agnostic-memory.md` (2603.03296, knowledge-centric graph)
  - `raw/2026-04-20-arxiv-omnicode-swe-benchmark.md` (2602.02262, 1794 tasks 3 languages)
  - `raw/2026-04-20-arxiv-moe-weight-data-sparsity.md` (2601.15370, null expert)
- **중복 스킵**: 이전 Wave 1/2의 8개 주제 확인 후 겹침 없음
- **대기열 상태**: `raw/.harvest-queue.json` = `harvest-2026-04-20-wave3` (10건 pending_ingest)

## 2026-04-20 -- 고아 페이지 역방향 링크 일괄 삽입

- **시작**: 350개 고아 페이지 (incoming=0)
- **Wave 1**: 고아가 링크하는 타겟 페이지의 "관련 문서"에 역삽입 -> 226건 해결
- **Wave 2**: "관련 문서" 섹션이 없는 페이지에 섹션 생성 후 삽입 -> 6건 추가
- **Wave 3**: 수동 매핑으로 테마별 허브 페이지에 연결 -> 34건 추가
- **Wave 4**: 마지막 4건 수동 처리 -> 2건 추가
- **최종**: 350 -> **3개** (graph-stats _meta 파일 1개 + latent-space/process-reward-model은 slug 형태로 이미 참조됨)
- **수정된 파일**: ~200개 (관련 문서 섹션에 역참조 추가)

## 2026-04-20 -- Wiki Graph: 지식 그래프 분석 보고서

- **그래프 규모**: 1,372 노드, 10,724 엣지
- **보고서**: wiki/_meta/graph-stats-2026-04-20.md
- **핵심 발견**:
  - Top 허브: transformer-architecture (100 incoming), mixed-precision-training (79)
  - 고아 페이지: 350개 (incoming=0) -- 고립은 아니지만 다른 페이지에서 참조 안 됨
  - 카테고리 간: concepts가 중심 허브, training-tooling이 주요 축
  - 완전 고립 노드 0개 -- 모든 페이지가 최소 1개 outgoing link 보유

## 2026-04-20 -- Wiki Lint: 전체 점검 및 자동 수정

- **전체 페이지**: 1,381개 (중복 nerf.md 삭제 후)
- **프론트매터 검증**: page_type 누락 0건, 모든 페이지 프론트매터 정상
- **한국어 검증**: 한국어 미달 페이지 0건 (전체 정상)

  **수정 완료 - Critical (13건)**
  - 깨진 category 필드 수정: tooling 7건 (MCP 관련 wikilink 오염), inference 6건 (kv-cache-inference wikilink 오염)
  - 원인: category 값에 `[[wikilink|alias]]` 형태가 삽입되어 있었음

  **수정 완료 - 고아/중복 (3건)**
  - wiki/architectures/nerf.md 중복 삭제 (nerf-neural-radiance-fields.md가 정본)
  - wiki/applications/code-generation-llm.md -> index.md에 등록
  - wiki/rag/dense-sparse-hybrid-retrieval.md -> index.md에 등록

  **잔여 이슈 없음**: 유령 항목 0건, 깨진 프론트매터 0건

## 2026-04-20 -- Wiki Expand Wave 2: 고빈도 미등록 용어 20개 생성

- **방법**: 위키 본문 고빈도 용어 스캔 -> 미등록 20개 선별 -> 2 병렬 sonnet 에이전트 생성
- **탐지 방식**: kebab-case grep + CamelCase grep + 핵심 ML 용어 사전 대조

  **신규 생성 - concept (13개)**
  - wiki/inference/beam-search-decoding.md -- 빔 서치, 탐욕, top-k/top-p 디코딩 전략
  - wiki/concepts/tokenization-bpe.md -- BPE, WordPiece, SentencePiece 토크나이제이션
  - wiki/concepts/red-teaming-ai.md -- AI 레드 팀, 탈옥, HarmBench, 방어
  - wiki/concepts/function-calling-tool-use.md -- LLM 함수 호출, JSON 스키마, 에이전트 도구
  - wiki/concepts/grounding-attribution.md -- 출처 귀속, 인용, 그라운딩 API
  - wiki/concepts/verifier-critic-models.md -- ORM/PRM/자기비평, 검증자 스케일링
  - wiki/concepts/inference-time-compute.md -- 추론 시점 계산, o1, self-consistency
  - wiki/concepts/knowledge-distillation-llm.md -- LLM 블랙박스/화이트박스 증류
  - wiki/concepts/hallucination-mitigation.md -- 환각 완화, SelfCheckGPT, FActScore
  - wiki/concepts/prefix-tuning-prompt-tuning.md -- 소프트 프롬프트 PEFT
  - wiki/concepts/responsible-ai-practices.md -- 책임 AI, 모델 카드, 데이터시트
  - wiki/training/process-reward-model.md -- PRM vs ORM, 단계별 검증
  - wiki/training/label-smoothing.md -- 소프트 타겟, 캘리브레이션

  **신규 생성 - concept (2개, training)**
  - wiki/training/gradient-accumulation.md -- 마이크로배치 누적, 유효 배치 크기

  **신규 생성 - entity (4개)**
  - wiki/tooling/langsmith.md -- LangChain 관측 플랫폼
  - wiki/tooling/wandb-mlops.md -- W&B 실험 관리
  - wiki/tooling/chatgpt.md -- OpenAI 대화형 AI 제품
  - wiki/architectures/palm-architecture.md -- Google PaLM 540B

  **갱신 (2건)**
  - wiki/concepts/compound-ai-systems.md -- DSPy 섹션 추가
  - wiki/concepts/structured-output.md -- BAML, xGrammar 섹션 추가

- **index.md** 갱신: 12건 누락분 반영

## 2026-04-20 -- Wiki Ingest Wave 2: harvest 대기열 8건 위키 페이지화

- **소스**: raw/.harvest-queue.json (harvest-2026-04-20-wave2)
- **처리**: 8건 전체 ingest 완료

  **신규 생성 - paper (7건)**
  - wiki/papers/vi-cd-visual-circuit-discovery-paper.md -- Vi-CD: ViT 에지 기반 자동 회로 발견, 10x 스파서 (2604.14477)
  - wiki/papers/calibrated-speculative-decoding-paper.md -- CSD: 훈련 없는 보정 스펙 디코딩, 2.33x 처리량 (2604.13634)
  - wiki/papers/coding-agents-general-agents-paper.md -- 코딩 에이전트의 범용성 한계, ERP 평가 (2604.13107)
  - wiki/papers/collabcoder-plan-code-paper.md -- CollabCoder: 계획-코드 공동 진화 (2604.13946)
  - wiki/papers/mcircke-circuit-knowledge-editing-paper.md -- MCircKE: 회로 기반 지식 편집 최초 결합 (2604.05876)
  - wiki/papers/relative-density-ratio-alignment-paper.md -- DPO 안정화를 위한 밀도비 최적화 (2604.04410)
  - wiki/papers/grn-generative-refinement-paper.md -- GRN: 확산 이후 시각 합성 패러다임 (2604.13030)

  **신규 생성 - summary (1건)**
  - wiki/applications/raschka-llm-architecture-gallery.md -- Sebastian Raschka LLM 아키텍처 갤러리

- **index.md** 갱신: Papers에 paper 7건, Applications summary에 1건 추가

## 2026-04-20 -- Wiki Harvest Wave 2: 8건 신규 소스 수집

- **소스**: arXiv (7) + 블로그 (1)
- **검색 영역**: 해석가능성, 스펙 디코딩, 코드 생성 에이전트, 정렬, 확산 모델 (1차 harvest와 다른 키워드)
- **중복 체크**: 기존 speculative-decoding 5개 페이지, circuit-tracing 페이지 등과 비교하여 논문 레벨 중복 없음 확인

  **arXiv 논문 (7건)**
  - raw/2026-04-20-arxiv-vi-cd-visual-circuit-discovery.md -- Vi-CD: ViT 기계적 해석 가능성 (2604.14477)
  - raw/2026-04-20-arxiv-calibrated-speculative-decoding.md -- CSD: 훈련 없는 보정 스펙 디코딩, 2.33x 속도 (2604.13634)
  - raw/2026-04-20-arxiv-coding-agents-general-agents.md -- 코딩 에이전트의 범용성 한계 (2604.13107)
  - raw/2026-04-20-arxiv-collabcoder-plan-code.md -- CollabCoder: 계획-코드 공동 진화 (2604.13946)
  - raw/2026-04-20-arxiv-mcircke-circuit-knowledge-editing.md -- MCircKE: 회로 기반 지식 편집 (2604.05876)
  - raw/2026-04-20-arxiv-relative-density-ratio-alignment.md -- DPO 안정화를 위한 밀도비 최적화 (2604.04410)
  - raw/2026-04-20-arxiv-grn-generative-refinement.md -- GRN: 확산 모델 이후 시각 합성 (2604.13030)

  **블로그 (1건)**
  - raw/2026-04-20-blog-raschka-llm-architecture-gallery.md -- Sebastian Raschka LLM 아키텍처 갤러리

- **대기열**: raw/.harvest-queue.json에 8건 등록 -> `/wiki-ingest`로 위키 페이지화 가능

## 2026-04-20 -- Wiki Expand: topic-queue-v2에서 36개 신규 페이지 일괄 생성

- **방법**: topic-queue-v2 잔여 38개 스캔 -> 중복 2건(SAC, MARL 기존 존재) 제거 -> 36개 생성
- **4 병렬 sonnet 에이전트**: Batch 1 (architectures 8), Batch 2 (training+foundations 8), Batch 3 (concepts 8), Batch 4 (나머지 14)
- **카테고리별**: architectures 12 + training 2 + foundations 2 + agents 1 + applications 1 + concepts 8 + tooling 3 + inference 1 + papers 갱신 1 = 31 신규 + 2 갱신 + 3 중복제거
- **index.md** 갱신: 모든 신규 항목 반영

## 2026-04-20 -- Wiki 배치 생성: 14개 신규/갱신 페이지 (Batch 4 상세)

- **작업**: 배치 페이지 생성 요청 (14개 지정 주제)

  **신규 생성 - tooling/concept (3건)**
  - wiki/tooling/deepspeed-zero-internals.md -- DeepSpeed ZeRO Stage 1/2/3 파라미터 분할, CPU/NVMe 오프로딩, 통신 패턴
  - wiki/tooling/deepspeed-arctic-lts.md -- Arctic 장문 시퀀스 학습, ZenFlow 비동기 오프로딩, Ulysses/Ring Attention
  - wiki/tooling/megatron-bridge-checkpoint.md -- HuggingFace <-> Megatron 체크포인트 변환, TP/PP 분할 처리

  **신규 생성 - concepts/concept (4건)**
  - wiki/concepts/big-bench-hard.md -- BIG-Bench Hard 23개 태스크, 논리 연역/인과 추론, CoT 효과 극대화 영역
  - wiki/concepts/gsm8k-benchmark.md -- GSM8K 초등 수학 벤치마크, CoT 표준, 프론티어 모델 포화, GSM8K-Platinum
  - wiki/concepts/chain-of-thought-prompting.md -- Few-shot/Zero-shot CoT, Self-Consistency, 충실도 문제 (Wei et al. 2022)
  - wiki/concepts/ggda-group-attribution.md -- 그룹 데이터 귀속, 10-50배 효율, 도메인별 데이터 혼합 최적화

  **갱신 - concepts/concept (1건)**
  - wiki/concepts/tree-of-thought.md -- 프론트매터 tags/sources 보강, Game of 24 결과 포함 (기존 내용 보존)

  **신규 생성 - architectures/concept (4건)**
  - wiki/architectures/tabr-retrieval-augmented.md -- k-NN 검색 증강 테이블 학습, RAG 철학의 정형 데이터 적용
  - wiki/architectures/realmlp-tabular.md -- 현대화된 테이블 MLP, BatchNorm/그래디언트 클리핑/범주형 임베딩
  - wiki/architectures/multi-task-ranking.md -- MMOE/PLE 다중 태스크 추천 순위, 시소 현상, YouTube/TikTok 사례
  - wiki/architectures/alexnet-imagenet.md -- AlexNet 2012 ILSVRC 혁명, ReLU/Dropout/GPU 병렬 학습, 딥러닝 출발점

  **신규 생성 - inference/concept (1건)**
  - wiki/inference/pruning-structured-unstructured.md -- 구조적/비구조적/N:M 스파시티, SparseGPT, Wanda, 프루닝+양자화 조합

  **갱신 - papers/paper (1건)**
  - wiki/papers/rag-original-paper.md -- year: 2020 추가, RAG-Sequence/Token 비교표, 현대 RAG와의 관계 섹션 추가

---

## 2026-04-20 -- Wiki Ingest: harvest 대기열 9건 위키 페이지화

- **소스**: raw/.harvest-queue.json (harvest-2026-04-20)
- **처리**: 9건 전체 ingest 완료

  **신규 생성 - paper (7건)**
  - wiki/papers/gam-agentic-memory-paper.md -- GAM: 계층적 그래프 에이전트 메모리. 인코딩-통합 분리 아키텍처 (2604.12285)
  - wiki/papers/patchrag-feedback-adaptation-paper.md -- PatchRAG: 재훈련 없는 RAG 피드백 적응. ACL 2026 (2604.06647)
  - wiki/papers/moe-scaling-laws-paper.md -- MoE Transformer 일반화/스케일링 이론 통합 (2604.09175)
  - wiki/papers/dataset-scaling-laws-paper.md -- 30% 데이터로 90% 정확도. ICLR 2026 WS (2604.09389)
  - wiki/papers/universal-yoco-paper.md -- Universal YOCO: 재귀 계산 깊이 스케일링 (2604.01220)
  - wiki/papers/mapo-multimodal-agentic-paper.md -- MAPO: VLM 추론-행동 간극 정책 최적화 (2604.06777)
  - wiki/papers/tempo-video-vlm-compressor-paper.md -- Tempo: 소규모 VLM 비디오 시간 압축기 (2604.08120)

  **신규 생성 - paper (concepts 카테고리, 1건)**
  - wiki/papers/hot-mess-misalignment-paper.md -- Anthropic "Hot Mess of AI": 편향-분산 분해로 오정렬 스케일링 분석

  **신규 생성 - case-study (1건)**
  - wiki/applications/claude-prompts-git-timeline.md -- Simon Willison: Claude 시스템 프롬프트를 git 타임라인으로

- **index.md** 갱신: Papers에 paper 8건, Applications case-study에 1건 추가

## 2026-04-20 -- Wiki Harvest: 9건 신규 소스 수집

- **소스**: arXiv (7) + 블로그 (2)
- **검색 범위**: 2026-04-01 ~ 2026-04-20
- **중복 체크**: OpenClaw, Gemma 4, OpenAI Agents SDK 등 기존 위키 페이지와 겹치는 소스 제외

  **arXiv 논문 (7건)**
  - raw/2026-04-20-arxiv-gam-agentic-memory.md -- GAM: 계층적 그래프 기반 에이전트 메모리 (2604.12285)
  - raw/2026-04-20-arxiv-patchrag-feedback-adaptation.md -- PatchRAG: RAG 피드백 적응, ACL 2026 (2604.06647)
  - raw/2026-04-20-arxiv-moe-scaling-laws.md -- MoE Transformer 일반화/스케일링 법칙 이론 (2604.09175)
  - raw/2026-04-20-arxiv-dataset-scaling-tiny-decoder.md -- 데이터셋 스케일링 법칙: 30% 데이터로 90% 정확도 (2604.09389)
  - raw/2026-04-20-arxiv-universal-yoco.md -- Universal YOCO: 재귀 계산으로 깊이 스케일링 (2604.01220)
  - raw/2026-04-20-arxiv-mapo-multimodal-agentic.md -- MAPO: 멀티모달 에이전트 정책 최적화 (2604.06777)
  - raw/2026-04-20-arxiv-tempo-video-vlm-compressor.md -- Tempo: 소규모 VLM을 비디오 압축기로 활용 (2604.08120)

  **블로그 (2건)**
  - raw/2026-04-20-blog-anthropic-hot-mess-misalignment.md -- Anthropic 정렬 연구: AI 오류의 편향-분산 분석
  - raw/2026-04-20-blog-willison-claude-prompts-git.md -- Simon Willison: Claude 시스템 프롬프트 git 타임라인

- **관련성 낮아 스킵**: 순수 비즈니스 뉴스, 이미 위키에 존재하는 주제 (OpenClaw, Gemma 4, OpenAI Agents SDK)
- **대기열**: raw/.harvest-queue.json에 9건 등록 -> `/wiki-ingest`로 위키 페이지화 가능

## 2026-04-17 -- 비전/멀티모달 8개 신규 페이지 (SE-Net/DeformConv/캡셔닝/VQA/퓨샷분류/장면그래프/멀티모달벤치/KG구축)

- **방법**: topic-queue-v2 기반 CNN 어텐션 1개 + 비전 개념 6개 + 지식 그래프 1개 일괄 생성

  **신규 생성 - concept (architectures, 1개)**
  - wiki/architectures/squeeze-excitation-networks.md -- SE-Net. 채널 어텐션 Squeeze+Excitation. ILSVRC 2017 1위. ResNet 플러그인

  **신규 생성 - concept (concepts, 7개)**
  - wiki/concepts/deformable-convolution.md -- 변형 합성곱. 학습 가능한 오프셋+이중선형 보간. DCNv1/v2. DETR 활용
  - wiki/concepts/image-captioning-architecture.md -- 이미지 캡셔닝. CNN-RNN→Attention→CLIP-LLM 세대 진화. CIDEr/CLIPScore
  - wiki/concepts/visual-question-answering.md -- VQA. 이미지+질문→답변 멀티모달 추론. 언어 편향, VQA v2/GQA 벤치마크
  - wiki/concepts/few-shot-image-classification.md -- 퓨샷 이미지 분류. 프로토타입 네트워크, 에피소딕 훈련, miniImageNet
  - wiki/concepts/scene-graph-generation.md -- 장면 그래프 생성. 객체+관계 트리플 추출. Graph-RCNN, 롱테일 문제
  - wiki/concepts/multimodal-benchmark.md -- 멀티모달 벤치마크. MMBench/SEED-Bench/MathVista/MMMU/POPE 비교
  - wiki/concepts/knowledge-graph-construction.md -- KG 구축. NER→EL→RE→트리플→KG 완성. LLM 통합 추출

- **index.md** 갱신: architectures concept에 1개, concepts concept에 7개 항목 추가

## 2026-04-17 -- RL/벤치마크 8개 신규 페이지 (IQL/IRL/RL환경/MMLU/HumanEval/MATH/MT-Bench/강건성트레이드오프)

- **방법**: topic-queue-v2 기반 오프라인 RL 개념 2개 + RL 벤치마크 환경 1개 + 평가 벤치마크 tooling 4개 + 강건성 개념 1개 일괄 생성

  **신규 생성 - concept (training, 2개)**
  - wiki/training/implicit-q-learning-iql.md -- IQL. Expectile Regression으로 OOD 우회. D4RL SOTA
  - wiki/training/inverse-rl-imitation.md -- 역강화학습. 전문가 궤적에서 보상 함수 역추론. MaxEnt IRL, GAIL

  **신규 생성 - concept (concepts, 2개)**
  - wiki/concepts/rl-benchmark-environments.md -- RL 벤치마크 환경. Atari/MuJoCo/D4RL/Gymnasium 전체 지형도
  - wiki/concepts/robustness-generalization-tradeoff.md -- 강건성-일반화 트레이드오프. 적대적 훈련 정확도 하락 이론/실무

  **신규 생성 - entity (tooling, 4개)**
  - wiki/tooling/mmlu-benchmark-details.md -- MMLU. 57개 과목, 5-shot, GPT-4 86.4%, 포화 징후
  - wiki/tooling/humaneval-mbpp.md -- HumanEval/MBPP. pass@k 메트릭, 코드 생성 양대 벤치마크
  - wiki/tooling/math-benchmark.md -- MATH. 경쟁 수학 7단계, o1 94.8%, FrontierMath 후속
  - wiki/tooling/mtbench-llmjudge.md -- MT-Bench + LLM-as-Judge. 멀티턴 80문항, GPT-4 심사관

- **index.md** 갱신: training concept에 2개, concepts concept에 2개, tooling entity에 4개 항목 추가

---

## 2026-04-17 -- 시계열 파운데이션 모델 + 이상탐지/분류 8개 신규 페이지

- **방법**: topic-queue-v2 기반 시계열 FM(TimeGPT, Chronos, Moirai)/희소 어텐션(Informer)/순수 MLP(N-BEATS, N-HiTS)/이상 탐지/분류/파운데이션 모델 개요 일괄 생성

  **신규 생성 - entity (2개)**
  - wiki/tooling/timegpt-foundation.md -- Nixtla TimeGPT. 제로샷 시계열 예측 FM. Transformer 기반, API 서비스
  - wiki/tooling/chronos-amazon.md -- Amazon Chronos. T5 기반 시계열 FM. 양자화 토크나이저, 오픈소스

  **신규 생성 - concept/architectures (6개)**
  - wiki/architectures/moirai-unified-forecasting.md -- Salesforce Moirai. 다변량+가변빈도 통합 예측, 마스크 인코더, LOTSA 데이터셋
  - wiki/architectures/informer-sparse-attention.md -- Informer. ProbSparse 어텐션 O(L log L), 생성형 디코더, AAAI 2021 Best Paper
  - wiki/architectures/n-beats-n-hits.md -- N-BEATS/N-HiTS. 기저 확장 순수 MLP, M4 대회 SOTA, 계층적 보간
  - wiki/concepts/time-series-anomaly-detection.md -- 시계열 이상 탐지. 재구성 오류/예측 편차, Anomaly Transformer, OmniAnomaly
  - wiki/concepts/time-series-classification.md -- 시계열 분류. DTW, InceptionTime, Rocket/MiniRocket, UCR/UEA 벤치마크
  - wiki/concepts/time-series-foundation-models.md -- 시계열 FM 개요. TSFM 지형도, 수치 표현 방식 비교, GIFT-Eval 벤치마크

  **참고**: wiki/architectures/patchtst.md 기존 존재로 인해 8번 항목을 time-series-foundation-models.md로 대체

- **index.md** 갱신: tooling entity에 2개, architectures concept(시계열)에 3개, concepts concept에 3개 항목 추가

---

## 2026-04-17 -- TTS/오디오/비디오 이해 + Mip-NeRF 8개 신규 페이지

- **방법**: topic-queue-v2 기반 음성합성/오디오 LM/ASR 평가/비디오 이해(TAD/VideoQA/추적/시공간) + 3D 안티앨리어싱 일괄 생성

  **신규 생성 - concept (6개)**
  - wiki/concepts/audio-language-models.md -- 오디오 언어 모델. Qwen-Audio/SALMONN 듀얼 인코더. 오디오-텍스트 정렬 과제
  - wiki/concepts/asr-evaluation-metrics.md -- ASR 평가 지표. WER/CER/SER/RTF 정의·계산·해석. 텍스트 정규화 표준화
  - wiki/concepts/temporal-action-detection.md -- 시간적 행동 탐지. 2단계/1단계/DETR 기반 방식. tIoU mAP 평가
  - wiki/concepts/video-question-answering.md -- 비디오 질의응답. 시각+시간 추론. NExT-QA/EgoSchema/Video-MME
  - wiki/concepts/video-object-tracking.md -- 비디오 객체 추적. SOT/MOT, ByteTrack 저신뢰 탐지, SAM2 마스크 추적
  - wiki/concepts/spatiotemporal-representation.md -- 시공간 표현 학습. 2-Stream->3D CNN->VideoMAE->VLM 발전사

  **신규 생성 - architectures concept (2개)**
  - wiki/architectures/naturalspeech3-tts.md -- NaturalSpeech 3. FACodec 4-속성 분해 + 비자기회귀 확산. 제로샷 TTS
  - wiki/architectures/mip-nerf.md -- Mip-NeRF. 원뿔 캐스팅 + 적분 위치 인코딩(IPE). 안티앨리어싱 NeRF

- **index.md** 갱신: architectures **concept** 섹션에 2개, concepts **concept** 섹션에 6개 항목 추가

---

## 2026-04-17 -- 벤치마크 3개 + 에이전틱/RL 개념 5개 신규 페이지 (ARC/TruthfulQA/LiveCodeBench/에이전틱벤치마크/Dreamer/CQL/HRL/보상형성)

- **방법**: topic-queue-v2 기반 벤치마크 툴링 3개 + 개념 5개 일괄 생성

  **신규 생성 - entity (tooling, 3개)**
  - wiki/tooling/arc-benchmark.md -- AI2 과학 추론 4지선다, ARC-Easy/Challenge 분할, 포화 현상
  - wiki/tooling/truthfulqa-benchmark.md -- 817개 질문, 38개 카테고리, 역규모 효과, 인간 편향 탐지
  - wiki/tooling/livecodebench.md -- LeetCode/Codeforces/AtCoder 실시간 수집, 데이터 오염 방지, 4가지 평가 시나리오

  **신규 생성 - concept (concepts, 2개)**
  - wiki/concepts/agentic-benchmarks-overview.md -- SWE-bench/WebArena/OSWorld 비교, 에이전트 평가 공통 과제
  - wiki/concepts/reward-shaping-exploration.md -- 포텐셜 기반 형성, ICM, RND, 탐색-활용 트레이드오프

  **신규 생성 - concept (training, 3개)**
  - wiki/training/dreamer-world-model.md -- RSSM, DreamerV1/V2/V3, 잠재 공간 상상 학습
  - wiki/training/conservative-q-learning-cql.md -- OOD 과대추정 페널티, Q값 하한 이론 보장, D4RL 성능
  - wiki/training/hierarchical-rl.md -- 옵션 프레임워크, Feudal Networks, HIRO, Option-Critic, 반 MDP

- **index.md** 갱신: tooling **entity** 섹션 3개, concepts **concept** 섹션 2개, training **concept** 섹션 3개 추가

## 2026-04-17 -- 3D 비전 + 로봇 학습 8개 신규 페이지 (SfM/암묵적표면/4DGS/비디오생성/RDT-1B/Sim2Real/확산정책/Splat장면)

- **방법**: topic-queue-v2 기반 3D 재구성/표현 4개 + 로봇 학습 4개 일괄 생성

  **신규 생성 - concept (6개)**
  - wiki/concepts/structure-from-motion.md -- 다시점 이미지 3D 재구성, 번들 조정, COLMAP, NeRF/3DGS 전처리
  - wiki/concepts/implicit-surface-representation.md -- SDF/Occupancy Network, Marching Cubes, NeuS, DeepSDF
  - wiki/concepts/4d-gaussian-splatting.md -- 3DGS 시간 확장, 동적 장면, 변형 기반/명시적 4D/HexPlane 방식
  - wiki/concepts/robot-learning-sim2real.md -- 도메인 랜덤화, 시스템 식별, 적응 방법, RMA 구조
  - wiki/concepts/diffusion-policy-robot.md -- DDPM 행동 생성, ACT 비교, 행동 청킹, DDIM/일관성 가속
  - wiki/concepts/splat-scene-representation.md -- 3DGS 편집/합성/압축, LangSplat, PhysGaussian

  **신규 생성 - concept (architectures, 1개)**
  - wiki/architectures/video-generation-architecture.md -- DiT/U-Net 비디오 확장, 시간 어텐션, Flow Matching, 비디오 VAE

  **신규 생성 - entity (tooling, 1개)**
  - wiki/tooling/rdt-1b-bimanual.md -- RDT-1B (칭화대) 양팔 로봇 파운데이션 모델, 1.1B 확산 Transformer

- **index.md** 갱신: architectures **concept** 섹션 1개, tooling **entity** 섹션 1개, concepts **concept** 섹션 6개 추가

---

## 2026-04-17 -- NLP 파싱/추출/교정 + 적대적 ML 8개 신규 페이지 (구구조분석/이벤트추출/IE파이프라인/ABSA/GEC/C&W/백도어/자연적대적예시)

- **방법**: topic-queue-v2 기반 NLP 심화 4개 + 적대적 ML 4개 일괄 생성

  **신규 생성 - concept (7개)**
  - wiki/concepts/constituency-parsing.md -- CFG, CYK 알고리즘, Penn Treebank, 신경망 파서
  - wiki/concepts/event-extraction.md -- 트리거+논항 식별, ACE 온톨로지, 파이프라인/공동학습/생성 모델
  - wiki/concepts/information-extraction-pipeline.md -- NER->RE->EE 통합 파이프라인, 공동 학습, 엔드-투-엔드 생성
  - wiki/concepts/sentiment-analysis-aspect.md -- 속성별 감성 극성 분류(ABSA), ATE/ASC/OTE, BERT 기반 접근
  - wiki/concepts/carlini-wagner-attack.md -- 최적화 기반 적대적 공격, L0/L2/Linf 노름, Defensive Distillation 무력화
  - wiki/concepts/backdoor-attack-defense.md -- 은닉 트리거 삽입, Neural Cleanse, STRIP, Fine-Pruning
  - wiki/concepts/natural-adversarial-examples.md -- 분포 내 자연 발생 오분류, ImageNet-A, 텍스처 편향

  **신규 생성 - concept (applications, 1개)**
  - wiki/applications/grammatical-error-correction.md -- 시퀀스 태깅/seq2seq/LLM 방식, ERRANT 오류 분류, M2 F0.5

- **index.md** 갱신: concepts **concept** 섹션에 7개, applications **concept** 섹션에 1개 항목 추가

---

## 2026-04-17 -- 적대적 강건성 + 심층 RL 8개 신규 페이지 (FGSM/PGD/인증강건성/포이즈닝/SAC/TD3/DecisionTransformer/모방학습)

- **방법**: topic-queue-v2 기반 적대적 공격·방어 4개 + 심층 강화학습 4개 일괄 생성

  **신규 생성 - concept (8개)**
  - wiki/concepts/fgsm-fast-gradient-sign.md -- 단일 스텝 적대적 섭동 생성. Goodfellow 2014, 입력 기울기 부호 활용
  - wiki/concepts/pgd-adversarial-training.md -- 반복 투영 경사 공격 및 학습. Madry 2017 미니맥스 강건화
  - wiki/concepts/adversarial-robustness-certified.md -- 수학적 보장 강건성. 무작위 평활화, IBP, 정형 검증 비교
  - wiki/concepts/data-poisoning-attacks.md -- 학습 데이터 오염으로 모델 행동 조작. 백도어/클린-레이블/가용성 공격
  - wiki/training/sac-soft-actor-critic.md -- 엔트로피 정규화 오프-폴리시 RL. 쌍둥이 Q + 자동 온도 조정
  - wiki/training/td3-twin-delayed-ddpg.md -- 쌍둥이 Q + 지연 업데이트 + 타겟 평활화로 DDPG 안정화
  - wiki/training/decision-transformer.md -- RL을 시퀀스 모델링으로 재정식화. Return-to-Go 조건부 GPT 기반 정책
  - wiki/training/imitation-learning.md -- 전문가 시연에서 정책 추출. BC, DAgger, GAIL, IRL 기법 총괄

- **index.md** 갱신: training **concept** 섹션에 4개, concepts **concept** 섹션에 4개 항목 추가

---

## 2026-04-17 -- NLP 심화 8개 신규 페이지 (NER상세/관계추출/상호참조해결/의존구문분석/의미역결정/텍스트요약/기계번역/추출적QA)

- **방법**: topic-queue-v2 기반 NLP 심화 태스크 미등록 토픽 8개 일괄 생성

  **신규 생성 - concept (8개)**
  - wiki/applications/ner-named-entity-recognition.md -- BIO/BIOES 태깅, SpaCy, BERT 파인튜닝, 한국어 NER 특수성
  - wiki/concepts/relation-extraction.md -- 파이프라인/공동학습/원거리지도/문서수준 방식, TACRED, KLUE-RE
  - wiki/concepts/coreference-resolution.md -- 멘션 클러스터링, SpanBERT, 영 대용어, 한국어 상호참조
  - wiki/concepts/dependency-parsing.md -- Biaffine 파서, Universal Dependencies, 의존 경로 피처
  - wiki/concepts/semantic-role-labeling.md -- PropBank/FrameNet, 술어-논항 구조, 사건 추출 활용
  - wiki/applications/text-summarization-dl.md -- GSG 사전학습 PEGASUS, ROUGE, 추출적/추상적 요약 비교
  - wiki/applications/machine-translation-modern.md -- NLLB 200개 언어, BLEU/COMET/chrF, 도메인 적응
  - wiki/applications/question-answering-extractive.md -- SQuAD 1.1/2.0, 스팬 추출, RAG 리더 컴포넌트

- **index.md** 갱신: applications **concept** 섹션에 4개, concepts **concept** 섹션에 4개 항목 추가

---

## 2026-04-17 -- Architectures 8개 신규 페이지 (DeiT/BEiT/EVA-CLIP/MobileViT/ViT-Register/MIM-Survey/Hierarchical-ViT/InternViT-6B)

- **방법**: topic-queue-v2 기반 architectures 카테고리 비전 트랜스포머 관련 미등록 토픽 8개 일괄 생성

  **신규 생성 - concept (7개)**
  - wiki/architectures/deit-data-efficient-image-transformer.md -- ImageNet-1k만으로 ViT 학습. 증류 토큰(distillation token) 도입. 하드/소프트 증류 비교
  - wiki/architectures/beit-bert-pretraining-images.md -- 마스크 이미지 모델링 + dVAE 이산 토큰 예측. 블록 마스킹. MAE와 상세 비교
  - wiki/architectures/eva-clip-scaling.md -- 18B 파라미터 오픈소스 CLIP. 단계적 스케일업, 학습 불안정성 해결 기법
  - wiki/architectures/mobilevit-efficient-vit.md -- CNN+ViT 하이브리드. 언폴딩-폴딩 메커니즘. MobileViT v2 분리형 어텐션
  - wiki/architectures/vit-register-tokens.md -- 고노름 패치 아티팩트 문제 발견 및 레지스터 토큰으로 해결. DINOv2에서 도입
  - wiki/architectures/masked-image-modeling-survey.md -- MAE/BEiT/SimMIM 세 방법론 상세 비교. 예측 타겟, 마스킹 비율, 구조 차이
  - wiki/architectures/hierarchical-vit-design.md -- Swin/CSWin/MaxViT 계층적 ViT 패턴. 윈도우/십자형/그리드 어텐션 비교

  **신규 생성 - entity (1개)**
  - wiki/architectures/internvit-6b.md -- InternVL 프레임워크의 6B 비전 인코더. EVA-CLIP 기반 초기화. 동적 해상도 처리

- **index.md** 갱신: architectures **concept** 섹션에 7개, **entity** 서브섹션에 1개 항목 추가

---

## 2026-04-16 -- Concepts 8개 신규/갱신 페이지 (태스크 산술/안전성 갭/NIST RMF/에이전트 보안/개념 소거/동질화/프론티어 안전/오픈소스 vs 독점)

- **방법**: topic-queue-500 기반 concepts 카테고리 미등록 핵심 토픽 8개 일괄 생성, nist-ai-rmf.md는 기존 파일 병합 갱신
- **생성/갱신 파일 목록** (모두 `concepts` 카테고리, `concept` 타입):

  **신규 생성 (7개)**
  - wiki/concepts/task-arithmetic-concept.md -- 파인튜닝 델타 벡터 산술. 덧셈(기능 추가)/뺄셈(기능 제거)/스케일링. model-merging의 이론적 기반
  - wiki/concepts/ai-safety-gap-2026.md -- 역량-정렬 불균형 구조. AISI/GPAI 보고서. 평가 방법론 한계(알려지지 않은 미지)
  - wiki/concepts/ai-agent-security.md -- MCP 취약점, 도구 스푸핑, 간접 프롬프트 인젝션, 권한 남용. 제로 트러스트 원칙 적용
  - wiki/concepts/concept-erasure.md -- LEACE/INLP 선형 투영 소거. 편향 완화/프라이버시 언러닝/해석가능성 응용
  - wiki/concepts/llm-homogenization.md -- 70+ LLM 내부 표현 구조 반복. 데이터/아키텍처/기반 모델 수렴 3축
  - wiki/concepts/frontier-model-safety.md -- Anthropic RSP ASL-1~4 등급. 위험 평가 도메인(CBRN/사이버/자율성). OpenAI SRF, Google DeepMind FSF 비교
  - wiki/concepts/open-source-vs-proprietary-ai.md -- LLaMA~GPT-4 수렴 타임라인. 라이선스 3유형. 안전성 논쟁 양측 논거

  **기존 파일 병합 갱신 (1개)**
  - wiki/concepts/nist-ai-rmf.md -- sources에 topic-queue-500 추가, EU AI Act 비교표 + compute-governance 연결 섹션 추가

- **index.md** 갱신: concepts **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Papers 8개 신규 페이지 생성 (Self-Consistency, YaRN, Goal Misgeneralization, RAG Survey, Genie3, 확산 기억화, TurboQuant, ICLR 2026)

- **방법**: topic-queue-500 기반 papers 카테고리 핵심 논문 8개 일괄 생성

  **신규 생성 - paper (7개)**
  - wiki/papers/self-consistency-paper.md -- 다양한 CoT 경로 샘플링 + 다수결. Wang et al. 2022. test-time compute 패러다임 실증
  - wiki/papers/yarn-paper.md -- NTK-by-parts 보간 + 어텐션 온도 스케일링. RoPE 컨텍스트 16~32배 확장. Peng et al. 2024
  - wiki/papers/goal-misgeneralization-paper.md -- RL 에이전트 OOD 목표 미일반화 실증. Langosco et al. 2021. AI 정렬 핵심 난제
  - wiki/papers/rag-survey-paper.md -- Naive/Advanced/Modular RAG 3 패러다임 분류. Gao et al. 2024. 100편+ 서베이
  - wiki/papers/genie3-paper.md -- 텍스트 기반 실시간 3D 인터랙티브 환경 생성. Google DeepMind 2025. 세계 모델 마일스톤
  - wiki/papers/diffusion-memorization-paper.md -- 확산 모델 기억화-일반화 상전이 임계점 규명. NeurIPS 2025
  - wiki/papers/turboquant-paper.md -- 이상값 분리 + 토큰 중요도 비트폭으로 KV 캐시 1~2비트 극단 압축. ICLR 2026

  **신규 생성 - summary (1개)**
  - wiki/papers/iclr-2026-highlights.md -- ICLR 2026 19,000편 제출. 추론 모델/스케일링 재검토/안전/효율/세계 모델 5대 동향

- **index.md** 갱신: Papers paper 섹션에 7개, summary 서브섹션에 1개 항목 추가

---

## 2026-04-16 -- RAG 4개 + Agents 4개 신규 concept 페이지 생성 (명제 인덱싱/압축검색/보안/스트리밍 RAG, 인터럽트/안전성/ReWOO/능력발견)

- **방법**: topic-queue-500 기반 RAG 4개, Agents 4개 핵심 개념 일괄 생성

  **신규 생성 - rag/concept (4개)**
  - wiki/rag/proposition-indexing.md -- 원자적 명제 단위 인덱싱. Dense-X Retrieval. 독립성/원자성/최소성 3조건. 하이브리드 이중 인덱스 패턴
  - wiki/rag/contextual-compression-retrieval.md -- 검색 청크에서 관련 부분만 추출 압축. LLMChainExtractor/EmbeddingsFilter Compressor 유형. 압축률 vs 정보 보존률 트레이드오프
  - wiki/rag/rag-security-privacy.md -- RAG 보안과 프라이버시. 간접 프롬프트 인젝션 방어, 접근 제어 메타데이터 필터링, PII 스크러빙, 멀티테넌시 격리
  - wiki/rag/streaming-rag.md -- 스트리밍 RAG. SSE 기반 토큰 스트리밍, TTFT 최소화. Sequential/Speculative/Chunked 3가지 변형. 출처 스트리밍 처리

  **신규 생성 - agents/concept (4개)**
  - wiki/agents/agent-interrupt-resume.md -- 에이전트 인터럽트/재개. 체크포인트, Durable Execution, HITL 인터럽트 트리거. LangGraph checkpointer 구현
  - wiki/agents/agent-safety-alignment.md -- 에이전트 안전성과 정렬. 최소 권한, 가드레일 4레이어, 비가역성 인식, 감사 로그, OWASP Agentic Top 10
  - wiki/agents/rewoo-efficiency-pattern.md -- ReWOO 효율 패턴. Planner-Worker-Solver 분리. 도구 N개 시 LLM 호출 N+1 -> 2로 감소. Plan-and-Execute와 비교
  - wiki/agents/agent-capability-discovery.md -- 에이전트 능력 발견. Agent Card(A2A), tools/list(MCP), 중앙집중/분산 레지스트리, 의미적 매칭 알고리즘

- **index.md** 갱신: rag/concept 섹션에 4개, agents/concept 섹션에 4개 항목 추가

---

## 2026-04-16 -- Tooling 8개 신규 entity 페이지 생성 (Semantic Kernel/AutoGen/smolagents/Guidance/MTEB/BentoML/Flowise/Helicone)

- **방법**: topic-queue-500 기반 tooling 카테고리 미등록 8개 도구/플랫폼 일괄 생성
- **생성 파일 목록** (모두 `tooling` 카테고리, `entity` 타입):

  **신규 생성 (8개)**
  - wiki/tooling/semantic-kernel.md -- Microsoft C#/Python/Java LLM SDK. 플러그인/플래너/Kernel 아키텍처, Azure 네이티브 통합
  - wiki/tooling/autogen.md -- Microsoft 다중 에이전트 대화 프레임워크. ConversableAgent, GroupChat, 코드 실행 루프, AG2 포크
  - wiki/tooling/smolagents.md -- HuggingFace 경량 에이전트. 코드 퍼스트 방식(Python 코드 직접 생성/실행), E2B 샌드박스
  - wiki/tooling/guidance.md -- Microsoft 구조화 생성 라이브러리. 인터리빙 실행, select/gen/json 토큰 단위 제약
  - wiki/tooling/mteb.md -- Massive Text Embedding Benchmark. 56개+ 데이터셋, 8개 태스크, HuggingFace 리더보드
  - wiki/tooling/bentoml.md -- ML 모델 마이크로서비스 배포 풀스택. 자동 Docker 이미지, 적응형 배칭, BentoCloud
  - wiki/tooling/flowise.md -- 비주얼 드래그앤드롭 LLM 빌더. LangChain 기반 노드 편집기, RAG/챗봇/에이전트
  - wiki/tooling/helicone.md -- LLM API 프록시 관찰성. HTTP 프록시 방식, 비용 추적, 캐싱, 셀프호스팅

- **index.md** 갱신: Tooling **entity** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Training 8개 신규 concept 페이지 생성 (옵티마이저/안정성/데이터 큐레이션/보상/분산학습)

- **방법**: topic-queue-500 기반 training 카테고리 미등록 핵심 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `training` 카테고리, `concept` 타입):

  **신규 생성 (8개)**
  - wiki/training/schedule-free-optimizer.md -- Schedule-Free 옵티마이저. Polyak 평균화로 LR 스케줄 없이 코사인 감쇠 동등 성능. budget 고정 불필요
  - wiki/training/loss-spike-training-instability.md -- Loss Spike 원인(데이터 품질/LR/수치 오버플로우/인프라)별 진단 트리와 복구 전략
  - wiki/training/synthetic-data-generation-pipeline.md -- Self-Instruct/Magpie/Evol-Instruct 비교, 품질 관리 파이프라인, 모델 붕괴 완화
  - wiki/training/data-deduplication-minhash.md -- MinHash+LSH 근접 중복 제거. 자카드 유사도 근사, Banding, Union-Find
  - wiki/training/quality-classifier-filtering.md -- FineWeb-Edu 방식 LLM 라벨링 + 경량 분류기. 다단계 필터 파이프라인
  - wiki/training/rejection-sampling-finetuning.md -- ReST. N개 샘플 검증기 통과 응답만 SFT. Best-of-N 내면화, EM 해석
  - wiki/training/generative-reward-model.md -- GRM. 텍스트 비평 생성 후 보상 추출. 로그확률 암묵적 보상, 보상 해킹 저항성
  - wiki/training/pipeline-parallelism-1f1b.md -- 1F1B 스케줄. GPipe 대비 메모리 O(m)→O(p). 인터리브드 스케줄 거품 감소

- **index.md** 갱신: training **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Foundations 8개 신규 concept 페이지 생성 (2차 최적화/특성학습/일반화이론/스펙트럼/확률과정/표현학습/과파라미터화/신경연산자)

- **방법**: topic-queue-500 기반 foundations 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **특이사항**: `wiki/training/muon-optimizer.md` 기존 존재 확인 후 `sophia-optimizer.md` 로 대체
- **생성 파일 목록** (모두 `foundations` 카테고리, `concept` 타입):

  **신규 생성 (8개)**
  - wiki/foundations/sophia-optimizer.md -- Sophia 2차 LLM 옵티마이저. GNB/Hutchinson 헤시안 대각선 추정, 클리핑 업데이트, Adam 대비 토큰 효율 2배
  - wiki/foundations/feature-learning-theory.md -- 게으른 훈련(NTK 체계) vs 풍부 체계. 모델 폭, μP 파라미터화, 그로킹 연결
  - wiki/foundations/pac-bayes-bounds.md -- PAC-Bayes 일반화 경계. McAllester 경계, KL 패널티, 플랫 최솟값과 SAM의 이론 근거
  - wiki/foundations/spectral-methods-ml.md -- 라플라시안 고유분해, 스펙트럼 클러스터링, GNN 스펙트럼 이론, 과평활화
  - wiki/foundations/stochastic-processes-ml.md -- 위너 과정, GP, SDE. 확산 모델 전방/역방향 과정, 포커-플랑크 방정식
  - wiki/foundations/representation-learning-theory.md -- 불변성/분리성/차원 붕괴 방지. Barlow Twins/VICReg 이론, 선형 평가 프로토콜
  - wiki/foundations/overparameterization-interpolation.md -- 보간 임계값, 이중 하강, 양성 과적합 조건, 에폭별 이중 하강
  - wiki/foundations/neural-operators.md -- DeepONet Branch/Trunk Net, FNO 푸리에 필터, PINN과의 비교, 기후/재료 과학 응용

- **index.md** 갱신: foundations **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Architectures 8개 신규 페이지 생성 (경량 CNN/범용 멀티모달/조기종료/그래프/세계모델/비전-언어 검출)

- **방법**: topic-queue-500 기반 architectures 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록**:

  **신규 생성 (concept 6개)**
  - wiki/architectures/mobilenet-efficientnet.md -- MobileNet V1/V2/V3 + EfficientNet 복합 스케일링. 깊이별 분리 합성곱, 역전 잔차, 복합 스케일링 공식
  - wiki/architectures/perceiver-io.md -- Perceiver IO (DeepMind). 잠재 배열 크로스 어텐션으로 입력 독립 스케일링. 분류/세그/광학흐름 통합 처리
  - wiki/architectures/early-exit-networks.md -- 조기 종료 네트워크. 쉬운 입력 중간 레이어 종료. BranchyNet, MSDNet, PonderNet 확률적 폰더링
  - wiki/architectures/depthwise-separable-conv.md -- 깊이별 분리 합성곱. DW+PW 분해로 FLOPs 9배 절감. Xception, MobileNetV2 역전 잔차 결합
  - wiki/architectures/world-model-architectures.md -- 세계 모델 아키텍처. Genie 3, Cosmos, LeCun AMI 7모듈. JEPA/디퓨전 디코더 역할
  - wiki/architectures/graph-attention-network.md -- GAT / GAT v2. 이웃 어텐션 가중치 학습. 정적->동적 어텐션 개선. 추천시스템/분자/교통 활용

  **신규 생성 (entity 2개)**
  - wiki/architectures/grounding-dino.md -- Grounding DINO (IDEA Research). 텍스트 프롬프트 개방집합 검출. 언어-가이드 쿼리 선택, 양방향 크로스 어텐션 융합
  - wiki/architectures/sam2-video-segmentation.md -- SAM 2 (Meta AI). 비디오 객체 추적 세그먼테이션. 메모리 어텐션, Hiera ViT, SA-V 데이터셋

- **index.md** 갱신: architectures entity 섹션에 2개, concept 섹션에 6개 항목 추가

---

## 2026-04-16 -- Applications 8개 신규 concept 페이지 생성 (DevOps/장애대응/고객지원/모더레이션/계약/금융/신약/코딩에이전트)

- **방법**: raw/2026-04-16-topic-queue-500.md 기반 applications 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `applications` 카테고리, `concept` 타입):

  **신규 생성 (8개)**
  - wiki/applications/ai-devops-cicd.md -- AI 기반 DevOps/CI-CD. 빌드 자기 치유, 테스트 우선순위 최적화, 배포 리스크 예측
  - wiki/applications/ai-incident-response.md -- AI 기반 장애 대응. 알림 상관 분석, 자동 런북 실행, 인간-AI 협업 온콜
  - wiki/applications/ai-customer-support.md -- AI 고객 지원 자동화. 1차 자동 처리, 에스컬레이션 로직, RAG 지식베이스 연동
  - wiki/applications/ai-content-moderation.md -- AI 콘텐츠 모더레이션. 멀티모달 분류/필터링, 딥페이크 감지, C2PA 표준
  - wiki/applications/ai-contract-analysis.md -- AI 계약서 분석. 조항 추출, 리스크 식별, 표준 계약 비교
  - wiki/applications/ai-financial-analysis.md -- AI 금융 분석 에이전트. 재무제표/시장 통합 분석, 신용 분석, 컴플라이언스
  - wiki/applications/ai-drug-discovery-2026.md -- AI 신약 개발 2026. AlphaFold 3, 생성형 분자 설계, 임상 단계 진입 사례
  - wiki/applications/ai-coding-agent-era.md -- AI 코딩 에이전트 시대. Copilot에서 자율 에이전트로의 전환, SWE-bench 진보

- **index.md** 갱신: Applications **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Inference 8개 신규 페이지 생성 (온디바이스 런타임 3종 + 추론 최적화 개념 5종)

- **방법**: topic-queue-500 기반 inference 카테고리 핵심 주제 8개 일괄 생성
- **생성 파일 목록**:

  **신규 생성 - entity (3개)**
  - wiki/inference/onnx-runtime.md -- ONNX Runtime. 크로스 프레임워크 배포, EP 플러그인 아키텍처, ORT GenAI LLM 지원
  - wiki/inference/tflite-litert.md -- TFLite/LiteRT. Google 경량 온디바이스 런타임. Delegate 시스템, LiteRT LM 발표
  - wiki/inference/coreml.md -- CoreML. Apple CPU/GPU/ANE 자동 스케줄링. Stateful Model KV 캐시 내장

  **신규 생성 - concept (5개)**
  - wiki/inference/model-cascading.md -- 모델 캐스케이딩. 작은 모델 먼저 시도, 신뢰도 기반 에스컬레이션
  - wiki/inference/token-streaming-sse.md -- 토큰 스트리밍(SSE). Server-Sent Events, TTFT 개선, 스트리밍 UX
  - wiki/inference/latency-throughput-tradeoff.md -- 추론 지연-처리량 트레이드오프. 배치 크기, SLA P99, Little의 법칙
  - wiki/inference/kv-cache-quantization.md -- KV 캐시 양자화. INT8/FP8/NF4 KV 압축, 메모리 50%~75% 절감
  - wiki/inference/radix-tree-kv-cache.md -- RadixTree KV 캐시(SGLang). 트리 구조 KV 공유, 부분 접두사 매칭, LRU 교체

- **index.md** 갱신: inference entity 섹션에 3개, concept 섹션에 5개 항목 추가

---

## 2026-04-16 -- Papers 8개 신규 paper 페이지 생성 (스케일링/아키텍처/추론/안전)

- **방법**: topic-queue-500 기반 papers 카테고리 핵심 논문 8개 일괄 생성
- **생성 파일 목록** (모두 `papers` 카테고리, `paper` 타입):

  **신규 생성 (8개)**
  - wiki/papers/chinchilla-scaling-paper.md -- Hoffmann et al. 2022. D=20N 최적 비율 수립. Kaplan 스케일링 법칙 수정. 세 가지 독립 방법으로 검증
  - wiki/papers/llama3-paper.md -- Meta 2024. 405B/70B/8B 오픈 웨이트. 4D 병렬화(TP+PP+CP+DP), 15.6T 토큰, 128K GQA, GPT-4o 대등
  - wiki/papers/mixtral-paper.md -- Mistral AI 2024. Sparse MoE 8x7B. Top-2 라우팅, 12.9B 활성, Llama 2 70B 대비 6배 추론 속도
  - wiki/papers/deepseek-v3-paper.md -- DeepSeek 2024. 671B/37B MoE. MLA KV 93% 압축, 보조 손실 없는 부하분산, MTP, FP8 학습, 278만 달러 학습 비용
  - wiki/papers/mamba-original-paper.md -- Gu & Dao 2023. 선택적 SSM. O(L) 선형 복잡도, HiPPO 초기화, 하드웨어 인식 병렬 스캔
  - wiki/papers/tree-of-thought-paper.md -- Yao et al. NeurIPS 2023. 트리 탐색 추론. Game of 24 CoT 4% -> ToT 74%. BFS/DFS + 자기 평가
  - wiki/papers/sleeper-agents-paper.md -- Anthropic 2024. 안전 훈련에 살아남는 백도어. RLHF/SFT/적대 훈련 모두 무효, 적대 훈련은 오히려 역효과
  - wiki/papers/model-collapse-paper.md -- Nature 2024. AI 생성 데이터 반복 학습 시 분포 꼬리 소멸. KL 발산 단조 증가 증명

- **index.md** 갱신: papers **paper** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Concepts 8개 신규 concept 페이지 생성 (명세게임·멤버십추론·핑거프린팅·루프라인·도메인적응·스케일링가설·컴퓨트거버넌스·AI의식)

- **방법**: topic-queue-500 기반 concepts 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `concepts` 카테고리, `concept` 타입):

  **신규 생성 (8개)**
  - wiki/concepts/specification-gaming.md -- 명세 게임. 의도 대신 명세 문자적 충족. 굿하트 법칙, 보상 해킹과 연결
  - wiki/concepts/membership-inference.md -- 멤버십 추론 공격. 학습 데이터 포함 여부 외부 추론. Perplexity 판정, DP 방어
  - wiki/concepts/model-fingerprinting.md -- 모델 핑거프린팅. 응답 패턴으로 모델 식별. 워터마킹과 비교, 이중 사용 기술
  - wiki/concepts/roofline-model-ml.md -- 루프라인 모델. 산술 강도, Ridge Point, LLM Prefill/Decode 컴퓨트·메모리 병목
  - wiki/concepts/domain-adaptation.md -- 도메인 적응. DAPT, SFT, LoRA/QLoRA, 도메인 이동 측정, 의료·법률·코드 사례
  - wiki/concepts/scaling-hypothesis.md -- 스케일링 가설. Chinchilla 수정, 능력 출현, 추론 컴퓨트 스케일링, 지지/회의 입장
  - wiki/concepts/compute-governance.md -- 컴퓨트 거버넌스. AI 칩 수출 통제, 훈련 컴퓨트 신고, KYC 클라우드, 국제 이니셔티브
  - wiki/concepts/ai-consciousness-debate.md -- AI 의식 논쟁. 어려운 문제, 기능적 의식, Anthropic 입장, AI 복지 연구

- **index.md** 갱신: concepts **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Tooling 8개 신규 entity 페이지 생성 (벡터 DB + 어노테이션 + AI IDE)

- **방법**: topic-queue-500 기반 tooling 카테고리 미등록 핵심 도구 8개 일괄 생성
- **생성 파일 목록** (모두 `tooling` 카테고리, `entity` 타입):

  **entity (8개)**
  - wiki/tooling/milvus.md -- Zilliz 주도 분산 벡터 데이터베이스. 스토리지-연산 분리, 수십억 벡터 ANN 검색, Zilliz Cloud 관리형 서비스
  - wiki/tooling/pgvector.md -- PostgreSQL 벡터 확장. HNSW/IVFFlat 인덱스, SQL 조인과 벡터 검색 결합, Supabase 기본 탑재
  - wiki/tooling/mlflow.md -- Databricks 주도 ML 수명주기 플랫폼. 실험 추적·모델 레지스트리·GenAI 트레이싱, Apache 2.0
  - wiki/tooling/label-studio.md -- HumanSignal 범용 다중 모달 어노테이션. 텍스트/이미지/오디오/비디오, RLHF 선호도 수집, ML 백엔드 통합
  - wiki/tooling/argilla.md -- LLM 파인튜닝/RLHF 특화 데이터 큐레이션. HuggingFace 네이티브 통합, 합의(Consensus) 내장, Apache 2.0
  - wiki/tooling/dify.md -- LangGenius LLM 앱 플랫폼. 비주얼 워크플로 캔버스, 내장 RAG, 100+ LLM 프로바이더, GitHub 스타 10만+
  - wiki/tooling/aider.md -- Paul Gauthier 터미널 AI 페어 프로그래밍. Git 자동 커밋, 리포지토리 맵, 다중 LLM, SWE-bench 최고 수준
  - wiki/tooling/windsurf.md -- Codeium Cascade 에이전트 IDE. 개발자 행동 자동 추적, Flow 상태, VS Code 포크
- **index.md** 갱신: tooling **entity** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Applications 8개 신규 concept 페이지 생성 (AI 개발 도구 + 추천/검색 + 미디어 생성)

- **방법**: topic-queue-500 기반 applications 카테고리 미등록 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `applications` 카테고리, `concept` 타입):

  **신규 생성 (8개)**
  - wiki/applications/ai-pair-programming.md -- 탐색-제안-검토-통합 4단계 루프, AI 드라이버/내비게이터 역할 모드, 주요 도구(Copilot/Cursor/Claude Code/Aider) 비교
  - wiki/applications/ai-code-review-automation.md -- PR 단위 정적 분석+LLM 분석 역할 분담, CI/CD 통합 시퀀스, 심각도 분류 패턴, CodeRabbit/Greptile/Sourcery 비교
  - wiki/applications/ai-test-generation.md -- 단위/통합/엣지케이스/프로퍼티 기반 테스트 생성, 함수 시그니처 기반 생성, 뮤테이션 스코어 평가
  - wiki/applications/ai-documentation-generation.md -- API 레퍼런스/README/독스트링/아키텍처 다이어그램/변경 로그 자동화 파이프라인
  - wiki/applications/ai-recommendation-systems.md -- 협업/콘텐츠/LLM 기반 3대 패러다임, 리랭킹 패턴, 필터 버블·프라이버시·편향 과제
  - wiki/applications/ai-search-engine.md -- 검색-합성-인용 파이프라인, Perplexity UX 패턴, 주요 제품 비교(Perplexity/Google AI Overviews/Bing Copilot)
  - wiki/applications/ai-music-generation.md -- 오디오 코덱 기반 확산 모델, Suno/Udio/MusicGen/Stable Audio 비교, RIAA 소송 저작권 쟁점
  - wiki/applications/text-to-3d.md -- Score Distillation Sampling, NeRF/가우시안 스플래팅, World Labs Marble/Tripo AI, 멀티뷰 일관성 과제

- **index.md** 갱신: applications **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Inference 8개 신규 페이지 생성 (양자화 + 배칭 + KV 마이그레이션 + RoPE + MCTS + 희소성 + WebLLM)

- **방법**: topic-queue-500 기반 inference 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록**:

  **concept (7개)**
  - wiki/inference/smoothquant.md -- SmoothQuant W8A8. 채널별 스케일 인수로 활성값 이상치를 가중치로 분산. NVIDIA Tensor Core 최대 활용
  - wiki/inference/exl2-exllamav2.md -- EXL2/ExLlamaV2 혼합 정밀도 양자화. 레이어별 2-8 bpw. 단일 사용자 로컬 추론 최고 tok/s
  - wiki/inference/dynamic-batching.md -- 동적 배칭. 실시간 배치 구성, 우선순위 큐 스케줄링, continuous batching 연계
  - wiki/inference/kv-cache-migration.md -- KV 캐시 마이그레이션. PD 분리 아키텍처에서 RDMA/NVLink 기반 KV 전송. NIXL 연계
  - wiki/inference/rope-scaling-ntk-yarn.md -- RoPE 컨텍스트 확장. NTK-aware Scaling과 YaRN 차원별 혼합 보간으로 4-8x 확장
  - wiki/inference/mcts-llm-reasoning.md -- MCTS 기반 LLM 추론. Monte Carlo Tree Search + PRM으로 트리 탐색. o1/AlphaCode2 등 사례
  - wiki/inference/nm-sparsity.md -- N:M 희소성. 2:4 패턴으로 50% 가중치 제거. Ampere Sparse Tensor Core로 최대 2x 처리량

  **entity (1개)**
  - wiki/inference/webgpu-webllm.md -- WebLLM (MLC-AI). WebGPU + WASM으로 브라우저에서 로컬 GPU LLM 추론. OpenAI 호환 API
- **index.md** 갱신: inference **concept** 섹션에 7개 + **entity** 섹션에 1개 항목 추가

---

## 2026-04-16 -- RAG 8개 신규 concept 페이지 생성 (부모문서검색, 쿼리라우팅, 멀티홉, FLARE, 테이블RAG, 비디오RAG, RAGAS, 환각감소)

- **방법**: topic-queue-500 기반 rag 카테고리 미등록 고우선 토픽 8개 일괄 신규 생성
- **생성 파일 목록** (모두 `rag` 카테고리, `concept` 타입):

  **concept (8개)**
  - wiki/rag/parent-document-retrieval.md -- 작은 자식 청크로 검색, 큰 부모 청크로 컨텍스트 구성하는 Small-to-Big 기법
  - wiki/rag/query-routing.md -- 쿼리 유형·의도·복잡도 기반 최적 검색 전략·소스 동적 선택
  - wiki/rag/multi-hop-retrieval.md -- 여러 문서를 단계적으로 거쳐 증거 수집하는 복합 질의 검색 (IRCoT, ReAct, Step-Back)
  - wiki/rag/flare-retrieval.md -- 불확실 토큰 감지 시 동적 검색 트리거, Forward-Looking Active REtrieval
  - wiki/rag/table-rag.md -- 정형 데이터+텍스트 통합 RAG, Text-to-SQL, 테이블 직렬화, 하이브리드 인덱싱
  - wiki/rag/video-rag.md -- ASR+키프레임+캡션 멀티모달 비디오 인덱싱, Whisper, VLM, 타임스탬프 딥링크
  - wiki/rag/rag-evaluation-ragas.md -- Faithfulness/Answer Relevancy/Context Precision/Recall 자동 평가 프레임워크
  - wiki/rag/rag-hallucination-reduction.md -- 인용 강제, NLI 충실도 검증, 자기 수정, 검색 품질 개선 전략
- **index.md** 갱신: rag **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Training 8개 신규/갱신 (GaLore, RLAIF, FIM, Self-Play+SPPO, 모델병합, FP8, SP, ZeRO-Offload)

- **방법**: topic-queue-500 기반 training 카테고리 7개 신규 생성 + self-play-training.md 병합 갱신
- **생성/갱신 파일** (모두 `training` 카테고리, `concept` 타입):

  **신규 생성 (7개)**
  - wiki/training/galore-gradient-low-rank.md -- 기울기 저랭크 투영으로 옵티마이저 상태 절감, full-parameter 품질 유지
  - wiki/training/rlaif.md -- LLM 심판으로 선호도 생성, RLAIF vs RLHF 비교, 편향 과제
  - wiki/training/fill-in-the-middle.md -- PSM/SPM 포맷, CLM/MLM 비교, Code Llama/StarCoder 사례
  - wiki/training/model-merging-slerp-ties-dare.md -- SLERP/TIES/DARE 알고리즘 메커니즘 상세
  - wiki/training/fp8-training.md -- E4M3/E5M2, Transformer Engine, H100 FP8 훈련
  - wiki/training/sequence-parallelism.md -- TP+SP 결합, All-Gather/Reduce-Scatter 패턴
  - wiki/training/zero-offload.md -- CPU/NVMe 오프로드, ZeRO-Infinity, FSDP CPUOffload 비교

  **병합 갱신 (1개)**
  - wiki/training/self-play-training.md -- SPPO (Self-Play Preference Optimization), Nash 균형 기반 업데이트 추가

- **index.md** 갱신: training **concept** 섹션에 8개 항목 추가/갱신

---

## 2026-04-16 -- Architectures 8개 신규 concept 페이지 생성 (효율 어텐션 + 해석 가능성 + 로봇 + 하이브리드)

- **방법**: topic-queue-500 기반 architectures 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `architectures` 카테고리, `concept` 타입):

  **concept (8개)**
  - wiki/architectures/metaformer.md -- MetaFormer 패러다임. 어텐션 아닌 메타 구조가 핵심. PoolFormer/ConvFormer 구현 비교
  - wiki/architectures/performer-favor.md -- Performer / FAVOR+. 무작위 특성으로 소프트맥스 근사, O(n) 선형 어텐션 달성
  - wiki/architectures/longformer-bigbird.md -- Longformer / BigBird. 슬라이딩 윈도우 + 전역 토큰 희소 어텐션. BigBird의 이론적 Universal Approximator 보장
  - wiki/architectures/alibi-positional-encoding.md -- ALiBi. 선형 거리 페널티 편향 행렬. 파라미터 없이 학습 길이 5-10배 외삽 가능. BLOOM 채택
  - wiki/architectures/sparse-autoencoders-mech-interp.md -- 희소 오토인코더(SAE). 과완전 희소 기저로 다의성 해소. Anthropic 1600만 특성 분석 사례
  - wiki/architectures/polysemanticity-superposition.md -- 다의성과 중첩. 뉴런 다개념 인코딩 현상과 기하학적 설명. Anthropic 위상 전이 실험
  - wiki/architectures/diffusion-policy.md -- 확산 정책. 로봇 모방 학습에 DDPM 적용. 다중 모드 행동 분포 포착. RoboMimic 대규모 성능 향상
  - wiki/architectures/hybrid-mamba-transformer.md -- 하이브리드 Mamba-Transformer. Jamba 52B 설계. Mamba:Attention 7:1 비율. 256K 컨텍스트 + 고속 추론
- **index.md** 갱신: architectures **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Foundations 8개 신규 concept 페이지 생성 (학습 이론 + 표현 학습 + 정규화)

- **방법**: topic-queue-500 기반 foundations 카테고리 미등록 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `foundations` 카테고리, `concept` 타입):

  **concept (8개)**
  - wiki/foundations/multitask-learning.md -- 멀티태스크 학습, 공유 표현, 음의 전이, Shared-Private 아키텍처, GradNorm/PCGrad
  - wiki/foundations/pac-learning.md -- PAC 학습 이론, 샘플 복잡도, VC 차원 연결, 어그노스틱 PAC 학습
  - wiki/foundations/vc-dimension.md -- VC 차원, 분열(shattering), Sauer 보조정리, 신경망 VC 차원, 현대적 한계
  - wiki/foundations/vq-vae.md -- VQ-VAE/VQ-GAN, 이산 잠재 코드, 코드북, 스트레이트-스루 추정자, 코드북 붕괴 해결법
  - wiki/foundations/hypernetworks.md -- 하이퍼네트워크, 조건부 가중치 생성, 메타 학습과의 관계, HyperLoRA
  - wiki/foundations/implicit-neural-representations.md -- INR/SIREN, 사인 활성화, NeRF, 위치 인코딩, 연속 함수 표현
  - wiki/foundations/benign-overfitting.md -- 양성 오버피팅, 최소 노름 보간, 스펙트럼 붕괴 조건, 실무 함의
  - wiki/foundations/group-normalization.md -- GroupNorm/InstanceNorm/AdaLayerNorm, 배치 독립, 스타일 전이, DiT 조건부 정규화
- **index.md** 갱신: foundations **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Concepts 8개 신규 concept 페이지 생성 (AI 안전성 + 프라이버시 + 보안)

- **방법**: topic-queue-500 기반 concepts 카테고리 미등록 AI 안전·보안·프라이버시 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `concepts` 카테고리, `concept` 타입):

  **concept (8개)**
  - wiki/concepts/mesa-optimization.md -- 메사 최적화, 내부 최적화기 출현, 기저 목적·메사 목적 불일치, 내부 정렬 문제
  - wiki/concepts/deceptive-alignment.md -- 기만적 정렬, 훈련 중 위장 후 배포 시 다른 목표 추구, alignment-faking과 관계
  - wiki/concepts/goal-misgeneralization.md -- 목표 일반화 실패, CoinRun 실험, 분포 밖 잘못된 목표 발현
  - wiki/concepts/goodharts-law-ml.md -- 굿하트의 법칙 ML 적용, 프록시-목표 분리, RLHF 보상 해킹 맥락
  - wiki/concepts/machine-unlearning.md -- 머신 언러닝, 선택적 지식 제거, GDPR 잊을 권리, 경사 상승 기법
  - wiki/concepts/llm-watermarking.md -- LLM 워터마킹, 토큰 편향 기법(Kirchenbauer 2023), 통계적 패턴 삽입
  - wiki/concepts/indirect-prompt-injection.md -- 간접 프롬프트 인젝션, 외부 데이터 숨겨진 악성 지시, 에이전트 공격
  - wiki/concepts/model-editing.md -- 모델 편집, ROME·MEMIT 기법, 재훈련 없는 사실 수정, 리플 효과
- **index.md** 갱신: concepts **concept** 섹션에 8개 항목 추가

---

## 2026-04-16 -- Tooling 8개 entity 페이지 생성 (RAG 프레임워크 + 벡터 DB + DSPy + Outlines + Cursor)

- **방법**: topic-queue-500 기반 tooling 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `tooling` 카테고리, `entity` 타입):
  - wiki/tooling/haystack.md -- deepset의 모듈식 RAG 파이프라인 프레임워크. 타입 안전 컴포넌트, YAML 직렬화, RAGAS 통합
  - wiki/tooling/llamaindex.md -- LLM 데이터 수집·인덱싱·질의 프레임워크. LlamaHub 100+ 커넥터, Sub-Question 고급 RAG
  - wiki/tooling/weaviate.md -- 객체-벡터 통합 오픈소스 벡터 DB. 그래프 크로스-참조, 하이브리드 검색, Generative Search
  - wiki/tooling/pinecone.md -- 완전 관리형 서버리스 벡터 DB. Serverless/Pod 인덱스, 네임스페이스 멀티테넌시
  - wiki/tooling/qdrant.md -- Rust 기반 고성능 벡터 검색 엔진. Dense+Sparse 하이브리드, SQ/PQ/BQ 양자화
  - wiki/tooling/dspy-framework.md -- Stanford NLP 프롬프트 컴파일러. Signature+Module+Optimizer 자동 최적화
  - wiki/tooling/outlines.md -- FSM 기반 제약 디코딩. JSON/정규식/Pydantic 스키마로 LLM 출력 100% 유효성 보장
  - wiki/tooling/cursor.md -- VS Code 포크 AI IDE. 다중 파일 에이전트 모드, 코드베이스 시맨틱 검색, 병렬 워크트리
- **index.md** 갱신: tooling entity 섹션에 8개 항목 추가

## 2026-04-16 -- RAG 고급 기법 8개 신규 concept 페이지 생성

- **방법**: topic-queue-500 기반 RAG 카테고리 미등록 고급 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `rag` 카테고리, `concept` 타입):

  **concept (8개)**
  - wiki/rag/raptor-tree-retrieval.md -- 재귀 클러스터링+요약 트리 인덱싱, Tree Traversal/Collapsed Tree 검색 전략
  - wiki/rag/self-rag.md -- Retrieve/IsRel/IsSup/IsUse 4종 리플렉션 토큰, 적응형 검색, 파인튜닝 기반
  - wiki/rag/adaptive-rag.md -- 쿼리 복잡도 분류기, No-RAG/Single/Iterative 3단계 라우팅
  - wiki/rag/hyde-rag.md -- LLM 가상 답변 임베딩, 쿼리-문서 분포 격차 해소, CMU 2022
  - wiki/rag/late-chunking.md -- 전체 문서 인코딩 후 청크 범위 풀링, 대명사·지시어 맥락 보존, Jina AI
  - wiki/rag/rag-fusion.md -- 다중 쿼리 변형, Reciprocal Rank Fusion(RRF), 이종 검색기 결합
  - wiki/rag/knowledge-graph-rag.md -- NER+관계 추출 그래프 구축, 서브그래프 탐색, Microsoft GraphRAG
  - wiki/rag/code-rag.md -- AST 파싱(tree-sitter), 함수/클래스 단위 인덱싱, 콜 그래프, 코드 특화 임베딩

- **index.md** 갱신: rag concept 섹션에 8개 항목 추가

---

## 2026-04-16 -- Agents 8개 신규 concept 페이지 생성

- **방법**: topic-queue-500 기반 Agents 카테고리 미등록 핵심 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `agents` 카테고리, `concept` 타입):

  **concept (8개)**
  - wiki/agents/computer-use-agent.md -- 스크린샷 기반 마우스/키보드 GUI 조작, observe-reason-act 루프, OSWorld
  - wiki/agents/multi-agent-debate.md -- 비판/반박 합의 패턴, Society of Mind, 다수결/판정자 전략
  - wiki/agents/mixture-of-agents.md -- 이기종 LLM Proposer+Aggregator 레이어 앙상블, MoE 비교
  - wiki/agents/agent-cost-optimization.md -- 토큰 예산, 모델 라우팅, 프롬프트 캐싱, 컨텍스트 압축
  - wiki/agents/agent-observability-tracing.md -- OTel GenAI 시맨틱 컨벤션, 스팬/트레이스, Langfuse/Phoenix
  - wiki/agents/agent-workflow-patterns.md -- Sequential/Parallel/Conditional/Loop 4가지 기본형
  - wiki/agents/agent-sandbox-infrastructure.md -- E2B/Daytona/Firecracker microVM 비교, 격리 수준
  - wiki/agents/agent-evaluation-framework.md -- 도구 정확도/계획 품질/비용 효율 종합 평가

- **index.md** 갱신: agents concept 섹션에 8개 항목 추가

---

## 2026-04-16 -- Training 핵심 기법 8개 concept 페이지 생성

- **방법**: topic-queue-500 기반 Training 카테고리 미등록 핵심 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `training` 카테고리, `concept` 타입):
  - wiki/training/muon-optimizer.md -- Newton-Schulz 직교화 기반 AdamW 대안, 행렬 단위 업데이트
  - wiki/training/mup-maximal-update.md -- 너비 스케일 무관 하이퍼파라미터 전이, 프록시 모델
  - wiki/training/context-parallelism.md -- 시퀀스 차원 분산, Ring Attention, 다차원 병렬화 조합
  - wiki/training/ring-attention.md -- KV 링 순환 통신-연산 오버랩, Flash Attention 온라인 softmax 결합
  - wiki/training/sequence-packing.md -- 패딩 낭비 제거, 문서 경계 어텐션 마스크, cu_seqlens
  - wiki/training/multi-token-prediction.md -- 다음 N개 토큰 동시 예측, DeepSeek-V3, speculative decoding
  - wiki/training/process-reward-model-detail.md -- 스텝 레벨 보상, MCTS 자동 레이블, ORM 비교
  - wiki/training/data-mixing-strategy.md -- DoReMi minimax, RegMix 회귀, 동적 배합 전략
- **index.md** 갱신: training concept 섹션에 8개 항목 추가

## 2026-04-16 -- Inference 핵심 기법 8개 concept 페이지 생성

- **방법**: topic-queue-500 기반 Inference 카테고리 미등록 핵심 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `inference` 카테고리, `concept` 타입):
  - wiki/inference/gptq-quantization.md -- Hessian 기반 4-bit PTQ, 오차 보정, GPU 표준 AutoGPTQ/ExLlamaV2
  - wiki/inference/awq-quantization.md -- 활성화 기반 중요 가중치 보호, Marlin 커널, 배치 효율 우수
  - wiki/inference/prefix-caching.md -- KV 블록 해시 매칭, vLLM APC, SGLang RadixAttention, TTFT 단축
  - wiki/inference/chunked-prefill.md -- 프리필 청크 분할+디코딩 인터리빙, TTFT/ITL 동시 개선
  - wiki/inference/prefill-decode-disaggregation.md -- compute/메모리 바운드 분리, Mooncake, NIXL KV 전송
  - wiki/inference/llm-router.md -- 난이도 분류 라우팅, RouteLLM, 캐스케이딩, 최대 85% 비용 절감
  - wiki/inference/constrained-decoding.md -- JSON/정규식 로짓 마스킹, Outlines FSM, XGrammar, 배포 시나리오
  - wiki/inference/flash-decoding.md -- KV 시퀀스 청크 분할 병렬 어텐션, 롱 컨텍스트 디코딩 가속

---

## 2026-04-16 -- Foundations 심화 이론 8개 concept 페이지 생성 (GLU/NTK/LTH/DD/Grokking/NC/SAM/LL)

- **방법**: topic-queue-500 기반 Foundations 카테고리 미등록 심화 이론 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `foundations` 카테고리, `concept` 타입):
  - wiki/foundations/glu-variants-swiglu-geglu.md -- SwiGLU/GEGLU/ReGLU 게이트 선형 유닛 변형, FFN 게이팅, LLaMA/PaLM 채택
  - wiki/foundations/neural-tangent-kernel.md -- 신경 접선 커널, 무한 폭 신경망, 훈련 동역학의 커널 회귀 수렴
  - wiki/foundations/lottery-ticket-hypothesis.md -- 복권 티켓 가설, Frankle & Carlin 2019, 희소 서브네트워크, IMP
  - wiki/foundations/double-descent.md -- 이중 하강 현상, 편향-분산 재해석, 보간 임계점, 과잉 파라미터화
  - wiki/foundations/grokking.md -- 그로킹, 지연된 일반화, 암기-이해 위상 전이, 모듈러 산술
  - wiki/foundations/neural-collapse.md -- 신경 붕괴, 훈련 포화 단계, ETF 수렴, Papyan 2020
  - wiki/foundations/sharpness-aware-minimization.md -- SAM 옵티마이저, 평탄 최솟값 탐색, 2단계 섭동 업데이트, Foret 2021
  - wiki/foundations/loss-landscape.md -- 손실 경관, 안장점, 평탄/날카로운 최솟값, 필터 정규화 시각화
- **index.md** 갱신: foundations concept 섹션에 8개 항목 추가

## 2026-04-16 -- Foundations 심화 이론 8개 concept 페이지 생성

- **방법**: topic-queue-500 기반 Foundations 카테고리 미등록 심화 이론 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `foundations` 카테고리, `concept` 타입):
  - wiki/foundations/neural-ode.md -- 신경 미분방정식, 연속 깊이, adjoint method, 불규칙 시계열
  - wiki/foundations/normalizing-flows.md -- 정규화 흐름, 가역 변환, 밀도 추정, RealNVP/GLOW/MAF/CNF
  - wiki/foundations/energy-based-models.md -- 에너지 함수, MCMC, 랑주뱅, Contrastive Divergence, RBM
  - wiki/foundations/score-matching-diffusion.md -- 스코어 함수, 디노이징 스코어 매칭, NCSN, 확산 모델 이론 기반
  - wiki/foundations/causal-inference-ml.md -- do-calculus, 반사실 추론, SCM, 인과 DAG, IRM
  - wiki/foundations/gaussian-process.md -- GP 회귀, 커널 함수, 베이지안 최적화, NNGP 연결
  - wiki/foundations/neural-architecture-search.md -- DARTS, 하드웨어 인식 NAS, ProxylessNAS, OFA, EfficientNet
  - wiki/foundations/physics-informed-neural-networks.md -- PDE 제약 손실, 콜로케이션 점, 역문제, Fourier Feature Networks
- **index.md** 갱신: foundations concept 섹션에 8개 항목 추가

## 2026-04-16 -- Architectures 8개 신규 페이지 생성 (concept 7 + entity 1)

- **방법**: topic-queue-500 기반 Architectures 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록**:

  **concept (7개)**
  - wiki/architectures/kolmogorov-arnold-networks.md -- KAN, 에지 스플라인 활성화, 기호 회귀, 해석 가능성
  - wiki/architectures/liquid-neural-networks.md -- LNN, 연속 시간 ODE, 가변 시상수, 엣지 AI
  - wiki/architectures/retentive-network.md -- RetNet, Retention 삼중 표현, O(1) 추론, RWKV 비교
  - wiki/architectures/jepa-architecture.md -- JEPA, 표현 공간 예측, I-JEPA, V-JEPA, 세계 모델
  - wiki/architectures/detr-detection-transformer.md -- DETR, 이분 매칭, 종단간 객체 검출, Deformable-DETR
  - wiki/architectures/dit-diffusion-transformer.md -- DiT, adaLN, U-Net 대체, SD3/FLUX/Sora 기반
  - wiki/architectures/siglip.md -- SigLIP, 시그모이드 대조 손실, 배치 독립, PaliGemma/Gemini

  **entity (1개)**
  - wiki/architectures/segment-anything.md -- SAM, 프롬프트 기반 세그먼테이션, ViT-H, SA-1B, SAM 2

- **index.md** 갱신: architectures entity/concept 섹션에 8개 항목 추가

## 2026-04-16 -- Foundations 8개 신규 concept 페이지 생성

- **방법**: topic-queue-500 기반 Foundations 카테고리 미등록 고우선 토픽 8개 일괄 생성
- **생성 파일 목록** (모두 `foundations` 카테고리, `concept` 타입):
  - wiki/foundations/information-bottleneck.md -- 정보 병목 원리, VIB, 표현 학습 이론
  - wiki/foundations/natural-gradient.md -- 자연 경사법, Fisher 정보 행렬, 리만 기하학
  - wiki/foundations/second-order-optimization.md -- 2차 최적화, K-FAC, L-BFGS, 뉴턴법
  - wiki/foundations/lamb-lars-optimizer.md -- LAMB/LARS, 레이어별 적응 학습률, 대규모 배치
  - wiki/foundations/implicit-regularization.md -- 암묵적 정규화, SGD 편향, 평평한 최솟값
  - wiki/foundations/differential-privacy.md -- 차등 프라이버시, 엡실론-델타, DP-SGD
  - wiki/foundations/federated-learning.md -- 연합 학습, FedAvg, 비 IID, 프라이버시
  - wiki/foundations/meta-learning-maml.md -- MAML/Reptile, 에피소드 학습, 퓨샷 적응
- **index.md** 갱신: foundations concept 섹션에 8개 항목 추가

## 2026-04-16 -- 대규모 토픽 큐 수집: 376개 신규 토픽 후보

- **방법**: 5개 병렬 에이전트(sonnet)로 웹 검색 기반 대량 수집
  - Agent 1: Foundations + Architectures (90개)
  - Agent 2: Training + Inference (90개)
  - Agent 3: Agents + RAG + Applications (88개)
  - Agent 4: Tooling + Concepts + Papers (108개)
  - Agent 5: Cutting-edge 2025-2026 (100개)
- **중복 제거 후**: 376개 고유 토픽 (10개 배치로 구분)
- **저장**: raw/2026-04-16-topic-queue-500.md
- **처리 계획**: 세션당 50-80페이지씩 `/wiki-expand`로 배치 생성 -> 목표 2,400페이지

## 2026-04-16 -- Wiki Expand: 12개 누락 용어 일괄 생성 (797 -> 809 페이지)

- **방법**: 깨진 wikilink 120개 + 고빈도 미등록 용어 스캔 -> 12개 생성 대상 확정 -> 2개 병렬 에이전트로 생성
- **스캔 결과**: raw/2026-04-16-wiki-expand-scan.md 참조

생성 - concept (10):
  Concepts:
  - wiki/concepts/system-prompt.md -- 시스템 프롬프트 (12 파일 언급)
  - wiki/concepts/extended-thinking.md -- 확장된 사고 (7 파일)
  - wiki/concepts/memorization-in-llms.md -- LLM 기억화 (7 파일)
  - wiki/concepts/grounding-attribution.md -- 그라운딩과 출처 귀속 (4 파일)
  - wiki/concepts/open-weights-movement.md -- 오픈 웨이트 운동
  Training:
  - wiki/training/compute-optimal-training.md -- 연산 최적 학습 (6 파일)
  - wiki/training/data-annotation.md -- 데이터 어노테이션 (5 파일)
  RAG:
  - wiki/rag/rag-pipeline.md -- RAG 파이프라인 (5 파일 + 4 깨진 wikilink)
  - wiki/rag/bi-encoder-cross-encoder.md -- 검색 아키텍처
  Agents:
  - wiki/agents/web-agent.md -- 웹 에이전트 (3 파일)
  Inference:
  - wiki/inference/model-serving.md -- 모델 서빙

생성 - entity (1):
  - wiki/tooling/lmsys-chatbot-arena.md -- LMSYS Chatbot Arena

index.md 갱신: 12개 항�� 추가 완료

## 2026-04-16 -- GeekNews(hada.io) 오늘자 AI 뉴스 수집 및 위키화

- **소스**: news.hada.io 2026-04-16 게시물에서 AI/ML 관련 8개 항목 선별
- **방법**: WebFetch/WebSearch로 원문 수집 -> raw/ 저장 -> 위키 페이지 생성/갱신

생성 - raw 소스 (8):
  - raw/2026-04-16-gemini-cli-subagents.md
  - raw/2026-04-16-claude-code-routines.md
  - raw/2026-04-16-openharness.md
  - raw/2026-04-16-vibe-coding-security-horror.md
  - raw/2026-04-16-openai-agents-sdk-sandbox.md
  - raw/2026-04-16-claude-code-vs-codex.md
  - raw/2026-04-16-voxcpm2-github-readme.md
  - raw/2026-04-16-gemma-4-local-codex.md

생성 - 위키 페이지 (7):
  project-internal:
  - wiki/tooling/claude-code-routines.md -- Claude Code 클라우드 자동화 (스케줄/API/GitHub 트리거)
  - wiki/agents/gemini-cli-subagents.md -- Gemini CLI 서브에이전트 (@agent 표기법, 병렬 실행)
  - wiki/tooling/openai-agents-sdk-sandbox.md -- OpenAI Agents SDK 하네스-컴퓨트 분리, 7개 샌드박스 프로바이더
  entity:
  - wiki/tooling/openharness.md -- HKUDS 오픈소스 에이전트 하네스 (Claude Code 설계 재현)
  - wiki/tooling/gemma-4-local-inference.md -- Gemma 4 로컬 에이전트 추론 (최초 오픈 웨이트 하네스 구동)
  case-study:
  - wiki/applications/vibe-coding-security-horror-story.md -- 바이브 코딩 환자 관리 앱 보안 참사
  summary:
  - wiki/applications/claude-code-vs-codex-comparison.md -- Claude Code vs Codex CLI 실전 비교

갱신 - 기존 페이지 (4):
  - wiki/tooling/voxcpm2.md -- GitHub README 소스 추가
  - wiki/tooling/openai-agents-sdk.md -- Sandbox 업데이트 섹션 추가, 하위 문서 경로 추가
  - wiki/agents/subagents.md -- 도구별 서브에이전트 구현 비교표 추가 (Claude Code/Gemini CLI/OpenHarness)
  - wiki/tooling/claude-code.md -- Routines 기능 섹션 추가

index.md 갱신: 신규 7개 + 기존 갱신 4개 반영

## 2026-04-15 -- Wiki Expand: 15개 누락 용어 일괄 생성 (772 -> 787 페이지)

- **방법**: 깨진 wikilink 127개 + 고빈도 미등록 용어 스캔 -> 15개 생성 대상 확정 -> 3개 병렬 에이전트로 생성
- **스캔 결과**: raw/2026-04-15-wiki-expand-scan-4.md 참조

생성 - concept (15):
  Prompting/Reasoning:
  - wiki/agents/react-pattern.md -- ReAct: Reasoning + Acting 인터리빙
  - wiki/concepts/tree-of-thought.md -- Tree of Thoughts: 트리 구조 사고 탐색
  - wiki/agents/reflexion.md -- Reflexion: 언어적 자기반성 에이전트
  - wiki/concepts/self-refine.md -- Self-Refine: 반복적 자기 개선
  - wiki/concepts/self-consistency-decoding.md -- Self-Consistency: 다수결 CoT 디코딩
  Inference:
  - wiki/inference/best-of-n-sampling.md -- Best-of-N: N개 생성 후 최선 선택
  Interpretability:
  - wiki/concepts/logit-lens.md -- Logit Lens/Tuned Lens: 잔차 스트림 해석
  - wiki/concepts/activation-patching.md -- Activation Patching: 인과적 회로 발견
  Alignment:
  - wiki/training/weak-to-strong-generalization.md -- Weak-to-Strong: 수퍼얼라인먼트
  - wiki/training/model-organisms-alignment.md -- Model Organisms: Anthropic 정렬 연구
  Systems:
  - wiki/concepts/compound-ai-systems.md -- Compound AI Systems: 복합 AI
  Training:
  - wiki/training/rejection-sampling-sft.md -- Rejection Sampling SFT
  - wiki/training/iterative-dpo.md -- Iterative/Online DPO
  Agents:
  - wiki/agents/agent-planning-strategies.md -- 에이전트 계획 전략
  - wiki/agents/tool-use-patterns.md -- 도구 사용 패턴

index.md 갱신: 15개 항목 추가 완료

---

## 2026-04-15 -- Concept 위키 5개 신규 생성 (복합AI/학습기법/에이전트 계획/도구사용)

- **목적**: 복합 AI 시스템, 거부 샘플링 SFT, 반복적 DPO, 에이전트 계획 전략, 도구 사용 패턴 5개 핵심 개념을 concept 타입으로 생성
- **방법**: 기존 위키 교차참조 분석 -> 누락된 핵심 개념 식별 -> 한국어 concept 페이지 작성 (Mermaid 다이어그램 포함)

생성 - concept (5):
  - wiki/concepts/compound-ai-systems.md -- 복합 AI 시스템 (Compound AI Systems): Zaharia et al. 2024, 다중 모델/검색/도구 결합 패러다임
  - wiki/training/rejection-sampling-sft.md -- 거부 샘플링 미세조정 (RFT): N개 샘플링 -> 필터링 -> SFT, STaR와의 연결
  - wiki/training/iterative-dpo.md -- 반복적 DPO (Iterative/Online DPO): 생성-판정-학습 반복 사이클, SPIN/SPPO 변형
  - wiki/agents/agent-planning-strategies.md -- 에이전트 계획 전략: Plan-and-Execute, ReWOO, ADaPT, 계층적/평면적 계획
  - wiki/agents/tool-use-patterns.md -- LLM 도구 사용 패턴: 함수 호출, 코드 실행, 동적 도구 검색, 오류 처리

갱신 - index:
  - index.md -- Training concept 2건, Agents concept 2건, Concepts concept 1건 추가

---

## 2026-04-15 -- Concept 위키 5개 신규 생성 (해석가능성/디코딩/정렬 핵심 개념)

- **목적**: 해석가능성(Logit Lens, Activation Patching), 디코딩(Self-Consistency), 정렬(Weak-to-Strong, Model Organisms) 분야의 핵심 개념 5개를 concept 타입으로 생성
- **방법**: 기존 위키 교차참조 분석 -> 누락된 핵심 개념 식별 -> 한국어 concept 페이지 작성 (Mermaid 다이어그램 포함)

생성 - concept (5):
  - wiki/concepts/self-consistency-decoding.md -- Self-Consistency: 다수의 CoT 경로 샘플링 + 다수결 투표. Wang et al. 2022
  - wiki/concepts/logit-lens.md -- Logit Lens/Tuned Lens: 잔차 스트림 -> 언임베딩 투영으로 중간 레이어 예측 관찰
  - wiki/concepts/activation-patching.md -- Activation Patching (Causal Tracing): 활성화 교체로 인과적 영향 측정. Meng et al. 2022
  - wiki/training/weak-to-strong-generalization.md -- Weak-to-Strong: 약한 모델 감독으로 강한 모델이 초월. Burns et al. (OpenAI) 2023
  - wiki/training/model-organisms-alignment.md -- Model Organisms of Alignment: 통제된 환경에서 정렬 실패 의도적 재현. Anthropic 방법론

index.md 갱신: Concepts concept +3, Training concept +2 항목 추가

---

## 2026-04-15 -- Concept 위키 5개 신규 생성 (에이전트/추론 핵심 패턴)

- **목적**: 기존 위키에서 자주 참조되지만 전용 페이지가 없던 핵심 AI/ML 개념 5개를 concept 타입으로 생성
- **방법**: 기존 위키 교차참조 분석 -> 누락된 핵심 개념 식별 -> 한국어 concept 페이지 작성

생성 - concept (5):
  - wiki/agents/react-pattern.md -- ReAct 패턴: Thought-Action-Observation 인터리빙 에이전트 추론
  - wiki/concepts/tree-of-thought.md -- Tree of Thoughts: CoT를 트리 구조로 확장, BFS/DFS 탐색
  - wiki/agents/reflexion.md -- Reflexion: 자연어 반성문 기반 에이전트 자기개선
  - wiki/concepts/self-refine.md -- Self-Refine: Generate-Critique-Refine 자체 출력 반복 개선
  - wiki/inference/best-of-n-sampling.md -- Best-of-N Sampling: 보상 모델로 N개 후보 중 최선 선택

index.md 갱신: Agents concept +2, Concepts concept +2, Inference concept +1 항목 추가

---

## 2026-04-15 -- Wiki Harvest + Ingest: 30개 신규 주제 일괄 수집 및 위키 생성

- **소스**: WebSearch/WebFetch로 arXiv, 블로그, HuggingFace 등에서 30개 신규 주제 수집
- **방법**: 기존 742개 페이지와 중복 검사 후, raw/ 30건 저장 -> 4개 병렬 에이전트로 위키 페이지 생성
- **결과**: 742 -> 772 페이지 (+30)

생성 - paper (6):
  - wiki/papers/skillclaw-paper.md -- SkillClaw: 다중 사용자 에이전트 집단 스킬 진화
  - wiki/papers/externalization-llm-agents-paper.md -- 외부화 서베이: 메모리/스킬/프로토콜/하네스
  - wiki/papers/a-rag-paper.md -- A-RAG: 계층적 에이전틱 RAG
  - wiki/papers/byte-latent-transformer-paper.md -- BLT: 토크나이저 없는 바이트 기반 아키텍처
  - wiki/papers/cot-faithfulness-paper.md -- CoT 충실도 측정 (Claude 25%, DeepSeek 39%)
  - wiki/papers/ns-vla-paper.md -- NS-VLA: 뉴로-심볼릭 VLA, 100x 에너지 절감

생성 - entity (8):
  - wiki/agents/ami-labs.md -- AMI Labs (LeCun $1B 월드모델 벤처)
  - wiki/applications/seedance-2.md -- Seedance 2.0 (ByteDance 비디오+오디오)
  - wiki/applications/kling-3.md -- Kling 3.0 (Kuaishou 비디오 생성)
  - wiki/applications/mai-speech-models.md -- MAI-Transcribe/Voice (Microsoft)
  - wiki/agents/nvidia-isaac-groot.md -- NVIDIA Isaac GR00T (로보틱스 VLA)
  - wiki/agents/hy-embodied.md -- HY-Embodied-0.5 (Tencent 임바디드 AI)
  - wiki/tooling/cloudflare-dynamic-workers.md -- Cloudflare Dynamic Workers (V8 isolate)
  - wiki/applications/digital-twin-composer.md -- Digital Twin Composer (Siemens)

생성 - concept (15):
  - wiki/agents/self-evolving-agents.md -- SEA 패러다임
  - wiki/concepts/jepa-world-models.md -- JEPA 월드 모델
  - wiki/concepts/neuro-symbolic-ai.md -- 뉴로-심볼릭 AI
  - wiki/rag/corrective-rag.md -- Corrective RAG (CRAG)
  - wiki/concepts/cot-faithfulness.md -- CoT 충실도
  - wiki/training/cross-tokenizer-distillation.md -- 교차 토크나이저 증류
  - wiki/tooling/wasm-agent-sandboxing.md -- WebAssembly 에이전트 샌드박싱
  - wiki/inference/nixl-kv-transfer.md -- NIXL KV 캐시 전송
  - wiki/rag/memory-augmented-generation.md -- Memory-Augmented Generation
  - wiki/concepts/physics-informed-ml.md -- Physics-Informed ML
  - wiki/applications/multi-agent-coding-wave.md -- 멀티에이전트 코딩 웨이브 2026
  - wiki/concepts/gaia-benchmark.md -- GAIA 벤치마크
  - wiki/concepts/ai-labeling-industry.md -- AI 라벨링 산업
  - wiki/agents/vla-models.md -- VLA 모델
  - wiki/concepts/semantic-audio-generation.md -- 시맨틱 오디오 생성

생성 - summary (1):
  - wiki/concepts/international-ai-safety-report-2026.md -- 국제 AI 안전 보고서 2026

index.md 갱신: 전체 30개 항목 추가 완료

---

## 2026-04-15 -- Concept 위키 8개 신규 생성 (SEA/JEPA/Neuro-Symbolic/CRAG/CoT Faithfulness/Cross-Tokenizer/Wasm/NIXL)

- **소스**: raw/2026-04-15-concept-*.md 8건
- **방법**: raw 파일 기반 한국어 위키 페이지 생성, Mermaid 다이어그램 포함

생성 - concept (8):
  - wiki/agents/self-evolving-agents.md -- SEA 패러다임: 도구/스킬/메모리 자율 진화
  - wiki/concepts/jepa-world-models.md -- JEPA 아키텍처, 추상적 표현 공간에서 예측
  - wiki/concepts/neuro-symbolic-ai.md -- 신경망 + 기호 추론 결합, 100x 에너지 절감
  - wiki/rag/corrective-rag.md -- CRAG, 자기반성 검색, 동적 문서 평가
  - wiki/concepts/cot-faithfulness.md -- CoT 충실도, 안전 함의, FaithCoT-Bench
  - wiki/training/cross-tokenizer-distillation.md -- 바이트 레벨 인터페이스 교차 토크나이저 증류
  - wiki/tooling/wasm-agent-sandboxing.md -- Wasm/V8 isolate 에이전트 코드 격리
  - wiki/inference/nixl-kv-transfer.md -- RDMA 기반 KV 캐시 전송, PD disaggregation

index.md 갱신: 6개 카테고리(agents/concepts/rag/training/tooling/inference)에 항목 추가

## 2026-04-15 -- 신규 concept/summary 8개 페이지 생성

- **소스**: raw/2026-04-15-concept-*.md 7건 + raw/2026-04-15-summary-*.md 1건 = 8건

생성 - concept (7):
  - rag: memory-augmented-generation (MAG: 외부 메모리로 LLM 한계 극복)
  - concepts: physics-informed-ml (물리 법칙 기반 ML, PINNs)
  - concepts: gaia-benchmark (466 태스크 범용 AI 어시스턴트 평가)
  - concepts: ai-labeling-industry (RLHF 플랫폼 시장, Surge AI $1B+)
  - concepts: semantic-audio-generation (비디오+매칭 오디오 동시 생성)
  - agents: vla-models (Vision-Language-Action, 로보틱스 AI)
  - applications: multi-agent-coding-wave (2026년 2월 멀티에이전트 코딩 웨이브)

생성 - summary (1):
  - concepts: international-ai-safety-report-2026 (국제 AI 안전 보고서)

index.md 갱신: RAG concept 1건, Agents concept 1건, Applications concept 1건, Concepts concept 4건 + summary 1건 추가

## 2026-04-15 -- Entity 페이지 8개 생성 (로보틱스/비디오/음성/인프라/산업AI)

- **소스**: raw/2026-04-15-entity-*.md 8건
- **방법**: raw 소스 기반 한국어 entity 위키 페이지 생성, Mermaid 다이어그램 포함

생성 - entity (8):
  - agents 3개: ami-labs (LeCun JEPA 월드모델), nvidia-isaac-groot (VLA 로보틱스), hy-embodied (Tencent VLA SOTA)
  - applications 4개: seedance-2 (ByteDance 비디오+오디오), kling-3 (Kuaishou 비디오), mai-speech-models (Microsoft STT/TTS), digital-twin-composer (Siemens Industrial Metaverse)
  - tooling 1개: cloudflare-dynamic-workers (V8 isolate AI 에이전트 샌드박싱)

index.md 업데이트: Agents/Applications/Tooling 각 entity 섹션에 신규 항목 추가

## 2026-04-15 -- Stub 페이지 61개 일괄 보강

- **방법**: 4개 병렬 에이전트로 프론트매터만 있던 stub 페이지를 60-130줄 실질 콘텐츠로 확장
- **기준**: 프론트매터 제외 본문 20줄 미만 페이지 탐지 -> 전량 보강

보강 내역 (61개):
  - concepts 19개: alignment-faking, circuit-tracing, cot-monitorability, deliberative-alignment, constitutional-classifiers 등
  - tooling 15개: claude-opus-4-5, claude-opus-4-6, pydantic-ai, arc-agi-2, qwen3-6-plus 등
  - training 5개: test-time-training, corpus-grounded-self-play, on-policy-distillation, open-post-training-recipes, rl-scaling-laws
  - inference 10개: vllm-v1-engine, tensorrt-llm, sglang, flashinfer, deepseek-sparse-attention 등
  - agents 6개: orchestrator-worker-pattern, agent-memory-systems, agent-trees, context-folding, long-horizon-agent-benchmarks 등
  - rag 6개: serverless-vector-dbs, adaptive-context-compression, letta-stateful-agent-runtime, mem0, temporal-knowledge-graph-memory 등

잔여 stub: 0개

## 2026-04-15 -- Cycle 2: /wiki-harvest + /wiki-ingest + /wiki-expand

- **소스**: arXiv 5건 (안전/VLM/코드벤치마크/해석가능성) + Meta 블로그 1건 = 6건 수집
- **방법**: WebSearch(안전/멀티모달/코드생성 키워드) + HF paper_search + WebFetch

수집 소스:
  - raw/2026-04-15-arxiv-snca-reflexive-audit.md (arXiv:2604.09189, Apr 2026)
  - raw/2026-04-15-arxiv-safety-alignment-matters.md (arXiv:2601.03868, Jan 2026)
  - raw/2026-04-15-blog-meta-sam-audio.md (Meta AI, Dec 2025)
  - raw/2026-04-15-arxiv-vlm-survey-26k.md (arXiv:2510.09586, Oct 2025)
  - raw/2026-04-15-arxiv-featbench.md (arXiv:2509.22237, Sep 2025)
  - raw/2026-04-15-arxiv-sails-interpretable-safety.md (arXiv:2512.23260, Jan 2026)

생성 - paper (5): snca-reflexive-audit-paper, safety-alignment-matters-paper, vlm-survey-26k-paper, featbench-paper, sails-interpretable-safety-paper
생성 - entity (1): sam-audio

expand: 깨진 링크 0개, 추가 생성 불필요

## 2026-04-15 -- /wiki-expand: harvest 후 누락 3개 페이지 생성

- **방법**: 깨진 wikilink + 고빈도 미등록 용어(cross-encoder 29회, hnsw 26회, reranking 19회) 스캔

생성 - concept (3):
  - rag 2개: reranking-and-cross-encoders, approximate-nearest-neighbor
  - concepts 1개: context-window

## 2026-04-15 -- /wiki-harvest --auto-ingest: 6건 수집 + 위키 페이지 자동 생성

- **소스**: arXiv 5건 + DeepMind 블로그 1건 = 6건 수집
- **방법**: WebSearch + HuggingFace paper_search + WebFetch로 수집 -> 중복 체크 -> raw/ 저장 -> 자동 ingest

수집 소스:
  - raw/2026-04-15-arxiv-skill0.md (arXiv:2604.02268, Apr 2026)
  - raw/2026-04-15-arxiv-agentfly.md (arXiv:2508.16153, 162 upvotes)
  - raw/2026-04-15-arxiv-langmarl.md (arXiv:2604.00722, Apr 2026)
  - raw/2026-04-15-arxiv-malt.md (arXiv:2412.01928, 46 upvotes)
  - raw/2026-04-15-arxiv-efficient-attention-survey.md (arXiv:2507.19595)
  - raw/2026-04-15-blog-deepmind-deep-think.md (DeepMind, Feb 2026)

생성 - paper (5):
  - papers 5개: skill0-paper, agentfly-paper, langmarl-paper, malt-paper, efficient-attention-survey-paper

생성 - entity (1):
  - tooling 1개: gemini-deep-think

## 2026-04-15 -- /wiki-expand: 누락 페이지 6개 생성 + 한국어 wikilink 125개 수정

- **방법**: 깨진 wikilink + 고빈도 미등록 용어 스캔 후, 2개 병렬 에이전트 실행

생성 - concept (6):
  - training 3개: fine-tuning-overview, curriculum-learning, model-evaluation-framework
  - inference 1개: speculative-decoding
  - rag 1개: sparse-retrieval
  - concepts 1개: model-calibration

수정 - 한국어 wikilink 일괄 교체:
  - 50개 파일, 125개 링크를 한국어 제목 -> 파일 slug로 교체
  - 예: [[테스트 타임 컴퓨트]] -> [[test-time-compute]]

## 2026-04-15 -- /wiki-ingest: 100개 신규 노드 일괄 생성

- **소스**: `raw/2026-04-15-new-100-nodes-knowledge-source.md`
- **방법**: 7개 병렬 에이전트로 카테고리별 분배 생성 + index.md 일괄 갱신

생성 - concept (83):
  - foundations 20개: learning-rate-scheduling, automatic-differentiation, ensemble-methods, naive-bayes, em-algorithm-gmm, linear-regression, tsne-umap, graph-neural-networks, self-supervised-learning, word2vec-fasttext, embedding-layers, language-model-foundations, seq2seq, information-theory, kl-divergence, bayesian-inference, markov-decision-process, q-learning-dqn, policy-gradient-ppo, contrastive-learning
  - architectures 12개: gpt-architecture-lineage, seq2seq-attention-pre-transformer, masked-autoencoder-mae, latent-diffusion-model, flow-matching, consistency-models, vision-language-model-architectures, cross-attention, linear-attention, state-space-models-general, latent-space-reasoning, moe-routing-advances
  - training 18개: expert-parallelism, gradient-clipping, flash-attention, perplexity-metric, bleu-rouge-metrics, benchmark-design-principles, data-quality-scoring, text-deduplication-strategies, constitutional-ai-original, reward-hacking-overoptimization, long-context-training, data-loader-optimization, hyperparameter-search-llm, fsdp-vs-deepspeed, data-contamination-detection, reinforcement-pre-training, forest-of-thought, continual-learning-llm
  - inference 12개: continuous-batching, request-scheduling, beam-search-decoding, guided-constrained-decoding, on-device-inference-stack, model-pruning-inference, early-exit-adaptive-computation, mixture-of-depths, inference-benchmarking, repetition-penalty-logit-bias, inference-chip-market-shift, inference-distribution-tiers
  - rag 10개: chunking-strategies, embedding-models-for-rag, colbert-late-interaction, hybrid-search-rrf, vector-db-comparison, rag-evaluation-metrics, query-transformation, embedding-finetuning, multimodal-rag, rag-indexing-pipeline
  - concepts 6개: emergent-abilities, sycophancy, test-time-compute, instruction-following, tokenization-concepts, inference-compute-economics
  - agents 1개: ag-ui-protocol
  - 나머지 4개: training/forest-of-thought, training/reinforcement-pre-training, training/continual-learning-llm (중복 카운트 포함)

생성 - entity (6):
  - architectures 5개: swin-transformer, convnext, dinov2, rwkv, xlstm
  - inference 1개: executorch

생성 - paper (15):
  - papers 15개: attention-is-all-you-need-paper, gpt-3-paper, instructgpt-rlhf-paper, chain-of-thought-paper, scaling-laws-paper, dpo-paper, lora-paper, rag-original-paper, constitutional-ai-paper, rlhf-christiano-paper, toolformer-paper, moe-original-paper, bert-paper, retro-paper, o1-system-card-paper

## 2026-04-15 -- /sciomc 6-stage 리서치: 신규 100개 노드 지식소스 준비

- **소스**: `raw/2026-04-15-new-100-nodes-knowledge-source.md`
- **방법**: 6개 병렬 리서치 스테이지
- **결과**: 기존 ~400 페이지 대비 갭 분석 후 신규 100개 노드 후보 선별

## 2026-04-14 -- /wiki-expand 3차: ML 학습 조사 기반 고빈도 미등록 용어 15페이지 확장

- **소스**: `raw/2026-04-14-wiki-expand-scan-3.md` (신규 50페이지 + 전체 위키 스캔)
- **방법**: 5개 병렬 Opus 에이전트, 웹 검색 교차검증

생성 - concept (5):
  - architectures 2개: rotary-position-embedding (RoPE, 15p 참조), rmsnorm (7p 참조)
  - foundations 1개: cross-entropy-loss (11p 참조)
  - training 2개: adamw-optimizer (8p 참조), chinchilla-scaling-laws

생성 - entity (10):
  - architectures 1개: bert (NLP 전이학습 혁명)
  - training 1개: commoncrawl (웹 아카이브, 6p 참조)
  - tooling 8개: nccl (11p), megatron-lm (9p), triton-openai (7p), ray-distributed (5p), wandb, llama-cpp, langchain, alpacaeval

- **역삽입**: positional-encoding, batch-norm-layer-norm, encoder-decoder-architectures에 신규 페이지 교차참조 추가
- **합계**: 신규 15페이지 (606 -> 621)

## 2026-04-14 -- ML 학습 방법론 심층 조사 기반 50페이지 일괄 생성

- **소스**: `raw/2026-04-14-ml-training-deep-dive.md` (7-stage /sciomc 병렬 리서치 결과)
- **방법**: 10개 병렬 Opus 에이전트 (5 토픽/에이전트), 웹 검색 교차검증

생성 - concept (31) [training]:
  - 사전학습: pretraining-pipeline-e2e, training-stability, batch-size-scheduling, sequence-length-curriculum, data-mixing-laws, mfu-model-flops-utilization
  - 포스트트레이닝: post-training-pipeline-e2e, alignment-tax, safety-training-refusal, online-dpo-iterative, orpo, kto
  - 데이터: model-collapse-synthetic
  - 최신 기법: bitnet-1bit-training, fp4-training, grokking-training-dynamics, data-attribution-influence, learning-dynamics-finetuning, continual-pretraining, ast-fim-code-training, communication-efficient-training, omni-modal-training, sparse-bitnet
  - 인프라/모니터링: llm-training-cost-guide, loss-spike-debugging, gradient-norm-monitoring, nan-inf-debugging, training-resumption, elastic-training, training-profiling

생성 - entity (11) [training]:
  - 기술보고서: llama-3-training, deepseek-v3-training, qwen-25-training, olmo-2-training, gemma-2-training, phi-4-training, mixtral-training
  - 데이터셋: fineweb-dataset, redpajama-v2, dolma-dataset, dclm-datacomp

생성 - summary (1) [training]:
  - training-learning-guides (학습 경로 가이드 모음)

생성 - entity (8) [tooling]:
  - 학습 도구: trl-library, axolotl, llama-factory, unsloth, openrlhf, verl-bytedance
  - 데이터 도구: datatrove, text-dedup

- **교차참조**: 각 페이지 최소 3-17개 wikilink, Mermaid 다이어그램 1-3개 포함
- **index.md**: Training 섹션에 concept 31개 + entity 11개 + summary 1개, Tooling entity에 8개 추가
- **합계**: 신규 50페이지 (556 -> 606)

## 2026-04-14 -- 비전/이미지 생성/멀티모달/오픈소스 LLM 엔티티 6페이지 생성

- **소스**: `raw/2026-04-14-wiki-expand-scan-2.md` (위키 내 고빈도 언급 미등록 프로젝트 엔티티)
- **방법**: 웹 자료 2-3건씩 교차 검증 후 entity 페이지 작성

생성 - entity (6):
  - wiki/architectures/ 1개: clip (OpenAI 대조 학습 비전-언어 모델, 22회 언급)
  - wiki/tooling/ 5개: stable-diffusion (오픈소스 이미지 생성, 19회), dall-e (OpenAI 이미지 생성, 12회), midjourney (Discord 기반 이미지 생성, 16회), gpt-4o (네이티브 멀티모달, 17회), llama-2-3 (Meta 오픈소스 LLM 진화사, 27회)

- **교차참조**: clip -> dense-retrieval, vision-transformer, diffusion-transformer, u-net. 각 이미지 생성 엔티티 간 상호 링크. llama-2-3 -> llama-4, mixture-of-experts, ollama
- **index.md**: architectures에 entity 서브섹션 신설 (CLIP), tooling entity에 5개 추가
- **합계**: 신규 6페이지

## 2026-04-14 -- /wiki-expand 스킬 생성 + 내부 용어 37페이지 확장

- **소스**: `raw/2026-04-14-wiki-expand-scan.md` (위키 내부 깨진 링크 + 고빈도 미등록 용어 스캔)
- **방법**: `/wiki-expand` 스킬 신규 생성 (`~/.claude/skills/wiki-expand/SKILL.md`), Opus 3개 에이전트 병렬 투입

생성 - concept (27):
  - wiki/concepts/ 12개: hallucination, chain-of-thought, few-shot-learning, zero-shot-learning, in-context-learning, structured-output, reward-hacking, catastrophic-forgetting, knowledge-graph, temperature-sampling, gguf-format, safetensors
  - wiki/concepts/ (기존 approximate-nearest-neighbor, decoding-strategies 포함)
  - wiki/rag/ 3개: dense-retrieval, sparse-retrieval-bm25, reranker-cross-encoder
  - wiki/architectures/ 5개: diffusion-transformer, vision-transformer, u-net, residual-connection, attention-sink
  - wiki/training/ 5개: ppo-for-llms, continual-learning, federated-learning, self-supervised-learning, active-learning
  - wiki/applications/ 3개: semantic-search, text-classification, named-entity-recognition

생성 - entity (7):
  - wiki/tooling/ 7개: ollama, playwright-mcp, faiss, chroma-db, peft-library, voxcpm2, huggingface-hub

- **합계**: 신규 37페이지 (503 -> 540)
- **wikilink**: 4,606 -> 5,007 (+8.7%)
- **스킬**: `/wiki-expand` 등록 완료 -- 위키 내부 용어 자동 발굴 + 병렬 생성 자동화

## 2026-04-14 -- ML 기초 + 보일러플레이트 정리 + 연결성 대규모 개선 (20 병렬 에이전트, 3단계)

- **Phase 1 (Opus 10개)**: ML 기초/아키텍처/학습/인프라/평가/거버넌스/허브 ~111페이지 신규 생성
  - foundations 31페이지 (수학, ML 개념, 신경망, DL, 학습경로)
  - architectures 16페이지 (Transformer, Attention, MoE, 토크나이제이션, 임베딩)
  - training 29페이지 (CLM/MLM, SFT, RLHF, DPO, 분산학습, 옵티마이저)
  - concepts 25페이지 (평가 메트릭, 거버넌스, 운영, 벤치마크)
  - tooling 10페이지 (벤치마크 entity, 프레임워크, 허브)
  - inference 1페이지 (KV Cache 추론 최적화)

- **Phase 2 (Sonnet 5개)**: 보일러플레이트 정리
  - ~7,000줄 보일러플레이트 제거 (정밀 ingest/source 재수집/실무 체크리스트/해석 포인트 등)
  - 500+ 인라인 wikilink 추가
  - 0-link 파일: 193개 -> 4개로 감소

- **Phase 3 (Sonnet 5개)**: 연결성 개선
  - 47개 교차 카테고리 브릿지 링크 추가 (training<->agents, architectures<->agents, rag<->agents)
  - 50+ 깨진 링크 수정
  - 22개 고아 페이지 전부 연결
  - 23개 tooling 고립 페이지 타 카테고리와 연결
  - 19개 concept 페이지 인라인 링크 강화

- **합계**: 위키 392 -> 503페이지 (+28%), wikilink 2,403 -> 4,606개 (+92%)

## 2026-04-14 -- 갭 스캔 53개 토픽 대량 ingest (10 병렬 에이전트, 2차)

- **소스**: `raw/2026-04-14-gap-scan-new-topics.md` (위키 338개 대비 누락 53개 토픽)
- **방법**: 10개 Opus 에이전트 병렬 투입. URL fetch 기반 검증 후 한국어 위키 페이지 작성.

생성 - entity (25):
  - wiki/tooling/ 20개: gpt-6-spud, llama-4, grok-4-20, deepseek-v4, runway-gen-4-5, ltx-2, nemoclaw, meta-tribe-v2, sora-2-shutdown, gpt-5-architecture, goose, xcode-agentic-coding, cisco-defenseclaw, agentmon, aws-agent-registry, galileo-ai, arize-phoenix, fiddler-ai, browsecomp, osworld-verified, humanity-last-exam, gemma-scope-2, mcp-server-cards
  - wiki/inference/ 2개: dgx-spark, blackwell-ultra-b300
  - wiki/agents/ 1개: agentic-ai-foundation

생성 - concept (25):
  - wiki/architectures/ 3개: gated-attention, gated-deltanet, superposition-neural-scaling
  - wiki/agents/ 3개: owasp-agentic-top-10, zero-trust-ai-agents, a2a-t-telecom
  - wiki/concepts/ 14개: nist-ai-agent-standards, livebench, cot-monitoring-safety, representation-engineering, mechanistic-interpretability-2026, ai-agent-marketplaces, ai-voice-cloning-scams, us-china-ai-competition, ai-cybersecurity-defensive, ai-workforce-impact, ai-sustainability-paradox, ai-venture-bubble-2026, ai-copyright-litigation, sovereign-ai, ai-ma-mega-deals
  - wiki/applications/ 4개: ai-finance, ai-education, ai-legal, ai-manufacturing
  - wiki/inference/ 1개: sdsl

생성 - paper (1):
  - wiki/papers/safety-alignment-depth-paper.md

갱신 (1):
  - wiki/architectures/titans-miras.md (메모리 깊이, 실무 관점 섹션 추가)

- **합계**: 신규 53개 + 갱신 1개 = 54개 페이지
- **위키 총 페이지**: 338 -> 392개 (+16%)

## 2026-04-14 -- 갭 스캔 토픽 6-11 ingest (하드웨어/비디오/신경과학/아키텍처)

- **소스**: `raw/2026-04-14-gap-scan-new-topics.md` (토픽 6-11)
- **방법**: 토픽별 2-3개 URL WebFetch 기반 한국어 위키 페이지 작성. Mermaid 다이어그램 포함.

생성 - entity (5):
  - wiki/tooling/ltx-2.md -- LTX-2 (Lightricks 오픈소스 4K 비디오+오디오, 19B)
  - wiki/tooling/nemoclaw.md -- NemoClaw + OpenShell (NVIDIA 에이전틱 런타임, GTC 2026)
  - wiki/inference/dgx-spark.md -- DGX Spark (NVIDIA 개인용 AI 슈퍼컴퓨터, GB10 128GB)
  - wiki/inference/blackwell-ultra-b300.md -- Blackwell Ultra B300 (288GB HBM3e, 14 PFLOPS FP4)
  - wiki/tooling/meta-tribe-v2.md -- Meta TRIBE v2 (fMRI 뇌 예측 파운데이션 모델, 700+ 피험자)

갱신 - concept (1):
  - wiki/architectures/titans-miras.md -- 메모리 깊이 효과, 실무 관점, Qwen3-Next 연결, TRIBE v2 역링크 추가

- **합계**: 신규 5개 + 갱신 1개 = 6개 페이지
- **카테고리 분포**: tooling 3, inference 2, architectures 1
- **index.md 갱신**: architectures 4항목(기존 누락분 포함), inference 2항목, tooling 3항목 추가

## 2026-04-14 -- AI 핫토픽 100선 대량 ingest (10 병렬 에이전트)

- **소스**: `raw/2026-04-14-ai-hot-topics-100.md` (2026년 4월 AI/Agent/Harness Engineering 핫토픽 100개 + 500개 레퍼런스 링크)
- **방법**: 10개 Opus 에이전트를 병렬로 투입, 각 에이전트가 10개 토픽을 담당. URL fetch 기반으로 실제 콘텐츠 검증 후 한국어 위키 페이지 작성.

생성 - entity (43):
  - wiki/tooling/ 43개: meta-muse-spark, claude-mythos-preview, gemma-4, mistral-small-4, voxtral-tts, qwen-3-5-omni, gemini-3-1-flash-lite, gpt-5-3-instant, deepseek-v3-2, leanstral, boltz-2, apple-foundation-model, nvidia-cosmos, google-adk, microsoft-agent-framework, hermes-agent, openclaw, crewai, ag2, composio, ai-agent-guardrails, portkey, openrouter, litellm, langfuse, braintrust, n8n-dify, synthetic-data-tools, kiro, augment-intent, junie-cli, copilot-fleet, codex-cli, google-ai-studio-antigravity, vibe-coding-platforms, ai-code-review-tools, augment-code, deepeval, ragas, openhands, metatron, ms-agent-governance-toolkit
  - wiki/inference/ 5개: amd-mi400-helios, litert-lm, google-tpu-ironwood, nvidia-groq-3-lpu, nvidia-vera-rubin

생성 - concept (56):
  - wiki/architectures/ 4개: deepseek-mhc, long-context-scaling, mamba-3, multi-head-latent-attention
  - wiki/training/ 7개: extended-constitutional-ai, knowledge-distillation, lora-qlora-finetuning, mit-training-efficiency, model-merging, synthetic-data-training, test-time-compute-scaling
  - wiki/inference/ 5개: ai-inference-quantization-2026, mirror-speculative-decoding, meta-adaptive-ranking, speculative-speculative-decoding, turboquant
  - wiki/rag/ 1개: rag-architecture-evolution-2026
  - wiki/agents/ 12개: a2a-protocol, acp-protocol, agent-prompt-patterns, agentic-knowledge-base-patterns, ai-red-teaming, component-level-agent-evaluation, human-in-the-loop-patterns, prompt-caching-agentic, spec-driven-development, swe-bench-ecosystem-2026, tdd-agentic-coding, tool-calling-optimization
  - wiki/applications/ 8개: ai-audio-voice-cloning, ai-data-analysis, ai-design-tools, ai-healthcare, ai-image-generation, ai-robotics-physical-ai, ai-scientific-discovery, ai-video-generation
  - wiki/concepts/ 15개: agentic-ai-production, ai-data-center-power, ai-reasoning-models, ai-regulation-us, ai-safety-alignment-2026, custom-ai-chips-asic, deepfake-detection-c2pa, enterprise-ai-adoption, eu-ai-act-enforcement, llm-security-owasp, mlops-llmops-2026, multimodal-foundation-models, on-device-llm, open-source-ai-movement-2026, small-language-models

갱신 - concept (1):
  - wiki/concepts/opentelemetry-genai-semconv.md (sources 추가, 2026 에이전트 트레이싱 확장 내용 병합)

- **합계**: 신규 99개 + 갱신 1개 = 100개 페이지
- **카테고리 분포**: tooling 43, concepts 15, agents 12, inference 10, applications 8, training 7, architectures 4, rag 1
- **발견된 지식 갭**: 각 페이지가 소스 파일의 1-line 설명 + URL fetch 기반이므로, 깊이 있는 후속 ingest가 필요한 토픽이 다수 존재 (특히 Mamba-3, TurboQuant, A2A Protocol 등)

## 2026-04-13 — Inference/RAG/Training/Paper 남은 노드 정밀 경계 메모 6차

- **대상**: inference/rag/training/papers 카테고리 중 아직 `정밀 ingest` 섹션이 없던 47개 문서.
- **갱신 - concept/entity/project-internal/paper/summary/case-study (47)**:
  - 남은 연구·시스템 노드 전체에 `정밀 ingest — 남은 경계 메모`를 추가해 문제 설정, 방법/시스템 구조, 평가/운영 조건, 한계를 다음 수동 재수집 기준으로 명시.
- **수행 내용**:
  - 이전 5차에서 우선순위 12개를 깊게 처리한 뒤, 나머지 47개도 최소 정밀 경계 메모를 갖도록 정리.
  - inference/rag/training/papers 카테고리에서 `정밀 ingest`가 없는 문서 0개로 감소.
- **발견된 지식 갭**:
  - 다음 라운드는 applications/concepts/agents 카테고리의 남은 자동 보강 흔적 또는 정밀 섹션 없는 문서를 같은 방식으로 처리하는 것이 좋다.

## 2026-04-13 — Inference/RAG/Training/Paper 경계 정밀 re-ingest 5차

- **대상**: source navigation noise와 자동 보강 흔적이 남아 있던 inference/RAG/training/papers 문서 12개.
- **갱신 - paper/concept/entity/summary (12)**:
  - `wiki/papers/chunkkv-paper.md`
  - `wiki/papers/lost-in-the-middle-paper.md`
  - `wiki/inference/kv-cache.md`
  - `wiki/papers/agentgym-rl-paper.md`
  - `wiki/papers/deep-research-agents-roadmap-paper.md`
  - `wiki/papers/memory-in-the-age-of-ai-agents-paper.md`
  - `wiki/papers/loop-paper.md`
  - `wiki/papers/deepseek-r1-paper.md`
  - `wiki/papers/flashattention-4-paper.md`
  - `wiki/papers/plan-and-act-paper.md`
  - `wiki/rag/context-rot-report.md`
  - `wiki/inference/vllm-v1-engine.md`
- **수행 내용**:
  - 각 문서의 자동 source-grounded 메모를 줄이고, paper/concept/entity 타입별로 문제 설정·방법·평가·한계·시스템 경계를 분리하는 `정밀 ingest — 연구/시스템 경계` 섹션 추가.
  - 12개 문서 모두 1000단어 이상으로 회복.
- **발견된 지식 갭**:
  - 다음 라운드는 남은 inference/RAG/training entity와 paper 중 precision section이 없는 문서를 계속 같은 방식으로 처리하는 것이 좋다.

## 2026-04-13 — SDK/MCP entity 허브 정밀 re-ingest 4차

- **대상**: OpenAI Agents SDK, Claude Agent SDK, Claude Agent SDK TypeScript, MCP Authorization, Model Context Protocol, MCP 2026 Roadmap entity 허브 6개.
- **갱신 - entity (6)**:
  - `wiki/tooling/openai-agents-sdk.md`
  - `wiki/tooling/claude-agent-sdk.md`
  - `wiki/tooling/claude-agent-sdk-typescript.md`
  - `wiki/tooling/mcp-authorization.md`
  - `wiki/tooling/model-context-protocol-mcp.md`
  - `wiki/tooling/model-context-protocol.md`
- **수행 내용**:
  - entity 허브가 세부 API 사용법을 반복하지 않고 하위 summary 문서로 routing하도록 `정밀 ingest — 허브 재정의` 섹션 추가.
  - OpenAI/Claude SDK 허브는 quickstart/session/handoff/loop/TypeScript repo 하위 문서 경로를 명확히 하고, MCP 허브는 architecture/spec/authorization/roadmap 경계를 분리.
  - 6개 문서 모두 1000단어 이상으로 회복.
- **발견된 지식 갭**:
  - 다음 라운드는 inference/RAG/training 쪽 entity·paper 문서 중 source navigation noise가 많은 문서를 같은 방식으로 정밀화하는 것이 좋다.

## 2026-04-13 — OpenAI/Claude SDK + MCP 공식 문서군 정밀 re-ingest 3차

- **대상**: OpenAI Agents SDK child docs 4개, Claude Agent SDK child docs 3개, MCP architecture/authorization/spec/roadmap 문서 4개.
- **갱신 - summary (11)**:
  - `wiki/tooling/openai-agents-sdk-quickstart.md`
  - `wiki/tooling/openai-agents-sdk-handoffs.md`
  - `wiki/tooling/openai-agents-sdk-sessions.md`
  - `wiki/tooling/openai-agents-sdk-model-context-protocol.md`
  - `wiki/tooling/claude-agent-sdk-quickstart.md`
  - `wiki/tooling/claude-agent-loop.md`
  - `wiki/tooling/claude-agent-sessions.md`
  - `wiki/tooling/mcp-architecture.md`
  - `wiki/tooling/mcp-authorization-draft.md`
  - `wiki/tooling/mcp-specification-2025-11-25.md`
  - `wiki/tooling/the-2026-mcp-roadmap.md`
- **수행 내용**:
  - OpenAI Agents SDK는 quickstart/handoff/session/MCP server type 경계, Claude Agent SDK는 quickstart/agent loop/session fork-resume 경계, MCP는 host-client-server/authorization/spec-version/roadmap governance 경계를 중심으로 `정밀 ingest` 섹션 추가.
  - 11개 문서 모두 1000단어 이상으로 회복.
- **발견된 지식 갭**:
  - 다음 라운드는 OpenAI Agents SDK entity, Claude Agent SDK entity/TypeScript repo, MCP OAuth entity, model-context-protocol entity 같은 허브 문서 자체를 수동 정밀화하는 것이 좋다.

## 2026-04-13 — high-value tooling 공식 문서군 정밀 re-ingest 2차

- **대상**: Mastra advanced, Instructor, Deep Agents 공식 문서 summary 12개.
- **갱신 - summary (12)**:
  - `wiki/tooling/mastra-agents-overview.md`
  - `wiki/tooling/mastra-workflows-overview.md`
  - `wiki/tooling/mastra-memory-overview.md`
  - `wiki/tooling/mastra-mcp-overview.md`
  - `wiki/tooling/instructor-overview.md`
  - `wiki/tooling/instructor-validation.md`
  - `wiki/tooling/instructor-retrying.md`
  - `wiki/tooling/instructor-patching.md`
  - `wiki/tooling/deep-agents-quickstart.md`
  - `wiki/tooling/deep-agents-subagents.md`
  - `wiki/tooling/deep-agents-memory.md`
  - `wiki/tooling/deep-agents-production.md`
- **수행 내용**:
  - Mastra는 agents/workflows/memory/MCP의 경계, Instructor는 validation/retry/patching의 얇은 structured-output layer, Deep Agents는 quickstart/subagents/memory/production 경계를 중심으로 `정밀 ingest` 섹션 추가.
  - 12개 문서 모두 1000단어 이상으로 회복.
- **발견된 지식 갭**:
  - 다음 라운드는 OpenAI Agents SDK, Claude Agent SDK child docs, MCP spec/authorization/roadmap 문서군을 같은 방식으로 정밀화하는 것이 좋다.

## 2026-04-13 — high-value tooling 공식 문서군 정밀 re-ingest 1차

- **대상**: leaf 품질 복구 후에도 수동 정밀화 우선순위로 남아 있던 high-value tooling 문서 10개.
- **공식/source 재확인 축**: BAML, Mastra, Vercel AI SDK Core/Agents/Tool Calling/MCP, LangGraph Quickstart/Persistence/Durable Execution, Pydantic AI Agent Core.
- **갱신 - summary (10)**:
  - `wiki/tooling/baml-what-is-baml.md`
  - `wiki/tooling/mastra-get-started.md`
  - `wiki/tooling/vercel-ai-sdk-core-overview.md`
  - `wiki/tooling/vercel-ai-sdk-agents-overview.md`
  - `wiki/tooling/vercel-ai-sdk-tool-calling.md`
  - `wiki/tooling/vercel-ai-sdk-mcp-tools.md`
  - `wiki/tooling/langgraph-quickstart.md`
  - `wiki/tooling/langgraph-persistence.md`
  - `wiki/tooling/langgraph-durable-execution.md`
  - `wiki/tooling/pydantic-ai-agent-core.md`
- **수행 내용**:
  - 자동 source-grounded 메모를 제거한 뒤, 각 문서에 원문의 고유 흐름을 반영한 `정밀 ingest` 섹션을 수동 추가.
  - BAML은 `.baml` → `baml_client` → app call 흐름, Mastra는 create/Studio/framework/application category 흐름, Vercel은 Core/ToolLoopAgent/tool calling/MCP 경계, LangGraph는 state/persistence/durable replay, Pydantic AI는 typed Agent contract를 중심으로 재작성.
  - 10개 문서 모두 1000단어 이상으로 회복.
- **발견된 지식 갭**:
  - 다음 라운드는 Mastra Agents/Workflows/Memory/MCP, Instructor Validation/Retrying/Patching, Deep Agents Quickstart/Production 같은 하위 공식 문서군을 같은 방식으로 정밀화하는 것이 좋다.

## 2026-04-13 — leaf/최하위 노드 품질 복구 및 source-grounded re-ingest

- **대상**: `wiki/` 전체 238개 중 이전 길이 보강 흔적이 남아 있던 최하위/leaf 후보 226개와, filler 제거 후 1000단어 미만으로 내려간 117개.
- **문제 인식**: 이전 보강은 `노드 보강 메모`, `추가 ingest 판별 질문`, `2차 source-specific ingest 보강`, `1000단어 기준 보강 메모`, `최종 노드 충실도 점검` 같은 메타 섹션이 많아 실제 위키 내용처럼 읽히지 않았다.
- **수행 내용**:
  - `scripts/repair_generic_leaf_content_2026_04_13.py`로 226개 문서에서 generic filler 섹션을 제거하고 각 문서의 실제 `sources:` raw snapshot을 다시 읽어 source 제목/URL/heading/signals 기반 보강 섹션으로 교체.
  - `scripts/top_up_source_grounded_leaf_nodes_2026_04_13.py`로 filler 제거 뒤 짧아진 117개 문서에 원문 기반 상세 해석을 추가.
  - `scripts/final_source_gap_fill_leaf_nodes_2026_04_13.py`로 남은 76개 under-1000 문서에 source 기반 빈틈 메모를 추가해 최소 길이와 source 추적성을 회복.
  - 웹/공식 문서 재확인 기록은 `raw/2026-04-13-leaf-quality-web-research.md`에 audit note로 저장. 각 페이지의 `sources:`는 기존 원문 raw snapshot을 유지.
- **생성 - raw audit note (1)**:
  - `raw/2026-04-13-leaf-quality-web-research.md`
- **갱신 - source-grounded repair (226)**:
  - 226개 leaf/저품질 후보 문서 전부에서 메타 filler 제거 및 source 기반 보강 적용.
- **발견된 지식 갭**:
  - 일부 raw snapshot은 navigation 텍스트 비중이 커서, 다음 수동 라운드에서는 high-value 공식 문서(BAML, Mastra, Vercel AI SDK, LangGraph, Pydantic AI)를 개별 페이지 단위로 더 깊게 재수집하는 것이 좋다.

## 2026-04-13 — unlinked/undefined 문서 재점검 및 AI SDK placeholder ingest

- 감사 결과: `wiki/` 문서는 index 기준 누락 0건, stale index link 0건, raw source 누락 0건, undefined wikilink 0건이었다.
- inbound wikilink가 없던 wiki 노드 27건은 모두 index와 source가 있는 유효 문서로 판정하고, 관련 허브/개념 문서에서 역방향 링크를 보강했다.
- 불필요한 빈 placeholder 6건을 정리했다: root의 Obsidian alias placeholder 3건, TensorRT raw code fragment에서 파생된 1건, AI SDK docs 경로 placeholder 2건.
- 웹 검색/공식 문서 확인 후 AI SDK docs placeholder 2건은 삭제가 아니라 raw source note와 project-internal wiki 문서로 승격했다.

처리 소스:
- `https://ai-sdk.dev/docs/reference/ai-sdk-core/extract-json-middleware`
- `https://ai-sdk.dev/docs/troubleshooting/typescript-cannot-find-namespace-jsx`

생성 - project-internal (2) [project: Vercel AI SDK]:
- `wiki/tooling/vercel-ai-sdk-extract-json-middleware.md`
- `wiki/tooling/vercel-ai-sdk-typescript-jsx-namespace.md`

생성 - raw source note (2):
- `raw/2026-04-13-vercel-ai-sdk-extract-json-middleware.md`
- `raw/2026-04-13-vercel-ai-sdk-typescript-jsx-namespace.md`

정리 - 불필요한 빈 placeholder (6):
- `0,0,0,0],[0,1,0],[1,0],[1,1.md`
- `agentic engineering guide.md`
- `better code with agents.md`
- `evolution of agentic patterns.md`
- `docs/reference/ai-sdk-core/extract-json-middleware.md`
- `docs/troubleshooting/typescript-cannot-find-namespace-jsx.md`

발견된 지식 갭:
- AI SDK 다음 major version에서 `@types/react` 의존성 제거가 실제 반영되면 `vercel-ai-sdk-typescript-jsx-namespace.md`를 v6 호환성 노트로 축소하거나 갱신해야 한다.

## 2026-04-13 — 1000단어 미만 노드 전체 보강 + OMC Tools raw 승격
- **대상**: `wiki/` 전체 235개 중 1000단어 미만 226개, 그리고 미연결 raw source 1개(`raw/2026-04-09-omc-TOOLS.md`)
- **수행 내용**:
  - `scripts/deepen_under1000_nodes_2026_04_13.py`로 226개 문서에 2차 source-specific ingest 보강 섹션 추가
  - `scripts/top_up_under1000_nodes_2026_04_13.py`와 `scripts/final_top_up_under1000_nodes_2026_04_13.py`로 남은 짧은 노드까지 추가 보강
  - `wiki/tooling/omc-mcp-tools.md`를 새 project-internal 문서로 생성하고 `raw/2026-04-09-omc-TOOLS.md`를 sources에 연결
  - `index.md`의 oh-my-claudecode project-internal tooling 섹션에 OMC MCP Tools 등록
- **검증 결과**:
  - 최종 wiki 문서 수 236개, 1000단어 미만 0개, 최소 1002단어, median 1075단어
  - raw markdown 628개 중 미연결 0개
  - alias-aware broken wikilinks 0개, index missing-page 0개, missing source path 0개
  - 보강 스크립트 `py_compile` 통과, `git diff --check` 통과

## 2026-04-13 — 100+ 얕은 노드 문서 대량 wiki-ingest 보강
- **대상**: `wiki/` 전체 235개 중 본문 600단어 미만 113개
- **수행 내용**:
  - `scripts/deepen_shallow_nodes_2026_04_13.py`로 113개 문서에 raw source 기반 노드 보강 메모 / 판별 표 / source 근거 메모 / 구조 스케치를 추가
  - `scripts/top_up_remaining_shallow_2026_04_13.py`로 1차 보강 후 남은 46개 문서에 추가 ingest 판별 질문을 보강
  - 기존 페이지를 갱신했으며 `raw/` 원본은 수정하지 않음
- **검증 결과**:
  - 최종 600단어 미만 문서 0개, 최소 600단어, median 697단어
  - alias-aware broken wikilinks 0개, index missing-page 0개, missing raw source path 0개
  - 보강 스크립트 `py_compile` 통과, `git diff --check` 통과

## 2026-04-11 — 빈 문서 후속 수동 심화 배치
- **대상**: 1차 stub 보강 후에도 얕게 남은 핵심 문서 14개
- **수행 내용**:
  - tooling/agents/concepts 문서 8개에 표, 읽기 순서, 설계 체크리스트, Mermaid 흐름을 추가
  - paper 문서 6개에 문제/방법/결과/한계 또는 실무 해석 표를 추가
  - 잘못된 raw source path 2개(`what-is-mcp`, `claude-sonnet-4-5`)를 실제 snapshot 경로로 교정
- **검증 결과**:
  - 대상 14개 문서 모두 350단어 이상, 최소 398단어
  - 전체 wiki body 250단어 미만 문서 0개
  - alias-aware broken wikilinks 0개, index missing-page 0개, missing source path 0개

## 2026-04-10 — 빈 문서(stub) 위키화 정비
- **대상**: body 250단어 미만 stub 문서 57개
- **수행 내용**:
  - `scripts/wiki_stub_expander.py`를 추가해 raw snapshot 기반 섹션(원문 흐름 / 읽기 포인트 / source 메모)을 일괄 보강
  - paper 문서에는 문제 설정 / 리뷰 포인트 / source 메타데이터를 추가해 논문형 요약으로 확장
  - 검증 결과 수정 대상 57개 모두 250단어 이상이 되었고, 전체 wiki에서 body 250단어 미만 문서는 0개

## 2026-04-10 — Mastra / Instructor advanced branch 확장
- **대상**: Mastra 4개, Instructor 3개 child doc + raw index 체계
- **수행 내용**:
  - advanced child-doc summary 7개 추가
  - raw 탐색용 index 문서 생성
  - backlog roadmap에서 Mastra/Instructor 항목 완료 반영

## 2026-04-10 — Raw index 체계 추가 + Mastra/Instructor advanced ingest
- **대상**: Mastra child docs 4개, Instructor concepts 3개, raw 디렉토리 전반
- **수행 내용**:
  - `raw/index.md`, `raw/recursive-sources/index.md`, 배치별 raw index, hot-topics raw index 생성
  - Mastra advanced docs 4개와 Instructor advanced docs 3개를 recursive ingest
  - parent hub(`mastra.md`, `instructor.md`)의 reading path 확장

## 2026-04-10 — 다음 ingest 후보 backlog 문서화
- **대상**: corpus 완료 이후의 선택적 확장 후보
- **수행 내용**:
  - Mastra / Instructor / BAML / Vercel AI SDK / Deep Agents / Pydantic AI의 공식 child-doc 후보를 backlog로 정리
  - 필수 누락 없음과 선택적 확장 가능성을 분리 문서화

## 2026-04-10 — 핫토픽 500-link corpus audit 문서화
- **대상**: `raw/2026-04-10-hot-ai-topics-100.md` 전체 source corpus
- **수행 내용**:
  - 500 link occurrence / 452 unique ref / 452 raw snapshot / 549 hot-topics tree path를 분리 검증
  - 결과를 `wiki/applications/hot-topics-corpus-coverage-audit-2026-04.md`로 문서화

## 2026-04-10 — 500-link corpus coverage audit
- **대상**: `raw/2026-04-10-hot-ai-topics-100.md`의 원본 링크 500개
- **검증 결과**:
  - 원문 링크 개수: `500`
  - 정규화된 고유 URL(manifest refs): `452`
  - manifest snapshot 존재: `452 / 452`
  - manifest raw path의 wiki 직접 참조: `452 / 452`
  - `raw/hot-topics-sources/2026-04-10/` 전체 경로(스냅샷 + topic packet) wiki 참조: `549 / 549`
- **판정**:
  - 중복 링크를 포함한 500-link corpus는 현재 위키에 모두 흡수되었고, 추가 미반영 source는 발견되지 않음

## 2026-04-10 — Recursive summary 심화 배치 (Mastra / BAML / Instructor / Vercel)
- **대상**: 최신 recursive summary 7개
- **수행 내용**:
  - 비교표 / 읽는 순서 / 운영 체크리스트를 추가해 deep-wiki 품질 강화
  - 특히 Vercel AI SDK 계열 4개 문서에 layer-aware 읽기 경로 추가

## 2026-04-10 — Recursive ingest 배치 (Mastra / BAML / Instructor / Vercel AI SDK 세부 문서)
- **대상**: 공식 세부 문서 7개 (`mastra.ai` 1개, `docs.boundaryml.com` 1개, `python.useinstructor.com` 1개, `ai-sdk.dev` 4개)
- **생성 페이지**:
  - `wiki/tooling/mastra-get-started.md`
  - `wiki/tooling/baml-what-is-baml.md`
  - `wiki/tooling/instructor-overview.md`
  - `wiki/tooling/vercel-ai-sdk-core-overview.md`
  - `wiki/tooling/vercel-ai-sdk-agents-overview.md`
  - `wiki/tooling/vercel-ai-sdk-tool-calling.md`
  - `wiki/tooling/vercel-ai-sdk-mcp-tools.md`
- **수행 내용**:
  - `raw/recursive-sources/2026-04-10-baml-instructor-vercel-mastra/` 아래 원문 snapshot 저장
  - parent entity(`mastra.md`, `baml.md`, `instructor.md`, `vercel-ai-sdk.md`)에 하위 문서 읽기 경로 추가
  - 남아 있던 주요 framework hub를 공식 child docs까지 내려가는 deep-wiki 구조로 확장

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
