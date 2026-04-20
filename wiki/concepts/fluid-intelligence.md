---
title: Fluid Intelligence (유동 지능)
category: concepts
page_type: concept
tags: [concepts, concept, fluid-intelligence, arc-agi, cognitive-science, intelligence-theory, benchmarks]
sources: [raw/2026-04-14-wiki-expand-scan-2.md]
created: 2026-04-14
updated: 2026-04-14
---
# Fluid Intelligence (유동 지능)

사전 지식이나 학습된 경험에 의존하지 않고, 새로운 상황에서 패턴을 인식하고 추상적 관계를 추론하여 문제를 해결하는 능력. Raymond Cattell이 1941년에 처음 제안한 개념으로, Cattell-Horn-Carroll(CHC) 이론의 핵심 축이며, ARC-AGI 벤치마크가 AI 시스템에서 이 능력을 측정하기 위해 설계되었다.

## 왜 중요한가

유동 지능은 AGI(범용 인공지능) 논의의 핵심 시금석이다. 현재 LLM이 보여주는 대부분의 능력은 결정화 지능(crystallized intelligence) -- 방대한 학습 데이터에서 축적된 지식과 패턴 -- 에 기반한다. 반면 유동 지능은 학습 데이터에 없는 완전히 새로운 문제를 풀 수 있는 능력을 요구하며, 이것이 현재 AI 시스템의 근본적 한계인지 아닌지가 AGI 달성 여부를 가르는 핵심 질문이다.

## Cattell-Horn-Carroll(CHC) 이론

현재 가장 포괄적이고 경험적으로 지지받는 인지 능력 이론으로 널리 인정받고 있다.

### 역사적 발전

- **1941년**: Raymond Cattell이 유동 지능(Gf)과 결정화 지능(Gc)의 구분을 최초 제안
- **1991년**: Cattell의 제자 John Horn이 모델을 9-10개 광범위 능력으로 확장
- **1993년**: John Carroll이 461개 요인분석 연구를 메타분석하여 3층 이론(Three-Stratum Theory) 제안
- **1990년대 후반**: 두 이론의 상당한 유사성으로 인해 통합 -> CHC 이론 탄생

### 3층 위계 구조

- **Stratum III (일반 능력)**: 단일 g 요인 -- 전반적 지능을 대표
- **Stratum II (광범위 능력)**: 9개 주요 인지 영역
- **Stratum I (협소 능력)**: 각 광범위 능력 내의 구체적, 측정 가능한 기술

### 9개 광범위 능력

| 기호 | 능력 | 설명 |
|------|------|------|
| **Gf** | 유동 추론 (Fluid Reasoning) | 미지 정보로 문제 해결, 새로운 환경 적응 |
| **Gc** | 이해-지식 (Comprehension-Knowledge) | 학습된 경험과 축적된 지식으로 추론 |
| **Gq** | 양적 지식 (Quantitative Knowledge) | 수학적 개념과 조작 |
| **Grw** | 읽기-쓰기 능력 (Reading & Writing) | 기초 문해 기술 |
| **Gsm** | 단기 기억 (Short-Term Memory) | 정보의 즉각적 보유와 활용 |
| **Glr** | 장기 저장-인출 (Long-Term Storage & Retrieval) | 정보의 저장과 회상 |
| **Gv** | 시각 처리 (Visual Processing) | 시각 패턴의 지각과 사고 |
| **Ga** | 청각 처리 (Auditory Processing) | 소리의 분석과 변별 |
| **Gs** | 처리 속도 (Processing Speed) | 압박 하에서 자동적 인지 과제 수행 |

### 유동 지능(Gf) vs. 결정화 지능(Gc)

| 측면 | 유동 지능 (Gf) | 결정화 지능 (Gc) |
|------|---------------|----------------|
| 정의 | 양적 추론, 처리 능력, 새로운 환경 적응, 신규 문제 해결 | 경험을 통한 지식 축적 (일반적, 절차적, 선언적) |
| 발달 궤적 | 약 20세에 정점, 이후 감소 | 생애 전체에 걸쳐 지속 증가 |
| 영향 요인 | 생물학적/신경학적 요인 + 환경 상호작용 | 교육, 경험, 문화적 노출 |
| AI 대응 | 신규 과제 일반화, zero-shot 추론 | 사전학습 지식, in-context learning |

