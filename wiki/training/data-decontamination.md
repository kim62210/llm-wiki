---
title: 데이터 오염 제거 (Data Decontamination)
category: training
page_type: concept
tags: [training, concept, data-decontamination, benchmark, evaluation, data-leak]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

# 데이터 오염 제거 (Data Decontamination)

## 개요

데이터 오염(data contamination)은 벤치마크 테스트 샘플 또는 그와 유사한 변형이 학습 데이터에 포함되어 평가 점수가 실제 능력보다 부풀려지는 현상이다. LLM의 사전학습 코퍼스가 웹 크롤 수조 토큰 규모에 달하면서, 공개 벤치마크(MMLU, GSM8K, HumanEval 등)의 문제가 학습 데이터에 섞일 가능성은 거의 필연적이다. 데이터 오염 제거(decontamination)는 이러한 누출을 탐지하고 방지하여 벤치마크 평가의 신뢰성을 유지하는 일련의 기법과 절차를 말한다.

## 왜 중요한가

오염된 벤치마크 점수는 모델 리더보드에서 부정 고득점을 만들어내지만, 실제 환경에서의 성능은 실망스러운 수준에 머문다. 이 괴리는 모델 선택, 비용 산정, 배포 결정을 왜곡한다. [[evaluation-during-training|학습 중 평가]] 지표로 벤치마크를 사용하는 경우, 오염이 학습 피드백 루프 자체를 오염시켜 모델 개발 방향을 잘못 이끌 수 있다.

## 오염 유형

### 직접 오염 (Direct Contamination)

벤치마크 문제와 정답이 학습 코퍼스에 그대로 포함되는 경우. 공개 벤치마크의 GitHub 저장소, 논문 부록, 교육 웹사이트 등을 통해 웹 크롤에 유입된다.

### 간접 오염 (Indirect Contamination)

벤치마크 문제의 패러프레이즈, 번역, 형식 변환 버전이 포함되는 경우. 직접 오염보다 탐지가 어렵지만 역시 점수를 부풀린다.

### 파인튜닝 단계 오염

사전학습 코퍼스뿐 아니라 지시 튜닝(instruction tuning)이나 [[preference-data-collection|선호도 데이터]] 생성 과정에서도 벤치마크 문제가 혼입될 수 있다. 이 경로는 사전학습 단계의 오염 제거를 수행해도 누출되는 사각지대다.

## 탐지 기법

### N-gram 중복 탐지

학습 데이터와 벤치마크 데이터 간 N-gram 중복률을 계산하는 가장 기본적인 방법이다. GPT-3 논문에서 13-gram 중복 기준으로 오염을 탐지했으나, 패러프레이즈나 형식 변환에는 무력하다.

### 퍼플렉시티 기반 탐지

모델이 특정 벤치마크 문제에 대해 비정상적으로 낮은 퍼플렉시티를 보이면 암기(memorization)를 의심한다. 그러나 실험 결과, 퍼플렉시티 기반 지표만으로는 오염된 샘플과 단순히 쉬운 샘플을 구분하기 어려운 것으로 나타났다.

### 임베딩 유사도 + LLM 판정

학습 코퍼스에서 벤치마크 문제와 가장 유사한 top-k 샘플을 임베딩 유사도로 추출한 뒤, GPT-4 같은 강력한 LLM이 "이 샘플이 벤치마크 문제와 실질적으로 동일한가"를 판정한다. 기존 자동 탐지 방법보다 높은 정확도를 보이며, 패러프레이즈 오염도 포착할 수 있다.

### 커널 발산 기반 탐지

학습 데이터에 노출된 샘플과 노출되지 않은 샘플 간의 모델 내부 표현(representation) 분포 차이를 커널 발산(kernel divergence)으로 측정한다. 블랙박스 모델에서도 API 출력만으로 오염을 추정할 수 있다는 장점이 있다.

## 방지 전략

### 사전학습 단계

- **벤치마크 저장소 제거**: 알려진 벤치마크 데이터의 원본 저장소(GitHub, HuggingFace)를 웹 크롤에서 명시적으로 제외
- **세밀한 중복 제거(deduplication)**: 정확 중복뿐 아니라 근사 중복(MinHash, SimHash)까지 제거하는 파이프라인 구축
- **파인튜닝 데이터 감사**: 지시 튜닝과 [[preference-data-collection|선호도 데이터]]에도 동일한 오염 검사 적용

### 평가 단계

- **비공개 벤치마크 (Private Benchmarking)**: 테스트 데이터를 비공개로 유지하고 API를 통해서만 평가. 모델에 테스트 데이터가 노출되지 않으므로 근본적 해결책이지만, 커뮤니티 투명성과 상충한다.
- **추론 시간 오염 제거 (Inference-Time Decontamination, ITD)**: 오염된 샘플을 탐지하여 난이도를 유지하면서 다시 작성(rewrite)한다. GSM8K에서 22.9%, MMLU에서 19.0%의 부풀려진 정확도를 보정한 사례가 보고되었다.
- **코드 리팩터링**: 코드 벤치마크(HumanEval 등)에서 변수명, 함수 구조를 리팩터링하여 단순 암기로 풀 수 없게 만드는 변환 연산자(mutation operator)를 적용한다.

## [[data-mixing-curriculum-learning|데이터 믹싱]]과의 관계

도메인별 가중치를 최적화하는 데이터 믹싱과 오염 제거는 사전학습 데이터 관리의 양대 축이다. 도메인 가중치를 높여도 해당 도메인에 벤치마크 데이터가 포함되어 있으면 평가 결과가 왜곡된다. 따라서 믹싱 최적화와 오염 제거는 반드시 결합하여 수행해야 한다.

## 열린 문제

- **대규모 코퍼스 검사 비용**: 수조 토큰 규모의 코퍼스를 완전히 검사하는 것은 계산적으로 비용이 크다. 효율적인 샘플링 기반 검사가 연구 중이다.
- **비공개 벤치마크의 딜레마**: 비공개 벤치마크는 오염을 방지하지만, 재현성과 공정한 비교를 저해한다. 완전 비공개와 완전 공개 사이의 균형점이 아직 합의되지 않았다.
- **새로운 벤치마크의 빠른 오염**: 새 벤치마크가 공개되면 빠르게 학습 데이터에 편입되므로, 벤치마크의 유효 수명이 계속 짧아지고 있다.

## 대표 자료

- [When Benchmarks Leak: Inference-Time Decontamination for LLMs (2026)](https://arxiv.org/html/2601.19334)
- [How Contaminated Is Your Benchmark? Measuring Dataset Leakage with Kernel Divergence (2025)](https://arxiv.org/html/2502.00678)
- [Rethinking Benchmark and Contamination for Language Models (2023)](https://arxiv.org/pdf/2311.04850)

## 관련 문서

- [[evaluation-during-training]] -- 학습 중 평가에서 오염이 미치는 영향
- [[data-mixing-curriculum-learning]] -- 오염 제거와 결합해야 하는 데이터 구성 최적화
- [[rlvr]] -- 검증 가능한 보상 기반 학습에서 벤치마크 오염의 영향
- [[grpo]] -- RL 학습에서 보상 신호가 오염된 벤치마크에 의존할 때의 위험
- [[process-reward-models]] -- 단계별 평가에서 오염된 문제의 영향
