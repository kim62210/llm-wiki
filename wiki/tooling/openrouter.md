---
title: OpenRouter (유니버설 AI API)
category: tooling
page_type: entity
project: OpenRouter
tags: [ai-gateway, api-routing, multi-model, openai-compatible, edge-infrastructure]
sources: [raw/2026-04-14-ai-hot-topics-100.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

OpenRouter는 250,000개 이상의 앱이 사용하는 유니버설 AI API 게이트웨이다. 60개 이상의 프로바이더에서 300개 이상의 모델에 단일 API로 접근할 수 있으며, OpenAI SDK와 호환되는 인터페이스를 제공한다. 엣지 인프라를 통한 최소 지연 라우팅과 프로바이더 장애 시 자동 폴백이 핵심 강점이다. 월 70조 이상의 토큰을 처리하며 420만 이상의 글로벌 사용자가 활용하고 있다. [[prompt-caching-agentic|프롬프트 캐싱]] 지원 여부가 프로바이더별로 다르므로, [[disaggregated-serving|분리형 추론 서빙]] 전략과 비용 효율성을 함께 분석해야 한다.

## 핵심 특징

### 단일 API, 다중 모델

하나의 API 키와 엔드포인트로 Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro 등 모든 주요 프론티어 모델에 접근한다. OpenAI SDK를 그대로 사용할 수 있어 기존 코드의 수정이 최소화된다.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<OPENROUTER_API_KEY>",
)

response = client.chat.completions.create(
    model="anthropic/claude-opus-4-6",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### 엣지 기반 라우팅

글로벌 분산 엣지 인프라로 사용자와 추론 엔드포인트 간 지연을 최소화한다. 프로바이더 장애 시 자동으로 대체 프로바이더로 폴백하여 가용성을 높인다. 라우팅 설정은 프로바이더별로 커스터마이징 가능하며, 재시도/폴백/우선순위를 세밀하게 제어할 수 있다.

### 데이터 거버넌스

세분화된 데이터 정책으로 프롬프트가 신뢰할 수 있는 모델과 프로바이더에만 라우팅되도록 보장한다. 조직별 정책 설정이 가능하며, Zero Data Retention(ZDR) 모드를 지원하여 프롬프트/응답 데이터가 저장되지 않도록 할 수 있다.

### 개발자 도구

- **모델 브라우저**: 300+ 활성 모델의 성능, 가격, 컨텍스트 길이를 실시간 비교
- **API 플레이그라운드**: 웹에서 직접 모델을 테스트하고 응답 품질 비교
- **사용량 대시보드**: 모델별, 앱별 토큰 사용량과 비용 분석
- **스트리밍 지원**: SSE(Server-Sent Events) 기반 실시간 토큰 스트리밍

## 기술 상세

### 크레딧 기반 과금

- 구독 없이 크레딧 선불 충전 방식
- 크레딧은 어떤 모델이든 사용 가능
- 프로바이더별 비용 비교를 통한 투명한 가격 정보 제공
- 사용량 분석: 모델별, 앱별 토큰 사용 통계

### 모델 선택 지원

- **모델 브라우저**: 300개 이상의 활성 모델을 검색/비교
- **벤치마크 랭킹**: 모델 간 성능 비교 데이터 제공
- **피처 모델**: 주요 신규 모델 하이라이트

### 규모 지표

| 지표 | 수치 |
|------|------|
| 앱 수 | 250,000+ |
| 사용자 수 | 5,000,000+ |
| 월간 토큰 처리량 | 70조+ |
| 모델 수 | 300+ |
| 프로바이더 수 | 60+ |

### 주요 모델 트래픽 (2026.04 기준)

| 모델 | 주간 토큰 | 성장률 |
|---|---|---|
| Claude Opus 4.6 (Anthropic) | 1.3조 | +11.63% |
| Gemini 3.1 Pro Preview (Google) | 524.9B | +67.37% |
| GPT-5.4 (OpenAI) | 509.2B | +8.75% |

### 자동 모델 라우팅 (openrouter/auto)

Not Diamond 기반의 `openrouter/auto` 모델 선택 기능을 제공한다. 추가 비용 없이 작업 특성에 맞는 최적 모델을 자동 선택하며, 프로바이더별 장애 시 자동 폴백한다.

### 데이터 정책

- **Zero Data Retention(ZDR)** 컨트롤: 프로바이더 수준의 데이터 보존 정책 필터링
- 프롬프트가 신뢰할 수 있는 모델/프로바이더에만 라우팅되도록 보장
- 조직별 세분화된 정책 설정 가능

### Portkey / Lite[[context-engineering|LLM]]과의 차이점

| 항목 | OpenRouter | Portkey | LiteLLM |
|---|---|---|---|
| 배포 모델 | SaaS 전용 (자체 호스팅 불가) | 클라우드 + 프라이빗 클라우드 + 셀프호스팅 | 완전 셀프호스팅 |
| 핵심 강점 | 300+ 모델 카탈로그, 자동 라우팅 | 라우팅/재시도/폴백/캐싱 + 옵저버빌리티 | 최대 인프라 제어, 로드밸런싱/쿨다운/백오프 |
| 가격 모델 | 크레딧 선불, 모델별 과금 | 무료 + 엔터프라이즈 | 오픈소스 무료 |
| 데이터 정책 | ZDR, 프로바이더 필터링 | Privacy Mode, 프라이빗 클라우드 | 완전 제어 (자체 인프라) |
| 적합 대상 | 빠른 시작, 다중 모델 실험 | 엔터프라이즈 거버넌스/관측성 | 자체 인프라 운영 팀 |

## 활용 패턴

### 기본 사용 -- OpenAI SDK 호환

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<OPENROUTER_API_KEY>",
)

# 특정 모델 지정
response = client.chat.completions.create(
    model="anthropic/claude-opus-4-6",
    messages=[{"role": "user", "content": "Hello"}]
)

# 자동 모델 선택 (Not Diamond 기반, 추가 비용 없음)
response = client.chat.completions.create(
    model="openrouter/auto",
    messages=[{"role": "user", "content": "Complex reasoning task"}]
)
```

### 통합 프로바이더 목록

Anthropic, OpenAI, Google, Microsoft, Meta, NVIDIA, Amazon, DeepSeek, Mistral, Cohere 등 60+ 프로바이더를 단일 API로 통합한다. 신규 모델 출시 시 별도 코드 변경 없이 `model` 파라미터만 변경하면 된다.

### 적합한 사용 사례

- **모델 평가/실험**: 300+ 모델을 동일 코드로 빠르게 비교 테스트
- **프로덕션 폴백**: 주 프로바이더 장애 시 자동 대체 프로바이더 라우팅
- **비용 최적화**: 동일 모델의 프로바이더별 가격 비교로 최저가 선택
- **다중 모델 애플리케이션**: 작업 유형별 최적 모델 자동 선택 (openrouter/auto)
- **프로토타이핑**: 구독 없이 크레딧 선불로 즉시 시작

### 제약사항

- SaaS 전용으로 자체 호스팅 불가 -- 데이터 주권이 핵심인 경우 Portkey 또는 LiteLLM 고려
- 크레딧 선불 방식으로 대량 사용 시 예산 관리 필요
- 프로바이더별 모델 가용성과 속도가 상이할 수 있음

## 관련 문서

- [[portkey]] - AI 게이트웨이 (자체 호스팅 가능)
- [[litellm]] - 오픈소스 LLM 프록시
- [[braintrust]] - AI 옵저버빌리티 (AI Proxy 기능 포함)
- [[tool-calling-optimization]] - 도구 호출 최적화
