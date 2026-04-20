---
title: Perplexity
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, metrics, language-model, perplexity]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# Perplexity

언어 모델의 가장 기본적인 내재 평가 지표다. 모델이 테스트 데이터의 다음 토큰을 얼마나 "확신" 있게 예측하는지를 수치화하며, 1977년 Frederick Jelinek 등이 음성 인식 맥락에서 처음 도입한 이후 반세기 가까이 언어 모델 연구의 표준 척도로 자리잡았다.

## 수학적 정의

Perplexity는 모델이 시퀀스에 부여하는 확률의 역수를 토큰 수로 정규화한 값이다. 구체적으로는 교차 엔트로피의 지수로 정의한다.

```
PPL(D) = exp( -1/N * sum_{i=1}^{N} log p(x_i | x_{<i}) )
```

여기서 N은 테스트 시퀀스의 토큰 수, p(x_i | x_{<i})는 모델이 i번째 토큰에 부여하는 조건부 확률이다. 정보 이론적으로 해석하면, perplexity는 각 위치에서 모델이 동등하게 확률을 배분한 "가상의 선택지 수"에 해당한다.

## 해석 방법

- 값이 낮을수록 모델의 예측 성능이 좋다
- Perplexity 1은 모델이 모든 토큰을 완벽하게 예측한다는 의미
- Perplexity가 어휘 크기(vocabulary size)와 같다면, 모든 토큰에 균등 확률을 부여하는 것과 동등 -- 사실상 무작위 추측
- 예를 들어, perplexity 20은 모델이 매 토큰마다 20개 중 하나를 고르는 것과 같은 수준의 불확실성을 가진다는 의미다

## 장점

Perplexity가 반세기 넘게 쓰이는 데는 이유가 있다.

- **해석 가능성**: "평균 분기 계수(branching factor)"라는 직관적 해석이 존재한다
- **모델 무관성**: 확률을 출력하는 모든 언어 모델에 적용 가능하다 -- n-gram, RNN, Transformer 모두 해당
- **인간 주석 불필요**: BLEU나 ROUGE와 달리 참조 텍스트가 필요 없다
- **계산 효율**: 테스트 셋에 대한 forward pass 한 번으로 산출 가능하다
- **학습 곡선 모니터링**: 사전학습 중 loss curve와 직접 연결되므로 학습 진행 상황을 실시간으로 추적할 수 있다

## 한계와 주의사항

perplexity가 낮다고 반드시 "좋은" 모델은 아니다.

**어휘 의존성**: 서로 다른 토크나이저를 사용하는 모델 간에는 perplexity를 직접 비교할 수 없다. BPE로 30,000개 어휘를 쓰는 모델과 SentencePiece로 50,000개 어휘를 쓰는 모델의 perplexity는 비교 기준 자체가 다르다.

**인간 판단과의 괴리**: perplexity는 주로 구문적 일관성(syntactic coherence)을 측정한다. 의미 이해, 사실 정확성, 복잡한 추론 능력은 직접 측정하지 못한다. GPT-4와 GPT-3.5의 perplexity 차이보다 실제 사용자 경험 차이가 훨씬 크다.

**도메인 민감성**: 의료 논문에서 학습한 모델의 perplexity를 소셜 미디어 텍스트로 평가하면 인위적으로 높은 값이 나온다. 평가 도메인과 학습 도메인의 분포 차이를 반영하기 때문이다.

**생성 품질 미반영**: 낮은 perplexity가 창의적이거나 유용한 응답을 보장하지 않는다. instruction-following 능력이나 대화 품질은 별도 평가가 필요하며, 이를 위해 [[mt-bench]]나 인간 평가 프로토콜 같은 보완 지표가 등장했다.

## 실무 활용 패턴

**사전학습 모니터링**: 대규모 언어 모델 학습 중 validation perplexity를 주기적으로 측정하여 학습 진행 상황을 추적한다. Chinchilla scaling laws 연구에서도 perplexity를 핵심 지표로 사용했다.

**모델 선택 1차 필터**: 동일 토크나이저를 공유하는 모델 패밀리(같은 base 모델의 서로 다른 체크포인트) 내에서 빠르게 비교할 때 유용하다.

**데이터 품질 평가**: 학습 데이터의 특정 도메인 서브셋에 대한 perplexity를 측정하여 데이터 품질이나 도메인 커버리지를 간접 평가할 수 있다.

**이상 탐지**: 특정 입력에 대한 perplexity가 비정상적으로 높다면 out-of-distribution 입력이거나 adversarial 입력일 가능성이 있다.

## 사전학습 vs 후속 평가에서의 역할

사전학습 단계에서 perplexity는 사실상 유일한 내재 평가 지표다. 하지만 SFT(supervised fine-tuning)나 RLHF 단계를 거친 모델은 perplexity만으로 평가하기 어렵다. 이 단계에서는 [[classification-metrics]]나 [[humaneval]], [[mmlu]] 같은 태스크 특화 벤치마크가 더 적합하다.

현대 LLM 평가 파이프라인에서 perplexity는 "1차 스크리닝" 역할을 하고, 최종 판단은 다운스트림 벤치마크와 인간 평가([[human-evaluation-protocols]])로 이루어진다. [[evaluation-harness]] 같은 통합 프레임워크는 perplexity와 태스크 벤치마크를 함께 실행할 수 있는 환경을 제공한다.

## 스케일링 법칙과 Perplexity

Kaplan et al. (2020)과 Hoffmann et al. (2022, Chinchilla)의 neural scaling laws 연구에서 perplexity는 핵심 종속 변수였다. 이 연구들은 모델 크기, 데이터 양, 컴퓨팅 예산과 perplexity 사이의 멱법칙(power law) 관계를 밝혀, 최적 학습 배분 전략을 수립하는 근거를 제공했다. perplexity가 모델 규모에 따라 예측 가능하게 감소한다는 발견은 LLM 학습 계획 수립에 직접 활용된다. 이 관계는 log-log 스케일에서 선형에 가까우며, 특정 perplexity 목표를 달성하기 위해 필요한 자원을 사전에 추정할 수 있게 해준다.

## Bits-per-character/byte와의 관계

perplexity 대신 bits-per-character(BPC) 또는 bits-per-byte(BPB)를 사용하는 경우도 있다. BPC = log2(PPL)로 변환되며, 토크나이저 의존성을 일부 해소할 수 있어서 서로 다른 아키텍처 간 비교에 활용된다. 하지만 문자/바이트 단위 분해가 모든 언어에서 자연스럽지는 않다는 한계가 남는다.

## 관련 문서

- [[bleu]] -- n-gram 기반 정밀도 메트릭
- [[rouge]] -- n-gram 기반 재현율 메트릭
- [[bertscore]] -- 의미적 유사도 기반 대안
- [[classification-metrics]] -- 분류 태스크 평가 지표
- [[evaluation-harness]] -- perplexity 측정을 포함하는 통합 평가 프레임워크
- [[benchmark-saturation-goodharts-law]] -- 단일 지표 최적화의 위험
- [[deepeval]] -- LLM 평가 프레임워크
