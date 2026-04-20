---
title: ChromaDB (오픈소스 임베딩 데이터베이스)
category: tooling
page_type: entity
project: ChromaDB
tags: [chromadb, vector-database, embedding, rag, search, open-source]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# ChromaDB

오픈소스 AI 데이터 인프라로, 벡터 검색, 하이브리드 검색, 전문 검색(full-text search)을 통합 제공하는 임베딩 데이터베이스. 직관적인 4-함수 API로 빠른 프로토타이핑이 가능하면서도 프로덕션 환경에서의 확장성을 갖추고 있다. 위키 내 8회 참조로 확인된 고빈도 엔티티다.

## 개요

ChromaDB(Chroma)는 "open-source data infrastructure for AI"를 표방하며, LLM 애플리케이션에 필요한 임베딩 저장과 검색을 단일 시스템으로 제공한다. Rust 코어 엔진(전체 코드의 67%) 위에 Python과 JavaScript 클라이언트를 제공하며, 로컬 인메모리 실행부터 클라이언트-서버 모드, Chroma Cloud 호스팅까지 다양한 배포 형태를 지원한다. Apache 2.0 라이선스로 공개되어 있으며, GitHub 스타 27.4K 이상의 활발한 커뮤니티를 보유한다.

## 핵심 API

ChromaDB의 설계 철학은 "4개의 함수로 시작"이다.

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("my_collection")

# 1. 데이터 추가
collection.add(
    documents=["문서 내용 1", "문서 내용 2"],
    metadatas=[{"source": "wiki"}, {"source": "paper"}],
    ids=["doc1", "doc2"]
)

# 2. 쿼리 (유사도 검색)
results = collection.query(
    query_texts=["검색할 내용"],
    n_results=5
)
```

자동 토큰화, 임베딩, 인덱싱을 내부적으로 처리하므로 사용자가 임베딩 파이프라인을 직접 구성할 필요가 없다. 물론 커스텀 임베딩을 직접 제공하는 것도 가능하다.

## 아키텍처

### 언어 구성

| 언어 | 비율 | 역할 |
|------|------|------|
| Rust | 67.0% | 핵심 엔진, 인덱싱, 검색 |
| Python | 16.9% | Python 클라이언트 |
| TypeScript | 7.5% | JavaScript 클라이언트 |
| Go | 5.3% | 서버 컴포넌트 |

### 검색 모드

- **벡터 검색(Semantic)**: 임베딩 기반 의미적 유사도 검색
- **하이브리드 검색**: 벡터 + 키워드 결합
- **전문 검색(Full-text)**: 키워드 기반 텍스트 매칭

### 배포 형태

| 모드 | 설명 | 적합한 상황 |
|------|------|------------|
| 인메모리 | 프로세스 내 실행, 영속화 없음 | 프로토타이핑, 테스트 |
| 영속 모드 | 로컬 디스크에 데이터 저장 | 단일 사용자 애플리케이션 |
| 클라이언트-서버 | HTTP API로 분리 실행 | 멀티 클라이언트, 프로덕션 |
| Chroma Cloud | 호스팅 서비스 | 관리 부담 최소화 |

## 메타데이터 필터링

ChromaDB는 메타데이터 기반 필터링을 내장 지원한다. 벡터 유사도 검색과 메타데이터 조건을 결합하여 정밀한 검색이 가능하다.

```python
results = collection.query(
    query_texts=["AI 안전성"],
    n_results=10,
    where={"source": "paper"},
    where_document={"$contains": "alignment"}
)
```

## RAG 파이프라인에서의 역할

ChromaDB는 [[rag-pipeline|RAG]] 파이프라인의 지식 저장소로 가장 많이 활용된다.

```
문서 --> 청킹 --> 임베딩 --> ChromaDB 저장
                                   |
쿼리 --> 임베딩 --> ChromaDB 검색 --> 상위 k개 --> LLM 컨텍스트
```

[[ollama|Ollama]]로 로컬 임베딩 모델을 실행하고, ChromaDB에 저장하여 완전 로컬 RAG 시스템을 구축하는 패턴이 인기 있다.

## FAISS와의 비교

| 항목 | ChromaDB | [[faiss|FAISS]] |
|------|----------|------|
| 유형 | 데이터베이스 | 라이브러리 |
| 임베딩 자동 생성 | 내장 지원 | 미지원 (직접 생성) |
| 메타데이터 필터링 | 네이티브 지원 | 미지원 |
| 영속성 | 자동 관리 | 수동 관리 |
| GPU 가속 | 제한적 | 강력한 CUDA 지원 |
| 적합한 상황 | 빠른 개발, 관리 편의 | 최대 성능, 대규모 커스터마이징 |

## 생태계 통합

- **[[langchain|LangChain]]**: 벡터 스토어 인터페이스로 직접 통합
- **[[langgraph|LangGraph]]**: 에이전트 메모리 스토어로 활용
- **[[ollama|Ollama]]**: 로컬 임베딩 모델 백엔드
- **[[huggingface-hub|Hugging Face Hub]]**: 임베딩 모델 소싱
- **[[pydantic-ai|Pydantic AI]]**: AI 에이전트의 RAG 백엔드

## 제한 사항

- 대규모(수십억 벡터) 환경에서는 [[faiss|FAISS]] 대비 성능이 부족할 수 있다
- GPU 가속이 FAISS만큼 강력하지 않다
- 분산 클러스터링은 Chroma Cloud 또는 별도 구성이 필요하다

## 관련 페이지

- [[faiss|FAISS]] -- Meta의 벡터 검색 라이브러리 (저수준 대안)
- [[rag-pipeline|RAG 파이프라인]] -- ChromaDB가 핵심 역할을 하는 아키텍처
- [[ollama|Ollama]] -- 로컬 RAG에서 임베딩 모델 제공
- [[huggingface-hub|Hugging Face Hub]] -- 임베딩 모델 생태계
- [[langchain|LangChain]] -- ChromaDB를 벡터 스토어로 통합하는 프레임워크
