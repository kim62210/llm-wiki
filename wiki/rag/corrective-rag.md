---
title: 교정 RAG (Corrective RAG, CRAG)
category: rag
page_type: concept
tags: [RAG, CRAG, 자기반성, 교정, 쿼리정제, 에이전틱RAG]
sources: [raw/2026-04-15-concept-corrective-rag.md]
created: 2026-04-15
updated: 2026-04-15
---

## 개요

교정 RAG(Corrective RAG, CRAG)는 검색된 문서를 **동적으로 평가**하고, 관련성이 부족하면 **교정 조치를 수행**하며, **쿼리를 자동 정제**하여 생성 응답의 품질을 높이는 RAG 패턴이다.

표준 RAG가 검색 결과를 그대로 LLM에 전달하는 반면, CRAG는 자기반성(self-reflection) 메커니즘을 통해 검색 품질을 능동적으로 관리한다. 2026년 기준 Agentic RAG에서 **지배적 패턴**으로 자리잡았다.

## 왜 중요한가

- 표준 RAG의 "검색하면 끝" 접근은 저품질 문서가 그대로 컨텍스트에 포함되어 **환각(hallucination) 위험을 증폭**
- 고위험 도메인(의료, 법률, 금융)에서는 검색 결과의 관련성 검증이 필수
- 사용자 쿼리가 모호하거나 복합적일 때 단일 쿼리로는 충분한 컨텍스트 확보 불가
- CRAG는 에이전틱 RAG의 핵심 빌딩블록 -- 자율적 검색 개선의 기반

## 핵심 메커니즘

```mermaid
flowchart TD
    Q[사용자 쿼리] --> Ret[검색 실행]
    Ret --> Eval{문서 관련성<br/>평가}
    Eval -->|"관련성 높음"| Gen[응답 생성]
    Eval -->|"관련성 낮음"| Correct[교정 단계]
    Correct --> RefQ[쿼리 정제/<br/>분해]
    RefQ --> AltSrc[대안 소스 접근<br/>웹 검색 등]
    AltSrc --> Ret2[재검색]
    Ret2 --> Eval2{재평가}
    Eval2 -->|"통과"| Gen
    Eval2 -->|"여전히 부족"| Fallback[폴백 응답<br/>"정보 부족" 안내]
    Gen --> Self[자기반성<br/>응답 품질 검증]
    Self -->|"확신 높음"| Output[최종 응답]
    Self -->|"확신 낮음"| RefQ
```

CRAG 파이프라인: 검색 -> 평가 -> 교정 -> 재검색의 루프를 자기반성이 제어한다.

### CRAG vs 표준 RAG 비교

| 측면 | 표준 RAG | 교정 RAG (CRAG) |
|------|---------|----------------|
| 검색 결과 처리 | 그대로 사용 | 관련성 평가 후 필터링 |
| 낮은 관련성 대응 | 무시하거나 그대로 포함 | 교정 조치 + 재검색 |
| 쿼리 전략 | 단일 쿼리 | 자동 정제/분해 |
| 환각 위험 | 높음 | 자기반성으로 감소 |
| 대안 소스 | 미지원 | 웹 검색/대체 데이터 소스 접근 |

### CRAG의 4단계 메커니즘

1. **검색 문서 평가(Retrieval Evaluation)**: 각 문서의 관련성을 LLM 또는 경량 분류기로 동적 평가
2. **교정 단계 트리거(Correction Trigger)**: 관련성 임계값 미달 시 교정 파이프라인 실행
3. **쿼리 정제(Query Refinement)**: 의미 이해를 활용해 쿼리를 재구성하거나 하위 쿼리로 분해
4. **대안 소스 접근(Alternative Source Access)**: 컨텍스트 불충분 시 웹 검색 또는 대체 데이터 소스 활용

### 자기반성 RAG (Self-Reflective RAG)

CRAG의 상위 개념으로, 모델이 자신의 검색과 출력을 스스로 평가:

- 증거가 약하거나 답변에 확신이 낮으면 재쿼리
- 응답 생성 후에도 "이 답변이 충분한 근거에 기반하는가" 자체 검증
- 고위험 도메인에서 환각 대폭 감소

## 2026년 현황

- **Agentic RAG에서 CRAG는 지배적 패턴**: 전문 에이전트가 검색과 검증을 병렬 처리
- **A-RAG**: 계층적 검색 인터페이스로 확장한 고급 아키텍처
- 에이전트 프레임워크(LangGraph, CrewAI 등)에서 CRAG 패턴을 내장 지원

## 실무 적용

- RAG 파이프라인에 관련성 판정 단계 추가 -- 단순한 임계값 필터링부터 시작 가능
- 교정 루프의 최대 반복 횟수를 제한하여 무한 루프 방지 (보통 2-3회)
- 쿼리 정제에 LLM을 사용할 때 추가 비용/지연 대비 품질 향상의 트레이드오프 고려
- 폴백 전략 설계: 충분한 근거가 없으면 "정보 부족" 안내가 환각보다 나음

## 관련 문서
- [[patchrag-feedback-adaptation-paper]] -- PatchRAG: RAG를 위한 피드백 적응

- [[adaptive-context-compression]] -- 컨텍스트 압축 기법
- [[agentic-knowledge-base-patterns]] -- 에이전틱 지식베이스 패턴
- [[agent-memory-systems]] -- 에이전트 메모리 시스템
- [[approximate-nearest-neighbor]] -- 벡터 검색 기법
