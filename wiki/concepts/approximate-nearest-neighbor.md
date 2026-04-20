---
title: Approximate Nearest Neighbor (ANN) -- HNSW, IVF, LSH
category: concepts
page_type: concept
tags: [concepts, ann, hnsw, ivf, lsh, vector-search, vector-database]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Approximate Nearest Neighbor (ANN) -- HNSW, IVF, LSH

고차원 벡터 공간에서 쿼리 벡터와 가장 가까운 이웃을 정확하게가 아닌 근사적으로 찾아, 검색 속도를 수 배에서 수천 배 향상시키는 알고리즘 군.

## 정의

Approximate Nearest Neighbor(ANN) 검색은 N개의 벡터 중 쿼리 벡터와 가장 유사한 k개를 찾는 문제에서, 100% 정확한 결과 대신 높은 확률로 정확한 결과를 반환하는 대가로 검색 속도를 극적으로 향상시키는 기법이다. 정확한 최근접 이웃 탐색(Exact NN)은 O(Nd) 시간 복잡도로 대규모 데이터셋에서 비현실적이므로, [[dense-retrieval|dense retrieval]], 추천 시스템, 이미지 검색 등 벡터 기반 응용에서 ANN은 필수 구성요소다.

## 왜 Exact NN이 불가능한가

1억 개의 768차원 벡터가 있다면, 쿼리 하나에 1억 번의 거리 계산이 필요하다. 이를 브루트포스라 하며, 단일 쿼리에 수 초-수십 초가 소요된다. 실시간 서비스에서는 10ms 이하의 지연시간이 요구되므로, 정확도를 약간 희생하더라도(recall@10 기준 95-99%) 속도를 확보하는 ANN이 표준이다.

고차원에서는 "차원의 저주"도 작용한다. 차원이 높아질수록 모든 벡터 간 거리가 비슷해져 tree 기반 정확 탐색(KD-Tree 등)의 효율이 급격히 떨어진다. ANN 알고리즘은 이 한계를 탐색 구조 설계로 우회한다.

## 주요 알고리즘

### HNSW (Hierarchical Navigable Small World)

그래프 기반 ANN의 대표. 2018년 Malkov & Yashunin이 제안했으며, 현재 가장 널리 사용되는 ANN 알고리즘이다.

**작동 원리**:
1. 다계층 그래프 구성. 상위 레이어는 노드가 적고 장거리 연결, 하위 레이어는 노드가 많고 단거리 연결
2. 검색 시 최상위 레이어에서 시작해 greedy하게 쿼리에 가까운 노드로 이동
3. 하위 레이어로 내려가며 점점 정밀한 탐색 수행
4. 최하위 레이어에서 최종 이웃 후보 확보

**핵심 파라미터**:
- `M`: 각 노드의 최대 연결 수. 높을수록 recall 증가, 메모리 증가
- `ef_construction`: 인덱스 구축 시 탐색 폭. 높을수록 인덱스 품질 향상, 구축 시간 증가
- `ef_search`: 검색 시 탐색 폭. 높을수록 recall 증가, 검색 시간 증가

**특성**: 검색 시간이 데이터 크기에 대해 O(log N)으로 스케일. recall이 매우 높아 정밀도 중심 애플리케이션에 적합. 단, 메모리 사용량이 크고(원본 벡터 + 그래프 구조), 인덱스 구축 시간이 길다.

### IVF (Inverted File Index)

파티션 기반 ANN. 데이터를 군집화한 뒤 쿼리와 가까운 군집만 탐색하는 방식이다.

**작동 원리**:
1. k-means로 데이터를 nlist개의 클러스터(Voronoi cell)로 분할
2. 각 클러스터에 소속 벡터를 역색인 형태로 저장
3. 검색 시 쿼리와 가장 가까운 nprobe개 클러스터만 탐색
4. 탐색한 클러스터 내에서 정확 거리 계산

**핵심 파라미터**:
- `nlist`: 클러스터 수. sqrt(N) ~ 4*sqrt(N) 권장
- `nprobe`: 검색 시 탐색할 클러스터 수. nprobe/nlist 비율이 recall-speed 트레이드오프 결정

**특성**: 구현이 단순하고 인덱스 구축이 HNSW보다 빠름. 데이터 분포에 자연스러운 클러스터가 있으면 효율적. PQ(Product Quantization)와 결합하면 메모리 절감 효과가 크다(IVF-PQ).

### LSH (Locality-Sensitive Hashing)

해싱 기반 ANN. 유사한 벡터가 같은 해시 버킷에 높은 확률로 배정되도록 설계된 해시 함수군을 사용한다.

