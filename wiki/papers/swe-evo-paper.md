---
title: SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios
category: papers
page_type: paper
tags: [paper, [[swe-bench-pro|benchmark]]s, coding-agents, software-engineering]
sources: [raw/hot-topics-sources/2026-04-10/035-swe-evo-benchmarking-coding-agents-in-long-horizon-software-evolution.md, raw/2026-04-10-hot-ai-topics-sources/long-horizon-agent-benchmarks/02-arxiv-org-swe-evo-benchmarking-coding-agents-in-long-horizon-software-.md]
created: 2026-04-10
updated: 2026-04-13
---
# SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios

코딩 에이전트를 단일 버그 수정이 아니라 release-note 기반의 다단계 진화 과제로 평가하는 long-horizon benchmark 논문이다.

## 핵심 기여

- 7개 성숙한 오픈소스 Python 프로젝트의 release notes를 기반으로 48개 long-horizon task 구성
- 평균 21개 파일, 874개 테스트 규모의 다중 수정 과제를 제시
- Fix Rate 같은 부분 진척도 지표를 도입

## 결과와 시사점

- GPT-5.4 + OpenHands가 SWE-EVO에서 25%에 그쳐, SWE-Bench Verified 72.8%와 큰 격차를 드러냄
- 현재 [[coding-agent|coding agent]]가 sustained multi-file reasoning에서 약하다는 점을 정량화

## 한계

Python OSS 중심 구성이라 언어·도메인 다양성 한계가 있고, benchmark 설계 자체가 특정 스타일의 evolution task에 편향될 수 있다.

## 실무 적용 관점

실무 팀은 '벤치마크 점수'보다 **한 이슈를 넘어 장기 변경을 유지할 수 있는가**를 봐야 한다는 경고로 읽을 가치가 크다.

## 문제 설정

`SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **2512.18470 SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios** — https://arxiv.org/abs/2512.18470 · 초록 단서: Existing benchmarks for AI coding agents focus on isolated, single-issue tasks such as fixing a bug or adding a small feature. However, real-world [[coding-agent|software engineering]] is a long... · snapshot: `raw/hot-topics-sources/2026-04-10/035-swe-evo-benchmarking-coding-agents-in-long-horizon-software-evolution.md`
- **SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios** — https://arxiv.org/abs/2512.18470 · 초록 단서: Existing benchmarks for AI coding agents focus on isolated, single-issue tasks such as fixing a bug or adding a small feature. However, real-world software engineering is a long... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-horizon-agent-benchmarks/02-arxiv-org-swe-evo-benchmarking-coding-agents-in-long-horizon-software-.md`

## 원문 기반 상세 해석

`SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `[2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios`이며, 원문 URL은 `https://arxiv.org/abs/2512.18470`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, quick links, Submission history, Access Paper:, References & Citations` 쪽에 모인다.

자동 추출된 원문 단서는 `[2512.18470] SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios; Skip to main content; Learn about arXiv becoming an independent nonprofit.; We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. 논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서
- [[reveal-paper]]
- [[are-gaia2-paper]]

- [[long-horizon-agent-benchmarks]]
- [[swe-bench-pro]]
- [[terminal-bench-2-0]]
