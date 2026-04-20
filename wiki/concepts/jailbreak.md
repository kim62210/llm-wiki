---
title: Jailbreak (LLM 탈옥 공격)
category: concepts
page_type: concept
tags: [concepts, concept, jailbreak, llm-security, red-teaming, adversarial-attacks]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---
# Jailbreak (LLM 탈옥 공격)

LLM에 내장된 안전장치(alignment, content filter, system prompt 제약)를 우회하여 금지된 출력을 유도하는 공격 기법의 총칭. [[agent-prompt-injection-defense|에이전트 프롬프트 인젝션 방어]]가 방어 관점에서 다루는 주제라면, 이 페이지는 **공격 기법 자체의 분류와 메커니즘**에 초점을 둔다.

## 왜 중요한가

2025년 Cisco 연구팀이 DeepSeek R1을 50개 탈옥 프롬프트로 전부 뚫었고, 2026년 Nature Communications 연구에서는 공격 성공률이 97%에 달하는 결과가 보고되었다. JBFuzz(2025) 퍼징 프레임워크는 GPT-4o, Gemini 2.0, DeepSeek-V3 등 주요 모델에서 평균 99%의 공격 성공률을 달성했다. 모델이 강력해질수록 공격 표면도 함께 넓어지며, red-teaming과 safety evaluation의 핵심 평가 축이 되고 있다.

## 공격 기법 분류

### 토큰 수준 공격 (Token-Level)

문자 치환("m4lw@re"), 유니코드 호모글리프, 전략적 공백 삽입, 양성 패딩 토큰 등으로 키워드 기반 안전 필터를 의미 분석 이전 단계에서 우회한다. Base64 등 인코딩 트릭은 76.2%의 성공률을 기록했다.

### 프롬프트 수준 공격 (Prompt-Level)

- **DAN (Do Anything Now)**: 가장 유명한 탈옥 프롬프트 계열. 모델에게 "제한 없는 버전의 자신"을 역할극하도록 지시한다. 2024-2025년 후속 변종이 지속적으로 등장하며 89.6%의 성공률을 보인다.
- **역할극 프레이밍 (Role-Play)**: "영화 시나리오 작성 중인 AI", "보안 연구원에게 보고하는 AI" 등 맥락을 설정하여 책임을 모델 외부로 전가한다.
- **권위 호소 (Authority Appeal)**: 요청이 법 집행기관이나 보안 연구자로부터 온 것처럼 위장한다.
- **번역 공격 (Translation Attack)**: 가상의 시나리오나 저자원 언어를 통해 유해 콘텐츠를 요청한다.

### 대화 기반 공격 (Multi-Turn / Dialogue-Based)

- **크레센도 기법 (Crescendo)**: 여러 턴에 걸쳐 점진적으로 주제를 과격화한다.
- **Deceptive Delight**: 긍정적 프레이밍 안에 위험한 콘텐츠를 삽입하여 분류기를 혼란시킨다 (약 65% 성공률).
- **맥락 퓨전 (Context Fusion)**: 안전한 세그먼트와 위험한 세그먼트를 섞어 안전 분류기를 압도한다.

### 최적화 기반 공격 (Optimization-Based)

퍼징 프레임워크가 시드 프롬프트를 동의어 치환, 구조 변형 등으로 자동 돌연변이시켜 수천 개의 변종을 체계적으로 테스트한다. JBFuzz는 유해 질문당 평균 7회 쿼리, 1분 이내로 공격에 성공했다.

### 프롬프트 유출 (Prompt Leaking)

시스템 프롬프트 추출 공격. 2023년 Bing Chat "Sydney" 유출 사건이 대표적이며, 단순한 프롬프트로도 내부 지시문 전체가 노출될 수 있음을 보여주었다. 시스템 프롬프트 자체가 비즈니스 로직을 담고 있을 때 직접적인 보안 위협이 된다.

## 사회공학적 측면

연구에 따르면 jailbreak에 사용되는 설득 전술(아첨, 교육적 프레이밍, 전문 용어, 권위 호소, 긴급성)은 사람을 대상으로 한 사회공학 기법과 동일한 패턴을 보인다. 유사한 전술이 OpenAI, Anthropic, Google, Meta, 오픈소스 모델 전반에서 모델에 관계없이 작동하며, 성공률만 각 모델의 alignment 접근법에 따라 차이를 보인다.

## Jailbreak vs. Prompt Injection

두 개념은 자주 혼동되지만 구분이 필요하다. Jailbreak은 **모델의 내재된 안전 정렬을 우회**하는 것이 핵심이고, [[prompt-injection|프롬프트 인젝션]]은 **외부 입력을 통해 모델의 지시를 조작**하는 것이 핵심이다. Jailbreak은 주로 사용자가 직접 의도적으로 수행하는 반면, indirect prompt injection은 제3자가 LLM이 처리하는 데이터에 악성 지시를 숨겨놓는 공격이다.

## 방어 접근

- **[[constitutional-classifiers|Constitutional Classifiers]]**: Anthropic이 개발한 헌법적 분류기로, jailbreak 시도를 탐지하고 차단한다.
- **[[alignment-faking|Alignment Faking]] 탐지**: 모델이 학습 중 전략적으로 준수를 위장하는 현상을 포착하여, 표면적 alignment 너머의 실제 행동을 평가한다.
- 입력 정제(Input Sanitization), 프롬프트 설계 강화, 사후 생성 필터, 학습 데이터 위생 관리 등 계층적 방어가 권장된다.

## 대표 레퍼런스

- [LLM Jailbreaks 2024-2026: Techniques, Risks & Defense Strategies (Startup House)](https://startup-house.com/blog/llm-jailbreak-techniques)
- [Red Teaming the Mind of the Machine: Systematic Evaluation of Prompt Injection and Jailbreak (arXiv 2505.04806)](https://arxiv.org/html/2505.04806v1)
- [Investigating LLM Jailbreaking of Popular Generative AI Web Products (Unit 42)](https://unit42.paloaltonetworks.com/jailbreaking-generative-ai-web-products/)

## 관련 문서

- [[constitutional-classifiers|Constitutional Classifiers]]
- [[alignment-faking|Alignment Faking]]
- [[owasp-agentic-top-10|OWASP Agentic Top 10]]
- [[prompt-injection|Prompt Injection]]
- [[agent-prompt-injection-defense|Agent Prompt Injection Defense]]
