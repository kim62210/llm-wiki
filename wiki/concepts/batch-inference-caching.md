---
title: 배치 추론과 캐싱 (Batch Inference & Caching)
category: concepts
page_type: concept
tags: [governance, batch-[[kv-cache-inference|inference]], caching, prompt-caching, semantic-cache, vllm, cost-optimization, inference]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

배치 추론(Batch Inference)은 다수의 추론 요청을 묶어 처리하여 처리량을 높이고 비용을 절감하는 기법이다. 캐싱(Caching)은 이전 추론 결과나 중간 계산(KV 캐시)을 재사용하여 중복 연산을 제거하는 기법이다. 두 기법 모두 프로덕션 LLM 시스템의 [[token-economics|토큰 비용]]과 지연 시간을 크게 줄이는 핵심 최적화 전략이며, [[model-lifecycle-management|모델 수명주기 관리]]의 배포/운영 단계에서 필수적이다.

## 배치 추론

### 정적 배치(Static Batching)

여러 요청을 고정 크기 배치로 묶어 한 번에 처리한다. 구현이 단순하지만, 배치 내 가장 긴 시퀀스가 완료될 때까지 짧은 시퀀스가 대기해야 하므로 GPU 활용률이 떨어진다.

### 연속 배치(Continuous Batching)

vLLM이 도입한 방식으로, 시퀀스가 완료되는 즉시 새 요청을 배치에 삽입한다. 정적 배치 대비 최대 23배 성능 향상을 달성할 수 있다. PagedAttention의 효율적 메모리 할당과 결합하면 GPU 활용률이 극대화된다. 2026년 기준 대부분의 프로덕션 서빙 프레임워크(vLLM, TensorRT-LLM, SGLang 등)가 연속 배치를 지원한다.

### API 배치 서비스

OpenAI Batch API, Anthropic Message Batches 등은 비실시간 워크로드에 대해 실시간 가격 대비 약 50% 할인을 제공한다. 24시간 내 처리를 보장하며, 대규모 평가, 데이터 처리, 분류 작업 등에 적합하다.

## 캐싱 전략

프로덕션 시스템은 일반적으로 다층 캐싱 아키텍처를 구현한다.

### 프롬프트 캐싱 (Prefix Caching)

동일한 프롬프트 접두사(시스템 메시지, 공통 컨텍스트 등)에 대한 KV 캐시를 재사용한다.

**Anthropic 프롬프트 캐싱**: 캐시 쓰기 시 기본 입력 비용의 1.25배, 캐시 읽기 시 0.1배만 청구하여 최대 90%의 비용 절감과 85%의 지연 시간 감소를 달성한다. 명시적으로 캐시 중단점(cache breakpoint)을 지정하는 방식이다.

**OpenAI 자동 캐싱**: 2024년 말부터 기본 활성화되어, 1024 토큰 이상의 공통 접두사를 자동으로 캐시한다. 50%의 비용 절감을 제공한다.

**자체 호스팅 접두사 캐싱**: vLLM의 Automatic Prefix Caching(APC)은 기존 요청과 동일한 접두사를 공유하는 새 요청에 대해 KV 캐시를 자동으로 재사용한다.

### 시맨틱 캐싱 (Semantic Caching)

정확히 동일한 텍스트가 아니더라도 의미적으로 유사한 쿼리에 대해 이전 응답을 재사용한다. 연구에 따르면 LLM 쿼리의 31%가 시맨틱 유사성을 보여, 캐싱 없이는 상당한 비효율이 발생한다.

한 클라우드 제공업체는 Redis 기반 시맨틱 캐싱으로 LLM 추론 비용을 40% 절감했다. 임베딩 모델로 쿼리 벡터를 생성하고, 벡터 유사도가 임계값을 넘으면 캐시된 응답을 반환하는 방식이다.

다만 시맨틱 캐싱은 캐시 무효화(invalidation)가 까다롭다. 유사한 쿼리라도 맥락에 따라 다른 응답이 필요한 경우가 있으며, 적중률(hit rate)과 응답 품질 사이의 균형을 조정해야 한다.

### 정확 일치 캐싱 (Exact Match Caching)

동일한 입력에 대해 이전 응답을 그대로 반환한다. 결정론적 결과가 필요한 분류, 구조화된 추출 등에 적합하다. 구현이 가장 단순하지만 적용 범위가 제한적이다.

## 다층 캐싱 아키텍처

프로덕션 시스템에서는 여러 캐싱 계층을 조합한다.

1. **시맨틱 캐시**: 100% 비용 절감 (캐시 적중 시 LLM 호출 불필요)
2. **프롬프트/접두사 캐시**: 50-90% 입력 비용 절감
3. **전체 추론**: 캐시 미적중 시 일반 추론

안정적인 시스템 프롬프트, 일관된 문서 검색, 반복적 사용자 질문이 있는 채팅 애플리케이션의 경우, 접두사 캐싱으로 입력 토큰의 70% 이상을 캐시하고, 시맨틱 캐싱으로 쿼리의 30%를 처리하여 결합 절감률 80% 이상을 달성할 수 있다.

## KV 캐시 최적화

2026년 연구에서는 SCORE(Similarity-Aware Contextual Overlap-Redundancy Eviction) 같은 기법이 등장하여, 캐시 예산을 동적으로 재할당하고 원래 KV 캐시의 1.5%만으로도 성능을 유지할 수 있음을 보여주었다.

## 관련 문서

- [[token-economics]] -- 토큰 비용 구조와 최적화 전략
- [[ai-observability-patterns]] -- 캐시 적중률 모니터링
- [[model-lifecycle-management]] -- 배포/운영 단계 최적화
- [[prompt-management-versioning]] -- 프롬프트 관리와 캐싱의 연계
