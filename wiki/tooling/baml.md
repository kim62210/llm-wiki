---
title: BAML
category: tooling
page_type: entity
project: BAML
tags: [tooling, entity, baml, dev-tooling-and-frameworks]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/baml.md, raw/hot-topics-sources/2026-04-10/423-baml-official-docs.md, raw/hot-topics-sources/2026-04-10/424-boundary-ml-homepage.md, raw/hot-topics-sources/2026-04-10/425-boundaryml-baml-github.md, raw/hot-topics-sources/2026-04-10/426-structured-outputs-create-false-confidence-baml-blog.md, raw/hot-topics-sources/2026-04-10/427-baml-go-package.md]
created: 2026-04-10
updated: 2026-04-10
---
# BAML

이 페이지는 BAML를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL이기 때문이다.

## 정의

프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL.

## 왜 지금 중요한가

Schema-Aligned Parsing(SAP) 알고리즘으로 새 모델 출시 Day-1부터 구조화 출력이 작동하고, 2026년 들어 Python/TS/Ruby/Go/Java/C#/Rust까지 지원 언어가 확장되며 "스트링 기반 프롬프트 → 스키마 엔지니어링" 전환의 대표 도구가 됐다.

## 개요

이 페이지는 **BAML** 자체를 지속적으로 누적·갱신하기 위한 허브 페이지다.

## 대표 자료

- [BAML Official Docs](https://docs.boundaryml.com/home)
- [Boundary ML Homepage](https://boundaryml.com/)
- [BoundaryML/baml GitHub](https://github.com/BoundaryML/baml)
- [Structured Outputs Create False Confidence — BAML Blog](https://boundaryml.com/blog/structured-outputs-create-false-confidence)
- [baml Go Package](https://pkg.go.dev/github.com/boundaryml/baml)

## 해석 포인트

BAML은 단순한 제품 소개보다 **모델 능력보다 개발자 경험과 운영 통합면이 중요한 도구 축** 으로 읽는 편이 유용하다. 이번 source 묶음에서도 `boundaryml.com×2, docs.boundaryml.com×1, github.com×1, pkg.go.dev×1`처럼 연구·문서·구현체 신호가 함께 모여 있어, 단일 발표보다 생태계 위치를 같이 봐야 한다.

실무에서는 이 엔티티를 '최신인가?'보다 **어떤 운영 전제와 통합면을 요구하는가**로 평가해야 한다. 즉 통합 난이도, 관측 가능성, 운영 비용, 교체 가능성 같은 기준으로 다른 대안과 비교해야 실제 도입 판단에 도움이 된다.

## 2026년 4월 큐레이션 요약

- 정의: 프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL.
- 왜 중요한가: Schema-Aligned Parsing(SAP) 알고리즘으로 새 모델 출시 Day-1부터 구조화 출력이 작동하고, 2026년 들어 Python/TS/Ruby/Go/Java/C#/Rust까지 지원 언어가 확장되며 "스트링 기반 프롬프트 → 스키마 엔지니어링" 전환의 대표 도구가 됐다.
- 직접 수집 원문: 5개
- 주요 도메인: boundaryml.com×2, docs.boundaryml.com×1, github.com×1, pkg.go.dev×1

## 핵심 포인트

BAML는 현재 시점에서 하나의 제품/모델/프레임워크 허브로 읽는 편이 맞다. 기본 정의는 이 페이지는 BAML를 허브처럼 따라가기 위한 엔티티 문서다. 현재 맥락에서 중요한 이유는 프롬프트를 타입 안전한 함수로 정의하는 구조화 출력 전용 DSL이기 때문이다.이며, 직접 수집한 source 5건은 boundaryml.com×2, docs.boundaryml.com×1, github.com×1, pkg.go.dev×1처럼 여러 채널에 걸쳐 분포한다.

## source로 보면

수집된 source는 boundaryml.com×2, docs.boundaryml.com×1, github.com×1, pkg.go.dev×1로 분포한다. 공식 문서와 구현 저장소가 같이 있어 실제 도입 관점의 정보가 강한 편이다.

## 실무 관점

도구/프레임워크 페이지는 기능 목록보다 생태계 위치가 중요하다. 어떤 모델·런타임·개발 흐름과 잘 맞는지, 그리고 팀 워크플로우에 어떤 경계 조건을 추가하는지까지 같이 봐야 한다.

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/baml.md`

### source별 핵심 신호

- **🏠 Welcome | Boundary Documentation** (`docs.boundaryml.com`): https://docs.boundaryml.com/home
  - 메모: Just as TSX/JSX provided the ideal abstraction for web development, BAML offers the perfect abstraction for prompt engineering. Watch our demo video to see it in action.
- **BAML** (`boundaryml.com`): https://boundaryml.com
  - 메모: Yes, we made a whole VSCode extension for BAML.
- **GitHub - BoundaryML/baml: The AI framework that adds the engineering to prompt engineering (Python/TS/Ruby/Java/C#/Rust/Go compatible) · GitHub** (`github.com`): https://github.com/BoundaryML/baml
  - 메모: To see all available qualifiers, see our documentation.
- **Structured Outputs Create False Confidence | BAML Blog** (`boundaryml.com`): https://boundaryml.com/blog/structured-outputs-create-false-confidence
  - 메모: Update (Dec 21): this post is now on the Hacker News front
- **baml module - github.com/boundaryml/baml - Go Packages** (`pkg.go.dev`): https://pkg.go.dev/github.com/boundaryml/baml
  - 메모: Opens a new window with list of versions in this module.


## source 종합 해석

`BAML`는 단일 발표보다 **여러 source가 어떤 관점에서 이 대상을 규정하는가**를 함께 읽을 때 의미가 커진다.

이번 수집에서는 🏠 Welcome | Boundary Documentation, BAML, GitHub - BoundaryML/baml: The AI framework that adds the engineering to prompt engineering (Python/TS/Ruby/Java/C#/Rust/Go compatible) · GitHub처럼 출시 공지·문서·평가 신호가 같이 모여, 기능 자체보다 생태계 위치와 운영 전제가 더 중요하다는 점이 드러난다.

함께 읽을 문서로는 ai-hot-topics-2026-04, pydantic-ai, claude-agent-sdk가 유용하다. 이 페이지가 다루는 주제의 인접 개념·구현·평가 층위를 보강해 준다.

## 실무 체크리스트

- 이 문서를 읽을 때는 이름보다 **어떤 병목을 해결하고 어떤 비용을 새로 만드는지**를 먼저 본다.
- 도입 판단 시 기능 목록만 보지 말고, 공식 문서·릴리스 노트·벤치마크가 서로 얼마나 일관되게 같은 메시지를 주는지 확인한다.
- 비교 후보와의 차이는 API/운영 통합, 성능 수치, 생태계 성숙도 같은 기준으로 정리하는 것이 좋다.

## 관련 문서

- [[ai-hot-topics-2026-04]]
- [[pydantic-ai]]
- [[claude-agent-sdk]]
