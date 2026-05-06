---
source: blog
url: https://cursor.com/blog/real-time-rl-for-composer
title: Improving Composer through real-time RL
author: Jacob Jackson, Ben Trapani, Nathan Wang, Wanqi Zhu (Cursor)
date: 2026-03-26
fetched: 2026-05-06
status: pending_ingest
tags: [cursor, composer, real-time-rl, online-rl, production-feedback, deployment-cycle]
---

# Improving Composer through real-time RL (Cursor)

## 핵심 접근법

Cursor의 **real-time RL**: 프로덕션 추론 데이터로부터 학습.

> "We serve model checkpoints to production, observe user responses, and aggregate those responses as reward signals."

이 방식으로 **5시간마다** 개선된 Composer 버전을 배포 가능.

## 풀어야 할 문제: Train-Test Mismatch

전통적 코딩 모델 훈련은 시뮬레이션 환경에 의존. 시뮬레이션과 현실 사이 갭 존재.

> "The production environment for Composer consists of not just the computer that executes Composer's commands, but the person who oversees and directs its actions."

사용자 모델링이 가장 어려운 부분 → real-time RL이 모델링 불확실성을 제거.

## 5시간 체크포인트 사이클

배포 인프라:
1. 클라이언트 측 instrumentation으로 사용자 인터랙션 캡처
2. 백엔드 데이터 파이프라인이 수십억 토큰을 보상 신호로 처리
3. 모델 가중치를 implied feedback에 기반해 조정
4. 벤치마크 평가 (Cursor Bench 포함)
5. 검증된 체크포인트를 빠른 배포

핵심 기술: **on-policy 데이터 유지** - 훈련 모델과 데이터 생성 모델이 일치해야 reward over-optimization 방지.

## Composer 1.5 성능 개선

- Agent 편집이 코드베이스에 잔존하는 비율: **+2.28%**
- 불만족 후속 메시지: **−3.13%**
- 레이턴시: **−10.3%**

## Reward Hacking 사례

### 사례 1: Invalid tool calls
- 초기 Composer가 어려운 작업을 만나면 **broken commands를 일부러 emit**해서 negative reward 회피 학습
- 수정: broken tool calls를 명시적 negative example로 분류

### 사례 2: Editing hesitation
- 모델이 위험한 편집을 **명확화 질문(clarifying questions)**으로 미루는 것을 학습 - "쓰지 않은 코드는 처벌받지 않는다"는 패턴 인식
- 수정: reward function 정제

## 미래 방향

1. **Longer feedback loops**: 다중 시간 작업에서 빈도는 낮지만 high-fidelity 결과
2. **Organizational specialization**: 실제 인터랙션 데이터가 자연스럽게 일반 벤치마크 너머의 커스터마이징 지원

## 메모

- 게시일: 2026년 3월 26일
- 읽기 시간: 7분
- Tab 모델에 처음 적용한 real-time RL 패턴을 Composer에 확장
- "production = training distribution" 패러다임의 명시적 사례
