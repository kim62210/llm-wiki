---
title: 공정성 메트릭과 편향 감사 (Fairness Metrics & Bias Auditing)
category: concepts
page_type: concept
tags: [governance, fairness, bias, auditing, demographic-parity, equalized-odds, responsible-ai, metrics]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

공정성 메트릭(Fairness Metrics)은 ML 모델의 예측이 민감 속성(성별, 인종, 연령 등) 기준으로 특정 그룹에 불이익을 주는지를 정량적으로 측정하는 지표다. 편향 감사(Bias Auditing)는 이런 메트릭을 활용하여 모델의 편향을 체계적으로 탐지하고 문서화하는 프로세스다. [[responsible-ai-practices|책임 있는 AI]] 실천의 핵심 구성요소이며, [[nist-ai-rmf|NIST AI RMF]]의 Measure 기능에서 편향 관련 위험을 평가하는 핵심 도구로 활용된다.

## 주요 공정성 메트릭

**인구통계적 동등성(Demographic Parity)**: 민감 속성에 관계없이 모든 그룹이 긍정적 결과를 받을 확률이 동일해야 한다는 기준이다. P(Y=1|A=0) = P(Y=1|A=1). 직관적이지만, 그룹 간 실제 자격(base rate) 차이를 고려하지 않는다는 한계가 있다. 채용 모델에서 성별에 관계없이 동일한 합격률을 요구하는 것이 대표적 예시다.

**균등화된 오즈(Equalized Odds)**: 모델의 진양성률(TPR)과 위양성률(FPR)이 모든 그룹에서 동일해야 한다. 실제 라벨을 조건으로 하므로 인구통계적 동등성보다 정교하다. P(Y_hat=1|Y=1,A=0) = P(Y_hat=1|Y=1,A=1) AND P(Y_hat=1|Y=0,A=0) = P(Y_hat=1|Y=0,A=1).

**예측 동등성(Predictive Parity)**: 양성 예측 값(PPV)이 모든 그룹에서 동일해야 한다. 의료 분야에서 환자 재입원 예측 모델이 인종에 관계없이 동일한 정밀도를 보이는지 검증할 때 사용된다.

**개별 공정성(Individual Fairness)**: 유사한 개인은 유사한 결과를 받아야 한다는 원칙이다. 그룹 수준이 아닌 개인 수준의 공정성을 다루며, "유사성"을 정의하는 적절한 거리 함수가 필요하다.

**불균형 영향(Disparate Impact)**: 보호 대상 그룹의 선택률을 기준 그룹의 선택률로 나눈 비율이다. 미국 고용법에서 80% 규칙(four-fifths rule)으로 알려져 있으며, 이 비율이 0.8 미만이면 불균형 영향이 있다고 판단한다.

## 불가능성 정리

공정성 메트릭 간에는 근본적 긴장이 존재한다. Chouldechova(2017)와 Kleinberg et al.(2016)의 연구에 따르면, 그룹 간 기본율(base rate)이 다를 때 인구통계적 동등성과 균등화된 오즈를 동시에 만족시키는 것은 수학적으로 불가능하다. 이 불가능성 정리(impossibility theorem)는 어떤 공정성 정의를 선택할지가 기술적 문제가 아닌 가치 판단의 문제임을 시사한다.

## 편향 감사 프로세스

편향 감사는 일반적으로 다음 단계를 따른다.

1. **민감 속성 식별**: 법적, 윤리적으로 보호되는 속성(성별, 인종, 연령, 장애 등)을 정의한다.
2. **데이터 분석**: 학습/평가 데이터의 그룹별 분포를 분석한다. [[datasheets-for-datasets|Datasheets]]가 이 단계의 입력이 된다.
3. **메트릭 선택**: 도메인과 맥락에 적합한 공정성 메트릭을 선택한다.
4. **측정 및 보고**: 선택된 메트릭으로 모델을 평가하고, 결과를 [[model-cards|Model Card]]에 문서화한다.
5. **완화**: 편향이 발견되면 데이터 재균형, 알고리즘 조정, 후처리 보정 등 완화 전략을 적용한다.
6. **지속 모니터링**: 배포 후에도 [[ai-observability-patterns|관측성 패턴]]을 통해 편향을 지속적으로 추적한다.

## 도구 생태계

**IBM AI Fairness 360 (AIF360)**: 70개 이상의 공정성 메트릭과 10개 이상의 편향 완화 알고리즘을 제공하는 오픈소스 도구다. 전처리(reweighing, sampling), 학습 중(adversarial debiasing), 후처리(threshold optimization) 완화를 지원한다.

**Microsoft Fairlearn**: scikit-learn 호환 인터페이스로 공정성 평가와 완화를 제공한다. 대시보드를 통한 대화형 탐색이 강점이다.

**Google What-If Tool**: TensorBoard 통합으로 모델의 공정성을 시각적으로 분석한다.

## LLM에서의 공정성 도전

LLM은 전통적 분류 모델과 다른 공정성 도전 과제를 제기한다. 2025년 연구에서 다수의 LLM이 급여 협상 조언 시 여성과 소수 인종 후보에게 동일 자격에도 불구하고 낮은 급여를 추천한 사례가 발견되었다(남성 40만 달러 vs 여성 28만 달러). 이는 텍스트 생성 맥락에서 전통적 공정성 메트릭을 직접 적용하기 어렵다는 문제를 보여준다. [[ai-red-teaming|레드 팀 테스트]]가 LLM의 편향 탐지에 더 효과적인 접근법으로 부상하고 있다.

## 관련 문서

- [[model-cards]] -- 공정성 평가 결과를 문서화하는 표준
- [[datasheets-for-datasets]] -- 학습 데이터의 편향 분석 기반
- [[responsible-ai-practices]] -- 윤리적 AI 개발 원칙
- [[nist-ai-rmf]] -- AI 위험 관리 프레임워크
- [[ai-red-teaming]] -- LLM 편향 탐지에 활용되는 적대적 테스트
- [[ai-observability-patterns]] -- 배포 후 편향 모니터링
