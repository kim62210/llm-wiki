---
title: Google ADK (Agent Development Kit)
category: tooling
page_type: entity
project: Google ADK
tags: [tooling, entity, google, adk, [[coding-agent|agent]], a2a, vertex-ai, multi-agent]
sources: [raw/2026-04-14-ai-hot-topics-100.md]
created: 2026-04-14
updated: 2026-04-14
---
# Google ADK (Agent Development Kit)

Google의 코드 퍼스트(Code-First) 오픈소스 AI 에이전트 개발 프레임워크. Python, Java, Go, TypeScript 4개 언어를 지원하며, A2A(Agent-to-Agent) 프로토콜 내장과 Vertex AI 배포 최적화가 핵심 차별점이다.

## 개요

Google ADK는 프로덕션 수준의 AI 에이전트를 "빌드, 디버그, 배포"하기 위한 엔터프라이즈급 오픈소스 프레임워크다. "프로토타입이 아닌 프로덕션 에이전트"를 표방하며, LangGraph, OpenAI Agents SDK, Mastra 등과 경쟁하면서도, Google Cloud 생태계(Vertex AI, Cloud Run, GKE)와의 네이티브 통합과 A2A 프로토콜 내장으로 차별화한다. ADK Go 1.0과 ADK Java 1.0이 최근 정식 릴리스됐다.

## 핵심 특징

### 멀티 언어 지원

| 언어 | 상태 | 주요 대상 |
|------|------|-----------|
| Python | Stable | 범용, ML 엔지니어 |
| TypeScript | Stable | 웹/풀스택 개발자 |
| Java | 1.0 출시 | 엔터프라이즈 |
| Go | 1.0 출시 | 인프라/시스템 |

### 에이전트 유형

| 유형 | 설명 |
|------|------|
| **LLM Agent** | LLM 기반 추론 에이전트 |
| **Workflow Agent** | Sequential, Loop, Parallel 워크플로우 |
| **Custom Agent** | 커스텀 로직 에이전트 |
| **Multi-Agent** | 다중 에이전트 오케스트레이션 |

### 모델 지원
- **Gemini** / **Gemma** (Google 네이티브)
- **Claude** (Anthropic)
- **Vertex AI 호스팅 모델**
- **Ollama** / **vLLM** / **LiteLLM** (오픈소스)

### A2A(Agent-to-Agent) 프로토콜
에이전트 간 통신을 위한 표준 프로토콜을 내장하여, 서로 다른 프레임워크나 언어로 작성된 에이전트들이 상호 운용할 수 있다. A2A는 Linux Foundation 프로젝트로 이관되어 150개 이상의 조직이 참여하고 있으며, Python/Go/Java에서 퀵스타트 구현을 제공한다. 이를 통해 ADK로 작성한 에이전트가 OpenAI Agents SDK, LangGraph, 또는 다른 프레임워크로 작성한 에이전트와 표준화된 방식으로 통신할 수 있다.

## 기술 상세

### 아키텍처

```mermaid
flowchart TB
    subgraph "Google ADK 아키텍처"
        A[Python / TypeScript / Java / Go SDK]
        B[에이전트 런타임]
        C[컨텍스트 관리 -- 구조화된 데이터]
        D[세션 & 메모리]
        E[도구 통합]
        F[평가 프레임워크]
    end
    subgraph "도구 레이어"
        E1[Function Tools]
        E2[[[model-context-protocol|MCP]] Tools]
        E3[OpenAPI Tools]
    end
    subgraph "배포 대상"
        G1[Vertex AI -- Agent Engine]
        G2[Cloud Run]
        G3[GKE]
        G4[자체 인프라 -- 컨테이너]
    end
    A --> B --> C
    B --> D
    B --> E --> E1 & E2 & E3
    B --> F
    B --> G1 & G2 & G3 & G4
```

### 컨텍스트 관리

ADK는 컨텍스트를 "소스 코드처럼" 취급한다. 단순 문자열 연결(Concatenation)이 아니라 **구조화된 데이터(Structured Data)** 로 관리하며:

