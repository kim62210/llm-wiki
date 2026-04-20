---
title: "Language Models are Few-Shot Learners (GPT-3, Brown et al., 2020)"
category: papers
page_type: paper
tags: [gpt-3, few-shot, in-context-learning, scaling]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# Language Models are Few-Shot Learners (GPT-3, Brown et al., 2020)

## 핵심 기여

OpenAI가 2020년 발표한 GPT-3(Generative Pre-trained Transformer 3)는 당시 세계 최대 규모인 **175B(1,750억) 파라미터** 언어 모델로, 파인튜닝(fine-tuning) 없이 프롬프트 내 예시만으로 다양한 NLP(Natural Language Processing) 태스크를 수행하는 **인컨텍스트 학습(in-context learning)** 개념을 대규모로 실증했다.

## 방법

### 아키텍처

GPT-2와 동일한 디코더 전용(decoder-only) Transformer 구조. 모델 크기에 따라 다양한 변형 존재:

- GPT-3 Small (125M) ~ GPT-3 (175B)까지 8가지 크기
- 96개 어텐션 헤드, 12,288 차원, 96개 레이어 (175B 기준)
- 300B 토큰 학습 데이터 (Common Crawl, WebText, Books, Wikipedia 등)

### 인컨텍스트 학습 (In-Context Learning)

파라미터 업데이트 없이 프롬프트만으로 태스크 적응:

- **제로샷(Zero-shot)**: 태스크 설명만 제공
- **원샷(One-shot)**: 예시 1개 제공
- **퓨샷(Few-shot)**: 예시 K개 제공 (K는 보통 10-100)

모델이 마치 "메타 학습(meta-learning)"을 수행하듯 프롬프트 패턴으로부터 태스크를 즉석 추론한다.

### 스케일링 관찰

모델 크기가 커질수록 퓨샷 성능이 비선형적으로 향상되며, 일부 태스크에서는 파인튜닝된 소형 모델보다도 우수한 성능을 보임.

## 결과 및 영향

- 다양한 NLP 벤치마크(TriviaQA, CoQA, WinoGrande 등)에서 파인튜닝 없이 SOTA에 근접하거나 초과
- **창발적 능력(emergent abilities)**: 충분한 스케일에서만 나타나는 새로운 능력 현상 최초 관찰
- 이후 ChatGPT, GPT-4, InstructGPT 등 모든 GPT 계열의 직접 선조
- 프롬프트 엔지니어링(prompt engineering) 연구 분야를 본격 촉발

## 한계

- 퓨샷 성능이 예시 선택 방식에 민감함 (프롬프트 설계에 따라 결과 편차 큼)
- 사실 정확도(factual accuracy)가 낮고 환각(hallucination)이 많음
- 지식 커트오프(knowledge cutoff) 문제
- 인간 가치와 의도에 정렬되지 않음 - InstructGPT로 보완
- 175B 모델 서빙 비용이 매우 높아 상용화 어려움

## 실무 적용 관점

- 인컨텍스트 학습의 원리를 이해하면 현재의 프롬프트 엔지니어링이 왜 효과가 있는지 설명 가능
- 모델 크기와 데이터 크기의 균형 - 이후 Chinchilla 논문이 GPT-3의 모델 과대/데이터 과소 문제를 지적
- 퓨샷 예시 품질과 순서가 성능에 직접 영향 → 프롬프트 데이터 큐레이션(curation) 중요

## 관련 문서

- [[Attention Is All You Need (Transformer 원논문)]]
- [[InstructGPT RLHF 정렬]]
- [[scaling-laws]]
- [[in-context-learning]]
- [[emergent-abilities]]
