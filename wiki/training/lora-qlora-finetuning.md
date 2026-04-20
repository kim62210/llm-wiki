---
title: LoRA/QLoRA 파인튜닝 (2026 표준)
category: training
page_type: concept
tags: [training, lora, qlora, [[supervised-fine-tuning|fine-tuning]], peft, adapter]
sources: [raw/2026-04-14-ai-hot-topics-100.md]
created: 2026-04-14
updated: 2026-04-14
---

# LoRA/QLoRA 파인튜닝

## 개요

LoRA(Low-Rank Adaptation)는 사전 학습된 가중치를 동결하고, 저랭크(low-rank) 분해된 두 개의 작은 행렬만 학습하는 파라미터 효율적 파인튜닝(PEFT) 기법이다. QLoRA는 베이스 모델을 4비트로 [[ai-inference-quantization-2026|양자화]]한 상태에서 LoRA를 적용하여 메모리를 추가로 절감한다. 2026년 현재 "하나의 베이스 모델 + 다수 LoRA 어댑터" 패턴이 기업 표준으로 자리잡았으며, QLoRA로 65B 모델을 단일 48GB GPU에서 파인튜닝할 수 있다.

## 핵심 개념

### 저랭크 분해 (Low-Rank Decomposition)

전체 가중치 행렬 W를 직접 업데이트하는 대신, 두 개의 작은 행렬 A와 B의 곱(BA)으로 업데이트를 근사한다. 원본 가중치는 동결 상태로 유지되며, 학습 후 어댑터 가중치를 베이스 모델에 병합(merge)하면 추론 지연시간 추가가 없다.

### 주요 하이퍼파라미터

| 파라미터 | 설명 | 권장값 |
|----------|------|--------|
| r (rank) | 업데이트 행렬의 랭크. 낮을수록 파라미터가 적음 | 8-64 (태스크 복잡도에 비례) |
| lora_alpha | LoRA 스케일링 인자 | r의 2-4배 (예: r=8이면 alpha=32) |
| target_modules | LoRA를 적용할 모듈 | ["q_proj", "k_proj", "v_proj", "o_proj"] |
| lora_dropout | 드롭아웃 비율 | 0.05-0.1 |
| init_lora_weights | 초기화 전략 | kaiming, gaussian, loftq |
| bias | 바이어스 학습 여부 | "none" (대부분의 경우) |

Rank-Stabilized LoRA는 `lora_alpha/sqrt(r)`로 스케일링을 안정화하여 랭크 변경 시 학습 동작의 일관성을 유지한다.

### 권장 학습 파라미터

| 모델 크기 | 학습률 | 배치 크기 | 비고 |
|-----------|--------|-----------|------|
| < 33B (LoRA) | 2e-4 | 128-256 | 표준 설정 |
| >= 33B (LoRA) | 1e-4 | 128-256 | 큰 모델은 낮은 학습률 |
| QLoRA | 2e-4 | 16-64 | 메모리 제약으로 작은 배치 |

혼합 정밀도(FP16/BF16) + 그래디언트 체크포인팅으로 VRAM 사용량을 약 50% 추가 절감 가능하다.

### QLoRA와 LoftQ 초기화

QLoRA는 베이스 모델을 4비트 NF4(NormalFloat4)로 양자화한 상태에서 LoRA를 학습한다. 이중 양자화(Double Quantization) 지원으로 양자화 상수 자체도 양자화하여 메모리를 추가 절감한다. LoftQ 초기화는 양자화 전에 LoRA 가중치를 양자화 오차를 최소화하도록 초기화하여 성능을 개선한다.

### LoRA vs QLoRA 비교

| 항목 | LoRA | QLoRA |
|------|------|-------|
| 베이스 모델 정밀도 | FP16/BF16 | 4비트 NF4 |
| 7B 모델 메모리 | ~14GB | ~10GB (33% 감소) |
| 학습 시간 (7B) | ~2시간 | ~3시간 |
| 65B 모델 | 다중 GPU 필요 | 단일 48GB GPU 가능 |

