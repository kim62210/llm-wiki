---
title: ROUGE
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, metrics, summarization, nlp, rouge]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# ROUGE

ROUGE(Recall-Oriented Understudy for Gisting Evaluation)는 자동 요약과 기계 번역 품질을 평가하기 위한 메트릭 집합이다. 2004년 Chin-Yew Lin이 제안한 이래, 텍스트 요약 평가의 사실상 표준으로 20년 넘게 사용되고 있다. [[bleu]]가 정밀도(precision)에 초점을 맞추는 것과 달리, ROUGE는 재현율(recall)을 중심에 놓는다 -- "참조 요약의 내용을 모델이 얼마나 빠짐없이 포착했는가"를 묻는 것이다.

## 핵심 변형(Variants)

ROUGE는 단일 메트릭이 아니라 여러 변형의 집합이다.

### ROUGE-N

참조 텍스트와 생성 텍스트 간의 n-gram 겹침을 측정한다. 가장 많이 쓰이는 것은 ROUGE-1(단어 단위)과 ROUGE-2(이중어 단위)이다.

```
ROUGE-N_recall = (참조와 생성 텍스트에서 매칭된 n-gram 수) / (참조 텍스트의 전체 n-gram 수)
```

ROUGE-1은 단어 수준 커버리지를, ROUGE-2는 구문 수준 일치를 반영한다. 실무에서는 두 지표를 함께 보고한다.

### ROUGE-L

최장 공통 부분 시퀀스(Longest Common Subsequence, LCS)를 기반으로 한다. n-gram과 달리 연속하지 않아도 순서만 유지하면 매칭된다. 문장 수준의 구조적 유사성을 포착하며, 연속 매칭에 보상을 주는 ROUGE-W(Weighted LCS) 변형도 있다.

### ROUGE-S

스킵 바이그램(skip-bigram) 기반으로, 문장 내에서 순서를 유지하는 단어 쌍을 평가한다. 단어 사이에 다른 단어가 끼어 있어도 매칭되므로, 표현 방식이 다른 동일 내용을 포착하는 데 유리하다.

## Recall, Precision, F1

ROUGE는 보통 재현율(recall)로 보고하지만, 정밀도(precision)와 F1도 계산할 수 있다.

- **Recall**: 참조 요약의 내용을 모델이 얼마나 포착했는가
- **Precision**: 모델 출력 중 참조 요약과 겹치는 비율 -- 불필요한 내용을 얼마나 줄였는가
- **F1**: 재현율과 정밀도의 조화 평균

추출적 요약(extractive summarization)에서는 recall이 핵심이고, 생성적 요약(abstractive summarization)에서는 F1이 더 균형 잡힌 지표로 간주된다.

## ROUGE의 강점

**속도와 비용**: 인간 평가 대비 수천 배 빠르고 비용이 거의 없다.

**범용성**: 언어에 독립적이며 토큰화만 되면 어떤 언어에도 적용 가능하다.

**인간 판단과의 상관**: 요약 품질에 대한 인간 판단과 합리적 수준의 상관관계를 보인다 -- 이것이 20년간 표준으로 유지된 이유다.

**단순함**: 구현이 간단하고, 결과 해석이 직관적이다. 높은 ROUGE-1은 핵심 단어를 잘 포착했다는 의미이고, 높은 ROUGE-2는 핵심 구문까지 유지했다는 의미다.

## 한계

**표면 수준 매칭**: ROUGE는 어휘적(lexical) 겹침만 본다. "가격이 올랐다"와 "비용이 상승했다"는 같은 뜻이지만 ROUGE에서는 매칭되지 않는다. 이 한계를 극복하기 위해 [[bertscore]] 같은 의미 기반 메트릭이 등장했다.

**참조 의존성**: 정답 요약이 하나뿐이면, 다른 관점에서 올바르게 요약한 텍스트가 불이익을 받는다. 참조 요약의 수와 품질에 평가 결과가 크게 좌우된다.

**추출적 편향**: ROUGE는 원문에서 문장을 그대로 가져오는 추출적 방식에 유리하다. 원문의 단어를 재구성하여 더 간결하게 표현하는 생성적 요약은 과소평가될 수 있다.

**길이 민감성**: 긴 요약이 짧은 요약보다 더 많은 n-gram 매칭 기회를 가지므로, 요약 길이 차이가 점수에 영향을 준다.

## 실무 활용 가이드

**보고 시 권장 조합**: ROUGE-1(커버리지), ROUGE-2(구문 정확도), ROUGE-L(구조적 유사성)을 함께 보고하는 것이 관례다.

**전처리 표준화**: 소문자 변환, 불용어 제거 여부, 토크나이제이션 방법에 따라 점수가 달라진다. 비교 실험에서는 동일 전처리를 사용해야 한다.

**보완 메트릭 병행**: ROUGE 단독으로 요약 품질을 판단하지 말고, [[bertscore]]나 factual consistency 메트릭(예: [[ragas]]에서 제공하는 faithfulness)을 함께 사용한다.

## LLM 시대에서의 위치

GPT-4, Claude 같은 LLM이 생성하는 고품질 생성적 요약에서 ROUGE의 한계가 더 두드러진다. 원문의 단어를 그대로 쓰지 않고도 핵심 내용을 정확히 전달하는 경우가 많기 때문이다. 이에 따라 LLM 요약 평가에서는 다음과 같은 보완 방법이 활용된다.

- [[bertscore]]: 임베딩 기반 의미 유사도
- LLM-as-Judge: GPT-4 등으로 요약 품질을 직접 판정 ([[llm-as-judge-calibration]])
- [[deepeval]], [[ragas]]: RAG 파이프라인의 요약/응답 품질 평가 프레임워크

그럼에도 ROUGE는 빠른 실험 주기에서의 sanity check, 논문의 기준선 비교, [[evaluation-harness]] 내 요약 태스크 평가에서 여전히 표준 지표로 사용된다.

## 관련 문서

- [[bleu]] -- 정밀도 중심 n-gram 메트릭
- [[bertscore]] -- 의미 기반 평가
- [[perplexity]] -- 언어 모델 내재 평가
- [[classification-metrics]] -- 분류 평가 지표
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[ragas]] -- RAG 평가 프레임워크
- [[human-evaluation-protocols]] -- 인간 평가 설계
