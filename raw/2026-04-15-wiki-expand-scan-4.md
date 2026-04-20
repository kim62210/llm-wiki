---
source: wiki-expand-scan
date: 2026-04-15
status: completed
---

# Wiki Expand Scan #4 (2026-04-15)

## 스캔 결과 요약

현재 위키: 772 페이지

### 깨진 wikilink (127개)
- 대부분 기존 페이지의 한국어 별칭 (예: "RLHF 파이프라인" -> rlhf-pipeline)
- 신규 페이지 필요 없음, 링크 수정으로 해결

### 고빈도 미등록 용어 (생성 대상 확정 15개)

| 용어 | 참조 수 | 카테고리 | 타입 | 비고 |
|------|---------|---------|------|------|
| react-pattern | 5+ | agents | concept | ReAct: Reasoning + Acting, 기본 에이전트 패턴 |
| tree-of-thought | 5 | concepts | concept | ToT 추론, forest-of-thought는 있으나 ToT 없음 |
| reflexion | 5 | agents | concept | 에이전트 자기반성 프레임워크 |
| self-refine | 4 | concepts | concept | 반복적 자기개선 |
| best-of-n-sampling | 5 | inference | concept | N개 생성 후 최선 선택 |
| self-consistency-decoding | 2 | concepts | concept | 다수결 CoT 디코딩 |
| logit-lens | 0 | concepts | concept | 잔차 스트림 각 레이어 해석 |
| activation-patching | 0 | concepts | concept | 인과적 개입 기법 |
| weak-to-strong-generalization | 1 | training | concept | OpenAI 수퍼얼라인먼트 |
| model-organisms-alignment | 0 | training | concept | Anthropic 정렬 연구 |
| compound-ai-systems | 0 | concepts | concept | 다중 모델/도구 결합 시스템 |
| rejection-sampling-sft | 0 | training | concept | RM으로 SFT 데이터 필터링 |
| iterative-dpo | 0 | training | concept | 다회차 DPO |
| agent-planning-strategies | 0 | agents | concept | 계획/재계획/하위목표 분해 |
| tool-use-patterns | 5 | agents | concept | 도구 호출, 함수 호출 패턴 |