### 코드 예시 (PEFT v0.10.0+)

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["k_proj", "v_proj", "q_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(base_model, config)
```

## 작동 원리

```mermaid
flowchart LR
    Base[베이스 모델 W 동결] --> LoRA[A, B 행렬 학습]
    LoRA --> Merge[W + BA 병합]
    Merge --> Deploy[추론 배포]
    
    Base --> Q[4비트 양자화 QLoRA]
    Q --> LoRA
```

1. 베이스 모델의 가중치를 동결
2. 타겟 모듈에 저랭크 행렬 A, B 삽입
3. A, B만 학습 (원본 파라미터의 극히 일부)
4. 학습 완료 후 `merge_and_unload()`로 베이스에 병합
5. 다수 어댑터를 `add_weighted_adapter()`로 조합 가능

### 멀티 어댑터 패턴

하나의 베이스 모델에 용도별 어댑터를 교체 장착하는 것이 2026년 기업 표준이다. 어댑터 교체(`unmerge_adapter` -> 새 어댑터 `merge_adapter`)가 모델 전체 재배포 없이 가능하다.

## 성능/효과

- 전체 파인튜닝 대비 학습 파라미터 수를 99% 이상 감소
- QLoRA로 65B 모델을 단일 48GB GPU(A6000/A100)에서 파인튜닝
- 완전 파인튜닝과 동등한 성능 달성 (다수 벤치마크에서 검증)
- 추론 시 병합 후 추가 지연시간 없음
- 어댑터 파일 크기가 수십~수백 MB로 배포 및 버전 관리 용이

### 실전 사례

의료 도메인 파인튜닝 사례에서 다음과 같은 결과를 보고:

| 지표 | 베이스라인 | LoRA 파인튜닝 후 |
|------|-----------|-----------------|
| F1 Score | 81.2% | 92.3% |
| 토큰당 지연시간 | 120ms | 37ms (3.2x 개선) |
| 학습 메모리 | - | 18GB (단일 GPU) |

### 주요 프레임워크 호환성

- Hugging Face Transformers + PEFT (v0.10.0+)
- bitsandbytes (v0.49.2+): 4비트 NF4 양자화
- Flash Attention, Liger Kernels 통합 지원
- Mistral, LLaMA, Qwen, BloomZ 등 주요 모델 지원

## 실전 도입 가이드

### 언제 LoRA vs QLoRA를 선택하는가

| 상황 | 권장 | 근거 |
|------|------|------|
| GPU 메모리 충분 (80GB+) | LoRA | 빠른 학습 속도 |
| 단일 소비자급 GPU (24-48GB) | QLoRA | 메모리 절감 |
| 65B+ 대형 모델 | QLoRA 필수 | 단일 GPU 적합성 |
| 추론 지연시간 민감 | LoRA (병합 후) | 추가 지연시간 제로 |
| 다수 어댑터 동시 운영 | LoRA + 동적 로딩 | 어댑터 교체 경량 |

### 흔한 실수와 해결

- **과적합**: r 값을 너무 높게 설정하면 소규모 데이터셋에서 과적합 발생. r=8-16에서 시작하여 점진 증가 권장
- **학습률**: QLoRA에서 LoRA와 동일한 학습률 사용 시 불안정. QLoRA는 약간 낮은 학습률(1e-4) 권장
- **타겟 모듈 누락**: 어텐션 블록만 타겟팅하면 성능이 제한적. 프로젝션 레이어(q, k, v, o)를 모두 포함하는 것이 일반적으로 효과적
- **양자화 순서**: QLoRA 적용 시 반드시 베이스 모델 양자화 후 LoRA를 삽입. 역순은 성능 저하

### 2026년 생태계 동향

"하나의 베이스 모델 + 다수 LoRA 어댑터" 패턴이 기업 표준으로 자리잡으면서, 어댑터 허브(adapter hub)와 어댑터 마켓플레이스가 등장하고 있다. [[apple-foundation-model]]의 LoRA 어댑터 동적 로딩 시스템은 이 패턴의 대표적인 상용 구현 사례이다.

## 관련 문서
- [[prefix-tuning-prompt-tuning]] -- 프리픽스 튜닝과 프롬프트 튜닝
- [[causal-language-modeling]]
- [[data-parallelism-fsdp]]

- [[knowledge-distillation]] -- 모델 압축의 또 다른 축
- [[small-language-models]] -- LoRA 파인튜닝의 주요 타겟
- [[synthetic-data-training]] -- 파인튜닝용 합성 데이터 생성
- [[apple-foundation-model]] -- LoRA 어댑터 동적 로딩의 상용 사례
