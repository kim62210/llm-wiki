---
title: 증거 귀속과 인용 생성 (Evidence Attribution & Citation Generation)
category: concepts
page_type: concept
tags: [attribution, citation, RAG, 검증, evidence, 인용, Anthropic, 신뢰성]
sources: []
created: 2026-04-27
updated: 2026-04-27
---

# 증거 귀속과 인용 생성 (Evidence Attribution & Citation Generation)

## 정의 / 본질

**증거 귀속(evidence attribution)**은 생성된 답변의 각 주장(claim)을 뒷받침하는 구체적인 소스 구절(passage)에 매핑하는 과정이다. 단순히 "소스를 사용했다"를 확인하는 충실성/그라운드니스 평가보다 한 단계 나아가, 주장-증거 쌍을 명시적으로 구성하고 인용(citation)으로 표면화한다.

**인용 생성(citation generation)**은 귀속 결과를 사용자에게 전달 가능한 형태 -- 인라인 `[1]`, 주석, 하이라이트 -- 로 변환하는 작업이다.

검증 가능한 RAG(verifiable RAG)의 핵심 구성요소로, 사용자가 답변의 근거를 직접 확인할 수 있게 함으로써 시스템 신뢰성을 높인다.

## 핵심 아이디어

### 증거 귀속의 세 단계

```mermaid
flowchart TD
    A[입력 문서들\n+ LLM 생성 답변] --> B[주장 분해\nClaim Decomposition]
    B --> C[주장 단위 목록]
    C --> D[증거 탐색\nEvidence Retrieval\n각 주장 - 소스 구절 매칭]
    D --> E[귀속 판단\nAttribution Judgment\nNLI or LLM-Judge]
    E --> F{귀속 가능?}
    F -->|Yes| G[인용 인덱스 할당\n주장에 [n] 태그 부착]
    F -->|No| H[미귀속 표시\n신뢰도 경고]
    G & H --> I[인용 포함 최종 응답]
```

### 주장-증거 매핑 방법론

귀속 방법은 크게 세 가지 계층으로 구분된다.

**1. 추출 방식 (Extractive)**
답변을 소스 구절에서 직접 추출한 텍스트로 제한. 귀속이 자명하지만 표현력이 제한됨.

**2. 근사 매칭 방식 (Approximate Matching)**
임베딩 유사도나 BM25로 주장과 가장 유사한 소스 구절을 찾아 귀속. 빠르고 저렴하나 의미적 수반 관계를 보장하지 않음.

**3. NLI / LLM 판단 방식 (Inference-based)**
각 (주장, 구절) 쌍을 NLI 모델이나 LLM으로 수반 관계를 판단. 정확하지만 계산 비용이 높음.

```python
from sentence_transformers import CrossEncoder

nli_model = CrossEncoder("cross-encoder/nli-deberta-v3-base")

def attribute_claim(claim: str, passages: list[str]) -> tuple[int | None, float]:
    """주장을 가장 잘 지지하는 구절 인덱스와 점수를 반환"""
    pairs = [(claim, p) for p in passages]
    scores = nli_model.predict(pairs)
    # 점수 형식: [contradiction, neutral, entailment]
    entailment_scores = [s[2] for s in scores]
    best_idx = max(range(len(entailment_scores)), key=lambda i: entailment_scores[i])
    best_score = entailment_scores[best_idx]
    if best_score > 0.7:
        return best_idx, best_score
    return None, best_score
```

### 인용 정확성 (Citation Accuracy)

생성된 인용이 실제로 주장을 지지하는지를 측정하는 별도의 메트릭. 단순히 인용이 존재하는 것과 인용이 정확한 것은 다르다.

| 평가 지표 | 정의 |
|-----------|------|
| **Citation Recall** | 귀속 가능한 주장 중 실제로 인용이 생성된 비율 |
| **Citation Precision** | 생성된 인용 중 실제로 주장을 지지하는 비율 |
| **Grounding Rate** | 전체 주장 중 검증된 소스로 귀속된 비율 (ATTR) |
| **Citation F1** | Citation Recall × Citation Precision의 조화 평균 |

## Anthropic Citations API

