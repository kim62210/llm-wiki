---
title: Context Rot Report (Chroma)
category: rag
page_type: summary
tags: [rag, summary, context-rot, chroma, long-context]
sources: [raw/2026-04-10-hot-ai-topics-sources/context-folding/05-trychroma-com-context-rot-how-increasing-input-tokens-impacts-llm-performa.md]
created: 2026-04-10
updated: 2026-04-13
---
# Context Rot Report (Chroma)

Chroma가 발표한 Context Rot 기술 보고서 요약이다. 광고되는 context window 크기와 실제 유효 컨텍스트 사이에 큰 차이가 있음을 강조한다.

## 핵심 내용

- 입력 길이가 길어질수록 성능은 균일하게 유지되지 않는다.
- frontier 모델도 실제로는 특정 길이 이후 회수 성능이 흔들린다.
- long-context 설계는 길이보다 effective context를 기준으로 봐야 한다.

## 왜 중요한가

이 보고서는 “긴 컨텍스트 지원”이라는 문구를 그대로 믿으면 안 된다는 점을 잘 보여준다. [[context-engineering|context engineering]], [[adaptive-context-compression|compression]], [[contextual-retrieval|retrieval]] ordering이 왜 필요한지 실험적으로 뒷받침한다.

## 실무 적용 관점

long-context 시스템 설계에서는 더 많이 넣는 것보다, 언제 성능이 무너지는지 측정하고 그 이전에 압축/선별하는 전략이 중요하다.

## 원문이 다루는 흐름

원문은 대체로 `Context Rot: How Increasing Input Tokens Impacts LLM Performance` → `—Table of Contents` → `Introduction` → `Contributions` → `Related Work` 순서로 전개된다. 따라서 `Context Rot Report (Chroma)` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: Context Rot: How Increasing Input Tokens Impacts LLM Performance, —Table of Contents, Introduction, Contributions, Related Work
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **Context Rot: How Increasing Input Tokens Impacts LLM Performance** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/context-folding/05-trychroma-com-context-rot-how-increasing-input-tokens-impacts-llm-performa.md` · source: https://www.trychroma.com/research/context-rot · 볼 섹션: Context Rot: How Increasing Input Tokens Impacts LLM Performance, —Table of Contents, Introduction, Contributions

## 관련 문서

- [[context-rot|Context Rot & Effective Context Window]]
- [[lost-in-the-middle-paper|Lost in the Middle: How Language Models Use Long Contexts]]
- [[context-engineering|Context Engineering]]
