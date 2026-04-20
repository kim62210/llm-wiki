---
title: [[blackwell-ultra-b300|NVIDIA]] Groq 3 LPU
category: inference
page_type: entity
project: Groq 3 LPU
tags: [inference, entity, nvidia, groq, lpu, sram, decode, accelerator]
sources: [raw/2026-04-14-ai-hot-topics-100.md]
created: 2026-04-14
updated: 2026-04-14
---
# NVIDIA Groq 3 LPU

NVIDIA가 200억 달러에 인수한 Groq의 SRAM 기반 추론 가속기. Vera Rubin 플랫폼의 디코드 코프로세서(Decode Coprocessor)로 통합되며, Samsung 4nm 공정으로 제조, 2026년 Q3 출하 예정. GTC 2026에서 최초 공개되었다.

## 개요

Groq의 LPU(Language Processing Unit)는 전통적인 GPU와 근본적으로 다른 추론 전용 아키텍처다. GPU가 범용 병렬 처리에 최적화된 반면, LPU는 언어 모델의 순차적 토큰 생성(Sequential Token Generation)에 특화된 결정론적(Deterministic), 컴파일러 오케스트레이션(Compiler-Orchestrated) 설계를 채택했다. 하드웨어 캐싱 대신 명시적 데이터 이동(Explicit Data Movement)을 사용하여 지연 시간의 예측 가능성을 극대화한다. NVIDIA는 이 기술의 전략적 가치를 인정하여 200억 달러를 투자했으며, Groq 3 LPU는 그 첫 번째 결실이다.

## 핵심 사양

### LP30 칩 스펙 (단일 LPU)

| 항목 | 사양 |
|------|------|
| 온칩 SRAM | 500 MB |
| SRAM 대역폭 | 150 TB/s |
| FP8 연산 성능 | 1.2 PFLOPS |
| C2C 링크 | 96개 x 112 Gbps (총 2.5 TB/s 스케일업) |
| 제조 공정 | Samsung 4nm |
| 설계 방식 | 결정론적, 컴파일러 오케스트레이션 |

### LPX 랙 구성 (256 LPU)

| 항목 | 사양 |
|------|------|
| LPU 수 | 256개 (32 트레이 x 8 LPU) |
| 총 SRAM 용량 | 128 GB |
| 총 SRAM 대역폭 | 40 PB/s |
| 총 FP8 성능 | 315 PFLOPS |
| 총 스케일업 대역폭 | 640 TB/s |
| 물리 구성 | 32개 액체 냉각 1U 트레이 |

### 트레이 단위 (8 LPU)

| 항목 | 사양 |
|------|------|
| SRAM | 4 GB |
| 대역폭 | 1.2 PB/s |
| FP8 성능 | 9.6 PFLOPS |
| 스케일업 | 20 TB/s |

## 핵심 특징

### SRAM 기반 아키텍처
기존 GPU가 HBM(High Bandwidth Memory) 기반으로 동작하는 것과 달리, Groq LPU는 SRAM을 주 메모리로 사용한다. SRAM은 HBM 대비 접근 지연이 극히 짧아 추론 시 예측 불가능성(Unpredictability)을 제거한다. 단일 LPU 기준 150 TB/s의 SRAM 대역폭은 최신 HBM4의 메모리 대역폭을 크게 상회한다.

### 결정론적 추론 설계
GPU 추론에서 발생하는 비결정적(Non-Deterministic) 스케줄링과 메모리 접근 패턴을 제거하여, 일관된 지연 시간과 처리량을 보장한다. 컴파일러가 모든 데이터 이동을 명시적으로 제어하는 구조로, 하드웨어 캐시 미스에 의한 성능 변동이 원천적으로 없다.

### Vera Rubin 통합
Groq 3 LPU는 독립 제품이 아니라 [[nvidia-vera-rubin]] 플랫폼의 디코드 코프로세서로 작동한다. Rubin GPU가 프리필(Prefill) 단계를 처리하고, Groq 3 LPU가 디코드(Decode) 단계를 담당하는 분업 구조로 전체 추론 파이프라인을 최적화한다.

## 기술 상세

### GPU vs LPU 비교

| 특성 | GPU (Rubin) | LPU (Groq 3 LP30) |
|------|-------------|---------------------|
| 주 메모리 | HBM4 | SRAM (500 MB/칩) |
| 메모리 대역폭 | ~10 TB/s (HBM4) | 150 TB/s (SRAM) |
| 설계 목적 | 범용 병렬 처리 + 학습 | 추론 전용 (디코드) |
| 스케줄링 | 비결정적 (하드웨어 스케줄러) | 결정론적 (컴파일러 제어) |
| 데이터 이동 | 캐시 계층 (L1/L2/HBM) | 명시적 데이터 이동 |
| 강점 | 프리필, 대규모 배치, 학습 | 순차 토큰 생성, 저지연 |
| 제조 공정 | - | Samsung 4nm |

### 추론 파이프라인 분업 (Disaggregated Serving)

```mermaid
flowchart LR
    A[입력 프롬프트] --> B[Rubin GPU<br/>프리필 단계<br/>긴 입력 컨텍스트 처리]
    B --> C[KV Cache 전달]
    C --> D[Groq 3 LPU<br/>디코드 단계<br/>저지연 토큰 생성]
    D --> E[토큰 출력 스트림]
    
    style B fill:#76b900,color:#fff
    style D fill:#0071c5,color:#fff
```

프리필 단계는 연산 집약적(compute-bound)이어서 높은 병렬성의 GPU에 적합하고, 디코드 단계는 메모리 대역폭 의존(memory-bound)이어서 SRAM의 초고대역폭이 결정적 우위를 제공한다. 이 분리 서빙(Disaggregated Serving) 패턴은 에이전틱 AI에서 빈번한 짧은 추론 호출을 최적화하는 데 핵심적이다.

### NVIDIA의 200억 달러 투자 구조

NVIDIA의 200억 달러는 단순 인수 비용이 아니라 R&D, Samsung 4nm 제조 라인 구축, 생산 커밋먼트를 포함한 전체 기술 방향에 대한 투자다. 이는 NVIDIA가 추론 워크로드에서 GPU만으로는 최적 효율을 달성할 수 없다는 판단을 반영한다. Vera Rubin 로드맵에서 Rubin CPX(CPU-GPU 통합 칩)가 퇴출되고 LPU가 그 자리를 차지한 것은 이 전략적 전환의 구체적 증거다.

### 출하 일정
- **공개**: GTC 2026 (2026년 3월, 산호세)
- **제조**: Samsung 4nm 공정
- **출하**: 2026년 Q3 예정
- **Vera Rubin 플랫폼 칩 7종 중 하나**: Rubin GPU, Vera CPU, Groq 3 LPU 등 7개 칩이 동시 양산 중

## 관련 문서

- [[nvidia-vera-rubin]] -- Groq 3 LPU가 통합되는 상위 플랫폼
- [[disaggregated-serving]] -- 프리필/디코드 분리 서빙 아키텍처
- [[nvidia-dynamo]] -- NVIDIA 추론 OS
- [[google-tpu-ironwood]] -- 경쟁 추론 하드웨어
- [Tom's Hardware: NVIDIA $20B Groq Deal](https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip)
- [NVIDIA Technical Blog: Groq 3 LPX](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)
