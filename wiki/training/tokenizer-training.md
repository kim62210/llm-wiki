---
title: 토크나이저 학습 (Tokenizer Training)
category: training
page_type: concept
tags: [training, tokenizer, bpe, wordpiece, unigram, sentencepiece, subword]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 토크나이저 학습 (Tokenizer Training)

## 개요

토크나이저 학습은 텍스트를 모델이 처리할 수 있는 정수 토큰 시퀀스로 변환하기 위한 서브워드 어휘(vocabulary)를 구축하는 과정이다. 현대 LLM에서 사용되는 세 가지 주요 알고리즘 -- BPE(Byte-Pair Encoding), WordPiece, Unigram -- 은 모두 문자 수준과 단어 수준 사이에서 균형을 잡는 서브워드 분할 방식이다. 토크나이저의 어휘 구성은 모델의 다국어 성능, 시퀀스 길이 효율, 희귀 단어 처리 능력에 직접적인 영향을 미치므로, [[pretraining-data-curation]]과 함께 사전 학습의 초기 결정 중 가장 중요한 요소 중 하나이다.

## 핵심 개념

### 서브워드 토크나이제이션의 필요성

| 방식 | 문제 |
|------|------|
| 문자 단위 | 시퀀스가 지나치게 길어지고, 의미 정보 손실 |
| 단어 단위 | 어휘 크기 폭발, OOV(미등록어) 문제 |
| 서브워드 | 적정 어휘 크기로 OOV 없이 효율적 분할 |

서브워드 토크나이제이션은 빈출 단어는 단일 토큰으로, 희귀 단어는 의미 있는 서브워드 조각으로 분해하여 어휘 크기를 관리 가능한 수준(보통 32K-128K)으로 유지한다.

### 1. BPE (Byte-Pair Encoding)

GPT-2, GPT-3, GPT-4, LLaMA, Mistral 등 대부분의 현대 [[causal-language-modeling]] 모델이 사용하는 알고리즘이다.

**학습 알고리즘:**
1. 코퍼스의 모든 단어를 개별 문자(또는 바이트)로 분할
2. 전체 코퍼스에서 가장 빈번한 인접 토큰 쌍(pair)을 찾음
3. 해당 쌍을 하나의 새 토큰으로 병합하는 규칙 생성
4. 목표 어휘 크기에 도달할 때까지 2-3 반복

GPT-2와 RoBERTa의 토크나이저는 문자 대신 바이트를 기본 단위로 사용하는 byte-level BPE를 채택했다. 기본 어휘 크기가 256(모든 바이트)으로 작아지면서, 어떤 문자도 [UNK]으로 변환되지 않는다는 장점이 있다.

**예시:** 코퍼스에서 "u"+"g"가 20회로 가장 빈번하면 "ug" 토큰을 생성하고, 다음으로 "h"+"ug"가 15회면 "hug" 토큰을 생성하는 식으로 진행된다.

### 2. WordPiece

BERT, DistilBERT, MobileBERT 등 Google의 encoder 계열 모델이 사용하는 알고리즘이다.

**BPE와의 핵심 차이점:**
- BPE: 가장 빈번한 쌍을 병합
- WordPiece: `freq(pair) / (freq(first) * freq(second))` 점수가 가장 높은 쌍을 병합

이 점수 방식은 개별적으로 빈번한 토큰의 무분별한 병합을 억제한다. 예를 들어 "un"과 "able"이 각각 매우 빈번하더라도, 개별 빈도가 높으므로 점수가 낮아 즉시 병합되지 않는다. 반면 "hu"+"gging"처럼 개별 빈도가 낮은 조합은 점수가 높아 빠르게 병합된다.

WordPiece는 단어 내부 서브워드에 "##" 접두사를 붙여 단어 경계를 표시한다 (예: "playing" -> ["play", "##ing"]).

### 3. Unigram (SentencePiece)

T5, ALBERT, XLNet, mBART 등이 사용하며, SentencePiece 라이브러리와 통합되어 사용된다.

