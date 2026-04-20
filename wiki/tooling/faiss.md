---
title: FAISS (Facebook AI Similarity Search)
category: tooling
page_type: entity
project: FAISS
tags: [faiss, vector-search, similarity-search, meta, ann, gpu, embedding]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# FAISS

Meta(구 Facebook)의 Fundamental AI Research 그룹이 개발한 고성능 벡터 유사도 검색 및 클러스터링 라이브러리. 수십억 개 규모의 고차원 벡터에서 효율적인 근사 최근접 이웃(ANN) 검색을 수행한다. RAG 파이프라인의 검색 백엔드로 널리 사용된다.

## 개요

FAISS(Facebook AI Similarity Search)는 대규모 밀집 벡터 집합에서 유사한 벡터를 빠르게 찾는 문제를 해결한다. C++로 작성된 코어 엔진에 Python/NumPy 래퍼를 제공하며, CPU와 GPU(CUDA, AMD ROCm) 모두에서 동작한다. RAM에 맞지 않는 수십억 개의 벡터도 처리할 수 있으며, 원본 벡터를 저장하지 않는 압축 표현 기반 검색도 지원한다. [[chroma-db|ChromaDB]] 같은 벡터 데이터베이스의 내부 인덱싱 엔진으로도 활용된다.

## 핵심 개념

### 거리 메트릭

FAISS는 두 가지 기본 거리 메트릭을 지원한다:

- **L2 (유클리드 거리)**: 벡터 간 기하학적 거리. 일반적인 유사도 검색에 사용
- **내적 (Inner Product)**: 코사인 유사도와 관련. 정규화된 벡터에서 코사인 유사도와 동일

### 인덱스 유형

FAISS의 핵심 설계는 다양한 인덱스 구조를 통해 정확도-속도-메모리 간 트레이드오프를 제공하는 것이다.

| 인덱스 | 유형 | 특징 |
|--------|------|------|
| IndexFlatL2 | 정확(brute-force) | 가장 정확하지만 느림. 기준선 역할 |
| IndexIVFFlat | 역인덱스 기반 | 클러스터링으로 검색 범위 축소 |
| IndexIVFPQ | 역인덱스 + 양자화 | 메모리 효율적. 대규모 데이터셋용 |
| IndexHNSW | 그래프 기반 | 높은 리콜, 빠른 검색. 메모리 소비 큼 |
| IndexNSG | 그래프 기반 | HNSW 대비 메모리 효율적 |
| IndexScalarQuantizer | 스칼라 양자화 | 벡터를 int8 등으로 압축 |

### ANN (Approximate Nearest Neighbor)

정확한 최근접 이웃 검색은 데이터 크기에 선형적으로 비용이 증가한다. FAISS의 핵심 가치는 정확도를 약간 희생하면서 검색 속도를 수십-수백 배 향상시키는 근사 검색(ANN) 알고리즘에 있다. HNSW(Hierarchical Navigable Small World)와 IVF(Inverted File Index)가 대표적이다.

### 양자화 (Product Quantization)

PQ(Product Quantization)는 고차원 벡터를 여러 하위 공간(subspace)으로 분할하고, 각 하위 공간의 벡터를 코드북의 가장 가까운 엔트리로 대체한다. 이를 통해 벡터당 메모리를 수십 바이트에서 수 바이트로 압축하면서도 유의미한 검색 품질을 유지한다.

## 사용법

### 설치

```bash
# CPU 버전
conda install -c pytorch faiss-cpu

# GPU 버전 (CUDA)
conda install -c pytorch faiss-gpu

# GPU + cuVS 가속
conda install -c pytorch faiss-gpu-cuvs
```

### 기본 검색 예제

```python
import faiss
import numpy as np

d = 128          # 벡터 차원
nb = 100000      # 데이터베이스 크기
nq = 10          # 쿼리 수

# 데이터 생성
xb = np.random.random((nb, d)).astype("float32")
xq = np.random.random((nq, d)).astype("float32")

# 인덱스 생성 및 검색
index = faiss.IndexFlatL2(d)
index.add(xb)
D, I = index.search(xq, k=5)  # 상위 5개
```

### GPU 활용

```python
res = faiss.StandardGpuResources()
gpu_index = faiss.index_cpu_to_gpu(res, 0, index)
D, I = gpu_index.search(xq, k=5)
```

## 성능 특성

### GPU 가속

FAISS GPU 구현은 고차원 벡터에 대한 정확 및 근사 최근접 이웃 검색에서 최고 수준의 성능을 제공한다. 단일 GPU에서 수백만 개 벡터의 밀리초 단위 검색이 가능하며, 다중 GPU 분산 처리도 지원한다.

### 확장성

- 수십억 개 벡터: 디스크 기반 인덱스와 메모리 매핑으로 RAM 초과 데이터 처리
- 다중 GPU: 인덱스를 여러 GPU에 분산하여 처리량 확대
- 샤딩: 데이터를 여러 인덱스로 분할하여 병렬 검색

## RAG 파이프라인에서의 역할

FAISS는 [[rag-pipeline|RAG(Retrieval-Augmented Generation)]] 파이프라인에서 검색 단계의 핵심 엔진으로 사용된다. 문서를 임베딩 모델로 벡터화한 후 FAISS 인덱스에 저장하고, 쿼리 시 유사한 문서 벡터를 빠르게 검색한다.

```
쿼리 --> 임베딩 --> FAISS 검색 --> 상위 k개 문서 --> LLM 생성
```

## 비교: FAISS vs 벡터 데이터베이스

| 항목 | FAISS | [[chroma-db|ChromaDB]] / Qdrant |
|------|-------|------|
| 유형 | 라이브러리 | 데이터베이스 |
| 메타데이터 필터링 | 미지원 (직접 구현 필요) | 내장 지원 |
| 영속성 | 인덱스 파일 수동 관리 | 자동 영속화 |
| 분산 처리 | GPU 멀티 샤딩 | 클라이언트-서버 아키텍처 |
| 적합한 상황 | 최대 성능, 커스터마이징 | 빠른 프로토타이핑, 관리 편의 |

## 관련 페이지

- [[chroma-db|ChromaDB]] -- FAISS를 내부적으로 활용할 수 있는 벡터 데이터베이스
- [[rag-pipeline|RAG 파이프라인]] -- FAISS가 검색 백엔드로 사용되는 맥락
- [[on-device-llm|온디바이스 LLM]] -- 로컬 RAG 파이프라인 구축 시 FAISS 활용
- [[huggingface-hub|Hugging Face Hub]] -- 임베딩 모델 소싱
