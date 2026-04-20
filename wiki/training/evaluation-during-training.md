---
title: 학습 중 평가 (Evaluation During Training)
category: training
page_type: concept
tags: [training, concept, evaluation, loss, perplexity, eval-harness, monitoring]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 학습 중 평가 (Evaluation During Training)

## 개요

LLM 학습은 수일에서 수주가 소요되는 대규모 투자다. 학습 중 평가(evaluation during training)는 이 과정에서 모델의 학습 상태를 실시간으로 진단하여, 조기에 문제를 발견하고 자원 낭비를 방지하는 일련의 지표와 도구를 말한다. 학습 손실(training loss), 퍼플렉시티(perplexity), 다운스트림 벤치마크 점수가 핵심 축이며, 이들을 체계적으로 측정하는 프레임워크로 lm-evaluation-harness가 사실상 표준으로 자리 잡았다.

## 핵심 지표

### 학습 손실 (Training Loss)

가장 기본적인 신호로, 모델의 예측과 실제 토큰 간 교차 엔트로피(cross-entropy)를 측정한다. 학습이 정상적으로 진행되면 손실이 단조 감소해야 하며, 비정상 패턴은 즉각적인 조사를 요한다.

| 패턴 | 의미 | 대응 |
|------|------|------|
| 급격한 손실 증가 (loss spike) | 불안정한 학습률, 데이터 품질 문제 | 학습률 감소, 해당 배치 데이터 점검 |
| 손실 정체 (plateau) | 학습률이 너무 낮거나 모델 용량 한계 | 학습률 스케줄 조정, 모델 크기 재검토 |
| 손실 발산 (divergence) | 학습률 과대, 수치 불안정 | 학습률 대폭 감소, 혼합 정밀도 설정 점검 |
| 검증 손실만 증가 | 과적합 | 정규화 강화, 데이터 다양성 확인 |

### 퍼플렉시티 (Perplexity)

퍼플렉시티는 토큰 수준 평균 음의 로그 우도를 지수화한 값으로, PPL(X) = exp(-1/t * sum(log p(x_i|x_{<i})))로 계산된다. 직관적으로 "모델이 각 위치에서 평균적으로 몇 개의 토큰 사이에서 고민하는가"를 나타낸다. 학습 손실과 단조 관계에 있지만(PPL = exp(loss)), 해석이 더 직관적이라 보고용으로 선호된다.

퍼플렉시티의 핵심 장점은 계산이 빠르고 학습 중 실시간 모니터링이 가능하다는 것이다. 다만 퍼플렉시티만으로는 모델의 실제 다운스트림 능력을 판단하기 어려우므로, 벤치마크 평가와 병행해야 한다.

### 검증 손실 (Validation Loss)

학습에 사용되지 않은 별도 검증 세트에서 측정하는 손실이다. 학습 손실과 검증 손실의 간극(gap)이 커지면 과적합을 의심한다. LLM 사전학습에서는 데이터 규모가 거대하여 전통적 의미의 과적합이 드물지만, [[data-mixing-curriculum-learning|데이터 믹싱]] 비율이 편향되었거나 특정 도메인에 과도하게 집중된 경우 발생할 수 있다.

### 다운스트림 벤치마크 점수

학습 중 주기적으로(보통 수백~수천 스텝마다) 소규모 벤치마크를 실행하여 실제 능력을 추적한다. 고비용이므로 빈도와 벤치마크 선택이 중요하다. [[data-decontamination|데이터 오염]]이 없는 벤치마크를 사용해야 학습 진행 상황을 정확히 반영한다.

## lm-evaluation-harness

EleutherAI가 개발한 lm-evaluation-harness는 200개 이상의 평가 과제를 제공하는 오픈소스 프레임워크로, LLM 학습 중 벤치마크 평가의 사실상 표준이다.

### 핵심 특징

- **통합 인터페이스**: 다양한 모델(HuggingFace, GGUF, API 등)을 동일한 인터페이스로 평가
- **few-shot 평가**: 파인튜닝 없이 few-shot 프롬프트로 다양한 과제 수행 능력 측정
- **지표 다양성**: F1, 정확도, BLEU, ROUGE, 퍼플렉시티 등 과제에 맞는 지표 자동 선택
- **재현성**: 동일 설정으로 모델 간 공정한 비교 보장

