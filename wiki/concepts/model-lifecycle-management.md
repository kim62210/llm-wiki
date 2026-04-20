---
title: 모델 수명주기 관리 (Model Lifecycle Management)
category: concepts
page_type: concept
tags: [governance, mlops, model-lifecycle, versioning, monitoring, deployment, retirement, responsible-ai]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

모델 수명주기 관리(Model Lifecycle Management)는 ML/AI 모델의 전체 수명주기 -- 데이터 준비, 학습, 검증, 배포, 모니터링, 재학습, 폐기 -- 를 체계적으로 관리하는 실천 체계다. MLOps(Machine Learning Operations)의 핵심 구성요소이며, [[responsible-ai-practices|책임 있는 AI]] 실천을 프로덕션 환경에서 구현하는 운영적 기반이다. 2026년 기준 70% 이상의 엔터프라이즈가 MLOps를 통해 AI 아키텍처를 운영화하고 있으며, 금융, 의료, 제조 등 규제 산업에서 특히 중요하다.

## 수명주기 단계

### 1. 데이터 준비와 피처 엔지니어링

학습 데이터의 수집, 정제, 변환, 피처 추출을 포함한다. [[datasheets-for-datasets|Datasheets]]로 데이터셋을 문서화하고, 피처 스토어(Feature Store)를 통해 피처를 중앙 관리한다. 데이터 버전 관리(DVC 등)로 재현 가능성을 보장한다.

### 2. 모델 학습과 실험

실험 추적 도구(W&B, MLflow 등)로 하이퍼파라미터, 메트릭, 아티팩트를 기록한다. 모델 레지스트리에 학습된 모델을 버전 관리하여 등록한다. [[model-cards|Model Cards]]를 작성하여 모델의 의도된 용도, 성능 특성, 한계를 문서화한다.

### 3. 모델 검증과 테스트

오프라인 평가(벤치마크, 교차 검증), [[fairness-metrics-bias-auditing|공정성 감사]], [[ai-red-teaming-methodology|레드 팀 테스트]]를 수행한다. A/B 테스트와 카나리 배포로 프로덕션 환경에서의 성능을 검증한다. 자동화된 CI/CD 파이프라인에 모델 테스트를 통합한다.

### 4. 모델 배포와 서빙

모델 서빙 인프라(TFServing, vLLM, Triton 등)에 배포한다. [[batch-inference-caching|배치 추론과 캐싱]]으로 비용과 지연 시간을 최적화한다. 블루-그린 배포, 카나리 릴리스 등 점진적 배포 전략을 적용한다.

### 5. 모니터링과 관측성

[[ai-observability-patterns|관측성 패턴]]을 통해 모델의 성능, 공정성, 안전성을 실시간으로 추적한다. 데이터 드리프트(입력 분포 변화)와 개념 드리프트(입출력 관계 변화)를 탐지한다. [[token-economics|토큰 비용]]과 자원 사용량을 모니터링한다.

### 6. 재학습과 업데이트

성능 저하, 데이터 드리프트, 새로운 요구사항이 감지되면 재학습을 트리거한다. 자동 재학습 파이프라인과 수동 재학습 프로세스를 병행한다. [[prompt-management-versioning|프롬프트 버전 관리]]가 LLM 기반 시스템에서 특히 중요하다.

### 7. 모델 폐기(Retirement)

모델이 더 이상 유효하지 않거나, 새로운 모델로 대체될 때 체계적으로 폐기한다. 폐기 전 영향 분석을 수행하고, 의존하는 다운스트림 시스템에 대한 마이그레이션 계획을 수립한다. 감사 추적과 규제 준수를 위해 폐기된 모델의 기록을 보존한다.

## MLOps의 5대 기술 기둥

2025-2026년 기준으로 성숙한 MLOps 실천은 다음 5개 기술 기둥을 포함한다.

**재현 가능한 파이프라인**: 데이터 전처리부터 모델 배포까지 전체 워크플로우를 코드로 정의하고 버전 관리한다.

**CI/CD와 자동화 테스트**: 모델 코드와 데이터 파이프라인에 대한 지속적 통합/배포를 자동화한다. 모델 성능, 공정성, 안전성 테스트를 파이프라인에 통합한다.

**모델 및 피처 레지스트리**: Git과 유사한 버전 관리를 모델과 피처에 적용한다. MLflow Model Registry, Vertex AI Model Registry 등이 대표적이다.

**확장 가능한 서빙과 배포**: 트래픽 패턴에 따른 자동 스케일링, A/B 테스트, 카나리 배포를 지원하는 서빙 인프라를 구축한다.

**포괄적 모니터링과 드리프트 탐지**: [[ai-observability-patterns|관측성 체계]]를 통해 모델 성능, 데이터 품질, 시스템 건강을 종합적으로 모니터링한다.

## LLM 시대의 특수 고려사항

LLM 기반 시스템에서는 전통 ML과 다른 수명주기 관리 패턴이 필요하다.

**프롬프트 관리**: [[prompt-management-versioning|프롬프트 버전 관리]]가 모델 버전 관리만큼 중요해졌다. 프롬프트 변경이 모델 교체와 동일한 영향을 미칠 수 있다.

**비용 관리**: [[token-economics|토큰 경제학]]에 기반한 비용 모니터링과 최적화가 필수적이다. [[batch-inference-caching|배치 추론과 캐싱]]으로 비용을 절감한다.

**안전성 모니터링**: 유해 출력, 탈옥 시도, [[ai-incident-response|장애 상황]]에 대한 실시간 감시와 대응 체계가 필요하다.

## 규제 준수

[[iso-42001|ISO/IEC 42001]]의 모델 관리 요구사항과 [[nist-ai-rmf|NIST AI RMF]]의 Manage 기능이 모델 수명주기 관리와 직접 연결된다. 감사 추적(audit trail), 문서화, 변경 관리 등이 규제 준수의 핵심 요소다.

## 관련 문서

- [[ai-observability-patterns]] -- 모니터링 아키텍처
- [[prompt-management-versioning]] -- 프롬프트 버전 관리
- [[token-economics]] -- 토큰 비용 관리
- [[batch-inference-caching]] -- 배치 추론과 캐싱
- [[model-cards]] -- 모델 문서화
- [[ai-incident-response]] -- AI 장애 대응
- [[responsible-ai-practices]] -- 책임 있는 AI 원칙
- [[nist-ai-rmf]] -- AI 위험 관리 프레임워크
- [[iso-42001]] -- AI 관리체계 인증 표준