- **자동 필터링**: 관련 없는 이벤트를 컨텍스트에서 자동 제외
- **대화 요약**: 오래된 대화 턴을 요약(Summarize)하여 토큰 효율 유지
- **지연 로딩 아티팩트**: 아티팩트를 필요할 때만 로드하여 메모리 효율화
- **토큰 사용량 추적**: 세션별, 에이전트별 토큰 소비를 모니터링

### 세션 관리

- **되감기(Rewind) 가능 세션**: 디버깅을 위해 이전 상태로 되돌리기 지원
- **세션 마이그레이션**: 에이전트 간 또는 환경 간 세션 이전
- **영속적 상태 및 메모리**: 세션 종료 후에도 상태와 메모리 유지

### 도구 통합
- **Function Tools**: Python/TypeScript/Java/Go의 callable을 직접 도구로 등록
- **MCP Tools**: Model Context Protocol 호환 도구 연결
- **OpenAPI Tools**: REST API의 OpenAPI 스펙 기반 자동 통합
- **내장 통합**: Google Search, Vertex AI Search 등 Google 서비스 네이티브 연동
- **Apigee AI Gateway**: 엔터프라이즈 API 관리와 통합

### 평가 프레임워크
- 시각적 디버깅 인터페이스로 에이전트 실행 흐름 추적
- 커스텀 메트릭 정의와 사용자 인터랙션 시뮬레이션
- 에이전트 품질을 체계적으로 측정하고 회귀 테스트 수행

### 스트리밍
Gemini Live API Toolkit을 통해 실시간 스트리밍을 지원한다. 오디오, 이미지, 비디오를 포함하는 멀티모달 스트리밍이 가능하며, 개발 가이드 파트 1-5로 단계별 구현을 안내한다.

### 배포 옵션

| 대상 | 특징 |
|------|------|
| Vertex AI (Agent Engine) | 관리형, 인증/추적 내장 |
| Cloud Run | 서버리스 컨테이너 |
| GKE | Kubernetes 기반 스케일링 |
| 자체 인프라 | 컨테이너화된 배포 |

### 경쟁 프레임워크 비교

| 특성 | Google ADK | LangGraph | OpenAI Agents SDK | Mastra |
|------|-----------|-----------|-------------------|--------|
| 언어 | Python, TS, Java, Go | Python, TS | Python | TypeScript |
| 멀티에이전트 | 내장 오케스트레이션 | 그래프 기반 | Handoff 패턴 | 워크플로우 기반 |
| 에이전트 간 프로토콜 | A2A 내장 | 미지원 | 미지원 | 미지원 |
| 클라우드 배포 | Vertex AI 네이티브 | LangSmith | OpenAI 플랫폼 | Vercel 중심 |
| MCP 지원 | 지원 | 지원 | 지원 | 지원 |
| 모델 범위 | 멀티 프로바이더 | 멀티 프로바이더 | OpenAI 중심 | 멀티 프로바이더 |

ADK의 주요 차별점은 (1) 4개 언어를 공식 지원하는 폭넓은 개발자 도달 범위, (2) A2A 프로토콜 내장으로 이기종 에이전트 간 상호 운용, (3) Google Cloud 네이티브 배포 최적화이다.

### 설치

```bash
# Python
pip install google-adk

# TypeScript/JavaScript
npm install @google/adk

# Go
go get google.golang.org/adk

# Java (Maven)
# com.google.adk:google-adk
```

## 관련 문서

- [[model-context-protocol-mcp]] -- ADK가 지원하는 MCP 도구 통합
- [[multi-agent-[[multi-agent-orchestration|orchestration]]]] -- 멀티에이전트 오케스트레이션 개념
- [[langgraph]] -- 경쟁 프레임워크: LangGraph
- [[openai-agents-sdk]] -- 경쟁 프레임워크: OpenAI Agents SDK
- [[mastra]] -- 경쟁 프레임워크: Mastra
- [ADK 공식 문서](https://adk.dev/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [ADK for TypeScript 발표](https://developers.googleblog.com/introducing-agent-development-kit-for-typescript-build-ai-agents-with-the-power-of-a-code-first-approach/)
- [ADK for Java 1.0 발표](https://developers.googleblog.com/announcing-adk-for-java-100-building-the-future-of-ai-agents-in-java/)
