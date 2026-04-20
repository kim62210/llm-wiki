---
title: MT-Bench
category: tooling
page_type: entity
tags: [tooling, entity, benchmark, evaluation, multi-turn, llm-judge, mt-bench]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# MT-Bench

MT-Bench는 LLM의 다중 턴(multi-turn) 대화 능력과 지시 수행(instruction-following) 능력을 평가하기 위한 벤치마크다. 2023년 Lianmin Zheng et al.이 "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" 논문(arXiv:2306.05685, NeurIPS 2023)에서 제안했다. 이 논문은 MT-Bench 벤치마크와 함께 [[llm-as-judge-calibration]] 패러다임을 체계적으로 검증한 연구이기도 하다.

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 이름 | MT-Bench (Multi-Turn Benchmark) |
| 저자 | Lianmin Zheng, Wei-Lin Chiang et al. (LMSYS) |
| 논문 | arXiv:2306.05685 (NeurIPS 2023) |
| 저장소 | github.com/lm-sys/FastChat (fastchat/llm_judge/) |
| 질문 수 | 80개 (2턴씩 = 160개 응답) |
| 카테고리 | 8개 |
| 평가 방식 | GPT-4 판정 (1~10점 척도) |
| 공개 데이터 | 80개 질문, 3K 전문가 투표, 30K 대화 |

## 벤치마크 구조

MT-Bench는 80개의 고품질 다중 턴 질문으로 구성된다. 각 질문은 2턴으로 이루어지며, 두 번째 턴은 첫 번째 턴의 응답을 기반으로 한 후속 질문이다.

**8개 카테고리**:
- Writing (글쓰기)
- Roleplay (역할극)
- Extraction (정보 추출)
- Reasoning (추론)
- Math (수학)
- Coding (코딩)
- Knowledge I (지식 I -- STEM)
- Knowledge II (지식 II -- 인문/사회)

각 카테고리에 10개 질문이 배정되어 있다. 카테고리 설계는 실제 사용자가 챗봇에게 하는 대표적 요청 유형을 반영한다.

## 평가 방식: LLM-as-Judge

MT-Bench의 핵심 혁신은 GPT-4를 자동 판정자(judge)로 사용하는 방식이다.

**Single-Answer Grading (기본 모드)**: GPT-4가 모델의 응답을 직접 읽고 1~10점 척도로 채점한다. 각 턴별로 점수가 매겨지며, 전체 점수는 두 턴의 평균이다. 쌍대 비교(pairwise comparison) 없이 절대 점수를 부여하므로 효율적이다.

**Pairwise Comparison (비교 모드)**: 두 모델의 응답을 나란히 놓고 GPT-4가 어느 쪽이 더 나은지 판정한다. 위치 편향(position bias)을 줄이기 위해 순서를 바꿔 두 번 판정한다.

**핵심 발견**: GPT-4 판정자는 인간 전문가와 80% 이상의 일치율을 보이며, 이는 인간 간 일치율과 동등한 수준이다. 이 결과가 [[llm-as-judge-calibration]] 접근법의 실용성을 뒷받침했다.

## Chatbot Arena와의 관계

MT-Bench는 LMSYS가 운영하는 Chatbot Arena와 한 쌍을 이룬다.

**Chatbot Arena**: 불특정 다수의 사용자가 두 익명 모델과 동시에 대화하고, 어느 쪽이 더 나은지 투표하는 크라우드소싱 플랫폼이다. Elo 레이팅 시스템으로 순위를 매긴다.

**상호 보완**: MT-Bench는 고정된 80개 질문으로 통제된 비교를 제공하고, Chatbot Arena는 실제 사용자의 다양한 질문으로 개방형 비교를 제공한다. 두 결과가 높은 상관관계를 보이면서 LLM 평가의 양대 축이 되었다.

## 장점

**비용 효율**: 인간 평가 대비 1/10 이하의 비용으로 유사한 품질의 평가가 가능하다.

**재현성**: 동일 질문 + 동일 판정 모델로 결과를 재현할 수 있다 (temperature 0 사용 시).

**개방형 평가**: [[mmlu]]나 [[gsm8k]] 같은 정답이 있는 벤치마크와 달리, 글쓰기, 역할극 등 정답이 없는 태스크도 평가할 수 있다.

**다중 턴 특화**: 대부분의 벤치마크가 단일 턴 평가인 데 반해, MT-Bench는 대화의 맥락 유지 능력까지 측정한다.

## 한계

**판정자 편향**: GPT-4가 판정하므로, GPT-4와 유사한 스타일의 응답이 체계적으로 높은 점수를 받을 가능성이 있다. 이를 "자기 향상 편향(self-enhancement bias)"이라 한다.

**규모 제한**: 80개 질문은 통계적으로 충분하지 않을 수 있다. 카테고리당 10개 문제로는 세분화된 능력 차이를 포착하기 어렵다.

**정적 질문셋**: 질문이 공개되어 있어 모델이 이 질문에 특화 학습할 위험이 있다 -- [[benchmark-contamination]] 문제다.

**판정 비용 변동**: GPT-4 API 가격 변동에 따라 평가 비용이 달라지며, 오픈소스 대안 판정자의 품질은 아직 GPT-4에 미치지 못한다.

## 후속 발전

- **Arena-Hard**: MT-Bench의 질문을 Chatbot Arena 데이터 기반으로 확장하고 난이도를 높인 자동 평가 파이프라인
- **WildBench**: 실제 사용자 질문 기반 벤치마크로 MT-Bench의 인위적 질문 한계를 보완
- **AlpacaEval**: 단일 턴이지만 대규모(805 질문) LLM-as-Judge 벤치마크
- **[[livebench]]**: 동적 질문 업데이트로 오염 문제를 해결

## 실무 활용 가이드

**모델 비교**: frontier 모델 비교에는 MT-Bench 점수와 Chatbot Arena Elo를 함께 참고한다. 오픈소스 모델 평가 시에는 [[evaluation-harness]]와 병행한다.

**자체 평가 구축**: FastChat의 llm_judge 모듈을 사용하면 커스텀 질문셋으로 MT-Bench 스타일 평가를 구축할 수 있다. [[deepeval]]에서도 유사한 LLM-as-Judge 평가를 지원한다.

**판정 모델 선택**: GPT-4 외에 Claude, Gemini 등을 판정자로 사용하여 교차 검증하면 편향을 줄일 수 있다.

## 관련 문서
- [[mtbench-llmjudge]] -- MT-Bench + LLM-as-Judge

- [[mmlu]] -- 지식 평가 벤치마크
- [[humaneval]] -- 코드 생성 벤치마크
- [[gsm8k]] -- 수학 추론 벤치마크
- [[truthfulqa]] -- 진실성 벤치마크
- [[llm-as-judge-calibration]] -- LLM 판정 기반 평가
- [[human-evaluation-protocols]] -- 인간 평가 설계
- [[evaluation-harness]] -- 통합 평가 프레임워크
- [[deepeval]] -- LLM 평가 프레임워크
- [[livebench]] -- 동적 벤치마크
- [[ragas]] -- RAG 평가 프레임워크
