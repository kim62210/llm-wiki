---
title: ACON: Optimizing Context Compression for Long-horizon LLM Agents
category: papers
page_type: paper
tags: [paper, context-engineering, compression, agents]
sources: [raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md, raw/2026-04-10-hot-ai-topics-sources/context-folding/03-arxiv-org-acon-optimizing-context-compression-for-long-horizon-llm-age.md]
created: 2026-04-10
updated: 2026-04-13
---
# ACON: Optimizing Context Compression for Long-horizon LLM Agents

장기 실행 에이전트의 문맥 압축을 단순 요약 문제가 아니라 **실패 원인 기반 최적화 문제**로 다룬 논문이다.

## 핵심 기여

- 환경 관측과 상호작용 히스토리를 함께 압축하는 ACON 프레임워크 제안
- 압축 실패 사례를 바탕으로 자연어 압축 가이드라인을 반복 최적화하는 루프 도입
- 큰 압축기를 작은 모델로 distillation하여 추가 모듈 오버헤드를 줄이는 전략 제시

## 결과와 시사점

- AppWorld, OfficeBench, Multi-objective QA에서 peak token을 26~54% 줄이면서 성능을 상당 부분 유지
- 작은 압축기로 distillation해도 95% 이상 정확도를 보존

## 한계

압축 가이드라인 최적화 자체가 별도 루프를 필요로 하므로, 온라인 비용과 파이프라인 복잡도가 늘어날 수 있다.

## 실무 적용 관점

실무에서는 context engineering을 '무엇을 남길까' 수준이 아니라 **어떤 실패를 줄이기 위해 어떤 정보를 보존할까**의 문제로 전환하게 만든다.

## 문제 설정

`ACON: Optimizing [[adaptive-context-compression|Context Compression]] for Long-horizon LLM Agents`는 **긴 컨텍스트/메모리 병목을 어떻게 줄이는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `ACON: Optimizing Context Compression for Long-horizon LLM Agents`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **2510.00615 ACON: Optimizing Context Compression for Long-horizon LLM Agents** — https://arxiv.org/abs/2510.00615 · 초록 단서: Large language models (LLMs) are increasingly deployed as agents in dynamic, real-world environments, where success requires both reasoning and effective tool use. A central cha... · snapshot: `raw/hot-topics-sources/2026-04-10/002-acon-optimizing-context-compression-for-long-horizon-llm-agents.md`
- **ACON: Optimizing Context Compression for Long-horizon LLM Agents** — https://arxiv.org/abs/2510.00615 · 초록 단서: Large language models (LLMs) are increasingly deployed as agents in dynamic, real-world environments, where success requires both reasoning and effective tool use. A central cha... · snapshot: `raw/2026-04-10-hot-ai-topics-sources/context-folding/03-arxiv-org-acon-optimizing-context-compression-for-long-horizon-llm-age.md`

## 원문 기반 상세 해석

`ACON: Optimizing Context Compression for Long-horizon LLM Agents`는 이전에는 그래프의 말단에서 짧은 요약만 제공하는 성격이 강했으므로, 이번 보강에서는 원문을 다시 열 때 바로 확인해야 할 **구체적 근거**를 본문 안에 남긴다. 1차 기준 source는 `[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents`이며, 원문 URL은 `https://arxiv.org/abs/2510.00615`이다. 이 source가 제공하는 구조 신호는 `요약 메모, 원문 추출, quick links, Submission history, Access Paper:, References & Citations` 쪽에 모인다.

자동 추출된 원문 단서는 `[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents; Skip to main content; Learn about arXiv becoming an independent nonprofit.; We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate`이다. 이 단서들은 그대로 인용하기보다, 이 위키 문서에서 어떤 질문을 던져야 하는지로 번역해 읽어야 한다. 즉 “무엇을 설치하는가/정의하는가”보다 “이 문서가 어떤 경계와 책임을 나누는가”를 먼저 본다. 그렇게 읽으면 말단 노드가 단순 제목 카드가 아니라, 상위 개념과 실제 source 사이를 연결하는 작은 탐색 표지가 된다.

편집 관점에서는 다음 원칙을 적용한다. 논문 노드는 문제 설정, 제안 방법, 실험 설계, 한계와 실무 적용 가능성을 분리해 읽어야 한다. 따라서 이 문서의 후속 갱신에서는 source가 제공한 고유 명사·단계·제약을 먼저 확인하고, 일반적인 AI 에이전트 설명으로 문장을 부풀리지 않는다. 반대로 여러 source에서 같은 구조가 반복되면 그 구조는 별도 concept 노드 후보가 된다.

실무 독자는 이 페이지를 읽은 뒤 바로 관련 문서로 이동하기보다, 먼저 source 표의 URL과 raw snapshot을 대조해 현재 문서의 정의가 아직 유효한지 확인하는 편이 좋다. 공식 문서나 논문이 업데이트되었으면 `updated` 날짜와 source 목록을 함께 갱신하고, 내용 변경이 제품별 구현 디테일인지 일반 개념인지 다시 판정해야 한다.

## 관련 문서

- [[context-engineering]]
- [[context-folding]]
- [[agent-memory-systems]]
