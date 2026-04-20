---
title: HyDE (가상 문서 임베딩)
category: rag
page_type: concept
tags: [hyde, hypothetical-document-embedding, query-gap, dense-retrieval, rag]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# HyDE (가상 문서 임베딩)

HyDE(Hypothetical Document Embeddings)는 검색 쿼리를 직접 임베딩하는 대신, **LLM이 쿼리에 대한 가상의 답변 문서를 생성**하고 그 문서를 임베딩해 검색에 사용하는 기법이다. 2022년 카네기멜론대학교 연구팀이 제안했으며, 쿼리 벡터와 정답 문서 벡터 사이의 **분포 격차(query-document gap)**를 해소하는 데 효과적이다.

## 문제 정의: 쿼리-문서 임베딩 격차

밀집 검색(dense retrieval)에서 쿼리와 문서는 동일한 임베딩 공간에 매핑되지만, 실제로는 두 유형의 텍스트가 **언어적·구조적으로 매우 다르다**.

- 쿼리: "트랜스포머 어텐션 메커니즘이 RNN보다 나은 이유는?"
- 문서: "Self-attention은 시퀀스의 모든 위치에서 직접 의존성을 계산하므로..."

쿼리는 짧고 불완전하지만 문서는 길고 완결된 산문이다. 이 격차 때문에 쿼리 임베딩이 실제 관련 문서 임베딩에 충분히 가깝지 않을 수 있다.

## HyDE 동작 원리

```mermaid
flowchart LR
    Q[사용자 쿼리] --> LLM[LLM 가상 답변 생성]
    LLM --> HD[가상 문서\nhypothetical doc]
    HD --> EMB[임베딩 모델]
    EMB --> HV[가상 문서 벡터]
    HV --> VDB[벡터 DB 검색\nANN 쿼리]
    VDB --> TOP[상위-k 실제 문서]
    TOP --> GEN[최종 답변 생성]
```

1. **가상 문서 생성**: LLM에게 "이 질문에 답하는 문서를 작성하라"고 지시해 가상의 답변 단락을 생성한다. 실제로 정확한 답일 필요는 없으며, **답변처럼 보이는 텍스트**이면 충분하다.
2. **가상 문서 임베딩**: 생성된 가상 문서를 [[embedding-layers]]로 임베딩한다.
3. **실제 문서 검색**: 가상 문서 벡터로 벡터 DB를 검색해 실제 관련 문서를 가져온다.
4. **최종 생성**: 검색된 실제 문서를 컨텍스트로 사용해 최종 응답을 생성한다.

## 왜 효과적인가

```mermaid
flowchart TD
    subgraph 기존["기존 방식"]
        Q1[쿼리 벡터] -. 거리 멀음 .-> D1[문서 벡터]
    end
    subgraph hyde["HyDE"]
        Q2[쿼리] --> H2[가상 문서 벡터]
        H2 -. 거리 가까움 .-> D2[문서 벡터]
    end
```

가상 문서는 쿼리보다 길고 산문 형식이므로, 실제 코퍼스 문서와 **동일한 언어 분포**를 공유한다. 결과적으로 가상 문서 벡터가 관련 실제 문서 벡터와 더 가까운 임베딩 공간 위치에 놓이게 된다.

## [[query-transformation]]과의 관계

HyDE는 [[query-transformation]] 기법의 한 유형으로 분류된다. 다른 쿼리 변환 기법과 비교하면:

| 기법 | 변환 방향 | 핵심 아이디어 |
|------|----------|--------------|
| HyDE | 쿼리 -> 가상 문서 | 쿼리를 문서 공간으로 변환 |
| 쿼리 재작성 | 쿼리 -> 개선된 쿼리 | 더 명확한 쿼리로 변환 |
| 서브쿼리 분해 | 쿼리 -> 여러 서브쿼리 | 복잡한 질의를 단순화 |
| RAG Fusion | 쿼리 -> 다중 쿼리 | 여러 관점으로 검색 |

## [[embedding-layers]] 선택의 중요성

HyDE의 효과는 가상 문서를 임베딩하는 모델의 품질에 크게 의존한다. 동일한 임베딩 모델로 코퍼스 문서와 가상 문서를 임베딩해야 공간 일관성이 보장된다. 임베딩 모델 불일치(예: 코퍼스는 OpenAI Ada, 가상 문서는 Cohere)는 검색 품질을 오히려 저하시킨다.

## 구현 예시

```python
from openai import OpenAI

client = OpenAI()

def generate_hypothetical_doc(query: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "주어진 질문에 답하는 단락을 100단어 내외로 작성하라. 정확하지 않아도 된다."
            },
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content

def hyde_retrieve(query: str, embedder, vector_db, k: int = 5):
    hyp_doc = generate_hypothetical_doc(query)
    hyp_vec = embedder.embed(hyp_doc)
    results = vector_db.search(hyp_vec, k=k)
    return results
```

## 한계와 주의사항

- **LLM 할루시네이션 전파**: 가상 문서에 잘못된 사실이 포함되더라도 검색 단계에서는 문제가 없다. 다만 가상 문서에 사용된 특정 오류 용어가 검색 편향을 유발할 수 있다.
- **레이턴시 증가**: 가상 문서 생성에 LLM 추론 1회가 추가된다. 레이턴시 민감 서비스에서는 캐싱이나 경량 모델로 대응해야 한다.
- **짧은 쿼리에 효과적**: 단어 몇 개로 구성된 짧은 쿼리일수록 HyDE의 효과가 두드러진다. 이미 상세한 자연어 쿼리라면 개선 폭이 작을 수 있다.
- **도메인 의존성**: 가상 문서 생성에 사용하는 LLM이 해당 도메인 지식을 충분히 보유해야 한다. 극히 전문적인 기술 도메인에서는 가상 문서 품질이 저하될 수 있다.

## 실무 적용 포인트

- 제로샷 검색(fine-tuning 없이 바로 사용)에서 초기 베이스라인 개선에 유효
- Embedding API를 직접 사용하는 환경에서 파인튜닝 없이 검색 품질 향상 가능
- BEIR, MS MARCO 등 다양한 도메인 벤치마크에서 표준 쿼리 임베딩 대비 일관된 향상 보고

## 관련 문서

- [[query-transformation]] - HyDE가 속하는 쿼리 변환 기법 범주
- [[embedding-layers]] - 가상 문서를 임베딩하는 핵심 컴포넌트
- [[rag-pipeline]] - HyDE가 삽입되는 전체 RAG 파이프라인
- [[rag-fusion]] - 다중 쿼리로 검색을 확장하는 상호 보완적 기법
