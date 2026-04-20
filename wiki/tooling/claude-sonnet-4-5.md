---
title: [[claude-agent-sdk|Claude]] Sonnet 4.5
category: tooling
page_type: entity
project: Claude Sonnet 4.5
tags: [tooling, entity, anthropic, model, sonnet]
sources: [raw/hot-topics-sources/2026-04-10/037-introducing-claude-sonnet-4-5.md]
created: 2026-04-10
updated: 2026-04-13
---
# Claude Sonnet 4.5

Anthropic이 2026년 공개한 frontier 모델 허브 페이지다. 이 모델은 특히 coding, computer use, long-horizon task 유지력 측면에서 강하게 포지셔닝되었다.

## 개요

Sonnet 4.5는 단순히 “작은 Opus”가 아니라, 실제 제품과 도구 생태계 안에서:

- 장시간 작업 지속
- [[coding-agent|coding agent]] 성능
- computer use
- reasoning / math

를 균형 있게 강화한 모델로 제시된다.

## 왜 중요한가

이 모델은 benchmark 수치뿐 아니라, Claude Code/Agent SDK/Chrome extension 같은 제품군과 함께 소개되었다는 점에서 중요하다. 즉 모델 하나의 성능보다 **제품화된 agent stack 안에서 어떤 역할을 하는가**를 같이 봐야 한다.

## 실무 적용 관점

Sonnet 4.5는 고비용 최고 성능만 추구하는 모델이라기보다, 실제 agentic coding과 tool use에 맞춘 **운영 가능한 frontier 모델**로 읽는 편이 유용하다.

## 원문이 다루는 흐름

참조 source는 `Claude Sonnet 4.5`를 하나의 정의로 닫지 않고, 주변 설계 맥락과 읽기 순서를 함께 제공한다. 그래서 짧은 소개문만으로 끝내기보다 **구조와 적용 포인트**를 같이 정리해야 위키 문서로서 가치가 생긴다.

- 위키에 남겨야 할 축: 이 대상이 맡는 역할, 연동 방식과 권한 경계, 도입 시 운영 제약

## source 메모

- **05-anthropic-com-introducing-claude-sonnet-4-5** — snapshot: `raw/hot-topics-sources/2026-04-10/037-introducing-claude-sonnet-4-5.md` · 볼 섹션: 핵심 heading 추출이 제한적

## 출시 메시지 핵심

| 축 | 원문 신호 | 위키 해석 |
|---|---|---|
| coding | "best coding model in the world" | Sonnet 4.5는 agentic coding의 기본 작업마로 포지셔닝된다 |
| complex agents | strongest model for building complex agents | 단순 채팅보다 장기 실행 하네스에 더 직접적으로 연결되는 모델 메시지다 |
| computer use | OSWorld 61.4%, 이전 Sonnet 4는 42.2% | GUI/브라우저 조작 능력을 제품 내장 기능과 함께 강조한다 |
| long-horizon focus | 30시간 이상 복잡한 multi-step task에 집중 유지 | frontier reasoning보다 **지속성**을 전면에 내세운 사례다 |
| 가격 | API 가격을 Sonnet 4와 동일한 $3/$15로 유지 | 성능 상승을 운영 비용 폭증 없이 쓰게 하려는 전략으로 읽힌다 |

## 제품 번들로 읽어야 하는 이유

이번 발표는 모델 하나만의 릴리스가 아니었다. 원문은 Sonnet 4.5와 함께 다음을 같이 묶어 설명한다.

- Claude Code 체크포인트와 터미널 UI 개편, 네이티브 VS Code extension
- Claude API의 context editing feature와 memory tool
- Claude 앱의 code execution / 파일 생성 기능
- Claude for Chrome 확장 공개 범위 확대
- 그리고 이를 외부 개발자에게 열어 주는 [[claude-agent-sdk|Claude Agent SDK]]

즉 Sonnet 4.5는 "모델 스펙"이 아니라 **Anthropic의 agent stack 전체를 밀어 올리는 중심 모델**로 읽어야 한다.

## 관련 문서

- [[claude-opus-4-6|Claude Opus 4.6]]
- [[claude-agent-sdk|Claude Agent SDK]]
- [[long-horizon-agent-benchmarks|Long-Horizon Agent Benchmarks (GAIA 2 / SWE-Bench Pro / SWE-EVO)]]
