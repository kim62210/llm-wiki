---
title: A/B Testing for LLMs
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, ab-testing, llm, statistical-significance, production]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# A/B Testing for LLMs

A/B 테스트는 두 가지 이상의 변형(variant)을 실제 사용자에게 무작위 배정하고, 사전 정의된 지표로 성과를 비교하여 통계적으로 유의미한 차이를 확인하는 실험 방법이다. LLM 시대에 벤치마크 점수의 한계([[benchmark-saturation-goodharts-law]])가 드러나면서, 프로덕션 환경에서의 A/B 테스트가 모델 선택과 프롬프트 최적화의 핵심 방법론으로 부상했다.

## 왜 LLM에서 A/B 테스트가 필요한가

전통적 ML 모델은 정확도, F1 같은 오프라인 메트릭으로 충분히 비교할 수 있었다. LLM은 다르다.

**출력의 확률적 특성**: 동일 프롬프트에 대해 매번 다른 응답을 생성한다. temperature, top-p 설정에 따라 변동성이 크다.

**다차원 품질**: 정확성, 유용성, 유창성, 안전성 등 여러 차원이 동시에 중요하며, 단일 메트릭으로 포착하기 어렵다.

**벤치마크 vs 현실 격차**: [[mmlu]]에서 2% 높은 모델이 실제 사용자 만족도에서도 더 나은지는 프로덕션에서 검증해야 한다.

**프롬프트 민감성**: 같은 모델이라도 프롬프트, 시스템 메시지, few-shot 예시에 따라 성능이 크게 달라진다.

## 실험 설계

### 변형(Variant) 정의

LLM A/B 테스트에서 비교 대상이 되는 변형은 다양하다.

- **모델 비교**: GPT-4 vs Claude 3.5 vs Gemini Pro
- **프롬프트 비교**: 동일 모델에서 프롬프트 A vs 프롬프트 B
- **파라미터 비교**: temperature 0.3 vs 0.7, 시스템 메시지 변형
- **파이프라인 비교**: RAG 설정 변형, 컨텍스트 길이 변형

### 지표 선택

LLM A/B 테스트의 지표는 크게 세 층위로 나뉜다.

**비즈니스 지표**: 전환율, 체류 시간, 재방문율, 태스크 완료율 -- 최종적으로 의사결정에 사용할 지표

**품질 지표**: LLM-as-Judge 점수([[llm-as-judge-calibration]]), BERTScore([[bertscore]]), 인간 평가 점수([[human-evaluation-protocols]])

**운영 지표**: 응답 지연(latency), 토큰 비용, 에러율

### 표본 크기(Sample Size) 결정

LLM의 확률적 특성 때문에 전통 A/B 테스트보다 더 큰 표본이 필요한 경우가 많다.

**검정력 분석(Power Analysis)**: 기대하는 효과 크기(effect size), 유의 수준(alpha, 보통 0.05), 검정력(power, 보통 0.80)을 기반으로 필요 표본 수를 사전에 계산한다.

**LLM 특수성**: 동일 질문에 대한 응답 변동이 크므로, 질문당 여러 번 샘플링하거나 사용자당 여러 세션을 수집해야 할 수 있다.

## 통계적 방법

### 기본 검정

**Wilcoxon 부호 순위 검정(Signed-Rank Test)**: 비모수적 방법으로, LLM 품질 점수 같은 순서형(ordinal) 데이터에 적합하다. 정규분포 가정이 불필요하여 LLM 출력 평가에 많이 사용된다.

**t-test**: 연속형 지표(응답 시간, BERTScore 등)가 정규분포에 가까울 때 사용한다.

**카이제곱 검정 / Fisher 정확 검정**: 이진 결과(태스크 성공/실패, 사용자 만족/불만족)에 적합하다.

### 다중 비교 보정

여러 모델/프롬프트를 동시에 비교할 때는 다중 비교 문제(multiple comparison problem)가 발생한다.

- **Bonferroni 보정**: 가장 보수적. alpha를 비교 횟수로 나눈다
- **Benjamini-Hochberg FDR 보정**: False Discovery Rate를 제어. 탐색적 분석에 더 적합
- **실무 권장**: 3개 이상 변형을 비교하면 FDR 보정을 적용한다

### 조기 중단의 위험

A/B 테스트를 계획된 표본 수에 도달하기 전에 중단하면 거짓 양성(false positive) 위험이 높아진다. "p-value가 0.05 미만으로 떨어졌으니 실험을 중단하자"는 잘못된 관행이다. 사전에 결정된 표본 수나 실험 기간을 준수해야 한다.

순차적 검정(sequential testing)을 사용하면 중간 확인을 허용하면서도 거짓 양성률을 제어할 수 있다.

## LLM A/B 테스트의 특수 도전

**평가자 일관성**: 인간 평가를 사용하면 평가자 간 일치도(inter-annotator agreement)가 문제가 된다. [[human-evaluation-protocols]]에서 다루는 Krippendorff alpha > 0.6이 최소 기준이다.

**자동 평가자 편향**: LLM-as-Judge를 사용하면 판정 모델의 편향이 결과에 영향을 준다. 판정 모델을 교차 사용하여 편향을 줄여야 한다.

**계절성과 사용자 세그먼트**: 시간대, 요일, 사용자 유형에 따라 결과가 달라질 수 있다. 충분한 실험 기간과 세그먼트 분석이 필요하다.

**비용 고려**: LLM API 호출 비용이 실험 비용의 상당 부분을 차지한다. 표본 크기와 비용 간의 균형을 맞춰야 한다.

## 도구 생태계

- **Statsig**: LLM 특화 A/B 테스트 플랫폼. online experimentation + LLM 지표 통합
- **[[deepeval]]**: 자동 평가 기반 오프라인 A/B 비교 지원
- **Braintrust**: LLM 평가 + 실험 관리 통합 플랫폼
- **자체 구축**: [[evaluation-harness]]로 오프라인 벤치마크 비교, 프로덕션에서는 자체 실험 프레임워크 구축

## 관련 문서

- [[benchmark-saturation-goodharts-law]] -- A/B 테스트가 필요한 배경
- [[benchmark-contamination]] -- 벤치마크 한계
- [[human-evaluation-protocols]] -- 인간 평가 설계
- [[llm-as-judge-calibration]] -- 자동 판정 기반 평가
- [[classification-metrics]] -- 기본 평가 지표
- [[mt-bench]] -- 다중 턴 벤치마크
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[ragas]] -- RAG 평가 프레임워크

