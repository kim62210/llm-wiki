---
title: Lost in the Middle
aliases: [lost in the middle]
category: concepts
page_type: concept
tags: [context-window, retrieval, attention, long-context]
sources: [raw/2026-04-09-evolution-of-ai-agentic-patterns.md]
created: 2026-04-10
updated: 2026-04-13
---
# Lost in the Middle

긴 컨텍스트에서 **중간에 놓인 정보의 회수 성능이 앞·뒤보다 유독 떨어지는 현상**이다. 장문 문서나 긴 프롬프트를 다루는 LLM 설계에서 핵심 제약으로 자주 언급된다. [[kv-cache-compression|KV 캐시 압축]]과 [[sparse-attention-patterns|sparse attention 패턴]]은 이 문제를 완화하는 주요 기법이다.

## 왜 중요한가

컨텍스트 길이가 커져도 필요한 정보가 항상 잘 회수되는 것은 아니다. 그래서 [[context-engineering]]의 Select 전략, 문서 재배열, 요약, 계층적 검색 같은 기법이 필요해진다.

## 대표 레퍼런스

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)

## 원문이 다루는 흐름

수집된 source는 `프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록` → `Opening Thesis` → `TL;DR` → `Section 1: 왜 지금 이 연대기인가?` → `Section 2: [[prompt-engineering|프롬프트 엔지니어링]] 에라 (2022-2024)` 흐름을 반복한다. 즉 `Lost in the Middle`는 단일 정의보다 **구조·실행 순서·제약 조건**을 함께 보아야 이해되는 문서다.

- 따라가야 할 순서: 프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록, Opening Thesis, TL;DR, Section 1: 왜 지금 이 연대기인가?, Section 2: 프롬프트 엔지니어링 에라 (2022-2024)
- 위키에 남겨야 할 축: 문제가 드러나는 조건, 완화 전략, 인접 개념과의 차이

## 읽기 포인트

- 이 문서는 **이 개념이 실제 병목과 설계 판단에 어떻게 연결되는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- `Lost in the Middle`는 개념 정의보다 실패 모드와 대응 전략이 핵심이므로, 어떤 상황에서 문제가 드러나는지와 어떤 완화 기법이 붙는지를 같이 기록해야 한다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **"프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록"** — snapshot: `raw/2026-04-09-evolution-of-ai-agentic-patterns.md` · source: https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html · 볼 섹션: 프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록, Opening Thesis, TL;DR, Section 1: 왜 지금 이 연대기인가?

## 어디서 문제가 드러나는가

| 정보 위치 | 모델이 보이는 경향 | 실무적 의미 |
|---|---|---|
| 앞부분 | 비교적 잘 찾는다 | system prompt, 핵심 제약, 작업 목표를 앞에 두는 설계가 유리하다 |
| 중간 | 회수 성능이 가장 흔들린다 | 긴 문서 중간에 묻힌 요구사항·예외 조건이 쉽게 사라진다 |
| 끝부분 | 최근 정보 보정 효과로 비교적 유리하다 | 최종 요약, 체크리스트, action item을 뒤에 재배치하는 이유가 된다 |

## 완화 전략

- 긴 문서를 그대로 던지기보다 **핵심 사실을 앞뒤에 재노출**시키는 것이 기본 대응이다.
- RAG 파이프라인에서는 문서 청크를 검색한 뒤 그대로 붙이는 대신, 질의와 관련된 부분을 요약해 상단에 올려주는 재배열이 효과적이다.
- 에이전트 하네스에서는 중간 로그를 통째로 누적하기보다 milestone 단위 요약이나 상태 파일로 외부화하는 편이 안전하다.
- 따라서 lost-in-the-middle은 단순한 attention 현상 설명이 아니라, [[context-engineering]]과 [[harness-engineering]] 설계 원칙으로 번역해야 하는 병목이다.

## 관련 문서

- [[context-engineering|Context Engineering]]
- [[kv-cache|KV Cache]]
- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
