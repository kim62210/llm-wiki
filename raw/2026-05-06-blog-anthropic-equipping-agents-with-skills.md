---
source: blog
url: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
title: Equipping agents for the real world with Agent Skills
author: Barry Zhang, Keith Lazuka, Mahesh Murag (Anthropic)
date: 2025-10-16
fetched: 2026-05-06
status: pending_ingest
tags: [claude-skills, agent-skills, anthropic-engineering, progressive-disclosure, skill-md, mcp-comparison]
---

# Equipping agents for the real world with Agent Skills (Anthropic Engineering)

## 개요

Agent Skills = Claude의 능력을 확장하는 프레임워크. 조직된 디렉토리에 instructions, scripts, resources를 묶어 일반 에이전트를 특화 도구로 변환.

## What Are Agent Skills

> "organized folders of instructions, scripts, and resources that agents can discover and load dynamically"

각 use case별 커스텀 에이전트 빌드 대신, 재사용 가능 능력으로 기존 에이전트 특화 - "onboarding 가이드 작성"과 유사.

## Core Architecture: SKILL.md

모든 skill은 `SKILL.md`로 시작 - YAML frontmatter:
- **name**: skill 식별자
- **description**: 목적 요약

이 메타데이터가 시작 시 Claude의 시스템 프롬프트에 로드 - skill 사용 적절성 인식.

## Progressive Disclosure (3단계 정보 구조)

1. **Level 1**: 시스템 프롬프트의 skill 이름 + 설명
2. **Level 2**: 관련 시 SKILL.md 전체 콘텐츠 로드
3. **Level 3+**: 컨텍스트별 추가 번들 파일 (참조 문서, 특화 지침)

PDF skill 예시:
- 핵심 지침은 SKILL.md에
- form-filling 가이드는 별도 `forms.md`에 - 필요 시에만 접근

## Context Window 관리

Skill 트리거 시 컨텍스트 윈도우를 동적으로 수정 - 불필요한 콘텐츠 로드 회피.
- Filesystem과 code execution 도구가 있는 에이전트는 효율적으로 무제한 skill 콘텐츠 참조 가능

## Code Execution 통합

Skills는 실행 가능 스크립트(Python, Bash)를 번들 가능 - Claude가 결정적으로 실행.

PDF skill 예시: form fields 추출 Python 스크립트 - 전체 PDF나 스크립트 코드를 컨텍스트에 차지하지 않음.

## 개발 모범 사례

- **Capability gaps 식별** - 대표적 작업 테스트
- **Scale 구조** - 거대한 SKILL.md 분할, 상호 배타적 컨텍스트 분리
- **Skill naming 우선** - Claude가 name/description으로 활성화 결정
- **협업 반복** - Claude의 사용 패턴/실패 자가 반성
- **보안 audit** - 파일 콘텐츠, 코드 의존성, 외부 연결 사전 검토

## 보안 고려사항

> "Install skills only from trusted sources"

- 알 수 없는 skill은 audit
- 번들 코드 의존성, 리소스 파일, untrusted 외부 연결 지시문 검토

## 가용성

지원 환경:
- Claude.ai
- Claude Code
- Claude Agent SDK
- Claude Developer Platform

## 향후 방향

- Skill discovery 인프라
- Skill sharing 인프라
- MCP servers와의 보완적 통합

## 메모

- 게시일: 2025년 10월 16일
- Simon Willison의 평가: "Skills will trigger a Cambrian explosion that will make this year's MCP rush look pedestrian"
- Anthropic Cookbook GitHub에 구현 가이드
- Skills의 핵심 차별: progressive disclosure로 토큰 효율 (full MCP는 모든 도구 메타데이터를 시작 시 로드)
