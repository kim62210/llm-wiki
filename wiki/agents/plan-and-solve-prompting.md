---
title: Plan-and-Solve 프롬프팅
category: agents
page_type: concept
tags: [plan-and-solve, prompting, chain-of-thought, step-by-step, EMNLP2023]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# Plan-and-Solve 프롬프팅

## 개념 정의

Plan-and-Solve(PS) 프롬프팅은 Wang et al.(EMNLP 2023)이 제안한 제로샷(zero-shot) 추론 강화 기법이다. "Let's think step by step"으로 유명한 기본 CoT의 두 가지 약점 - **계획 부재**와 **계산 실수** - 를 해결하기 위해 추론 전에 명시적 계획 단계를 삽입한다.

기본 아이디어: 복잡한 문제를 만났을 때 바로 계산/추론에 뛰어들지 말고, 먼저 문제를 하위 단계로 나누는 **계획(plan)**을 작성한 뒤 각 단계를 순서대로 **해결(solve)**하라.

```mermaid
flowchart LR
    Problem[문제 입력] --> Plan[계획 수립\n하위 단계 분리]
    Plan --> S1[단계 1 실행]
    S1 --> S2[단계 2 실행]
    S2 --> S3[단계 3 실행]
    S3 --> Synthesize[결과 통합]
    Synthesize --> Answer[최종 답변]
```

## CoT와의 비교

| 속성 | 기본 CoT | Plan-and-Solve |
|------|----------|----------------|
| 트리거 프롬프트 | "Let's think step by step" | "Let's first understand and devise a plan..." |
| 계획 단계 | 없음 (암묵적) | 명시적 계획 생성 |
| 계산 오류 | 높음 | 감소 (단계별 검증 유도) |
| 변수 추적 | 약함 | 강함 (PS+ 변형) |
| 제로샷 성능 | 기준선 | 대부분 벤치마크에서 우세 |

## 프롬프트 패턴

### 기본 Plan-and-Solve (PS)

```
{문제 설명}

먼저 문제를 이해하고, 해결을 위한 계획을 세운 뒤, 계획에 따라 단계별로 문제를 풀어라.
```

### Plan-and-Solve+ (PS+)

PS+는 기본 PS에 변수 추적과 계산 정확성을 강조하는 지시문을 추가한 강화 버전이다:

```
{문제 설명}

먼저 문제를 이해하고 해결을 위한 계획을 세워라.
그 다음, 계획을 실행하면서 각 단계에서 관련 변수의 값을 정확하게 계산하고,
중간 결과를 기록하면서 단계별로 문제를 풀어라.
계산 실수가 없도록 각 수식을 신중하게 검토한다.
```

## 동작 예시: 수학 문제

### 입력 문제
"사과 3상자가 있고 각 상자에는 사과가 24개 있다. 배가 가득 든 바구니가 2개 있고 각 바구니에는 배가 18개 있다. 사과와 배를 합한 총 개수는?"

### 기본 CoT 응답 (문제 있음)
```
사과: 3 x 24 = 72
배: 2 x 18 = 36  
합계: 72 + 36 = 108 개
```
(단계가 단순하면 맞지만 복잡해지면 중간 오류가 전파됨)

### PS+ 응답

```
[계획]
1. 사과 총 개수 계산: 상자 수 x 상자당 사과 수
2. 배 총 개수 계산: 바구니 수 x 바구니당 배 수
3. 합산

[실행]
단계 1: 사과 상자 수 = 3, 상자당 사과 수 = 24
        사과 총 개수 = 3 x 24 = 72

단계 2: 배 바구니 수 = 2, 바구니당 배 수 = 18
        배 총 개수 = 2 x 18 = 36

단계 3: 총 과일 수 = 72 + 36 = 108

[최종 답변] 108개
```

## 알고리즘 구조

