---
title: OMC Agent Catalog
aliases: ["OMC Agent Catalog", "Agents"]
category: agents
page_type: project-internal
project: oh-my-claudecode
tags: [omc, agents, catalog, lanes, delegation]
sources: [raw/2026-04-09-omc-AGENTS.md, raw/2026-04-09-omc-ARCHITECTURE.md, raw/2026-04-09-omc-GETTING-STARTED.md]
created: 2026-04-09
updated: 2026-04-09
---

# OMC Agent Catalog

> OMC의 19개 전문 에이전트를 4개 레인(Build/Analysis, Review, Domain, Coordination)으로 분류.

## 호출 방법

OMC 에이전트는 다음 중 하나로 호출한다:

- **Claude Code 커스텀 프롬프트**: `/prompts:name` (예: `/prompts:architect "review auth module"`)
- **슬래시 명령**: `/oh-my-claudecode:<agent-name>` 형태
- **Task 툴 위임**: 부모 에이전트가 `Task(subagent_type="oh-my-claudecode:executor", model="sonnet", prompt=...)` 호출
- **child_agent_protocol**: 부모가 `~/.codex/prompts/{role}.md` 읽어서 `spawn_agent(message: prompt)` 호출

## Build/Analysis Lane (빌드·분석)

개발 라이프사이클 전반을 커버하는 주력 에이전트들.

| 에이전트 | 모델 | 역할 | Does NOT |
|---|---|---|---|
| `explore` | haiku | 코드베이스 탐색, 파일/심볼 매핑 | 구현, 계획 |
| `analyst` | opus | 요구사항 명확화, 숨은 제약 발견, 수용 기준 | 코드 분석, 기획 |
| `planner` | opus | 태스크 시퀀싱, 실행 계획, 리스크 플래그 | 요구사항 분석, 플랜 리뷰 |
| `architect` | opus | 시스템 설계, 경계/인터페이스, 장기 트레이드오프 | 요구사항 수집, 기획 |
| `debugger` | sonnet | 근본원인 분석, 회귀 격리, 실패 진단 | - |
| `executor` | sonnet | 코드 구현, 리팩터링, 기능 작업 | - |
| `verifier` | sonnet | 완료 근거, 주장 검증, 테스트 적정성 확인 | - |
| `tracer` | sonnet | 증거 기반 인과 추적, 경쟁 가설 분석 | - |

### 일반 워크플로우

```
explore → analyst → planner → critic → executor → verifier
(탐색)   (분석)    (시퀀싱)  (리뷰)   (구현)    (확인)
```

## Review Lane (리뷰)

핸드오프 전 품질 게이트. 정확성과 보안 이슈를 잡는다.

| 에이전트 | 모델 | 역할 |
|---|---|---|
| `style-reviewer` | - | 포맷팅, 네이밍, 관용구, 린트 규약 |
| `code-reviewer` | opus | 종합 리뷰 — 로직 결함, 유지보수성, 안티패턴, 스타일, 성능, API 계약, 하위 호환성 |
| `api-reviewer` | - | API 계약, 버저닝, 하위 호환성 |
| `security-reviewer` | sonnet | 취약점, 신뢰 경계, authn/authz |
| `performance-reviewer` | - | 핫스팟, 복잡도, 메모리/지연 최적화 |

## Domain Lane (도메인 전문)

도메인 지식이 필요할 때 호출되는 전문가들.

| 에이전트 | 모델 | 역할 |
|---|---|---|
| `test-engineer` | sonnet | 테스트 전략, 커버리지, flaky 테스트 강화 |
| `designer` | sonnet | UI/UX 아키텍처, 인터랙션 설계 |
| `writer` | haiku | 문서, 마이그레이션 노트, 사용자 가이드 |
| `qa-tester` | sonnet | tmux 기반 인터랙티브 CLI/서비스 런타임 검증 |
| `scientist` | sonnet | 데이터 분석, 통계 리서치 |
| `git-master` | sonnet | 커밋 전략, 히스토리 위생, 리베이스 관리 |
| `document-specialist` | sonnet | 외부 문서/API/SDK 레퍼런스 조사 |
| `code-simplifier` | opus | 코드 명확성, 단순화, 유지보수성 개선 |
| `dependency-expert` | - | 외부 SDK/API/패키지 평가 |
| `quality-strategist` | - | 품질 전략, 릴리즈 준비도, 리스크 평가 |
| `researcher` | - | 외부 문서 및 레퍼런스 리서치 |

## Coordination Lane (조율)

