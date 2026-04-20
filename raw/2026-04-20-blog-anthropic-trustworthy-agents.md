---
source: anthropic_research
title: "Trustworthy agents in practice"
authors: ["Anthropic"]
date: 2026-04-09
url: "https://www.anthropic.com/research/trustworthy-agents"
fetched: 2026-04-20
status: pending_ingest
tags: [agent-safety, agent-oversight, prompt-injection, plan-mode, trust-framework, policy]
---

## Summary

Claude Code, Claude Cowork 같은 고자율 에이전트 시스템이 확산되면서 productivity gain과 risk가 동시에 커지는 상황에서, Anthropic의 "신뢰 가능한 에이전트" 설계 원칙 5가지를 제시한 실무 가이드.

## 에이전트의 네 가지 구성 요소

1. **모델(model)** — 추론·판단 핵심
2. **하니스(harness)** — 운영 지시·도구 호출 프로토콜
3. **도구(tools)** — 실행 가능한 액션
4. **환경(environment)** — 실행 컨텍스트 (파일시스템, 네트워크 등)

각 구성 요소는 capability이자 control point — 권한 축소 레버로 사용 가능.

## 신뢰 프레임워크 5원칙

| 원칙 | 요약 |
|------|------|
| **Human Control** | 사용자가 도구 가용성·승인 요구 수준 결정 |
| **Goal Alignment** | 애매한 상황에서는 clarification 요청하도록 학습 |
| **Security** | 모델·하니스·도구·환경 각 레이어에 다층 방어 |
| **Transparency** | 능력·한계 증거 공유 |
| **Privacy** | 에이전트 작동 전반의 데이터 보호 |

## Plan Mode

- 개별 액션 승인 → 종합 전략 검토로 오버사이트 전환
- 복잡한 멀티스텝 작업에서 friction 감소

## 서브에이전트 조정

- 여러 에이전트가 병렬로 다른 작업 부분을 처리하는 새 패러다임
- 새로운 오버사이트 접근 필요 (개별 에이전트가 아닌 조정자 수준)

## 프롬프트 인젝션 방어

- 단일 방어는 보장하지 않음 → 다층 방어 필수
- 모델 학습(injection 패턴 인식) + production 트래픽 모니터링 + external red-teaming
- 사용자·조직은 도구, 권한, 환경을 신중히 구성해야 함

## 정량 관찰

- 사용자 interrupt 빈도는 과제 복잡도와 큰 차이 없음
- Claude 자체 check-in은 복잡한 과제에서 약 2배 — 적절히 캘리브레이션됨

## 업계·표준 권고

- Prompt injection 저항성·불확실성 탐지에 대한 표준 벤치마크
- 제3자 검증을 포함한 평가 생태계
- MCP(Model Context Protocol) 같은 open standards로 인프라에 보안 내재화

## Raw 요약 키워드
agent safety, Plan Mode, harness, MCP, prompt injection defense, check-in frequency, five principles
