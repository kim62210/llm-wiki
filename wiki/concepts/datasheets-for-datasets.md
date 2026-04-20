---
title: Datasheets for Datasets (데이터셋 데이터시트)
category: concepts
page_type: concept
tags: [governance, datasheets, dataset-documentation, transparency, data-provenance, Gebru, responsible-ai]
sources: [raw/2026-04-14-ml-foundations-gap.md]
created: 2026-04-14
updated: 2026-04-14
---

## 개요

Datasheets for Datasets는 Timnit Gebru et al.이 2018년에 제안한 데이터셋 문서화 프레임워크다. 전자 부품의 데이터시트에서 영감을 받아, ML 학습에 사용되는 모든 데이터셋에 표준화된 문서를 동반할 것을 권장한다. 데이터셋 생성자와 소비자 사이의 커뮤니케이션을 개선하고, ML 커뮤니티의 투명성과 책임성을 높이는 것이 목표다.

데이터셋과 배포 맥락의 불일치(mismatch)는 형사 사법, 채용, 금융 등 고위험 영역에서 특히 심각한 결과를 초래할 수 있다. Datasheets는 이런 불일치를 사전에 드러내는 역할을 한다.

## 프레임워크 구성

Gebru et al.은 데이터셋 문서화를 위한 안내 질문(guiding questions)을 7개 섹션으로 구조화했다.

**동기(Motivation)**: 데이터셋이 왜 만들어졌는가? 누가 만들었고, 누가 자금을 지원했는가? 어떤 특정 과제를 염두에 두었는가? 이 섹션은 데이터셋의 의도를 명확히 하여, 원래 목적과 다른 맥락에서의 오용을 방지한다.

**구성(Composition)**: 데이터셋의 인스턴스는 무엇을 나타내는가(문서, 사진, 사람, 국가 등)? 총 인스턴스 수는? 라벨이나 대상 변수가 있는가? 누락된 데이터가 있는가? 데이터에 기밀 정보가 포함되어 있는가?

**수집 과정(Collection Process)**: 데이터가 어떻게 수집되었는가? 누가 수집에 참여했고, 보상을 받았는가? 윤리 심사(IRB 등)를 거쳤는가? 크라우드소싱의 경우 작업자 모집 및 보상 방식은?

**전처리/정제/라벨링(Preprocessing)**: 원시 데이터에 어떤 전처리가 적용되었는가? 원시 데이터도 제공되는가? 라벨링 과정과 품질 보증 방법은?

**용도(Uses)**: 데이터셋이 이미 사용된 과제가 있는가? 향후 사용에 영향을 미칠 수 있는 구성적 한계는? 적합하지 않은 용도는?

**배포(Distribution)**: 데이터셋이 어떻게 배포되는가? 라이선스는? 접근 제한이 있는가?

**유지보수(Maintenance)**: 누가 데이터셋을 유지 관리하는가? 업데이트 계획은? 오류 발견 시 대응 절차는?

## LLM 학습 데이터에 대한 적용

LLM 시대에 Datasheets의 중요성은 더욱 커졌다. 수조 토큰 규모의 사전학습 데이터에 대한 투명성 요구가 증가하고 있지만, 실무적으로는 여러 도전 과제가 있다.

**규모의 문제**: Common Crawl, C4, The Pile 등 웹 크롤 데이터셋은 수십억 개의 문서를 포함한다. 개별 인스턴스 수준의 문서화는 비현실적이므로, 통계적 프로필(언어 분포, 도메인 분포, 독성 비율 등)로 대체하는 경우가 많다.

**저작권과 라이선스**: 웹에서 크롤링한 데이터의 저작권 상태를 개별적으로 확인하는 것은 거의 불가능하다. [[ai-supply-chain-security|AI 공급망 보안]] 관점에서 데이터 출처 추적(provenance)의 중요성이 부각되고 있다.

**합성 데이터**: 2025-2026년 합성 데이터 활용이 급증하면서, 합성 데이터의 생성 모델, 프롬프트, 필터링 기준 등을 문서화하는 새로운 요구가 등장했다.

## [[model-cards]]와의 관계

[[model-cards|Model Cards]]가 모델을 문서화한다면, Datasheets는 데이터를 문서화한다. 완전한 AI 투명성을 위해서는 두 문서가 상호 참조되어야 한다. 모델의 Model Card는 학습 데이터의 Datasheet를 가리키고, Datasheet는 해당 데이터로 학습된 모델의 Model Card를 역참조한다.

## 규제 환경에서의 역할

EU AI Act는 고위험 AI 시스템에 대해 학습 데이터의 문서화를 의무화한다. Datasheets 프레임워크는 이 요구사항을 충족하는 실질적 도구로 주목받고 있다. [[nist-ai-rmf|NIST AI RMF]]의 Map 기능에서도 데이터 관련 위험을 파악하기 위해 Datasheets 수준의 문서화를 권장한다.

[[iso-42001|ISO/IEC 42001]]의 데이터 거버넌스 및 품질 요구사항은 Datasheets의 수집 과정, 전처리, 유지보수 섹션과 직접적으로 대응된다.

## 채택 사례

**Hugging Face**: Dataset Cards라는 이름으로 Hub의 모든 데이터셋에 문서화를 요구한다. Datasheets 프레임워크를 기반으로 하되, 플랫폼에 맞게 간소화한 형식이다.

**Microsoft**: 연구 조직 차원에서 Datasheets 작성을 장려하며, 내부 데이터셋에 대한 문서화 템플릿을 제공한다. 공저자인 Hanna Wallach가 Microsoft Research 소속이기도 하다.

**Google**: Know Your Data 도구를 통해 데이터셋의 구성과 잠재적 편향을 시각적으로 탐색할 수 있는 기능을 제공한다.

## 한계

Datasheets 작성에는 상당한 노력이 필요하며, 특히 대규모 웹 크롤 데이터셋에 대해서는 완전한 Datasheet 작성이 현실적으로 어렵다. 또한 데이터셋이 시간이 지남에 따라 변화(drift)하는 경우, Datasheet의 업데이트가 따라가지 못하는 문제가 있다. 그럼에도 불구하고 Datasheets는 데이터 투명성의 기준점으로서 가치를 유지하고 있으며, [[fairness-metrics-bias-auditing|편향 감사]]의 출발점이 되는 경우가 많다.

## 관련 문서

- [[model-cards]] -- 모델 문서화 표준
- [[fairness-metrics-bias-auditing]] -- 공정성 정량 측정과 편향 감사
- [[responsible-ai-practices]] -- 윤리적 AI 개발 원칙
- [[ai-supply-chain-security]] -- 모델/데이터셋 공급망 보안
- [[nist-ai-rmf]] -- AI 위험 관리 프레임워크
- [[iso-42001]] -- AI 관리체계 인증 표준