### 실무 운용 패턴

```
학습 시작
  |
  +--> 매 스텝: 학습 손실 로깅 (W&B, MLflow)
  |
  +--> 매 500 스텝: 검증 세트 퍼플렉시티 측정
  |
  +--> 매 5,000 스텝: 핵심 벤치마크 3-5개 실행 (eval harness)
  |
  +--> 체크포인트 저장 시: 전체 벤치마크 스위트 실행
```

## [[grpo|GRPO]]/[[rlvr|RLVR]] 학습에서의 평가

RL 기반 후학습에서는 사전학습과 다른 평가 관점이 필요하다.

- **보상 추이**: [[reward-model-training|보상 모델]]이 부여하는 점수의 평균/분산 추적. 보상이 지속적으로 상승하되 분산이 줄어들면 정상, 보상이 급등하면 보상 해킹을 의심
- **KL 발산**: 현재 정책과 참조 모델 간 [[kl-divergence-penalty|KL 발산]] 추적. 지나치게 커지면 정책 이탈(policy drift)
- **응답 다양성**: 엔트로피, 고유 n-gram 비율 등으로 모드 붕괴(mode collapse) 감지
- **과제별 정확도**: [[rlvr|RLVR]]에서는 수학(GSM8K, MATH), 코드(HumanEval) 등 검증 가능한 과제의 정확도를 직접 추적

## 스케일링 법칙과의 관계

학습 중 평가 지표는 스케일링 법칙(scaling laws) 검증에도 활용된다. 소형 모델에서 관찰된 손실 감소 추세를 대형 모델에 외삽하여 최종 성능을 예측하며, [[data-mixing-curriculum-learning|DoReMi]]의 프록시 모델 접근이 이 원리에 기반한다. 학습 초기 수백 스텝의 손실 곡선만으로 최종 성능을 상당히 정확하게 예측할 수 있다는 연구도 존재한다.

## 실무 권장사항

- 퍼플렉시티는 빠르고 저렴한 1차 진단 도구로 유용하지만, 다운스트림 능력의 완전한 대리 지표(proxy)는 아니다. 반드시 벤치마크와 병행해야 한다.
- 평가용 벤치마크는 [[data-decontamination|데이터 오염]]이 확인되지 않은 것만 사용한다. 오염된 벤치마크의 점수 상승은 실제 능력 향상과 무관하다.
- 학습 곡선의 비정상 패턴은 무시하지 말고 즉시 원인을 조사한다. 후반부에 발견하면 이미 수십만 GPU-시간이 낭비된 후일 수 있다.
- 평가 비용을 줄이기 위해 전체 벤치마크 대신 대표 서브셋을 선별하여 빈번하게 실행하고, 전체 스위트는 체크포인트 저장 시에만 실행한다.

## 대표 자료

- [lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness)
- [A Deep Dive on LLM Evaluation (Parlance Labs)](https://parlance-labs.com/education/evals/schoelkopf.html)
- [Perplexity of Fixed-Length Models (HuggingFace Docs)](https://huggingface.co/docs/transformers/perplexity)

## 관련 문서
- [[cicd-for-ml]] -- CI/CD for ML (머신러닝 CI/CD)
- [[wandb-mlops]] -- Weights & Biases (W&B) - ML 실험 관리

- [[data-decontamination]] -- 평가 벤치마크의 신뢰성을 보장하는 오염 제거
- [[data-mixing-curriculum-learning]] -- 평가 지표로 믹싱/커리큘럼 효과를 측정
- [[reward-model-training]] -- RL 학습에서 보상 추이 모니터링
- [[kl-divergence-penalty]] -- RL 학습에서 정책 이탈 추적 지표
- [[grpo]] -- RL 학습 루프에서의 평가 관점
- [[rlvr]] -- 검증 가능한 보상의 과제별 정확도 추적
- [[process-reward-models]] -- 단계별 보상으로 추론 과정을 평가하는 접근
