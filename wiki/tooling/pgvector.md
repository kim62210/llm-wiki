---
title: pgvector (PostgreSQL 벡터 확장)
category: tooling
page_type: entity
project: pgvector
tags: [pgvector, postgresql, vector-database, embedding, rag, sql, open-source]
sources: [raw/2026-04-16-topic-queue-500.md]
created: 2026-04-16
updated: 2026-04-16
---

# pgvector

PostgreSQL에 벡터 저장 및 유사도 검색 기능을 추가하는 오픈소스 확장. 기존 PostgreSQL 인프라에서 별도의 벡터 데이터베이스 없이 임베딩 벡터를 관리할 수 있게 한다. Supabase, Neon, AWS RDS, Azure Database for PostgreSQL 등 주요 관리형 PostgreSQL 서비스가 pgvector를 기본 지원한다.

## 개요

| 항목 | 내용 |
|---|---|
| 이름 | pgvector |
| 유형 | PostgreSQL 확장(Extension) |
| 라이선스 | PostgreSQL License |
| 저장소 | github.com/pgvector/pgvector |
| 코어 언어 | C |
| 지원 거리 메트릭 | L2(유클리드), 코사인, 내적, L1(맨해튼), 해밍, 잭카드 |
| 지원 인덱스 | IVFFlat, HNSW |
| 최대 차원 | 16,000 (HNSW), 2,000 (IVFFlat) |

## 설치와 기본 사용법

```sql
-- 확장 활성화
CREATE EXTENSION IF NOT EXISTS vector;

-- 벡터 컬럼을 포함한 테이블
CREATE TABLE documents (
    id     BIGSERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536)  -- OpenAI text-embedding-3-small 차원
);

-- 유사도 검색 (코사인 거리)
SELECT content, 1 - (embedding <=> '[0.1, 0.2, ...]') AS similarity
FROM documents
ORDER BY embedding <=> '[0.1, 0.2, ...]'
LIMIT 5;
```

### 거리 연산자

| 연산자 | 거리 유형 | 용도 |
|---|---|---|
| `<->` | L2 (유클리드) | 기하학적 거리 기반 검색 |
| `<=>` | 코사인 | 방향 기반 텍스트 유사도 |
| `<#>` | 음의 내적 | 정규화된 벡터의 코사인과 동일 |
| `<+>` | L1 (맨해튼) | 희소 벡터에 효율적 |

## 인덱스

### HNSW (권장)

```sql
-- HNSW 인덱스 생성 (코사인 거리)
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- 검색 시 ef_search 파라미터로 정확도-속도 트레이드오프 조정
SET hnsw.ef_search = 100;
```

### IVFFlat

```sql
-- IVFFlat 인덱스 (데이터 삽입 후에 생성하는 것이 권장됨)
CREATE INDEX ON documents USING ivfflat (embedding vector_l2_ops)
WITH (lists = 100);
```

| 인덱스 | 빌드 속도 | 검색 속도 | 메모리 | 적합 상황 |
|---|---|---|---|---|
| HNSW | 느림 | 빠름 | 많음 | 프로덕션, 고성능 검색 |
| IVFFlat | 빠름 | 중간 | 적음 | 초기 프로토타입, 메모리 제약 |

## 아키텍처: 단일 DB 스택

pgvector의 가장 큰 강점은 별도 벡터 데이터베이스를 추가하지 않고 **기존 PostgreSQL 스택에서 벡터 검색을 통합**한다는 점이다.

```mermaid
flowchart LR
    App[애플리케이션] --> PG[(PostgreSQL\n+ pgvector)]
    subgraph PG ["PostgreSQL + pgvector"]
        Rel[관계형 테이블\n사용자, 제품, 문서...]
        Vec[벡터 컬럼\n임베딩]
        Idx[HNSW 인덱스]
        Vec --> Idx
    end
    PG --> SQL[SQL 쿼리로\n관계형 + 벡터 검색 결합]
```

## 관계형 + 벡터 결합 쿼리

pgvector의 핵심 가치는 SQL 조인과 벡터 검색을 단일 쿼리로 결합하는 것이다.

```sql
-- 특정 사용자의 즐겨찾기 카테고리 문서만 유사도 검색
SELECT d.content, d.category,
       1 - (d.embedding <=> $1) AS similarity
FROM documents d
JOIN user_preferences up ON d.category = up.category
WHERE up.user_id = 42
  AND d.created_at >= NOW() - INTERVAL '30 days'
ORDER BY d.embedding <=> $1
LIMIT 10;
```

전용 벡터 데이터베이스(Milvus, [[weaviate|Weaviate]])에서는 이런 메타데이터 조인을 애플리케이션 레이어에서 수동으로 처리해야 하는 반면, pgvector는 단일 쿼리로 해결한다.

## Python 연동

```python
import psycopg2
import numpy as np
from pgvector.psycopg2 import register_vector

conn = psycopg2.connect("postgresql://user:pass@localhost/mydb")
register_vector(conn)

cur = conn.cursor()
embedding = np.random.rand(1536).astype(np.float32)

# 삽입
cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)",
            ("예시 문서", embedding))

# 검색
cur.execute("""
    SELECT content, embedding <=> %s AS distance
    FROM documents
    ORDER BY distance LIMIT 5
""", (embedding,))
results = cur.fetchall()
```

## pgvector vs 전용 벡터 데이터베이스

| 항목 | pgvector | [[faiss|FAISS]] | [[weaviate|Weaviate]] / Milvus |
|---|---|---|---|
| 인프라 추가 | 없음 (PostgreSQL에 통합) | 없음 (라이브러리) | 신규 서비스 |
| 관계형 조인 | 네이티브 SQL | 없음 | 없음 |
| 수평 확장 | PostgreSQL 수준 | 수동 샤딩 | 클러스터 내장 |
| 벡터 규모 | 수천만 (실용적 한계) | 수십억 | 수십억 |
| 운영 복잡도 | 낮음 | 낮음 | 높음 |
| 적합 규모 | 스타트업 ~ 중규모 | 연구/고성능 | 대규모 프로덕션 |

## 실무 관점

pgvector는 **"벡터 검색이 필요한데 PostgreSQL을 이미 쓰고 있는"** 팀에게 최적이다. 별도 인프라를 추가하지 않고 기존 백업, 복제, 모니터링 파이프라인을 그대로 활용할 수 있다. 수천만 개 이하 벡터에서는 HNSW 인덱스로 충분한 성능을 낸다. 수억~수십억 개 규모로 성장할 계획이라면 pgvector에서 시작해 나중에 전용 벡터 DB로 마이그레이션하는 전략도 유효하다. Supabase를 사용하는 경우 pgvector가 기본 내장되어 별도 설정 없이 바로 사용할 수 있다.

## 관련 문서

- [[faiss|FAISS]] - Meta의 고성능 벡터 검색 라이브러리 (수십억 벡터 규모)
- [[weaviate|Weaviate]] - 독립형 벡터 데이터베이스 (그래프 모델 지원)
- [[rag-pipeline|RAG 파이프라인]] - pgvector가 검색 레이어로 활용되는 맥락
- [[chroma-db|ChromaDB]] - 소규모 RAG 프로토타이핑용 벡터 스토어
