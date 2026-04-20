---
title: 학습 프레임워크 (PyTorch / JAX / Megatron-LM / NeMo)
category: tooling
page_type: entity
project: Training Frameworks
tags: [tooling, pytorch, jax, megatron-lm, nemo, distributed-training, framework]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 학습 프레임워크

## 개요

LLM 학습 프레임워크는 모델 정의, 분산 학습, 체크포인팅, 혼합 정밀도 등의 기능을 통합 제공하는 소프트웨어 스택이다. 2026년 현재 PyTorch가 연구와 산업 모두에서 지배적이며, JAX는 Google 생태계와 고급 연구에서, NVIDIA의 Megatron-LM과 NeMo는 대규모 사전학습에서 핵심 위치를 차지한다. 프레임워크 선택은 [[data-parallelism-fsdp]], [[tensor-pipeline-parallelism]], [[deepspeed-zero]] 등 분산 학습 전략의 구현 방식에 직접적 영향을 미친다.

## PyTorch

### 개요

Meta(구 Facebook)가 개발한 딥러닝 프레임워크로, 동적 계산 그래프(eager mode)와 Pythonic API가 핵심 특징이다. 2026년 현재 ML 연구 논문의 80% 이상이 PyTorch를 사용하며, HuggingFace Transformers, DeepSpeed, TorchTitan 등 핵심 생태계가 PyTorch 위에 구축되어 있다.

**핵심 분산 학습 기능**:
- `torch.distributed`: DDP, [[data-parallelism-fsdp]]의 FSDP2 네이티브 지원
- `torch.amp`: [[mixed-precision-training]] 자동화
- TorchTitan: TP + PP + DP 다차원 병렬화 통합 솔루션
- `torch.compile`: 그래프 최적화로 연산 속도 향상

**장점**: 생태계 최대, 디버깅 용이(eager mode), 빠른 프로토타이핑
**단점**: 순수 eager mode에서는 JAX XLA 대비 연산 최적화 제한적

### 최신 발전 (2025-2026)

- **FSDP2**: DTensor 기반 per-parameter 샤딩으로 FSDP1 대체
- **TorchTitan**: 프로덕션급 LLM 사전학습을 위한 올인원 솔루션
- **torch.compile 성숙**: 학습 워크로드에서도 안정적 성능 향상
- **Distributed Checkpoint (DCP)**: 리샤딩, 비동기 저장 지원

## JAX

### 개요

Google이 개발한 함수형 프로그래밍 기반 ML 프레임워크다. 순수 함수와 불변 데이터 구조를 강조하며, XLA(Accelerated Linear Algebra) 컴파일러를 통해 자동으로 연산 그래프를 최적화한다. Google의 TPU 생태계와 긴밀하게 통합되어 있다.

**핵심 기능**:
- `jax.jit`: XLA 컴파일로 자동 최적화
- `jax.pmap`: 단일 명령어로 다중 디바이스 병렬화
- `jax.vmap`: 자동 벡터화
- `jax.grad`: 자동 미분

**장점**: XLA 최적화로 높은 연산 효율, TPU 네이티브 지원, 함수형 스타일의 재현성
**단점**: 학습 곡선 가파름, 함수형 패러다임 강제, PyTorch 대비 작은 생태계

**주요 사용처**: Google DeepMind(Gemini), 고급 ML 연구, TPU 기반 학습

### JAX 기반 학습 라이브러리

- **Flax**: Google 공식 신경망 라이브러리
- **Optax**: 옵티마이저 라이브러리 ([[optimizer-selection]] 관련)
- **MaxText**: Google의 LLM 학습 레퍼런스 구현 (WSD 스케줄 등 지원)
- **Orbax**: 체크포인팅 라이브러리

## Megatron-LM

### 개요

NVIDIA가 개발한 대규모 Transformer 모델 학습 전용 프레임워크다. [[tensor-pipeline-parallelism]]을 체계화한 논문(2019)과 함께 공개되었으며, 수조 파라미터 규모의 LLM 사전학습에 최적화되어 있다.

