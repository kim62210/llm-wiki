---
title: SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios
category: papers
page_type: paper
tags: [paper, benchmarks, coding-agents, software-engineering]
sources: [raw/hot-topics-sources/2026-04-10/035-swe-evo-benchmarking-coding-agents-in-long-horizon-software-evolution.md]
created: 2026-04-10
updated: 2026-04-10
---

# SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios

코딩 에이전트를 단일 버그 수정이 아니라 release-note 기반의 다단계 진화 과제로 평가하는 long-horizon benchmark 논문이다.

## 핵심 기여

- 7개 성숙한 오픈소스 Python 프로젝트의 release notes를 기반으로 48개 long-horizon task 구성
- 평균 21개 파일, 874개 테스트 규모의 다중 수정 과제를 제시
- Fix Rate 같은 부분 진척도 지표를 도입

## 결과와 시사점

- GPT-5.4 + OpenHands가 SWE-EVO에서 25%에 그쳐, SWE-Bench Verified 72.8%와 큰 격차를 드러냄
- 현재 coding agent가 sustained multi-file reasoning에서 약하다는 점을 정량화

## 한계

Python OSS 중심 구성이라 언어·도메인 다양성 한계가 있고, benchmark 설계 자체가 특정 스타일의 evolution task에 편향될 수 있다.

## 실무 적용 관점

실무 팀은 '벤치마크 점수'보다 **한 이슈를 넘어 장기 변경을 유지할 수 있는가**를 봐야 한다는 경고로 읽을 가치가 크다.

## 관련 문서

- [[long-horizon-agent-benchmarks]]
- [[swe-bench-pro]]
- [[terminal-bench-2-0]]
