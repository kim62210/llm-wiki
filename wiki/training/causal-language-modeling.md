---
title: 인과적 언어 모델링 (Causal Language Modeling)
category: training
page_type: concept
tags: [training, clm, autoregressive, gpt, pretraining, language-modeling]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 인과적 언어 모델링 (Causal Language Modeling)

## 개요

인과적 언어 모델링(Causal Language Modeling, CLM)은 주어진 이전 토큰들의 시퀀스를 조건으로 다음 토큰의 확률을 예측하는 자기회귀(autoregressive) 사전 학습 목적 함수이다. GPT 계열(GPT-1, GPT-2, GPT-3, GPT-4) 및 LLaMA, Mistral, DeepSeek 등 현재 주류 대규모 언어 모델의 사전 학습 방식이 모두 CLM에 기반한다. 모델은 왼쪽에서 오른쪽으로만 토큰을 참조할 수 있으며, 미래 토큰은 볼 수 없다는 점에서 "인과적(causal)"이라 부른다.

## 핵심 개념

### 자기회귀 분해 (Autoregressive Factorization)

CLM은 시퀀스의 결합 확률을 조건부 확률의 곱으로 분해한다.

P(x_1, x_2, ..., x_T) = P(x_1) * P(x_2|x_1) * P(x_3|x_1, x_2) * ... * P(x_T|x_1, ..., x_{T-1})

각 시점 t에서 모델은 x_1부터 x_{t-1}까지만 참조하여 x_t를 예측한다. 이 단방향 제약은 Transformer의 self-attention에서 causal mask(삼각 마스크)로 구현된다. 미래 위치의 attention score를 -inf로 설정하여 정보 유출을 방지한다.

### 학습 목적 함수

CLM의 학습 손실은 교차 엔트로피(cross-entropy) 손실이다.

L = -(1/T) * sum_{t=1}^{T} log P(x_t | x_1, ..., x_{t-1})

학습 시에는 교사 강제(teacher forcing)를 사용한다. 모델의 예측과 무관하게 항상 실제 정답 토큰을 다음 입력으로 제공하는 방식이다. 이는 학습을 안정화하고 수렴 속도를 높이지만, 추론 시에는 자신의 예측을 입력으로 사용해야 하므로 학습-추론 불일치(exposure bias)가 발생할 수 있다.

### Decoder-Only 아키텍처

CLM은 Transformer의 디코더 블록만 사용하는 decoder-only 구조와 결합된다. GPT-1(2018)이 이 조합을 처음 제안했으며, 이후 GPT-2가 "충분히 큰 언어 모델은 별도 파인튜닝 없이도 다양한 태스크를 수행한다"는 것을 보여주면서 사전 학습 패러다임의 중심이 되었다.

| 모델 | 파라미터 | 학습 토큰 | 특징 |
|------|----------|-----------|------|
| GPT-1 (2018) | 117M | ~5B (BookCorpus) | CLM + Transformer decoder 최초 조합 |
| GPT-2 (2019) | 1.5B | ~10B (WebText) | zero-shot 능력 시연 |
| GPT-3 (2020) | 175B | ~300B | in-context learning, few-shot |
| LLaMA (2023) | 7-65B | 1-1.4T | 오픈소스 CLM 모델 선도 |
| LLaMA 3 (2024) | 8-405B | 15T+ | 데이터 스케일링 극대화 |

## 작동 원리

```mermaid
flowchart LR
    Input["입력: x_1, x_2, ..., x_{t-1}"] --> Embed[토큰 임베딩 + 위치 인코딩]
    Embed --> Blocks[Transformer 디코더 블록 x N]
    Blocks --> Head[언어 모델 헤드 softmax]
    Head --> Predict["예측: P(x_t)"]
    
    Predict --> Loss["cross-entropy 손실 계산"]
    Loss --> Update[역전파 + 파라미터 업데이트]
```

