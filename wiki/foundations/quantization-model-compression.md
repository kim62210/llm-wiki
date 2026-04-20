---
title: Quantization & Model Compression (양자화와 모델 압축)
aliases: [quantization, 양자화, model compression, 모델 압축, INT8, INT4, pruning, distillation]
category: foundations
page_type: concept
tags: [quantization, model-compression, int8, int4, pruning, knowledge-distillation, inference-optimization]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# Quantization & Model Compression (양자화와 모델 압축)

## 정의

**모델 압축(Model Compression)**은 학습된 대규모 모델의 크기와 연산 비용을 줄이면서 성능을 최대한 보존하는 기법의 총칭이다. 학습 비용은 한 번이지만 추론은 수백만 번 발생하므로, 배포 단계의 효율은 곧 비용과 직결된다.

세 가지 핵심 전략: **양자화**(정밀도 축소), **가지치기**(불필요한 가중치 제거), **증류**(작은 모델로 지식 전달).

## 양자화 (Quantization)

양자화는 모델 가중치와 활성값의 수치 정밀도를 낮추는 기법이다. FP32(32비트) -> FP16(16비트) -> INT8(8비트) -> INT4(4비트)로 갈수록 메모리와 연산이 절감되지만 정보 손실이 발생한다.

### 정밀도별 비교

| 형식 | 비트 수 | 메모리 절감 | 70B 모델 크기 | 품질 영향 |
|------|--------|-----------|-------------|----------|
| FP32 | 32 | 기준 | ~280GB | 없음 |
| FP16/BF16 | 16 | 2배 | ~140GB | 무시 가능 |
| INT8 | 8 | 4배 | ~70GB | 경미 |
| INT4 | 4 | 8배 | ~35GB | 보통 |
| INT2 | 2 | 16배 | ~17.5GB | 상당 |

### PTQ vs QAT

**학습 후 양자화(Post-Training Quantization, PTQ)**: 이미 학습된 모델에 양자화를 적용한다. 추가 학습이 불필요하므로 비용이 낮다. 대부분의 실용적 양자화가 이 방식이다.

**양자화 인식 학습(Quantization-Aware Training, QAT)**: 학습 과정에서 양자화 효과를 시뮬레이션하여 모델이 저정밀도에 적응하도록 한다. PTQ보다 정확하지만 학습 비용이 추가된다.

### 주요 양자화 기법

**GPTQ**: 레이어별 최적 양자화를 수행한다. 각 가중치를 양자화할 때 나머지 가중치를 보정하여 출력 오차를 최소화한다. 4비트에서도 높은 품질을 유지하며 GPU 추론에 최적화되어 있다.

**AWQ(Activation-Aware Weight Quantization)**: 활성값 분포를 기반으로 중요한 가중치 채널을 식별하고, 해당 채널의 스케일을 조정하여 양자화 오차를 줄인다. "모든 가중치가 동등하게 중요하지 않다"는 통찰에 기반한다.

**bitsandbytes**: 즉석 양자화(on-the-fly)를 지원하여 별도 캘리브레이션 없이 모델 로딩 시 바로 INT8/INT4로 변환한다. HuggingFace Transformers와 긴밀히 통합되어 접근성이 높다.

**GGUF(llama.cpp)**: CPU 추론에 최적화된 양자화 포맷이다. 2-8비트의 다양한 양자화 레벨을 지원하며, Apple Silicon(Metal)에서도 효율적으로 동작한다. 로컬 LLM 실행의 사실상 표준이다.

### 이상치 문제와 해결

Transformer 모델의 활성값에는 소수의 극단적 이상치(outlier)가 존재한다. 이 이상치가 양자화의 동적 범위를 지배하면서 나머지 값의 정밀도가 크게 떨어진다.

**LLM.int8()**: 이상치 특징을 FP16으로 유지하고 나머지만 INT8로 양자화하는 혼합 정밀도 접근법이다.

**SmoothQuant**: 활성값의 스케일 분산을 가중치 쪽으로 오프라인에서 이전(migrate)하여 양쪽 모두 양자화하기 쉽게 만든다. 수학적으로 등가인 변환이므로 정확도 손실이 최소화된다.

## 가지치기 (Pruning)

