---
title: 에이전트 청킹
category: rag
page_type: concept
tags: [청킹, RAG, 에이전트, LLM청킹, 자율청크결정, 고품질RAG]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# 에이전트 청킹

## 정의

에이전트 청킹(agentic chunking)은 **LLM 에이전트가 문서의 내용과 구조를 이해한 뒤 청크 경계를 스스로 결정**하는 청킹 전략이다. 규칙 기반(고정 길이, 재귀 분할)이나 단순 유사도 기반(의미적 청킹)이 아니라, 에이전트가 문서를 읽고 "여기서 끊는 것이 의미론적으로 최선"이라는 추론을 통해 청크를 구성한다.

가장 비싸지만 현존하는 청킹 방식 중 최고 품질을 달성할 수 있으며, 일반적인 텍스트 분할로는 처리하기 어려운 복잡한 문서 구조에 특히 효과적이다.

```mermaid
flowchart TD
    DOC[원본 문서] --> AGENT[LLM 에이전트]
    AGENT --> ANALYZE{문서 분석}
    ANALYZE --> STRUCT["구조 파악\n(섹션, 논증, 예시)"]
    ANALYZE --> INTENT["주제 의도 파악\n(핵심 vs 보조 정보)"]
    STRUCT --> DECIDE[청크 경계 결정]
    INTENT --> DECIDE
    DECIDE --> C1["청크 1\n(논리적 단위 A)"]
    DECIDE --> C2["청크 2\n(논리적 단위 B)"]
    DECIDE --> C3["청크 3\n(논리적 단위 C)"]
    C1 --> META[메타데이터 생성\n(요약, 키워드, 관계)]
    C2 --> META
    C3 --> META
    META --> INDEX[인덱싱]
```

위 다이어그램은 에이전트가 문서를 이해하고 추론을 통해 청크 경계와 메타데이터를 동시에 생성하는 흐름이다.

---

## 핵심 차이점

### 전통적 청킹 vs 에이전트 청킹

| 구분 | 전통적 청킹 | 에이전트 청킹 |
|------|------------|-------------|
| 경계 결정 기준 | 토큰 수, 문자 수, 유사도 임계값 | LLM 추론 (의미, 구조, 목적) |
| 문서 이해 | 없음 | 전체 문서 읽고 이해 |
| 메타데이터 | 없거나 기본적 | 요약, 키워드, 관계 자동 생성 |
| 적응성 | 모든 문서에 동일 규칙 | 문서마다 최적 전략 선택 |
| 비용 | 낮음 | 매우 높음 |

---

## 구현 방식

### 방식 1: 청크 경계 직접 결정

LLM에게 문서를 제시하고 어디서 끊어야 하는지 직접 판단하게 한다:

```python
from openai import OpenAI
import json

client = OpenAI()

AGENTIC_CHUNKING_PROMPT = """다음 문서를 분석하고 최적의 청크 경계를 결정하세요.

목표:
- 각 청크는 하나의 완결된 주제/개념을 담아야 합니다
- 청크 간 논리적 흐름이 끊기지 않아야 합니다
- 각 청크는 독립적으로 검색되어도 유용해야 합니다
- 너무 짧거나 (50토큰 미만) 너무 길지 (1000토큰 초과) 않게 설정하세요

출력 형식 (JSON):
{{
  "chunks": [
    {{
      "start_sentence": "청크 시작 문장 첫 10 단어",
      "end_sentence": "청크 끝 문장 마지막 10 단어",
      "topic": "이 청크의 핵심 주제",
      "rationale": "여기서 끊은 이유"
    }}
  ]
}}

문서:
{document}"""


def agentic_chunk_boundaries(document: str) -> list[dict]:
    """에이전트가 청크 경계를 결정."""
    response = client.chat.completions.create(
        model="gpt-4o",  # 추론 품질이 중요하므로 고성능 모델 사용
        messages=[{
            "role": "user",
            "content": AGENTIC_CHUNKING_PROMPT.format(document=document),
        }],
        response_format={"type": "json_object"},
        temperature=0.1,
    )
    result = json.loads(response.choices[0].message.content)
    return result.get("chunks", [])
```

### 방식 2: 순차적 청크 구성 에이전트

에이전트가 문서를 처음부터 읽으며 현재 청크에 추가할지, 새 청크를 시작할지 결정한다:

```python
SEQUENTIAL_CHUNKING_PROMPT = """당신은 문서 청킹 에이전트입니다.
현재까지 모은 청크 내용과 다음 문장을 보고 결정하세요:

현재 청크 (현재까지 {current_len} 토큰):
{current_chunk}

다음 문장:
{next_sentence}

결정:
1. "continue" - 현재 청크에 추가 (같은 주제 계속)
2. "split" - 새 청크 시작 (주제 전환, 충분한 길이)

이유도 함께 제공하세요.
JSON: {{"decision": "continue"|"split", "reason": "..."}}"""


def sequential_agentic_chunking(
    sentences: list[str],
    min_chunk_tokens: int = 100,
    max_chunk_tokens: int = 800,
) -> list[str]:
    """문장을 순차적으로 읽으며 에이전트가 청크를 구성."""
    chunks = []
    current_chunk = []
    current_len = 0

    for sentence in sentences:
        sent_tokens = len(sentence.split())

        # 최소 길이 미달 시 강제 추가
        if current_len < min_chunk_tokens:
            current_chunk.append(sentence)
            current_len += sent_tokens
            continue

        # 최대 길이 초과 시 강제 분리
        if current_len + sent_tokens > max_chunk_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_len = sent_tokens
            continue

        # 에이전트에게 결정 요청
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 빠른 결정에는 소형 모델
            messages=[{
                "role": "user",
                "content": SEQUENTIAL_CHUNKING_PROMPT.format(
                    current_len=current_len,
                    current_chunk=" ".join(current_chunk[-3:]),  # 마지막 3문장만
                    next_sentence=sentence,
                ),
            }],
            response_format={"type": "json_object"},
            temperature=0,
        )
        decision_data = json.loads(response.choices[0].message.content)

        if decision_data["decision"] == "split":
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_len = sent_tokens
        else:
            current_chunk.append(sentence)
            current_len += sent_tokens

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
```

