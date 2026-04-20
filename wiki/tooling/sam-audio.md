---
title: SAM Audio (Meta 통합 오디오 분리 모델)
category: tooling
page_type: entity
project: SAM Audio
tags: [meta, audio-separation, multimodal, flow-matching, diffusion-transformer]
sources: [raw/2026-04-15-blog-meta-sam-audio.md]
created: 2026-04-15
updated: 2026-04-15
---

# SAM Audio (Meta 통합 오디오 분리 모델)

## 개요

**SAM Audio(Segment Anything Model for Audio)**는 Meta가 개발한 최초의 **통합 멀티모달 오디오 분리(universal audio source separation)** 모델이다. 이미지 분할 분야의 SAM에서 영감을 받아, 오디오 혼합물(audio mixture)에서 특정 소리를 자유로운 형태의 프롬프트(텍스트, 비주얼, 시간 구간)로 지정하여 분리하는 것을 목표로 한다.

기존 오디오 분리 모델들이 특정 도메인(음악, 음성, 환경음)에 특화된 반면, SAM Audio는 단일 모델로 모든 유형의 소리를 다룬다. 실시간(RTF, Real-Time Factor) 처리 성능도 **~0.7**로 실용적인 수준을 달성하며 SOTA 성능을 기록했다.

## 시스템 아키텍처

```mermaid
flowchart LR
    MIX[오디오 혼합물\nAudio Mix] --> ENC

    subgraph 프롬프트
        P1[텍스트 프롬프트\n"바이올린 소리만"]
        P2[비주얼 프롬프트\n영상 프레임]
        P3[시간 프롬프트\n시작~끝 타임스탬프]
    end

    P1 --> ENC[멀티모달 인코더\nPE-AV 포함]
    P2 --> ENC
    P3 --> ENC

    ENC --> DIT[Flow-Matching\nDiffusion Transformer]
    DIT --> OUT1[목표 오디오\nTarget Audio]
    DIT --> OUT2[잔여 오디오\nResidual Audio]
```

이 파이프라인에서 잔여 오디오(residual audio)는 원본 혼합물에서 목표 소리를 제거한 나머지를 의미한다. 분리 품질 검증 및 후처리에 활용된다.

## 핵심 기술 구성 요소

### 1. PE-AV (Positional Encoding for Audio-Visual)

PE-AV는 SAM Audio의 핵심 혁신 중 하나로, **비디오 프레임과 오디오 신호를 시간 축에서 동기화**하는 메커니즘이다.

- 영상에 등장하는 악기나 소리 발생원을 시각적으로 추적
- 해당 시각 정보를 오디오 분리의 가이드 신호로 활용
- 입술 움직임(lip sync), 악기 연주 동작 등 비주얼-오디오 상관관계 학습

### 2. Flow-Matching Diffusion Transformer

생성 모델의 핵심 백본으로 **플로우 매칭(flow-matching)** 기반의 디퓨전 트랜스포머(diffusion transformer)를 사용한다.

- 디퓨전 모델의 고품질 생성 능력 + 플로우 매칭의 빠른 샘플링 효율을 결합
- 오디오 스펙트로그램(spectrogram) 도메인에서 작동
- 확률적 생성 과정을 통해 마스킹 기반 방법보다 자연스러운 분리 결과 산출

### 3. SAM Audio Judge (참조 없는 평가 시스템)

기존 오디오 분리 평가는 정답 레퍼런스 오디오(reference audio)가 필요했다. SAM Audio Judge는 **레퍼런스 없이(reference-free)** 분리 품질을 평가하는 자동 판별 모델이다.

- 분리된 오디오의 아티팩트(artifact), 누락 성분, 혼선(bleed) 등을 탐지
- 인간 청취자의 선호도와 높은 상관관계
- 실환경 배포에서 품질 모니터링에 활용 가능

### 4. SAM Audio-Bench (실환경 벤치마크)

기존 오디오 분리 벤치마크는 인위적으로 합성된 혼합물을 사용한다. SAM Audio-Bench는 **실제 녹음 환경에서 수집한 복잡한 혼합물**로 구성된다.

- 다수의 소음원이 자연스럽게 겹치는 현실적 시나리오
- 다양한 녹음 환경(스튜디오, 야외, 공연장)
- 프롬프트 유형별(텍스트/비주얼/시간) 서브셋 포함

## 성능 지표

| 지표 | SAM Audio | 기존 SOTA |
|------|-----------|-----------|
| 분리 품질 (SI-SNRi) | SOTA | - |
| 실시간 처리 비율 (RTF) | ~0.7 | >1.0 (일부 모델) |
| 지원 프롬프트 유형 | 3종 (텍스트/비주얼/시간) | 단일 유형 |
| 대상 도메인 | 범용 | 특화 도메인 |

RTF < 1.0은 처리 속도가 실시간보다 빠름을 의미한다.

## 한계 및 미지원 기능

- **오디오 프롬프트(audio prompt) 미지원**: 레퍼런스 오디오 샘플을 프롬프트로 사용하는 기능은 현재 버전에 포함되지 않음
- **유사 소스 분리의 한계**: 같은 악기 두 대가 함께 연주되는 경우처럼 음향적으로 유사한 소리 간 분리 품질이 저하됨
- **오디오 생성과의 혼동**: SAM Audio는 분리(separation) 모델이지, 오디오 생성(generation) 모델이 아님

## 실무 활용 시나리오

- **포스트 프로덕션**: 영화/방송 편집에서 특정 배우 음성만 추출
- **음악 제작**: 믹스된 음원에서 특정 악기 트랙 분리
- **접근성 보조**: 다중 화자 환경에서 특정 화자만 선택적으로 청취
- **콘텐츠 분석**: 비디오에서 배경음과 음성을 분리하여 각각 처리

## 관련 문서

- [[multimodal-foundation-models]] - 멀티모달 파운데이션 모델의 아키텍처와 학습 방법
- [[mechanistic-interpretability-2026]] - 생성 모델 내부 표현 해석
