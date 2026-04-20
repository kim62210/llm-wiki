---
title: VoxCPM2 (Tokenizer-Free TTS)
category: tooling
page_type: entity
project: VoxCPM2
tags: [voxcpm2, tts, text-to-speech, openbmb, tokenizer-free, diffusion, voice-cloning, multilingual]
sources: [raw/2026-04-14-wiki-expand-scan.md, raw/2026-04-16-voxcpm2-github-readme.md]
created: 2026-04-14
updated: 2026-04-16
---

# VoxCPM2

OpenBMB가 개발한 토크나이저 프리(tokenizer-free) 텍스트-투-스피치(TTS) 모델. 음성을 이산 토큰으로 변환하는 기존 TTS 접근과 달리, AudioVAE V2의 연속 잠재 공간(latent space)에서 직접 작동하는 확산 자기회귀(diffusion autoregressive) 패러다임을 채택했다. 2B 파라미터 규모, 200만 시간 이상의 다국어 음성 데이터로 학습되었으며, 30개 언어를 지원한다. Apache 2.0 라이선스.

## 개요

전통적 TTS 시스템은 음성 파형을 이산 토큰(discrete token)으로 변환한 뒤 언어 모델로 토큰 시퀀스를 생성하고, 이를 다시 파형으로 디코딩하는 파이프라인을 따른다. 이 과정에서 토크나이저가 음성의 미세한 뉘앙스(음색, 감정, 리듬)를 양자화 손실로 소거하는 문제가 있다. VoxCPM2는 이 토크나이저 단계를 완전히 제거하고, 연속적인 잠재 표현 공간에서 직접 음성을 생성함으로써 48kHz 스튜디오 품질의 자연스러운 합성을 달성한다.

## 아키텍처

VoxCPM2의 핵심 파이프라인은 네 단계로 구성된다:

```
텍스트 --> LocEnc --> TSLM --> RALM --> LocDiT --> 48kHz 오디오
```

| 단계 | 모듈 | 역할 |
|------|------|------|
| 1 | LocEnc (Local Encoder) | 입력 텍스트를 로컬 언어 표현으로 인코딩 |
| 2 | TSLM (Text-Speech Language Model) | 텍스트-음성 정렬 및 잠재 표현 생성 |
| 3 | RALM (Residual Autoregressive LM) | 잔차 자기회귀 모델로 세밀한 음성 특성 보강 |
| 4 | LocDiT (Local Diffusion Transformer) | 확산 트랜스포머로 최종 고품질 오디오 생성 |

### AudioVAE V2

AudioVAE V2는 비대칭 인코드/디코드 설계를 사용한다. 참조 오디오를 16kHz로 입력받아 내부 잠재 공간에서 처리한 뒤, 내장 초해상도(super-resolution)를 통해 48kHz 네이티브 오디오를 출력한다. LM 토큰 레이트는 6.25Hz로, 기존 토큰 기반 TTS 대비 시퀀스 길이를 대폭 줄여 효율적인 생성을 가능하게 한다.

### 토크나이저 프리 접근의 이점

- **양자화 손실 제거**: 이산 토큰으로 변환하지 않으므로 음성의 미세한 뉘앙스가 보존됨
- **엔드-투-엔드 확산**: 잠재 공간에서의 확산 과정이 풍부한 표현력을 제공
- **통합 파이프라인**: 별도의 보코더(vocoder) 없이 단일 모델에서 고품질 오디오 직접 출력

## 핵심 기능

### 다국어 음성 합성

30개 언어를 지원하며, 언어 태그 없이 입력 텍스트만으로 자동 언어 감지 및 합성이 가능하다.

**지원 언어**: 아랍어, 미얀마어, 중국어, 덴마크어, 네덜란드어, 영어, 핀란드어, 프랑스어, 독일어, 그리스어, 히브리어, 힌디어, 인도네시아어, 이탈리아어, 일본어, 크메르어, 한국어, 라오어, 말레이어, 노르웨이어, 폴란드어, 포르투갈어, 러시아어, 스페인어, 스와힐리어, 스웨덴어, 타갈로그어, 태국어, 터키어, 베트남어

중국어 방언도 별도 지원한다: 사천, 광동, 우(Wu), 동북, 허난, 산시, 산동, 텐진, 민남 방언.

### 음성 디자인 (Voice Design)