### 방식 3: 메타데이터 동시 생성

청크 경계 결정과 함께 검색 품질을 높이는 메타데이터를 동시에 생성한다:

```python
RICH_CHUNKING_PROMPT = """문서를 청크로 나누고 각 청크에 대한 메타데이터를 생성하세요.

문서: {document}

각 청크에 대해 다음을 제공하세요:
- text: 청크 내용
- summary: 1-2문장 요약
- keywords: 핵심 키워드 5개
- questions: 이 청크로 답할 수 있는 질문 3개
- chunk_type: "definition"|"explanation"|"example"|"comparison"|"procedure"

JSON 배열로 반환:"""


def agentic_chunking_with_metadata(document: str) -> list[dict]:
    """청킹과 메타데이터 동시 생성."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": RICH_CHUNKING_PROMPT.format(document=document),
        }],
        response_format={"type": "json_object"},
        temperature=0.2,
    )
    result = json.loads(response.choices[0].message.content)
    return result.get("chunks", [])
```

---

## 비용 관리

에이전트 청킹의 가장 큰 제약은 비용이다.

### 비용 추정

```python
# 대략적인 비용 추정 (GPT-4o 기준, 2024년)
def estimate_agentic_chunking_cost(
    documents: list[str],
    avg_doc_tokens: int = 2000,
    cost_per_1k_input: float = 0.005,
    cost_per_1k_output: float = 0.015,
) -> dict:
    total_input = len(documents) * avg_doc_tokens
    total_output = len(documents) * 500  # 청크 결정 + 메타데이터

    return {
        "input_cost": total_input / 1000 * cost_per_1k_input,
        "output_cost": total_output / 1000 * cost_per_1k_output,
        "total_cost": (
            total_input / 1000 * cost_per_1k_input
            + total_output / 1000 * cost_per_1k_output
        ),
        "documents": len(documents),
    }

# 예: 1000개 문서, 평균 2000 토큰
# -> 약 $25-40 (일회성 인덱싱 비용)
```

### 비용 절감 전략

1. **계층적 접근**: 먼저 재귀 분할로 초벌 청킹 -> 경계 후보만 에이전트로 검증
2. **소형 모델 활용**: GPT-4o 대신 GPT-4o-mini 또는 Claude Haiku로 결정
3. **캐싱**: 동일 문서의 재처리 방지
4. **선택적 적용**: 중요 문서에만 에이전트 청킹, 나머지는 의미적 청킹

```python
def selective_agentic_chunking(
    documents: list[str],
    importance_threshold: float = 0.8,
) -> list[list[str]]:
    """중요도가 높은 문서에만 에이전트 청킹 적용."""
    results = []
    for doc in documents:
        importance = estimate_document_importance(doc)  # 별도 분류기
        if importance >= importance_threshold:
            chunks = agentic_chunking_with_metadata(doc)
            results.append([c["text"] for c in chunks])
        else:
            results.append(semantic_chunking(doc))  # 빠른 대안
    return results
```

---

## 장단점

### 장점

- **최고 품질**: 규칙/통계 기반 방법이 실패하는 복잡한 문서 구조 처리
- **문서 이해**: 비선형 구조, 표, 코드+설명 혼합 등 다양한 형식 대응
- **풍부한 메타데이터**: 청킹과 동시에 요약, 키워드, 예상 질문 생성 가능
- **적응성**: 문서 유형마다 다른 전략 자동 선택

### 단점

- **높은 비용**: 명제 단위 청킹보다도 비쌈 (문서당 $0.01-$0.10+)
- **낮은 처리량**: 대량 문서 인덱싱에 비현실적
- **일관성 부족**: LLM의 확률적 특성으로 같은 문서도 실행마다 결과가 다를 수 있음
- **디버깅 어려움**: 청크 경계 결정 이유를 추적하기 어려움

---

## 실무 적용 시나리오

에이전트 청킹이 실질적 가치를 제공하는 상황:

1. **고가치 전문 문서**: 법률 계약서, 의료 가이드라인, 특허 문서
2. **복잡한 기술 문서**: API 레퍼런스, 아키텍처 설계 문서
3. **비정형 혼합 문서**: 코드 + 설명 + 다이어그램이 섞인 문서
4. **소규모 고품질 RAG**: 문서 수 < 1000개이고 검색 정밀도가 최우선인 경우
5. **오프라인 인덱싱**: 실시간이 아닌 사전 배치 처리가 가능한 경우

---

## 관련 문서

- [[chunking-strategies]] - 전체 청킹 전략 비교
- [[propositional-chunking]] - LLM 활용 명제 단위 청킹
- [[semantic-chunking-strategies]] - 더 저렴한 의미 기반 청킹
- [[context-aware-chunking]] - 문서 구조를 활용한 청킹
- [[contextual-retrieval]] - Anthropic의 컨텍스트 보강 방식
- [[agentic-rag]] - 에이전트 기반 전체 RAG 파이프라인
- [[rag-indexing-pipeline]] - 인덱싱 파이프라인에서의 위치
