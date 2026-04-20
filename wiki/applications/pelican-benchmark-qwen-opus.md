---
title: "Pelican 벤치마크: Qwen3.6 vs Claude Opus 4.7"
category: applications
page_type: summary
tags: [applications, summary, pelican-benchmark, qwen, claude-opus-4-7, llm-evaluation, informal-benchmark, svg-generation]
sources: [raw/2026-04-20-blog-willison-qwen-beats-opus.md]
created: 2026-04-20
updated: 2026-04-20
---

# Pelican 벤치마크: Qwen3.6 vs Claude Opus 4.7

Simon Willison이 2026년 4월 16일 공개한 비교 분석. "pelican riding a bicycle" SVG 생성 태스크에서 **로컬 구동 Qwen3.6-35B-A3B(20.9GB 양자화)가 Claude Opus 4.7을 이겼다**. 이 결과는 단일 창작 태스크 성능과 전반적 유용성 간의 단절을 보여주는 사례로 제시됐다.

## 원본 소스

- 저자: Simon Willison
- 발행: 2026-04-16
- URL: https://simonwillison.net/2026/Apr/16/qwen-beats-opus/

## 비교 환경

| 항목 | Qwen3.6-35B-A3B | Claude Opus 4.7 |
|------|-----------------|-----------------|
| 출시일 | 2026-04-16 | 2026-04-16 |
| 구동 방식 | LM Studio 로컬 (MacBook Pro M5) | Anthropic API |
| 모델 크기 | 20.9GB (양자화) | 비공개 (프로프라이어터리) |
| 추론 방식 | 기본 | Extended thinking 포함 |

## Pelican 테스트 결과

"자전거를 탄 펠리컨(pelican riding a bicycle)" SVG를 생성하는 비공식 벤치마크.

| 평가 항목 | Qwen | Opus 4.7 |
|----------|------|----------|
| 자전거 프레임 구조 | 정상적으로 표현 | "전혀 잘못된 모양" |
| 펠리컨 부리 주머니 | 뚜렷이 표현 | 불분명 |
| Extended thinking 효과 | N/A | 2차 시도도 malformed |

## Flamingo 보조 테스트

"유니사이클을 탄 플라밍고" 2차 테스트:

- **Qwen**: 선글라스, 나비넥타이 추가. SVG 코멘트 `<!-- Sunglasses on flamingo! -->` 삽입. 개성 있는 결과
- **Opus 4.7**: Willison 평가 - "유능하지만 다소 지루한 벡터 일러스트"

## Willison의 핵심 인용

> "Today, even that loose connection to utility has been broken."

벤치마크 성능과 실제 유용성 간의 연결이 끊어지고 있다는 주장이다.

동시에 Willison은 결론을 단순화하지 않았다:

> "I very much doubt that a 21GB quantized version of their latest model is more powerful or useful than Anthropic's latest proprietary release."

## 분석: 벤치마크-유용성 단절

이 사례가 드러내는 구조적 문제:

1. **특화 태스크 우위**: 단일 창작 태스크(SVG 생성)에서 로컬 오픈소스 모델이 플래그십 프로프라이어터리 모델을 이길 수 있다
2. **진단 가치의 한계**: pelican benchmark 같은 단일 태스크 성능은 모델의 일반 유용성을 예측하지 못한다
3. **오픈소스 격차 축소**: 특정 창작 영역에서 오픈소스-프로프라이어터리 격차가 역전 가능해졌다
4. **informal benchmark의 역설**: 추적 신호로는 여전히 유효하지만(2024-10 모델 대비 품질 향상 확인), 해석에 주의 필요

## 관련 문서

- [[pelican-benchmark|Pelican 벤치마크 (개념)]]
- [[claude-opus-4-7|Claude Opus 4.7]]
- [[prompt-archaeology-willison|Claude 시스템 프롬프트 Archaeology (Willison)]]
