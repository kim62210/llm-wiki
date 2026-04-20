---
title: Sparse Retrieval -- BM25, TF-IDF 키워드 기반 검색
category: rag
page_type: concept
tags: [rag, sparse-retrieval, bm25, tf-idf, keyword-search, information-retrieval]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Sparse Retrieval -- BM25, TF-IDF 키워드 기반 검색

문서와 쿼리를 어휘 크기의 고차원 희소 벡터로 표현하고, 정확한 키워드 일치를 기반으로 관련 문서를 찾는 전통적 정보 검색 기법.

## 정의

Sparse Retrieval(희소 검색)은 문서를 어휘 사전(vocabulary) 크기의 벡터로 표현하되, 해당 문서에 등장하는 단어 위치에만 0이 아닌 값을 부여하는 방식이다. 대부분의 차원이 0이므로 "sparse"라 부른다. TF-IDF와 BM25가 대표적이며, 1960년대부터 발전해온 정보 검색(IR)의 근간 기술이다. [[dense-retrieval|Dense retrieval]]이 등장한 이후에도 전문용어, 고유명사, 코드 검색 등에서 여전히 강력하며, 현대 RAG 시스템에서는 하이브리드 검색의 한 축을 담당한다.

## TF-IDF에서 BM25로

### TF-IDF (Term Frequency - Inverse Document Frequency)

TF-IDF는 가장 기본적인 텍스트 가중치 기법이다.

- **TF(w, d)**: 문서 d에서 단어 w의 출현 빈도
- **IDF(w)**: log(전체 문서 수 / 단어 w를 포함하는 문서 수). 흔한 단어의 가중치를 낮춤
- **TF-IDF(w, d)** = TF(w, d) x IDF(w)

TF-IDF의 한계는 두 가지다. 첫째, 단어 빈도가 높을수록 점수가 무한히 증가한다(빈도 포화 없음). 둘째, 문서 길이를 고려하지 않아 긴 문서가 불리하게 또는 유리하게 편향된다.

### BM25 (Best Matching 25)

BM25는 1994년 Robertson 등이 제안한 확률적 검색 함수로, TF-IDF의 두 한계를 직접 해결한다. "Okapi BM25"라는 이름은 런던 시티대학교의 Okapi 시스템에서 유래했다.

```
BM25(q, d) = sum_i IDF(qi) * (f(qi, d) * (k1 + 1)) / (f(qi, d) + k1 * (1 - b + b * |d| / avgdl))
```

핵심 개선점:

1. **빈도 포화(Term Frequency Saturation)**: 파라미터 k1(기본값 1.2-2.0)이 단어 빈도의 영향에 상한을 둔다. 같은 단어가 100번 나오든 200번 나오든 점수 차이가 거의 없다.
2. **문서 길이 정규화**: 파라미터 b(기본값 0.75)가 문서 길이를 평균 문서 길이(avgdl) 대비로 정규화한다. b=0이면 길이 무시, b=1이면 완전 정규화.
3. **IDF 개선**: 음수 IDF를 방지하는 변형 공식 사용

## 역색인 (Inverted Index)

Sparse retrieval의 실행 엔진은 역색인이다.

1. **인덱싱**: 각 단어가 어떤 문서에 몇 번 등장하는지 역으로 매핑 (단어 -> 문서 목록)
2. **검색**: 쿼리 단어들의 역색인을 조회해 후보 문서 집합 확보
3. **스코어링**: BM25 공식으로 각 후보 문서 점수 산출
4. **정렬**: 점수 내림차순 정렬 후 상위 k건 반환

역색인은 구축 비용이 낮고, 문서 추가/삭제가 간단하며, 점수 계산이 투명하다. Elasticsearch, Apache Lucene, Whoosh 같은 검색 엔진이 모두 역색인 기반이다.

## Neural Sparse Retrieval

2023년 이후 등장한 SPLADE(SParse Lexical AnD Expansion) 계열은 전통 sparse retrieval과 neural 학습을 결합한다.

