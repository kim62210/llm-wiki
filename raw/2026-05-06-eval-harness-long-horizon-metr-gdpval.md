---
source: METR + OpenAI papers/posts
url: https://metr.org/ + https://openai.com/index/gdpval/
title: Long-horizon agent harness — METR HCAST / GDPval / Time Horizon
fetched: 2026-05-06
status: pending_ingest
---

# Long-Horizon Agent Evaluation Harness

장기 (1분~수일) 작업의 agent 성능 측정 인프라. 단발성 정답 비교가 아닌 **인간 baseline 시간 + 부분 성공 + scaffold sensitivity** 를 평가에 포함.

## 1) METR HCAST (Human-Calibrated Autonomy Software Tasks)

### 정체성

> 189 tasks across machine learning, cybersecurity, software engineering, and general reasoning domains designed to capture realistic challenges of widely varying complexity that typically require multi-step sequential decision-making, are largely derived from real-world work, take between 1-2 minutes and 8+ hours, and undergo multiple stages of manual quality assurance and review.

(METR HCAST whitepaper)

핵심 차별점:
- 모든 task 가 **human baseline time 측정** 거침 (실제 사람이 풀게 해서 시간 기록)
- task 길이가 1분~8+시간 으로 광범위
- 4개 도메인 (ML, cybersec, SWE, general reasoning)

### Time Horizon 1.1 (2026-01-29) 업데이트

| 측면 | TH 1.0 | TH 1.1 |
|---|---|---|
| Task 수 | 170 | 228 (+34%) |
| Long task (8h+) | 14 | 31 |
| 추가 | - | HCAST 73개 신규 |
| 제거 | - | 15개 |
| 갱신 | - | 53개 |
| 인프라 | Vivaria (in-house) | **Inspect AI (UK AISI)** |

> "Only 5 of 31 long tasks use measured human baselines; the remainder rely on estimates."

장기 task 는 baseline 측정 비용이 폭증해 추정에 의존하는 한계 존재.

### 50%-time-horizon metric

> "the model's 50% time horizon is the human task completion time at which this curve intersects the 50% success probability threshold, representing the estimated time a human expert would typically take to complete tasks which the AI model can complete with 50% success rate."

방법:
1. 각 task 에 (human baseline 시간, AI 성공/실패) 페어 수집
2. logistic regression 으로 task 시간 → AI 성공 확률 곡선 fit
3. 50% 성공 임계점에서의 task 시간 = "50% time horizon"

추세 결과: 2023 이후 doubling time 165일 → TH 1.1 에서 131일 (20% 빠름).

### Vivaria → Inspect 마이그레이션 시사점

> "two models (GPT-4o, o3) scored 'statistically significantly higher' under Vivaria, suggesting 'scaffold sensitivity.'"

같은 task, 같은 모델인데 harness 가 다르면 결과가 통계적으로 다름 → **harness 자체가 결과에 큰 영향**. 이는 long-horizon agent eval 의 reproducibility 위험을 정면으로 드러내는 사례.

## 2) OpenAI GDPval

### 정체성

> "GDPval covers the top 9 sectors contributing to U.S. GDP, with at least 30 tasks per occupation in the full set across 44 occupations."

OpenAI 가 2025-10 공개 (arXiv 2510.04374). real-world economically valuable task 평가.

### Task 구조

> "Unlike traditional benchmarks, GDPval tasks are not simple text prompts. They come with reference files and context, and the expected deliverables span documents, slides, diagrams, spreadsheets, and multimedia."

- **참조 파일** (PDF, 스프레드시트, 이미지 등)
- **결과물 (deliverable)**: 문서, 슬라이드, 다이어그램, 스프레드시트, 멀티미디어
- **각 task 는 실제 expert 가 만든 work product 기반**

### 평가 방법

> "The primary evaluation metric is head-to-head human expert comparison, and an experimental automated grader service is provided for the 220 open-sourced gold subset of tasks."

