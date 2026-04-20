---
source: arxiv
arxiv_id: "2604.08377"
title: "SkillClaw: Let Skills Evolve Collectively with Agentic Evolver"
authors: ["DreamX Team"]
date: 2026-04-11
url: "https://arxiv.org/abs/2604.08377"
fetched: 2026-04-15
status: pending_ingest
---

## Abstract

SkillClaw is a framework for collective skill evolution in multi-user agent ecosystems, which treats cross-user and over-time interactions as the primary signal for improving skills. SkillClaw continuously aggregates trajectories generated during use and processes them with an autonomous evolver, which identifies recurring behavioral patterns and translates them into updates to the skill set by refining existing skills or extending them with new capabilities.

The resulting skills are maintained in a shared repository and synchronized across users, allowing improvements discovered in one context to propagate system-wide while requiring no additional effort from users.

## Key Points

- 핵심 기여: 다중 사용자 에이전트 생태계에서 스킬을 집단적으로 진화시키는 프레임워크
- 방법론: 사용 중 생성된 궤적을 자율적 evolver가 분석하여 반복 패턴을 스킬 업데이트로 변환
- 결과: WildClawBench에서 Qwen3-Max 기준 +42.1% 평균 성능 개선
- 공유 리포지토리: 한 맥락에서 발견된 개선이 시스템 전체로 전파
