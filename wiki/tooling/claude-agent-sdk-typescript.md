---
title: Claude Agent SDK [[claude-agent-sdk-quickstart|TypeScript]]
category: tooling
page_type: entity
project: Claude Agent SDK TypeScript
tags: [tooling, entity, typescript, claude-[[coding-agent|agent]]-sdk, github]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-running-agent-harnesses/05-github-com-anthropics-claude-agent-sdk-typescript.md]
created: 2026-04-10
updated: 2026-04-13
---
# Claude Agent SDK TypeScript

Anthropic의 TypeScript Agent SDK 구현 저장소를 추적하는 허브 페이지다. 문서 요약이 아니라 실제 구현체와 공개 레퍼런스 코드를 중심으로 본다.

## 개요

이 저장소는 Claude Agent SDK를 TypeScript 환경에서 어떻게 쓰고 확장할 수 있는지 보여주는 구현 중심 레퍼런스다.

## 왜 중요한가

공식 overview 문서가 개념을 설명한다면, 이 저장소는 실제 코드 구조와 사용 예시를 제공한다. 따라서 SDK를 이해할 때 문서와 구현을 함께 봐야 한다.

## 실무 적용 관점

TypeScript 환경에서는 SDK의 public API보다도:

- 세션 관리 방식
- tool wiring 방식
- example 프로젝트 구조

를 빠르게 확인하는 것이 중요하다. 그런 의미에서 이 저장소는 문서보다 더 강한 레퍼런스가 될 수 있다.

## 원문이 다루는 흐름

관련 source를 묶어 보면 `Claude Agent SDK TypeScript`는 `GitHub - anthropics/claude-agent-sdk-typescript · GitHub` → `Navigation Menu` → `Search code, repositories, users, issues, pull requests...` → `Provide feedback` → `Saved searches` 축으로 설명된다. 즉 기능 목록 하나보다 **정체성·연동 방식·운영 경계**를 같이 봐야 이 항목의 의미가 선명해진다.

- 따라가야 할 순서: GitHub - anthropics/claude-agent-sdk-typescript · GitHub, Navigation Menu, Search code, repositories, users, issues, pull requests..., Provide feedback, Saved searches
- 위키에 남겨야 할 축: 이 대상이 맡는 역할, 연동 방식과 권한 경계, 도입 시 운영 제약

## source 메모

- **GitHub - anthropics/claude-agent-sdk-typescript** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-running-agent-harnesses/05-github-com-anthropics-claude-agent-sdk-typescript.md` · source: https://github.com/anthropics/claude-agent-sdk-typescript · 볼 섹션: GitHub - anthropics/claude-agent-sdk-typescript · GitHub, Navigation Menu, Search code, repositories, users, issues, pull requests..., Provide feedback

## 관련 문서

- [[claude-agent-sdk|Claude Agent SDK]]
- [[claude-agent-sdk-overview|Claude Agent SDK Overview]]
- [[long-running-agent-harnesses|Agent Harnesses for Long-Running Coding Sessions]]
공식 문서와 구현체를 교차 확인한다.
공식 문서와 구현체를 교차 확인한다.
공식 문서와 구현체를 교차 확인한다.
공식 문서와 구현체를 교차 확인한다.
공식 문서와 구현체를 교차 확인한다.
관련 허브와 다시 연결한다.
관련 허브와 다시 연결한다.
관련 허브와 다시 연결한다.
TypeScript 구현체는 npm package와 GitHub repository의 public API가 일치하는지 확인하는 기준점이다. 다음 갱신에서는 README의 설치 예시, export surface, session/tool 관련 example을 우선 확인하고 Python SDK 허브와 차이를 별도로 남긴다.

이 구분이 허브 품질의 핵심이다.
