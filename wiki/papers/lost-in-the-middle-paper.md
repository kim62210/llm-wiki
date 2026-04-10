---
title: Lost in the Middle: How Language Models Use Long Contexts
category: papers
page_type: paper
tags: [paper, long-context, evaluation, retrieval]
sources: [raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md]
created: 2026-04-10
updated: 2026-04-10
---

# Lost in the Middle: How Language Models Use Long Contexts

긴 컨텍스트에서 관련 정보가 중간에 있을 때 LLM 성능이 크게 저하된다는 고전적이면서도 여전히 중요한 논문이다.

## 핵심 기여

- multi-document QA와 key-value retrieval로 long-context 사용 방식을 분석
- 정보 위치가 모델 성능에 미치는 영향을 정량적으로 보여줌
- context engineering 시대의 핵심 failure mode를 논문 수준으로 정식화

## 결과와 시사점

- 정보가 문맥 앞·뒤에 있을 때보다 가운데에 있을 때 성능이 크게 하락
- 명시적으로 long-context를 지원하는 모델에서도 동일 경향 관찰

## 한계

이 논문은 현상을 밝히는 데 강하지만, 실제 production retrieval stack에서 이를 어떻게 완화할지는 후속 연구와 엔지니어링이 필요하다.

## 실무 적용 관점

RAG, context compression, prompt ordering, tool calling 등 모든 long-context 설계가 결국 **중간 정보 소실을 어떻게 피할지**의 문제라는 점을 상기시킨다.

## 관련 문서

- [[lost-in-the-middle]]
- [[context-engineering]]
- [[context-rot]]
