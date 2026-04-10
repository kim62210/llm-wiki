---
title: Context Rot Report (Chroma)
category: rag
page_type: summary
tags: [rag, summary, context-rot, chroma, long-context]
sources: [raw/2026-04-10-hot-ai-topics-sources/context-folding/05-trychroma-com-context-rot-how-increasing-input-tokens-impacts-llm-performa.md]
created: 2026-04-10
updated: 2026-04-10
---

# Context Rot Report (Chroma)

Chroma가 발표한 Context Rot 기술 보고서 요약이다. 광고되는 context window 크기와 실제 유효 컨텍스트 사이에 큰 차이가 있음을 강조한다.

## 핵심 내용

- 입력 길이가 길어질수록 성능은 균일하게 유지되지 않는다.
- frontier 모델도 실제로는 특정 길이 이후 회수 성능이 흔들린다.
- long-context 설계는 길이보다 effective context를 기준으로 봐야 한다.

## 왜 중요한가

이 보고서는 “긴 컨텍스트 지원”이라는 문구를 그대로 믿으면 안 된다는 점을 잘 보여준다. context engineering, compression, retrieval ordering이 왜 필요한지 실험적으로 뒷받침한다.

## 실무 적용 관점

long-context 시스템 설계에서는 더 많이 넣는 것보다, 언제 성능이 무너지는지 측정하고 그 이전에 압축/선별하는 전략이 중요하다.

## 관련 문서

- [[context-rot|Context Rot & Effective Context Window]]
- [[lost-in-the-middle-paper|Lost in the Middle: How Language Models Use Long Contexts]]
- [[context-engineering|Context Engineering]]

