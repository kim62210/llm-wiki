---
title: PEFT (Parameter-Efficient Fine-Tuning 라이브러리)
category: tooling
page_type: entity
project: PEFT
tags: [peft, lora, fine-tuning, huggingface, adapter, parameter-efficient]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# PEFT (Parameter-Efficient Fine-Tuning)

Hugging Face가 개발한 파라미터 효율적 파인튜닝 라이브러리. 대규모 사전 학습 모델의 전체 가중치 대신 소수의 추가 파라미터만 학습하여 계산 비용과 저장 비용을 대폭 절감한다. [[lora-qlora-finetuning|LoRA/QLoRA]]를 포함한 다양한 PEFT 기법을 통합 인터페이스로 제공한다. 위키 내 6회 참조.

## 개요

LLM 파인튜닝의 핵심 문제는 수십억 개의 파라미터를 모두 업데이트하는 것이 GPU 메모리와 학습 시간 측면에서 비현실적이라는 점이다. PEFT 라이브러리는 이 문제를 해결하기 위해 모델의 극히 일부분(전형적으로 0.1-1%)만 학습하는 여러 기법을 구현한다. 예를 들어 Qwen2.5-3B 모델(30억 파라미터)에 LoRA를 적용하면 368만 개(0.12%)의 파라미터만 학습하면서도 경쟁력 있는 성능을 달성한다. GitHub 스타 20.9K, Apache 2.0 라이선스.

## 지원 기법

### LoRA (Low-Rank Adaptation)

가장 널리 사용되는 PEFT 기법. 모델의 특정 가중치 행렬에 저랭크(low-rank) 행렬 쌍(A, B)을 추가하여 학습한다. 원본 가중치는 동결(frozen) 상태로 유지되며, 학습 후 어댑터를 베이스 모델에 병합(merge)하면 추론 시 추가 지연이 없다. 상세한 하이퍼파라미터 가이드는 [[lora-qlora-finetuning|LoRA/QLoRA 파인튜닝]] 참조.

### Prefix Tuning

모델의 각 Transformer 레이어 앞에 학습 가능한 접두사 벡터를 추가한다. 모델 가중치 자체는 변경하지 않으면서 입력 표현을 조정하는 방식이다. 생성 태스크에 효과적이다.

### Prompt Tuning

소프트 프롬프트(soft prompt)라고도 불린다. 입력 임베딩 공간에 학습 가능한 연속 벡터를 추가하여, 모델의 행동을 태스크에 맞게 조정한다. 디스크릿 프롬프트 엔지니어링의 연속 최적화 버전이라고 할 수 있다.

### IA3 (Infused Adapter by Inhibiting and Amplifying Inner Activations)

학습된 벡터로 키(key), 값(value), 피드포워드 레이어의 활성화를 선택적으로 스케일링한다. LoRA보다 학습 파라미터가 적으면서도 유사한 성능을 달성할 수 있다.

### 추가 지원 기법

AdaLoRA(적응적 랭크 할당), LoftQ(양자화 인식 초기화), 멀티태스크 프롬프트 튜닝 등 다양한 최신 기법을 지속적으로 통합하고 있다.

## 메모리 효율성

PEFT의 핵심 가치는 GPU 메모리 절감이다.

| 모델 | 전체 파인튜닝 | PEFT-LoRA | 메모리 절감 |
|------|-------------|----------|----------|
| T0-3B (3B) | 47.14 GB | 14.4 GB | 약 70% |
| bloomz-7b1 (7B) | OOM (메모리 부족) | 32 GB | 실행 가능화 |
| mt0-xxl (12B) | OOM | 56 GB | 실행 가능화 |

어댑터 체크포인트 크기도 약 8-19 MB로, 전체 모델(수 GB-수십 GB) 대비 극히 작다. 이는 "하나의 베이스 모델 + 다수 어댑터" 패턴을 실용적으로 만든다.

## 사용법

### 설치 및 기본 설정

```python
# pip install peft
from transformers import AutoModelForCausalLM
from peft import LoraConfig, TaskType, get_peft_model

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
# trainable params: 3,670,016 || all params: 3,093,903,360 || trainable%: 0.12%
```

### 추론 시 어댑터 로드

```python
from peft import PeftModel

base_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
model = PeftModel.from_pretrained(base_model, "my-adapter-path")
```

### 멀티 어댑터 전환

단일 베이스 모델에서 여러 태스크별 어댑터를 동적으로 전환할 수 있다.

```python
model.load_adapter("adapter_1", adapter_name="task1")
model.load_adapter("adapter_2", adapter_name="task2")
model.set_adapter("task1")  # 태스크 1용 어댑터 활성화
```

## 생태계 통합

PEFT는 Hugging Face 생태계의 핵심 컴포넌트로, 다양한 라이브러리와 긴밀히 통합된다.

| 라이브러리 | 통합 방식 |
|-----------|----------|
| Transformers | `add_adapter()`, `load_adapter()`, `set_adapter()` 네이티브 메서드 |
| Diffusers | 이미지 생성 모델 LoRA (어댑터 크기 약 19MB) |
| Accelerate | 분산 학습, 멀티 GPU 추론 |
| TRL | [[rlhf-pipeline|RLHF]], [[direct-preference-optimization|DPO]] 기반 학습 |
| [[huggingface-hub|Hugging Face Hub]] | 어댑터 업로드/다운로드/공유 |

## 양자화 결합

4비트/8비트 양자화와 PEFT를 결합하면 메모리를 추가로 절감할 수 있다. [[lora-qlora-finetuning|QLoRA]]는 NormalFloat4(NF4) 양자화된 베이스 모델에 LoRA를 적용하는 대표적인 결합 기법으로, 65B 모델을 단일 48GB GPU에서 파인튜닝할 수 있게 한다.

## 관련 페이지

- [[lora-qlora-finetuning|LoRA/QLoRA 파인튜닝]] -- PEFT의 대표 기법 상세
- [[huggingface-hub|Hugging Face Hub]] -- PEFT 어댑터 공유 플랫폼
- [[rlhf-pipeline|RLHF 파이프라인]] -- PEFT + TRL로 보상 모델 학습
- [[supervised-fine-tuning|SFT]] -- PEFT가 적용되는 학습 단계
- [[training-frameworks|학습 프레임워크]] -- 학습 인프라 전체 맵
