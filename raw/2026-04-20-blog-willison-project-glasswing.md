---
source: simon_willison_blog
title: "Anthropic's Project Glasswing - restricting Claude Mythos to security researchers - sounds necessary to me"
authors: ["Simon Willison"]
date: 2026-04-07
url: "https://simonwillison.net/2026/Apr/7/project-glasswing/"
fetched: 2026-04-20
status: pending_ingest
tags: [claude-mythos, project-glasswing, offensive-security, vulnerability-discovery, model-release-policy, anthropic]
---

## Summary

Anthropic이 Claude Opus 4.6급 신 모델 **Claude Mythos**를 일반 출시하지 않고 **Project Glasswing**을 통해 보안 연구자·파트너사에만 제한 배포한 결정에 대한 Simon Willison의 분석. Willison은 "합리적 trade-off"로 평가.

## Claude Mythos란?

- Claude Opus 4.6과 비슷한 일반 능력
- **사이버보안 연구 능력**이 극적으로 강화된 변형
- Anthropic은 공개 런칭 대신 승인된 security partner에게만 접근 허용

## 능력 격차 (Opus 4.6 vs Mythos)

- Firefox JavaScript exploit 테스트에서
  - Opus 4.6: 수백 회 시도 중 **2회 성공**
  - Mythos: **181회 성공**
- Mythos Preview 사전 테스트에서 "every major OS·web browser에서 thousands of high-severity vulnerabilities" 발견
- 브라우저 샌드박스 escape, 권한 상승 공격 자율 개발 능력

## Project Glasswing 구조

- **파트너사**: AWS, Apple, Microsoft, Google, Linux Foundation 등
- **목적**: 광범위 배포 전에 보안팀이 proactive 패치 가능하도록
- **리소스 배정**
  - $100M 사용 크레딧 할당
  - $4M 오픈소스 보안 조직 직접 기부

## 업계 맥락

- Greg Kroah-Hartman, Daniel Stenberg 등 보안 전문가들이 AI 생성 보안 보고서가 "slop → legitimate threats"로 전환됐다고 경고
- AI 기반 취약점 발견의 워크로드 급증

## Willison의 평가

"합리적 trade-off" — 일반 가용성 지연을 수용하는 대신, 가장 위험한 능력에 대한 safeguard를 개발할 시간 확보.

## 모델 출시 정책 시사점

- 능력별 차등 출시(capability-gated release)가 frontier 모델의 새 표준이 될 수 있음
- responsible disclosure 기간과 유사한 **capability disclosure window** 개념
- 보안 능력이 "dual-use"로 관리되는 전례

## Raw 요약 키워드
Claude Mythos, Project Glasswing, capability-gated release, offensive security, vulnerability discovery, Opus 4.6 comparison, responsible disclosure
