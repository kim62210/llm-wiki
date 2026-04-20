---
source: arxiv
arxiv_id: "2602.02262"
title: "OmniCode: A Benchmark for Evaluating Software Engineering Agents"
authors: ["Atharv Sonwane", "Eng-Shen Tu", "Wei-Chung Lu", "Claas Beger", "Carter Larsen", "Debjit Dhar", "Simon Alford", "Rachel Chen", "Ronit Pattanayak", "Tuan Anh Dang", "Guohao Chen", "Gloria Geng", "Kevin Ellis", "Saikat Dutta"]
date: 2026-02-02
url: "https://arxiv.org/abs/2602.02262"
fetched: 2026-04-20
status: pending_ingest
tags: [swe-benchmark, coding-agents, multilingual-eval, bug-fixing, test-generation, code-review, swe-agent]
---

## Abstract

HumanEval, SWE-Bench가 "competition programming·patch generation" 같은 좁은 과제에 국한된 점을 보완하는 포괄적 SWE 에이전트 벤치마크. **1,794 tasks, 3 languages(Python/Java/C++), 4 categories** 규모.

## 4가지 과제 범주

| 범주 | 설명 |
|------|------|
| **Bug fixing** | 버그 재현·패치 |
| **Test generation** | 기존 코드에 단위·통합 테스트 생성 |
| **Code review fixing** | 리뷰 코멘트 대응 수정 |
| **Style fixing** | 스타일 가이드 준수 수정 |

## 언어별 커버리지

- Python, Java, C++
- 각 언어·범주 조합의 성능 격차 측정 가능

## 방법론적 강점

- **Manual validation**: 정의 불명확 문제 제거
- **Synthetic task generation**: 데이터 누설(data leakage) 방지
- SWE-Agent 등 기존 에이전트 프레임워크와 다양한 LLM 조합 평가

## 주요 결과

- 기존 에이전트는 **영역별 성능 편차 극심**
- SWE-Agent + DeepSeek-V3.1
  - Python bug fix는 무난
  - Java Test Generation에서 **최고 20.9%**에 불과
- Python-편향 학습 데이터가 multilingual 일반화를 막고 있음을 시사

## 시사점

- SWE-Bench 과대적합 우려에 대한 반례 → **multilingual·multi-task** 평가가 필수
- 현재 코딩 에이전트는 "Python bug fix specialist"에 가까움
- Test generation, code review는 향후 에이전트 학습에서 집중 영역

## 기존 페이지 업데이트 후보

- `wiki/concepts/swe-benchmarks.md` — OmniCode 추가
- `wiki/agents/swe-agent.md` — multilingual 한계 언급
- `wiki/papers/coding-agents-general-agents-paper.md` — 동일 테마의 보완 논문

## Raw 요약 키워드
OmniCode, 1794 tasks, multilingual SWE, Python/Java/C++, bug fixing, test generation, code review fixing, style fixing, SWE-Agent, 20.9% Java test generation
