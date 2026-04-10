---
title: Lost in the Middle
aliases: ["lost in the middle"]
category: concepts
page_type: concept
tags: [context-window, retrieval, attention, long-context]
sources: [raw/2026-04-09-evolution-of-ai-agentic-patterns.md]
created: 2026-04-10
updated: 2026-04-10
---

# Lost in the Middle

긴 컨텍스트에서 **중간에 놓인 정보의 회수 성능이 앞·뒤보다 유독 떨어지는 현상**이다. 장문 문서나 긴 프롬프트를 다루는 LLM 설계에서 핵심 제약으로 자주 언급된다.

## 왜 중요한가

컨텍스트 길이가 커져도 필요한 정보가 항상 잘 회수되는 것은 아니다. 그래서 [[context engineering]]의 Select 전략, 문서 재배열, 요약, 계층적 검색 같은 기법이 필요해진다.

## 대표 레퍼런스

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)

## 관련 문서

- [[context-engineering|Context Engineering]]
- [[kv-cache|KV Cache]]
- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]

