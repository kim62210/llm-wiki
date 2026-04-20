---
title: Scaling Long-Horizon LLM Agent via Context-Folding
category: papers
page_type: paper
tags: [paper, [[coding-agent|agent]]s, context-folding, rl]
sources: [raw/hot-topics-sources/2026-04-10/029-scaling-long-horizon-llm-agent-via-context-folding.md, raw/2026-04-10-hot-ai-topics-sources/context-folding/01-arxiv-org-scaling-long-horizon-llm-agent-via-context-folding.md]
created: 2026-04-10
updated: 2026-04-13
---
# Scaling Long-Horizon LLM Agent via Context-Folding

서브태스크를 branch한 뒤 fold하여 요약으로 되돌리는 **Context-Folding**을 RL 프레임워크로 학습시킨 논문이다.

## 핵심 기여

- sub-trajectory를 완료 후 접어 넣는 folding 연산을 long-horizon agent의 기본 행동으로 제안
- FoldGRPO라는 end-to-end RL 학습 프레임워크 도입
- summarization-based context management보다 더 작은 active context로 경쟁력 있는 성능을 달성

## 결과와 시사점

- Deep Research, SWE 계열 과제에서 ReAct baseline과 동등 또는 우수 성능
- active context를 약 10배 줄이면서도 성능 유지

## 한계

folding 정책을 학습시키는 보상 설계가 까다롭고, 요약이 잘못되면 이후 단계 전체에 누적 오류가 생길 수 있다.

## 실무 적용 관점

장기 호흡 agent를 설계할 때 context budget을 늘리는 대신 **작업 구조 자체를 접는 방식**으로 문제를 풀 수 있음을 보여준다.

## 문제 설정

`Scaling Long-Horizon LLM Agent via Context-Folding`는 **긴 컨텍스트/메모리 병목을 어떻게 줄이는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다
- 검증 신호 자체를 학습·강화해야 test-time scaling이 의미를 가진다는 관점이 숨어 있다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `Scaling Long-Horizon LLM Agent via Context-Folding`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **2510.11967 Scaling Long-Horizon LLM Agent via Context-Folding** — https://arxiv.org/abs/2510.11967 · 초록 단서: Large language model (LLM) agents are fundamentally constrained by context length on long-horizon tasks. We introduce Context-Folding, a framework that empowers agents to active... · snapshot: `raw/hot-topics-sources/2026-04-10/029-scaling-long-horizon-llm-agent-via-context-folding.md`
- **Scaling Long-Horizon LLM Agent via Context-Folding** — https://arxiv.org/abs/2510.11967 · 초록 단서: Large language model (LLM) agents are fundamentally constrained by context length on long-horizon tasks. We introduce Context-Folding, a framework that empowers agents to active... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/context-folding/01-arxiv-org-scaling-long-horizon-llm-agent-via-context-folding.md`

## 원문 기반 상세 해석

`Scaling Long-Horizon LLM Agent via Context-Folding`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `[2510.11967] Scaling Long-Horizon LLM Agent via Context-Folding`이며, 원문 URL은 `https://arxiv.org/abs/2510.11967`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, quick links, Submission history, Access Paper:, References & Citations` 쪽에 모인다.

자동 추출된 원문 단서는 `[2510.11967] Scaling Long-Horizon LLM Agent via Context-Folding; Skip to main content; Learn about arXiv becoming an independent nonprofit.; We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. 논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서

- [[context-folding]]
- [[long-horizon-rl-training-for-agents]]
- [[subagents]]
