---
title: AI 벤치마크 개요 (AI Benchmarks Overview)
category: concepts
page_type: concept
tags: [benchmarks, evaluation, swe-bench, hle, browsecomp, mmlu, overview, hub]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

이 페이지는 AI 모델 평가에 사용되는 주요 벤치마크들을 연결하는 허브다. 2026년의 벤치마크 지형은 그 어느 때보다 풍부하지만, 동시에 포화, 오염, Goodhart의 법칙(측정이 목표가 되면 좋은 측정이 아니게 된다) 같은 근본적 도전에 직면해 있다. 벤치마크의 가치는 실제 능력을 얼마나 잘 대리(proxy)하느냐에 달려 있으며, 단일 벤치마크 점수가 모델의 전반적 능력을 대표한다고 볼 수 없다.

## 벤치마크 분류 체계

### 지식과 추론

**MMLU / MMLU-Pro**: 57개(MMLU) 또는 확장된 학문 분야의 다지선다 문제. MMLU는 2024년 이후 주요 모델들이 90%를 넘기며 포화 상태에 도달했다. MMLU-Pro는 더 어려운 문제와 10개 선택지로 난이도를 높였다.

**GPQA (Graduate-Level Google-Proof Q&A)**: 대학원 수준의 과학 문제로, 도메인 전문가도 구글 검색으로 쉽게 풀 수 없는 난이도를 목표로 한다.

**[[humanity-last-exam|HLE (Humanity's Last Exam)]]**: CAIS와 Scale AI가 공동 개발한 2,500개 전문가 검증 멀티모달 학술 문항. 100개 이상 학문 분야를 포괄한다. 2026년 4월 기준 최고 성적은 Claude Mythos Preview의 약 64.7%로, 인간 전문가 추정 정답률(약 90%)과 큰 격차가 있다. 기존 벤치마크 포화에 대응하여 설계되었으며, "Google-proof" 문항으로 단순 정보 검색이 아닌 깊은 추론을 요구한다.

**TruthfulQA**: 모델의 진실성을 평가한다. 인간이 흔히 틀리는 질문에 대해 모델이 사실과 다른 대중적 오해를 반복하는지 검증한다.

### 수학과 과학 추론

**GSM8K**: 초등학교 수준의 수학 문제 약 8,500개. 다단계 산술 추론을 측정한다. 주요 모델들이 95% 이상을 달성하며 포화에 가까워졌다.

**MATH**: GSM8K보다 어려운 고등/대학 수준의 수학 문제.

### 코딩

**HumanEval / MBPP**: 함수 수준 코드 생성 벤치마크. pass@k 메트릭을 사용한다. 주요 모델들이 높은 점수를 달성하며 차별력이 줄었다.

**LiveCodeBench**: 실시간으로 새 문제가 추가되어 데이터 오염을 방지하는 동적 코딩 벤치마크.

**[[swe-bench-pro|SWE-bench Verified / SWE-bench Pro]]**: 실제 GitHub 이슈를 해결하는 소프트웨어 엔지니어링 벤치마크. SWE-bench Verified는 500개 인간 검증 이슈로 구성되며, 2026년 가장 많이 인용되는 코딩 벤치마크다. 다만 OpenAI 감사에서 모든 프론티어 모델의 학습 데이터와 겹침이 발견되어 오염 문제가 제기되었다. [[swe-bench-pro|SWE-bench Pro]]는 Scale AI의 SEAL 리더보드에서 이 오염 문제를 해결하기 위해 설계된 후속 벤치마크다. 2026년 Q1 기준 Claude Code(Opus 4.6)가 SWE-bench Verified에서 80.8%로 최고 점수를 기록했다.

**[[terminal-bench-2-0|Terminal-Bench 2.0]]**: 터미널 환경에서의 코딩 에이전트 평가.

### 에이전트와 실세계 상호작용

**[[browsecomp|BrowseComp]]**: OpenAI가 2025년 4월 발표한 웹 브라우징 에이전트 벤치마크. 1,266개 질문으로, 인터넷에서 찾기 어려운 얽힌 정보를 탐색하는 능력을 측정한다. MiniMax M2.5가 76.3%를 달성했다.

**[[osworld-verified|OSWorld-Verified]]**: 컴퓨터 사용 에이전트 평가. 실제 데스크톱 환경에서 작업을 수행하는 능력을 측정한다.

**[[long-horizon-agent-benchmarks|장기 호흡 에이전트 벤치마크]]**: 복잡한 멀티스텝 작업 수행 능력을 평가한다. [[metr-time-horizon-benchmark|METR Time Horizon Benchmark]]가 대표적이다.

### 다중 턴 대화

**MT-Bench**: 다중 턴 대화에서 LLM의 대화 능력을 LLM 판정(LLM-as-judge)으로 평가한다.

**Arena Hard / Chatbot Arena**: ELO 레이팅 기반의 인간 선호도 평가. 실제 사용자의 블라인드 비교를 통해 모델을 랭킹한다.

## 벤치마크의 도전 과제

**데이터 오염(Contamination)**: 벤치마크 데이터가 학습 데이터에 포함되면 점수가 실제 능력을 과대 평가한다. SWE-bench Verified의 오염 문제가 대표적이다. 동적 벤치마크(LiveCodeBench, SWE-bench Pro)가 이를 해결하려는 시도다.

**포화(Saturation)**: MMLU, GSM8K 등은 주요 모델들이 높은 점수를 달성하며 차별력을 잃었다. [[humanity-last-exam|HLE]]는 이에 대응하여 설계되었다.

**Goodhart의 법칙**: 벤치마크 점수 최적화가 실제 능력 향상과 괴리되는 현상. 특정 벤치마크에 과적합(overfitting)된 모델이 실제 작업에서는 기대에 미치지 못하는 사례가 반복된다.

**벤치마크 다양성**: 단일 벤치마크가 모델의 전반적 능력을 대표할 수 없다. 다차원 평가(지식, 추론, 코딩, 안전성, 공정성)를 종합하는 평가 프레임워크가 필요하다.

## 관련 문서

- [[humanity-last-exam]] -- HLE 벤치마크 상세
- [[swe-bench-pro]] -- SWE-bench Pro 상세
- [[swe-bench-ecosystem-2026]] -- SWE-bench 생태계
- [[browsecomp]] -- BrowseComp 벤치마크
- [[osworld-verified]] -- OSWorld 벤치마크
- [[terminal-bench-2-0]] -- Terminal-Bench 2.0
- [[metr-time-horizon-benchmark]] -- METR 시간 지평 벤치마크
- [[long-horizon-agent-benchmarks]] -- 장기 호흡 에이전트 벤치마크
- [[arc-agi-2]] -- ARC-AGI-2 추론 벤치마크
- [[livebench]] -- LiveBench 동적 벤치마크
- [[component-level-agent-evaluation]] -- 에이전트 평가 방법론
- [[multi-turn-agent-evaluation]] -- 다중 턴 에이전트 평가
