---
title: Anthropic Multi-Agent Research System
category: agents
page_type: summary
tags: [agents, summary, anthropic, multi-agent, research]
sources: [raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md, raw/2026-04-10-hot-ai-topics-sources/agent-trees/05-anthropic-com-how-we-built-our-multi-agent-research-system.md]
created: 2026-04-10
updated: 2026-04-13
---
# Anthropic Multi-Agent Research System

Anthropic이 Claude Research 기능의 백엔드로 사용한 멀티 에이전트 연구 시스템을 설명하는 엔지니어링 글 요약이다. 단일 에이전트를 더 똑똑하게 만드는 대신, **리드 에이전트와 병렬 [[subagents|서브에이전트]]의 협업 구조**로 성능을 확장한 사례라는 점에서 중요하다.

## 핵심 내용

- 리드 에이전트가 사용자 질의를 해석하고 조사 전략을 세운다. [[orchestrator-worker-pattern|오케스트레이터-워커 패턴]]의 실제 프로덕션 사례이다.
- 서브에이전트들은 서로 다른 방향으로 병렬 탐색을 수행한다.
- 각 서브에이전트는 자기 컨텍스트 안에서 검색과 도구 사용을 반복하고, 결과만 압축해 반환한다.
- 마지막에는 citation agent가 근거 위치를 정리해 응답의 출처를 강화한다.

## 왜 중요한가

이 글은 멀티 에이전트 시스템이 단순한 아이디어 차원이 아니라, 실제 프로덕션급 Research 기능에 적용되었음을 보여준다. 특히 Anthropic이 내부 평가에서 **lead agent + parallel subagents** 구조가 단일 agent보다 크게 우수했다고 밝힌 점은, 오케스트레이션 자체가 성능 스케일링 레버라는 점을 뒷받침한다. [[agent-memory-systems|메모리 시스템]]과의 결합이 다음 단계 과제다.

## 설계 포인트

### 1. breadth-first 탐색에 강함
독립 방향을 동시에 파고들 수 있기 때문에, 검색 공간이 넓은 문제에서 강점을 보인다.

### 2. context window를 병렬로 확장
서브에이전트가 각자 독립 컨텍스트를 가지므로, 전체 시스템은 사실상 더 많은 토큰 예산을 병렬로 사용할 수 있다.

### 3. coordination cost가 생김
에이전트 수가 늘수록 tool design, evaluation, prompt engineering, coordination failure가 더 중요해진다.

## 실무 적용 관점

이 문서는 “멀티 에이전트가 좋다”가 아니라, **언제 멀티 에이전트가 비용을 정당화하는가**를 묻도록 만든다. 검색 범위가 넓고 병렬 탐색 가치가 큰 태스크에서는 유효하지만, 실시간 협업과 강한 상태 공유가 필요한 작업에서는 오히려 coordination cost가 병목이 될 수 있다.

## 원문이 다루는 흐름

원문은 대체로 `Benefits of a multi-agent system` → `Architecture overview for Research` → `Prompt engineering and evaluations for research agents` → `Effective evaluation of agents` → `Production reliability and engineering challenges` 순서로 전개된다. 따라서 `Anthropic Multi-Agent Research System` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: Benefits of a multi-agent system, Architecture overview for Research, Prompt engineering and evaluations for research agents, Effective evaluation of agents, Production reliability and engineering challenges
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **How we built our multi-agent research system \ Anthropic** — snapshot: `raw/hot-topics-sources/2026-04-10/006-how-we-built-our-multi-agent-research-system.md` · source: https://www.anthropic.com/engineering/multi-agent-research-system · 볼 섹션: 핵심 heading 추출이 제한적
- **How we built our multi-agent research system** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/agent-trees/05-anthropic-com-how-we-built-our-multi-agent-research-system.md` · source: https://www.anthropic.com/engineering/multi-agent-research-system · 볼 섹션: Benefits of a multi-agent system, Architecture overview for Research, Prompt engineering and evaluations for research agents, Effective evaluation of agents

## 역할 분해 표

| 역할 | 원문에서 맡는 일 | 설계상 이유 |
|---|---|---|
| lead agent | 질의를 해석하고 조사 계획을 세우며 서브태스크를 나눈다 | 병렬 탐색이 겹치지 않도록 문제를 먼저 구조화해야 하기 때문이다 |
| subagent | 독립 컨텍스트 안에서 검색·도구 사용·부분 정리를 수행한다 | breadth-first 탐색과 컨텍스트 분리를 동시에 얻는다 |
| citation agent | 최종 응답의 근거 위치를 정리한다 | "좋은 답"뿐 아니라 **검증 가능한 답**을 만들기 위해서다 |

## 프롬프트/평가 교훈

원문에서 특히 실무적으로 중요한 부분은 아키텍처 자체보다 **오케스트레이터를 어떻게 가르쳤는가**다.

- `Think like your agents`: 프롬프트를 고칠 때는 추상 원칙보다 실제 에이전트 시뮬레이션을 보며 실패 모드를 찾는 편이 훨씬 빠르다.
- `Teach the orchestrator how to delegate`: 서브에이전트에게는 목적, 출력 형식, 사용할 도구, 경계 조건이 함께 전달되어야 중복 조사와 공백을 줄일 수 있다.
- `Scale effort to query complexity`: 단순 질문에 과도한 병렬성을 쓰지 않도록 agent 수와 tool call 예산을 프롬프트 안에 명시하는 것이 중요하다.
- `Tool design and selection are critical`: MCP처럼 도구 수가 늘어날수록 툴 설명 품질 자체가 성능 레버가 된다.

## 관련 문서

- [[orchestrator-worker-pattern|Orchestrator-Worker Multi-Agent Pattern]]
- [[agent-trees|Hierarchical Planning with Agent Trees]]
- [[subagents|Subagents]]
