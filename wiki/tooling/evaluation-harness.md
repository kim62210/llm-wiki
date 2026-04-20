---
title: Evaluation Harness
category: tooling
page_type: entity
tags: [tooling, entity, evaluation, lm-evaluation-harness, openai-evals, framework]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---
# Evaluation Harness

LLM 평가 하니스(evaluation harness)는 다양한 벤치마크를 표준화된 환경에서 실행하고 결과를 비교할 수 있게 해주는 프레임워크다. 이 페이지에서는 두 가지 핵심 프로젝트를 다룬다: EleutherAI의 lm-evaluation-harness(LM Eval Harness)와 OpenAI의 Evals. 이 두 프레임워크는 LLM 평가의 인프라 계층을 구성하며, [[mmlu]], [[humaneval]], [[gsm8k]], [[truthfulqa]] 같은 개별 벤치마크를 실행하는 "실행 엔진" 역할을 한다.

## lm-evaluation-harness (EleutherAI)

### 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 이름 | Language Model Evaluation Harness (lm-eval) |
| 개발 | EleutherAI |
| 저장소 | github.com/EleutherAI/lm-evaluation-harness |
| 라이선스 | MIT |
| 지원 태스크 | 400개 이상 |
| 주요 사용처 | Hugging Face Open LLM Leaderboard 백엔드 |

### 탄생 배경

lm-evaluation-harness는 OpenAI의 GPT-3 논문("Language Models are Few-Shot Learners", 2020)이 계기가 되었다. 논문에서 수십 개의 벤치마크 결과를 보고했지만 평가 코드는 공개하지 않았다. EleutherAI는 동일한 벤치마크를 재현하고 누구나 사용할 수 있는 통합 프레임워크를 만들기 위해 이 프로젝트를 시작했다.

### 핵심 설계 원칙

**통합 인터페이스**: 어떤 causal language model이든 동일한 입력과 코드베이스로 테스트한다. HuggingFace 모델, OpenAI API, vLLM, 커스텀 로컬 API 등을 모두 지원한다.

**태스크 버전 관리**: 각 벤치마크 태스크에 버전을 부여하여 재현성을 보장한다. 같은 태스크명이라도 프롬프트 형식, few-shot 예시 선택 등이 버전마다 다를 수 있다.

**확장성**: 새로운 벤치마크를 YAML 설정 파일로 간단히 추가할 수 있다.

### 지원 벤치마크 (주요 항목)

lm-eval은 400개 이상의 태스크를 지원한다. 이 위키에서 다루는 벤치마크 대부분이 포함된다.

- **지식 평가**: [[mmlu]], MMLU-Pro, ARC, HellaSwag, Winogrande
- **추론**: [[gsm8k]], MATH, BBH (BIG-Bench Hard)
- **코드**: [[humaneval]], MBPP
- **진실성**: [[truthfulqa]]
- **언어 이해**: LAMBADA, SQuAD, BoolQ
- **VLM (프로토타입)**: MMMU 등 시각-언어 모델 평가

### 실행 방법

기본적인 사용법은 간결하다.

```bash
# MMLU 5-shot 평가
lm_eval --model hf \
  --model_args pretrained=meta-llama/Llama-3.1-8B \
  --tasks mmlu \
  --num_fewshot 5 \
  --batch_size auto

# 여러 벤치마크 동시 실행
lm_eval --model hf \
  --model_args pretrained=... \
  --tasks mmlu,gsm8k,truthfulqa_mc2,hellaswag

# OpenAI API 모델 평가
lm_eval --model openai-completions \
  --model_args model=gpt-4 \
  --tasks mmlu
```

### Hugging Face Open LLM Leaderboard

lm-evaluation-harness는 Hugging Face의 Open LLM Leaderboard의 백엔드로 사용된다. 이 리더보드는 오픈소스 LLM의 사실상 표준 순위표이며, 수백 개의 모델이 동일한 하니스로 평가되어 직접 비교 가능하다. 이 통일된 평가 환경이 오픈소스 LLM 생태계의 건전한 경쟁을 촉진한 핵심 인프라다.

### 조직 채택

NVIDIA, Cohere, BigScience, BigCode 등 수십 개 조직이 내부 평가에 lm-eval을 사용한다. 수백 편의 논문에서 인용되어 학술 평가의 사실상 표준이 되었다. Mozilla Foundation은 "LLM 감사(auditing)를 위한 벤치마크 설정"이라는 관점에서 이 프레임워크를 조명했다.

