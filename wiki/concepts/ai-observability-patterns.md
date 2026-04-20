---
title: AI 관측성 패턴 (AI Observability Patterns)
category: concepts
page_type: concept
tags: [governance, observability, monitoring, logging, tracing, llm-ops, production, patterns]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

AI 관측성(AI Observability)은 프로덕션 환경의 LLM/AI 시스템을 모니터링하고, 추적하며, 분석하는 실천 체계다. 전통적 소프트웨어 관측성(로그, 메트릭, 트레이스)을 기반으로 하되, AI 시스템 고유의 비결정론적 특성 -- 프롬프트-응답 품질, 토큰 사용량, 안전성, 공정성 -- 을 추가로 다룬다. [[model-lifecycle-management|모델 수명주기 관리]]의 모니터링 단계를 구체적으로 구현하는 아키텍처 패턴이며, [[ai-incident-response|장애 대응]]의 전제 조건이기도 하다.

이 페이지는 특정 도구가 아닌, 도구에 독립적인 아키텍처 패턴을 다룬다.

## 3대 관측성 기둥

### 로깅 (Logging)

프롬프트, 응답, 토큰 사용량, 에러 등을 구조화된 형태로 기록한다. AI 시스템에서 로깅의 핵심은 재현 가능성이다. 사용자 요청이 들어올 때, 시스템이 응답을 생성하기까지의 모든 단계를 추적할 수 있어야 한다.

LLM 특화 로깅 항목은 다음을 포함한다: 프롬프트 전문과 시스템 메시지, 모델 응답 전문, 토큰 수(입력/출력/추론), [[prompt-management-versioning|프롬프트 버전]] ID, 사용된 모델과 파라미터(temperature, max_tokens 등), 지연 시간(TTFT, TPS), 에러와 재시도 정보.

### 메트릭 (Metrics)

시계열 수치 데이터로, 시스템의 건강 상태를 실시간으로 파악한다.

**성능 메트릭**: 지연 시간(latency), 첫 토큰까지의 시간(TTFT), 초당 토큰 수(TPS), 요청 처리량(throughput), 에러율.

**품질 메트릭**: 정확도, 일관성, 관련성을 자동 평가기(LLM-as-judge 등)로 측정한다. 인간 피드백(thumbs up/down, 수정 빈도)도 품질 신호로 활용한다.

**비용 메트릭**: [[token-economics|토큰 사용량]]과 비용을 요청별, 기능별, 사용자별로 추적한다. 예산 임계값 초과 시 경고를 트리거한다.

**안전성 메트릭**: 정책 위반, 독성, 프롬프트 인젝션 시도 횟수를 추적한다.

### 분산 트레이싱 (Distributed Tracing)

사용자 요청의 전체 수명주기를 마이크로서비스, 외부 도구 호출, 모델 호출을 거쳐 추적한다. 2025년 기준 분산 트레이싱은 LLM 관측성의 기반이 되었다. OpenTelemetry의 GenAI 시맨틱 컨벤션이 LLM 호출의 표준 스팬(span) 속성을 정의한다.

에이전트 시스템에서는 트레이싱이 특히 중요하다. 도구 호출, 하위 에이전트 위임, 멀티턴 추론 등 복잡한 실행 경로를 시각화하고 병목을 식별할 수 있다.

## AI 특화 모니터링 차원

### 드리프트 탐지

**데이터 드리프트**: 입력 데이터의 분포가 학습 데이터와 달라지는 것을 탐지한다. 임베딩 공간에서의 분포 변화, 입력 길이 변화 등을 모니터링한다.

**개념 드리프트**: 입력과 정답 간의 관계가 변화하는 것을 탐지한다. 모델의 성능 메트릭이 시간에 따라 저하되는 패턴으로 나타난다.

### 환각 탐지

모델이 사실과 다른 정보를 생성하는 빈도를 추적한다. RAG 시스템에서는 생성된 응답이 검색된 문서와 일치하는지를 자동으로 검증하는 파이프라인을 구축한다.

### 편향 모니터링

[[fairness-metrics-bias-auditing|공정성 메트릭]]을 프로덕션 환경에서 지속적으로 측정한다. 인구통계 그룹별 응답 품질 차이, 거부율 차이 등을 추적한다.

## 아키텍처 패턴

### 사이드카 패턴

LLM 호출 프록시가 모든 요청/응답을 가로채어 로깅과 메트릭 수집을 수행한다. 애플리케이션 코드의 수정 없이 관측성을 추가할 수 있다.

### 비동기 평가 파이프라인

프로덕션 트래픽의 샘플을 비동기적으로 품질 평가기(자동/인간)에 전달한다. 실시간 서빙에 영향을 주지 않으면서 품질을 지속적으로 측정한다.

### 피드백 루프

사용자 피드백(명시적: 평점, 수정 / 암시적: 재생성 빈도, 세션 이탈)을 수집하여 품질 신호로 활용한다. 이 피드백은 [[prompt-management-versioning|프롬프트 개선]]과 모델 재학습의 입력이 된다.

## 2025년 기준 모범 사례

분산 트레이싱, 토큰 회계(token accounting), 자동화된 평가(automated evals), 인간 피드백 루프가 프로덕션 LLM 관측성의 기본 요구사항이 되었다. 기존 APM(Application Performance Monitoring) 도구의 LLM 확장(Datadog LLM Observability 등)이 표준 APM 트레이스와 LLM 스팬을 상관시켜, 모델 지연이 전체 애플리케이션 성능에 미치는 영향을 파악할 수 있게 한다.

## 관련 문서

- [[model-lifecycle-management]] -- 모니터링은 수명주기의 핵심 단계
- [[token-economics]] -- 비용 모니터링
- [[ai-incident-response]] -- 관측성은 장애 탐지의 전제 조건
- [[prompt-management-versioning]] -- 프롬프트 버전별 성능 추적
- [[fairness-metrics-bias-auditing]] -- 프로덕션 편향 모니터링
- [[batch-inference-caching]] -- 캐시 적중률 모니터링
