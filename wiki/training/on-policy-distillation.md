---
title: On-Policy Distillation
category: training
page_type: concept
tags: [training, concept, policy, distillation, training-and-post-training]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/on-policy-distillation.md, raw/hot-topics-sources/2026-04-10/281-on-policy-distillation.md, raw/hot-topics-sources/2026-04-10/282-qwen3-technical-report.md, raw/hot-topics-sources/2026-04-10/283-self-distilled-reasoner-on-policy-self-distillation-for-large-language-models.md, raw/hot-topics-sources/2026-04-10/284-revisiting-on-policy-distillation-empirical-failure-modes-and-simple-fixes.md, raw/hot-topics-sources/2026-04-10/285-reinforcement-aware-knowledge-distillation-for-llm-reasoning.md]
created: 2026-04-10
updated: 2026-04-10
---
# On-Policy Distillation

이 페이지는 On-Policy Distillation를 다룬다. 핵심은 학생이 직접 롤아웃한 궤적에 교사 모델이 토큰별 밀집 피드백을 주는 증류 기법이며, 2026년 4월 시점에 왜 다시 중요해졌는지 정리한다.

## 정의

학생이 직접 롤아웃한 궤적에 교사 모델이 토큰별 밀집 피드백을 주는 증류 기법.

## 왜 지금 중요한가

Thinking Machines Lab이 Qwen3-8B에서 RL 대비 1/10 비용으로 동등 성능을 재현해 화제가 됐고, RL과 SFT의 장점을 결합한 post-training의 새 축으로 부상 중이다.

## 대표 자료

- [On-Policy Distillation (Thinking Machines Lab blog)](https://thinkingmachines.ai/blog/on-policy-distillation/)
- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)
- [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)
- [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](https://arxiv.org/html/2603.25562)
- [Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://arxiv.org/abs/2602.22495)

## source 기반 참고

- 수집 소스 수: 5
- 상위 도메인: arxiv.org 4건, thinkingmachines.ai 1건

### source 맵

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/on-policy-distillation.md`
- [On-Policy Distillation - Thinking Machines Lab](https://thinkingmachines.ai/blog/on-policy-distillation) — `raw/hot-topics-sources/2026-04-10/281-on-policy-distillation.md`
  - 메모: --- title: On-Policy Distillation - Thinking Machines Lab source_url: https://thinkingmachines.ai/blog/on-policy-distillation final_url: https://thinkingmachines.ai/blog/on-policy-distillation/ status: 200 content_type: text/html; charset=utf-8 topics: [On-Policy Distillation] se
- [282-qwen3-technical-report](https://arxiv.org/pdf/2505.09388) — `raw/hot-topics-sources/2026-04-10/282-qwen3-technical-report.md`
  - 메모: --- title: Qwen3 Technical Report source_url: https://arxiv.org/pdf/2505.09388 final_url: https://arxiv.org/pdf/2505.09388 status: 200 content_type: application/pdf topics: [On-Policy Distillation] sections: [Training & Post-training] fetched_at: 2026-04-10T01:44:02.745542+00:00 
- [[2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734) — `raw/hot-topics-sources/2026-04-10/283-self-distilled-reasoner-on-policy-self-distillation-for-large-language-models.md`
  - 메모: --- title: [2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models source_url: https://arxiv.org/abs/2601.18734 final_url: https://arxiv.org/abs/2601.18734 status: 200 content_type: text/html; charset=utf-8 topics: [On-Policy Distillation] sect
- [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](https://arxiv.org/html/2603.25562) — `raw/hot-topics-sources/2026-04-10/284-revisiting-on-policy-distillation-empirical-failure-modes-and-simple-fixes.md`
  - 메모: --- title: Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes source_url: https://arxiv.org/html/2603.25562 final_url: https://arxiv.org/html/2603.25562 status: 200 content_type: text/html; charset=utf-8 topics: [On-Policy Distillation] sections: [Trainin
- [[2602.22495] Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://arxiv.org/abs/2602.22495) — `raw/hot-topics-sources/2026-04-10/285-reinforcement-aware-knowledge-distillation-for-llm-reasoning.md`
  - 메모: --- title: [2602.22495] Reinforcement-aware Knowledge Distillation for LLM Reasoning source_url: https://arxiv.org/abs/2602.22495 final_url: https://arxiv.org/abs/2602.22495 status: 200 content_type: text/html; charset=utf-8 topics: [On-Policy Distillation] sections: [Training & 

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[process-reward-models]]
- [[rl-scaling-laws]]
