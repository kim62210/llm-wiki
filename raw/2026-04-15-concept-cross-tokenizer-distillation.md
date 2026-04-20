---
source: arxiv
title: "Cross-Tokenizer Distillation via Byte-Level Interface"
arxiv_id: "2604.07466"
url: "https://arxiv.org/abs/2604.07466"
date: 2026-04-10
fetched: 2026-04-15
status: pending_ingest
---

## Overview

서로 다른 토크나이저를 사용하는 교사-학생 모델 간 지식 증류를 가능하게 하는 방법. 바이트 레벨을 공통 인터페이스로 사용하여 토크나이저 차이를 극복.

## Problem

- 지식 증류는 보통 동일 토크나이저 가정
- 실제로는 교사(GPT-4)와 학생(Llama) 모델이 다른 토크나이저 사용
- 토큰 레벨 확률 분포를 직접 비교할 수 없음

## Byte-Level Distillation (BLD)

1. 교사의 출력 분포를 바이트 레벨 확률로 변환
2. 학생 모델에 경량 바이트 레벨 디코더 헤드 추가
3. 바이트 레벨에서 교사-학생 분포를 매칭
4. 토크나이저에 무관하게 밀집(dense) 피드백 전달

## Related Developments

- Byte Latent Transformer (BLT): 아예 토크나이저 없이 바이트에서 학습
- BoundlessBPE: 단어 경계 제약 해제, bytes/token 15% 개선
- Universal Tokenizer: 사전학습 후 언어 확장을 위한 범용 토크나이저

## Implications

- 이기종 모델 간 증류 경로 개방
- 다국어 모델에서 특히 유용: 언어별 토크나이저 효율성 편차 극복
- 향후 토크나이저 없는 아키텍처로의 전환 촉진
