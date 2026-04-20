---
title: AI 장애 대응 (AI Incident Response)
category: concepts
page_type: concept
tags: [governance, incident-response, post-mortem, ai-safety, production, reliability, responsible-ai]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

AI 장애 대응(AI Incident Response)은 AI/ML 시스템에서 발생하는 장애, 안전 사고, 보안 침해를 탐지하고, 격리하며, 조사하고, 복구하는 구조화된 프로세스다. 전통적 IT 장애 대응이 인프라 가용성과 데이터 침해에 초점을 맞추는 반면, AI 장애 대응은 확률적 시스템의 고유한 장애 모드 -- 환각, 편향 증폭, 프롬프트 인젝션, 모델 조작 등 -- 를 추가로 다룬다. [[ai-observability-patterns|관측성 체계]]가 장애 탐지의 전제 조건이며, [[model-lifecycle-management|모델 수명주기 관리]]의 운영 단계에서 핵심적이다.

## AI 고유의 장애 유형

전통 IT 장애와 달리, AI 시스템은 다음과 같은 고유한 장애 유형을 보인다.

**환각과 허위 정보 생성**: 모델이 사실과 다른 정보를 자신 있게 생성한다. 의료, 법률, 금융 등 고위험 도메인에서 특히 심각한 결과를 초래할 수 있다.

**편향 증폭**: 학습 데이터의 편향이 배포 후 증폭되거나, 사용 맥락의 변화로 새로운 편향이 나타난다. [[fairness-metrics-bias-auditing|공정성 메트릭]]으로 모니터링한다.

**프롬프트 인젝션/탈옥**: 악의적 입력으로 모델의 안전 가드레일을 우회하여 유해 콘텐츠를 생성하거나 시스템 프롬프트를 노출시킨다.

**데이터 유출**: 모델이 학습 데이터의 민감 정보(개인정보, 영업비밀 등)를 응답에 포함시킨다.

**모델 성능 저하**: 데이터 드리프트, 개념 드리프트로 인한 점진적 성능 하락. 즉각적 장애보다 탐지가 어렵다.

**에이전트 시스템 장애**: 자율 에이전트의 예기치 않은 행동, 도구 호출 오류, 무한 루프 등. 에이전트의 행동 범위가 넓을수록 장애 영향도 커진다.

## GenAI-IRF 프레임워크

생성형 AI 시스템의 장애 대응을 위한 Practical Incident-Response Framework(GenAI-IRF)는 기존 사이버보안 표준(NIST SP 800-61r3)과 AI 보증 원칙(NIST AI 600-1, MITRE ATLAS, OWASP LLM Top-10)을 결합한다. 6가지 반복 사건 유형을 식별하고, 각 유형에 대한 구조화된 대응 플레이북을 제공한다.

## 대응 프로세스

### 1. 탐지 (Detection)

[[ai-observability-patterns|관측성 체계]]를 통해 이상 신호를 탐지한다. 자동 탐지(메트릭 임계값, 이상치 탐지)와 수동 보고(사용자 피드백, 내부 리뷰)를 병행한다. 거짓 경보(false positive) 억제가 중요하며, AI를 활용한 경보 상관 분석과 우선순위 지정이 효과적이다.

### 2. 분류와 에스컬레이션 (Triage & Escalation)

장애의 심각도와 영향 범위를 평가한다. AI 장애의 분류 기준은 전통 IT와 다를 수 있다. 안전성 위반(유해 콘텐츠 생성, 개인정보 노출)은 성능 저하보다 높은 우선순위를 받는다.

### 3. 격리 (Containment)

장애 확산을 방지한다. 모델 롤백, 트래픽 리디렉션(이전 안정 버전으로), 기능 플래그 비활성화, 속도 제한(rate limiting) 등의 조치를 취한다. 에이전트 시스템에서는 에이전트의 권한을 즉시 축소하거나 수동 모드로 전환한다.

### 4. 조사 (Investigation)

[[ai-observability-patterns|관측성 데이터]]를 분석하여 근본 원인을 파악한다. AI 시스템의 비결정론적 특성 때문에 완벽한 재현이 어려울 수 있으므로, 로그와 트레이스의 충분한 기록이 중요하다.

### 5. 복구 (Recovery)

근본 원인을 해결하고 정상 운영으로 복귀한다. 모델 패치, 프롬프트 수정, 가드레일 강화, 데이터 필터 추가 등의 조치를 포함한다.

### 6. 사후 분석 (Post-Mortem)

무엇이 발생했는지뿐 아니라 왜 발생했는지를 분석한다. 비난 없는(blameless) 사후 분석 문화가 중요하다. 유사 장애 방지를 위한 구체적 행동 항목을 도출하고, [[model-lifecycle-management|모델 수명주기]] 프로세스 개선에 반영한다.

## 실제 사례 (2025)

2025년 MIT AI Incident Database에 따르면, 프라이버시, 보안, 시스템 신뢰성 관련 AI 사고가 일상적으로 발생하고 있으며, 대부분 예측 가능하고 예방 가능한 패턴을 보였다. 자율주행 차량 사고, AI 기반 채용 시스템의 차별적 결과, 의료 AI의 오진 등이 대표적이다.

## 규제 요구사항

[[nist-ai-rmf|NIST AI RMF]]의 Manage 기능은 장애 대응 절차의 수립을 요구한다. [[iso-42001|ISO/IEC 42001]]은 AI 관련 사고에 대한 체계적 대응과 기록을 관리체계 요구사항에 포함한다. EU AI Act는 고위험 AI 시스템에 대해 심각한 사고의 보고 의무를 부과한다.

## 관련 문서

- [[ai-observability-patterns]] -- 장애 탐지의 전제 조건
- [[model-lifecycle-management]] -- 운영 단계의 핵심 프로세스
- [[ai-red-teaming-methodology]] -- 사전 예방적 취약점 탐지
- [[responsible-ai-practices]] -- 안전성 원칙의 운영적 구현
- [[nist-ai-rmf]] -- Manage 기능과의 연계
- [[ai-supply-chain-security]] -- 공급망 관련 사고 대응
