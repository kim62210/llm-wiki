---
title: LTX-2 (오픈소스 4K 비디오+오디오 생성 모델)
category: tooling
page_type: entity
project: LTX-2
tags: [ltx-2, lightricks, video-generation, audio-generation, open-source, diffusion-transformer]
sources: [raw/2026-04-14-gap-scan-new-topics.md]
created: 2026-04-14
updated: 2026-04-14
---

# LTX-2

Lightricks가 2026년 1월에 공개한 오픈소스 비디오+오디오 생성 모델이다. 총 19B 파라미터(14B 비디오 + 5B 오디오)로 구성되며, 오픈소스 모델 중 최초로 네이티브 4K@50fps 비디오와 동기화 오디오를 단일 모델에서 생성한다.

## 왜 지금 중요한가

2026년 상반기 AI 비디오 생성 시장은 [[runway-gen-4-5|Runway Gen-4.5]], Sora 2(종료)를 거치며 급변하고 있다. 이 와중에 LTX-2는 상용 모델에 버금가는 4K 해상도와 오디오 동기화를 Apache 2.0 라이선스로 완전 공개해, 오픈소스 비디오 생성의 실용 가능성을 처음으로 입증했다. 특히 라이선스된 학습 데이터(Getty Images, Shutterstock)를 사용해 저작권 리스크까지 해소한 점이 차별적이다.

## 핵심 사양

| 항목 | 내용 |
|------|------|
| 파라미터 | 총 19B (비디오 14B + 오디오 5B) |
| 최대 해상도 | 4K (3840x2160) |
| 프레임률 | 최대 50fps |
| 최대 길이 | 20초 |
| 아키텍처 | Diffusion Transformer |
| 오디오 | 네이티브 동기화 오디오 생성 |
| 라이선스 | Apache 2.0 |
| 상업 이용 | 연 매출 $10M 미만 무료 |
| 양자화 | NVIDIA NVFP8 지원 (크기 30% 감축, 속도 2배) |
| 공개 채널 | GitHub, Hugging Face |

## 아키텍처 개요

```mermaid
flowchart TD
    Input[텍스트/이미지 입력] --> VideoEnc[비디오 DiT 14B]
    Input --> AudioEnc[오디오 DiT 5B]
    VideoEnc --> Sync[동기화 모듈]
    AudioEnc --> Sync
    Sync --> Output[4K@50fps 비디오 + 동기화 오디오]
    
    subgraph 양자화
        NVFP8[NVFP8 양자화] --> Opt[크기 30% 감축<br>속도 2배 향상]
    end
```

LTX-2는 비디오와 오디오를 각각 독립된 [[diffusion-transformer|Diffusion Transformer]]로 처리한 뒤, 동기화 모듈에서 시간축 정렬을 수행하는 듀얼 파이프라인 구조를 취한다.

## 주요 특징

### 네이티브 오디오 동기화

기존 오픈소스 비디오 모델은 영상만 생성하고 오디오는 별도 모델로 후처리해야 했다. LTX-2는 단일 모델 내에서 비디오와 오디오를 동시 생성하며, 시간축 동기화를 보장한다. 이는 영화 예고편, 광고, 소셜 미디어 콘텐츠 등 실무 활용에서 후처리 파이프라인을 크게 단순화한다.

### 라이선스 안전성

Getty Images와 Shutterstock에서 라이선스를 확보한 학습 데이터를 사용한다. AI 생성 콘텐츠의 저작권 소송이 급증하는 2026년 상황에서, 학습 데이터 출처가 명확한 오픈소스 모델은 기업 도입의 법적 장벽을 낮춘다.

### NVFP8 양자화 최적화

NVIDIA의 NVFP8 양자화 기술을 적용해 모델 크기를 약 30% 줄이면서 추론 속도를 최대 2배 향상시켰다. 소비자급 GPU에서의 실행 가능성을 높여 접근성을 확대한다.

## 비교 맥락

| 모델 | 파라미터 | 최대 해상도 | 오디오 | 라이선스 |
|------|----------|------------|--------|---------|
| LTX-2 | 19B | 4K@50fps | 네이티브 동기화 | Apache 2.0 |
| HunyuanVideo | 13B | 1280x720 | 없음 | 오픈소스 |
| Wan 2.1 | MoE | HD | 없음 | 오픈소스 |
| Runway Gen-4.5 | 비공개 | 4K | 네이티브 | 상용 |

## 실무 관점

- 4K+오디오 동기화가 가능한 최초의 오픈소스 모델로, 상용 API 비용 없이 자체 인프라에서 영상 생성 파이프라인을 구축할 수 있다
- Apache 2.0 + 라이선스된 학습 데이터로 기업 법무팀의 승인 장벽이 낮다
- NVFP8 양자화로 [[dgx-spark]] 같은 개인용 AI 하드웨어에서도 실행 가능성이 열린다
- 20초 제한은 롱폼 콘텐츠에 부족하지만, 광고/숏폼/프로토타이핑 용도에는 충분하다

## 관련 문서

- [[dgx-spark]] - NVIDIA 개인용 AI 슈퍼컴퓨터
- [[blackwell-ultra-b300]] - NVIDIA GPU (NVFP8 양자화 지원)
- [[runway-gen-4-5]] - Runway의 상용 비디오 생성 모델 (비교 대상)
- [[nvidia-cosmos]] - NVIDIA의 오픈소스 비디오 생성 플랫폼
