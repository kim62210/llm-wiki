---
title: NLP 개요 (Natural Language Processing Overview)
category: concepts
page_type: concept
tags: [concepts, concept, nlp, nlu, nlg, ner, sentiment-analysis, machine-translation]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---
# NLP 개요 (Natural Language Processing Overview)

자연어 처리(Natural Language Processing, NLP)는 인간 언어를 이해하고 생성하는 인공지능 분야의 총칭이다. 자연어 이해(NLU), 자연어 생성(NLG), 개체명 인식(NER), 감정 분석, 질의응답(QA), 요약, 기계 번역 등 다양한 하위 과제를 포괄하며, 규칙 기반 시스템에서 통계적 방법, 딥러닝, 그리고 현재의 LLM 시대까지 근본적인 패러다임 전환을 거쳐왔다.

## 왜 중요한가

NLP 시장 규모는 2025년 기준 약 348억 달러로, CAGR 21.5%로 성장 중이다. 챗봇, 검색 엔진, 번역기, 음성 비서, 문서 분석 등 일상의 거의 모든 AI 인터페이스가 NLP에 기반하며, LLM의 등장으로 NLP의 모든 하위 과제가 단일 모델로 통합되는 패러다임 전환이 진행 중이다.

## 핵심 하위 분야

### NLU (Natural Language Understanding)

기계가 문법과 문맥을 통해 문장의 의도된 의미를 결정하는 것. 입력 텍스트의 의미, 의도, 감정, 엔티티를 파악하는 "읽기 이해" 능력에 해당한다.

**주요 과제:**
- **의도 분류 (Intent Classification)**: 사용자 발화의 목적 파악 ("날씨 알려줘" -> 날씨 조회 의도)
- **개체명 인식 (NER, Named Entity Recognition)**: 텍스트에서 인명, 지명, 기관명, 날짜 등 고유 엔티티 추출
- **감정 분석 (Sentiment Analysis)**: 텍스트의 긍/부정/중립 극성 및 감정 강도 판별
- **관계 추출 (Relation Extraction)**: 엔티티 간의 관계 식별 ("삼성전자의 CEO는 이재용이다")
- **상호참조 해소 (Coreference Resolution)**: "그", "이것" 등 대명사가 가리키는 대상 연결

### NLG (Natural Language Generation)

주어진 데이터셋이나 구조화된 정보를 바탕으로 자연어 텍스트를 생성하는 분야. NLU가 "읽기"라면 NLG는 "쓰기"에 해당한다.

**주요 과제:**
- **텍스트 요약 (Summarization)**: 긴 문서를 핵심 정보만 추출하여 축약 (추출적/생성적)
- **기계 번역 (Machine Translation)**: 언어 간 자동 번역
- **대화 생성 (Dialogue Generation)**: 맥락에 맞는 자연스러운 응답 생성
- **데이터-투-텍스트 (Data-to-Text)**: 표/그래프/수치를 자연어 보고서로 변환

### 질의응답 (Question Answering, QA)

자연어 질문에 대해 정확한 답변을 생성하거나 추출하는 과제. 오픈도메인 QA(위키피디아 등 대규모 지식에서 답변)와 클로즈도메인 QA(특정 문서 내에서 답변)로 구분된다. 현대 LLM은 RAG(Retrieval-Augmented Generation) 패턴으로 두 접근을 결합한다.

## 패러다임 진화

### 1세대: 규칙 기반 (1950s-1990s)

어휘 사전, 문법 규칙, 의미론, 논리 추론 규칙을 수작업으로 정의하여 의미와 엔티티를 추출했다. ELIZA(1966), SHRDLU(1970) 등이 대표적이다. 높은 정밀도가 가능하지만, 규칙 작성 비용이 막대하고 새로운 도메인/언어에 대한 확장성이 극히 낮다.

**장점:** 결과의 설명 가능성, 결정론적 동작, 도메인 특화 정확도
**한계:** 스케일링 불가, 애매모호성 처리 미흡, 유지보수 비용

### 2세대: 통계적 방법 (1990s-2010s)

