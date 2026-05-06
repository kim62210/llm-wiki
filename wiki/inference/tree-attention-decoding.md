---
title: 트리 어텐션 디코딩
category: inference
page_type: concept
tags: [추측디코딩, 트리어텐션, 병렬검증, KV공유, inference]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 트리 어텐션 디코딩 (Tree Attention Decoding)

## 개요

트리 어텐션 디코딩(Tree Attention Decoding)은 [[speculative-decoding]]에서 여러 개의 드래프트 토큰 후보를 **트리(tree) 구조로 조직화하여 한 번의 포워드 패스로 동시에 검증**하는 기법이다. 선형(linear) 추측 디코딩이 하나의 드래프트 시퀀스만 검증하는 것과 달리, 트리 어텐션은 다수의 분기(branch)를 병렬로 검증하여 수용 토큰 수를 극대화한다.

이 기법은 [[medusa-multi-head-decoding]], [[eagle-3-speculative-decoding]], 그리고 SpecInfer 등에서 핵심 구성 요소로 활용된다.

## 선형 추측 디코딩의 한계

표준 추측 디코딩([[speculative-decoding]])은 드래프트 시퀀스를 하나만 생성한다:

```
드래프트: [A, B, C, D]  (선형 시퀀스)
검증:      A 맞음 -> B 맞음 -> C 틀림 -> 중단
결과:      [A, B, 수정된_C] (2개 드래프트 수용)
```

드래프트 시퀀스가 틀린 위치에서 이후 토큰이 아무리 맞아도 채택이 불가능하다. 트리 구조는 이 제약을 극복한다.

## 트리 구조의 이점

```mermaid
flowchart TD
    루트[x_t: 입력 토큰] --> A1[드래프트 a1]
    루트 --> A2[드래프트 a2]
    A1 --> B1[b1 | a1]
    A1 --> B2[b2 | a1]
    A2 --> B3[b3 | a2]
    A2 --> B4[b4 | a2]
    B1 --> C1[c1 | b1,a1]
    B2 --> C2[c2 | b2,a1]
    B3 --> C3[c3 | b3,a2]

    style 루트 fill:#e8f5e9
    style A1 fill:#bbdefb
    style A2 fill:#bbdefb
```

트리의 각 경로는 독립적인 드래프트 시퀀스다. 검증 시 타겟 모델은 트리의 모든 노드를 한 번의 포워드 패스로 처리하고, 각 위치에서 올바른 토큰인지 판단한다.

## 트리 어텐션 마스크

트리 구조에서 어텐션은 각 노드가 **자신의 조상 노드(ancestor)**에만 주의를 기울이도록 마스킹되어야 한다. 같은 부모를 공유하는 형제 노드끼리는 주의를 기울이지 않는다.

```
트리 노드:    [x_t, a1, a2, b1|a1, b2|a1, b3|a2]
어텐션 마스크 (O = 주의 허용):

         x_t  a1   a2  b1|a1  b2|a1  b3|a2
x_t:      O    -    -    -      -      -
a1:       O    O    -    -      -      -
a2:       O    -    O    -      -      -
b1|a1:    O    O    -    O      -      -
b2|a1:    O    O    -    -      O      -
b3|a2:    O    -    O    -      -      O
```

이 마스크는 각 드래프트 경로가 올바른 컨텍스트 내에서 검증되도록 보장한다.

## 수학적 표현

$N$개 노드를 가진 트리에서 각 노드 $v$의 조상 집합을 $\text{Anc}(v)$라 하면, 어텐션은:

$$\text{Attn}(v) = \text{softmax}\left(\frac{q_v \cdot K_{\text{Anc}(v)}^T}{\sqrt{d}}\right) \cdot V_{\text{Anc}(v)}$$

이를 전체 트리에 대해 일반적인 Transformer 포워드 패스로 표현하면:

$$\text{Output} = \text{Transformer}(X_{\text{tree}}, \text{Mask}_{\text{tree}})$$

여기서 $X_{\text{tree}}$는 트리의 모든 노드를 일렬로 나열한 시퀀스이고, $\text{Mask}_{\text{tree}}$는 위의 조상-관계 마스크다.

## KV 캐시 공유

트리의 공통 조상 경로는 KV 캐시를 공유할 수 있다. 예를 들어 a1 노드의 KV는 b1|a1과 b2|a1 모두에서 재사용된다:

```mermaid
flowchart LR
    subgraph KV캐시 ["KV 캐시 (공유)"]
        K1[x_t의 KV]
        K2[a1의 KV]
        K3[a2의 KV]
    end
    subgraph 노드들 ["트리 노드"]
        N1[b1|a1]
        N2[b2|a1]
        N3[b3|a2]
    end
    K1 --> N1
    K1 --> N2
    K1 --> N3
    K2 --> N1
    K2 --> N2
    K3 --> N3
```

