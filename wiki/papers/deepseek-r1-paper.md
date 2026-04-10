---
title: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
category: papers
page_type: paper
tags: [paper, training, reasoning, rlvr]
sources: [raw/hot-topics-sources/2026-04-10/261-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learnin.md]
created: 2026-04-10
updated: 2026-04-10
---

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

인간 라벨 reasoning trace 없이도 pure RL만으로 reasoning 패턴이 출현할 수 있음을 강하게 보여준 전환점 논문이다.

## 핵심 기여

- human-labeled reasoning trajectory 없이 RL만으로 self-reflection, verification, strategy adaptation을 유도
- reasoning capability를 RL의 emergent behavior로 해석하는 관점 제시
- 이후 RLVR 류 post-training 붐의 기준점 역할

## 결과와 시사점

- 수학, 코딩, STEM 과제에서 기존 supervised demonstration 기반 접근을 상회
- 큰 모델에서 나타난 reasoning 패턴을 작은 모델로 이전하는 가능성 제시

## 한계

RL 보상 설계와 검증 가능 과제에 강하게 의존하기 때문에, open-ended domain이나 calibration 문제는 별도 보강이 필요하다.

## 실무 적용 관점

현대 reasoning model 학습은 CoT annotation을 더 많이 모으는 문제를 넘어, **검증 가능한 보상 구조를 어떻게 만들 것인가**의 문제로 이동했음을 보여준다.

## 관련 문서

- [[rlvr]]
- [[grpo]]
- [[agentic-rl]]
