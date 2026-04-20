---
title: Google AI Studio + Antigravity
category: tooling
page_type: entity
project: Google AI Studio
tags: [google, ai-studio, antigravity, firebase, vibe-coding, [[coding-agent|agent]]-ide, gemini]
sources: [raw/2026-04-14-ai-hot-topics-100.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

Google AI Studio + Antigravity는 Google이 제공하는 에이전트 퍼스트 IDE와 풀스택 앱 빌더 통합 플랫폼이다. Antigravity는 AI Studio 내장 코딩 에이전트로, 자연어 프롬프트에서 프로덕션 수준의 웹 애플리케이션을 빌드한다. Firebase 백엔드 인프라와 직접 통합되어 데이터베이스, 인증, 호스팅까지 한 곳에서 처리할 수 있다.

Antigravity는 원래 2025년 11월 독립 VS Code 기반 IDE로 출시되었다(Windsurf 팀 $2.4B 인수 기반). 이후 2026년 3월 20일 AI Studio의 브라우저 기반 Build 모드에 직접 통합되었다. 기존 Firebase Studio(구 Project IDX)는 출시 약 11개월 만에 점진적 종료되었으며, AI Studio로 기능이 통합되고 있다.

## 핵심 특징

### Antigravity 코딩 에이전트

GitHub Copilot이나 Cursor와 근본적으로 다른 방식으로 동작한다 -- 코드 제안을 넘어 에이전트가 전체 개발 과정을 주도한다:

- 자연어로 전체 앱 구조 생성 (프론트엔드 + 백엔드 + DB 스키마)
- 체크포인트 기반 워크플로: 목표 기술 -> 프로젝트 구조 계획 -> 코드 작성 -> 테스트 -> 사용자 승인 요청
- 실시간 프리뷰로 변경사항 즉시 확인
- 텍스트 입력 또는 음성 입력(speech-to-text) 지원
- "I'm Feeling Lucky" 버튼으로 AI가 프로젝트 아이디어 생성
- AI Chips: 이미지 생성, Google Maps 등 특정 기능을 원클릭으로 추가

### Firebase 네이티브 통합

에이전트가 프롬프트에서 백엔드 필요성을 자동 감지하고 Firebase 서비스를 프로비저닝한다:

- **Firestore**: NoSQL 데이터베이스 스키마 자동 생성, 초기 보안 규칙 설정, 실시간 데이터 동기화
- **Authentication**: Google 로그인, 이메일/패스워드 인증 자동 설정
- **Cloud Functions**: 서버리스 백엔드 로직 자동 배포
- **Hosting**: Google Antigravity 인프라에 원클릭 배포, 공유 가능한 URL 즉시 생성

기존 Firebase 프로젝트 연결도 가능하며, 이 경우 기존 Firestore 데이터와 인증 설정이 유지된다.

### 멀티플레이어 앱 빌더

여러 사용자가 동시에 동일한 프로젝트에서 작업할 수 있는 협업 기능을 제공한다. Anti-Gravity 프로젝트에서 유래한 실시간 협업 인프라:

- 소켓 연결 기반 실시간 데이터 동기화
- 자동 충돌 해결(conflict resolution)
- 오프라인 큐잉과 재접속 시 동기화
- 라이브 프레즌스 감지와 상태 동기화

실제 활용 사례: 멀티플레이어 레이저 태그 게임(실시간 리더보드), 협업 3D 파티클 시각화 등

## 기술 상세

### 아키텍처

```mermaid
graph TD
    A[자연어 프롬프트<br/>텍스트/음성] --> B[Google AI Studio<br/>Build 모드]
    B --> C[Antigravity 에이전트<br/>[[gemini-3-1-pro|Gemini]] 2.5 Pro]
    C --> D[프론트엔드 생성<br/>React/Angular/Next.js]
    C --> E[백엔드 생성<br/>Cloud Functions]
    C --> F[DB 스키마<br/>Firestore + 보안 규칙]
    D --> G[실시간 프리뷰]
    E --> H[Firebase 배포<br/>Antigravity 호스팅]
    F --> H
    G --> I[사용자 리뷰 + 수정<br/>반복 프롬프트]
    I --> C
    H --> J[프로덕션 앱<br/>공유 URL]
    
    K[코드 다운로드] --> L[로컬 개발<br/>npm install && npm run dev]
    H --> K
```

### Gemini 모델 구성

Gemini 2.5 Pro가 Build 모드의 권장 모델로 자동 선택된다. Gemini 3.1 Pro, Gemini 3.1 Flash 등 Gemini 패밀리 모델을 지원하며 복잡도-비용-속도 트레이드오프에 따라 선택한다. AI Studio는 Gemini 전용 -- Claude, GPT 등 다른 모델은 사용 불가하다.

### 지원 프레임워크

- **React** (주력)
- **Angular**
- **Next.js**
- npm 패키지 자동 설치 (프롬프트 기반)
- Framer Motion(애니메이션), Shadcn(UI 컴포넌트) 등 전문 라이브러리 자동 구성
- Vue.js, Svelte 지원은 추후 추가 예정

### Firebase Studio와의 관계

| 항목 | Firebase Studio (구) | AI Studio + Antigravity (신) |
|------|---------------------|----------------------------|
| 핵심 | 클라우드 IDE | 에이전트 퍼스트 IDE |
| AI 역할 | 코드 어시스턴트 | 풀스택 앱 빌더 에이전트 |
| 개발 방식 | 코드 직접 작성 | 자연어 프롬프트 기반 |
| 상태 | 2026.03 종료 (출시 ~11개월) | 활발히 개발 중 |

### 가격 구조

| 항목 | 비용 |
|------|------|
| 프로토타이핑/테스트 | 무료 |
| Gemini API (프로덕션) | 토큰 기반 과금 |
| Firebase 백엔드 | Spark(무료) / Blaze(종량제) |

주요 경쟁 도구(Cursor $20/월, Replit $25/월) 대비 "유의미한 무료 티어가 있는 유일한 풀스택 바이브 코딩 도구"를 표방한다.

### 한계

- Google 생태계(Gemini + Firebase) 종속
- 대규모 리팩토링에서 의도하지 않은 사이드 이펙트 발생 가능
- 프로덕션 규모의 Gemini API 비용 예측이 어려움
- Google의 제품 지속성 리스크 (Firebase Studio 11개월 만에 종료 선례)

### 경쟁 포지션

Google AI Studio는 [[vibe-coding-platforms]]과 동일한 "자연어로 앱 빌드" 시장에 위치하면서도, Google Cloud/Firebase 인프라와의 네이티브 통합으로 차별화한다. Replit, v0 등이 범용 플랫폼을 지향하는 반면, AI Studio는 Google 생태계 안에서의 풀스택 개발에 최적화되어 있다. 코드 다운로드 후 로컬에서 `npm install && npm run dev`로 독립 개발 전환도 가능하다.

## 관련 문서

- [[vibe-coding-platforms]] - 바이브 코딩 플랫폼 비교
- [[vibe-coding]] - 바이브 코딩 개념
- [[kiro]] - AWS 스펙 드리븐 IDE
- [[google-stitch]] - Google Stitch 디자인 도구
