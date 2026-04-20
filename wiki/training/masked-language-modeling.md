---
title: 마스크 언어 모델링 (Masked Language Modeling)
category: training
page_type: concept
tags: [training, mlm, bert, bidirectional, pretraining, language-modeling]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 마스크 언어 모델링 (Masked Language Modeling)

## 개요

마스크 언어 모델링(Masked Language Modeling, MLM)은 입력 시퀀스의 일부 토큰을 [MASK] 토큰으로 치환한 뒤, 양방향 문맥을 활용하여 원래 토큰을 복원하는 사전 학습 목적 함수이다. BERT(Bidirectional Encoder Representations from Transformers, Devlin et al., 2019)가 이 방식을 최초로 제안했으며, RoBERTa, ALBERT, ELECTRA, DeBERTa 등 encoder 계열 모델의 핵심 학습 방법이다. [[causal-language-modeling]]과 달리 양방향 문맥을 동시에 참조하므로 자연어 이해(NLU) 태스크에 강점을 보인다.

## 핵심 개념

### 마스킹 전략 (80-10-10 Rule)

BERT의 원본 논문에서 제안한 마스킹 전략은 입력 토큰의 15%를 선택한 뒤, 세 가지 방식으로 처리한다.

| 비율 | 처리 방식 | 목적 |
|------|-----------|------|
| 80% | [MASK] 토큰으로 교체 | 마스크된 위치의 토큰을 예측하도록 학습 |
| 10% | 랜덤한 다른 토큰으로 교체 | 모델이 모든 위치의 표현을 정확히 유지하도록 유도 |
| 10% | 원래 토큰 유지 | 실제 입력과 사전 학습 사이의 불일치 완화 |

이 80-10-10 전략은 [MASK] 토큰이 파인튜닝 시에는 나타나지 않는 사전 학습-파인튜닝 불일치 문제를 완화하기 위해 설계되었다.

### 학습 목적 함수

MLM의 손실은 마스크된 위치에서만 계산되는 교차 엔트로피이다.

L_MLM = -(1/|M|) * sum_{i in M} log P(x_i | x_{\M})

여기서 M은 마스크된 토큰 위치의 집합이고, x_{\M}은 마스크된 토큰을 제외한 나머지 입력이다. 전체 시퀀스가 아닌 마스크된 15%에 대해서만 손실을 계산하므로, CLM 대비 학습 효율이 낮다는 단점이 있다.

### Next Sentence Prediction (NSP)

BERT는 MLM과 함께 NSP(다음 문장 예측)를 보조 목적 함수로 사용했다. 두 문장 A, B가 실제로 연속인지(IsNext) 무관한지(NotNext)를 이진 분류한다. 그러나 이후 연구에서 NSP의 효과에 의문이 제기되었다. RoBERTa(Liu et al., 2019)는 NSP를 제거하고 더 큰 배치, 더 많은 데이터, 동적 마스킹으로 BERT를 개선하여 상당한 성능 향상을 달성했다.

### Encoder-Only 아키텍처

MLM은 Transformer의 인코더 블록만 사용하는 encoder-only 구조와 결합된다. 양방향 self-attention을 사용하므로 각 토큰이 시퀀스 전체의 문맥을 참조할 수 있다.

## 작동 원리

```mermaid
flowchart LR
    Input["입력: The [MASK] sat on the mat"] --> Embed[토큰 임베딩 + 위치 + 세그먼트]
    Embed --> Encoder[Transformer 인코더 x N 양방향 attention]
    Encoder --> MLMHead["MLM 헤드: [MASK] 위치의 토큰 예측"]
    MLMHead --> Loss[cross-entropy 마스크 위치만]
```

1. 입력 토큰의 15%를 마스킹 (80-10-10 규칙 적용)
2. 토큰 임베딩 + 위치 임베딩 + 세그먼트 임베딩 합산
3. N개의 [[multi-head-latent-attention|Transformer]] 인코더 블록 통과 (양방향 self-attention)
4. 마스크된 위치의 은닉 상태를 어휘 크기 로짓으로 변환
5. 마스크된 위치에서만 cross-entropy 손실 계산

### 정적 vs 동적 마스킹

| 방식 | 설명 | 대표 모델 |
|------|------|-----------|
| 정적 마스킹 | 사전 처리 시 마스크 위치 고정 | BERT |
| 동적 마스킹 | 에포크마다 다른 위치 마스킹 | RoBERTa, ALBERT |

동적 마스킹은 같은 데이터에서 더 다양한 학습 신호를 추출하여 데이터 효율을 높인다.

## 주요 MLM 기반 모델

| 모델 | 파라미터 | 주요 개선점 |
|------|----------|-------------|
| BERT (2019) | 110M/340M | MLM + NSP 최초 제안 |
| RoBERTa (2019) | 125M/355M | NSP 제거, 동적 마스킹, 대규모 학습 |
| ALBERT (2020) | 12M-235M | 파라미터 공유, 문장 순서 예측(SOP) |
| ELECTRA (2020) | 14M-335M | 마스크 대신 replaced token detection |
| DeBERTa (2021) | 100M-1.5B | disentangled attention, enhanced mask decoder |

### ELECTRA: MLM의 효율성 개선

ELECTRA(Clark et al., 2020)는 MLM의 "15%만 학습 신호로 활용"하는 비효율을 해결했다. 작은 생성기가 마스크 위치에 대체 토큰을 생성하고, 판별기가 모든 토큰이 원본인지 대체된 것인지를 판별한다. 모든 토큰에서 학습 신호를 얻으므로 같은 연산량에서 BERT 대비 우수한 성능을 달성했다.

## MLM의 위치: 2026년 관점

2026년 현재 프론티어 모델의 대부분은 [[causal-language-modeling]] 기반의 decoder-only 구조를 채택하고 있으며, MLM 기반 encoder-only 모델은 주로 다음 영역에서 여전히 활발히 사용된다.

- **텍스트 분류/감성 분석**: 양방향 문맥이 분류 성능에 유리
- **명명 개체 인식(NER)**: 전후 문맥을 동시에 참조해야 하는 시퀀스 라벨링
- **문장 임베딩**: Sentence-BERT 등 문장 유사도 계산
- **검색 증강 생성(RAG)**: 문서 인코딩 및 의미 검색

[[instruction-tuning]]과 [[supervised-fine-tuning]]의 발전으로 CLM 모델이 NLU 태스크에서도 강력한 성능을 보이면서, MLM의 독점적 우위는 줄어들었지만, 경량화와 추론 효율 측면에서 encoder 모델의 가치는 유지되고 있다.

## 대표 자료

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al., 2019)](https://arxiv.org/abs/1810.04805)
- [RoBERTa: A Robustly Optimized BERT Pretraining Approach (Liu et al., 2019)](https://arxiv.org/abs/1907.11692)
- [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators (Clark et al., 2020)](https://arxiv.org/abs/2003.10555)

## 관련 문서

- [[causal-language-modeling]] -- 단방향 자기회귀 사전 학습 (GPT 계열)
- [[transfer-learning-for-nlp]] -- MLM이 NLP 전이 학습에 기여한 패러다임 전환
- [[tokenizer-training]] -- BERT의 WordPiece 등 토크나이저 학습
- [[supervised-fine-tuning]] -- 사전 학습된 MLM 모델의 태스크 적응
- [[multi-task-learning]] -- T5 등 encoder-decoder 모델과의 관계
- [[instruction-tuning]] -- MLM 모델에도 적용 가능한 지시문 튜닝
