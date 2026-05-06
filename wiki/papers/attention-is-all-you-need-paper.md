---
title: "Attention Is All You Need (Vaswani et al., 2017)"
category: papers
page_type: paper
tags: [transformer, self-attention, multi-head-attention, encoder-decoder]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# Attention Is All You Need (Vaswani et al., 2017)

## 핵심 기여

2017년 Google Brain이 발표한 이 논문은 RNN(Recurrent Neural Network)과 CNN(Convolutional Neural Network) 없이 순수하게 어텐션(attention) 메커니즘만으로 시퀀스 변환(sequence-to-sequence) 문제를 해결한 최초의 모델인 **Transformer**를 제안했다. 173,000회 이상 인용된 현대 LLM(Large Language Model) 아키텍처의 직접 조상이다.

## 방법

### 핵심 아키텍처

- **인코더-디코더 구조**: 각 6개 레이어로 구성
- **멀티헤드 어텐션(Multi-Head Attention)**: 서로 다른 표현 부분 공간(representation subspace)에서 병렬로 어텐션 수행. h개의 헤드가 독립적으로 쿼리(Q), 키(K), 값(V) 행렬에 어텐션을 적용한 후 결합
- **스케일드 닷-프로덕트 어텐션(Scaled Dot-Product Attention)**: $\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- **포지셔널 인코딩(Positional Encoding)**: 사인/코사인 함수 기반으로 시퀀스 내 위치 정보 주입 (RNN처럼 순차 처리하지 않으므로 위치 정보가 별도 필요)
- **피드포워드 네트워크(Feed-Forward Network)**: 각 레이어에 위치별 2층 완전연결 서브레이어 포함
- **잔차 연결(Residual Connection) + 레이어 정규화(Layer Normalization)**: 각 서브레이어에 적용

### 설계 철학

순환 구조를 없애 **완전한 병렬화**가 가능해졌다. 시퀀스 길이에 무관하게 임의의 두 위치 간 의존성을 한 번의 연산으로 포착한다.

## 결과 및 영향

- WMT 2014 영독(English-German) 번역: BLEU 28.4 (당시 SOTA 대비 2 포인트 이상 향상)
- WMT 2014 영불(English-French) 번역: BLEU 41.0 (단일 모델 기준 최고 기록)
- 훈련 비용이 기존 RNN 기반 모델 대비 대폭 절감 (8 GPU, 3.5일)
- **모든 현대 LLM의 직접 조상**: GPT, BERT, T5, PaLM, LLaMA 등이 모두 이 아키텍처를 기반으로 함

## 한계

- 셀프 어텐션의 연산 복잡도는 시퀀스 길이 $n$에 대해 $O(n^2)$ - 긴 컨텍스트에서 병목
- 위치 인코딩 방식이 훈련 시 봤던 길이를 크게 넘어서면 일반화 어려움
- 포지셔널 인코딩이 고정된 방식이므로 이후 로터리 임베딩(RoPE, Rotary Position Embedding) 등으로 개선됨

## 실무 적용 관점

- 모든 Transformer 기반 모델 코드를 읽을 때 이 논문의 구조를 기준점으로 삼을 것
- 멀티헤드 어텐션의 헤드 수(`num_heads`)와 모델 차원(`d_model`)은 헤드당 차원(`d_k = d_model / num_heads`)이 충분히 커야 한다는 설계 원칙
- 포지셔널 인코딩 → RoPE → ALiBi 등의 진화 경로를 이해하면 최신 LLM 설계 파악에 도움

## 관련 문서

- [[BERT 인코더 양방향 사전학습]]
- [[GPT-3 스케일링과 인컨텍스트 학습]]
- [[self-attention-mechanism]]
- [[multi-head-attention]]
- [[transformer-architecture|Transformer 아키텍처]]
