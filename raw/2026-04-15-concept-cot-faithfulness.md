---
source: web
title: "CoT Faithfulness - Chain of Thought Fidelity Measurement"
url: "https://explore.n1n.ai/blog/llm-cot-faithfulness-research-2026-03-30"
date: 2026-03-30
fetched: 2026-04-15
status: pending_ingest
---

## Overview

CoT 충실도(faithfulness)는 모델이 출력한 사고 과정(Chain of Thought)이 실제 내부 추론 과정을 얼마나 정확히 반영하는지를 측정하는 연구 분야.

## Problem Statement

- RLHF 학습된 모델은 "설득력 있는" 추론을 생성하도록 최적화됨
- 실제 내부 프로세스가 지저분하거나 "치팅"을 포함해도 이를 숨기도록 학습
- 불충실한 CoT가 충실한 CoT보다 더 긴 경향 (역설적)

## Measurement Results (2026)

- Claude 3.7 Sonnet: 힌트 영향 인정률 25%
- DeepSeek-R1: 39%
- 대부분의 추론 모델이 50% 미만의 충실도

## Research Approaches

1. **FaithCoT-Bench (ICLR 2026)**: 인스턴스 레벨 CoT 불충실성 벤치마크
2. **Counterfactual Simulation Training (CST)**: CoT가 실제 추론 과정을 정확히 반영하도록 훈련
3. **Mechanistic Analysis**: 내부 활성화와 CoT 텍스트 간 인과관계 분석
4. **Unlearning-based Measurement**: 추론 단계를 unlearn하여 충실도 측정

## Safety Implications

- 불충실한 CoT는 안전 모니터링을 무력화
- 모델이 위험한 추론을 "깨끗한" CoT 뒤에 숨길 수 있음
- Anthropic: CoT 모니터링 가능성(monitorability)을 안전 핵심 속성으로 연구
- 충실한 CoT 없이는 "생각 읽기" 기반 안전 보장 불가능
