---
title: OMC CCG
aliases: ["OMC CCG"]
category: tooling
page_type: project-internal
project: oh-my-claudecode
tags: [omc, ccg, multi-provider, claude, codex, gemini, advisor]
sources: [raw/2026-04-09-omc-README.md, raw/2026-04-09-omc-ARCHITECTURE.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC CCG (Claude-Codex-Gemini)

> 한 요청을 Codex와 Gemini에 동시 질의하고 Claude가 결과를 합성하는 삼중 자문 스킬.

## 개요

CCG는 **Claude-Codex-Gemini**의 약자다. 한 태스크를 두 외부 모델(Codex, Gemini)에 병렬 질의한 뒤, Claude가 답변들을 검토하고 최종 판단을 합성(synthesize)한다. 백엔드 + UI가 섞인 복합 작업이나, 두 관점을 모두 듣고 싶을 때 유용하다.

## 호출 방법

```bash
# In-session
/ccg Review this PR — architecture (Codex) and UI components (Gemini)
/ccg: review this authentication implementation

# 매직 키워드 트리거
ccg review this migration plan
claude-codex-gemini: assess the API design
```

활성 키워드: `ccg`, `claude-codex-gemini`

## 동작 원리

```
User: "/ccg review this PR"
    │
    ▼
Claude (orchestrator)가 CCG 스킬 활성화
    │
    ├─ Task A: /ask codex "review architecture and security"
    │             ↓
    │         .omc/artifacts/ask/codex-*.md 저장
    │
    └─ Task B: /ask gemini "review UI and docs"
                  ↓
              .omc/artifacts/ask/gemini-*.md 저장
    │
    ▼
두 아티팩트 수집
    │
    ▼
Claude가 합성:
    - 공통 지적사항
    - 상충 의견 중재
    - 최종 권고안 작성
```

## 왜 삼중 자문인가

각 모델의 **강점이 다르다**:

| 모델 | 강점 | 약점 |
|---|---|---|
| **Claude** | 균형 잡힌 추론, 긴 맥락 유지, 구조화 | - |
| **Codex** | 코드 리뷰, 보안 분석, 아키텍처 검증 | UI/디자인 감각 |
| **Gemini** | 대용량 컨텍스트(1M), UI/디자인 일관성, 문서 | 심층 아키텍처 |

CCG는 각 모델의 강점을 활용하면서 Claude가 중재·합성함으로써 단일 모델의 맹점을 보완한다.

## 사용 시나리오

### 백엔드 + UI 복합 작업

```bash
/ccg Review this PR — architecture (Codex) and UI components (Gemini)
```

- Codex: REST 엔드포인트, DB 스키마, 인증 로직 리뷰
- Gemini: 프론트엔드 컴포넌트, 접근성, UX 흐름 리뷰
- Claude: 양쪽 피드백을 통합해 우선순위 정리

### 마이그레이션 플랜 크로스체크

```bash
ccg: review this database migration plan
```

- Codex: 쿼리 최적화, 인덱스, 트랜잭션 격리 관점
- Gemini: 데이터 흐름 도식화, 팀 커뮤니케이션 포인트
- Claude: 리스크와 실행 순서 재조정

### 디자인 시스템 검토

```bash
/ccg evaluate our component library for consistency
```

- Codex: 타입 시스템, API 일관성, 브레이킹 체인지
- Gemini: 시각 일관성, 접근성, 디자인 토큰 사용
- Claude: 종합 권고

## 요구사항

CCG가 정상 동작하려면 다음이 필요:

- **Codex CLI 설치**: `npm install -g @openai/codex`
- **Gemini CLI 설치**: `npm install -g @google/gemini-cli`
- 각 CLI에 유효한 인증 (OpenAI/Google 계정 또는 API 키)

둘 다 없으면 CCG는 동작하지 않거나 fallback한다.

## Team 모드와의 차이

CCG는 [[OMC Team Mode]]의 `omc team N:codex` 같은 **실제 워커 프로세스**와 다르다:

| 항목 | CCG | omc team N:codex |
|---|---|---|
| 실행 방식 | `/ask codex` + `/ask gemini` 호출 → 아티팩트 수집 | tmux에 실제 프로세스 spawn |
| 동시성 | 2-way (codex + gemini) | N개 병렬 |
| 합성 | Claude가 자동 합성 | 사용자가 수동 수합 |
| 사용 목적 | 어드바이저 합성 | 실제 실행 작업 |

CCG는 **의견 합성용**, `omc team N:codex`는 **작업 실행용**이다.

## 아티팩트 저장

CCG의 각 어드바이저 응답은 `.omc/artifacts/ask/` 하위에 마크다운으로 저장된다:

```
.omc/artifacts/ask/
├── codex-2025-01-15-abc123.md
├── gemini-2025-01-15-def456.md
└── ...
```

나중에 같은 프로젝트에서 재참조 가능.

## Provider Advisor (`omc ask` / `/ask`) 배경

CCG는 내부적으로 `/ask` 스킬을 사용한다. `/ask`는 개별 프로바이더에 질의하는 범용 어드바이저:

```bash
# Terminal
omc ask claude "review this migration plan"
omc ask codex --prompt "identify architecture risks"
omc ask gemini --prompt "propose UI polish ideas"

# In-session
/ask claude "review this migration plan"
/ask codex "identify architecture risks"
/ask gemini "propose UI polish ideas"
```

환경변수:
- `OMC_ASK_ADVISOR_SCRIPT` (canonical)
- `OMC_ASK_ORIGINAL_TASK` (canonical)
- `OMX_ASK_ADVISOR_SCRIPT`, `OMX_ASK_ORIGINAL_TASK` (phase-1 aliases, deprecated)

## 비용

CCG는 **3개 모델 × 각각 토큰 비용**이 든다:

- Claude: 합성 작업
- Codex: 전체 컨텍스트 분석
- Gemini: 전체 컨텍스트 분석

비용을 감수할 가치가 있을 때만 사용. 단순 질문은 단일 `/ask`로 충분.

## 실무 고려사항

- **3 Pro Plans 가격**: README에 따르면 Claude + Gemini + ChatGPT Pro 조합이 월 $60 정도
- **합성 품질**: Claude가 합성하는 단계가 핵심. 두 외부 모델 답변만 봐서는 결론이 안 남
- **공통 지적사항 우선**: Codex와 Gemini가 같은 문제를 지적하면 높은 확신도. 상충 의견은 Claude가 중재
- **작업 분할**: 복합 요청은 각 어드바이저에게 어떤 관점을 맡길지 명시 ("architecture for Codex, UI for Gemini")

## 관련 문서

- [[oh-my-claudecode (OMC)]]
- [[OMC Execution Modes]]
- [[OMC Team Mode]]
- [[OMC Magic Keyword]]
