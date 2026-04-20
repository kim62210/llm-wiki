---
title: Structured Output (구조화된 출력)
aliases: [structured output, 구조화된 출력, constrained decoding, JSON mode, 제약 디코딩]
category: concepts
page_type: concept
tags: [structured-output, constrained-decoding, json, inference, production, BAML, xGrammar, 2024-2026]
sources: [raw/2026-04-14-wiki-expand-scan.md]
created: 2026-04-14
updated: 2026-04-20
---
# Structured Output (구조화된 출력)

## 정의

**Structured Output**은 LLM이 JSON, XML, YAML 등 사전 정의된 스키마에 맞는 형식화된 출력을 생성하도록 강제하는 기술이다. 자유 형식 텍스트 대신 프로그래밍적으로 파싱 가능한 구조를 보장함으로써, LLM 출력을 소프트웨어 파이프라인에 안정적으로 통합할 수 있게 한다.

## 왜 필요한가

LLM은 본질적으로 자연어 텍스트를 생성한다. 프로덕션 시스템에서는 이 출력을 코드로 처리해야 하는데, 형식이 불안정하면:

- JSON 파싱 실패로 파이프라인 중단
- 누락된 필드로 인한 다운스트림 오류
- 타입 불일치 (문자열 대신 숫자가 필요한 곳에 텍스트)
- 예상 외 필드 추가로 인한 보안 위험

[[agentic-ai-production|에이전틱 AI 프로덕션]]에서 도구 호출(tool calling)의 파라미터 전달은 structured output의 대표적 적용 사례다.

## 접근법의 진화: 3세대

### 1세대: 프롬프트 엔지니어링 (80-95% 신뢰도)

[[prompt-engineering|프롬프트]]에 "JSON으로 응답하시오"라고 지시하고, [[few-shot-learning|few-shot]] 예시로 형식을 안내. 대부분 작동하지만 **구문 오류 방지를 보장할 수 없다**. 정규식으로 후처리하는 패턴이 흔했다.

### 2세대: Function Calling / Tool Use (95-99%)

OpenAI가 2023년 도입. 함수 시그니처를 API에 전달하면 모델이 해당 형식으로 응답. JSON Schema로 필드와 타입을 정의하되, 간헐적 오류 가능.

### 3세대: Constrained Decoding (100% 스키마 유효성)

2024-2025년에 프로덕션 레벨에 도달. 추론 시점에 토큰 생성을 제한하여 **구문 오류가 구조적으로 불가능**하게 만든다.

## Constrained Decoding의 작동 원리

### 핵심 메커니즘

매 토큰 생성 단계에서:

1. 모델이 전체 어휘에 대한 로짓(logit) 분포를 계산
2. **문법 엔진**이 현재 상태에서 허용 가능한 토큰만 마스킹
3. 마스킹된 분포에서 [[temperature-sampling|샘플링]]
4. 결과적으로 스키마를 위반하는 토큰은 **절대 선택되지 않음**

### 주요 엔진 (2025-2026)

| 엔진 | 개발 | 특성 |
|---|---|---|
| **XGrammar** | xAI/커뮤니티 | 어휘를 context-independent/dependent 집합으로 분할. 기존 방법 대비 **100배 속도** 향상 |
| **llguidance** | Microsoft | Rust 기반. 128K 어휘에서 토큰당 **약 50 마이크로초** CPU 시간 |
| **Outlines** | .txt | Python 기반 오픈소스. JSON Schema, 정규식, CFG 지원 |
| **LMQL** | ETH Zurich | SQL 스타일 쿼리 언어로 제약 조건 표현 |

### CFG-Level 표현력

XGrammar과 llguidance는 Context-Free Grammar(CFG) 수준의 표현력을 지원한다. JSON Schema뿐 아니라 임의의 문법 규칙을 정의하여 복잡한 출력 구조를 강제할 수 있다.

## 주요 제공업체 지원 현황 (2026)

2026년 기준, 모든 주요 제공업체가 네이티브 structured output을 지원한다:

