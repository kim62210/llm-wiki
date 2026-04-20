---
title: Scaling Managed Agents
category: tooling
page_type: summary
tags: [tooling, summary, anthropic, managed-[[coding-agent|agent]]s, infrastructure]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-running-agent-harnesses/03-anthropic-com-scaling-managed-agents-decoupling-the-brain-from-the-hands.md]
created: 2026-04-10
updated: 2026-04-13
---
# Scaling Managed Agents

Anthropic의 Managed Agents 설계 글 요약이다. 핵심 메시지는, 에이전트 시스템을 하나의 컨테이너에 다 넣는 대신 **brain / hands / session**을 분리된 인터페이스로 다뤄야 스케일과 복구 가능성이 생긴다는 점이다.

원문 URL: https://www.anthropic.com/engineering/managed-agents

## 핵심 내용

원문은 다음 순서로 전개된다: `Don't adopt a pet` → `The session is not Claude's context window` → `Many brains, many hands` → `Conclusion`.

- harness를 컨테이너에서 떼어내고 tool 호출 형태로 추상화한다.
- sandbox는 교체 가능한 cattle로 다룬다 (pet으로 다루면 안 됨).
- session log를 외부에 두어 harness가 죽어도 복구 가능하게 만든다.
- 보안 경계는 sandbox 안에서 토큰을 직접 다루지 못하게 만드는 방향으로 설계한다.
- Harness는 `execute(name, input) → string` 계약으로 추상화되어 모델 개선에도 안정적으로 유지된다.

## 왜 중요한가

이 글은 long-running agent 문제가 단순히 "더 좋은 모델을 쓰자"가 아니라, **세션 지속성, 보안, 재시작 가능성, 디버깅 가능성**의 문제라는 점을 매우 구체적으로 보여준다. [[tool-contracts-for-agents|Tool Contracts]] 관점에서도 핵심 레퍼런스가 된다.

## 실무 적용 관점

Managed agent를 설계할 때는 다음 세 가지를 먼저 봐야 한다:

1. 세션 로그가 어디에 남는가
2. harness와 sandbox가 어떻게 분리되는가
3. credential이 어느 경계 밖에 머무는가

[[claude-agent-sdk|Claude Agent SDK]]와 함께 읽으면 이론과 구현의 연결이 선명해진다.

## 관련 문서

- [[long-running-agent-harnesses|Agent Harnesses for Long-Running Coding Sessions]]
- [[claude-agent-sdk|Claude Agent SDK]]
- [[tool-contracts-for-agents|Tool Contracts & Writing Tools for Agents]]