- **SPLADE**: Transformer가 각 단어의 가중치를 학습하되, 출력이 여전히 어휘 크기의 희소 벡터
- **확장(Expansion)**: 문서에 직접 등장하지 않지만 의미적으로 관련된 단어도 벡터에 포함. 동의어 문제 완화
- **희소성 제약**: L1 정규화로 벡터의 0이 아닌 요소 수를 제한하여 검색 효율 유지

Neural sparse는 BM25보다 의미적 매칭이 강하면서도 역색인 인프라를 그대로 활용할 수 있어 실무 전환 비용이 낮다.

## Dense Retrieval과의 비교

| 속성 | Sparse (BM25) | [[dense-retrieval|Dense Retrieval]] |
|------|--------------|------|
| 강점 | 전문용어, 고유명사, 정확 일치 | 동의어, 패러프레이즈, 의미적 유사성 |
| 약점 | 어휘 불일치 (vocabulary mismatch) | 학습 데이터 밖 용어 취약 |
| 인덱싱 | 역색인 (CPU, 저비용) | 벡터 인덱스 (GPU, 고비용) |
| 갱신 | 문서 단위 즉시 갱신 | 재인코딩 필요 |
| 해석성 | 어떤 단어가 매칭됐는지 확인 가능 | 블랙박스 |
| 지연시간 | 수 밀리초 | 수십 밀리초 (ANN 의존) |

## RAG 파이프라인에서의 역할

현대 RAG 시스템에서 BM25는 두 가지 역할을 수행한다.

1. **하이브리드 검색의 한 축**: Dense retrieval + BM25 점수를 Reciprocal Rank Fusion(RRF) 또는 가중합으로 결합. [[contextual-retrieval|Contextual Retrieval]]은 이 조합에서 BM25 성능을 극대화하기 위해 청크에 문서 맥락을 사전 주입한다.
2. **1단계 후보 확보**: 대규모 코퍼스에서 BM25로 빠르게 후보를 확보한 뒤, [[reranker-cross-encoder|cross-encoder reranker]]로 정밀 재순위. 이 2단계 파이프라인은 비용 대비 정확도가 높다.

[[agentic-rag|Agentic RAG]]에서는 에이전트가 keyword search 도구(BM25)와 semantic search 도구(dense)를 상황에 따라 선택적으로 호출한다. A-RAG 논문은 keyword/semantic/chunk-read 3-tool 인터페이스로 멀티홉 QA SOTA를 경신했다.

## 실무 파라미터 튜닝

BM25의 핵심 파라미터:
- **k1 = 1.2-2.0**: 빈도 포화 강도. 짧은 문서 위주면 낮게, 긴 문서 위주면 높게
- **b = 0.75**: 문서 길이 정규화 강도. 길이가 균일하면 낮게, 편차가 크면 높게

Elasticsearch 기본값(k1=1.2, b=0.75)이 대부분의 경우 합리적이지만, 도메인에 따라 그리드 서치로 최적값을 찾는 것을 권장한다.

## 참고 자료

- [Okapi BM25 -- Wikipedia](https://en.wikipedia.org/wiki/Okapi_BM25)
- [TF-IDF and BM25 for RAG -- A Complete Guide](https://www.ai-bites.net/tf-idf-and-bm25-for-rag-a-complete-guide/)
- [The Past and Present of Sparse Retrieval -- Hugging Face Blog](https://huggingface.co/blog/yjoonjang/the-past-and-present-of-sparse-retrieval)

## 관련 페이지

- [[dense-retrieval|Dense Retrieval]] -- 임베딩 기반 의미적 검색
- [[reranker-cross-encoder|Reranker / Cross-Encoder]] -- 2단계 재순위 모델
- [[contextual-retrieval|Contextual Retrieval]] -- 문서 맥락 주입으로 BM25 강화
- [[agentic-rag|Agentic RAG]] -- 에이전트가 BM25/dense 도구를 선택 호출
- [[graphrag-in-production|GraphRAG]] -- 지식 그래프 + 검색 결합


## 관련 문서

- [[pgvector]] -- pgvector