불필요하거나 중요도가 낮은 가중치를 제거하여 모델을 희소(sparse)하게 만드는 기법이다.

### 비구조적 가지치기(Unstructured Pruning)

개별 가중치를 0으로 설정한다. 절대값이 작은 가중치부터 제거하는 **크기 기반 가지치기(Magnitude Pruning)**가 대표적이다. 높은 희소성(90%+)을 달성할 수 있지만, 불규칙한 메모리 접근 패턴 때문에 실제 하드웨어 가속이 어렵다.

### 구조적 가지치기(Structured Pruning)

뉴런, 어텐션 헤드, 레이어 전체를 제거한다. 하드웨어 친화적이며 실제 속도 향상으로 이어진다.

**N:M 희소성**: N개 중 M개 가중치만 유지하는 패턴이다. 예를 들어 2:4 희소성은 연속 4개 가중치 중 2개를 유지한다. NVIDIA A100/H100이 하드웨어 수준에서 지원하여 실제 2배 가속이 가능하다.

### 가지치기 전략

- **점진적 크기 기반 가지치기(GMP)**: 학습 중 희소성을 점진적으로 높인다
- **반복 가지치기(Iterative Pruning)**: 가지치기와 재학습을 교대로 수행
- **가중치 되감기(Weight Rewinding)**: 가지치기 후 초기 학습 단계의 가중치로 되돌린 뒤 재학습

## 지식 증류 (Knowledge Distillation)

큰 **교사(teacher) 모델**의 지식을 작은 **학생(student) 모델**로 전달하는 기법이다. 학생 모델은 정답 레이블뿐 아니라 교사 모델의 출력 확률 분포(soft labels)를 학습한다.

**왜 soft labels이 유효한가**: 교사 모델의 출력 분포에는 정답뿐 아니라 "거의 정답인 후보"에 대한 정보가 담겨 있다. 예를 들어 고양이 사진에 대해 [고양이: 0.8, 호랑이: 0.15, 개: 0.05]라는 분포는 "고양이와 호랑이는 비슷하고, 개는 다르다"는 관계 정보를 전달한다.

**대표 사례**: DistilBERT는 BERT의 파라미터를 40% 줄이면서 성능의 97%를 유지했다.

**현대 LLM에서의 증류**: 대형 모델의 출력으로 소형 모델을 학습시키는 것이 일반화되었다. Alpaca(Stanford)는 GPT-3.5의 출력으로 LLaMA 7B를 instruction-tuning한 초기 사례이다.

## 세 기법의 조합

실전에서는 세 기법을 조합하여 사용한다:

```
교사 모델 (70B, FP16)
  |
  v  [증류]
학생 모델 (7B, FP16)
  |
  v  [가지치기]
희소 학생 모델 (7B, 50% sparse)
  |
  v  [양자화]
최종 배포 모델 (7B, INT4, sparse) -- 원래 대비 ~40배 절감
```

## 실용적 선택 가이드

| 상황 | 권장 접근 |
|------|----------|
| GPU 메모리가 부족할 때 | bitsandbytes INT4/INT8 즉석 양자화 |
| 최고 품질의 INT4 | GPTQ 또는 AWQ (캘리브레이션 필요) |
| CPU/로컬 실행 | GGUF (llama.cpp) |
| 모바일/엣지 | 증류 + INT4 양자화 |
| 학습 비용 절감 | 증류로 모델 크기 축소 후 미세조정 |

## 다음에 읽을 페이지

- [[scaling-laws]] -- 모델 크기와 성능의 관계: 어디까지 줄여도 되는가
- [[distributed-training-overview]] -- 큰 모델을 학습하는 인프라 (압축의 전 단계)
- [[attention-mechanism-overview]] -- 어텐션 메커니즘: 압축이 가장 민감한 영역

## 출처

- Lilian Weng, "Large Transformer Model Inference Optimization" (2023) - https://lilianweng.github.io/posts/2023-01-10-inference-optimization/
- HuggingFace Transformers Quantization Overview - https://huggingface.co/docs/transformers/main/en/quantization/overview
- Hinton et al., "Distilling the Knowledge in a Neural Network" (2015) - https://arxiv.org/abs/1503.02531


## 관련 문서

- [[model-pruning]] -- Model Pruning (모델 가지치기)