Anthropic은 Claude API에 **Citations** 기능을 제공한다. 이 기능은 답변 생성 시 소스 구절을 명시적으로 참조하도록 모델에 지시하여, 구조화된 인용 메타데이터를 응답에 포함시킨다.

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "document",
                "source": {
                    "type": "text",
                    "media_type": "text/plain",
                    "data": "변압기는 두 개 이상의 코일로 구성되며...",
                },
                "title": "전기 기초",
                "citations": {"enabled": True}
            },
            {
                "type": "text",
                "text": "변압기의 구성에 대해 설명해주세요."
            }
        ]
    }]
)
```

응답에는 텍스트 블록과 함께 해당 텍스트가 소스의 어느 부분에 기반하는지 `start_char_index`, `end_char_index`가 포함된 `citations` 필드가 담긴다. [교차검증 필요: Anthropic Citations API 파라미터 상세 구조는 공식 문서에서 확인할 것]

## 실제 사례 / 응용

### 의학 정보 시스템

환자가 "이 약의 부작용이 무엇인가요?" 질문 시, 각 부작용 주장을 의약품 첨부 문서(Package Insert)의 정확한 섹션으로 귀속하여 의료진이 원문을 직접 확인할 수 있도록 함.

```mermaid
flowchart LR
    Q[환자 질문] --> RAG[RAG 생성]
    RAG --> C[주장 분해]
    C --> M[의약품 DB 매칭]
    M --> V[NLI 귀속 검증]
    V --> R["답변 + [PI §4.5] 형태 인용"]
```

### 법률 리서치 도구

판례 요약 시스템에서 각 법적 주장을 해당 판결문의 특정 단락으로 귀속. 변호사가 원문 확인 후 인용 가능하게 함.

### 뉴스 팩트체크 시스템

주장을 뉴스 기사 데이터베이스의 구체적인 단락에 귀속하여, 정보의 출처와 날짜를 명시. 사용자가 편향이나 맥락 왜곡을 감지할 수 있게 함.

### 엔터프라이즈 지식 베이스 Q&A

내부 문서 기반 QA에서 귀속은 답변의 신뢰성뿐 아니라 "이 정책이 어느 문서 몇 페이지에 있는지"를 바로 찾아주는 생산성 도구 역할을 한다.

## 귀속 실패 유형 분류

```mermaid
flowchart TD
    F[귀속 실패] --> F1[소스 없음\nNo Source\n관련 소스가 검색 안됨]
    F --> F2[약한 수반\nWeak Entailment\n소스가 있지만 주장을 충분히 지지 못함]
    F --> F3[복합 귀속\nMulti-source\n여러 소스의 조합으로만 지지됨]
    F --> F4[반박 소스\nContradicting Source\n소스가 주장과 충돌]
    F1 --> R1[추가 검색 또는 '소스 없음' 표시]
    F2 --> R2[신뢰도 점수 하향 + 경고]
    F3 --> R3[복수 인용 표시 [1,2]]
    F4 --> R4[충돌 경고 + 원문 제시]
```

## 한계 / 비판

### 인용 환각 (Citation Hallucination)

LLM이 존재하지 않는 소스를 인용하거나, 실제 소스가 주장을 지지하지 않는데도 인용을 생성하는 현상. 단순히 인용 형식을 출력하도록 학습된 모델에서 자주 발생.

이를 방지하려면 모델이 생성한 인용을 항상 사후 검증하는 계층이 필요하다 ([[faithfulness-attribution]] 참조).

### 세분화 단위 문제

주장을 너무 작게 쪼개면 귀속이 불필요하게 복잡해지고, 너무 크게 잡으면 정확한 소스 위치를 특정하기 어렵다. 적절한 주장 단위(granularity)가 도메인마다 다르다.

### 소스 구절 범위 결정

"이 인용은 소스의 어디서 어디까지인가"를 결정하는 것이 비자명하다. 문장 단위, 단락 단위, 슬라이딩 윈도우 등 다양한 분할 전략이 결과에 영향.

### 계산 비용

주장 n개 × 소스 구절 m개의 모든 조합을 NLI 모델로 검증하면 $O(n \times m)$ 연산이 필요하다. 실용화를 위해 후보 구절을 먼저 BM25/임베딩으로 줄이는 2단계 접근이 일반적.

## 관련 문서

- [[faithfulness-attribution]] -- 충실성과 출처 귀속의 개념적 관계
- [[groundedness-evaluation]] -- 그라운드니스 평가 방법론
- [[hallucination-mitigation]] -- 인용 환각 포함 환각 전반 완화
- [[advanced-rag-patterns]] -- 귀속을 RAG 파이프라인에 통합하는 패턴
- [[verifier-critic-models]] -- 귀속 판단에 사용되는 검증기 모델
