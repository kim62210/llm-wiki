---
title: "GIF Optimization with WebAssembly — Case Study"
aliases: ["gif optimization case study", "GIF optimization case study"]
category: applications
page_type: case-study
tags: [case-study, wasm, gifsicle, claude-code, prompts]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-09
---

# GIF Optimization with WebAssembly — Case Study

Simon Willison이 [[agentic engineering guide]] Section 5 "Annotated Prompts"에 실은 실전 사례. [[Claude Code]]에게 Gifsicle을 WebAssembly로 컴파일하고 브라우저 인터페이스를 만들게 하는 과정을 주석 달린 프롬프트로 보여준다.

## 목표

- 브라우저에서 GIF 최적화 (파일 크기 축소)
- 드래그&드롭 업로드
- 여러 압축 버전 비교
- 설정 tweak 가능

## 초기 프롬프트 (요지)

Simon이 Claude Code에 전달한 내용:
- `gif-optimizer.html` 생성
- **Gifsicle을 WASM으로 컴파일**
- 드래그&드롭 GIF 업로드 웹페이지
- 파일 크기와 다운로드 버튼이 포함된 여러 압축 버전 표시
- 프리뷰에서 설정을 "tweak"할 수 있는 수동 컨트롤

## 주석 포인트

### 1. 파일명이 곧 컨텍스트

`gif-optimizer.html`이라는 이름만으로 Simon의 **simonw/tools 저장소** 컨텍스트 안에서 "또 하나의 브라우저 도구"라는 의도가 명확해진다. 에이전트는 같은 저장소의 기존 도구 패턴(드래그&드롭 HTML UI)을 레퍼런스로 삼는다.

### 2. Gifsicle을 이름으로 부르기

30년 역사의 널리 쓰이는 소프트웨어. 이름을 명시하면 Claude가 학습한 지식을 끌어올 수 있다. "GIF 최적화 도구"라고만 하면 덜 구체적.

### 3. WASM 컴파일은 어려운 일

WASM 컴파일은 Emscripten 툴체인 작업이 필요하다. Simon의 관찰:

> "Coding agents are fantastic at trial and error! They can often brute force their way to a solution where I would have given up after the fifth inscrutable compiler error."

→ 사람이 포기할 만한 반복 실패를 에이전트는 끈질기게 이어간다. 이는 코딩 에이전트의 강점이다.

### 4. 과소명세(Under-specification)

Simon은 세부 설정을 과도하게 지정하지 않는다. Claude의 "적절한 기본값 판단 능력"을 믿고 맡긴다. 이는 [[hoard things you know how to do|기존 도구 패턴의 재사용]]과도 연결된다.

## 테스트

Simon은 브라우저 테스트 단계에서 `uvx rodney --help`를 실행하게 해 [[Rodney]]를 설치/활용하게 했다. 세션 transcript를 보면 Claude가 **CSS 이슈를 스스로 식별하고 수정**하는 모습이 나온다 — [[agentic manual testing|에이전트에 의한 수동 테스트]]의 실전 예시.

## Follow-up 프롬프트

첫 결과물 이후 Simon이 추가한 지시들:

1. **빌드 스크립트/패치는 lib/ 하위에 포함**
2. **Gifsicle을 /tmp에 클론** — 풀 소스를 저장소에 커밋하지 말 것
3. **WASM 번들(233KB)은 GitHub Pages 배포용으로 커밋**
4. **Gifsicle을 크레딧하고 원본 저장소 링크**

결과 푸터:
> "Built with gifsicle by Eddie Kohler, compiled to WebAssembly. gifsicle is released under the GNU General Public License, version 2."

## 배울 수 있는 것

- **이름을 명시하라** — 유명 라이브러리, 파일명, 저장소 이름
- **과소명세를 두려워 말라** — 적절한 기본값은 모델이 안다
- **반복 실패가 예상되는 작업은 에이전트에게 유리** — Emscripten 컴파일 같은 것
- **테스트 도구를 제공하라** — Rodney, Playwright로 자가 검증
- **크레딧/라이선스를 지시하라** — 에이전트는 시키면 잘 지킨다
- **Follow-up으로 세부 조정** — 한 번에 모든 것을 지시하지 않는다

## [[code is cheap]]과의 연결

Simon이 이 사례에서 재확인하는 원칙:
> "Writing code is cheap now... providing testing capabilities significantly improves agent performance during development."

코드 생성 비용이 낮아진 만큼, 테스트 인프라와 반복 능력을 갖춘 에이전트가 실제 사용 가능한 도구를 생산해낸다.

## 관련 문서

- [[code is cheap]]
- [[hoard things you know how to do]]
- [[agentic manual testing]]
- [[Rodney]]
- [[Claude Code]]
- [[prompts library]]
- [[agentic engineering guide]]
