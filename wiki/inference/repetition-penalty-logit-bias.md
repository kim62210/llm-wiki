---
title: 반복 패널티와 로짓 바이어스 (Repetition Penalty & Logit Bias)
category: inference
page_type: concept
tags: [repetition-penalty, frequency-penalty, presence-penalty, logit-bias]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# 반복 패널티와 로짓 바이어스 (Repetition Penalty & Logit Bias)

## 개요

LLM은 특정 토큰이나 구절을 과도하게 반복하는 경향이 있다. 반복 패널티(Repetition Penalty)와 로짓 바이어스(Logit Bias)는 디코딩 단계에서 토큰 확률을 직접 조작하여 이 문제를 완화하거나 특정 토큰의 출현을 강제/억제하는 기법이다.

## 반복 패널티 유형

### Repetition Penalty (기본형)

이미 생성된 토큰의 로짓을 패널티 계수로 나눈다.

$$\text{logit}'_i = \begin{cases} \frac{\text{logit}_i}{\theta} & \text{if token } i \in \text{generated} \\ \text{logit}_i & \text{otherwise} \end{cases}$$

- `theta > 1`: 이미 나온 토큰 확률 감소 (패널티)
- `theta < 1`: 이미 나온 토큰 확률 증가 (비권장)
- 기본값: `1.0` (패널티 없음), 권장: `1.1-1.3`
- 생성된 모든 토큰에 동등하게 적용

### Frequency Penalty (빈도 비례)

생성 횟수에 비례하여 패널티를 부과한다. 많이 나올수록 더 강한 패널티.

$$\text{logit}'_i = \text{logit}_i - \alpha \cdot \text{count}(i)$$

- 반복이 많을수록 해당 토큰을 더 강하게 억제
- 장문 생성에서 단어 다양성 향상에 효과적
- 범위: `-2.0` ~ `2.0` (OpenAI 기준)

### Presence Penalty (존재 여부)

한 번이라도 등장했으면 고정 패널티 부과. 빈도와 무관.

$$\text{logit}'_i = \text{logit}_i - \beta \cdot \mathbb{1}[\text{token } i \in \text{generated}]$$

- 한 번 나온 토큰은 다시 나오기 어려움
- 토픽 다양성 향상, 새로운 개념 도입 촉진
- 범위: `-2.0` ~ `2.0` (OpenAI 기준)

## 세 가지 패널티 비교

| 항목 | Repetition Penalty | Frequency Penalty | Presence Penalty |
|------|-------------------|------------------|-----------------|
| 패널티 형태 | 나눗셈 (비율) | 선형 감산 (빈도 비례) | 고정 감산 (존재 여부) |
| 반복 횟수 의존 | 없음 (동일 패널티) | 있음 (많을수록 강함) | 없음 (동일) |
| 범위 | [1, 무한) | [-2, 2] | [-2, 2] |
| 주 사용처 | HuggingFace 생태계 | OpenAI API | OpenAI API |
| 과도 적용 시 | 문법 파괴, 의미 왜곡 | 관련 단어 회피 | 주제 이탈 |

## Logit Bias API

특정 토큰 ID에 직접 바이어스 값을 추가하는 낮은 수준의 API. Repetition Penalty보다 세밀한 제어 가능.

```python
# OpenAI API 예시
response = client.chat.completions.create(
    model="gpt-4",
    messages=[...],
    logit_bias={
        "8504": -100,  # 특정 토큰 완전 금지 (-100 = 사실상 금지)
        "1234": 5,     # 특정 토큰 확률 증가
    }
)
```

- 값 범위: `-100` (완전 금지) ~ `100` (강제 생성)
- 토크나이저의 토큰 ID를 직접 지정해야 함
- Anthropic Claude: 현재 logit_bias 직접 지원 안 함

## 구현 차이 비교

| 플랫폼 | Repetition Penalty | Frequency Penalty | Presence Penalty | Logit Bias |
|--------|-------------------|------------------|-----------------|------------|
| HuggingFace Transformers | O (`repetition_penalty`) | 일부 | 일부 | O (`suppress_tokens`) |
| OpenAI API | X | O | O | O |
| Anthropic Claude | X (프롬프트로 유도) | X | X | X |
| vLLM | O | O | O | O |
| llama.cpp | O | O | O | O |

## 실용 가이드

### 반복 문제 해결

```
단순 반복(같은 문장) → repetition_penalty = 1.2-1.3
단어 다양성 부족 → frequency_penalty = 0.5-1.0
주제 고착 → presence_penalty = 0.5-1.0
```

### 주의사항

- 과도한 패널티는 정보 밀도 높은 도메인(코드, 수식)에서 품질 저하
- 반복 패널티 + Top-p 조합이 일반적으로 효과적
- 짧은 출력(< 50 토큰)에서는 패널티 효과 미미

## 관련 문서

- [[beam-search-decoding]] - 반복 방지를 위한 no_repeat_ngram_size
- [[guided-constrained-decoding]] - 로짓 마스킹의 구조적 활용
- [[inference-benchmarking]] - 패널티 설정이 품질 지표에 미치는 영향
