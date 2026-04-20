---
title: BLEU
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, metrics, machine-translation, nlp, bleu]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# BLEU

BLEU(Bilingual Evaluation Understudy)는 기계 번역 품질을 자동으로 평가하는 n-gram 정밀도 기반 메트릭이다. 2002년 IBM의 Papineni, Roukos, Ward, Zhu가 발표한 이 메트릭은 NLP 자동 평가의 시대를 열었으며, 20년이 넘도록 기계 번역과 텍스트 생성 평가의 기준점으로 사용되고 있다.

## 핵심 아이디어

"기계 번역이 전문 번역가의 번역에 가까울수록 좋다"는 단순한 원칙에 기반한다. 기계가 생성한 텍스트(candidate)와 하나 이상의 참조 번역(reference) 사이에서 n-gram이 얼마나 겹치는지를 측정한다.

## 수학적 구조

BLEU는 세 가지 핵심 요소로 구성된다.

**수정된 n-gram 정밀도(Modified Precision)**: 단순 정밀도는 같은 단어를 반복하면 높은 점수를 받을 수 있다. 이를 방지하기 위해 각 n-gram의 매칭 횟수를 참조 번역에서의 최대 출현 횟수로 클리핑(clipping)한다. 즉, `min(count(n-gram in candidate), max_count(n-gram in reference))` 방식이다.

**간결성 페널티(Brevity Penalty)**: 짧은 번역은 포함된 n-gram만 정확하면 높은 정밀도를 얻을 수 있다. 이를 보정하기 위해 candidate 길이(c)가 참조 번역 길이(r)보다 짧으면 페널티를 부과한다. BP = exp(1 - r/c) (c < r일 때), 그 외에는 1이다.

**기하 평균**: 1-gram부터 4-gram까지의 수정 정밀도를 기하 평균으로 합산한다. 실무에서는 보통 BLEU-4(4-gram까지)를 기본으로 사용한다.

```
BLEU = BP * exp( sum_{n=1}^{N} w_n * log(p_n) )
```

여기서 w_n은 가중치(보통 균등 1/N), p_n은 n-gram 수정 정밀도다.

## 점수 해석

BLEU 점수는 0에서 1 사이 값을 가지며(퍼센트로 표시할 때 0~100), 1에 가까울수록 참조 번역과 유사하다. 실무적 기준은 다음과 같다.

- 0.1 미만: 거의 무의미한 번역
- 0.1~0.2: 대략적 의미 전달
- 0.2~0.3: 이해 가능한 수준
- 0.3~0.4: 양호한 품질
- 0.4 이상: 높은 품질 (인간 번역도 보통 0.5~0.7 범위)
- 1.0: 참조 번역과 완전 일치 (실무에서는 거의 불가능)

단, 이 기준은 언어 쌍과 도메인에 따라 크게 달라진다.

## BLEU가 중요한 이유

BLEU 이전에는 기계 번역 품질 평가가 전적으로 인간 평가자에게 의존했다. BLEU는 세 가지 측면에서 패러다임을 바꿨다.

- **속도**: 인간 평가에 비해 수천 배 빠르게 평가할 수 있다
- **재현성**: 동일 입력에 대해 항상 같은 점수를 산출한다
- **비용**: 평가 비용이 사실상 0에 가깝다

이러한 장점 덕분에 BLEU는 모델 개발 사이클을 크게 단축시켰고, 연구자들이 빠르게 반복 실험할 수 있는 기반을 만들었다.

## 한계

20년 이상 사용되면서 BLEU의 한계도 명확하게 드러났다.

**의미 무시**: "The cat sits on the mat"과 "A feline rests upon a rug"는 같은 뜻이지만 n-gram 겹침이 거의 없어 낮은 BLEU를 받는다. 이 문제를 해결하기 위해 [[bertscore]] 같은 의미 기반 메트릭이 등장했다.

**문장 수준 불안정성**: 짧은 문장에서는 n-gram 통계가 충분하지 않아 점수 변동이 크다. BLEU는 본래 코퍼스 수준(corpus-level) 평가를 위해 설계되었으며, 문장 수준 점수는 신뢰도가 낮다.

**토크나이제이션 의존성**: 동일 텍스트라도 토크나이저에 따라 점수가 달라진다. 이 문제를 완화하기 위해 sacrebleu 같은 표준화 도구가 등장했다.

**문법 무시**: 유창성(fluency)이나 문법적 정확성을 직접 평가하지 않는다. n-gram 겹침이 높아도 비문법적 텍스트일 수 있다.

**참조 번역 의존**: 정답이 될 수 있는 번역은 무수히 많지만, 보통 1~4개의 참조 번역만 사용한다. 참조에 포함되지 않은 올바른 표현은 패널티를 받는다.

## BLEU 변형과 후속 메트릭

BLEU의 한계를 보완하기 위해 다양한 후속 메트릭이 등장했다.

- **SacreBLEU**: 토크나이제이션을 표준화하여 재현성 문제를 해결
- **chrF/chrF++**: 문자(character) 수준 n-gram으로 형태론이 풍부한 언어에 더 적합
- **METEOR**: 동의어 매칭과 어간 추출을 추가
- **COMET**: 신경망 기반 학습된 메트릭으로 인간 판단과 더 높은 상관관계

## LLM 시대에서의 위치

GPT-4, Claude 같은 대규모 언어 모델 시대에 BLEU의 위상은 변화하고 있다. 기계 번역 평가에서도 COMET 같은 학습 기반 메트릭이 BLEU보다 인간 판단과 높은 상관관계를 보이며 주류로 올라오고 있다. LLM의 개방형 응답 평가에서는 BLEU가 거의 사용되지 않으며, [[mt-bench]]나 [[llm-as-judge-calibration]] 같은 LLM-as-Judge 방식이 대세다.

그럼에도 BLEU는 여전히 기계 번역 논문의 표준 보고 지표이며, 빠른 개발 주기에서의 sanity check 용도로 유효하다. [[evaluation-harness]]에서도 번역 태스크 평가에 BLEU를 기본으로 지원한다.

## 관련 문서

- [[rouge]] -- 재현율 중심의 n-gram 메트릭
- [[bertscore]] -- 의미 기반 임베딩 유사도
- [[perplexity]] -- 언어 모델 내재 평가
- [[mt-bench]] -- 다중 턴 대화 평가
- [[llm-as-judge-calibration]] -- LLM 판정 기반 평가
- [[human-evaluation-protocols]] -- 인간 평가 설계
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
