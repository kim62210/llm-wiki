---
title: Constitutional Classifiers++ (Jailbreak Defense)
category: concepts
page_type: concept
tags: [concepts, concept, constitutional, classifiers]
sources: [raw/2026-04-10-hot-ai-topics-100.md, raw/hot-topics-sources/2026-04-10/topics/constitutional-classifiers.md, raw/hot-topics-sources/2026-04-10/373-next-generation-constitutional-classifiers.md, raw/hot-topics-sources/2026-04-10/374-constitutional-classifiers-defending-against-universal-jailbreaks.md, raw/hot-topics-sources/2026-04-10/375-constitutional-classifiers-efficient-production-grade-defenses.md, raw/hot-topics-sources/2026-04-10/376-constitutional-classifiers.md, raw/hot-topics-sources/2026-04-10/377-cost-effective-constitutional-classifiers-via-representation-re-use.md]
created: 2026-04-10
updated: 2026-04-10
---
# Constitutional Classifiers++ (Jailbreak Defense)

헌법 규칙 기반 합성 데이터로 학습한 입출력 분류기로 범용 jailbreak 차단.

## 왜 중요한가

2026년 1월 Anthropic이 공개한 차세대 버전이 1,700시간 레드팀에서 universal jailbreak 완전 차단에 성공하며 컴퓨트 비용을 40배 줄였고, 프로덕션 배포 가능한 jailbreak 방어의 업계 표준으로 부상했다.

## 대표 레퍼런스

- [Next-generation Constitutional Classifiers (Anthropic)](https://www.anthropic.com/research/next-generation-constitutional-classifiers)
- [Constitutional Classifiers: Defending against universal jailbreaks](https://www.anthropic.com/research/constitutional-classifiers)
- [Constitutional Classifiers++: Efficient Production-Grade Defenses (arXiv 2601.04603)](https://arxiv.org/abs/2601.04603)
- [Constitutional Classifiers (arXiv 2501.18837)](https://arxiv.org/pdf/2501.18837)
- [Cost-Effective Constitutional Classifiers via Representation Re-use](https://alignment.anthropic.com/2025/cheap-monitors/)

## 2026년 4월 큐레이션 요약

- 정의: 헌법 규칙 기반 합성 데이터로 학습한 입출력 분류기로 범용 jailbreak 차단.
- 왜 중요한가: 2026년 1월 Anthropic이 공개한 차세대 버전이 1,700시간 레드팀에서 universal jailbreak 완전 차단에 성공하며 컴퓨트 비용을 40배 줄였고, 프로덕션 배포 가능한 jailbreak 방어의 업계 표준으로 부상했다.
- 직접 수집 원문: 5개
- 주요 도메인: anthropic.com×2, arxiv.org×2, alignment.anthropic.com×1

## source 기반 참고

- topic packet: `raw/hot-topics-sources/2026-04-10/topics/constitutional-classifiers.md`

### source별 핵심 신호

- **Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks \ Anthropic** (`anthropic.com`): https://www.anthropic.com/research/next-generation-constitutional-classifiers
  - 메모: Large language models remain vulnerable to jailbreaks—techniques that can circumvent safety guardrails and elicit harmful information.
- **Constitutional Classifiers: Defending against universal jailbreaks \ Anthropic** (`anthropic.com`): https://www.anthropic.com/research/constitutional-classifiers
  - 메모: Large language models have extensive safety training to prevent harmful outputs. For example, we train Claude to refuse to respond to user queries involving the production of biological or chemical weapons.
- **[2601.04603] Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks** (`arxiv.org`): https://arxiv.org/abs/2601.04603
  - 메모: We introduce enhanced Constitutional Classifiers that deliver production-grade jailbreak robustness with dramatically reduced computational costs and refusal rates compared to previous-generation defenses.
- **Constitutional Classifiers (arXiv 2501.18837)** (`arxiv.org`): https://arxiv.org/pdf/2501.18837
  - 메모: << /Type /XObject /Subtype /Form /BBox [ 0 0 100 100 ]
- **Cost-Effective Constitutional Classifiers via Representation Re-use** (`alignment.anthropic.com`): https://alignment.anthropic.com/2025/cheap-monitors/
  - 메모: We study cost-effective jailbreak detection.

## 관련 문서

- [[ai-hot-topics-2026-04|2026년 4월 AI 개발 핫토픽 100선]]
- [[alignment-faking|Alignment Faking in LLMs]]
- [[agent-prompt-injection-defense|Agent Prompt Injection Defense & Trustworthy Agents]]
- [[context-engineering|Context Engineering]]