1. 입력 토큰 시퀀스를 임베딩 레이어와 [[positional-encoding]]으로 변환
2. 다수의 [[multi-head-latent-attention|Transformer]] 디코더 블록을 통과 (각 블록에서 causal self-attention 적용)
3. 최종 은닉 상태를 어휘 크기의 로짓으로 변환 후 softmax 적용
4. 정답 토큰과의 cross-entropy 손실 계산
5. 추론 시에는 한 토큰씩 생성하며, [[kv-cache-inference]]로 이전 계산을 재활용하여 효율화

### CLM vs MLM 비교

| 항목 | CLM (GPT 계열) | [[masked-language-modeling|MLM]] (BERT 계열) |
|------|---------------|----------------------------------------------|
| 방향 | 단방향 (왼쪽->오른쪽) | 양방향 |
| 마스킹 | causal mask (삼각) | 랜덤 토큰 마스킹 (15%) |
| 생성 능력 | 자연스러운 텍스트 생성 | 생성에 부적합 |
| 주요 용도 | 텍스트 생성, 코드 생성, 대화 | 분류, NER, QA |
| 대표 모델 | GPT, LLaMA, Mistral | BERT, RoBERTa, ALBERT |

## 성능/효과

CLM은 단순한 목적 함수에도 불구하고 [[superposition-neural-scaling]]에 따라 모델 크기, 데이터 양, 연산량을 늘리면 예측 가능하게 성능이 향상된다. GPT-3에서 확인된 in-context learning, chain-of-thought 추론 등 창발적 능력은 CLM의 스케일링이 가져온 대표적 성과이다.

사전 학습된 CLM 모델은 이후 [[supervised-fine-tuning]]을 통해 특정 태스크에 적응하거나, [[rlhf-pipeline]]을 통해 인간 선호에 정렬된다. 2026년 현재 "CLM 사전 학습 -> SFT -> RLHF/DPO" 파이프라인이 프론티어 모델 개발의 표준 경로이다.

### 학습 데이터와 토크나이저

CLM의 성능은 사전 학습 데이터의 품질에 크게 좌우된다. [[pretraining-data-curation]]을 통한 웹 크롤 필터링, 중복 제거, 품질 분류가 필수적이다. 또한 [[tokenizer-training]]에서 어떤 서브워드 분할 알고리즘(BPE, Unigram 등)을 선택하는지가 모델의 효율성과 다국어 성능에 직접적인 영향을 미친다.

### 한계

- **노출 편향(exposure bias)**: 학습 시 교사 강제를 쓰지만 추론 시 자기 예측을 사용하는 불일치
- **단방향 문맥**: 미래 토큰을 참조할 수 없어 양방향 이해가 필요한 태스크에서 MLM 대비 불리할 수 있음
- **[[hallucination|환각(hallucination)]]**: 확률적으로 가장 높은 다음 토큰을 생성하므로 사실과 다른 내용을 유창하게 생성할 위험
- **반복 퇴화(repetition degeneration)**: 탐욕적 디코딩 시 동일 구문 반복 경향

## 대표 자료

- [Improving Language Understanding by Generative Pre-Training (GPT-1, Radford et al., 2018)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [Language Models are Unsupervised Multitask Learners (GPT-2, Radford et al., 2019)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Language Models are Few-Shot Learners (GPT-3, Brown et al., 2020)](https://arxiv.org/abs/2005.14165)
- [HuggingFace: Causal Language Modeling Guide](https://huggingface.co/docs/transformers/main/en/tasks/language_modeling)

## 관련 문서

- [[masked-language-modeling]] -- CLM과 쌍을 이루는 양방향 사전 학습 목적 함수
- [[superposition-neural-scaling]] -- CLM 모델의 스케일링 법칙
- [[supervised-fine-tuning]] -- CLM 사전 학습 이후 지도 학습 단계
- [[rlhf-pipeline]] -- SFT 이후 인간 선호 정렬 단계
- [[tokenizer-training]] -- CLM 모델에 사용되는 토크나이저 학습
- [[pretraining-data-curation]] -- 사전 학습 데이터 품질 관리
- [[transfer-learning-for-nlp]] -- CLM이 NLP 전이 학습 패러다임에서 차지하는 위치
- [[lora-qlora-finetuning]] -- CLM 모델의 파라미터 효율적 파인튜닝
