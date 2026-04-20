---
title: Reranker / Cross-Encoder -- 2단계 재순위 모델
category: rag
page_type: concept
tags: [rag, reranker, cross-encoder, two-stage-retrieval, information-retrieval]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Reranker / Cross-Encoder -- 2단계 재순위 모델

1단계 검색으로 확보한 후보 문서를 쿼리-문서 쌍으로 동시에 입력받아 정밀한 관련성 점수를 산출하고, 상위 문서만 선별하는 2단계 재순위 모델.

## 정의

Reranker(재순위 모델)는 쿼리와 문서를 하나의 시퀀스로 결합해 Transformer에 입력하고, 0-1 사이의 관련성 점수를 출력하는 모델이다. Cross-encoder라고도 부르는데, 쿼리와 문서가 인코더 내부에서 "교차(cross)" 어텐션을 수행하기 때문이다. [[dense-retrieval|Bi-encoder]](1단계)가 쿼리와 문서를 독립적으로 인코딩하는 것과 대조적으로, cross-encoder는 두 텍스트 간의 토큰 레벨 상호작용을 직접 모델링하므로 더 정밀한 관련성 판단이 가능하다.

## Bi-Encoder vs Cross-Encoder

```
Bi-Encoder (1단계):
  쿼리 -> [Encoder] -> vec_q \
                                 > cosine(vec_q, vec_d) = 점수
  문서 -> [Encoder] -> vec_d /

Cross-Encoder (2단계):
  [CLS] 쿼리 [SEP] 문서 [SEP] -> [Encoder] -> [CLS] 벡터 -> 선형 레이어 -> 점수
```

| 속성 | Bi-Encoder | Cross-Encoder |
|------|-----------|--------------|
| 입력 | 쿼리/문서 독립 인코딩 | 쿼리+문서 동시 입력 |
| 사전 계산 | 문서 벡터 사전 저장 가능 | 불가. 매 쿼리마다 추론 |
| 정밀도 | 정보 압축으로 손실 발생 | 토큰 레벨 상호작용으로 고정밀 |
| 속도 | 수백만 건 ms 단위 | 4천만 건 처리 시 50시간 이상 |
| 역할 | 후보 확보 (recall) | 재순위 (precision) |

핵심 트레이드오프: bi-encoder는 빠르지만 부정확하고, cross-encoder는 정확하지만 느리다. 따라서 실무에서는 둘을 결합한 2단계 파이프라인이 표준이다.

## 2단계 검색 파이프라인

```
[전체 코퍼스] --1단계 검색--> [후보 50-200건] --2단계 재순위--> [상위 3-10건] ---> [LLM]
              (bi-encoder/BM25)              (cross-encoder)
```

1. **1단계 (Retrieval)**: [[dense-retrieval|Dense retrieval]], [[sparse-retrieval-bm25|BM25]], 또는 하이브리드로 넓은 후보군 확보. 핵심 지표는 recall.
2. **2단계 (Reranking)**: Cross-encoder가 각 쿼리-후보 쌍을 개별 평가. 핵심 지표는 precision.
3. **LLM 전달**: 재순위 상위 문서만 컨텍스트에 포함. "lost in the middle" 문제 완화.

후보 수 설정이 중요하다. LLM 채팅 애플리케이션은 50건, 포괄적 웹 검색은 100-200건이 권장되며, 대부분의 경우 50-75건이 최적이다.

## 왜 Reranking이 필요한가

MIT 연구에 따르면, cross-encoder 재순위를 추가한 2단계 검색이 단일 벡터 검색 대비 여러 벤치마크에서 유의미하게 우수한 정확도를 보인다. 특히 RAG에서 재순위가 중요한 이유는 다음과 같다.

1. **Recall-Precision 딜레마**: 1단계에서 많은 문서를 검색하면 recall은 높지만, 모두 LLM에 넣으면 컨텍스트 윈도우가 낭비되고 "중간에서 길을 잃는" 현상이 발생한다. Reranking은 recall을 유지하면서 precision을 극대화한다.
2. **비용 절감**: 하이브리드 검색 + 재순위를 도입한 기업은 토큰 사용량과 비용을 25% 절감했다는 보고가 있다.
3. **의미적 세밀함**: Bi-encoder는 문서 전체를 하나의 벡터로 압축하므로 세부 뉘앙스가 손실된다. Cross-encoder는 쿼리의 특정 키워드가 문서의 어떤 부분과 매칭되는지까지 포착한다.

