---
title: OpenAI Agents SDK
category: tooling
page_type: entity
project: OpenAI Agents SDK
tags: [tooling, entity, openai, agents, sdk, dev-tooling-and-frameworks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/openai-agents-sdk.md, raw/hot-topics-sources/2026-04-10/433-openai-agents-python-docs.md, raw/hot-topics-sources/2026-04-10/434-openai-openai-agents-python-github.md, raw/hot-topics-sources/2026-04-10/435-openai-agents-pypi.md, raw/hot-topics-sources/2026-04-10/436-openai-swarm-github.md, raw/hot-topics-sources/2026-04-10/437-openai-agents-typescript-sdk.md]
created: 2026-04-10
updated: 2026-04-16
---
# OpenAI Agents SDK

이 페이지는 OpenAI Agents SDK를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 Swarm의 후속 프로덕션 버전인 OpenAI 공식 에이전트 오케스트레이션 SDK이기 때문이다.

## 정의

Swarm의 후속 프로덕션 버전인 OpenAI 공식 에이전트 오케스트레이션 SDK.

## 왜 지금 중요한가

2025년 3월 프로덕션 릴리스 이후 Agents·Handoffs·Guardrails 3대 프리미티브와 Sessions·Tracing·Voice(gpt-realtime-1.5)까지 통합되며 2026년 4월 v0.13.x 시리즈에서 MCP·100+ 모델 호환으로 확장됐다.

## 개요

이 페이지는 **OpenAI Agents SDK** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [OpenAI Agents Python Docs](https://openai.github.io/openai-agents-python/)
- [openai/openai-agents-python GitHub](https://github.com/openai/openai-agents-python)
- [openai-agents PyPI](https://pypi.org/project/openai-agents/)
- [OpenAI Swarm (Legacy/Educational) GitHub](https://github.com/openai/swarm)
- [OpenAI Agents TypeScript SDK](https://openai.github.io/openai-agents-js/)

## 해석 포인트

OpenAI Agents SDK은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `openai.github.io×2, github.com×2, pypi.org×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: Swarm의 후속 프로덕션 버전인 OpenAI 공식 에이전트 오케스트레이션 SDK.
- 왜 중요한가: 2025년 3월 프로덕션 릴리스 이후 Agents·Handoffs·Guardrails 3대 프리미티브와 Sessions·Tracing·Voice(gpt-realtime-1.5)까지 통합되며 2026년 4월 v0.13.x 시리즈에서 MCP·100+ 모델 호환으로 확장됐다.
- 직접 수집 원문: 5개
- 주요 도메인: openai.github.io×2, github.com×2, pypi.org×1

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## 2026년 4월 Sandbox 업데이트

2026년 4월 대규모 업데이트로 **하네스-컴퓨트 분리 아키텍처**가 도입되었다. 에이전트 오케스트레이션(하네스)과 실행 환경(샌드박스)을 분리하여, 간단한 챗봇 프레임워크에서 장기 실행(long-horizon) 에이전트 플랫폼으로 진화했다.

핵심 변화:
- 하네스와 컴퓨트의 물리적 분리 (컨테이너/VM 기반 샌드박스)
- 7개 샌드박스 프로바이더 공식 지원 (Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel)
- Manifest 추상화로 이식 가능한 워크스페이스 서술
- S3/GCS/Azure Blob/R2 마운트 지원

상세: [[openai-agents-sdk-sandbox|OpenAI Agents SDK Sandbox]]

## 하위 문서 읽기 경로

- [[openai-agents-sdk-quickstart|OpenAI Agents SDK Quickstart]] — 설치부터 첫 agent 실행, tool 추가, handoff 연결까지 가장 짧은 입문 경로
- [[openai-agents-sdk-handoffs|OpenAI Agents SDK Handoffs]] — specialist agent로 제어권을 넘길 때의 routing 규칙
- [[openai-agents-sdk-sessions|OpenAI Agents SDK Sessions]] — 장기 대화 메모리, resumable runs, history compaction 정리
- [[openai-agents-sdk-model-context-protocol|OpenAI Agents SDK MCP]] — hosted/HTTP/stdio MCP 연결과 approval 설계
- [[openai-agents-sdk-sandbox|OpenAI Agents SDK Sandbox]] — 하네스-컴퓨트 분리, 샌드박스 프로바이더, 보안 모델

## 관련 문서
- [[chatgpt]] -- ChatGPT - OpenAI 대화형 AI

- [[ai-hot-topics-2026-04]]
- [[claude-agent-sdk]]
- [[vercel-ai-sdk]]
- [[orchestrator-worker-pattern]] -- Handoffs가 구현하는 오케스트레이터-워커 패턴
- [[human-in-the-loop-patterns]] -- Guardrails와 연결되는 인간-루프 개입 개념

