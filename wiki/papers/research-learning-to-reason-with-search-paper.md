---
title: ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning
category: papers
page_type: paper
tags: [paper, search, reinforcement-learning, reasoning]
sources: [raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/05-arxiv-org-research-learning-to-reason-with-search-for-llms-via-reinfor.md]
created: 2026-04-10
updated: 2026-04-13
---
# ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning

search를 reasoning 과정의 일부로 보고, 이를 강화학습으로 최적화하는 접근을 제안한 논문이다.

## 핵심 기여

- search policy와 reasoning policy를 함께 학습 대상으로 설정
- retrieval을 외부 부가 기능이 아니라 문제 해결 루프의 핵심 행동으로 통합
- RL을 통해 search-aware reasoning agent를 훈련하는 틀을 제공

## 결과와 시사점

- long-horizon reasoning에서 search는 단순 retrieval step이 아니라 적극적인 탐색 전략이 된다.
- search와 reasoning을 함께 학습시키는 것이 정적 CoT보다 더 강한 agent behavior를 만들 수 있음을 시사한다.

## 한계

search 품질과 환경 노이즈에 따라 학습 안정성이 흔들릴 수 있고, 실제 검색 인프라와의 결합 비용도 크다.

## 실무 적용 관점

이 논문은 “검색을 붙인 모델”보다 **검색을 배우는 에이전트**라는 관점이 앞으로 더 중요해질 수 있음을 보여준다.

## 문제 설정

`ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning** — https://arxiv.org/abs/2503.19470 · 초록 단서: Large Language Models (LLMs) have shown remarkable capabilities in reasoning, exemplified by the success of OpenAI-o1 and DeepSeek-R1. However, integrating reasoning with extern... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/long-horizon-rl-training-for-agents/05-arxiv-org-research-learning-to-reason-with-search-for-llms-via-reinfor.md`

## 원문 기반 상세 해석

`ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning`이며, 원문 URL은 `https://arxiv.org/abs/2503.19470`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, quick links, Submission history, Access Paper:, References & Citations` 쪽에 모인다.

자동 추출된 원문 단서는 `# ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning; - 원본 URL: https://arxiv.org/abs/2503.19470; - 연결된 토픽: Long-Horizon RL Training for Agents (Multi-Turn [[rlvr|RLVR]]); Title: ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. 논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서

- [[agentic-rl-survey-paper|The Landscape of Agentic Reinforcement Learning for LLMs: A Survey]]
- [[agentic-rag|Agentic RAG with Hierarchical Retrieval Interfaces]]
- [[tool-invocation-evaluators|Tool Selection & Tool Invocation Evaluators]]