**작동 원리**:
1. 랜덤 하이퍼플레인(또는 랜덤 프로젝션)으로 공간을 분할
2. 각 벡터에 비트 문자열 해시 코드 할당
3. 검색 시 쿼리의 해시 코드와 동일한 버킷의 벡터만 후보로 평가
4. 여러 해시 테이블을 사용해 recall 향상

**특성**: 이론적 보장이 명확(확률적 recall 하한). 하지만 고차원에서 높은 recall을 달성하려면 많은 해시 테이블이 필요하여 메모리와 검색 시간이 증가한다. HNSW/IVF 대비 실무 성능이 떨어져 최근에는 단독 사용이 줄고 있다.

## 비교 요약

| 속성 | HNSW | IVF | LSH |
|------|------|-----|-----|
| 구조 | 다계층 그래프 | 파티션 (k-means) | 해시 테이블 |
| 검색 복잡도 | O(log N) | O(nprobe * N/nlist) | O(L * B) |
| Recall | 매우 높음 (>98%) | 높음 (파라미터 의존) | 중간 (테이블 수 의존) |
| 메모리 | 높음 | 중간 (PQ 결합 시 낮음) | 중간-높음 |
| 인덱스 구축 | 느림 | 중간 | 빠름 |
| 동적 갱신 | 가능 (삽입 O(log N)) | 재군집화 필요 | 해시 재계산 |
| 주요 구현체 | Faiss, hnswlib, pgvector | Faiss, Milvus | Annoy, Falconn |

## Product Quantization (PQ)

PQ는 ANN 알고리즘이라기보다 벡터 압축 기법이며, IVF/HNSW와 결합하여 메모리를 절감한다.

1. 원본 벡터를 m개의 서브벡터로 분할
2. 각 서브벡터를 별도의 코드북(256개 중심점)으로 양자화
3. 768차원 float32 벡터(3KB)를 m바이트(예: 96B)로 압축

IVF-PQ는 Faiss의 대표 인덱스이며, 10억 벡터 규모에서도 단일 머신으로 운영 가능한 수준의 메모리 효율을 달성한다.

## RAG / 벡터 검색에서의 역할

[[dense-retrieval|Dense retrieval]]은 ANN 없이는 대규모 서비스가 불가능하다. 실무 선택 기준:

- **정밀도 우선** (의료, 법률 검색): HNSW, ef_search 높게 설정
- **비용/메모리 우선** (10억+ 벡터): IVF-PQ 또는 ScaNN
- **실시간 갱신 빈번**: HNSW (삽입 지원) 또는 streaming index

[[agentic-rag|Agentic RAG]]에서 에이전트가 반복 검색을 수행할 때, ANN 인덱스의 지연시간이 루프 전체 성능을 좌우한다. [[graphrag-in-production|GraphRAG]]는 엔티티 임베딩을 ANN으로 검색한 뒤 그래프 탐색으로 확장하는 패턴을 사용한다.

## 벤치마크

[ANN Benchmarks](http://ann-benchmarks.com/)는 다양한 데이터셋과 차원에서 ANN 알고리즘의 recall-QPS(queries per second) 트레이드오프를 비교하는 표준 벤치마크다. 2026년 기준 HNSW 계열(hnswlib, Faiss HNSW)이 recall@10 > 0.95 구간에서 최상위 QPS를 기록하고 있다.

## 참고 자료

- [Hierarchical Navigable Small Worlds (HNSW) -- Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/)
- [ANN Search Explained: IVF vs HNSW vs PQ -- TiDB](https://www.pingcap.com/article/approximate-nearest-neighbor-ann-search-explained-ivf-vs-hnsw-vs-pq/)
- [ANN Algorithm Overview: LSH -- APXML](https://apxml.com/courses/vector-databases-semantic-search/chapter-3-approximate-nearest-neighbor-search/ann-algorithm-lsh)

## 관련 페이지

- [[dense-retrieval|Dense Retrieval]] -- ANN이 지탱하는 1단계 의미적 검색
- [[reranker-cross-encoder|Reranker / Cross-Encoder]] -- ANN 검색 후 정밀 재순위
- [[agentic-rag|Agentic RAG]] -- 반복 검색 루프에서 ANN 지연시간이 핵심
- [[graphrag-in-production|GraphRAG]] -- 엔티티 임베딩의 ANN 검색 + 그래프 탐색
- [[contextual-retrieval|Contextual Retrieval]] -- 임베딩 품질이 ANN recall에 직접 영향


## 관련 문서

- [[milvus]] -- Milvus (분산 벡터 데이터베이스)
