---
title: MCP Roadmap (Development)
category: tooling
page_type: summary
tags: [tooling, summary, mcp, roadmap, governance]
sources: [raw/2026-04-10-hot-ai-topics-sources/model-context-protocol/02-modelcontextprotocol-io-mcp-roadmap.md]
created: 2026-04-10
updated: 2026-04-13
---
# MCP Roadmap (Development)

Model Context Protocol 공식 사이트의 development roadmap 문서 요약이다. 블로그 글보다 더 구조화된 형태로 작업 그룹, 기여 절차, governance 흐름을 보여 준다.

## 핵심 내용

- MCP roadmap을 단순 릴리스 일정이 아니라 workstream 중심으로 정리한다.
- contributor communication, working groups, governance, SEP 절차를 연결한다.
- protocol 발전이 소수 maintainers 중심에서 커뮤니티 기반 구조로 이동했음을 보여준다.

## 왜 중요한가

블로그 로드맵은 우선순위를 설명하고, 이 문서는 실제로 **어떻게 참여하고 어떻게 진화하는지**를 보여 준다. 그래서 구현자나 기여자 입장에서는 이 문서가 더 직접적이다.

## 실무 적용 관점

MCP를 채택하는 조직은 스펙만 보는 것으로 끝나지 않는다. roadmap / governance / SEP 흐름을 이해해야 향후 변경과 호환성 리스크를 더 잘 예측할 수 있다.

## 원문이 다루는 흐름

원문은 대체로 `Roadmap - Model Context Protocol` → `Get Involved` → `Propose Changes` → `Governance` → `Working Group Charters` 순서로 전개된다. 따라서 `MCP Roadmap (Development)` 페이지도 세부 API 목록보다 **입문 → 구조 이해 → 운영 확장**의 흐름으로 읽는 편이 좋다.

- 따라가야 할 순서: Roadmap - Model Context Protocol, Get Involved, Propose Changes, Governance, Working Group Charters
- 위키에 남겨야 할 축: 입문 경로, 핵심 구조, 다음에 읽을 세부 문서

## 읽기 포인트

- 이 문서는 **원문을 어떤 순서로 읽어야 실무 판단으로 이어지는가**라는 질문을 붙잡고 읽으면 훨씬 덜 얕아진다.
- 소개 문단만 읽고 끝내지 말고, 원문 snapshot에서 실제 섹션 이름·예시·제약 조건을 다시 확인하는 습관이 중요하다.
- summary 문서는 결론 고정본이 아니라 읽기 가이드다. 따라서 입문, 세부 문서, 운영 문서를 어떤 순서로 볼지까지 안내해야 위키 품질이 올라간다.
- 공식 문서/논문/저장소가 함께 있으면 발표 글 하나만 믿지 말고, 사양 문서와 구현 저장소를 교차 확인하는 것이 안전하다.

## source 메모

- **Roadmap - Model Context Protocol** — snapshot: `raw/2026-04-10-hot-ai-topics-sources/model-context-protocol/02-modelcontextprotocol-io-mcp-roadmap.md` · source: https://modelcontextprotocol.io/development/roadmap · 볼 섹션: Roadmap - Model Context Protocol, Get Involved, Propose Changes, Governance

## 원문 기반 상세 해석

`MCP Roadmap (Development)`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `Roadmap - Model Context Protocol`이며, 원문 URL은 `https://modelcontextprotocol.io/development/roadmap`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, [​](https://modelcontextprotocol.io/development/roadmap#sep-prioritization), [​](https://modelcontextprotocol.io/development/roadmap#priority-areas), [​](https://modelcontextprotocol.io/development/roadmap#1-transport-evolution-and-scalability), [​](https://modelcontextprotocol.io/development/roadmap#2-[[coding-agent|agent]]-communication)` 쪽에 모인다.

자동 추출된 원문 단서는 `# Roadmap - Model Context Protocol; - 원본 URL: https://modelcontextprotocol.io/development/roadmap; - 연결된 토픽: MCP 2026 Roadmap & Enterprise Readiness; Title: Roadmap - Model Context Protocol`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. summary 노드는 원문 목차를 대체하지 않고, 독자가 원문으로 돌아갈 때 어떤 순서로 읽을지 알려 주는 압축 지도여야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서

- [[the-2026-mcp-roadmap|The 2026 MCP Roadmap]]
- [[mcp-[[mcp-specification-2025-11-25|specification]]-2025-11-25|MCP Specification 2025-11-25]]
- [[model-context-protocol-mcp|Model Context Protocol (MCP)]]

