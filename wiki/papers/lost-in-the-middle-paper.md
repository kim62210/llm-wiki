---
title: Lost in the Middle: How Language Models Use Long Contexts
category: papers
page_type: paper
tags: [paper, long-context, evaluation, retrieval]
sources: [raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md]
created: 2026-04-10
updated: 2026-04-13
---
# Lost in the Middle: How Language Models Use Long Contexts

긴 컨텍스트에서 관련 정보가 중간에 있을 때 LLM 성능이 크게 저하된다는 고전적이면서도 여전히 중요한 논문이다.

## 핵심 기여

- multi-document QA와 key-value retrieval로 long-context 사용 방식을 분석
- 정보 위치가 모델 성능에 미치는 영향을 정량적으로 보여줌
- context engineering 시대의 핵심 failure mode를 논문 수준으로 정식화

## 결과와 시사점

- 정보가 문맥 앞·뒤에 있을 때보다 가운데에 있을 때 성능이 크게 하락
- 명시적으로 long-context를 지원하는 모델에서도 동일 경향 관찰

## 한계

이 논문은 현상을 밝히는 데 강하지만, 실제 production retrieval stack에서 이를 어떻게 완화할지는 후속 연구와 엔지니어링이 필요하다.

## 실무 적용 관점

RAG, [[adaptive-context-compression|context compression]], prompt ordering, tool calling 등 모든 long-context 설계가 결국 **중간 정보 소실을 어떻게 피할지**의 문제라는 점을 상기시킨다.

## 문제 설정

`Lost in the Middle: How Language Models Use Long Contexts`는 **긴 컨텍스트/메모리 병목을 어떻게 줄이는가**라는 문제를 다루는 논문으로 읽는 것이 안전하다. 단순히 새로운 방법 이름을 외우기보다, 어떤 병목 때문에 이 방법이 등장했는지부터 확인해야 한다.

- 컨텍스트 길이 증가가 비용과 회수 품질을 동시에 악화시키는 조건을 전제로 읽는다
- 주장 자체보다 어떤 벤치마크/환경에서 검증했는지까지 같이 봐야 한다

## 리뷰 포인트

- `Lost in the Middle: How Language Models Use Long Contexts`를 읽을 때는 방법 이름보다 **무엇을 압축/계획/검증/학습 대상으로 삼는지**를 먼저 분리해 적는 편이 좋다.
- 결과 수치가 있다면 절대 성능만 보지 말고, 토큰 비용·턴 수·벤치마크 난이도처럼 함께 움직이는 비용 축을 같이 봐야 한다.
- 실무 적용 판단은 '바로 도입할 수 있는가'보다 '기존 하네스나 평가 체계에 어떤 설계 힌트를 주는가'로 하는 편이 현실적이다.

## source 메타데이터

- **Lost in the Middle: How Language Models Use Long Contexts** — https://arxiv.org/abs/2307.03172 · 초록 단서: While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. We analyze the performance of la... · snapshot: `raw/hot-topics-sources/2026-04-10/166-lost-in-the-middle-how-language-models-use-long-contexts.md`

## 실험 설계 요약

| 실험 축 | 논문이 한 일 | 관찰된 결과 |
|---|---|---|
| multi-document QA | 관련 문서 위치를 앞/중간/뒤로 바꿔가며 답변 성능 측정 | 중간에 있을 때 회수 성능이 크게 떨어졌다 |
| key-value retrieval | 필요한 키-값 쌍의 위치만 바꿔 장기 문맥 활용 능력 측정 | 긴 컨텍스트를 받는 모델도 중간 정보 접근이 약했다 |
| long-context claims 검증 | 명시적으로 long-context를 지원하는 모델도 비교 | 컨텍스트 길이 지원과 정보 활용 능력은 별개라는 점이 드러났다 |

## 실무에서 번역되는 규칙

- 중요한 사실을 한 번만 중간에 묻어 두지 말고, 앞쪽 요약과 뒤쪽 체크리스트로 재노출시켜야 한다.
- RAG에서 retrieval hit만으로 안심하면 안 되고, **모델 입력 안에서의 배치 순서**를 별도 설계 변수로 봐야 한다.
- 따라서 이 논문은 context window marketing claim을 곧이곧대로 믿지 말고, 실제 배치 실험으로 확인하라는 경고로 읽는 편이 맞다.

## 관련 문서
- [[context-rot-report]]
- [[context-engineering-open-source-software-paper]]

- [[lost-in-the-middle]]
- [[context-engineering]]
- [[context-rot]]
