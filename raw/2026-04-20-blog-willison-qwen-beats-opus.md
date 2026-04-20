---
source: simonwillison.net
title: "Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7"
author: "Simon Willison"
date: 2026-04-16
url: "https://simonwillison.net/2026/Apr/16/qwen-beats-opus/"
fetched: 2026-04-20
status: pending_ingest
tags: [llm-evaluation, pelican-benchmark, qwen, claude-opus-4-7, informal-benchmark]
---

## 핵심 주장

Simon Willison의 "pelican riding a bicycle" SVG 벤치마크에서 **로컬 Qwen3.6-35B-A3B(20.9GB 양자화)가 Claude Opus 4.7을 이겼다**. 플라밍고-유니사이클 2차 테스트에서도 Qwen 승.

## 비교 대상

- **Qwen3.6-35B-A3B**: 2026-04-16 출시, MacBook Pro M5 + LM Studio 로컬 구동, 20.9GB 양자화
- **Claude Opus 4.7**: 같은 날 출시, extended thinking 포함 테스트

## Pelican 테스트 결과

| 항목 | Qwen | Opus 4.7 |
|------|------|----------|
| 자전거 프레임 | 정상 | "전혀 잘못된 모양" |
| 펠리컨 주머니 | 뚜렷이 표현 | 불분명 |
| Extended thinking | N/A | 2차 시도도 malformed |

## Flamingo 보조 테스트

- Qwen: 선글라스, 나비넥타이, SVG 코멘트 `<!-- Sunglasses on flamingo! -->` 추가. 개성 있음
- Opus: "유능하지만 다소 지루한 벡터 일러스트"

## Willison의 결론

> "Today, even that loose connection to utility has been broken."

**벤치마크-유용성 간 연결이 끊어짐**을 보여주는 사례. 단일 태스크(SVG 창작)에서 로컬 모델이 플래그십 모델을 이길 수 있지만, 실제 일반 유용성에서는 여전히 Opus가 우위라고 Willison 자신도 인정:

> "I very much doubt that a 21GB quantized version of their latest model is more powerful or useful than Anthropic's latest proprietary release."

## 함의

- **특화 벤치마크의 진단가치 한계**: 단일 태스크 성능은 일반 유용성을 예측하지 못함
- **오픈소스 vs 프로프라이어터리** 격차가 특정 창작 태스크에서는 역전 가능
- **2024-10 vs 2026-04 SVG 품질 개선**: pelican benchmark가 모델 진화를 추적하는 informal 신호로 여전히 유효
- 모델 평가는 **다차원 평가 + 실제 작업 기반 회귀 테스트** 방향으로 가야

## 기존 페이지 업데이트 후보

- `wiki/concepts/llm-evaluation-difficulty.md` (있으면) 또는 신규 concept 페이지 후보
- `wiki/tooling/claude-opus-4-7.md` — 약점 섹션에 인용 가능
- `wiki/tooling/qwen.md` 또는 `wiki/tooling/qwen-family.md` (있으면)
- `wiki/concepts/benchmark-gaming.md` 또는 `wiki/concepts/pelican-benchmark.md` 신규 가능

## Raw 요약 키워드
pelican benchmark, Qwen3.6-35B-A3B, Claude Opus 4.7, LM Studio local inference, SVG creativity, benchmark-utility disconnect, informal eval
