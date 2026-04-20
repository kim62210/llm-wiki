---
title: Agent Skills Specification
category: agents
page_type: summary
tags: [agents, summary, skills, specification, agent-skills]
sources: [raw/hot-topics-sources/2026-04-10/022-agent-skills-specification.md]
created: 2026-04-10
updated: 2026-04-13
---
# Agent Skills Specification

Agent Skills 포맷을 공식적으로 정의하는 specification 문서 요약이다. [[agent-skills|Agent Skills]] 개념의 기술적 상세를 다룬다. SKILL.md 기반 능력 번들을 어떻게 배치하고 기술하며, 클라이언트가 이를 어떻게 로딩해야 하는지에 대한 규약을 제공한다.

## 핵심 내용

- skill의 디렉토리 구조를 표준화한다.
- SKILL.md의 frontmatter 필드(name, description 등)를 정의한다.
- skill 제작자와 client 구현자 양쪽을 위한 규칙을 제공한다.
- 단순 텍스트 프롬프트가 아니라 **재사용 가능한 능력 패키지**라는 관점을 강조한다.

## 왜 중요한가

에이전트 생태계가 커질수록 “능력을 어떻게 묶고 배포할 것인가”가 중요해진다. 이 specification은 skill을 특정 벤더 기능이 아니라 **도구 간 호환 가능한 패키징 규약**으로 정리한다는 점에서 의미가 크다. [[agentic-ai-foundation|에이전틱 생태계]]에서 [[agent-memory-systems|메모리]]와 함께 에이전트 역량의 핵심 축을 이룬다.

## 실무 적용 관점

스킬 시스템을 설계할 때 중요한 것은 프롬프트 한 파일이 아니라:

1. 어떤 메타데이터가 discovery를 돕는가  
2. 어떤 리소스를 lazy-loading할 것인가  
3. skill 실행 범위를 얼마나 명확히 구분할 것인가

라는 점이다. 이 문서는 바로 그 계약을 제공한다.

## 원문이 다루는 흐름

참조 source는 `Agent Skills Specification`를 하나의 정의로 닫지 않고, 주변 설계 맥락과 읽기 순서를 함께 제공한다. 그래서 짧은 소개문만으로 끝내기보다 **구조와 적용 포인트**를 같이 정리해야 위키 문서로서 가치가 생긴다.

- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **Specification - Agent Skills** — snapshot: `raw/hot-topics-sources/2026-04-10/022-agent-skills-specification.md` · source: https://agentskills.io/specification · 볼 섹션: 핵심 heading 추출이 제한적

## 문서에서 바로 확인할 계약

| 계약 요소 | 원문에서 주는 신호 | 위키 관점에서의 해석 |
|---|---|---|
| 디렉토리 구조 | `SKILL.md`가 최소 필수 파일이고 `scripts/`, `references/`, `assets/`는 선택적 디렉토리로 제시된다 | skill은 "프롬프트 한 장"이 아니라 실행 코드·참고 자료·템플릿을 함께 묶는 배포 단위다 |
| frontmatter | `name`, `description`가 필수이고 `license`, `compatibility`, `metadata`, `allowed-tools`는 선택이다 | discovery와 안전한 실행 범위를 frontmatter 계약으로 표준화하려는 의도가 분명하다 |
| progressive disclosure | 큰 설명을 한 파일에 다 넣지 말고 필요할 때만 references/scripts를 읽게 한다 | 컨텍스트 예산을 아끼면서도 skill 패키지를 풍부하게 유지하는 핵심 패턴이다 |
| validation | 형식 제약과 파일 참조 규칙을 별도 항목으로 둔다 | client 구현체가 skill을 신뢰하려면 로딩 전에 기계적으로 검사 가능한 규칙이 필요하다는 뜻이다 |

## 제작자 체크리스트

- 설명문은 "무엇을 하는가"보다 **언제 써야 하는가 / 언제 쓰지 말아야 하는가**를 먼저 드러내야 discovery 품질이 올라간다.
- `scripts/`는 반복 가능한 동작을 코드로 옮길 때 쓰고, 긴 배경지식은 `references/`로 밀어 progressive disclosure를 유지하는 편이 좋다.
- `allowed-tools` 같은 실험적 필드는 편의 기능이지만, 실제로는 skill 본문 안에 **도구 권한 경계와 실패 시 fallback**를 같이 적어두는 편이 안전하다.

## 관련 문서

- [[agent-skills|Agent Skills]]
- [[writing-effective-tools-for-agents|Writing Effective Tools for Agents]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]