**핵심 기능**:
- **Megatron Core**: GPU 최적화 학습 기법의 모듈러 라이브러리
- **텐서/파이프라인/시퀀스/컨텍스트/전문가 병렬화**: 6차원 이상의 병렬화
- **Megatron Bridge**: HuggingFace <-> Megatron 체크포인트 양방향 변환
- **Dynamic Context Parallelism**: 가변 길이 시퀀스에서 최대 1.48x 속도 향상

**장점**: 최고 수준의 학습 처리량, NVIDIA GPU 최적화, 프로덕션 검증
**단점**: NVIDIA GPU 전용, 높은 진입 장벽, 연구용 프로토타이핑에는 과도

### Megatron-DeepSpeed

Megatron-LM의 모델 병렬화와 [[deepspeed-zero]]의 메모리 최적화를 결합한 프로젝트다. ZeRO Stage 1-3과 TP/PP를 동시에 활용하여 최대 규모의 모델 학습이 가능하다.

## NeMo Framework

### 개요

NVIDIA의 엔드투엔드 LLM 개발 프레임워크다. Megatron Core를 핵심 학습 엔진으로 사용하면서, 데이터 큐레이션, 사전학습, 파인튜닝, 정렬(alignment), 추론까지의 전체 라이프사이클을 통합한다.

**핵심 구성요소**:
- **NeMo Megatron Bridge**: Megatron Core 기반 학습 루프, 6D 병렬화 지원
- **NeMo-RL v0.3**: Megatron Core 백엔드로 효율적 RLHF/DPO 후학습
- **NeMo Curator**: 대규모 학습 데이터 큐레이션
- **NeMo Guardrails**: 추론 시 안전성 제어

**장점**: 사전학습부터 배포까지 통합, NVIDIA 하드웨어 최적화, 엔터프라이즈 지원
**단점**: NVIDIA 생태계 종속, 무거운 의존성

### 체크포인팅 성능

NeMo의 분산 체크포인팅은 PyTorch 네이티브 대비 Nemotron-4 15B에서 50배, 340B에서 26배 빠른 [[model-checkpointing-sharding]] 성능을 달성했다.

## 프레임워크 비교

### 사용 목적별 권장

| 목적 | 1순위 | 2순위 | 비고 |
|------|------|------|------|
| 연구/프로토타이핑 | PyTorch | JAX | 유연성, 디버깅 |
| 소규모 학습/파인튜닝 | PyTorch + HF | NeMo | [[lora-qlora-finetuning]] 생태계 |
| 대규모 사전학습 | NeMo / Megatron | JAX + MaxText | 처리량 최적화 |
| Google TPU 환경 | JAX | - | TPU 네이티브 |
| NVIDIA GPU 최적화 | NeMo / Megatron | PyTorch + TorchTitan | GPU 전용 최적화 |
| 엔터프라이즈 MLOps | NeMo | PyTorch + 커스텀 | 통합 파이프라인 |

### 생태계 통합

| 기능 | PyTorch | JAX | Megatron | NeMo |
|------|---------|-----|----------|------|
| 분산 학습 | FSDP2, DDP | pjit, pmap | TP/PP 네이티브 | Megatron Core |
| [[mixed-precision-training]] | torch.amp | jax.default_matmul_precision | Transformer Engine | Transformer Engine |
| [[experiment-tracking]] | W&B, MLflow | W&B, TensorBoard | 커스텀 | W&B, TensorBoard |
| 모델 허브 | HuggingFace Hub | HuggingFace Hub | Megatron Bridge | NGC, HuggingFace |
| [[optimizer-selection]] | torch.optim | Optax | 내장 | Megatron Core |

## 관련 문서

- [[data-parallelism-fsdp]] -- PyTorch FSDP2
- [[tensor-pipeline-parallelism]] -- Megatron-LM TP/PP
- [[deepspeed-zero]] -- PyTorch 기반 메모리 최적화
- [[mixed-precision-training]] -- AMP, Transformer Engine
- [[model-checkpointing-sharding]] -- 분산 체크포인팅
- [[experiment-tracking]] -- W&B, MLflow 통합
- [[nvidia-vera-rubin]] -- 학습 하드웨어
