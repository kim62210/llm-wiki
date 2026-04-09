---
source_url: https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html
title: "프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록"
published: 2026-04-05
fetched: 2026-04-09
category: insights / agentic-ai
tags: [prompt-engineering, context-engineering, harness-engineering, agentic-patterns, llm-architecture, vibe-coding]
---

# 프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록

**Published**: 2026-04-05
**Source**: bits-bytes-nn.github.io Insights / Agentic AI

## Opening Thesis

이 글은 "엔지니어링의 엄밀함은 사라지지 않는다 — 이동할 뿐이다"를 핵심 주장으로 삼는다. Chad Fowler의 [Relocating Rigor](https://www.honeycomb.io/blog/production-is-where-the-rigor-goes) 원칙에서 가져온 개념이다.

### TL;DR

- 2022-2026 사이 AI 개발 패러다임이 세 번 이동: Prompt Engineering → Context Engineering → Harness Engineering
- 각 전환은 "이전 패러다임이 약속을 지키지 못했기 때문"에 일어났다
- 2026년의 핵심 메트릭은 프롬프트 품질이 아니라 KV-캐시 히트율과 하네스 복잡도로 이동
- 이 글은 각 시대가 왜 실패했는지를 추적하는 부검 보고서(autopsy report)다

---

## Section 1: 왜 지금 이 연대기인가?

2025년 6월, AI 타임라인이 "context engineering"을 축으로 회전했다. Shopify CEO Tobi Lütke가 6월 19일 논의를 점화했고, 이어서 Karpathy와 Andrew Ng가 동참했다. 이 용어는 업계 담론에서 "prompt engineering"을 빠르게 대체했다.

Epsilla의 비유는 이 4년을 요약한다:
- **2022**: 완벽한 이메일을 쓰는 법을 연구
- **2025**: 인박스 관리 학습
- **2026**: 이메일 시스템 자체를 설계

---

## Section 2: 프롬프트 엔지니어링 에라 (2022-2024)

### 2.1 GitHub Copilot이 문을 열다

GitHub Copilot은 ChatGPT보다 5개월 빠른 2022년 6월 월 $10로 출시. OpenAI Codex 기반, "ghost text" 자동완성 제공.

**임팩트 메트릭**:
- 개발자 88%가 생산성 향상 보고
- 2024년까지: 2천만 명 이상 사용자, 470만 유료 구독자
- Fortune 100 기업 90% 채택

### 2.2 ChatGPT의 패러다임 전환

2022년 11월 출시: 5일 만에 100만 사용자, 2개월 만에 1억 명.

Andrej Karpathy가 "[Software 3.0](https://www.latent.space/p/s3)" 용어를 제시 — 자연어 지시가 프로그램 자체가 되는 패러다임.

### 2.3 학술적 기반: 프롬프트로 추론을 유도하기

**Chain-of-Thought (CoT) Prompting** — [Wei et al., 2022](https://arxiv.org/abs/2201.11903)

모델이 "단계별로 생각"하도록 유도. GSM8K 벤치마크에서 PaLM 540B 정확도가 17.9%에서 58.1%로 상승.

**ReAct: Reasoning + Acting** — [Yao et al., 2022](https://arxiv.org/abs/2210.03629)

모델이 Thought → Action → Observation을 반복하면서 외부 도구 사용과 환각 감소를 이끌어냄.

**Tree-of-Thought** — [Yao et al., 2023](https://arxiv.org/abs/2305.10601)

여러 추론 경로를 동시에 탐색하지만 프로덕션에서 지수적 비용 폭발을 겪음.

**Self-Refine, Reflexion** — [Madaan et al., 2023](https://arxiv.org/abs/2303.17651), [Shinn et al., 2023](https://arxiv.org/abs/2303.11366)

모델이 자신의 출력을 비평하고 개선. 피드백 품질이 모델 자체 능력에 의존.

### 2.4 Andrew Ng의 4가지 Agentic Design Patterns (2024)

- **Reflection**: 모델이 자기 출력을 셀프 비평. 같은 모델이 다른 페르소나로 질을 올림
- **Tool Use**: 모델이 자율적으로 외부 도구(API, DB, 계산기) 호출 시점을 결정
- **Planning**: 복잡한 작업을 서브태스크로 분해. "악마는 디테일에 있다"
- **Multi-Agent Collaboration**: 역할이 다른 특화 에이전트들이 결과를 교환하며 협력

### 2.5 벽에 부딪히기: 프롬프트의 한계

Mitchell Hashimoto는 "[Blind Prompting](https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting)"을 지적 — 엄밀한 측정 없이 trial-and-error에만 의존하는 최적화.

**구조적 문제**: 모델은 비결정적이다. 완벽한 프롬프트도 컨텍스트 창에 관련 정보가 없으면 실패한다. 진짜 문제는 프롬프트 텍스트가 아니라 불완전한 컨텍스트였다.

---

## Section 3: AI 코딩 도구 폭발과 바이브 코딩 숙취 (2024-2025)

### 3.1 Cursor: "컨텍스트 이해" 에디터

2023년 3월 MIT 졸업생들이 출시. 핵심 혁신: AST 파싱과 시맨틱 검색으로 코드베이스 전체 분석, `@file`, `@codebase`, `@Docs` 참조 제공.

**Cursor Composer 모드 (2024)**: 프로젝트 범위의 다중 파일 동시 편집.

**성장**: 2025년 $1.2B ARR, $29.3B 밸류에이션.

### 3.2 AI 코딩 도구의 캄브리아기 폭발

- **Devin** (Cognition Labs, 2024년 3월): "최초의 AI 소프트웨어 엔지니어"로 마케팅했으나 독립 테스트에서 20개 과제 중 3개만 성공
- **Windsurf**: 자동완성 확장에서 "Cascade" agentic assistant 탑재 풀 IDE로 진화
- **Ralph, Aider, Cline, Void Editor**: 접근 방식의 확산 (오픈소스, 프라이버시 중심, 엔터프라이즈, 터미널 기반)

GitHub 리포 성장: 14개 프레임워크(1,000+ stars) → 1년 후 89개로 증가 (535%).

**개발자 채택**: GitHub 2024 서베이에서 AI 코딩 도구 사용자 92%.

### 3.3 Vibe Coding: 프롬프트 엔지니어링의 극단

2025년 2월: Karpathy가 Cursor 제안을 diff 검토 없이 전부 수락하고 있다고 고백. 코드가 인간 이해 수준을 넘었다는 이유.

"Vibe coding"이라는 용어가 등장 — 검증 없이 AI 생성 변경을 전부 수락하고, 에러는 허용 가능한 비용으로 취급.

**Vibe Coding Hangover (2025년 9월)**: Fast Company가 현실을 보도 — 3개월 된 AI MVP가 투자자 자금을 받았고, 버그가 쌓였으며, 아무도 코드베이스를 이해하지 못했다.

**CodeRabbit 메트릭**:
- AI 생성 코드: 메이저 이슈 1.7배 많음
- 보안 취약점 비율 45% 높음

Simon Willison의 교정: "If you reviewed and tested, it's not vibe coding — it's engineering."

---

## Section 4: 컨텍스트 엔지니어링 에라 (2025년 중반)

### 4.1 기원: 2025년 6월 동시 발견

**2025년 6월 19일**: Tobi Lütke가 "context engineering" 용어 제안 — 모델이 작업을 풀 수 있도록 완전한 컨텍스트를 제공.

**Karpathy의 응답**: 컨텍스트 엔지니어링을 "미묘한 기술과 과학"이 요구되는 작업으로 정의. 컨텍스트 창을 정확히 필요한 정보로 채우는 것.

### 4.2 LLM-as-OS: Karpathy의 운영체제 메타포

| OS 컴포넌트 | 역할 | LLM OS 대응 |
|---|---|---|
| Kernel | 시스템 리소스 관리 | LLM 추론 엔진 |
| RAM | 작업 메모리 | 컨텍스트 창 |
| File system | 영구 저장소 | RAG / 벡터 DB |
| System calls | 하드웨어 제어 | Tool calls / APIs |
| Process management | 멀티태스킹 | 멀티 에이전트 오케스트레이션 |

**핵심 통찰**: 프롬프트는 단일 커맨드 라인 명령어에 불과. 실제 성능은 RAM(컨텍스트 창)에 무엇을 채우는지에 달렸다.

### 4.3 핵심 원칙: 엄밀함이 이동한 곳

**Anthropic의 4전략 프레임워크**:

- **Write (작성)**: 시스템 프롬프트를 명확하고 명시적으로 구조화
- **Select (선택)**: 컨텍스트적으로 관련 있는 정보만 전달. "[Lost-in-the-Middle](https://arxiv.org/abs/2307.03172)" 성능 저하에 대응
- **Compress (압축)**: 긴 대화를 80%+ 정보 보존하면서 축약
- **Isolate (격리)**: 특화 작업을 범위가 제한된 컨텍스트를 가진 서브 에이전트에 위임

### 4.4 KV-Cache: 프로덕션 메트릭

KV-cache (Key-Value Cache)는 계산된 어텐션 가중치를 저장한다. 프롬프트 접두사가 이전 요청과 일치하면 캐시 재사용으로 비용이 **90% 감소**.

**결정적 통찰**: 접두사의 단 한 토큰이라도 바뀌면 캐시가 무효화된다. 안정적 접두사(시스템 프롬프트, 도구 정의)는 가변 접미사(사용자 입력, 도구 결과) 앞에 놓여야 한다.

**Google ADK 아키텍처**:
- **Stable Prefix**: 시스템 프롬프트, 에이전트 정체성, 도구 정의, 장기 요약
- **Variable Suffix**: 최신 사용자 입력, 새 도구 출력

### 4.5 Agentic Infrastructure

**MCP (Model Context Protocol)** — Anthropic, 2024년 11월

도구-에이전트 통신을 표준화. 채택이 폭발: 2025년 12월 월 9700만+ SDK 다운로드, 10,000+ 커뮤니티 서버. Linux Foundation 거버넌스 확립.

**Skills, Sub-agents, Swarms**:
- **Skills**: 재사용 가능한 능력 번들, lazy-load되는 정의
- **Sub-agents**: 특화 에이전트가 위임 작업에 대해 범위가 제한된 컨텍스트 수신
- **Swarms**: OpenAI 패턴, 에이전트-에이전트 자율 핸드오프

**Context Hub** — Andrew Ng

68+ API에서 검증된 최신 API 문서를 코드 생성 전 에이전트 컨텍스트에 주입하여 "순행성 건망증(anterograde amnesia)"에 대응.

**Memory Systems**: 외부 상태(파일, git history, JSON)가 세션 간 컨텍스트 창 의존을 대체.

### 4.6 여전히 불충분: 컨텍스트도 자기 벽에 부딪힌다

**첫째 한계**: 단일 턴 중심. 기법들이 "이번 호출에 무엇을 주입할까"에 최적화되어 있어 멀티턴 순차적 결정 체인을 놓친다.

**둘째 한계**: 에러 복구 부재. 비용 자각, 보상 감쇠 탐지, 서킷 브레이커 패턴에 대한 메커니즘이 없다.

**셋째 한계**: 보안 공백. 완벽한 컨텍스트도 민감 데이터 시스템에 대한 프롬프트 인젝션 공격을 막지 못한다.

---

## Section 5: 하네스 엔지니어링 에라 (2026~)

### 5.1 기원: 2026년 2월 다중 발견

**Mitchell Hashimoto의 "[My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)"**: "에이전트가 실수할 때, 같은 실수가 구조적으로 재발하지 못하도록 시스템을 바꾼다."

2주 만에 OpenAI, Martin Fowler/Birgitta Böckeler, Ethan Mollick이 독립적으로 정렬된 결론을 발표 — "다중 발견(multiple discovery)".

**핵심 공식**: Agent = Model + Harness (모델을 제외한 모든 것)

### 5.2 하네스 해부학: 4사분면

Fowler/Böckeler의 2×2 분류:

|  | **Feedforward (사전 유도)** | **Feedback (사후 교정)** |
|---|---|---|
| **Deterministic** | **Guides**: AGENTS.md, .cursorrules, 컨벤션 | **Computational**: 컴파일러, 타입 체커, 린터 |
| **Non-deterministic** | **System prompts**: 역할 정의, 행동 제약, few-shot 예시 | **Inferential**: LLM-as-a-judge, 시맨틱 코드 리뷰 |

- **좌상 (Guides)**: 제로 비용 유도. 강제력 없음. 무시될 수 있음.
- **우상 (Computational)**: 기계적으로 강제되는 교정. 구조 위반 포착.
- **좌하 (System prompts)**: 뉘앙스를 다루는 타협 불가능한 행동 가이드라인.
- **우하 (Inferential)**: LLM 기반 품질 평가. 시맨틱 에러 포착.

### 5.3 3가지 케이스 스터디

**Anthropic의 3-Agent 아키텍처**:
- **Planner**: brief를 상세 제품 스펙으로 확장
- **Generator**: sprint당 한 기능 구현, 주기적으로 컨텍스트 리셋
- **Evaluator**: Playwright로 E2E 테스트 실행, 실패 시 구체적 피드백 반환

비용: 22배 높음 ($200 vs $9) 하지만 완성도는 비교 불가.

**OpenAI Codex 5개월 실험**:
- 수동 작성 코드 0줄
- 약 100만 라인 생성
- 약 1,500 PR
- 10배 속도 향상

핵심 발견: 엔지니어는 코드를 쓰지 않았다 — 컨텍스트 생성 환경을 설계했다:
1. **지식 체계화**: 이전엔 tribal하던 아키텍처 결정을 문서화
2. **기계적 강제**: 커스텀 린터가 인간 코드 리뷰를 대체
3. **점진적 공개**: 에이전트에게 매뉴얼 대신 지도를 제공

**Ralph Pattern**: PRD 완료까지 자동 루프, 반복 간 클린 컨텍스트 리셋. 상태는 git history와 파일에 유지.

### 5.4 보안: Lethal Trifecta & Rule of Two

**Lethal Trifecta** — Simon Willison

에이전트가 다음 셋을 동시에 갖추면 보안 사고는 불가피:
1. 비신뢰 입력 처리
2. 민감 시스템/데이터 접근
3. 상태 수정 능력

**Meta의 Rule of Two**: 에이전트는 최대 두 개까지만 동시 보유 가능. 세 개가 필요하면 human-in-the-loop 승인 필수.

예시:
- 외부 읽기 + 민감 데이터 처리 → 상태 변경 차단 (승인 필요)
- 외부 읽기 + 상태 변경 → 민감 데이터 접근 차단 (샌드박스 격리)

---

## Section 6: 3 에라 부검 보고서

### 6.1 종합 비교표

| 차원 | Prompt Engineering | Context Engineering | Harness Engineering |
|---|---|---|---|
| **에라** | 2022-2024 | 2025 | 2026+ |
| **핵심 질문** | "무엇을 말할까?" | "어떤 정보를 주입할까?" | "어떤 시스템을 구축할까?" |
| **엄밀함의 위치** | 프롬프트 텍스트 | 컨텍스트 창 구성 | 시스템 아키텍처 |
| **핵심 메트릭** | 응답 품질 (주관적) | KV-캐시 히트율 | 작업 완료율, 작업당 비용 |
| **실패 모드** | Blind prompting, 비결정성 | 컨텍스트 오염, Lost-in-Middle | 오케스트레이션 버그, 보안 침해 |

### 6.2 이동 패턴 (Relocation Pattern)

각 에라는 전임자를 대체하지 않는다 — 포함한다. 좋은 하네스는 좋은 컨텍스트를 요구하고, 좋은 컨텍스트는 좋은 프롬프트를 요구한다. 진화는 포기가 아닌 추상화 수준의 상승을 의미한다.

### 6.3 앞으로의 지평

- **Guardian Agent**: 정책 위반 배포를 막는 실시간 감시 에이전트. 엄밀함이 "실행"에서 "감독"으로 이동
- **Evaluation Engineering**: 벤치마크 점수에서 실제 작업 완료로 전환. 가독성·미적 가치 등 검증 불가 보상 문제 대응
- **Knowledge Engines**: 코드 그래프, 커밋 히스토리, 프로젝트 설계 의도를 통합하여 현재 시맨틱 검색의 한계를 넘어섬

---

## 결론

Karpathy (2023): "The hottest new programming language is English."

2026 현실: 가장 뜨거운 새 엔지니어링은 컨텍스트 창 구조, 에이전트 루프 상태 머신, 보안 가드레일 레이어링을 이해하는 것. 영어는 여전히 중요하다 — 시스템 자체가 아닌 시스템의 한 컴포넌트로서.

---

## References

37개의 학술/산업 출처 인용. Wei, Yao, Madaan, Shinn 등의 논문과 Anthropic, OpenAI, Google, GitHub, 독립 연구자들의 기술 포스트 포함.
