---
title: Dense Retrieval -- 임베딩 기반 의미적 검색
category: rag
page_type: concept
tags: [rag, dense-retrieval, embedding, semantic-search, vector-search]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Dense Retrieval -- 임베딩 기반 의미적 검색

쿼리와 문서를 동일한 벡터 공간에 임베딩한 뒤, 벡터 유사도로 의미적으로 관련 있는 문서를 찾는 신경망 기반 검색 기법.

## 정의

Dense Retrieval(밀집 검색)은 Transformer 인코더가 텍스트를 고차원 실수 벡터로 변환하고, 쿼리 벡터와 문서 벡터 사이의 코사인 유사도 또는 내적(dot product)을 계산하여 관련 문서를 찾는 방식이다. "dense"라는 이름은 벡터의 모든 차원에 0이 아닌 값이 채워진다는 점에서 [[sparse-retrieval-bm25|sparse retrieval]]과 대비된다. 2020년 Facebook의 DPR(Dense Passage Retrieval) 논문이 이 분야의 기점이며, 이후 Sentence-BERT, E5, GTE, BGE 등 다양한 임베딩 모델이 등장했다.

## 핵심 아키텍처: Bi-Encoder

Dense retrieval의 표준 구조는 bi-encoder(이중 인코더)다.

1. **쿼리 인코더**: 사용자 질의를 d차원 벡터로 변환
2. **문서 인코더**: 문서(또는 청크)를 동일 d차원 벡터로 변환
3. **유사도 계산**: cosine similarity 또는 dot product로 관련성 점수 산출

두 인코더는 독립적으로 동작하므로, 문서 벡터를 사전에 계산해 인덱스에 저장해두면 쿼리 시점에는 쿼리 인코딩 + 벡터 검색만 수행하면 된다. 이 구조 덕분에 수백만-수십억 건의 문서에서도 밀리초 단위 검색이 가능하다. 벡터 인덱싱에는 Faiss, ScaNN 같은 [[approximate-nearest-neighbor|ANN 라이브러리]]가 사용된다.

## Sparse Retrieval과의 비교

| 속성 | Dense Retrieval | [[sparse-retrieval-bm25|Sparse Retrieval (BM25)]] |
|------|----------------|------|
| 표현 방식 | 실수 벡터 (768-4096차원) | 어휘 크기 희소 벡터 |
| 매칭 원리 | 의미적 유사도 | 정확한 키워드 일치 |
| 동의어/패러프레이즈 | 자연스럽게 처리 | 처리 불가 |
| 전문용어/고유명사 | 학습 데이터에 없으면 취약 | 정확 일치로 강력 |
| 인덱싱 비용 | 높음 (GPU 인코딩 필요) | 낮음 (역색인 구성) |
| 해석 가능성 | 낮음 (블랙박스) | 높음 (TF-IDF 점수 확인 가능) |

실무에서는 둘의 장점을 결합한 하이브리드 검색이 표준이다. [[contextual-retrieval|Contextual Retrieval]]은 청크에 문서 맥락을 주입해 dense + BM25 결합 시 실패율을 67% 감소시켰다.

## 학습 방식

Dense retrieval 모델의 핵심 학습 신호는 대조 학습(contrastive learning)이다.

- **Positive pair**: 쿼리 - 관련 문서
- **Negative pair**: 쿼리 - 비관련 문서 (hard negative가 중요)
- **손실 함수**: InfoNCE 또는 ranking loss 계열

Hard negative mining -- 벡터 공간에서 가깝지만 실제로는 관련 없는 문서를 학습에 활용 -- 이 모델 성능에 결정적 영향을 미친다. ANCE(Approximate Nearest Neighbor Negative Contrastive Estimation)는 ANN 인덱스 자체를 활용해 hard negative를 동적으로 채굴하는 기법이다.

2025-2026년에는 학습 패러다임이 더 발전했다. Query Embedding Alignment은 의미적으로 유사한 쿼리가 유사한 검색 결과를 반환하도록 정렬하고, Similarity Margin Consistency는 positive/negative 문서 간 유사도 마진을 일관되게 유지한다. Sparse Autoencoder Decomposition은 dense 임베딩을 해석 가능한 희소 개념 집합으로 분해하는 시도로, dense retrieval의 블랙박스 한계를 극복하려는 방향이다.

## 주요 모델 계보

| 모델 | 특징 |
|------|------|
| DPR (2020) | BERT 기반, 최초의 대규모 dense retrieval |
| Sentence-BERT (2019) | 시맨틱 유사도에 특화된 문장 임베딩 |
| ColBERT (2020) | 토큰 레벨 late interaction, 정밀도 향상 |
| E5 / GTE / BGE (2023-2024) | 대규모 대조학습 + 지시문 기반 범용 임베딩 |
| Voyage-3 / voyage-context-3 (2025-2026) | 문서 맥락 반영 임베딩, contextual embedding |

## RAG 파이프라인에서의 위치

전형적인 RAG 파이프라인에서 dense retrieval은 1단계 검색(first-stage retrieval)을 담당한다.

1. **1단계**: Dense retrieval (+ BM25 하이브리드)로 후보 50-200건 확보
2. **2단계**: [[reranker-cross-encoder|Cross-encoder reranker]]로 상위 3-10건 재순위
3. **3단계**: LLM에 전달하여 답변 생성

[[agentic-rag|Agentic RAG]]에서는 에이전트가 dense retrieval 도구를 반복 호출하며 multi-hop 탐색을 수행한다. [[graphrag-in-production|GraphRAG]]는 지식 그래프와 dense retrieval을 결합해 엔티티 간 관계 추론까지 지원한다.

## 한계와 도전

- **도메인 이동**: 범용 모델이 특정 도메인(법률, 의학)에서 성능 저하. 도메인 적응 파인튜닝 필요
- **임베딩 차원의 저주**: 고차원에서 모든 벡터 간 거리가 비슷해지는 현상. Manifold-aware retrieval은 KNN 그래프 최단 경로 거리로 이를 완화하며 OOD recall을 최대 26% 향상
- **인덱스 갱신 비용**: 문서 추가/삭제 시 재인코딩 필요. streaming indexing 기법으로 대응
- **해석 가능성 부족**: 왜 특정 문서가 검색됐는지 설명 어려움. Concept-Level Sparse Retrieval(CL-SR)이 대안으로 연구 중

## 참고 자료

- [Dense Retrieval Models: Principles & Advances -- EmergentMind](https://www.emergentmind.com/topics/dense-retrieval-models-drms)
- [Decoding Strategies in Large Language Models -- Hugging Face Blog](https://huggingface.co/blog/mlabonne/decoding-strategies)
- [Dense vs Sparse Retrieval: Mastering FAISS, BM25, and Hybrid Search -- DEV Community](https://dev.to/qvfagundes/dense-vs-sparse-retrieval-mastering-faiss-bm25-and-hybrid-search-4kb1)

## 관련 페이지

- [[sparse-retrieval-bm25|Sparse Retrieval (BM25)]] -- 키워드 기반 검색과의 비교
- [[reranker-cross-encoder|Reranker / Cross-Encoder]] -- 2단계 재순위 모델
- [[approximate-nearest-neighbor|Approximate Nearest Neighbor]] -- 벡터 인덱싱 알고리즘
- [[contextual-retrieval|Contextual Retrieval]] -- 문서 맥락 주입 기법
- [[agentic-rag|Agentic RAG]] -- 에이전트 기반 다단계 RAG
- [[graphrag-in-production|GraphRAG]] -- 지식 그래프 + RAG
