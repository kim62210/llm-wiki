---
source: blog
url: https://simonwillison.net/2025/Oct/16/claude-skills/
title: Claude Skills are awesome, maybe a bigger deal than MCP
author: Simon Willison
date: 2025-10-16
fetched: 2026-05-06
status: pending_ingest
tags: [claude-skills, mcp, agent-skills, simon-willison, prompt-engineering]
---

# Claude Skills are awesome, maybe a bigger deal than MCP (Simon Willison)

## 핵심 주장

> "I think Claude Skills will trigger a Cambrian explosion in Skills which will make this year's MCP rush look pedestrian by comparison."

Anthropic의 새 패턴 **Claude Skills**가 MCP보다 더 큰 임팩트를 가질 것이라는 평가.

## Skills 정의

Simon의 요약:
> "A skill is a Markdown file telling the model how to do something, optionally accompanied by extra documents and pre-written scripts."

Skills는 **폴더** 단위로 instructions, scripts, resources를 묶는 시스템.

## 작동 메커니즘

토큰 효율적 시스템:
- 세션 시작 시 Claude의 harness가 skill 파일들을 스캔
- YAML frontmatter에서 짧은 설명만 읽음
- 각 skill은 **수십 개 토큰**만 차지
- Full details는 사용자 요청과 관련 있을 때만 로드됨

## SKILL.md 예시

slack-gif-creator 스킬 메타데이터:
> "Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives."

- 공유 리소스 경로: `/mnt/skills/examples/slack-gif-creator`
- 출력 경로: `/mnt/user-data/outputs/`

## 실제 테스트 사례

Simon이 slack-gif-creator skill 테스트:
- PIL 이미지 라이브러리 사용
- skill의 core 디렉토리에서 `GIFBuilder` 클래스 임포트
- Slack 특화 검증: 파일 크기 **2MB 최대** 제약 확인

## Skills vs MCP 비교

Simon이 Skills를 MCP보다 우수하다고 보는 이유:

### Token 효율
- MCP 구현은 종종 "tens of thousands of tokens of context"를 소비
- 실제 작업할 공간이 부족
- Skills는 metadata만 처음에 로드 → 효율적

### 단순성
- MCP: 프로토콜 사양 필요
- Skills: 실행 가능한 스크립트 + 문서만

### 유연성
- CLI 도구 + `--help` 플래그로 설명 토큰 오버헤드 감소
- "Almost everything I might achieve with an MCP can be handled by a CLI tool instead."

## Skills가 더 큰 deal인 이유

- "nothing preventing them from being used with other models"
- Anthropic 외 다른 모델에서도 동일 패턴 채택 가능
- MCP는 클라이언트 구현 필요, Skills는 prompt + filesystem 패턴

## 미래 응용 시나리오

데이터 저널리즘 워크플로우:
- 인구 조사 데이터 접근 절차
- SQLite/DuckDB 로딩 절차
- S3 publication 방법
- 스토리텔링 프레임워크
- D3 visualization 패턴

→ "data journalism agent that can discover and help publish stories"

## 메모

- 게시일: 2025년 10월 16일
- Anthropic의 동시 발표: "Equipping agents for the real world with Agent Skills" (Barry Zhang, Keith Lazuka, Mahesh Murag)
- Simon은 GitHub에 `/mnt/skills` 내용을 통째로 공개: `simonw/claude-skills`
- 후속 블로그: "Code execution with MCP" (2025-11-04) - Anthropic이 MCP를 코드 실행으로 재정의
