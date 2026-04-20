---
title: Decoding Strategies -- Greedy, Beam Search, Top-k, Nucleus (Top-p)
category: concepts
page_type: concept
tags: [concepts, decoding, sampling, beam-search, greedy, top-p, top-k, nucleus-sampling, temperature]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Decoding Strategies -- Greedy, Beam Search, Top-k, Nucleus (Top-p)

LLM이 확률 분포에서 다음 토큰을 선택하는 전략 모음. 결정론적(greedy, beam search)부터 확률적(top-k, top-p, temperature) 방식까지 포괄한다.

## 정의

Decoding strategy(디코딩 전략)는 언어 모델이 각 시점에서 출력하는 어휘 전체의 확률 분포로부터 실제 다음 토큰을 어떻게 선택할지 결정하는 규칙이다. 동일한 모델이라도 디코딩 전략에 따라 출력 텍스트의 품질, 다양성, 창의성이 크게 달라진다. 모든 전략의 출발점은 모델이 생성하는 로짓(logit) 벡터이며, 이를 softmax로 확률로 변환한 뒤 전략별 선택 규칙을 적용한다.

## 결정론적 전략

### Greedy Search

매 시점에서 가장 높은 확률의 토큰 하나만 선택한다.

```
t=1: P("of")=0.32 -> 선택
t=2: P("being")=0.10 -> 선택
...
```

- **장점**: 구현 단순, 속도 최고, 재현성 100%
- **단점**: 근시안적(myopic). 현재 최선이 전체 시퀀스 최선을 보장하지 않음. 반복적이고 단조로운 텍스트 생성 경향
- **용도**: 짧은 분류 라벨, 코드 자동완성 등 결정론적 출력이 필요한 경우

### Beam Search

greedy의 일반화. 매 시점에서 상위 B개(beam width) 시퀀스를 동시에 추적한다.

```
beam_width = 3일 때:
t=1: "I have a dream of", "I have a dream that", "I have a dream to"
t=2: 각 beam에서 상위 3개 확장 -> 9개 후보 중 상위 3개 유지
...
최종: 누적 log 확률이 가장 높은 시퀀스 선택
```

- **점수 계산**: log P(w) = sum(log P(w_i | w_1...w_{i-1})), 길이 정규화 적용
- **장점**: greedy보다 높은 품질, 전역적으로 더 나은 시퀀스 탐색
- **단점**: beam 수에 비례한 계산 비용. 개방형 생성에서는 여전히 반복적/일반적 텍스트 경향
- **용도**: 기계 번역, 요약 등 정확성이 중요한 과제. beam_width 4-8이 일반적

## 확률적 전략 (Sampling)

### Temperature Scaling

모든 샘플링 전략의 기반이 되는 파라미터. softmax 함수의 입력 로짓을 온도 T로 나누어 확률 분포의 형태를 조절한다.

```
softmax(x_i / T) = exp(x_i / T) / sum_j exp(x_j / T)
```

| 온도 | 분포 형태 | 효과 |
|------|----------|------|
| T << 1 (예: 0.1) | 첨예(peaked) | 최고 확률 토큰에 집중. greedy에 수렴 |
| T = 1 | 원본 분포 | 모델 학습 시의 분포 그대로 |
| T >> 1 (예: 2.0) | 평탄(flat) | 균일 분포에 가까워짐. 무작위성 증가 |

실무에서 temperature는 단독으로 쓰기보다 top-k 또는 top-p와 조합한다. 일반적으로:
- 사실적 QA, 코드 생성: T = 0.0-0.3
- 일반 대화: T = 0.7-1.0
- 창의적 글쓰기, 브레인스토밍: T = 1.0-1.5

### Top-k Sampling

확률 상위 k개 토큰만 남기고 나머지를 0으로 마스킹한 뒤, 남은 토큰 중에서 확률적으로 샘플링한다.

```
k=3일 때:
P(A)=0.30, P(B)=0.15, P(C)=0.05, P(D)=0.01, ...
-> D 이하 제거 -> 재정규화: P(A)=0.60, P(B)=0.30, P(C)=0.10
-> 이 분포에서 샘플링
```

- **장점**: 극히 낮은 확률의 비합리적 토큰 제거
- **단점**: 고정된 k가 모든 상황에 맞지 않음. 분포가 첨예하면 k개 중 대부분이 불필요하고, 분포가 평탄하면 k개가 부족
- **일반적 설정**: k = 20-50

### Nucleus Sampling (Top-p)

