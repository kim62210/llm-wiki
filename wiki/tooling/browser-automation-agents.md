---
title: Browser Automation for Coding Agents
aliases: [Playwright, Rodney, Showboat, agent-browser, browser automation, browser automation agents]
category: tooling
page_type: concept
tags: [playwright, rodney, agent-browser, showboat, browser-automation, testing]
sources: [raw/2026-04-09-simon-willison-agentic-engineering-patterns.md]
created: 2026-04-09
updated: 2026-04-13
---
# Browser Automation for Coding Agents

Simon Willison이 [[agentic-engineering-guide]] Section 3 ([[agentic-manual-testing]])에서 언급하는 브라우저 자동화 도구 모음. 웹 UI를 에이전트가 직접 조작·검증하게 하기 위한 기반.

## 왜 필요한가

에이전트는 코드를 생성할 수 있지만, **웹 UI의 실제 동작을 확인**하려면 브라우저에서 상호작용해야 한다. 자동 테스트만으로는:
- 레이아웃 깨짐 포착 불가
- 클라이언트 JS 런타임 에러 누락 가능
- 인터랙션 시퀀스 검증 불가

→ 에이전트가 브라우저를 직접 조작하게 하면 이 간극을 메운다.

## 주요 도구

### 1. Playwright

> "The most powerful browser automation tool" — Simon Willison

- **공급사**: Microsoft (오픈소스)
- **언어**: Python, TypeScript/JS, .NET, Java 등 다언어 바인딩
- **브라우저**: Chromium, Firefox, WebKit
- **기능**: 네트워크 mocking, 스크린샷, 비디오, trace viewer

코딩 에이전트가 Playwright 스크립트를 직접 작성·실행해 UI 테스트를 수행 가능.

### 2. agent-browser (Vercel)

Vercel이 만든 **코딩 에이전트 전용 CLI 래퍼**. Playwright 같은 도구 위에 에이전트 친화적 인터페이스를 덧씌운 것.

### 3. Rodney (Simon Willison)

Simon 본인의 오픈소스 프로젝트:

- **기술**: Chrome DevTools Protocol을 통해 **Chrome 인스턴스를 직접 제어**
- **설치**: `uvx rodney --help` 명령으로 에이전트가 자동 설치
- **주요 능력**:
  - 스크린샷 (LLM의 vision 능력과 결합)
  - JavaScript 실행
  - 스크롤, 클릭, 타이핑
  - Accessibility tree 읽기

Simon의 사용 팁:
> "Request agents 'look at screenshots' to leverage their vision abilities."

에이전트에게 "스크린샷을 찍고 살펴봐"라고 지시하면 vision 능력을 UI 검증에 활용하게 된다.

### 4. Showboat

브라우저 자동화 **도구 자체는 아니지만**, 테스트/탐색 흐름을 **문서화**하는 짝 도구.

| 커맨드 | 역할 |
|--------|------|
| `showboat note` | Markdown 노트 추가 |
| `showboat exec` | 명령 실행 + 출력 기록 (결과 위조 억제) |
| `showboat image` | 이미지 추가 (예: Rodney 스크린샷) |

Rodney + Showboat 조합:
1. Rodney로 페이지를 열고 스크린샷
2. Showboat의 `image`로 스크린샷을 워크쓰루 문서에 삽입
3. `exec`로 실제 명령 출력을 증거로 기록

## 통합 워크플로우 예

웹 앱의 새 기능을 에이전트로 개발·검증하는 흐름:

```
1. 기능 구현 (Claude Code)
2. Unit tests 작성 (red/green TDD)
3. uvx rodney --help → 브라우저 자동화 준비
4. Rodney로 기능을 브라우저에서 테스트, 스크린샷 캡처
5. 문제 발견 → 수정 → 재테스트
6. showboat로 테스트 워크쓰루 문서 생성
7. 스크린샷/비디오를 PR에 첨부 → 리뷰어에게 증거 제공
```

이 흐름은 [[anti-patterns|"리뷰 안 한 PR 떠넘기기" 안티패턴]]을 방지하는 데에도 효과적이다.

## 선택 가이드

| 상황 | 추천 |
|------|------|
| 크로스 브라우저 (Firefox/WebKit까지) 필요 | Playwright |
| 에이전트 친화 CLI 원함 | agent-browser |
| Chrome만 쓰고 Simon 스타일 워크플로우 | Rodney |
| 테스트 흐름을 문서화하고 싶음 | Showboat (위 도구들과 조합) |

## 관련 문서

- [[agentic-manual-testing]]
- [[gif-optimization-case-study]]
- [[linear-walkthroughs]]
- [[anti-patterns]]
- [[agentic-engineering-guide]]
