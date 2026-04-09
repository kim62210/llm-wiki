---
title: Blind Prompting (맹목적 프롬프팅)
aliases: ["blind prompting", "맹목적 프롬프팅"]
category: concepts
page_type: concept
tags: [prompt-engineering, anti-pattern, mitchell-hashimoto, measurement]
sources: [raw/2026-04-09-evolution-of-ai-agentic-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Blind Prompting (맹목적 프롬프팅)

## 정의

**Blind Prompting**은 Mitchell Hashimoto가 지적한 안티패턴이다:

> **엄밀한 측정 없이 trial-and-error에만 의존하는 프롬프트 최적화.**

프롬프트를 "이게 더 좋아 보인다"는 주관적 느낌만으로 수정하면서 반복하지만, 실제로 성능이 개선되었는지 **측정하지 않는** 상태를 뜻한다.

## 원본 출처

Mitchell Hashimoto (HashiCorp 공동 창업자)가 블로그 포스트 "[Prompt Engineering vs Blind Prompting](https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting)"에서 제시한 개념. 이 글은 [[prompt engineering]] 에라의 벽을 드러낸 중요한 지적이었다.

## 왜 안티패턴인가

### 측정 없이는 개선도 없다

- 프롬프트 A와 프롬프트 B 중 어느 것이 더 나은지 주관적 느낌으로 판단
- 샘플이 작거나 평가 기준이 없음
- 한 케이스에서 잘 된 변경이 다른 케이스에서 퇴보를 초래해도 인지 못 함

### 모델의 비결정성

같은 프롬프트도 다른 출력을 낸다. 한두 번 시도에서 "좋아졌다"고 느낀 것은 분산(variance)일 수 있다. 통계적 판단 없이는 신호와 노이즈를 구분할 수 없다.

### 프롬프트 텍스트는 진짜 병목이 아니다

Blind prompting의 더 큰 문제: **시간을 엉뚱한 곳에 쓴다**는 것이다. 많은 경우 실패의 원인은 프롬프트 텍스트가 아니라 **컨텍스트 창에 관련 정보가 없음**이었다. 프롬프트를 아무리 다듬어도 이 근본 문제는 해결되지 않는다.

이 통찰이 [[context engineering]] 에라의 시작점 중 하나였다.

## 진짜 프롬프트 엔지니어링의 조건

Hashimoto의 원 주장: "Prompt engineering"이라는 말을 쓰려면 **엔지니어링다운 엄밀함**이 있어야 한다:

1. **측정 가능한 평가 메트릭**: 정확도, F1, BLEU, 사용자 승인 등
2. **벤치마크 데이터셋**: 프롬프트 변경을 정량적으로 비교할 수 있는 케이스 모음
3. **A/B 테스트**: 두 프롬프트를 같은 조건에서 비교
4. **버전 관리**: 어떤 변경이 어떤 효과를 냈는지 추적
5. **회귀 탐지**: 새 프롬프트가 과거 성공 케이스를 망가뜨리지 않는지 확인

이 조건을 갖추지 못한 작업은 "blind prompting"이며 엔지니어링이 아니다.

## [[vibe coding|바이브 코딩]]과의 관계

Vibe coding은 blind prompting의 **극단적 표현**이다:
- 프롬프트 효과 측정 안 함
- 결과 코드도 리뷰 안 함
- "느낌(vibe)"으로 수락

Blind prompting은 "프롬프트 품질 측정 포기", vibe coding은 "결과 품질 측정 포기". 둘 다 [[relocating rigor|엄밀함]]이 이동하지 않고 **증발**한 상태다.

## [[harness engineering|하네스 엔지니어링]] 시대의 대응

Blind prompting을 피하려면 하네스 4사분면 중 **우하(Inferential)** 또는 **우상(Computational)** 사분면에 측정 장치가 있어야 한다:

- **자동화된 평가 세트**: 에이전트 출력을 정량 비교
- **LLM-as-a-judge**: 시맨틱 품질 평가
- **CI에 통합**: 프롬프트 변경 시 자동 회귀 테스트

이것이 하네스 엔지니어링이 "프롬프트 엔지니어링의 후계"인 구체적 이유다 — 측정 장치 자체가 시스템에 편입되었다.

## 실무 체크리스트

프롬프트를 수정할 때마다 묻기:

1. [ ] 이 변경의 효과를 측정할 방법이 있는가?
2. [ ] 비교할 벤치마크 케이스가 있는가?
3. [ ] 과거에 잘 되던 케이스가 여전히 잘 되는지 확인했는가?
4. [ ] 한 번이 아닌 여러 번 실행해 분산을 고려했는가?
5. [ ] 위 네 개가 모두 "아니오"라면 — 지금 하고 있는 것은 blind prompting이다

## 관련 문서

- [[evolution of agentic patterns]] — Section 2.5에서 원본 지적 인용
- [[prompt engineering]] — blind prompting이 안티패턴으로 작동하는 에라
- [[context engineering]] — "프롬프트가 병목이 아니었다"는 재정의
- [[harness engineering]] — 측정 장치를 시스템에 내장한 패러다임
- [[vibe coding]] — 극단적 표현
- [[relocating rigor]] — 엄밀함이 이동하지 않고 증발한 경우

## 지식 갭

- [ ] Mitchell Hashimoto의 "Prompt Engineering vs Blind Prompting" 원문 수집
- [ ] 실제 A/B 테스트 프레임워크 (PromptFoo, Langfuse 등) 개별 페이지
