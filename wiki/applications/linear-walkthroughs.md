---
title: Linear Walkthroughs
aliases: [linear walkthroughs]
category: applications
page_type: concept
tags: [code-understanding, documentation, showboat, claude-code]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-13
---
# Linear Walkthroughs

Simon Willison이 [[agentic-engineering-guide]] Section 4에서 소개하는 "에이전트가 코드를 설명하게 만드는 기법".

## 언제 쓰나

코딩 에이전트에게 코드베이스를 **구조화된 방식으로 설명**하게 할 때:
- 처음 보는 기존 코드를 이해해야 할 때
- 본인이 쓴 코드지만 세부가 기억나지 않을 때
- "[[vibe-coding|vibe coded]]"해서 구현 디테일을 보지 않은 코드
- 동료에게 온보딩 문서를 만들어야 할 때

Frontier 모델 + 제대로 된 에이전트 하네스는 상세한 walkthrough를 구성할 수 있다.

## 사례: Simon의 Present 앱

Simon의 시연 사례:

1. Mac에서 Claude Code + Opus 4.6으로 SwiftUI 슬라이드 프레젠테이션 앱을 **"vibe coded"**
2. 코드를 GitHub에 공개
3. 자기 앱이 어떻게 동작하는지 스스로 이해하지 못함을 깨달음
4. Claude Code for web을 열고 저장소를 가리키며 다음 프롬프트 전달:

```
Read the source code.
Plan a linear walkthrough explaining how everything works in detail.
Run "uvx showboat --help" to learn the Showboat tool.
Create a walkthrough.md file using Showboat to build the walkthrough.
```

## Showboat를 쓰는 이유

[[Showboat]] = 에이전트가 작업을 시연하는 문서를 쓰기 위한 도구.

- `showboat note` → Markdown 콘텐츠 추가
- `showboat exec` → shell 명령을 실행하고 명령 + 출력 모두 기록

Simon의 추가 지시: "use sed or grep or cat or whatever you need" — 이 지시의 목적은 에이전트가 **코드 스니펫을 손으로 복사하지 않도록** 강제하는 것이다. 손 복사는 할루시네이션이나 실수의 위험을 만든다.

## 결과

Simon의 6개 Swift 파일 앱에 대해:
- 모든 파일에 대한 clear, actionable한 설명
- Simon 본인이 **SwiftUI 아키텍처와 Swift 언어 디테일을 상당히 배움**

## 핵심 통찰

> "Even brief projects created through rapid iteration can become opportunities to explore new ecosystems and develop new technical skills through agent-generated explanations."

빠른 iteration으로 만든 짧은 프로젝트도 에이전트 생성 설명을 통해 새 생태계 학습 기회가 된다. [[cognitive-debt]]를 갚는 주요 수단이다.

## 선형 vs 인터랙티브 walkthrough

- **Linear**: 텍스트 기반, 파일 단위로 순차적 설명. Showboat로 문서화. → 이 페이지
- **Interactive**: 애니메이션/UI로 알고리즘의 동작을 시각화. → [[interactive-explanations]]

Simon은 word cloud 사례에서 이 두 단계를 순차적으로 적용했다:
1. 먼저 linear walkthrough로 Rust 코드 구조 파악
2. 그래도 Archimedean spiral 알고리즘이 와닿지 않자 → interactive 애니메이션 요청

## 실무 프롬프트 템플릿

```
Read the source code in this repository.
Plan a linear walkthrough explaining how everything works in detail.
Use sed, grep, or cat to quote code directly — do not retype snippets.
Write the walkthrough to walkthrough.md.
```

Showboat까지 쓰려면:
```
Run "uvx showboat --help" first.
Then use showboat note and showboat exec to build a walkthrough document.
```

## 관련 문서

- [[interactive-explanations]]
- [[cognitive-debt]]
- [[vibe-coding]]
- [[Showboat]]
- [[claude-code]]
- [[agentic-engineering-guide]]
