---
title: 퍼플렉시티 (Perplexity)
category: training
page_type: concept
tags: [perplexity, evaluation, language-model, cross-entropy]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 퍼플렉시티 (Perplexity)

## 개념 요약

퍼플렉시티(PPL, Perplexity)는 언어 모델이 텍스트를 얼마나 잘 예측하는지 측정하는 **자동 평가 지표**다. 교차 엔트로피(cross-entropy) 손실의 지수 함수로 정의되며, 직관적으로는 "모델이 다음 토큰을 예측할 때 평균적으로 몇 가지 후보를 균등하게 고민하는가"를 나타낸다.

## 수식 정의

시퀀스 $W = (w_1, w_2, \ldots, w_N)$에 대해:

$$
\text{PPL}(W) = \exp\left(-\frac{1}{N}\sum_{i=1}^{N} \log P(w_i \mid w_1, \ldots, w_{i-1})\right)
$$

$$
= \exp\left(\mathcal{L}_{\text{cross-entropy}}\right)
$$

- PPL = 1: 완벽한 예측 (가능 어휘 1개만 남음)
- PPL = V (어휘 크기): 완전히 무작위 예측
- 실제 GPT 계열 모델: WikiText-103 기준 약 15-30 수준

## 직관: "다음 토큰 후보 수"

PPL이 10이라면, 모델이 매 토큰 예측 시 평균적으로 10개의 후보를 동등하게 고민한다고 해석할 수 있다. 값이 낮을수록 모델이 더 확신있게 예측한다.

## 슬라이딩 윈도우 PPL

컨텍스트 길이보다 긴 문서를 평가할 때, 문서를 고정 크기 청크로 자르면 청크 경계에서 컨텍스트 정보가 단절된다. **슬라이딩 윈도우(sliding window)** 방식은 매 스텝마다 전체 컨텍스트를 갱신해 이를 해소한다.

- stride $S$와 window 크기 $L$을 설정
- 각 윈도우에서 오직 stride 부분의 PPL만 집계
- 계산 비용이 증가하지만 더 정확한 평가 가능
- 특히 긴 컨텍스트 모델(32K+) 평가 시 권장

## 토크나이저 의존성 문제

PPL은 **토크나이저에 의존적**이어서 토크나이저가 다른 모델 간 직접 비교가 불가능하다.

- "hello world"를 `["hello", " world"]` (2 토큰) vs `["he", "llo", " wo", "rld"]` (4 토큰)로 처리하면 분모 N이 달라져 PPL이 달라짐
- 어휘 크기가 클수록 토큰당 더 많은 정보를 압축하므로 PPL 수치 자체가 낮게 나오는 경향

## BPB (Bits Per Byte) 변환으로 정규화

토크나이저 불일치를 해소하기 위해 **BPB(Bits Per Byte)** 로 변환한다.

$$
\text{BPB} = \frac{\log_2 \text{PPL}}{\text{평균 토큰당 바이트 수}}
$$

- 바이트 단위로 정규화하므로 토크나이저 독립적
- 서로 다른 어휘 크기의 모델을 공정하게 비교 가능
- 값이 낮을수록 우수 (완벽 압축: 영어 평균 약 1.0 bits/byte 수준)

## PPL과 벤치마크 성능의 상관/비상관

PPL과 downstream 벤치마크 성능 간의 관계는 단순하지 않다:

| 상황 | 관계 |
|------|------|
| 사전학습 진행 중 | 대체로 양의 상관 (PPL 감소 = 성능 향상) |
| 모델 간 비교 | 약한 상관 - 동일 PPL에서 태스크 성능 차이 가능 |
| 특수 태스크 (코딩, 수학) | PPL과 무관하게 태스크별 능력 차이 존재 |
| 오버피팅 발생 시 | PPL 감소에도 불구하고 실제 성능 저하 가능 |

> PPL은 유용한 프록시 지표이지만 모델의 실제 능력을 완전히 반영하지는 않는다. 사전학습 모니터링 용도로는 적합하고, 최종 평가는 반드시 태스크별 벤치마크를 병행해야 한다.

## 관련 문서
- [[model-evaluation-framework]] -- 모델 평가 프레임워크 (Model Evaluation Framework)

- [[bleu-rouge-metrics]] - 다른 자동 평가 지표들
- [[benchmark-design-principles]] - 벤치마크 설계와 평가의 한계
- [[evaluation-during-training]] - 학습 중 평가 전략
- [[causal-language-modeling]] - PPL이 측정하는 학습 목표
