---
title: Hoard Things You Know How To Do
aliases: ["hoard things you know how to do"]
category: concepts
page_type: concept
tags: [knowledge-management, prototypes, simon-willison, reuse]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# Hoard Things You Know How To Do

Simon Willison이 [[agentic engineering guide]]에서 제시하는 핵심 프로페셔널 스킬. "할 줄 아는 것을 축적하라."

## 기본 아이디어

엔지니어링에서 가치를 만드는 순간은 대개 "이게 기술적으로 가능한가?"와 "어떻게 하면 되는가?"에 답할 수 있을 때 온다. 예시 질문들:

- JavaScript가 브라우저에서 OCR을 할 수 있나?
- iPhone 앱이 백그라운드에서 Bluetooth에 연결될 수 있나?
- Python이 100GB JSON 파일을 메모리에 다 올리지 않고 처리할 수 있나?

> "The more answers to questions like this you have under your belt, the more likely you'll be able to spot opportunities to deploy technology to solve problems."

## 자기 "작동하는 코드" 라이브러리 구축

최고의 신뢰 형성 방법은 실제로 *작동하는 코드*를 본인이 한 번 돌려본 것. Simon이 유지하는 컬렉션:

- **개인 블로그 + TIL(Today I Learned) 블로그** — 기법 기록
- **GitHub 1,000+ 저장소** — proof-of-concept 모음
- **tools.simonwillison.net** — HTML 기반 도구들
- **simonw/research** — 에이전트가 조사하고 작동 코드로 만든 연구 보고서들

## 예제 재조합: PDF OCR 웹 도구

Simon이 든 사례:
- 이미 작업해본 것 1: [[Tesseract.js]] — WebAssembly로 포팅된 Tesseract OCR 엔진
- 이미 작업해본 것 2: PDF.js — Mozilla의 PDF→이미지 변환 라이브러리

두 작동 예제를 Claude 3 Opus에 함께 넘기면서 "결합하라"고 지시 → 드래그&드롭 PDF → JPEG 변환 → OCR 텍스트 추출이 가능한 단일 HTML 페이지가 나왔다.

## 코딩 에이전트가 이 전략을 증폭시키는 방법

에이전트는 다음을 할 수 있다:
- URL에서 작동 예제를 가져와 분석
- 로컬 저장소에서 패턴 검색
- 공개 저장소를 clone해 참조 코드 확보
- 예제를 유사 문제의 템플릿으로 사용

## 핵심 원칙

> "Coding agents mean we only ever need to figure out a useful trick once."

한 번 알아낸 트릭은 영원히 재사용 가능하다. 이는 개인 예제 저장소에 대한 투자를 매우 높은 ROI로 만든다.

## 실무 적용

- **TIL 블로그/노트를 운영하라** — 반복 검색 대신 자기 기록에서 찾기
- **작동하는 최소 예제를 저장하라** — 문서가 아니라 실행 가능한 코드
- **에이전트에 "내 TIL 저장소를 참고해" 식으로 컨텍스트 주입** 가능

## 관련 문서

- [[code is cheap]]
- [[Tesseract.js]]
- [[prompts library]]
- [[agentic engineering guide]]
