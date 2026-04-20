---
title: NIST AI RMF (AI 위험 관리 프레임워크)
category: concepts
page_type: concept
tags: [governance, nist, ai-rmf, risk-management, regulation, framework, responsible-ai]
sources: [raw/2026-04-14-ml-foundations-gap.md, raw/2026-04-16-topic-queue-500.md]
created: 2026-04-14
updated: 2026-04-16
---

## 개요

NIST AI RMF(AI Risk Management Framework)는 미국 국립표준기술연구소(NIST)가 개발한 AI 위험 관리 프레임워크다. AI 시스템의 설계, 개발, 배포, 운영 전체 수명주기에 걸쳐 위험을 체계적으로 식별하고 관리하기 위한 자발적(voluntary) 지침이다. 2023년 1월 AI RMF 1.0이 발행되었고, 2024년 2월 AI RMF 2.0으로 업데이트되었다. 법적 구속력은 없지만, 산업계에서 AI 거버넌스의 사실상 표준 참조 프레임워크로 널리 채택되고 있다.

## 4대 핵심 기능

NIST AI RMF는 Govern, Map, Measure, Manage 4개 기능(function)으로 운영된다. 이 기능들은 순차적 단계가 아닌 반복적으로 상호 연결된 프로세스다.

**Govern(거버넌스)**: 위험 인식 조직 문화의 구축을 강조한다. 리더십의 헌신, 명확한 거버넌스 구조, 정책, 역할과 책임 정의가 핵심이다. 다른 세 기능의 기반이 되며, AI 위험 관리의 조직적 맥락을 설정한다. [[responsible-ai-practices|책임 있는 AI]] 원칙이 조직 전체에 내재화되어야 한다.

**Map(매핑)**: AI 시스템을 운영 환경의 더 넓은 맥락에서 파악한다. 기술적, 사회적, 윤리적 차원에 걸친 잠재적 영향을 식별한다. [[model-cards|Model Cards]]와 [[datasheets-for-datasets|Datasheets]]는 Map 기능에서 AI 시스템의 맥락과 영향을 문서화하는 핵심 도구로 활용된다.

**Measure(측정)**: 위험 평가의 세부 작업을 다룬다. 정량적, 정성적 접근 방법을 모두 활용하여 AI 관련 위험의 가능성과 잠재적 결과를 이해한다. [[fairness-metrics-bias-auditing|공정성 메트릭]]과 [[ai-red-teaming|레드 팀 테스트]] 결과가 이 기능의 핵심 입력이다.

**Manage(관리)**: 식별된 위험에 대한 대응을 안내한다. 위험 우선순위 지정, 완화 전략 수립, 모니터링 체계 구축을 포함한다. [[ai-incident-response|AI 장애 대응]] 절차와 [[model-lifecycle-management|모델 수명주기 관리]]가 이 기능과 직접 연결된다.

## 주요 특성

**자발적 프레임워크**: 법적 구속력이 없어 조직의 규모와 상황에 맞게 유연하게 적용할 수 있다. 다만 EU AI Act, 미국 행정명령 등 규제 환경에서 NIST AI RMF 준수를 권장하거나 참조하는 사례가 늘고 있다.

**기술 중립적**: 특정 기술이나 방법론에 종속되지 않는다. 전통 ML, 딥러닝, LLM, 에이전트 시스템 등 모든 AI 유형에 적용 가능하다.

**이해관계자 중심**: 기술 팀뿐 아니라 경영진, 법무, 윤리, 최종 사용자 등 다양한 이해관계자의 참여를 강조한다.

## 생성형 AI 프로필 (AI 600-1)

2024년 7월 NIST는 생성형 AI 고유의 위험을 다루기 위한 Generative AI Profile(NIST AI 600-1)을 발행했다. 이 문서는 AI RMF의 4대 기능을 생성형 AI 맥락에 구체적으로 매핑한다.

생성형 AI 프로필이 다루는 주요 위험 영역은 다음과 같다: 유해 콘텐츠 생성(CBRN 정보 포함), 데이터 프라이버시 침해, 환각(hallucination)과 허위 정보, 지적 재산권 침해, 환경 영향, [[ai-supply-chain-security|공급망 위험]] 등이다.

## ARIA 프로그램

NIST의 ARIA(Assessing Risks and Impacts of AI) 프로그램은 AI RMF의 실무 검증을 위해 2024년에 시작되었다. 2025년 11월 발행된 AI 700-2 보고서에 따르면, 약 51명의 레드 팀원이 7개 AI 애플리케이션에 대해 508건의 테스트 세션을 수행했다. 이 프로그램에서 도입된 CoRIx(Contextual Robustness Index)는 AI 시스템의 출력이 의도된 사용 맥락의 요구사항을 충족하는 정도를 측정하는 지표다.

## [[iso-42001]]과의 관계

[[iso-42001|ISO/IEC 42001]]이 인증 가능한 관리체계 표준이라면, NIST AI RMF는 위험 관리에 초점을 맞춘 지침이다. 둘은 상호 보완적이며, ISO 42001 인증을 추구하는 조직이 NIST AI RMF를 위험 관리 방법론으로 채택하는 경우가 많다. ISO 42001의 위험 평가 요구사항을 NIST AI RMF의 Map-Measure 기능으로 충족할 수 있다.

## 관련 표준 및 문서

NIST AI 100-2 E2025는 적대적 기계학습에 대한 분류 체계와 용어를 제공하며, [[ai-red-teaming|AI 레드 팀 테스트]]의 위협 분류에 활용된다. MITRE ATLAS와 OWASP LLM Top-10도 NIST AI RMF 생태계와 연계되어 AI 시스템의 보안 위험을 분류한다.

## EU AI Act와의 비교

[[eu-ai-act-enforcement]]처럼 규제 의무를 부과하는 방식과 달리, AI RMF는 원칙 중심의 자율 준수 모델을 채택한다:

| 항목 | NIST AI RMF | EU AI Act |
|-----|------------|----------|
| 법적 구속력 | 없음 (자발적) | 있음 (규정) |
| 적용 범위 | 모든 AI 시스템 | 위험 등급별 차등 |
| 처벌 조항 | 없음 | 최대 매출 7% 과징금 |
| 설계 원칙 | 원칙 중심 | 규칙 기반 |

## [[compute-governance]]와의 연결

대규모 컴퓨팅 자원을 사용하는 프론티어 모델의 경우 GOVERN 기능에서 컴퓨팅 자원 접근 통제와 모니터링이 중요한 요소가 된다. 특히 MEASURE 단계에서 학습 컴퓨팅 임계값(예: 10^26 FLOPs 이상)을 리스크 식별 기준으로 활용하는 방향이 논의되고 있다.

## 관련 문서
- [[ai-governance-regulation]] -- AI 거버넌스와 규제 현황

- [[eu-ai-act-enforcement]] - EU의 규제 의무 기반 AI 거버넌스 체계
- [[compute-governance]] - 컴퓨팅 자원 접근 통제를 통한 AI 안전 거버넌스
- [[ai-safety-gap-2026]] - NIST AI RMF가 대응하려는 안전성 갭 문제
- [[frontier-model-safety]] - 프론티어 모델의 자체 안전 프레임워크와 비교
- [[iso-42001]] - AI 관리체계 인증 표준
- [[model-cards]] - 모델 문서화 표준
- [[fairness-metrics-bias-auditing]] - 공정성 메트릭과 편향 감사
- [[ai-red-teaming]] - 적대적 테스트 방법론
- [[ai-incident-response]] - AI 장애 대응 절차
- [[responsible-ai-practices]] - 윤리적 AI 개발 원칙