**BPE/WordPiece와의 근본적 차이:**
- BPE/WordPiece: 작은 어휘에서 시작하여 병합으로 성장
- Unigram: 큰 어휘에서 시작하여 제거로 축소

**학습 알고리즘:**
1. 빈출 서브스트링으로 구성된 큰 초기 어휘 구축
2. 각 토큰에 확률(빈도/전체) 부여 -- unigram 언어 모델
3. 각 토큰 제거 시 전체 코퍼스 손실 증가량 계산
4. 손실 증가가 가장 적은 하위 p%(보통 10-20%)의 토큰 제거
5. 목표 어휘 크기에 도달할 때까지 2-4 반복

토크나이제이션 시에는 Viterbi 알고리즘으로 최적 분할을 찾는다. SentencePiece는 공백을 특수 문자("_")로 치환하여 언어에 관계없이(공백이 단어 구분자가 아닌 언어 포함) 동일한 전처리를 적용한다.

## 알고리즘 비교

| 항목 | BPE | WordPiece | Unigram |
|------|-----|-----------|---------|
| 방향 | 상향식 (병합) | 상향식 (병합) | 하향식 (제거) |
| 병합 기준 | 빈도 | 빈도/개별빈도 점수 | 손실 기여도 |
| 내부 접두사 | 없음 (바이트 기반) | ## | 단어 시작 _ |
| 대표 모델 | GPT, LLaMA, Mistral | BERT, DistilBERT | T5, XLNet, ALBERT |
| 공백 처리 | 바이트로 인코딩 | 사전 토큰화 | SentencePiece 통합 |
| OOV 처리 | 바이트 폴백 | [UNK] 반환 | 문자 폴백 |

## 실무 고려사항

### 어휘 크기

| 어휘 크기 | 장단점 |
|-----------|--------|
| 32K (GPT-2) | 시퀀스 길이 길어짐, 작은 임베딩 테이블 |
| 50K-64K (LLaMA) | 균형점 |
| 100K-128K (GPT-4) | 짧은 시퀀스, 큰 임베딩 테이블 |

어휘 크기가 커지면 같은 텍스트를 더 적은 토큰으로 표현할 수 있어 시퀀스 길이가 줄어들지만, 임베딩 테이블의 파라미터 수가 증가하고 희귀 토큰의 학습이 불충분해질 수 있다.

### 다국어 토크나이저

다국어 모델에서 토크나이저의 언어별 효율성 차이는 심각한 문제가 된다. 영어 중심으로 학습된 토크나이저는 한국어, 일본어 등에서 동일 의미의 텍스트를 2-5배 더 많은 토큰으로 분해한다. 이는 비용과 문맥 길이 양쪽에서 불리하다.

### 토크나이저-모델 관계

토크나이저는 모델 학습 전에 결정되며, 학습 후 변경이 사실상 불가능하다. 따라서 [[pretraining-data-curation]]에서 결정된 코퍼스 구성이 토크나이저 품질을 좌우하며, 이것이 다시 [[causal-language-modeling]]이나 [[masked-language-modeling]]의 학습 효율에 직접 영향을 미치는 연쇄 관계이다.

## 대표 자료

- [Neural Machine Translation of Rare Words with Subword Units (Sennrich et al., 2016 -- BPE 원전)](https://arxiv.org/abs/1508.07909)
- [SentencePiece: A simple and language independent subword tokenizer (Kudo & Richardson, 2018)](https://arxiv.org/abs/1808.06226)
- [HuggingFace NLP Course: Tokenizer Algorithms](https://huggingface.co/learn/nlp-course/en/chapter6/5)

## 관련 문서

- [[pretraining-data-curation]] -- 토크나이저 학습의 입력이 되는 코퍼스 구축
- [[causal-language-modeling]] -- BPE 토크나이저를 주로 사용하는 GPT 계열 학습
- [[masked-language-modeling]] -- WordPiece 토크나이저를 사용하는 BERT 계열 학습
- [[multi-task-learning]] -- SentencePiece/Unigram을 사용하는 T5 계열
- [[transfer-learning-for-nlp]] -- 토크나이저가 전이 학습 효과에 미치는 영향