## 주요 Reranking 모델 (2025-2026)

| 모델 | 특징 |
|------|------|
| Cohere Rerank 4 Pro | v3.5 대비 +170 ELO, 비즈니스/금융에서 +400 ELO |
| FlashRank | 경량 모델, 실시간/대용량 시나리오에 적합 |
| Jina Reranker v2 | 다국어 지원, 8192 토큰 컨텍스트 |
| BGE Reranker v2.5 | 오픈소스, MTEB 벤치마크 상위권 |
| NVIDIA NIM Reranking | 마이크로서비스 형태, GPU 최적화 |

모델 선택 시 고려사항: 정확도, 지원 언어, 컨텍스트 길이, 지연시간, 비용. 도메인별 성능 차이가 크므로 자체 평가 데이터셋으로 벤치마크하는 것이 필수다.

## Late Interaction: 중간 지대

ColBERT로 대표되는 late interaction 모델은 bi-encoder와 cross-encoder의 중간 지대를 차지한다.

- 쿼리와 문서를 독립적으로 인코딩하되, 최종 점수 계산 시 토큰 레벨 유사도를 사용
- 문서 토큰 벡터를 사전 저장할 수 있어 cross-encoder보다 빠름
- Bi-encoder보다 정밀하지만 cross-encoder만큼은 아님
- 1.5단계 검색 또는 가벼운 재순위 용도로 활용

## RAG 파이프라인에서의 연결

[[contextual-retrieval|Contextual Retrieval]] + BM25 + reranking 조합은 Anthropic 벤치마크에서 검색 실패율을 67% 감소시켰다. [[agentic-rag|Agentic RAG]]에서는 에이전트가 검색 결과의 품질을 자체 평가하고, 불충분하면 재검색하는 루프를 수행하는데 reranker 점수가 이 판단 기준으로 활용된다. [[graphrag-in-production|GraphRAG]]는 그래프 탐색 결과와 벡터 검색 결과를 reranker로 통합 순위를 매기는 패턴이 늘고 있다.

## 한계

- **지연시간**: 후보 수에 비례해 추론 시간 증가. 실시간 서비스에서는 후보 수를 제한하거나 경량 모델 사용
- **비용**: API 기반 reranker(Cohere 등)는 호출당 과금. 오픈소스 모델 자체 호스팅이 대안
- **컨텍스트 길이**: 긴 문서는 잘려서 입력됨. 청킹 전략과 reranker 컨텍스트 길이의 정합이 중요
- **도메인 편향**: 범용 reranker가 특정 도메인에서 오히려 성능 저하를 일으킬 수 있음

## 참고 자료

- [Rerankers and Two-Stage Retrieval -- Pinecone](https://www.pinecone.io/learn/series/rag/rerankers/)
- [Reranking and Two-Stage Retrieval: Precision When It Matters Most -- DEV Community](https://dev.to/qvfagundes/reranking-and-two-stage-retrieval-precision-when-it-matters-most-3j)
- [Ultimate Guide to Choosing the Best Reranking Model in 2026 -- ZeroEntropy](https://www.zeroentropy.dev/articles/ultimate-guide-to-choosing-the-best-reranking-model-in-2025)

## 관련 페이지

- [[dense-retrieval|Dense Retrieval]] -- 1단계 임베딩 기반 검색
- [[sparse-retrieval-bm25|Sparse Retrieval (BM25)]] -- 1단계 키워드 기반 검색
- [[contextual-retrieval|Contextual Retrieval]] -- reranking과 결합해 실패율 67% 감소
- [[agentic-rag|Agentic RAG]] -- reranker 점수를 재검색 판단에 활용
- [[graphrag-in-production|GraphRAG]] -- 그래프 + 벡터 결과의 통합 순위
