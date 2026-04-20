---
title: Ollama (로컬 LLM 실행 플랫폼)
category: tooling
page_type: entity
project: Ollama
tags: [ollama, local-llm, llama-cpp, inference, open-source, on-device]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-14
---
# Ollama

오픈소스 LLM을 로컬 환경에서 간편하게 실행할 수 있도록 설계된 플랫폼. 내부적으로 [[llama-cpp|llama.cpp]]를 백엔드로 사용하며, Docker 스타일의 CLI 인터페이스로 모델 다운로드-실행-관리를 단일 워크플로우로 통합한다.

## 개요

Ollama는 "Start building with open models"를 슬로건으로, Gemma, DeepSeek, Qwen, Llama 등 주요 오픈소스 모델을 한 줄 명령으로 실행할 수 있는 환경을 제공한다. macOS, Windows, Linux 네이티브 설치와 Docker 컨테이너 배포를 모두 지원하며, REST API를 통해 프로그래밍 방식으로 모델과 상호작용할 수 있다. [[on-device-llm|온디바이스 LLM]] 추론의 대중화에 핵심적인 역할을 하고 있다.

## 핵심 아키텍처

### llama.cpp 기반 추론 엔진

Ollama의 추론 엔진은 Georgi Gerganov가 창시한 [[llama-cpp|llama.cpp]] 프로젝트를 기반으로 한다. llama.cpp는 C/C++로 작성된 경량 LLM 추론 라이브러리로, CPU와 GPU(CUDA, Metal, ROCm) 모두에서 효율적으로 양자화된 모델을 실행한다. Ollama는 이 엔진을 감싸서 모델 관리, 서빙, API 계층을 추가한 것이다.

### Modelfile 시스템

Docker의 Dockerfile에 영감을 받은 Modelfile로 모델 구성을 선언적으로 정의한다. 베이스 모델 지정, 시스템 프롬프트 설정, 파라미터 튜닝(temperature, top_p 등), 어댑터 적용 등을 하나의 파일로 관리한다.

### 서빙 아키텍처

로컬에서 HTTP 서버(기본 포트 11434)를 실행하고, OpenAI 호환 API 엔드포인트를 제공한다. 이를 통해 기존 OpenAI SDK 기반 애플리케이션을 최소한의 수정으로 로컬 모델에 연결할 수 있다.

## 사용법

### 기본 실행

```bash
# 설치 (macOS)
brew install ollama

# 모델 실행 (자동 다운로드)
ollama run gemma3

# 대화형 세션
ollama run llama3.2 "한국의 수도는?"
```

### REST API

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [{"role": "user", "content": "Hello"}]
}'
```

### 프로그래밍 라이브러리

Python과 JavaScript 클라이언트 라이브러리를 공식 제공한다.

```python
import ollama
response = ollama.chat(model="gemma3", messages=[
    {"role": "user", "content": "Hello"}
])
```

## 지원 모델 생태계

Ollama는 [[gguf-format|GGUF 포맷]]으로 양자화된 모델을 사용한다. 공식 모델 라이브러리에서 주요 오픈소스 모델을 바로 다운로드할 수 있으며, 커뮤니티가 변환한 커스텀 모델도 지원한다.

| 모델 계열 | 대표 모델 | 특징 |
|-----------|----------|------|
| Meta Llama | Llama 3.2 1B/3B/8B/70B | 범용, 엣지부터 서버까지 |
| Google Gemma | Gemma 3 | 모바일 최적화 |
| DeepSeek | DeepSeek-V3, R1 | 추론 특화 |
| Alibaba Qwen | Qwen 3 | 다국어, 코딩 |
| Microsoft Phi | Phi-4 mini | 소형 고성능 |

## 핵심 특징

### 양자화 지원

[[gguf-format|GGUF]] 양자화 포맷의 다양한 정밀도(Q2, Q4, Q5, Q6, Q8, F16)를 지원한다. 사용자는 모델 크기와 품질 간 트레이드오프를 선택할 수 있다. Q4_K_M이 품질과 크기의 균형점으로 가장 많이 사용된다.

### GPU 가속

NVIDIA CUDA, Apple Metal, AMD ROCm을 통한 GPU 가속을 지원한다. GPU 메모리가 부족한 경우 자동으로 CPU/GPU 분할 추론(offloading)을 수행한다.

### 멀티모달 지원

LLaVA, Gemma 3 등 비전-언어 모델을 지원하여 이미지 입력과 함께 대화할 수 있다.

### 클라우드 배포

Google Cloud, Fly.io, Koyeb 등 클라우드 플랫폼에서의 배포 가이드를 공식 제공한다.

## 에코시스템 통합

Ollama는 로컬 LLM 추론의 사실상 표준 인터페이스로 자리잡으면서, 다양한 도구와 연동된다.

- **[[langchain|LangChain]]/[[langgraph|LangGraph]]**: LLM 체이닝 프레임워크 백엔드
- **Open WebUI**: ChatGPT 스타일 웹 인터페이스
- **[[litellm|LiteLLM]]**: 통합 LLM API 프록시의 로컬 백엔드
- **Coding Agent 통합**: Continue, Aider 등 코딩 에이전트의 로컬 모델 백엔드
- **[[chroma-db|ChromaDB]]**: 로컬 RAG 파이프라인 구축 시 임베딩 모델 제공

## 제한 사항

- 모델 크기가 시스템 RAM/VRAM에 의해 제한된다. 70B 모델은 최소 40GB 이상의 메모리가 필요하다
- [[safetensors]] 포맷을 직접 로드할 수 없으며, GGUF로의 변환이 필요하다
- 분산 추론(multi-node)은 기본 지원하지 않는다
- 파인튜닝 기능은 제공하지 않으며, 추론 전용 도구다

## 관련 페이지

- [[llama-cpp|llama.cpp]] -- Ollama의 추론 백엔드
- [[gguf-format|GGUF 포맷]] -- Ollama가 사용하는 모델 파일 포맷
- [[on-device-llm|온디바이스 LLM]] -- 로컬 LLM 실행의 상위 개념
- [[openrouter|OpenRouter]] -- 클라우드 기반 멀티 모델 게이트웨이 (대조 개념)
- [[litellm|LiteLLM]] -- 통합 API 프록시