[[paged-attention]] 기반 KV 캐시 관리에서 트리의 공통 접두사(prefix)를 하나의 물리적 블록으로 저장하고 논리적으로만 공유함으로써 메모리 효율을 높인다.

## 트리 선택 전략

어떤 드래프트 후보들로 트리를 구성할지 결정하는 것이 중요하다:

### 1. 상위-k 샘플링 기반 트리

각 위치에서 드래프트 모델의 상위 $k$개 토큰을 후보로 선택:

```python
def build_draft_tree(draft_model, context, depth=3, branching=2):
    """
    depth: 트리 깊이
    branching: 각 노드에서의 분기 수
    """
    tree = {0: {'token': None, 'parent': -1}}
    frontier = [0]

    for d in range(depth):
        new_frontier = []
        for node_id in frontier:
            # 해당 노드의 컨텍스트로 드래프트 모델 실행
            context_for_node = get_context(tree, node_id, context)
            logits = draft_model(context_for_node)
            top_k_tokens = logits.topk(branching).indices

            for tok in top_k_tokens:
                new_id = len(tree)
                tree[new_id] = {'token': tok, 'parent': node_id}
                new_frontier.append(new_id)

        frontier = new_frontier
    return tree
```

### 2. 온도 샘플링 기반 트리

결정론적 top-k 대신 샘플링으로 다양성을 확보한다. 온도가 높을수록 더 다양한 후보를 생성한다.

### 3. EAGLE 드래프트 헤드 기반 트리

[[eagle-3-speculative-decoding]]의 드래프트 헤드는 학습을 통해 수용률이 높은 후보를 우선적으로 생성하도록 최적화되어 있어, 트리 기반 검증과 결합 시 더 높은 효율을 달성한다.

## Medusa의 트리 어텐션 구현

[[medusa-multi-head-decoding]]은 트리 어텐션을 사용하는 대표적 시스템이다. Medusa의 특수성:

- **독립 헤드**: 각 미래 위치에 독립적인 예측 헤드 사용
- **고정 트리 구조**: 미리 정의된 트리 템플릿 사용 (런타임 동적 생성 아님)
- **수용률 최적화**: 학습 중 트리 구조를 최적화하여 수용률 극대화

Medusa 트리의 전형적 형태:
```
위치 1:  top-3 후보 (a1, a2, a3)
위치 2:  각 후보에 대해 top-2 (총 6개)
위치 3:  일부 경로만 top-1 확장 (총 10개)
```

## SpecInfer의 접근

SpecInfer(2023)는 Hydra와 유사하게 여러 드래프트 모델로부터 다수의 추측 시퀀스를 생성하고, 이를 트리로 병합하여 한 번의 LLM 검증 패스로 모두 검증한다. 트리 어텐션 마스크가 이 병합 과정의 핵심이다.

## 배치 트리 처리

여러 요청을 동시에 처리하는 배치 환경에서 트리 어텐션은 추가 복잡성을 가진다. 각 요청이 서로 다른 트리 구조를 가질 수 있으므로:

- 요청별로 독립적인 트리 마스크를 구성
- 배치 내에서 패딩(padding) 없이 트리를 이어 붙여 처리 (시퀀스 패킹과 유사)
- [[continuous-batching-internals]]와 통합 시 트리 크기 관리가 중요

## 성능 분석

트리 크기 $T$ (노드 수)에 따른 이론적 가속:

$$\text{유효 가속} = \frac{E[\text{채택 토큰 수}]}{T \cdot c_{\text{드래프트}} + c_{\text{검증}}}$$

트리가 클수록 채택 토큰 수가 늘지만, 검증 비용도 증가한다. 최적 트리 크기는 드래프트 모델 속도와 수용률에 따라 결정된다.

실험적으로 트리 크기 10-20개 노드에서 최적 효율이 관찰되며, 이 범위에서 선형 추측 디코딩 대비 15-30% 추가 가속이 가능하다.

## 관련 문서

- [[speculative-decoding]] - 추측 디코딩 기반 개념
- [[medusa-multi-head-decoding]] - 트리 어텐션을 사용하는 다중 헤드 추측 디코딩
- [[eagle-3-speculative-decoding]] - 학습된 드래프트 헤드와 트리 검증
- [[hydra-speculation-cascade]] - 캐스케이드 추측 디코딩
- [[blockwise-parallel-decoding]] - 블록단위 선형 검증
- [[paged-attention]] - KV 캐시 공유 지원
- [[flash-decoding]] - 효율적 어텐션 계산
- [[continuous-batching-internals]] - 배치 환경에서의 트리 처리
