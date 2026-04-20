---
title: Classification Metrics
category: concepts
page_type: concept
tags: [concepts, concept, evaluation, metrics, classification, precision, recall, f1, auc-roc]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# Classification Metrics

Precision, Recall, F1 Score, AUC-ROC는 분류 모델의 성능을 평가하는 기본 지표군이다. 이 네 가지 메트릭은 ML/AI 평가의 근간이며, 언어 모델 시대에도 감정 분석, 독성 탐지, 스팸 필터링, 의도 분류 등 분류 기반 태스크에서 핵심 역할을 한다. LLM 평가 프레임워크인 [[deepeval]]이나 [[ragas]]에서도 이 메트릭들을 기반으로 다양한 파생 지표를 구성한다.

## 혼동 행렬(Confusion Matrix)

모든 분류 메트릭의 출발점은 혼동 행렬이다.

```
                 예측: Positive  예측: Negative
실제: Positive      TP              FN
실제: Negative      FP              TN
```

- **TP (True Positive)**: 양성을 양성으로 올바르게 예측
- **TN (True Negative)**: 음성을 음성으로 올바르게 예측
- **FP (False Positive)**: 음성을 양성으로 잘못 예측 (Type I Error)
- **FN (False Negative)**: 양성을 음성으로 잘못 예측 (Type II Error)

## Precision (정밀도)

```
Precision = TP / (TP + FP)
```

모델이 "양성"이라고 예측한 것 중 실제로 양성인 비율이다. FP를 최소화하는 것이 중요한 상황에서 핵심 지표가 된다.

**사용 사례**: 스팸 필터링(정상 메일을 스팸으로 분류하면 안 된다), 법적 문서 분류(잘못된 분류의 비용이 크다), LLM의 유해 콘텐츠 탐지(과도한 차단은 사용성을 떨어뜨린다).

## Recall (재현율)

```
Recall = TP / (TP + FN)
```

실제 양성 중 모델이 올바르게 찾아낸 비율이다. FN을 최소화하는 것이 중요한 상황에서 핵심 지표가 된다.

**사용 사례**: 의료 진단(암 환자를 정상으로 분류하면 치명적이다), 보안 위협 탐지(하나라도 놓치면 안 된다), RAG 시스템의 문서 검색(관련 문서를 빠뜨리면 응답 품질이 떨어진다).

## Precision-Recall Trade-off

Precision과 Recall은 "영원한 줄다리기" 관계다. 분류 임계값(threshold)을 낮추면 더 많은 양성을 잡아내어 recall이 올라가지만, 오탐(FP)도 늘어나 precision이 떨어진다. 반대로 임계값을 높이면 precision은 올라가지만 recall이 떨어진다.

이 trade-off는 비즈니스 맥락에 따라 결정해야 한다. "놓치는 것이 더 위험한가, 오탐이 더 위험한가"에 따라 최적점이 달라진다.

## F1 Score

```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

Precision과 Recall의 조화 평균이다. 산술 평균 대신 조화 평균을 사용하는 이유는, 두 값의 불균형을 더 엄격하게 패널티하기 위함이다. Precision 0.9, Recall 0.1이면 산술 평균은 0.5이지만 F1은 0.18로 크게 떨어진다.

**불균형 데이터에서의 중요성**: 클래스 불균형이 심한 데이터셋(예: 사기 탐지에서 사기 비율 0.1%)에서는 정확도(accuracy)가 99.9%여도 의미가 없다. F1은 이런 상황에서 더 신뢰할 수 있는 지표다.

**변형**:
- **Macro F1**: 각 클래스의 F1을 계산한 후 평균. 클래스 크기와 무관하게 각 클래스를 동등하게 취급
- **Micro F1**: 전체 TP, FP, FN을 합산한 후 F1 계산. 대규모 클래스에 가중치가 더 실림
- **Weighted F1**: 각 클래스의 F1을 해당 클래스의 support(실제 개수)로 가중 평균

## AUC-ROC

ROC(Receiver Operating Characteristic) 곡선은 분류 임계값을 변화시키면서 True Positive Rate(= Recall)과 False Positive Rate(= FP/(FP+TN))의 관계를 그린 곡선이다.

AUC(Area Under the Curve)는 이 곡선 아래의 면적으로, 0에서 1 사이 값을 가진다.

- **AUC = 0.5**: 무작위 추측과 동등
- **AUC = 1.0**: 완벽한 분류
- **AUC < 0.5**: 무작위보다 못함 (레이블이 뒤바뀌었을 가능성)

**임계값 독립성**: AUC-ROC의 핵심 장점은 특정 임계값에 의존하지 않고 모델의 전반적 판별 능력을 평가한다는 것이다. 두 모델을 "어떤 임계값에서도" 비교할 수 있다.

**PR-AUC 대안**: 클래스 불균형이 극심한 경우(양성 비율 < 1%), ROC-AUC는 과도하게 낙관적 값을 줄 수 있다. 이때는 Precision-Recall 곡선의 AUC(PR-AUC)가 더 신뢰할 수 있다.

## LLM 평가에서의 응용

전통적 분류 메트릭이 LLM 시대에도 중요한 이유가 있다.

**독성/안전성 분류**: LLM 출력의 유해성을 분류하는 guard 모델의 성능 평가에 precision/recall이 직접 사용된다. 과도 차단(low recall, high precision)과 과소 차단(high recall, low precision) 사이의 균형이 핵심이다.

**RAG 검색 품질**: [[ragas]]에서 context recall, context precision은 검색된 문서의 관련성을 분류 메트릭 관점에서 측정한다.

**NER/정보 추출**: LLM을 활용한 개체명 인식, 관계 추출에서 entity 단위 F1이 표준 평가 지표다.

**벤치마크 채점**: [[mmlu]], [[truthfulqa]] 같은 다지선다 벤치마크에서 정확도(accuracy)는 사실상 balanced class에서의 precision/recall과 동등하다.

## 실무 선택 가이드

| 상황 | 우선 지표 |
|---|---|
| FP 비용이 높은 경우 (스팸, 유해 콘텐츠 차단) | Precision |
| FN 비용이 높은 경우 (의료, 보안) | Recall |
| 균형 잡힌 평가가 필요한 경우 | F1 |
| 임계값 독립적 모델 비교 | AUC-ROC |
| 극심한 클래스 불균형 | PR-AUC |
| 멀티클래스 전반 성능 | Macro F1 |

## 관련 문서

- [[perplexity]] -- 언어 모델 내재 평가
- [[bleu]] -- 번역 평가 메트릭
- [[rouge]] -- 요약 평가 메트릭
- [[bertscore]] -- 의미 기반 평가
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[ragas]] -- RAG 평가 프레임워크
- [[benchmark-saturation-goodharts-law]] -- 단일 지표 최적화의 위험
- [[human-evaluation-protocols]] -- 인간 평가 설계