대량 코퍼스에서 확률적 패턴을 학습하는 접근. Hidden Markov Model(HMM), 조건부 랜덤 필드(CRF), n-gram 언어 모델, TF-IDF 등이 활용되었다. IBM 모델(통계 기계 번역)이 규칙 기반 번역을 대체하기 시작했다.

**장점:** 데이터 기반 일반화, 규칙 수작업 감소
**한계:** 특징 엔지니어링(feature engineering) 의존, 장거리 문맥 파악 한계

### 3세대: 딥러닝 (2013-2018)

Word2Vec(2013)이 단어를 연속 벡터 공간에 임베딩하면서 패러다임이 전환되었다. RNN, LSTM, Seq2Seq + Attention 메커니즘이 기계 번역과 QA에서 돌파구를 열었고, 특징 엔지니어링이 자동화되었다. ELMo(2018)가 문맥 의존 임베딩을 도입하여 다의어 처리를 개선했다.

**장점:** 자동 특징 학습, 장거리 의존성 포착, 전이 학습 기반
**한계:** 대량 라벨링 데이터 필요, 계산 비용, 블랙박스 특성

### 4세대: 트랜스포머와 LLM (2018-현재)

Transformer(2017, "Attention Is All You Need")가 RNN의 순차적 처리를 병렬 self-attention으로 대체하면서 스케일링의 문이 열렸다. BERT(2018)가 양방향 사전학습으로 NLU 벤치마크를 석권하고, GPT 시리즈가 생성 능력을 증명했다.

**현재 LLM의 특징:**
- 수천억 파라미터의 사전학습 모델이 NLU/NLG/QA/요약/번역 등 거의 모든 NLP 과제를 단일 모델로 처리
- Few-shot/Zero-shot 학습으로 과제별 학습 데이터 의존도 급감
- RLHF/Constitutional AI로 안전성과 유용성 정렬
- 규칙 기반 접근과의 시너지 연구 진행 중 (하이브리드 시스템)

## 규칙 기반 vs. LLM 기반의 시너지

2025년 MDPI 연구에 따르면, 규칙 기반과 LLM 기반 기술은 상호 보완적이다. 규칙 기반은 결정론적 정확도, 설명 가능성, 규제 준수가 필요한 영역에서 강점을 유지하고, LLM은 일반화, 문맥 이해, 창의적 생성에서 우위를 보인다. 의료, 법률, 금융 등 고위험 도메인에서는 LLM 출력을 규칙 기반 검증기로 후처리하는 하이브리드 파이프라인이 부상하고 있다.

## NLP 주요 과제 맵

| 과제 | NLU/NLG | 설명 |
|------|---------|------|
| 개체명 인식 (NER) | NLU | 텍스트에서 고유명사/엔티티 추출 |
| 감정 분석 | NLU | 텍스트의 감정/극성 판별 |
| 의도 분류 | NLU | 발화의 목적 분류 |
| 텍스트 요약 | NLG | 긴 텍스트의 핵심 축약 |
| 기계 번역 | NLU+NLG | 언어 간 자동 번역 |
| 질의응답 (QA) | NLU+NLG | 자연어 질문에 답변 |
| 대화 시스템 | NLU+NLG | 맥락 기반 대화 생성 |
| 텍스트 분류 | NLU | 문서/문장을 카테고리로 분류 |
| 정보 추출 | NLU | 비정형 텍스트에서 구조화된 정보 추출 |

## 대표 레퍼런스

- [NLP vs. NLU vs. NLG: What's the Difference? (IBM)](https://www.ibm.com/think/topics/nlp-vs-nlu-vs-nlg)
- [Strengths and Weaknesses of LLM-Based and Rule-Based NLP Technologies (MDPI, 2025)](https://www.mdpi.com/2079-9292/14/15/3064)
- [Large Language Models versus Natural Language Understanding and Generation (ACM, 2024)](https://dl.acm.org/doi/fullHtml/10.1145/3635059.3635104)

## 관련 문서

- [[ai-reasoning-models|AI Reasoning Models]]
- [[ai-benchmarks-overview|AI Benchmarks Overview]]