```python
def plan_and_solve(problem: str, llm, use_ps_plus: bool = True) -> str:
    """Plan-and-Solve 프롬프팅 구현"""
    if use_ps_plus:
        instruction = (
            "먼저 문제를 이해하고 해결을 위한 계획을 세워라. "
            "그 다음, 계획을 실행하면서 각 단계에서 관련 변수의 값을 "
            "정확하게 계산하고, 중간 결과를 기록하면서 단계별로 문제를 풀어라. "
            "계산 실수가 없도록 각 수식을 신중하게 검토한다."
        )
    else:
        instruction = "먼저 문제를 이해하고, 해결을 위한 계획을 세운 뒤, 계획에 따라 단계별로 문제를 풀어라."

    prompt = f"{problem}\n\n{instruction}"
    return llm.generate(prompt)
```

## 성능 특성

EMNLP 2023 논문에서 보고된 주요 결과:

- **수학 추론(GSM8K, MATH)**: 기본 CoT 대비 PS+가 일관되게 우세
- **상식 추론(CommonSenseQA)**: 소폭 향상
- **기호 추론(Letter Concatenation)**: 유의미한 개선
- **GPT-3.5 vs GPT-4**: 모든 모델 크기에서 PS/PS+ 효과 확인

핵심 이점은 계획 단계가 모델로 하여금:
1. 문제의 전체 구조를 파악하게 함
2. 각 단계의 입력/출력을 명확히 하게 함
3. 불필요한 단계를 건너뛰는 실수를 방지함

## Chain-of-Thought 계열 위치

PS 프롬프팅은 [[chain-of-thought-prompting]] 계열에서 다음과 같이 위치한다:

```mermaid
flowchart TD
    CoT[Chain-of-Thought\n암묵적 단계 추론] --> ZS[Zero-Shot CoT\n"Let's think step by step"]
    ZS --> PS[Plan-and-Solve\n명시적 계획 + 단계 실행]
    PS --> PSPlus[PS+\n변수 추적 + 계산 검증]
    PSPlus --> PAE[Plan-and-Execute\n계획과 실행을 별도 에이전트로]
```

[[plan-and-execute-pattern]]은 PS의 에이전트 버전으로, 계획 수립과 실행을 별도 모델/에이전트가 담당한다.

## 적용 시 주의사항

### 과잉 계획
단순한 문제에 긴 계획을 강요하면 오히려 성능이 저하된다. 복잡도 기반 라우팅: 단순 문제는 기본 CoT, 복잡한 문제만 PS를 적용한다.

### 계획과 실행의 불일치
생성된 계획과 실제 실행 단계가 괴리될 수 있다. 계획을 생성한 뒤 각 단계를 계획과 대조하는 자기 검증 단계를 추가하면 도움된다.

### 도메인 의존성
수학/논리 추론에서는 효과가 크지만, 자유로운 창의적 생성이나 감성적 텍스트에는 계획 구조가 오히려 딱딱한 결과를 낳는다.

### 토큰 비용
계획 단계가 추가되므로 출력 토큰이 증가한다. 비용에 민감한 애플리케이션에서는 PS+ 대신 기본 PS 또는 적절히 단축된 변형을 사용한다.

## 실무 적용 패턴

### 수학/과학 문제 해결 도우미
계산 단계가 많은 물리, 통계 문제에서 PS+를 기본으로 적용. 중간 결과를 표 형태로 기록하게 하면 검증이 용이하다.

### 코드 생성
코드 작성 전 알고리즘 계획을 먼저 생성하게 하면 구현 일관성이 높아진다.

### 문서 분석
긴 문서의 특정 정보 추출 시, 먼저 "어떤 섹션을 어떤 순서로 확인할지" 계획을 수립하게 한 뒤 실행한다.

## 관련 문서

- [[chain-of-thought]] - 선형 추론 전개 기법
- [[chain-of-thought-prompting]] - CoT 프롬프팅 상세
- [[selfask-decomposition]] - 자기 질문 분해 패턴
- [[plan-and-execute-pattern]] - 에이전트 수준 계획-실행 분리
- [[agent-planning-strategies]] - 에이전트 계획 전략 개요
- [[self-consistency-decoding]] - 다수결 앙상블로 정확도 향상
- [[react-pattern]] - 추론-행동 통합 패턴
