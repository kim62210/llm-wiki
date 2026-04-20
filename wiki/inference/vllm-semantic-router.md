---
title: vLLM Semantic Router
category: inference
page_type: project-internal
project: vLLM
tags: [inference, project-internal, vllm, semantic, router, infra-and-serving]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/vllm-semantic-router.md, raw/hot-topics-sources/2026-04-10/338-vllm-semantic-router-v0-1-iris-the-first-major-release.md, raw/hot-topics-sources/2026-04-10/339-getting-started-with-vllm-semantic-router-athena-release-red-hat-developer.md, raw/hot-topics-sources/2026-04-10/340-vllm-project-semantic-router-github-repository.md, raw/hot-topics-sources/2026-04-10/341-vllm-semantic-router-official-site.md, raw/hot-topics-sources/2026-04-10/342-intelligent-semantic-[[nvidia-dynamo|routing]]-vllm-production-stack-docs.md]
created: 2026-04-10
updated: 2026-04-13
---
# vLLM Semantic Router

이 페이지는 [[vllm-v1-engine|vLLM]] 내부에서 vLLM Semantic Router이 어떤 역할을 하는지 정리한 프로젝트 스냅샷이다. 핵심 범위는 mmBERT 기반 신경 분류기로 요청을 적절한 모델에 라우팅하는 시스템 레벨 Mixture-of-Models이다.

## 정의

mmBERT 기반 신경 분류기로 요청을 적절한 모델에 라우팅하는 시스템 레벨 Mixture-of-Models.

## 왜 지금 중요한가

2026년 1월 5일 v0.1 Iris 첫 메이저 릴리스, 3월 10일 v0.2 Athena가 연이어 공개되며 600+ PR을 흡수했고, Athena는 벤치마크에서 86% 요청을 로컬 무료 모델로 라우팅해 토큰 비용 최적화의 새로운 표준을 제시했다.

## 프로젝트 맥락

이 항목은 **vLLM** 내부 구현 또는 제품 기능을 다루는 문서다. 일반 개념 페이지로 보기보다 특정 프로젝트의 현재 설계와 운영 스냅샷으로 읽는 것이 적절하다.

## 대표 자료

- [vLLM Semantic Router v0.1 Iris: The First Major Release (2026-01-05)](https://blog.vllm.ai/2026/01/05/vllm-sr-iris.html)
- [Getting started with vLLM Semantic Router Athena release - Red Hat Developer (2026-03-25)](https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release)
- [vllm-project/semantic-router GitHub Repository](https://github.com/vllm-project/semantic-router)
- [vLLM Semantic Router Official Site](https://vllm-semantic-router.com/)
- [Intelligent Semantic Routing - vLLM production-stack Docs](https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html)

## 구현·운영 관점

2026년 1월 5일 v0.1 Iris 첫 메이저 릴리스, 3월 10일 v0.2 Athena가 연이어 공개되며 600+ PR을 흡수했고, Athena는 벤치마크에서 86% 요청을 로컬 무료 모델로 라우팅해 토큰 비용 최적화의 새로운 표준을 제시했다. 따라서 이 페이지는 개념 자체보다 '어떤 병목을 풀기 위해 도입되는가'와 '어떤 하드웨어/서빙 스택을 전제하는가'를 중심으로 읽는 편이 유용하다.

## 실무 관점

실무 관점에서는 지연시간, 처리량, 메모리 사용량, 비용 구조를 함께 봐야 한다. 따라서 이 페이지의 개념은 단독 기법이 아니라 전체 serving stack 안에서 어떤 병목을 줄이는지로 이해하는 편이 좋다.

## 관련 문서
- [[lmcache]]

- [[ai-hot-topics-2026-04]]
- [[lmcache-kv-cache-layer]]
- [[tensorrt-llm]]

