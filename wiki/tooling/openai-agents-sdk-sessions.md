---
title: OpenAI Agents SDK Sessions
category: tooling
page_type: summary
tags: [tooling, summary, openai-agents-sdk, sessions, memory]
sources: [raw/recursive-sources/2026-04-10-openai-langgraph/openai-agents-sdk-sessions.md]
created: 2026-04-10
updated: 2026-04-10
---

# OpenAI Agents SDK Sessions

OpenAI Agents SDK의 Session 인터페이스와 내장 세션 구현체를 설명하는 공식 가이드 요약이다. 장기 대화 메모리, resumable runs, history compaction 전략이 핵심이다.

## 구조도

```mermaid
flowchart LR
    U[새 사용자 입력] --> S[Session.getItems]
    S --> M[과거 history 병합]
    M --> R[Runner.run]
    R --> P[session.addItems로 저장]
    P --> N[다음 턴 / 재개 실행]
```

Session은 단순 저장소가 아니라, 다음 턴 실행 전에 history를 주입하고 완료 후 결과를 적재하는 메모리 인터페이스다.

## 핵심 구조

- 문서는 Session을 “persistent memory layer”로 정의한다. `Runner.run`에 Session 구현체를 넘기면, 이전 대화 복원과 새 결과 저장을 SDK가 자동 처리한다.
- 기본 구현체는 OpenAI Conversations API를 쓰는 `OpenAIConversationsSession`과 로컬 개발용 `MemorySession`이다.
- Responses 모델을 쓸 때는 `OpenAIResponsesCompactionSession`으로 감싸 history를 자동 압축할 수 있다는 점이 실무적으로 중요하다.

## 구현체 비교

| 구현체 | 용도 | 장점 | 주의점 |
| --- | --- | --- | --- |
| OpenAIConversationsSession | 서버 연동형 대화 메모리 | 다중 프로세스/원격 상태와 잘 맞음 | OpenAI API 의존성 |
| MemorySession | 로컬 실험·테스트 | 설정이 단순함 | 프로세스 종료 시 소실 |
| Custom Session | 자체 DB/캐시/로그와 통합 | 팀 인프라에 맞춤화 가능 | CRUD/merge semantics를 직접 설계해야 함 |

## 실무에서 중요한 부분

- 세션을 도입하면 history stitching을 매번 수동으로 하지 않아도 되지만, 반대로 “무엇을 언제 저장할지” 정책이 시스템 품질을 좌우한다.
- 중단 후 재개(resumable runs)와 human approval 흐름에서는 같은 session을 계속 전달해야 메모리와 실행 상태가 분리되지 않는다.
- 장기 세션은 결국 context budget 문제로 이어지므로 compaction이나 pruning 전략 없이는 비용이 빠르게 커진다.

## 운영 체크포인트

- 서버 상태(`conversationId`, `previousResponseId`)와 SDK session을 중복 사용하지 않도록 규칙을 정했는가?
- 세션 기록을 수정·삭제·감사할 수 있는 CRUD 경로가 있는가?
- 재개 실행 시 같은 session 객체/식별자를 보장하는가?
- history compaction이 품질 저하 없이 동작하는지 eval로 검증했는가?

## 관련 문서

- [[openai-agents-sdk|OpenAI Agents SDK]]
- [[openai-agents-sdk-quickstart|OpenAI Agents SDK Quickstart]]
- [[openai-agents-sdk-handoffs|OpenAI Agents SDK Handoffs]]
- [[context-engineering|Context Engineering (컨텍스트 엔지니어링)]]