- **주 평가**: human expert pairwise comparison (winner 결정)
- **보조 평가**: automated grader (220 gold subset, experimental)
- 220개는 open-source, 나머지는 비공개

### 도메인 (9 sectors, 44 occupations)

미국 GDP 기여 상위 9개 sector — 의료, 법률, 금융, IT/SWE, 마케팅, 미디어 제작, 부동산, 교육, 행정 등 (정확한 sector 분류는 paper 참조).

### Performance reference (2026)

- GPT-5.5: 84.9% on GDPval (2026-04 launch)
- GPT-5.2 Thinking: 70.9% of comparisons "beats or ties top industry professionals"

### 다른 long-horizon eval 과의 차이

| 측면 | GDPval | HCAST | SWE-bench |
|---|---|---|---|
| 1차 metric | human pairwise | 50%-time-horizon | resolved (test pass) |
| Task 출처 | expert deliverable | real-world software work | GitHub issue |
| Deliverable | 다양 (문서/슬라이드 등) | software artifact | code patch |
| 자동 채점 | 220 gold subset 만 | task-specific scorer | unit test |
| 도메인 | 경제적 가치 (44 직업) | software/ML/security | Python OSS |

GDPval 의 **head-to-head human comparison** 은 비용이 크지만 객관성이 높고, AI 가 실제 산업 전문가 대체 가능성을 가장 직접적으로 측정하는 패턴이다.

## 3) Expert-SWE (OpenAI 내부)

OpenAI 가 GPT-5.x 평가에 사용하는 internal frontier eval:
- median human completion time 20시간
- long-horizon coding task
- 비공개 (논문/공식 spec 없음)

이는 외부에서 검증 불가능한 내부 harness 의 한 예 — frontier AI 회사들이 점점 자체 long-horizon eval 을 보유하는 추세.

## 공통 인프라 패턴: long-horizon agent harness

> "Agents navigate complex environments over extended time horizons, using tools from browsers to bash shells, often consuming hundreds of thousands of tokens per rollout, demanding purpose-built infrastructure that tracks not just what agents output, but how they achieve it, what they cost, and where they break."

요구 인프라:
1. **장기 sandbox 유지** — agent 가 시간 차이로 재진입해도 환경 상태 보존
2. **tool 사용 트래킹** — bash 호출, 파일 변경, network request 모두 로깅
3. **token cost 추적** — rollout 별 입출력 token 추적
4. **partial credit / progress 측정** — 완전 실패가 아니라 어디까지 진행했는지
5. **scaffold ablation 가능성** — 같은 모델 + 다른 prompt/tool → 결과 변동 측정

이러한 요구가 Inspect AI 같은 framework 가 부상하는 근본 이유. Inspect 의 SandboxEnvironment + async exec + grading log 가 위 5개 요구를 모두 충족.

## Holistic Agent Leaderboard (HAL)

Princeton CS 가 공개하는 통합 dashboard (https://hal.cs.princeton.edu/) — 같은 agent 를 여러 harness (SWE-bench, GAIA, WebArena, ...) 에 동시에 돌려 **scaffold 변동성** 을 정량화. arxiv 2510.11977 에서 `Holistic Agent Leaderboard` 로 공식화.

## 출처

- METR HCAST whitepaper: https://metr.org/hcast.pdf
- METR Time Horizon 1.1 blog: https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Epoch AI METR Time Horizons: https://epoch.ai/benchmarks/metr-time-horizons
- METR research: https://metr.org/research/
- OpenAI GDPval landing: https://openai.com/index/gdpval/
- GDPval paper: https://arxiv.org/pdf/2510.04374 (cdn copy: https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf)
- GDPval-AA leaderboard: https://artificialanalysis.ai/evaluations/gdpval-aa
- GPT-5.5 launch (84.9% GDPval): https://openai.com/index/introducing-gpt-5-5/
- HAL paper: https://arxiv.org/pdf/2510.11977
- HAL dashboard: https://hal.cs.princeton.edu/
