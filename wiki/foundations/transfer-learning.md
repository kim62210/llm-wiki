---
title: Transfer Learning (전이 학습)
aliases: [transfer learning, 전이 학습, pretrain-finetune, ULMFiT]
category: foundations
page_type: concept
tags: [transfer-learning, ulmfit, pretrain-finetune, foundation-model, nlp]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# Transfer Learning (전이 학습)

## 정의

**전이 학습(Transfer Learning)**은 하나의 태스크에서 학습한 지식을 다른 태스크에 재사용하는 기법이다. 컴퓨터 비전에서는 ImageNet 사전학습이 2012년부터 표준이었지만, NLP에서는 2018년까지 각 태스크마다 처음부터 학습하는 것이 관례였다. ULMFiT와 BERT가 이 관행을 뒤집었다.

## 왜 전이 학습이 작동하는가

신경망의 하위 레이어는 범용적 특징(구문 구조, 단어 관계)을 학습하고, 상위 레이어로 갈수록 태스크 특화 특징을 학습한다. 대규모 데이터로 사전학습된 모델의 하위 레이어 가중치는 새로운 태스크에도 유용하다. 이 원리가 전이 학습의 핵심이다.

전이 학습의 이점:

- **데이터 효율성**: 소량의 레이블 데이터로도 높은 성능 달성
- **학습 시간 단축**: 사전학습된 가중치에서 출발하므로 수렴이 빠름
- **일반화 향상**: 대규모 코퍼스에서 학습한 표현이 과적합을 방지

## ULMFiT: NLP 전이 학습의 기원 (2018)

Jeremy Howard와 Sebastian Ruder가 제안한 **ULMFiT(Universal Language Model Fine-tuning)**은 NLP에서 전이 학습이 체계적으로 작동함을 최초로 입증했다. 핵심 결과: 100개의 레이블 데이터만으로 100배 더 많은 데이터로 처음부터 학습한 모델과 동등한 성능을 달성했으며, 6개 텍스트 분류 벤치마크에서 오류를 18-24% 줄였다.

### 3단계 프로세스

```
1. 범용 언어 모델 사전학습 (General-Domain LM Pretraining)
   대규모 비지도 코퍼스(예: Wikitext-103)에서 다음 단어 예측
   
2. 도메인 적응 미세조정 (Target-Domain LM Fine-tuning)
   목표 도메인 데이터로 언어 모델을 추가 학습
   
3. 분류기 미세조정 (Classifier Fine-tuning)
   레이블 데이터로 최종 태스크 학습
```

### ULMFiT의 핵심 기법

**판별적 미세조정(Discriminative Fine-tuning)**: 레이어마다 다른 학습률을 적용한다. 하위 레이어(범용 특징)는 느리게, 상위 레이어(태스크 특화)는 빠르게 업데이트한다.

**기울어진 삼각형 학습률(Slanted Triangular Learning Rates)**: 학습률을 빠르게 올린 후 천천히 감소시킨다. 초반에 적절한 영역을 빠르게 탐색하고, 후반에 정밀 수렴한다.

**점진적 해동(Gradual Unfreezing)**: 마지막 레이어부터 순차적으로 동결을 해제하며 미세조정한다. 사전학습된 범용 지식이 파괴되는 것(catastrophic forgetting)을 방지한다.

## 사전학습-미세조정 패러다임의 확장

ULMFiT 이후 사전학습-미세조정 패러다임은 NLP 전체를 재편했다:

| 모델 | 연도 | 사전학습 방식 | 특징 |
|------|------|-------------|------|
| ULMFiT | 2018 | 단방향 LM | NLP 전이 학습 최초 체계화 |
| ELMo | 2018 | 양방향 LSTM | 문맥 의존적 임베딩 |
| GPT-1 | 2018 | 단방향 Transformer | Transformer 기반 사전학습 |
| BERT | 2018 | 마스크 언어 모델(MLM) | 양방향 Transformer, 미세조정 표준화 |
| GPT-2/3 | 2019/2020 | 자기회귀 LM | 스케일업, few-shot/zero-shot |
| T5 | 2020 | 텍스트-투-텍스트 | 모든 태스크를 텍스트 생성으로 통합 |

## GPT 시대: 미세조정에서 프롬프팅으로

GPT-3(2020)는 전이 학습의 패러다임을 한 단계 더 전환시켰다. 모델이 충분히 크면 미세조정 없이 프롬프트만으로 태스크를 수행할 수 있음을 보여줬다(few-shot, zero-shot learning). 이것이 현재의 **프롬프트 엔지니어링** 시대로 이어졌다.

그러나 미세조정은 사라지지 않았다. 현대 LLM 파이프라인은 여전히 전이 학습의 확장판이다:

```
사전학습(Pretraining) -> SFT(지도 미세조정) -> RLHF/DPO(선호도 정렬)
```

각 단계가 이전 단계의 지식을 전이받아 점진적으로 특화된다.

## 현대적 변형: 파라미터 효율적 미세조정

전체 모델을 미세조정하는 것은 수십억 파라미터 시대에 비용이 크다. **PEFT(Parameter-Efficient Fine-Tuning)** 기법들이 등장했다:

- **LoRA(Low-Rank Adaptation)**: 가중치 행렬의 저랭크 분해로 학습 파라미터를 0.1% 수준으로 축소
- **Adapter**: 레이어 사이에 소규모 모듈 삽입
- **Prefix Tuning**: 입력 앞에 학습 가능한 벡터 추가

이 기법들은 ULMFiT의 "필요한 부분만 조정한다"는 철학의 직계 후손이다.

## 다음에 읽을 페이지

- [[scaling-laws]] -- 모델 크기와 성능의 관계: 왜 큰 모델이 더 잘 전이하는가
- [[attention-mechanism-overview]] -- Transformer 어텐션의 진화: 전이 학습을 가능케 한 아키텍처
- [[distributed-training-overview]] -- 대규모 사전학습을 위한 분산 학습 기초

## 출처

- Howard & Ruder, "Universal Language Model Fine-tuning for Text Classification" (2018) - https://arxiv.org/abs/1801.06146
- Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers" (2018) - https://arxiv.org/abs/1810.04805
- Brown et al., "Language Models are Few-Shot Learners" (GPT-3, 2020) - https://arxiv.org/abs/2005.14165


## 관련 문서

- [[nlp-overview]] -- NLP 개요 (Natural Language Processing Overview)
