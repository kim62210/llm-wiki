---
title: vLLM Semantic Router
category: inference
page_type: project-internal
project: vLLM
tags: [inference, project-internal, vllm, semantic, router, infra-and-serving]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/vllm-semantic-router.md, raw/hot-topics-sources/2026-04-10/338-vllm-semantic-router-v0-1-iris-the-first-major-release.md, raw/hot-topics-sources/2026-04-10/339-getting-started-with-vllm-semantic-router-athena-release-red-hat-developer.md, raw/hot-topics-sources/2026-04-10/340-vllm-project-semantic-router-github-repository.md, raw/hot-topics-sources/2026-04-10/341-vllm-semantic-router-official-site.md, raw/hot-topics-sources/2026-04-10/342-intelligent-semantic-routing-vllm-production-stack-docs.md]
created: 2026-04-10
updated: 2026-04-10
---
# vLLM Semantic Router

이 페이지는 vLLM 내부에서 vLLM Semantic Router이 어떤 역할을 하는지 정리한 프로젝트 스냅샷이다. 핵심 범위는 mmBERT 기반 신경 분류기로 요청을 적절한 모델에 라우팅하는 시스템 레벨 Mixture-of-Models이다.

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

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: vllm.ai 1건, developers.redhat.com 1건, github.com 1건
- source 조합: 구현체, 공식 문서

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/vllm-semantic-router.md`
- [vLLM Semantic Router v0.1 Iris: The First Major Release | vLLM Blog](https://blog.vllm.ai/2026/01/05/vllm-sr-iris.html) — `raw/hot-topics-sources/2026-04-10/338-vllm-semantic-router-v0-1-iris-the-first-major-release.md`
  - 메모: --- title: vLLM Semantic Router v0.1 Iris: The First Major Release | vLLM Blog source_url: https://blog.vllm.ai/2026/01/05/vllm-sr-iris.html final_url: https://vllm.ai/blog/vllm-sr-iris status: 200 content_type: text/html; charset=utf-8 topics: [vLLM Semantic Router (Iris / Athen
- [Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer](https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release) — `raw/hot-topics-sources/2026-04-10/339-getting-started-with-vllm-semantic-router-athena-release-red-hat-developer.md`
  - 메모: --- title: Getting started with the vLLM Semantic Router project's Athena release: Optimize your tokens for agentic AI | Red Hat Developer source_url: https://developers.redhat.com/articles/2026/03/25/getting-started-vllm-semantic-router-athena-release final_url: https://develope
- [GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub](https://github.com/vllm-project/semantic-router) — `raw/hot-topics-sources/2026-04-10/340-vllm-project-semantic-router-github-repository.md`
  - 메모: --- title: GitHub - vllm-project/semantic-router: System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge · GitHub source_url: https://github.com/vllm-project/semantic-router final_url: https://github.com/vllm-project/semantic-router status: 200 conte
- [Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router](https://vllm-semantic-router.com) — `raw/hot-topics-sources/2026-04-10/341-vllm-semantic-router-official-site.md`
  - 메모: --- title: Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router source_url: https://vllm-semantic-router.com final_url: https://vllm-semantic-router.com status: 200 content_type: text/html; charset=UTF-8 topics: [vLLM Semantic Router (Iris / Athena)] sections: [Inf
- [Intelligent Semantic Routing — production-stack](https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html) — `raw/hot-topics-sources/2026-04-10/342-intelligent-semantic-routing-vllm-production-stack-docs.md`
  - 메모: --- title: Intelligent Semantic Routing — production-stack source_url: https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.html final_url: https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/semantic-router-integration.htm

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[lmcache-kv-cache-layer]]
- [[tensorrt-llm]]
