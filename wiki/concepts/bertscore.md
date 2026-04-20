---
title: BERTScore
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, metrics, semantic-similarity, bertscore, nlp]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# BERTScore

BERTScore는 사전학습된 Transformer 모델의 문맥적 임베딩을 활용하여 텍스트 간 의미적 유사도를 측정하는 평가 메트릭이다. 2019년 Zhang et al.이 제안했으며(arXiv:1904.09675), [[bleu]]와 [[rouge]]가 표면적 n-gram 겹침에 의존하는 한계를 극복하기 위해 설계되었다. "The cat sits on the mat"과 "A feline rests upon a rug"처럼 같은 뜻이지만 단어가 다른 텍스트도 높은 유사도로 평가할 수 있다는 것이 핵심 차별점이다.

## 작동 원리

BERTScore는 세 단계로 계산된다.

**1단계 -- 토큰 임베딩 추출**: 참조 텍스트와 생성 텍스트를 각각 사전학습된 모델(BERT, RoBERTa, DeBERTa 등)에 통과시켜 각 토큰의 문맥적 임베딩 벡터를 얻는다.

**2단계 -- 코사인 유사도 행렬 계산**: 참조 텍스트의 각 토큰 임베딩과 생성 텍스트의 각 토큰 임베딩 사이의 코사인 유사도를 모두 계산하여 행렬을 만든다.

**3단계 -- 최대 유사도 집계**: 
- **Recall**: 참조 텍스트의 각 토큰에 대해, 생성 텍스트 토큰과의 최대 코사인 유사도를 찾아 평균낸다
- **Precision**: 생성 텍스트의 각 토큰에 대해, 참조 텍스트 토큰과의 최대 코사인 유사도를 찾아 평균낸다
- **F1**: precision과 recall의 조화 평균

선택적으로 IDF(Inverse Document Frequency) 가중치를 적용하여 흔한 단어의 영향을 줄일 수 있다.

## 지원 모델

BERTScore는 다양한 사전학습 모델을 백엔드로 사용할 수 있다.

- **microsoft/deberta-xlarge-mnli**: 공식 저장소에서 최고 정확도로 권장하는 모델
- **microsoft/deberta-large-mnli**: 속도 최적화 배포용
- **roberta-large**: 범용적으로 많이 사용
- **bert-base-uncased**: 가벼운 실험용

백엔드 모델에 따라 점수 범위와 특성이 달라지므로, 비교 실험에서는 반드시 동일 모델을 사용해야 한다.

## 기존 메트릭 대비 장점

**의미 이해**: 동의어, 의역(paraphrase), 어순 변경을 자연스럽게 처리한다. BLEU/ROUGE가 어휘적 겹침만 보는 반면, BERTScore는 문맥화된 의미를 비교한다.

**인간 판단과의 상관**: 인간 평가와의 상관관계에서 BERTScore는 BLEU(47~50%)보다 높은 59% 수준을 보인다. 특히 personalized text generation 같은 의미 중심 태스크에서 차이가 두드러진다.

**다국어 지원**: 다국어 모델(mBERT, XLM-R 등)을 백엔드로 사용하면 다양한 언어에 적용 가능하다.

## 한계

**계산 비용**: n-gram 기반 메트릭 대비 GPU 연산이 필요하고, 대규모 코퍼스 평가 시 시간과 자원이 상당히 소요된다. 수만 건 이상의 평가에서는 병렬화가 필수다.

**모델 의존성**: 백엔드 모델의 품질과 학습 데이터에 따라 결과가 달라진다. 의료, 법률 등 특수 도메인에서는 범용 모델의 임베딩이 도메인 용어를 제대로 반영하지 못할 수 있다.

**점수 범위 직관성**: BLEU/ROUGE와 달리 점수가 보통 0.85~0.95 범위에 몰려 있어서, 점수 차이의 실질적 의미를 해석하기 어렵다. 이를 위해 baseline rescaling을 적용하기도 한다.

**사실 정확성 미검증**: 의미적으로 유사하더라도 사실과 다른 내용을 생성했는지는 판별하지 못한다. hallucination 탐지에는 별도 메트릭이 필요하며, [[ragas]]의 faithfulness 메트릭이 이 영역을 다룬다.

## 실무 활용 패턴

**BLEU/ROUGE 보완**: ROUGE로 표면 커버리지를, BERTScore로 의미적 충실도를 동시에 측정하여 상호 보완하는 것이 일반적이다.

**생성적 요약 평가**: 원문의 단어를 재구성하는 abstractive summarization에서 ROUGE보다 공정한 평가를 제공한다.

**RAG 파이프라인 평가**: [[ragas]], [[deepeval]] 같은 RAG 평가 프레임워크에서 answer relevancy 측정에 BERTScore 또는 유사 임베딩 기법을 활용한다.

**다국어 평가**: 다국어 모델을 백엔드로 사용하여 언어 간 번역 품질을 의미 수준에서 비교할 수 있다.

## BERTScore 이후의 발전

BERTScore 이후에도 의미 기반 평가는 계속 발전하고 있다.

- **MoverScore**: Word Mover's Distance를 문맥 임베딩에 적용
- **BLEURT**: BERT 위에 인간 판단 점수를 직접 학습한 메트릭
- **COMET**: 기계 번역 특화 학습 메트릭으로 BERTScore보다 높은 인간 상관
- **UniEval**: 여러 평가 차원(유창성, 일관성, 관련성 등)을 통합 평가

이러한 학습 기반 메트릭들은 BERTScore의 "비학습(reference-free)" 특성을 유지하면서 인간 판단과의 정합성을 높이려는 시도다. 하지만 BERTScore는 추가 학습 데이터가 필요 없다는 접근성 때문에 여전히 널리 사용된다.

## 관련 문서

- [[bleu]] -- n-gram 정밀도 기반 메트릭
- [[rouge]] -- n-gram 재현율 기반 메트릭
- [[perplexity]] -- 언어 모델 내재 평가
- [[classification-metrics]] -- 분류 태스크 평가 지표
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[ragas]] -- RAG 평가 프레임워크
- [[human-evaluation-protocols]] -- 인간 평가 설계
- [[llm-as-judge-calibration]] -- LLM 판정 기반 평가
