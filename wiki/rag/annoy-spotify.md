---
title: Annoy - Spotify ANN 라이브러리
category: rag
page_type: entity
project: Annoy
tags: [ann, vector-index, spotify, random-projection, tree-index, approximate-nearest-neighbor, memory-mapped]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# Annoy - Spotify ANN 라이브러리

Annoy(Approximate Nearest Neighbors Oh Yeah)는 Spotify가 개발한 오픈소스 [[approximate-nearest-neighbor]] 검색 라이브러리다. 2013년 Erik Bernhardsson이 Spotify의 음악 추천 시스템을 위해 개발했으며, 현재 GitHub에서 1만 스타 이상을 보유한 성숙한 프로젝트다. 메모리 매핑(mmap) 방식의 디스크 기반 인덱스와 C++ 구현 기반의 빠른 읽기 성능이 특징이다.

## 아키텍처 개요

```mermaid
flowchart TD
    subgraph 구축["인덱스 구축"]
        벡터["벡터 컬렉션"]
        투영["무작위 초평면 선택\n(random hyperplane)"]
        분할["이진 공간 분할\n(Binary Space Partitioning)"]
        트리["이진 트리 생성\n(n_trees개 독립 트리)"]
        벡터 --> 투영 --> 분할 --> 트리
    end
    
    subgraph 검색["검색"]
        쿼리["쿼리 벡터"]
        우선순위["우선순위 큐\n(모든 트리 동시 탐색)"]
        후보["후보 풀 수집\n(search_k 크기)"]
        정렬["정확한 거리 계산\n후 K-NN 반환"]
        쿼리 --> 우선순위 --> 후보 --> 정렬
    end
```

## 핵심 메커니즘: 무작위 투영 트리

**인덱스 구축 절차:**
1. 무작위 초평면(hyperplane)을 선택하여 벡터 공간을 두 반공간으로 분할
2. 각 절반에 대해 재귀적으로 동일 과정 반복 (트리 깊이 = $O(\log n)$)
3. 리프 노드에는 K개 이하의 벡터 ID 저장
4. 이 과정을 `n_trees`번 반복하여 독립적인 트리 앙상블 생성

**검색 절차:**
1. 모든 트리에서 동시에 쿼리 위치를 확인
2. 우선순위 큐를 사용하여 경계 노드도 탐색 (greedy가 아닌 best-first)
3. `search_k`개의 후보를 수집한 뒤 실제 거리 계산으로 K-NN 반환

## 주요 특성

| 항목 | 특성 |
|------|------|
| 구현 언어 | C++ (Python 바인딩 제공) |
| 지원 거리 | 유클리드(Euclidean), 코사인(Cosine), 맨하탄(Manhattan), 해밍(Hamming), 도트 프로덕트 |
| 메모리 방식 | 메모리 매핑(mmap) - 인덱스를 디스크에 저장, RAM 최소화 |
| 동시성 | 다중 프로세스 읽기 지원, 쓰기 잠금 |
| 인덱스 수정 | 불가 (구축 후 읽기 전용) |
| 삭제 | 미지원 |

## 핵심 파라미터

| 파라미터 | 의미 | 기본값 | 영향 |
|----------|------|--------|------|
| `n_trees` | 독립 트리 수 | 10 | 클수록 정확도 증가, 메모리/구축 시간 증가 |
| `search_k` | 검색 시 검사할 노드 수 | `n * n_trees` | 클수록 정확도 증가, 검색 시간 증가 |
| `metric` | 거리 메트릭 | `angular` | 태스크에 따라 선택 |

`search_k`는 런타임에 조정 가능하여 정확도-속도 트레이드오프를 유연하게 제어할 수 있다.

## 사용 예시

```python
from annoy import AnnoyIndex

# 인덱스 생성 (차원, 거리 메트릭)
t = AnnoyIndex(128, 'angular')

# 벡터 추가 (ID, 벡터)
for i, vec in enumerate(vectors):
    t.add_item(i, vec)

# 인덱스 구축 (n_trees)
t.build(50)

# 디스크에 저장 (메모리 매핑)
t.save('music.ann')

# 나중에 로드 (메모리 매핑, 낮은 RAM 사용)
u = AnnoyIndex(128, 'angular')
u.load('music.ann')  # mmap으로 로드

# 검색 (ID 기준, K개, search_k)
neighbors = u.get_nns_by_item(0, 10, search_k=1000)
query_neighbors = u.get_nns_by_vector(query_vec, 10, search_k=1000)

# 거리도 함께 반환
ids, dists = u.get_nns_by_vector(query_vec, 10, include_distances=True)
```

## 장점과 한계

**장점:**
- 메모리 매핑으로 인덱스를 디스크에 유지 가능 - 대용량 데이터에서 RAM 절약
- 다중 프로세스 간 인덱스 공유 가능 (파일 기반)
- 설치와 사용이 매우 단순
- 쓰기 잠금 없이 여러 프로세스에서 동시 읽기 가능

**한계:**
- 인덱스 구축 후 벡터 추가/삭제 불가 (정적 인덱스)
- [[hnsw-graph-index|HNSW]]나 [[scann-google-search|ScaNN]] 대비 재현율이 낮은 경우 있음
- 고차원(>1000)에서 성능 저하
- GPU 가속 미지원

## Spotify에서의 활용

Spotify는 Annoy를 음악 추천 시스템의 핵심 구성 요소로 사용했다. 수천만 개의 곡 임베딩에서 유사한 곡을 실시간으로 검색하는 데 활용되었으며, 여러 프로세스가 같은 인덱스 파일을 공유하는 방식으로 서버 메모리를 효율화했다.

> "It creates a search index in a file that can be memory-mapped and easily used by many processes."
> - Annoy 공식 문서

## 경쟁 라이브러리와 비교

| 라이브러리 | 알고리즘 | 메모리 효율 | 재현율 | 동적 업데이트 |
|-----------|---------|-----------|--------|-------------|
| Annoy | 랜덤 투영 트리 | 매우 좋음 (mmap) | 중간 | 불가 |
| [[hnsw-graph-index|HNSW (FAISS)]] | 그래프 | 보통 | 높음 | 제한적 |
| [[scann-google-search|ScaNN]] | 양자화 + 트리 | 좋음 | 매우 높음 | 불가 |
| [[diskann-microsoft|DiskANN]] | 그래프 + SSD | 매우 좋음 | 높음 | 가능 |

## 현재 상태

Spotify는 이후 더 고성능의 자체 ANN 솔루션으로 전환했으나, Annoy는 오픈소스로 계속 유지되고 있다. 단순성과 메모리 효율 덕분에 프로토타입 개발, 교육 목적, 소규모 프로덕션 시스템에서 여전히 널리 사용된다.

## 관련 문서

- [[approximate-nearest-neighbor]] - ANN 검색 전반 개요
- [[hnsw-graph-index]] - 그래프 기반 ANN (더 높은 재현율)
- [[scann-google-search]] - Google의 정량화 ANN
- [[diskann-microsoft]] - 디스크 기반 십억 규모 ANN
- [[ivf-pq-vector-index]] - 메모리 효율 중심 인덱스
- [[vector-db-comparison]] - 벡터 DB 시스템 비교
