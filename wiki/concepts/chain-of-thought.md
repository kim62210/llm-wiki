---
title: Chain-of-Thought Prompting (CoT)
aliases: [chain-of-thought, CoT, CoT prompting, 사고의 사슬, 단계별 추론]
category: concepts
page_type: concept
tags: [chain-of-thought, prompting, reasoning, emergent-ability, 2022-2026]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Chain-of-Thought Prompting (CoT)

## 정의

**Chain-of-Thought (CoT) Prompting**은 LLM에게 최종 답변 전에 중간 추론 단계를 생성하도록 유도하는 프롬프팅 기법이다. Wei et al. (2022)이 "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"에서 제안했다. 위키 내 **104회 이상 언급**될 만큼 현대 LLM 활용의 기초 개념이다.

## 핵심 발견: Wei et al. (2022)

### 실험 결과

- GSM8K 벤치마크: PaLM 540B 정확도 **17.9% -> 58.1%** (프롬프트만으로)
- 산술, 상식, 기호 추론 태스크 전반에서 성능 향상
- 특별한 파인튜닝 없이 프롬프트에 "단계별로 생각하라"는 지시만 추가

### 창발적 능력 (Emergent Ability)

CoT는 **충분히 큰 모델에서만** 나타나는 창발적 능력이다. 소형 모델(예: 1B 파라미터 이하)에서는 중간 단계를 생성해도 정확도가 향상되지 않거나 오히려 하락한다. 이 임계값의 존재가 CoT의 본질적 특성이다.

## 세 가지 변형

### Manual CoT (수동 CoT)

[[few-shot-learning|Few-shot]] 예시에 추론 과정을 수동으로 포함시킨다.

```
Q: 주차장에 차가 3대 있고, 2대가 더 왔다. 총 몇 대?
A: 처음에 3대가 있었다. 2대가 더 왔으므로 3 + 2 = 5. 답: 5대.

Q: 카페에 손님 5명이 있고, 3명이 떠났다가 8명이 왔다. 총 몇 명?
A: ...
```

소수의 시연만으로도 극적 성능 향상을 달성한다.

### Zero-Shot CoT

Kojima et al. (2022)의 "Large Language Models are Zero-Shot Reasoners." 예시 없이 **"Let's think step by step"** 한 문장만 추가하면 모델이 자체적으로 추론 체인을 생성한다. 수동 시연 작성의 부담을 제거하면서도 상당한 성능 향상을 보인다.

### Auto-CoT (자동 CoT)

Zhang et al. (2022). 두 단계로 자동화:

1. **클러스터링**: 질문들을 유사도 기반으로 그룹화
2. **시연 생성**: 각 클러스터에서 대표 질문을 샘플링하고 [[zero-shot-learning|zero-shot]] 프롬프팅으로 추론 체인 생성

수동 노력 없이 Manual CoT에 근접한 정확도를 달성한다.

## CoT의 확장

### Tree-of-Thought (ToT)

Yao et al. (2023). 단일 추론 경로가 아닌 **트리 구조**로 여러 경로를 동시 탐색한다. 복잡한 퍼즐에서 성능이 향상되지만, 프로덕션에서 **지수적 비용 폭발**이 한계다.

### Self-Refine / Reflexion

모델이 자기 출력을 비평하고 개선하는 패턴. CoT의 반복적 적용으로 볼 수 있다. 피드백 품질이 모델 자체 능력에 의존한다는 제약이 있다.

### ReAct: Reasoning + Acting

Yao et al. (2022). Thought(추론) -> Action(도구 호출) -> Observation(관찰) 루프. CoT를 외부 도구 사용과 결합하여 [[hallucination|환각]]을 감소시킨다. 현대 [[coding-agent|코딩 에이전트]] 루프의 원형이다.

## 2025-2026년: CoT의 가치 감소?

### Wharton 연구 (2025년 6월)

Meincke, Mollick et al.의 "The Decreasing Value of Chain of Thought in Prompting"이 업계에 파장을 일으켰다.

**핵심 발견**:
- **추론 전용 모델**(o1, o3 등)에서 명시적 CoT 프롬프팅의 추가 효과가 **미미하거나 없음**
- 많은 최신 모델이 요청하지 않아도 **내부적으로 CoT 유사 추론을 수행**
- CoT 프롬프팅은 직접 답변 대비 **훨씬 많은 토큰을 소모**하면서, 추론 모델에서는 정확도 향상이 무시할 수준

### 비추론 모델에서는 여전히 유효

추론 기능이 내장되지 않은 모델(GPT-4 등)에서는 CoT가 여전히 평균 성능을 소폭 향상시킨다. 특히 모델이 기본적으로 단계별 처리를 하지 않는 경우에 효과가 있다.

### 패러다임 전환

| 시기 | CoT의 위치 |
|---|---|
| 2022 | 혁명적 발견. 프롬프트만으로 추론 성능 3배 |
| 2023-2024 | 표준 기법. 거의 모든 프롬프트에 기본 적용 |
| 2025-2026 | 선택적 사용. 모델이 자체 추론할 때는 불필요 |

## CoT와 안전성

### 모니터 가능성

[[cot-monitorability|CoT 모니터 가능성]]은 AI 안전성의 핵심 주제다. 모델의 추론 체인이 외부에 노출되므로, 어떤 근거로 결론에 도달했는지 감시할 수 있다. 그러나 [[cot-monitoring-safety|CoT 모니터링 안전성]] 연구는 모델이 "생각과 다른" 추론 체인을 생성할 수 있음을 경고한다.

### 환각 감소

[[hallucination|환각]] 완화에서 CoT는 프롬프트 기반 전략 중 가장 효과적이다. 중간 단계가 자기 검증 역할을 하여 팩트 정합성을 높인다.

## 실무 가이드라인

1. **추론 모델 사용 시**: 명시적 CoT 불필요. 토큰 낭비 회피
2. **비추론 모델 사용 시**: "단계별로 생각하라" 추가로 성능 향상
3. **복잡한 수학/논리 문제**: Manual CoT (few-shot 예시 포함)가 최고 성능
4. **환각 감소 목적**: CoT + [[rag-architecture-evolution-2026|RAG]] 결합이 효과적
5. **비용 민감한 환경**: CoT의 토큰 비용 대비 정확도 향상을 측정한 후 적용

## 관련 문서

- [[prompt-engineering]] -- CoT가 속한 Era 1의 전체 맥락
- [[ai-reasoning-models]] -- CoT를 내재화한 추론 전용 모델
- [[cot-monitorability]] -- CoT 추론의 감시 가능성
- [[cot-monitoring-safety]] -- CoT 모니터링의 안전성 한계
- [[few-shot-learning]] -- CoT의 시연 기반 변형
- [[zero-shot-learning]] -- Zero-Shot CoT의 기반
- [[hallucination]] -- CoT를 통한 환각 완화
- [[in-context-learning]] -- CoT가 ICL의 일종
- [[token-economics]] -- CoT의 토큰 비용 문제
