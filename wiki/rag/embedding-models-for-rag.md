---
title: RAG용 임베딩 모델 비교 (Embedding Models for RAG)
category: rag
page_type: concept
tags: [embedding, sentence-transformers, bge, e5, voyage, mteb]
sources: [raw/2026-04-15-new-100-nodes-knowledge-source.md]
created: 2026-04-15
updated: 2026-04-15
---

# RAG용 임베딩 모델 비교 (Embedding Models for RAG)

## 개요

임베딩 모델(Embedding Model)은 텍스트를 고차원 벡터로 변환하여 의미적 유사도 검색을 가능하게 한다. RAG 파이프라인에서 청크와 쿼리를 같은 벡터 공간에 매핑하는 핵심 컴포넌트다. 모델 선택이 검색 품질의 천장을 결정한다.

## 주요 임베딩 모델

### SBERT (Sentence-BERT)

UKP Lab의 오픈 소스 라이브러리. BERT를 Siamese 네트워크 구조로 파인튜닝하여 문장 임베딩에 최적화.

- 대표 모델: `all-MiniLM-L6-v2`, `all-mpnet-base-v2`
- 차원: 384, 768
- 특징: 경량, 범용, 로컬 실행 가능
- 한계: 영어 중심, 최신 MTEB에서 중위권

### BGE-M3 (BAAI General Embedding)

BAAI(베이징 AI 연구소)의 다국어 임베딩 모델.

- **Multi-Linguality**: 100+ 언어 지원, 한국어 포함
- **Multi-Granularity**: 문장~8192 토큰 긴 문서까지
- **Multi-Functionality**: Dense, Sparse(BM25형), ColBERT 방식 통합
- 차원: 1024
- 오픈소스, 로컬 실행 가능

### E5-Mistral-7B

Microsoft가 Mistral-7B LLM을 임베딩 모델로 파인튜닝.

- LLM 기반 임베딩: 생성 모델의 표현력 활용
- 차원: 4096
- MTEB 상위권, 특히 긴 문서 검색 강점
- 연산 비용 높음 (7B 파라미터)
- Instruction-tuned: 쿼리 측에 태스크 프리픽스 사용 필요

### Voyage AI

Anthropic 투자를 받은 임베딩 전문 스타트업.

- `voyage-3`: 범용 고성능
- `voyage-code-3`: 코드 검색 특화
- `voyage-3-lite`: 경량/저비용 버전
- 도메인 특화 모델 라인업 (법률, 의료, 금융)
- API 전용 (로컬 실행 불가)

### Cohere Embed v3

Cohere의 멀티링구얼 임베딩 API.

- `embed-multilingual-v3.0`: 다국어 지원
- `embed-english-v3.0`: 영어 특화
- Input type 지시: `search_document` vs `search_query` 구분
- 차원: 1024 (Matryoshka 지원: 256까지 축소 가능)

## 모델 비교 표

| 모델 | 차원 | 최대 토큰 | 다국어 | 로컬 | 특징 |
|------|------|-----------|--------|------|------|
| all-MiniLM-L6-v2 | 384 | 512 | X | O | 경량/빠름 |
| BGE-M3 | 1024 | 8192 | O | O | 다기능 통합 |
| E5-Mistral-7B | 4096 | 32768 | 부분 | O (고사양) | LLM 기반 고성능 |
| Voyage-3 | 1024 | 32000 | 부분 | X | 고품질 API |
| Cohere Embed v3 | 1024 | 512 | O | X | Input type 지정 |
| OpenAI text-embedding-3-large | 3072 | 8191 | 부분 | X | Matryoshka 지원 |

## MTEB 리더보드

MTEB(Massive Text Embedding Benchmark)는 56개+ 태스크에서 임베딩 모델을 평가하는 표준 벤치마크.

- **분류(Classification)**, **클러스터링(Clustering)**, **검색(Retrieval)** 등 다양한 태스크
- 검색(Retrieval) 서브셋이 RAG 성능과 가장 관련
- 순위는 자주 바뀜 — 모델 선택 시 최신 리더보드 확인 필수

## Instruction-Tuned Embeddings

쿼리와 문서에 서로 다른 프리픽스(prefix)를 사용하여 태스크를 명시.

```python
# E5-Mistral 예시
query_prefix = "Instruct: Retrieve relevant passages\nQuery: "
query = query_prefix + "파이썬에서 리스트 정렬하는 방법은?"

# 문서 측은 프리픽스 없음
document = "Python 리스트는 sort() 메서드로 정렬할 수 있습니다..."
```

- 비대칭 검색(asymmetric retrieval): 쿼리와 문서 표현 분리
- 같은 프리픽스 사용 vs 다른 프리픽스 사용 → 성능 차이 발생

## Matryoshka Representation Learning (MRL)

러시아 마트료시카 인형처럼 하나의 임베딩 안에 다양한 차원 수준을 내포시키는 기법.

- 3072차원 임베딩을 256/512/1024 등으로 잘라도 의미 보존
- 검색 속도/비용 vs 품질 트레이드오프 동적 조절
- OpenAI text-embedding-3, Cohere v3 지원

## 도메인별 선택 가이드

| 도메인 | 권장 모델 |
|--------|-----------|
| 범용 한국어 | BGE-M3 |
| 코드 검색 | Voyage-code-3, CodeBERT 계열 |
| 법률/의료 | Voyage 도메인 특화 또는 파인튜닝 |
| 고성능 영어 | E5-Mistral-7B, Voyage-3 |
| 비용 최적화 | all-MiniLM-L6-v2, BGE-small |

## 관련 문서

- [[chunking-strategies]] - 임베딩 전 문서 분할
- [[colbert-late-interaction]] - 토큰 수준 임베딩 활용
- [[embedding-finetuning]] - 도메인 적응 파인튜닝
- [[hybrid-search-rrf]] - 밀집 임베딩 + 희소 검색 결합
- [[embedding-leaderboard-shakeup-2026]] - 최신 MTEB 동향
