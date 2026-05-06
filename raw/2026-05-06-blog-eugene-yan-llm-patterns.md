---
source: blog
url: https://eugeneyan.com/writing/llm-patterns/
title: Patterns for Building LLM-based Systems & Products
author: Eugene Yan
date: 2023-07-30
fetched: 2026-05-06
status: pending_ingest
tags: [llm-patterns, eugene-yan, evals, rag, fine-tuning, caching, guardrails, defensive-ux, feedback-loop]
---

# Patterns for Building LLM-based Systems & Products (Eugene Yan)

## 개요

7개 패턴을 두 축으로 정리:
- 성능 향상 vs 비용/위험 감소
- 데이터 가까이 vs 사용자 가까이

## 7가지 패턴

### 1. Evals - 성능 측정

벤치마크:
- **MMLU**: 57개 작업 (수학, 역사, 컴퓨터과학, 법)
- **HELM**: 다영역 종합 평가 (정확성, calibration, robustness, fairness)
- **AlpacaEval**: 자동화된 LLM 선호도 win rate

| Metric | 목적 | 한계 |
|--------|------|------|
| BLEU | n-gram precision | 인간 판단 상관 낮음 |
| ROUGE | summarization recall | 창의적 작업에서 상관 낮음 |
| BERTScore | embedding 기반 시맨틱 유사도 | BLEU/ROUGE보다 동의어 처리 우수 |
| MoverScore | soft 토큰 정렬 | many-to-one 매칭 |

> "How important evals are to the team is a major differentiator between folks rushing out hot garbage and those seriously building products."

신흥 접근법: G-Eval - Strong LLM (GPT-4)을 reference-free evaluator로, CoT 프롬프팅과 결합.

권고: 작업 특화 eval set 구축, "Eval Driven Development" (EDD) 적용.

### 2. RAG (Retrieval-Augmented Generation) - 지식 추가

핵심 논문:
- **Dense Passage Retrieval (DPR)**: Fine-tuned BERT encoders → top-5 정확도 65.2% vs BM25 42.9%
- **Fusion-in-Decoder (FiD)**: 검색된 passages를 인코더에서 독립 처리
- **RETRO**: pre-training 동안 검색 수행, chunked cross-attention

추천 임베딩 모델:
- FastText (157 언어)
- Sentence-Transformers (100+ 언어)
- E5 family (instruction-based: "passage:", "query:")
- Instructor models (커스터마이저블 prompts)
- GTE (Alibaba, MTEB 리더보드 상위)

ANN 인덱스:
- FAISS (GPU-optimized)
- HNSW (계층 그래프)
- ScaNN (recall/latency 트레이드오프)

**Hybrid retrieval**: BM25 + 시맨틱 임베딩 조합 - 이름/약어/ID 검색을 임베딩 단독으로는 놓침.

### 3. Fine-tuning - 작업 특화

종류:
- Continued pre-training (도메인 데이터)
- Instruction fine-tuning (instruction-output 쌍)
- Single-task fine-tuning
- RLHF (인간 선호도)

주요 모델:
- ULMFit (2018) - pre-training → fine-tuning 패러다임 정립
- BERT, GPT, T5, InstructGPT

Parameter-Efficient 기법:
| 기법 | 업데이트 파라미터 | Full fine-tuning 대비 |
|------|------------------|----------------------|
| Soft Prompt Tuning | trainable input embeddings | 비슷 |
| Prefix Tuning | hidden states (~0.1%) | extrapolation에서 우수 |
| Adapter | task-specific layers (3.6%) | 0.4% gap |
| LoRA | low-rank matrix products | 우수 + regularization |
| QLoRA | 4-bit + LoRA | 65B 모델 **48GB vs 780GB** |

권고: Falcon-7B, BERT, RoBERTa 등 작은 모델로 production 가능성 우선.

### 4. Caching - 지연/비용 감소

GPTCache 컴포넌트:
- Embedding generator
- Similarity evaluator (vector store 비교)
- Cache storage (FAISS, Hnswlib, 클라우드)

안전 캐싱 기준:
- **Item IDs** (사전 계산 요약)
- **Item pairs** (영화 비교)
- **Constrained inputs** (드롭다운 선택)
- 단순 시맨틱 유사도는 위험

Cache hit rate가 power-law 분포일 때만 효과적.

### 5. Guardrails - 출력 품질 보장

**Pydantic-style Validation** (Guardrails 패키지):
- Single-value 검증 (predefined choices, length/range)
- Syntactic checks (URL, executable code)
- Semantic checks (cosine similarity to reference)
- Safety checks (profanity, toxicity)

**LLM-based Evaluation** (NeMo-Guardrails):
- Fact-checking (검색된 컨텍스트와 일관성)
- Hallucination detection (다중 completion)
- Content moderation

**Structural Guidance** (Microsoft Guidance):
- Domain-specific language
- 토큰 주입으로 형식 강제
- Token healing (토크나이저 버그 회피)
- 유효한 JSON 보장

### 6. Defensive UX - 에러 우아하게 처리

가이드라인:
- **Microsoft Human-AI Interaction (18 가이드라인)**: 초기 능력 명료화 → 진행 중 컨텍스트 인식 → 잘못됐을 때 쉬운 dismissal → 시간이 지나며 학습
- **Google People + AI Guidebook (23 패턴)**: 안전한 탐색, 익숙함에 anchor, 기대치 설정
- **Apple ML Human Interface**: 역할 결정, 사용자 경험 거꾸로 설계

실용 패턴:
- **Set Expectations**: Bard의 "This code won't work" 면책
- **Enable Dismissal**: Copilot의 무시하기 쉬운 제안
- **Provide Attribution**: BingChat 인용
- **Anchor on Familiarity**: 알려진 UI 패턴, chat-only 인터페이스 회피
- **Lower Effort Interactions**: 스크롤 추천이 chat 검색보다 낮은 성능 기대

### 7. User Feedback - 데이터 플라이휠

**Explicit**:
- 좋아요/싫어요 (ChatGPT)
- Regenerate/variation (Midjourney)
- Accept/ignore (Copilot)

**Implicit**:
- Full acceptance vs minor tweaks vs ignoring
- 대화 길이, 세션 지속
- 생성 후 입력 수정
- 기능 사용 패턴, daily active usage

전략: 코어 UX에 피드백을 통합, 별도 설문 회피.

## 부가 개념

**Text Embeddings**: 압축된 고정 크기 벡터 → MTEB로 측정 (57 언어).

**추가 패턴**:
- **Data Flywheel**: 사용 → 피드백 → 개선 모델 → 더 나은 UX → 더 많은 사용
- **Cascade**: 복잡 작업을 하위 작업으로
- **Monitoring**: A/B test 실패 사례 (LLM 지원으로 12배 손실)

## 핵심 결론

> "There is a large class of problems that are easy to imagine and build demos for, but extremely hard to make products out of."

프로덕션 LLM 시스템 = evals + RAG + fine-tuning + guardrails + defensive UX + feedback의 조합.

## 메모

- 게시일: 2023년 7월 30일
- 66분 분량
- 본 글은 LLM 시스템 아키텍처의 가장 영향력 있는 1차 자료 중 하나