- **OpenAI**: `response_format: { type: "json_schema", json_schema: {...} }`
- **Anthropic Claude**: Tool use with JSON Schema
- **Google Gemini**: `response_mime_type` + `response_schema`
- **Mistral**: Function calling + JSON mode
- **Amazon Bedrock**: Converse API with tool configuration

## JSON vs. XML

| 측면 | JSON | XML |
|---|---|---|
| LLM 친화성 | 높음 (객체, 배열, 문자열 매핑 자연스러움) | 중간 (태그 기반 구조, 토큰 소모 큼) |
| 스키마 도구 | 풍부함 (JSON Schema 생태계) | 있음 (XSD, 그러나 LLM 생태계 지원 부족) |
| 프로덕션 사용 | 압도적 다수 | 레거시 시스템 연동 시 |
| 파싱 | `JSON.parse()` 한 줄 | DOM/SAX 파서 필요 |

2026년 현재 LLM 생태계에서는 **JSON이 사실상 표준**이다.

## 설계 패턴

### Pydantic / Zod 모델 연동

스키마를 코드의 타입 시스템으로 정의하고 자동으로 JSON Schema를 생성하는 패턴. Instructor(Python), Vercel AI SDK(TypeScript) 등이 이 패턴을 구현한다.

### 점진적 파싱 (Streaming)

전체 JSON이 완성되기 전에 부분적으로 파싱하여 UI에 실시간 표시하는 패턴. `{ "title": "..." }`의 title 필드가 생성되는 즉시 렌더링.

### 재시도와 자기 치유

constrained decoding이 없는 환경에서, 출력이 스키마를 위반하면 오류 메시지와 함께 재시도를 요청하는 패턴. Instructor 라이브러리의 핵심 기능이다.

## 한계와 주의점

### 품질 대 형식의 트레이드오프

형식 제약이 강할수록 모델의 "사고 공간"이 줄어들 수 있다. 복잡한 추론이 필요한 태스크에서 즉시 JSON을 요구하면 품질이 하락할 수 있다. [[chain-of-thought|CoT]] 추론 후 structured output을 생성하는 2단계 접근이 권장된다.

### 스키마 설계의 중요성

JSON Schema의 필드 이름, 설명, 열거형 값이 모델의 출력 품질에 직접 영향을 준다. 스키마 자체가 일종의 프롬프트이므로, 명확하고 서술적인 필드명을 사용해야 한다.

## BAML: 타입 안전 LLM 출력 DSL (추가)

BoundaryML이 개발한 BAML(Basically A Made-up Language)은 LLM 함수를 타입 안전하게 정의하는 도메인 특화 언어(DSL)다.

```baml
function ExtractPerson(text: string) -> Person {
  client GPT4o
  prompt #"
    Extract the person from: {{ text }}
    {{ ctx.output_format }}
  "#
}

class Person {
  name string
  age int
  occupation string?
}
```

- Python, TypeScript, Ruby 등으로 컴파일
- 재시도(retry), 스트리밍, 폴백 내장
- LLM 출력 파싱 실패를 컴파일 타임에 타입으로 명시

## xGrammar의 성능 혁신 (추가)

MLC-LLM 팀의 xGrammar(2024)는 제약 디코딩 오버헤드 문제를 해결했다.

- 문법 구조를 context-independent/dependent 집합으로 분할해 사전 컴파일
- CUDA 커널 최적화로 GPU에서 효율적 마스킹
- LLM 추론 시간 대비 제약 디코딩 오버헤드를 1% 미만으로 감소 (기존 방법 대비 100배 속도 향상)

## 관련 문서

- [[prompt-engineering]] -- 1세대 접근법
- [[few-shot-learning]] -- 형식 제어를 위한 예시 제공
- [[temperature-sampling]] -- constrained decoding이 샘플링과 결합하는 방식
- [[agentic-ai-production]] -- structured output의 핵심 사용처
- [[hallucination]] -- 형식은 보장하되 내용의 정확성은 별개
- [[함수 호출과 도구 사용]] -- 함수 호출 기반 구조화 출력
- [[복합 AI 시스템 (Compound AI Systems)]] -- 파이프라인에서 구조화 출력의 역할
