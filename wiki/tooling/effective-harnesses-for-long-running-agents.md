---
title: Effective Harnesses for Long-Running Agents
category: tooling
page_type: summary
tags: [tooling, summary, anthropic, harness, long-running-agents]
sources: [raw/hot-topics-sources/2026-04-10/041-effective-harnesses-for-long-running-agents.md]
created: 2026-04-10
updated: 2026-04-10
---

# Effective Harnesses for Long-Running Agents

Anthropic이 장기 실행 에이전트를 다루기 위해 제안한 하네스 설계 글 요약이다. 핵심은 모델이 긴 작업을 한 번에 끝내리라고 기대하는 대신, **초기 환경 설정(initializer)과 반복 실행(coding agent)** 을 분리해 세션을 이어 붙이는 것이다.

## 핵심 내용

- 에이전트는 여러 context window를 넘나들며 일해야 한다.
- compaction만으로는 세션 간 일관성을 보장하기 어렵다.
- initializer agent가 환경과 작업 구조를 잡고,
- coding agent가 한 세션마다 **작은 진전 + 깨끗한 상태**를 남기는 구조가 효과적이다.

## 중요한 설계 요소

### initializer agent
처음 한 번만 실행되며, 프로젝트 구조와 진행 파일을 설정한다.

### progress artifact
`claude-progress.txt` 같은 외부 상태 파일이 세션 간 기억을 이어주는 핵심이 된다.

### feature list
작업을 구체적 기능 단위로 쪼개고, 아직 실패 상태임을 명시해 premature completion을 막는다.

## 왜 중요한가

이 글은 long-running agent 문제를 “모델이 더 길게 생각하게 하자”가 아니라, **세션 경계에서 상태를 어떻게 외부화할 것인가**의 문제로 바꿔 놓는다. 이는 이후 harness engineering 담론의 중요한 기준점이 되었다.

## 실무 적용 관점

장기 실행 에이전트는 보통 두 가지로 망가진다:

1. 한 번에 너무 많은 걸 하려다 context를 소모해버림  
2. 중간 상태를 보고 이미 끝났다고 착각함

이 문서는 이를 막기 위한 가장 실용적인 대책으로 **초기화 단계, 점진적 진전, 외부 상태 파일**을 제시한다.

## 관련 문서

- [[long-running-agent-harnesses|Agent Harnesses for Long-Running Coding Sessions]]
- [[generator-evaluator-architecture|Generator-Evaluator Architecture]]
- [[claude-agent-sdk|Claude Agent SDK]]