Holtzman et al. (2020)이 제안. 누적 확률이 p를 초과하는 최소 토큰 집합("nucleus")에서 샘플링한다.

```
p=0.9일 때:
정렬: P(A)=0.30, P(B)=0.15, P(C)=0.12, P(D)=0.10, P(E)=0.08, ...
누적: 0.30, 0.45, 0.57, 0.67, 0.75, ... 0.92 (여기서 컷오프)
-> nucleus에 포함된 토큰에서 재정규화 후 샘플링
```

- **장점**: 분포 형태에 따라 nucleus 크기가 자동 조절. 첨예한 분포에서는 소수 토큰만, 평탄한 분포에서는 다수 토큰 포함
- **단점**: top-k보다 약간 복잡한 구현
- **일반적 설정**: p = 0.9-0.95

Top-p가 top-k보다 유연하므로, 2024년 이후 대부분의 LLM API는 top-p를 기본 제공한다. OpenAI, Anthropic, Google 모두 top-p 파라미터를 노출한다.

## 조합 전략

실무에서는 여러 전략을 조합한다.

```
[로짓] -> temperature 적용 -> top-k 필터링 -> top-p 필터링 -> 샘플링
```

예시 조합:
- **코드 생성**: temperature=0, top_p=1.0 (사실상 greedy)
- **일반 대화**: temperature=0.7, top_p=0.95
- **창의적 작문**: temperature=1.2, top_k=40, top_p=0.95

### Min-p (2024-)

최근 등장한 전략. 최고 확률 토큰의 p배 미만인 토큰을 제거한다. 예를 들어 최고 확률이 0.4이고 min_p=0.1이면, 0.04 미만의 토큰이 제거된다. Top-k와 달리 분포 형태에 적응적이며, top-p보다 직관적이라는 주장이 있다. llama.cpp, vLLM 등에서 지원하며 점차 채택이 늘고 있다.

## 평가 관점

디코딩 전략의 선택은 태스크에 따라 다르며, 만능 설정은 없다.

| 태스크 | 권장 전략 | 이유 |
|--------|----------|------|
| 기계 번역 | Beam search (B=4-8) | 정확성과 유창성 |
| 코드 생성 | Greedy 또는 T=0 | 구문 정확성 |
| 열린 대화 | Top-p=0.9, T=0.7-1.0 | 자연스러움과 다양성 |
| 창의적 글쓰기 | Top-p=0.95, T=1.0-1.5 | 예측 불가능한 표현 |
| 사실 기반 QA | T=0.0-0.3 | 환각 최소화 |

[[agentic-rag|Agentic RAG]]에서 에이전트의 추론 단계는 낮은 temperature로, 최종 응답 생성은 중간 temperature로 설정하는 패턴이 일반적이다.

## 구현 패턴

```python
def sample_next_token(logits, temperature=1.0, top_k=0, top_p=1.0):
    # 1. Temperature 적용
    logits = logits / temperature

    # 2. Top-k 필터링
    if top_k > 0:
        indices_to_remove = logits < torch.topk(logits, top_k).values[-1]
        logits[indices_to_remove] = float('-inf')

    # 3. Top-p 필터링
    if top_p < 1.0:
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
        sorted_indices_to_remove = cumulative_probs > top_p
        sorted_indices_to_remove[1:] = sorted_indices_to_remove[:-1].clone()
        sorted_indices_to_remove[0] = False
        indices_to_remove = sorted_indices[sorted_indices_to_remove]
        logits[indices_to_remove] = float('-inf')

    # 4. 샘플링
    probs = F.softmax(logits, dim=-1)
    return torch.multinomial(probs, num_samples=1)
```

## 참고 자료

- [Decoding Strategies in Large Language Models -- Hugging Face Blog](https://huggingface.co/blog/mlabonne/decoding-strategies)
- [How to Generate Text: Using Different Decoding Methods -- Hugging Face Blog](https://huggingface.co/blog/how-to-generate)
- [Decoding Strategies: How LLMs Choose The Next Word -- AssemblyAI](https://www.assemblyai.com/blog/decoding-strategies-how-llms-choose-the-next-word)

## 관련 페이지

- [[agentic-rag|Agentic RAG]] -- 추론 단계별 temperature 분리 패턴
- [[contextual-retrieval|Contextual Retrieval]] -- 생성 품질이 검색 컨텍스트에 의존
- [[graphrag-in-production|GraphRAG]] -- 그래프 탐색 기반 생성에서의 디코딩 설정
