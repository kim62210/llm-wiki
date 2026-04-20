---
title: Whisper (OpenAI 음성 인식)
category: tooling
page_type: entity
project: Whisper
tags: [whisper, asr, speech-recognition, openai, multilingual, transcription]
sources: [raw/2026-04-17-topic-queue-v2.md]
created: 2026-04-17
updated: 2026-04-17
---

# Whisper

Radford et al. (2022)이 공개한 OpenAI의 범용 음성 인식(ASR) 모델. 680,000시간의 다국어 웹 오디오로 학습된 인코더-디코더 Transformer로, 99개 언어의 음성을 텍스트로 변환한다.

## 아키텍처

```mermaid
flowchart LR
    Audio[오디오 30초] --> MelSpec[로그 멜 스펙트로그램<br/>80채널]
    MelSpec --> Encoder[Transformer 인코더]
    Encoder --> Decoder[Transformer 디코더<br/>자기회귀 텍스트 생성]
    Decoder --> Text[텍스트 + 타임스탬프]
```

## 모델 크기

| 모델 | 파라미터 | 영어 WER | 다국어 |
|------|---------|---------|--------|
| tiny | 39M | 7.6% | 제한적 |
| base | 74M | 5.0% | 양호 |
| small | 244M | 3.4% | 좋음 |
| medium | 769M | 2.9% | 매우 좋음 |
| **large-v3** | **1.5B** | **2.0%** | **최고** |

## 멀티태스크 학습

단일 모델이 음성 인식, 번역, 언어 감지, 타임스탬프를 모두 수행. 특수 토큰(`<|transcribe|>`, `<|translate|>`, `<|ko|>`)으로 태스크를 지정한다.

## 실전 활용

- **[[audio-rag|오디오 RAG]]**: 팟캐스트/회의록 전사 + 인덱싱
- **실시간 자막**: Whisper.cpp로 저지연 온디바이스 실행
- **faster-whisper**: CTranslate2 기반 4x 가속 구현

## 관련 문서

- [[audio-rag]] -- 오디오 RAG
- [[video-rag]] -- 비디오 RAG (ASR 컴포넌트)
- [[voxcpm2]] -- VoxCPM2 (TTS, Whisper의 역방향)
