---
title: 연합 학습 (Federated Learning)
category: training
page_type: concept
tags: [federated-learning, privacy-preserving, distributed-learning, differential-privacy, aggregation]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---

# 연합 학습 (Federated Learning)

## 개요

연합 학습(Federated Learning, FL)은 다수의 분산된 클라이언트(기기 또는 조직)가 원본 데이터를 중앙 서버에 전송하지 않고, 로컬에서 학습한 모델 업데이트만 공유하여 글로벌 모델을 협력적으로 학습하는 분산 기계학습 패러다임이다. Google이 2017년에 "Communication-Efficient Learning of Deep Networks from Decentralized Data" 논문으로 공식화한 이후, 개인정보 보호와 데이터 규제가 강화되는 환경에서 핵심적인 학습 기법으로 자리잡았다.

## 핵심 구조

### 학습 사이클

연합 학습의 기본 사이클은 다음과 같다:

1. **모델 배포**: 중앙 서버가 글로벌 모델의 현재 파라미터를 참여 클라이언트에 배포
2. **로컬 학습**: 각 클라이언트가 자신의 로컬 데이터로 모델을 학습 (수 에폭)
3. **업데이트 전송**: 클라이언트가 학습된 모델 업데이트(그래디언트 또는 가중치 차이)를 서버에 전송
4. **글로벌 집약**: 서버가 모든 클라이언트의 업데이트를 집약하여 글로벌 모델 갱신
5. **반복**: 수렴 조건이 충족될 때까지 1-4단계 반복

### FedAvg 알고리즘

가장 기본적인 집약 전략인 FedAvg(Federated Averaging)는 각 클라이언트의 로컬 모델 가중치를 데이터 크기에 비례하여 가중 평균한다:

```
w_global = SUM(n_k / n) * w_k  (k = 1, ..., K)
```

여기서 n_k는 클라이언트 k의 데이터 수, n은 전체 데이터 수, w_k는 클라이언트 k의 로컬 모델 가중치다. 단순하지만 IID(독립 동일 분포) 데이터에서는 놀라울 만큼 효과적이다.

### 연합 학습의 유형

| 유형 | 데이터 분할 | 참여자 | 대표 사례 |
|------|-----------|--------|----------|
| **수평 FL** | 동일 특성, 다른 샘플 | 다수의 동종 기기 | 모바일 키보드 예측 |
| **수직 FL** | 동일 샘플, 다른 특성 | 소수의 이종 기관 | 은행 + 보험사 공동 모델링 |
| **연합 전이 학습** | 다른 샘플, 다른 특성 | 이질적 도메인 | 도메인 간 협력 학습 |

## 프라이버시 보호 메커니즘

원본 데이터를 공유하지 않는 것만으로는 충분하지 않다. 모델 업데이트(그래디언트)로부터 원본 데이터를 역추론하는 **그래디언트 역전 공격(gradient inversion attack)**이 가능하기 때문이다.

### 차등 프라이버시 (Differential Privacy)

모델 업데이트에 보정된 노이즈를 추가하여, 개별 데이터 포인트의 존재 여부를 통계적으로 구분할 수 없게 만든다. 프라이버시 예산 epsilon이 작을수록 강한 보호를 제공하지만, 모델 유틸리티와 트레이드오프 관계에 있다.

### 안전한 집약 (Secure Aggregation)

동형 암호화(Homomorphic Encryption)나 안전 다자간 연산(Secure Multi-Party Computation)을 사용하여, 서버가 개별 클라이언트의 업데이트를 볼 수 없이 집약된 결과만 얻도록 한다. 서버 자체가 타협되더라도 개별 업데이트가 노출되지 않는다.

### 보호 기법 비교

| 기법 | 보호 대상 | 오버헤드 | 유틸리티 영향 |
|------|----------|---------|-------------|
| **차등 프라이버시** | 개별 데이터 포인트 | 낮음 | 노이즈로 인한 정확도 하락 |
| **안전한 집약** | 개별 클라이언트 업데이트 | 높은 통신/연산 비용 | 없음 (정확한 집약) |
| **동형 암호화** | 서버에서의 데이터 노출 | 매우 높음 | 없음 |

