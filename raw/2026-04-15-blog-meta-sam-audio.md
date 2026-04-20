---
source: blog
title: "SAM Audio: The First Unified Multimodal Model for Audio Separation"
publisher: Meta AI
date: 2025-12-16
url: "https://ai.meta.com/blog/sam-audio/"
fetched: 2026-04-15
status: pending_ingest
---

## Summary

Meta의 SAM Audio는 텍스트/비주얼/시간 프롬프트로 복잡한 오디오 혼합물에서 특정 소리를 분리하는 최초의 통합 멀티모달 오디오 분리 모델이다. Flow-matching diffusion transformer 아키텍처 사용.

## Key Points

- 텍스트("dog barking"), 비디오 클릭, 시간 범위 마커 등 멀티모달 프롬프트 지원
- 음성/음악/일반 소리 분리에서 SOTA, 실시간 효율(RTF ~0.7)
- Perception Encoder Audiovisual (PE-AV): 비디오-오디오 시간 동기화
- SAM Audio Judge(참조 없는 평가 모델) + SAM Audio-Bench(최초 실환경 벤치마크) 공개
- Flow-matching diffusion transformer 프레임워크로 타겟+잔차 오디오 동시 생성