참조 오디오 없이 자연어 설명만으로 새로운 음성을 생성할 수 있다. 성별, 나이, 톤, 감정, 속도 등을 텍스트로 지정하면 해당 특성을 가진 음성이 합성된다.

### 음성 클로닝 (Voice Cloning)

짧은 참조 오디오 클립에서 음색(timbre)을 복제하며, 선택적으로 스타일 가이던스를 통해 감정, 속도, 표현을 조절할 수 있다. 궁극적 클로닝(Ultimate Cloning) 모드에서는 참조 오디오와 트랜스크립트를 함께 제공하여 음색, 리듬, 감정, 스타일의 모든 뉘앙스를 재현하는 오디오 연속 기반 합성을 수행한다.

## 벤치마크 성능

Seed-TTS-eval 벤치마크에서의 결과:

| 테스트셋 | 오류율 | 유사도 |
|---------|--------|--------|
| test-EN | WER 1.84% | 75.3% |
| test-ZH | CER 0.97% | 79.5% |
| test-Hard | WER 8.13% | 75.3% |

제로샷 및 제어 가능한 TTS 벤치마크에서 SOTA 또는 동등한 수준의 결과를 달성했다.

## 추론 성능

| 환경 | RTF (Real-Time Factor) |
|------|----------------------|
| RTX 4090 (기본) | ~0.30 |
| RTX 4090 + Nano-vLLM 가속 | ~0.13 |

VRAM 요구량은 약 8GB로, 소비자용 GPU에서도 실행 가능하다.

## 기존 TTS와의 비교

| 항목 | 토큰 기반 TTS | VoxCPM2 (토크나이저 프리) |
|------|-------------|------------------------|
| 음성 표현 | 이산 토큰 (코드북 인덱스) | 연속 잠재 벡터 |
| 양자화 손실 | 존재 (음색/감정 뉘앙스 소실) | 없음 (연속 공간 직접 작동) |
| 보코더 | 별도 필요 (HiFi-GAN 등) | 불필요 (LocDiT에서 직접 생성) |
| 출력 품질 | 16-24kHz 일반적 | 48kHz 네이티브 |
| 시퀀스 길이 | 긴 토큰 시퀀스 | 6.25Hz로 압축 |

토큰 기반 접근은 음성을 수백-수천 개의 이산 코드로 표현하므로, 코드북에 없는 미세한 음성 변화를 포착하지 못한다. VoxCPM2의 연속 잠재 공간 접근은 이 한계를 근본적으로 해소하여, 특히 감정 표현과 자연스러운 억양 재현에서 우위를 보인다.

## 실무적 의의

VoxCPM2는 TTS 분야에서 토크나이저 프리 패러다임의 실용성을 입증한 중요한 사례다. 8GB VRAM으로 실행 가능한 접근성, 30개 언어 지원의 범용성, 그리고 LoRA 파인튜닝으로 5-10분 분량의 데이터만으로 도메인 적응이 가능한 효율성을 동시에 갖추고 있다. Apache 2.0 라이선스로 상업적 사용이 자유로워, 프로덕션 TTS 시스템 구축의 베이스 모델로 활용할 수 있다.

## 파인튜닝

VoxCPM2는 SFT(Supervised Fine-Tuning)와 [[lora-qlora-finetuning|LoRA]] 파인튜닝을 모두 지원한다. 5-10분 분량의 오디오 데이터만으로 특정 화자, 언어, 도메인에 적응시킬 수 있다. [[peft-library|PEFT]] 생태계와의 결합으로 효율적인 커스터마이징이 가능하다.

## 대표 자료

- [VoxCPM GitHub (OpenBMB)](https://github.com/OpenBMB/VoxCPM)
- [VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning (arXiv)](https://arxiv.org/abs/2509.24650)
- [VoxCPM2 모델 (Hugging Face)](https://huggingface.co/openbmb/VoxCPM2)

## 관련 페이지

- [[voxtral-tts|Voxtral TTS]] -- Mistral AI의 TTS 모델과의 비교
- [[huggingface-hub|Hugging Face Hub]] -- 모델 배포 플랫폼
- [[lora-qlora-finetuning|LoRA/QLoRA 파인튜닝]] -- VoxCPM2 파인튜닝에 활용
- [[peft-library|PEFT]] -- 파라미터 효율적 파인튜닝 라이브러리
