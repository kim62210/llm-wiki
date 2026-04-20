# VoxCPM2 GitHub README

Source: https://github.com/OpenBMB/VoxCPM
Fetched: 2026-04-16

## Overview

VoxCPM2 is a 2B parameter tokenizer-free text-to-speech system from OpenBMB. Uses "diffusion autoregressive architecture" generating continuous speech representations without discrete tokenization.

## Capabilities

- **Voice Design**: Create new voices from natural language descriptions (gender, age, tone, emotion, pace) without reference audio
- **Controllable Voice Cloning**: Clone from short clips with style guidance for emotion, pace, expression
- **Ultimate Cloning**: Highest fidelity with reference audio + transcript
- **Multilingual**: 30 languages with automatic prosody inference

## 30 Supported Languages

Arabic, Burmese, Chinese (standard + 9 dialects including Cantonese/Sichuanese), Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Khmer, Korean, Lao, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swahili, Swedish, Tagalog, Thai, Turkish, Vietnamese.

## Architecture

Four-stage pipeline: **LocEnc -> TSLM -> RALM -> LocDiT**, operating in AudioVAE V2 latent space. Native 48kHz output with built-in super-resolution.

## Benchmarks

- Seed-TTS-eval: 1.84% WER, 75.3% similarity (English)
- 30-language ASR: average 1.68% error rate
- InstructTTSEval voice design: 85.2% Chinese, 84.2% English

## Model Variants

- **VoxCPM2** (Latest): 2B params, 30 langs, 48kHz, ~0.30 RTF on RTX 4090
- **VoxCPM1.5** (Stable): 0.6B params, 2 langs, 44.1kHz, ~0.15 RTF
- **VoxCPM-0.5B** (Legacy): 0.5B params, 2 langs, 16kHz, ~0.17 RTF

## Production

Nano-vLLM-VoxCPM for high-throughput serving: RTF ~0.13, concurrent requests, async API.

## Fine-tuning

Full fine-tuning and LoRA supported. 5-10 minutes of audio for adaptation.

## License

Apache-2.0
