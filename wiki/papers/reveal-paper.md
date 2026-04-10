---
title: ReVeal: Self-Evolving Code Agents via Reliable Self-Verification
category: papers
page_type: paper
tags: [paper, coding-agents, self-verification, software-engineering]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/04-arxiv-org-reveal-self-evolving-code-agents-via-iterative-generation-ve.md]
created: 2026-04-10
updated: 2026-04-10
---

# ReVeal: Self-Evolving Code Agents via Reliable Self-Verification

코드 에이전트가 자기검증 루프를 통해 스스로 진화하도록 만드는 구조를 제안한 논문이다.

## 핵심 기여

- code generation과 verification을 반복 루프로 결합
- self-verification을 신뢰 가능한 개선 신호로 사용
- coding agent를 점진적으로 개선하는 자기진화 구조를 제시

## 결과와 시사점

- coding agent의 품질은 단일 generation보다 verifier 품질과 feedback loop 설계에 강하게 좌우된다.
- reliable verification은 self-improving agent 설계의 중요한 기반이 된다.

## 한계

verification이 잘못 설계되면 루프 전체가 잘못된 방향으로 수렴할 수 있다. 따라서 verifier의 신뢰성이 병목이 된다.

## 실무 적용 관점

이 논문은 코드 에이전트에서 중요한 것은 “더 잘 쓰게 하기”만이 아니라, **더 잘 검증하게 하기**라는 점을 분명히 보여준다.

## 관련 문서

- [[generator-evaluator-architecture|Generator-Evaluator Architecture]]
- [[self-evaluation-bias|Self-Evaluation Bias]]
- [[swe-evo-paper|SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios]]

