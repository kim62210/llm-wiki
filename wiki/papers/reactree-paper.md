---
title: ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning
category: papers
page_type: paper
tags: [paper, agents, [[context-engineering|planning]], hierarchy]
sources: [raw/hot-topics-sources/2026-04-10/030-reactree-hierarchical-llm-agent-trees-with-control-flow-for-[[long-running-agent-harnesses|long-horizon]]-task-pl.md, raw/2026-04-10-hot-ai-topics-sources/agent-trees/01-arxiv-org-reactree-hierarchical-llm-agent-trees-with-control-flow-for-.md]
created: 2026-04-10
updated: 2026-04-13
---
# ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

단일 trajectory 대신 agent tree와 control flow node를 도입해 장기 계획 문제를 푸는 hierarchical planning 논문이다.

## 핵심 기여

- 복잡한 목표를 subgoal tree로 쪼개는 agent node + control flow node 구조 제안
- episodic memory와 working memory를 함께 엮어 트리 탐색 품질 향상
- ReAct 같은 평면적 루프 대비 hierarchy의 장점을 정량적으로 제시

## 결과와 시사점

- WAH-NL에서 Qwen 2.5 72B 기준 61% 성공률로 ReAct 31%를 크게 상회
- ALFRED 등 장기 계획 과제에서도 일관된 우위 보고

## 한계

트리 확장 전략과 control flow 자체가 추가 복잡도를 만들며, 환경별 탐색 비용이 커질 수 있다.

## 실무 적용 관점

long-horizon planning에서 핵심은 더 긴 CoT가 아니라 **계획 구조를 계층화하고 기억을 국소화하는 것**이라는 메시지를 준다.

## 문제 설정

`ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning`는 **장기 실행 에이전트의 계획·검증·탐색 구조를 어떻게 설계하는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다

## 리뷰 포인트

- `ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **2511.02424 ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning** — https://arxiv.org/abs/2511.02424 · 초록 단서: Recent advancements in large language models (LLMs) have enabled significant progress in decision-making and task planning for embodied autonomous agents. However, most existing... · snapshot: `raw/hot-topics-sources/2026-04-10/030-reactree-hierarchical-llm-agent-trees-with-control-flow-for-long-horizon-task-pl.md`
- **ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning** — https://arxiv.org/abs/2511.02424 · 초록 단서: Recent advancements in large language models (LLMs) have enabled significant progress in decision-making and task planning for embodied autonomous agents. However, most existing... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/agent-trees/01-arxiv-org-reactree-hierarchical-llm-agent-trees-with-control-flow-for-.md`

## 원문 기반 상세 해석

`ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `[2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning`이며, 원문 URL은 `https://arxiv.org/abs/2511.02424`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, quick links, Submission history, Access Paper:, References & Citations` 쪽에 모인다.

자동 추출된 원문 단서는 `[2511.02424] ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning; Skip to main content; Learn about arXiv becoming an independent nonprofit.; We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. 논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서

- [[agent-trees]]
- [[subagents]]
- [[agent-memory-systems]]
