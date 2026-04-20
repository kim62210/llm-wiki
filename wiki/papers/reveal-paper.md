---
title: ReVeal: Self-Evolving Code Agents via Reliable Self-Verification
category: papers
page_type: paper
tags: [paper, coding-agents, self-verification, software-engineering]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/04-arxiv-org-reveal-self-evolving-code-agents-via-iterative-generation-ve.md]
created: 2026-04-10
updated: 2026-04-13
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

## 문제 설정

`ReVeal: Self-Evolving Code Agents via Reliable Self-Verification`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 검증 신호 자체를 학습·강화해야 test-time scaling이 의미를 가진다는 관점이 숨어 있다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `ReVeal: Self-Evolving Code Agents via Reliable Self-Verification`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **ReVeal: Self-Evolving Code Agents via Reliable Self-Verification** — https://arxiv.org/abs/2506.11442 · 초록 단서: Reinforcement learning with verifiable rewards (RLVR) has advanced the reasoning capabilities of large language models. However, existing methods rely solely on outcome rewards,... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/04-arxiv-org-reveal-self-evolving-code-agents-via-iterative-generation-ve.md`

## 한눈에 보기

| 항목 | 내용 |
|---|---|
| 문제 | outcome reward만으로는 자기검증 품질이 약해 test-time scaling이 제한된다 |
| 방법 | generation-verification turn을 반복하는 multi-turn RL + tool-based evaluation + TAPO credit assignment |
| 근거 | LiveCodeBench에서 학습은 3턴인데 추론 시 20+ turn 자기개선, Pass@k 향상 |
| 핵심 함의 | code generation보다 verification 자체를 강화해야 self-improving code agent가 가능하다 |

## 왜 중요한가

ReVeal은 RLVR 담론을 한 단계 밀어 올린다. 기존에는 "정답이 맞았는가"가 보상 설계의 중심이었다면, 이 논문은 **검증 행동 자체를 얼마나 신뢰할 수 있게 만들 것인가**를 학습 대상으로 삼는다. 그래서 이 논문은 코드 에이전트 논문이면서 동시에 [[generator-evaluator-architecture|generator-evaluator loop]]를 강화하는 방법론 논문으로 읽는 편이 맞다.

## 원문 기반 상세 해석

`ReVeal: Self-Evolving Code Agents via Reliable Self-Verification`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `ReVeal: Self-Evolving Code Agents via Reliable Self-Verification`이며, 원문 URL은 `https://arxiv.org/abs/2506.11442`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, quick links, Submission history, Access Paper:, References & Citations` 쪽에 모인다.

자동 추출된 원문 단서는 `# ReVeal: Self-Evolving Code Agents via Reliable Self-Verification; - 원본 URL: https://arxiv.org/abs/2506.11442; - 연결된 토픽: Long-Horizon RL Training for Agents (Multi-Turn [[rlvr|RLVR]]); Title: ReVeal: Self-Evolving Code Agents via Reliable Self-Verification`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. 논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서

- [[generator-evaluator-architecture|Generator-Evaluator Architecture]]
- [[self-evaluation-bias|Self-Evaluation Bias]]
- [[swe-evo-paper|SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios]]
