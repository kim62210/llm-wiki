---
title: Human Evaluation Protocols
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, human-evaluation, annotation, protocols, inter-annotator-agreement]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# Human Evaluation Protocols

인간 평가(human evaluation)는 LLM 출력의 품질을 인간 평가자가 직접 판정하는 방법이다. [[perplexity]], [[bleu]], [[rouge]] 같은 자동 메트릭이 포착하지 못하는 유용성, 자연스러움, 사실 정확성, 안전성 등을 평가할 수 있어, 자동 평가의 "최종 검증" 역할을 한다. LLM-as-Judge([[llm-as-judge-calibration]])가 빠르게 성장하고 있지만, 인간 평가는 여전히 gold standard이며 자동 평가의 보정 기준(calibration reference)으로 필수다.

## 왜 인간 평가가 필요한가

자동 메트릭은 빠르고 저렴하지만, 구조적 한계가 있다.

- **[[bleu]]/[[rouge]]**: 표면 텍스트 겹침만 측정하며 의미적 동치를 놓친다
- **[[bertscore]]**: 의미 유사도는 포착하지만 사실 정확성은 검증하지 못한다
- **벤치마크 점수**: 포화([[benchmark-saturation-goodharts-law]])와 오염([[benchmark-contamination]])으로 신뢰성이 저하된다
- **LLM-as-Judge**: 판정 모델 자체의 편향(장문 선호, 자기 모델 선호)이 존재한다

인간 평가는 이러한 한계를 보완하여 모델 출력이 "실제로 유용한가"를 직접 확인한다.

## 평가 설계(Protocol Design)

### 평가 차원(Evaluation Dimensions)

LLM 출력을 평가할 때 흔히 사용하는 차원은 다음과 같다.

- **유용성(Helpfulness)**: 사용자의 의도에 적합한 정보를 제공하는가
- **정확성(Accuracy/Factuality)**: 사실에 근거한 내용인가, hallucination이 없는가
- **유창성(Fluency)**: 문법적으로 자연스럽고 읽기 쉬운가
- **안전성(Safety)**: 유해하거나 편향된 내용이 없는가
- **일관성(Coherence)**: 응답 내 논리적 흐름이 일관적인가
- **지시 준수(Instruction Following)**: 사용자의 지시사항을 정확히 따랐는가

모든 차원을 항상 평가할 필요는 없다. 평가 목적에 맞는 핵심 2~3개 차원을 선택하고, 각 차원의 정의와 척도를 명확히 문서화하는 것이 중요하다.

### 척도(Rating Scale)

**리커트 척도 (Likert Scale)**: 1~5점 또는 1~7점 척도. 절대 평가에 적합하며 분석이 용이하다.

**쌍대 비교 (Pairwise Comparison)**: 두 응답 중 어느 쪽이 나은지 판정. 절대 점수보다 평가자 일치도가 높고, Chatbot Arena가 이 방식을 사용한다.

**순위 (Ranking)**: 3개 이상의 응답에 순위를 매김. 정보량은 많지만 평가 부담이 크다.

**이진 판정 (Binary)**: 수용 가능/불가능. 가장 단순하며 안전성 평가에 적합하다.

## 가이드라인 작성

평가 가이드라인의 품질이 인간 평가의 품질을 결정한다.

**핵심 원칙**:
- 모든 평가 차원에 대해 10~20개의 점수별 예시(worked examples)를 포함한다
- 경계 사례(edge case)에 대한 판정 기준을 명시한다
- "이 응답이 3점인 이유는 X이고, 4점이 아닌 이유는 Y이다" 형식의 설명을 포함한다

**반복적 개선**: 초기 가이드라인으로 파일럿 평가 -> 평가자 간 일치도 측정 -> 불일치 지점 논의 -> 가이드라인 수정 -> 본 평가. 이 사이클을 최소 1~2회 거쳐야 한다.

## 평가자 간 일치도(Inter-Annotator Agreement)

인간 평가의 신뢰성을 보장하는 핵심 지표다.

### 주요 일치도 메트릭

**Cohen's Kappa**: 두 평가자 간 일치도. 우연 일치를 보정한다. 0.6 이상이면 실질적 일치(substantial agreement).

**Krippendorff's Alpha**: 2명 이상의 평가자, 다양한 척도(명목, 순서, 구간)에 적용 가능. 가장 범용적이며, 결측치도 처리한다. LLM 평가에서는 alpha > 0.6을 최소 기준, > 0.8을 우수 기준으로 본다.

**Fleiss' Kappa**: 3명 이상의 평가자가 명목 척도로 평가할 때 적합하다.

### 보정 세션(Calibration Session)

본 평가 전에 평가자들이 동일한 "골드" 예시를 독립적으로 평가하고, 결과를 비교하여 기준을 맞추는 과정이다. 보정 세션에서 일치도가 기준(예: kappa > 0.6)에 도달하지 않으면, 가이드라인을 수정하고 재보정한다.

## LLM-as-Judge와의 협력

인간 평가와 [[llm-as-judge-calibration]]은 경쟁이 아니라 보완 관계다.

**LLM 판정의 장점**: 속도와 비용이 인간 대비 1/10~1/100. 대규모 평가에 적합하다.

**인간 평가의 역할**:
- LLM 판정자의 보정 기준(gold standard) 제공
- LLM 판정 결과의 신뢰성 검증 (인간과의 일치율 측정)
- LLM이 체계적으로 잘못 판정하는 패턴 발견

**하이브리드 접근**: ICLR 2025 연구에 따르면, LLM 판정자는 개별 인간 평가자와 동등한 정확도를 보이지만, 자신의 정확도를 과대평가(over-confident)하는 경향이 있다. 따라서 LLM으로 대규모 1차 평가를 하고, 인간이 불확실한 사례를 검증하는 "에스컬레이션" 방식이 효과적이다.

**인간-LLM 협력 주석**: LLM이 먼저 자동 레이블링하고, 인간이 양성 판정 사례를 검증하는 방식으로 효율과 품질을 동시에 확보한다.

## 비용과 확장성

인간 평가의 최대 단점은 비용과 속도다. 일반적으로 응답당 $0.5~$5 수준이며, 전문 도메인(의료, 법률)에서는 더 높아진다. 이 비용 문제를 완화하는 접근:

- **샘플링 기반 평가**: 전체 데이터 중 대표 표본만 인간이 평가
- **능동 학습(Active Learning)**: LLM 판정이 불확실한 사례만 인간에게 라우팅
- **크라우드소싱**: Chatbot Arena처럼 사용자 참여를 유도하여 비용 분산
- **평가 전문 서비스**: Scale AI, Surge AI 등 전문 주석 업체 활용

## 관련 문서

- [[llm-as-judge-calibration]] -- LLM 판정 기반 평가
- [[mt-bench]] -- LLM-as-Judge의 대표 벤치마크
- [[ab-testing-llms]] -- 프로덕션 A/B 테스트
- [[classification-metrics]] -- 기본 분류 메트릭
- [[bleu]] -- 자동 평가 메트릭 (번역)
- [[rouge]] -- 자동 평가 메트릭 (요약)
- [[bertscore]] -- 의미 기반 자동 평가
- [[benchmark-saturation-goodharts-law]] -- 자동 평가의 한계
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[ragas]] -- RAG 평가 프레임워크

