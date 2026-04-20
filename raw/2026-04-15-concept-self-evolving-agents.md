---
source: web
title: "Self-Evolving Agents (SEA Paradigm)"
url: "https://medium.com/@linz07m/self-evolving-agents-ii-1551b6fb3bd2"
date: 2026-04-01
fetched: 2026-04-15
status: pending_ingest
---

## Overview

현재 LLM 기반 에이전트는 에피소딕 태스크 실행에서 강한 성능을 보이지만, 정적 툴셋과 에피소딕 기억상실(episodic amnesia)에 의해 제약된다. Self-Evolving Agent(SEA) 패러다임은 에이전트가 사용 과정에서 도구, 스킬, 메모리를 스스로 진화시키는 방향을 제시.

## Key Concepts

- **정적 에이전트의 한계**: 고정된 도구셋, 에피소드 간 학습 없음
- **SEA 패러다임**: 에이전트가 경험에서 학습하여 스킬/도구/프로토콜을 자율적으로 개선
- **SEA-Eval 벤치마크**: SEA 특성을 평가 -- 태스크 내 실행 신뢰성 + 장기 진화 성능

## Core Characteristics

1. **Intra-task Execution Reliability**: 단일 태스크 내에서의 안정적 실행
2. **Long-term Evolutionary Performance**: 시간에 걸친 지속적 성능 향상
3. **Tool/Skill Discovery**: 새로운 도구와 스킬의 자율적 발견
4. **Memory Accumulation**: 경험의 축적과 재활용

## Related Work

- SkillClaw: 집단적 스킬 진화 프레임워크 (DreamX Team)
- SkillRL: 재귀적 스킬 증강 RL
- Externalization 패러다임: 메모리, 스킬, 프로토콜의 외부화
