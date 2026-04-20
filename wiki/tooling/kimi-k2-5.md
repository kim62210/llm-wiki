---
title: Kimi K2.5
category: tooling
page_type: entity
project: Kimi K2.5
tags: [tooling, entity, kimi, model-releases-and-benchmarks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/kimi-k2-5.md, raw/hot-topics-sources/2026-04-10/130-kimi-k2-5-moonshot-ai.md, raw/hot-topics-sources/2026-04-10/131-moonshotai-kimi-k2-5-hugging-face.md, raw/hot-topics-sources/2026-04-10/132-moonshot-ai-official-site.md, raw/hot-topics-sources/2026-04-10/133-kimi-api-newsletter-moonshot-platform.md, raw/hot-topics-sources/2026-04-10/134-moonshot-ai-wikipedia.md]
created: 2026-04-10
updated: 2026-04-13
---
# Kimi K2.5

2026년 1월 Moonshot AI가 공개한 1T 파라미터 오픈소스 네이티브 멀티모달 에이전트 모델. MoE 구조와 Agent Swarm 기능은 [[llama-4|Llama 4 Maverick]]의 접근과 비교할 때 차이가 드러난다.

## 왜 지금 중요한가

2026년 1월 27일 오픈소스로 출시된 1T 총 파라미터/32B 활성 MoE 모델로, MoonViT 비전 인코더와 최대 100개 병렬 서브 에이전트를 조율하는 Agent Swarm 기능을 탑재해 [[claude-opus-4-5|Claude Opus 4.5]]를 능가하는 비전-코딩 성능을 보여줬다.

## 대표 자료

- [Kimi K2.5 — Moonshot AI](https://www.kimi.com/ai-models/kimi-k2-5)
- [moonshotai/Kimi-K2.5 — Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.5)
- [Moonshot AI Official Site](https://www.moonshot.ai/)
- [Kimi API Newsletter — Moonshot Platform](https://platform.moonshot.ai/blog/posts/Kimi_API_Newsletter)
- [Moonshot AI — Wikipedia](https://en.wikipedia.org/wiki/Moonshot_AI)

## 해석 포인트

Kimi K2.5은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축**으로 읽는 편이 유용하다. 이번 source 묶음에서도 `kimi.com×1, huggingface.co×1, moonshot.ai×1, platform.moonshot.ai×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

## 2026년 4월 큐레이션 요약

- 정의: 2026년 1월 Moonshot AI가 공개한 1T 파라미터 오픈소스 네이티브 멀티모달 에이전트 모델. MoE 구조와 Agent Swarm 기능은 [[llama-4|Llama 4 Maverick]]의 접근과 비교할 때 차이가 드러난다.
- 왜 중요한가: 2026년 1월 27일 오픈소스로 출시된 1T 총 파라미터/32B 활성 MoE 모델로, MoonViT 비전 인코더와 최대 100개 병렬 서브 에이전트를 조율하는 Agent Swarm 기능을 탑재해 Claude Opus 4.5를 능가하는 비전-코딩 성능을 보여줬다.
- 직접 수집 원문: 5개
- 주요 도메인: kimi.com×1, huggingface.co×1, moonshot.ai×1, platform.moonshot.ai×1, en.wikipedia.org×1

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

### source별 핵심 신호

- **Kimi K2.5 | Open Visual Agentic Model for Real Work** (`kimi.com`): Kimi CodeAI Code Agent for Terminal & IDE
- **moonshotai/Kimi-K2.5 · Hugging Face** (`huggingface.co`): The default system prompt might cause confusion to users and unexpected behaviours, so we remove it.
- **New Kimi K2 Models & Updated Pricing** (`platform.moonshot.ai`): Two big updates on the Kimi API: we're shipping new models and updating our pricing.
- **Moonshot AI - Wikipedia** (`en.wikipedia.org`): Yang has stated his goal for founding Moonshot AI is to build foundation models to achieve AGI.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[gemini-3-1-pro]]
- [[minimax-m2-5]]
