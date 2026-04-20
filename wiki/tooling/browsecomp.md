---
title: BrowseComp
category: tooling
page_type: entity
project: BrowseComp
tags: [tooling, entity, [[benchmark-contamination|benchmark]], web-browsing, openai, [[coding-agent|agent]]ic-evaluation]
sources: [raw/2026-04-14-gap-scan-new-topics.md]
created: 2026-04-14
updated: 2026-04-14
---
# BrowseComp

OpenAI가 2025년 4월 발표한 웹 브라우징 에이전트 벤치마크. 1,266개 질문으로 구성되며, 인터넷에서 찾기 어려운 얽힌 정보를 탐색하는 능력을 측정한다.

## 왜 지금 중요한가

기존 웹 검색 평가가 단순 질의-응답에 머물렀던 반면, BrowseComp는 **다중 홉 추론과 지속적 탐색**을 요구하는 최초의 대규모 벤치마크다. 단순히 브라우징 도구를 장착하는 것만으로는 성능이 거의 향상되지 않으며(GPT-4o + browsing: 1.9%), Deep Research 같은 전문 에이전틱 시스템만이 의미 있는 성과(51.5~78%)를 달성한다는 점에서, 도구 접근성과 에이전트 능력 사이의 간극을 정량적으로 드러냈다.

## 벤치마크 구조

BrowseComp는 "역방향 질문 방법론(inverted question methodology)"을 채택한다.

1. 인간 브라우저가 실제 탐색으로 검증 가능한 사실을 발견
2. "답은 찾기 어렵지만 검증은 쉬운" 질문으로 역변환
3. GPT-4o와 o1이 풀 수 없음을 확인하여 난도 보장
4. 상위 검색 결과에 답이 노출되지 않음을 검증

질문당 정확히 5회의 Google 검색을 수행하도록 설계했고, 인간이 40% 이상 정답률을 보이는 질문은 난도를 재조정했다.

```mermaid
flowchart LR
    A[인간 브라우저가 사실 발견] --> B[역방향 질문 생성]
    B --> C[GPT-4o/o1 풀 수 없음 확인]
    C --> D[검색 상위 결과 미노출 검증]
    D --> E[최종 1,266문항 확정]
```

## 핵심 수치

| 시스템 | 정확도 |
|---|---|
| GPT-4.5 (브라우징 없음) | 0.9% |
| GPT-4o + 브라우징 도구 | 1.9% |
| Deep Research (단일 시도) | 51.5% |
| Deep Research (복수 시도) | 78.0% |
| 인간 평가자 | 29.2% (86.4% 일치율) |

주목할 점은 인간 평가자 정확도(29.2%)도 낮다는 것이다. 이는 벤치마크가 의도적으로 **극도로 찾기 어려운** 정보를 대상으로 했기 때문이며, Deep Research가 인간을 크게 초과하는 첫 웹 탐색 벤치마크가 되었다.

## 설계 특성

BrowseComp는 프로그래밍 경시대회가 코딩 에이전트의 불완전하지만 유용한 벤치마크인 것처럼, 브라우징 에이전트의 핵심 역량인 **끈기와 창의성**을 측정한다. 의도적으로 단순화한 부분이 있다.

- **채점**: exact-match 정확도 (짧고 검증 가능한 답)
- **미포함**: 실제 사용자 쿼리 분포, 긴 응답 생성, 쿼리 모호성 해소
- **공개**: OpenAI simple-evals 저장소에서 오픈소스로 제공

## 시사점

BrowseComp가 드러낸 27배 성능 격차(기본 브라우징 1.9% vs Deep Research 51.5%)는 단순한 도구 접근이 아닌 **전략적 계획, 지속적 탐색, 다중 홉 추론**이 웹 탐색 성공을 결정한다는 것을 보여준다. 이는 [[osworld-verified]]와 함께 에이전틱 AI 평가의 새로운 축을 형성한다.

## 대표 자료

- [BrowseComp (OpenAI)](https://openai.com/index/browsecomp/)
- [BrowseComp: a benchmark for browsing agents (arXiv 2504.12516)](https://arxiv.org/abs/2504.12516)
- [What is BrowseComp? (Galileo AI)](https://galileo.ai/blog/what-is-browsecomp-openai-benchmark-web-browsing-agents)
- [BrowseComp Benchmark (BenchLM)](https://benchlm.ai/benchmarks/browseComp)

## 관련 문서

- [[osworld-verified]] -- 컴퓨터 사용 에이전트 벤치마크, BrowseComp와 상호 보완
- [[swe-bench-pro]] -- 소프트웨어 엔지니어링 장기 호흡 벤치마크
- [[terminal-bench-2-0]] -- 터미널 중심 에이전트 벤치마크
- [[cot-monitoring-safety]] -- 추론 모델 안전성 모니터링
