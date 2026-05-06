---
title: Nomic Embed - 오픈소스 임베딩 모델
category: rag
page_type: entity
project: Nomic
tags: [임베딩, 오픈소스, RAG, 장문-컨텍스트, matryoshka, 재현가능]
sources: [raw/2026-04-27-topic-queue-v3.md]
created: 2026-04-27
updated: 2026-04-27
---

# Nomic Embed - 오픈소스 임베딩 모델

## 개요

**Nomic Embed Text**는 Nomic AI가 개발한 완전 오픈소스 텍스트 임베딩 모델이다. 출시 당시 OpenAI `text-embedding-ada-002`를 MTEB(Massive Text Embedding Benchmark) 벤치마크에서 능가하면서 주목받았으며, 137M 파라미터 규모에도 불구하고 상업 모델과 경쟁 가능한 성능을 보여준다. **완전 재현 가능(fully reproducible)**한 학습 파이프라인을 공개해 오픈소스 임베딩 생태계에 중요한 기여를 했다.

```mermaid
flowchart LR
    소스텍스트["입력 텍스트"] --> 토큰화["토크나이저\n(BERT 계열)"]
    토큰화 --> 인코더["Nomic Embed\n인코더 (137M)"]
    인코더 --> 풀링["Mean Pooling"]
    풀링 --> 벡터["임베딩 벡터\n(768차원)"]
    벡터 --> MRL["Matryoshka 표현\n64~768차원 지원"]
    MRL --> 검색["벡터 검색 / RAG"]
```

위 다이어그램은 Nomic Embed의 추론 파이프라인을 보여준다. 단일 모델이 다양한 차원으로 출력을 지원하는 [[matryoshka-embeddings]] 구조를 활용한다.

---

## 핵심 사양

| 항목 | 값 |
|------|-----|
| 모델 파라미터 | 137M |
| 임베딩 차원 | 768 (MRL로 64~768 가변) |
| 최대 시퀀스 길이 | 8,192 토큰 |
| 라이선스 | Apache 2.0 |
| 학습 데이터 | 완전 공개 (재현 가능) |
| 지원 작업 | 검색, 분류, 군집화, 의미 유사도 |

---

## 주요 특징

### 1. 오픈소스 완전 재현 가능성

Nomic Embed의 가장 큰 차별점 중 하나는 학습에 사용된 **데이터, 코드, 가중치 모두를 공개**했다는 점이다. 기존 오픈소스 임베딩 모델들도 가중치는 공개했지만 학습 데이터나 파이프라인을 공개하지 않는 경우가 많았다. Nomic은 이를 극복해 커뮤니티가 독립적으로 재현하고 개선할 수 있는 기반을 마련했다.

### 2. 8K 장문 컨텍스트 지원

일반적인 BERT 계열 모델이 512 토큰으로 제한되는 것과 달리, Nomic Embed는 **8,192 토큰**까지 처리할 수 있다. 이는 긴 문서를 청킹 없이 통째로 임베딩하거나, 큰 청크 단위로 처리하는 RAG 파이프라인에 유리하다.

### 3. Matryoshka 표현 학습 (MRL)

단일 모델로 여러 차원의 임베딩을 생성할 수 있는 [[matryoshka-embeddings]] 기법을 채택했다. 768차원 전체를 사용하면 최고 품질, 더 작은 차원(예: 256, 128, 64)을 사용하면 저장 공간과 검색 속도를 절약할 수 있다.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)

# 기본 768차원 임베딩
embeddings = model.encode(["검색 예시 텍스트"], convert_to_tensor=True)

# 검색 태스크용 접두사 활용 (task prefix)
queries = ["search_query: 파이썬 임베딩 모델"]
docs = ["search_document: Nomic Embed는 오픈소스 임베딩 모델이다"]

query_embs = model.encode(queries)
doc_embs = model.encode(docs)
```

### 4. 태스크 접두사 (Task Prefix)

Nomic Embed v1.5 이후로 **태스크 접두사(task prefix)**를 활용해 동일 모델로 다양한 작업 유형에 최적화된 임베딩을 생성할 수 있다:

| 접두사 | 용도 |
|--------|------|
| `search_query:` | 검색 쿼리 인코딩 |
| `search_document:` | 검색 대상 문서 인코딩 |
| `classification:` | 분류 태스크 |
| `clustering:` | 군집화 태스크 |

이 방식은 [[instructor-embedding-model]]의 지시 튜닝 접근법과 유사하지만, 더 간결한 접두사 형태를 사용한다.

---

## MTEB 성능

Nomic Embed는 출시 시점(2024년 초) 기준 오픈소스 모델 중 최고 수준의 MTEB 성능을 기록했다:

- **전체 평균**: OpenAI `text-embedding-ada-002` 대비 우위
- **검색(Retrieval)**: BEIR 벤치마크에서 강력한 성능
- **STS (의미 유사도)**: 경쟁력 있는 수준
- **분류/군집화**: 높은 범용성

[[mteb]] 리더보드에서의 위치는 이후 버전이 출시되면서 지속적으로 갱신되었다.

---

## 버전 이력

| 버전 | 특징 |
|------|------|
| v1.0 | 최초 공개, 512토큰 제한 |
| v1.5 | 8K 컨텍스트 확장, MRL 지원, task prefix 추가 |

---

## 실무 활용 가이드

### Ollama를 통한 로컬 실행

```bash
# Ollama로 로컬 임베딩 서버 실행
ollama pull nomic-embed-text
```

```python
import ollama

response = ollama.embeddings(
    model="nomic-embed-text",
    prompt="검색 예시 텍스트"
)
embedding = response["embedding"]  # 768차원 벡터
```

### LangChain 통합

```python
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector = embeddings.embed_query("RAG 시스템 구축 방법")
```

### 선택 기준

Nomic Embed가 적합한 경우:
- 비용 절감이 중요하고 자체 호스팅 가능한 환경
- 8K 토큰 이상의 긴 문서 처리가 필요할 때
- 재현 가능한 학습 파이프라인이 필요한 연구 환경
- 오픈소스 라이선스(Apache 2.0) 요건이 있을 때

---

## 왜 중요한가

Nomic Embed는 **"오픈소스 임베딩도 상업 모델과 경쟁할 수 있다"**는 것을 실증했다. 완전 재현 가능한 파이프라인은 AI 투명성 측면에서도 의미가 크며, 로컬 실행이 가능하므로 프라이버시 민감 환경(의료, 금융 등)에서도 활용 가능하다. [[embedding-models-for-rag]] 선택 시 비용 대비 성능을 고려할 때 항상 우선 검토 대상이 된다.

---

## 관련 문서

- [[embedding-models-for-rag]] - 임베딩 모델 전체 비교
- [[matryoshka-embeddings]] - 가변 차원 임베딩 기법
- [[mteb]] - 임베딩 벤치마크 기준
- [[mean-vs-cls-pooling]] - 풀링 전략 (Nomic은 Mean Pooling 사용)
- [[token-pooling-strategies]] - 다양한 풀링 전략 비교
- [[embedding-finetuning]] - 도메인 특화 파인튜닝
- [[dense-retrieval]] - 밀집 검색 기반 RAG
- [[instructor-embedding-model]] - 지시 튜닝 기반 임베딩 비교
