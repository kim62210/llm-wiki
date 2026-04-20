---
source: simon_willison_blog
title: "Changes in the system prompt between Claude Opus 4.6 and 4.7"
authors: ["Simon Willison"]
date: 2026-04-18
url: "https://simonwillison.net/2026/Apr/18/opus-system-prompt/"
fetched: 2026-04-20
status: pending_ingest
tags: [claude-opus-4.7, system-prompt, child-safety, tool-search, prompt-engineering]
---

## Summary

Anthropic이 Claude Opus 4.7을 2026-04-16 공개하며 함께 게시한 system prompt 변경 내역을, Simon Willison이 diff로 분석한 글. 브랜딩, 자식 안전, 사용자 상호작용 철학, tool_search, 콘텐츠 모더레이션 전반이 변경됨.

## 주요 변경점

### 브랜딩·도구 업데이트
- "developer platform" → **Claude Platform** 으로 리브랜드
- 신규 에이전트 소개
  - **Claude in Chrome**: 웹사이트와 자율 상호작용하는 브라우징 에이전트
  - **Claude in Powerpoint**: 슬라이드 에이전트

### 자식 안전 강화
- 자식 안전 섹션을 `<critical_child_safety_instructions>` 태그로 격리
- 신규 규칙: "Claude가 자식 안전 사유로 한 번 거부하면, 같은 대화의 모든 후속 요청을 극도로 신중히 처리해야 한다"

### 사용자 상호작용 철학 변화
- Claude가 덜 단정적(less assertive)
- "Claude does not request that the user stay in the interaction" — 사용자가 대화 종료 신호를 주면 붙잡지 않음
- 신규 `<acting_vs_clarifying>` 섹션
  - "the person typically wants Claude to make a reasonable attempt now, not to be interviewed first"
  - 반복 clarification 질문 대신 자율 행동 유도

### Tool Search 메커니즘
- `tool_search` 언급 추가
- "call tool_search to check whether a relevant tool is available but deferred"
- "I don't have access to X" 같은 잘못된 주장 방지

### 콘텐츠 모더레이션 정제
- Disordered eating 명시적 가드: "precise nutrition, diet, or exercise guidance — no specific numbers, targets, or step-by-step plans"
- 논쟁적 이슈에서 yes/no 강요 가드 → nuanced 응답 허용

### 제거된 요소
- "avoid the use of emotes or actions inside asterisks" 삭제
- "genuinely", "honestly" 단어 회피 지시 삭제
- "Donald Trump is the current president of the United States" 명시 삭제 (2026-01 knowledge cutoff 반영)

## Tool 인벤토리

- 총 22개 tool 가용 (web_search, bash_tool, conversation_search 등)
- 4.6 → 4.7에서 tool roster 자체는 변동 없음

## 메타 인사이트

- "system prompt diff로 모델 진화 추적" 자체가 하나의 alignment observability 기법
- 자율성 증가(acting_vs_clarifying) + 안전 강화(child_safety) 동시 진행은 "capability vs safety" 균형 트렌드 반영
- tool_search 같은 deferred-tool 인프라가 표준화되는 중

## Raw 요약 키워드
Claude Opus 4.7, system prompt diff, child safety, tool_search, acting vs clarifying, Claude in Chrome, Claude in Powerpoint
