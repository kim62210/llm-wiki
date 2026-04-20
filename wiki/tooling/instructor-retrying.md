---
title: Instructor Retrying
category: tooling
page_type: summary
tags: [tooling, summary, instructor, retry, reliability]
sources: [raw/recursive-sources/2026-04-10-mastra-instructor-advanced/instructor-retrying.md]
created: 2026-04-10
updated: 2026-04-13
---
# Instructor Retrying

[[instructor|Instructor]]의 retrying 문서 요약이다. Tenacity 기반 exponential backoff, error-specific retry, context-based validation retry, failed attempt tracking을 정리한다.

## 구조도

```mermaid
flowchart TD
    A[validation failure] --> B[retry condition 판단]
    B --> C[backoff 전략 적용]
    C --> D[재시도 실행]
    D --> E[성공 또는 failed attempt tracking]
```

[[instructor|Instructor]]의 retry는 단순 재호출이 아니라, 어떤 오류를 어떤 조건에서 얼마나 다시 시도할지 정책으로 다뤄진다.

## 핵심 구조

- 문서는 Tenacity 기반 기본 retry, error-specific retries, custom retry conditions, context-based validation with retries, logging/monitoring, failed attempts tracking을 다룬다.
- 즉 retry는 단순 편의 기능이 아니라 validation과 결합된 reliability layer다.
- failed attempts tracking이 포함된 점은 운영 가시성을 중시한다는 뜻이다.

## 왜 중요한가

- structured output 실패를 수동으로 감싸기보다, retry policy를 별도 개념으로 두는 것이 production에 훨씬 유리하다.
- 특히 어떤 오류는 재시도 가치가 있지만 어떤 오류는 즉시 실패해야 한다는 구분이 중요하다.
- Instructor는 이 구분을 lightweight하게 제공하는 방향으로 읽힌다.

## 실무 관점

- retry는 [[instructor-validation|validation]]과 함께 설계하지 않으면 비용만 늘릴 수 있다.
- logging/monitoring과 failed attempt tracking을 꼭 같이 붙여야 실제 운영에서 조정이 가능하다.
- 이 문서는 [[instructor-validation|Instructor Validation]]과 함께 봐야 의미가 커진다.

## 원문이 다루는 흐름

원문은 대체로 `Retry on API errors with longer delays` → `Retry on validation errors with shorter delays` 순서로 전개된다.

## 도입 판단표

| 판단 축 | 내용 |
|---|---|
| 잘 맞는 상황 | structured output 실패가 재시도로 회복 가능한 운영 오류일 때 |
| 피해야 할 오해 | 무한 재시도나 비용 폭주를 막는 stop condition과 logging 없이 retry를 켜는 것 |
| 비교/연결 기준 | schema-validation retry 계층으로, [[instructor-validation|Instructor Validation]]과 함께 설계해야 한다. |

## 관련 문서

- [[instructor|Instructor]]
- [[instructor-validation|Instructor Validation]]
- [[instructor-patching|Instructor Patching]]