## 핵심 과제

### Non-IID 데이터 문제

현실 세계에서 각 클라이언트의 데이터 분포는 크게 다르다(non-IID). 예를 들어 모바일 키보드 예측에서 각 사용자의 언어 패턴, 어휘, 주제가 모두 다르다. Non-IID 환경에서 FedAvg의 수렴 속도가 크게 저하되고, 글로벌 모델이 특정 클라이언트 분포에 편향될 수 있다.

**완화 전략**:
- **FedProx**: 로컬 업데이트와 글로벌 모델 간 거리에 페널티 부여
- **SCAFFOLD**: 클라이언트별 제어 변수로 그래디언트 드리프트 보정
- **개인화 FL**: 글로벌 모델 + 로컬 적응 레이어 분리

### 통신 효율성

모델 파라미터의 반복적 전송은 대역폭 병목을 야기한다. 특히 LLM 규모의 모델에서는 한 라운드의 통신량이 수 GB에 달할 수 있다.

- **그래디언트 압축**: 중요한 그래디언트만 선택적 전송 (top-k sparsification)
- **양자화 통신**: 업데이트를 저정밀도로 양자화하여 전송 ([[ai-inference-quantization-2026|양자화]] 기법 적용)
- **로컬 학습 확대**: 통신 라운드 수를 줄이고 로컬 에폭을 늘림 (수렴 품질과 트레이드오프)

### 시스템 이질성

클라이언트 간 연산 능력, 네트워크 속도, 가용 시간이 다르다. 느린 클라이언트(straggler)가 전체 학습을 지연시키는 문제가 있으며, 비동기 집약이나 부분 참여(partial participation) 전략으로 대응한다.

## 적용 분야

| 분야 | 활용 | 데이터 민감도 |
|------|------|-------------|
| **헬스케어** | 병원 간 질병 예측 모델 공동 학습 | 환자 의료 기록 (HIPAA) |
| **금융** | 사기 탐지 모델의 은행 간 협력 학습 | 거래 내역 (금융 규제) |
| **모바일** | 키보드 예측, 음성 인식 개선 | 사용자 입력 데이터 |
| **자율주행** | 주행 데이터의 분산 학습 | 위치/영상 데이터 (GDPR) |
| **제조** | 공장 간 품질 예측 모델 공유 | 생산 공정 데이터 (영업 비밀) |

## LLM과 연합 학습

LLM의 연합 학습은 모델 크기로 인해 독특한 도전을 제시한다. 전체 모델 파라미터를 매 라운드 전송하는 것은 비현실적이므로, [[lora-qlora-finetuning|LoRA]] 어댑터만 연합 학습하는 **FedLoRA** 패턴이 주목받고 있다. 각 클라이언트가 저랭크 어댑터만 로컬 학습하고, 서버에서 어댑터 가중치를 집약하는 방식으로 통신 비용을 수십 배 줄일 수 있다.

## 관련 문서

- [[lora-qlora-finetuning]] -- FedLoRA의 기반이 되는 파라미터 효율적 학습
- [[data-parallelism-fsdp]] -- 분산 학습의 또 다른 패러다임
- [[distributed-communication]] -- 분산 학습의 통신 프로토콜
- [[ai-inference-quantization-2026]] -- 통신 효율화를 위한 양자화 기법
- [[knowledge-distillation]] -- 연합 증류(Federated Distillation) 기법과의 접점

## 참고 자료

- [Federated Learning: A Survey on Privacy-Preserving Collaborative Intelligence (arXiv 2025)](https://arxiv.org/html/2504.17703v3)
- [Privacy preservation in federated learning: An insightful survey from the GDPR perspective (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0167404821002261)
- [Exploring privacy mechanisms and metrics in federated learning (Springer 2025)](https://link.springer.com/article/10.1007/s10462-025-11170-5)