Cattell은 유동 지능이 생물학적-신경학적 요인과 환경 상호작용에 의해 영향받으며, 결정화 지능은 유동 지능의 "투자"를 통해 축적된다고 보았다(투자 이론, Investment Theory).

## ARC-AGI 벤치마크

Francois Chollet이 설계한 Abstraction and Reasoning Corpus(ARC)는 AI 시스템의 유동 지능을 직접 측정하기 위한 벤치마크이다.

### 설계 철학

ARC-AGI는 발달심리학에서 식별된 핵심 인지 빌딩 블록(대상 영속성, 목표 지향성, 기초 기하학, 수량 감각)에 기반하며, 언어나 도메인 특화 지식 같은 문화적 산물을 의도적으로 배제한다. 이를 통해 인간과 기계의 추론 능력을 동등한 조건에서 비교하는 "문화 공정(culture-fair)" 평가가 가능하다.

### 과제 구조

3-5개의 입출력 그리드 쌍이 변환 규칙을 시연하고, 풀이 시스템은 기저 논리를 추론하여 새로운 테스트 케이스에 적용해야 한다. 과제 유형은 객체 식별, 기하학적 변환, 공간 추론, 수치 연산, 패턴 완성, 구성적 추론의 6개 범주를 포괄한다.

### 버전별 진화와 성과

| 버전 | 출시 | 핵심 특성 | AI 최고 점수 | 인간 수준 |
|------|------|-----------|-------------|----------|
| **ARC-AGI-1** | 2019 | 평균 1.3단계 구성, 기본 추상화 | 93-96% (2026) | ~98% |
| **ARC-AGI-2** | 2024 | 평균 2.7단계 구성, 문맥 의존 규칙 | 54-69% (공개), 24% (자원 제약) | ~98% |
| **ARC-AGI-3** | 2026 preview | 1000+ 레벨, 150+ 환경, 상호작용형 | 12.58% | 측정 중 |

ARC-AGI-1 점수는 2020년 78.8%에서 2023-2024년 정체기를 거쳐 2026년 Opus 4.6가 93%에 도달하며 급등했다. 그러나 ARC-AGI-2에서는 모든 접근법이 2.5-3배 성능이 하락하며, 구성적 추론(composition) 처리의 근본적 한계를 드러낸다. 인간은 모든 버전에서 거의 완벽에 가까운 성능을 유지한다.

### 2025년 핵심 트렌드: 정제 루프

2025년의 핵심 주제는 "정제 루프(refinement loop)" -- 과제별로 피드백 신호를 통해 프로그램을 반복적으로 최적화하는 접근법 -- 의 부상이다. 테스트 타임 컴퓨트를 대량 투입하여 각 과제에 특화된 솔루션을 탐색하는 전략이 성과를 보이고 있다.

## AI 연구에서의 함의

유동 지능 개념은 AI 능력 평가의 프레임워크를 근본적으로 재구성한다:

- **벤치마크 오염 문제**: 기존 NLP/비전 벤치마크는 결정화 지능을 주로 측정하며, 학습 데이터 유출(contamination)에 취약하다. ARC-AGI는 이 문제를 구조적으로 회피한다.
- **일반화의 정의**: 유동 지능 관점에서 진정한 일반화란 학습 분포 밖의 완전히 새로운 문제를 풀 수 있는 능력이다.
- **스케일링 한계**: 모델 크기와 학습 데이터를 늘리는 것만으로 유동 지능이 자연 발생하는지는 미해결 질문이며, ARC-AGI-2/3의 결과는 현재로서는 부정적 증거를 제시한다.

## 대표 레퍼런스

- [Cattell-Horn-Carroll theory (Wikipedia)](https://en.wikipedia.org/wiki/Cattell%E2%80%93Horn%E2%80%93Carroll_theory)
- [The ARC of Progress towards AGI: A Living Survey (arXiv 2603.13372)](https://arxiv.org/html/2603.13372v1)
- [ARC-AGI: A Benchmark for Fluid Intelligence in the AI Boom (StreamlineFeed)](https://streamlinefeed.co.ke/news/arcagi-a-benchmark-for-fluid-intelligence-in-the-ai-boom-and-the-road-to-agi-727a8ad7)

## 관련 문서

- [[ai-benchmarks-overview|AI Benchmarks Overview]]
- [[ai-reasoning-models|AI Reasoning Models]]
- [[benchmark-saturation-goodharts-law|Benchmark Saturation & Goodhart's Law]]