다른 에이전트들의 플랜과 설계를 비판적으로 검토. 플랜은 이 게이트를 통과해야 실행으로 넘어간다.

| 에이전트 | 모델 | 역할 |
|---|---|---|
| `critic` | opus | 플랜/설계 갭 분석, 다각도 리뷰 |
| `vision` | - | 이미지/스크린샷/다이어그램 분석 |

## Product Lane (제품 특화)

제품 발굴과 UX 감사 전용.

| 에이전트 | 모델 | 역할 |
|---|---|---|
| `product-manager` | - | 문제 framing, 페르소나/JTBD, PRD 작성 |
| `ux-researcher` | - | 휴리스틱 감사, 사용성, 접근성 |
| `information-architect` | - | 분류 체계, 내비게이션, 검색성 |
| `product-analyst` | - | 제품 지표, 퍼널 분석, 실험 |

## 에이전트 선택 가이드

| 태스크 | 추천 에이전트 | 모델 |
|---|---|---|
| 빠른 코드 lookup | `explore` | haiku |
| 기능 구현 | `executor` | sonnet |
| 복잡한 리팩터링 | `executor` (opus) | opus |
| 단순 버그 수정 | `debugger` | sonnet |
| 복잡한 디버깅 | `architect` | opus |
| UI 컴포넌트 | `designer` | sonnet |
| 문서 작성 | `writer` | haiku |
| 테스트 전략 | `test-engineer` | sonnet |
| 보안 리뷰 | `security-reviewer` | sonnet |
| 종합 코드 리뷰 | `code-reviewer` | opus |
| 데이터 분석 | `scientist` | sonnet |

## 에이전트 역할 경계

OMC는 각 에이전트가 **하지 말아야 할 일**도 명시해 컨텍스트 경계를 유지한다:

| 에이전트 | Does | Does Not |
|---|---|---|
| `architect` | 코드 분석, 디버깅, 검증 | 요구사항 수집, 기획 |
| `analyst` | 요구사항 갭 찾기 | 코드 분석, 기획 |
| `planner` | 태스크 플랜 작성 | 요구사항 분석, 플랜 리뷰 |
| `critic` | 플랜 품질 리뷰 | 요구사항 분석, 코드 분석 |

이 경계는 에이전트가 자기 역할을 벗어나지 않도록 프롬프트에 강제된다.

## 팀 구성 패턴

전형적 시나리오별 조합:

| 시나리오 | 에이전트 순서 |
|---|---|
| **Feature Development** | `analyst → planner → executor → test-engineer → code-reviewer → verifier` |
| **Anti-Slop Cleanup** | `planner → test-engineer → executor → code-reviewer → verifier` |
| **Bug Investigation** | `explore + debugger + executor + test-engineer + verifier` |
| **Code Review** | `style-reviewer + code-reviewer + api-reviewer + security-reviewer` |
| **Product Discovery** | `product-manager + ux-researcher + product-analyst + designer` |
| **UX Audit** | `ux-researcher + information-architect + designer + product-analyst` |

## 에이전트 숏컷 (자연어 → 에이전트)

매직 키워드로 직접 호출 가능 (슬래시 없이):

| 키워드 | 내부 에이전트 |
|---|---|
| `analyze` | debugger |
| `deepsearch` | explore |
| `tdd` | test-engineer |
| `build-fix` | debugger |
| `code-review` | code-reviewer |
| `security-review` | security-reviewer |
| `frontend-ui-ux` | designer |
| `git-master` | git-master |

## 커스터마이징

`~/.claude/agents/` 하위의 에이전트 파일을 직접 편집해 동작을 변경할 수 있다:

```yaml
---
name: architect
description: Your custom description
tools: Read, Grep, Glob, Bash, Edit
model: opus
---
Your custom system prompt here...
```

## 실무 고려사항

- **19개 에이전트를 다 외우지 말 것**: 매직 키워드와 자동 라우팅을 활용. 필요할 때 카탈로그 참조
- **역할 침범 방지**: architect에게 요구사항 수집 시키면 품질 저하 → 적절한 에이전트 선택
- **critic 게이트**: 중요한 플랜은 critic을 반드시 통과시킬 것
- **child agent 상한**: 최대 6개 동시 실행. 그 이상 필요하면 Team 모드 사용

## 관련 문서

- [[oh-my-claudecode (OMC)]]
- [[Multi-Agent Orchestration]]
- [[OMC Model Routing]]
- [[OMC Delegation Categories]]
- [[OMC Execution Modes]]