## OpenAI Evals

### 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 이름 | OpenAI Evals |
| 개발 | OpenAI |
| 저장소 | github.com/openai/evals |
| 초점 | chat/completion 모델의 행동 평가 |
| 특징 | 커스텀 eval 정의가 용이 |

### 설계 철학

OpenAI Evals는 lm-eval과 상호 보완적 위치에 있다. lm-eval이 기존 학술 벤치마크의 표준화된 실행에 초점을 맞추는 반면, OpenAI Evals는 실무자가 자신의 사용 사례에 맞는 커스텀 평가를 쉽게 정의하고 실행하는 데 초점을 맞춘다.

### 핵심 기능

- **커스텀 Eval 정의**: JSONL 파일로 입력-출력 쌍을 정의하면 자동으로 평가 파이프라인이 구성된다
- **다양한 평가 방식**: exact match, includes, model-graded (LLM-as-Judge) 등
- **커뮤니티 Eval**: 누구나 새로운 eval을 PR로 제출하여 공유할 수 있다

## lm-eval vs OpenAI Evals 비교

| 차원 | lm-eval | OpenAI Evals |
|---|---|---|
| 주요 용도 | 학술 벤치마크 표준 실행 | 커스텀 실무 평가 |
| 태스크 수 | 400개+ 내장 | 커스텀 중심 |
| 모델 지원 | HF, API, vLLM 등 범용 | OpenAI API 중심 |
| 리더보드 | HF Open LLM Leaderboard | 없음 |
| 확장 방식 | YAML task config | JSONL + Python |
| 강점 | 재현성, 표준화 | 유연성, 커스텀 |

## 관련 평가 프레임워크

lm-eval과 OpenAI Evals 외에도 목적에 따라 다양한 프레임워크가 있다.

- **[[deepeval]]**: LLM 응답의 다차원 품질(관련성, 충실도, 독성 등) 평가. pytest 통합으로 CI/CD 파이프라인에 삽입 가능
- **[[ragas]]**: RAG 파이프라인 특화 평가. context recall/precision, faithfulness 등
- **HELM (Stanford)**: 투명성, 공정성, 강건성 등 다차원 평가 프레임워크
- **Inspect AI (UK AISI)**: AI 안전성 평가 특화 프레임워크

## 실무 활용 가이드

**오픈소스 모델 비교**: lm-eval로 [[mmlu]], [[gsm8k]], [[truthfulqa]] 등 표준 벤치마크를 동일 환경에서 실행한다.

**프로덕션 모델 평가**: OpenAI Evals나 [[deepeval]]로 자사 사용 사례에 맞는 커스텀 eval을 구성한다.

**RAG 시스템 평가**: [[ragas]]로 검색-생성 파이프라인의 종합 품질을 측정한다.

**결과 해석**: [[benchmark-contamination]]과 [[benchmark-saturation-goodharts-law]]를 감안하여 결과를 해석한다. 자동 평가 결과는 [[human-evaluation-protocols]]로 교차 검증한다.

**SWE 평가**: 코드 생성 에이전트의 실무 능력은 [[swe-bench-pro]]로 평가한다.

## 관련 문서
- [[alpacaeval]] -- AlpacaEval (LLM 자동 평가 벤치마크)
- [[dspy-framework]] -- DSPy (프롬프팅 대신 프로그래밍)

- [[mmlu]] -- 지식 평가 벤치마크
- [[humaneval]] -- 코드 생성 벤치마크
- [[gsm8k]] -- 수학 추론 벤치마크
- [[truthfulqa]] -- 진실성 벤치마크
- [[mt-bench]] -- 다중 턴 대화 벤치마크
- [[perplexity]] -- 언어 모델 내재 평가
- [[benchmark-contamination]] -- 데이터 오염 문제
- [[benchmark-saturation-goodharts-law]] -- 벤치마크 포화
- [[classification-metrics]] -- 분류 평가 지표
- [[human-evaluation-protocols]] -- 인간 평가 설계
- [[deepeval]] -- LLM 평가 프레임워크
- [[ragas]] -- RAG 평가 프레임워크
- [[swe-bench-pro]] -- 소프트웨어 엔지니어링 벤치마크
- [[livebench]] -- 동적 벤치마크
- [[humanity-last-exam]] -- 극난이도 벤치마크
