---
title: ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference
category: papers
page_type: paper
tags: [paper, inference, kv-cache, compression]
sources: [raw/hot-topics-sources/2026-04-10/105-chunkkv-semantic-preserving-kv-cache-compression-for-efficient-long-context-llm-.md]
created: 2026-04-10
updated: 2026-04-10
---

# ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference

토큰 단위 중요도 대신 의미 청크를 보존 단위로 삼아 KV cache를 압축하는 기법을 제안한 논문이다.

## 핵심 기여

- semantic chunk를 압축 기본 단위로 삼아 의미 구조 보존
- layer-wise index reuse로 추가 계산 오버헤드 감소
- LongBench, GSM8K, jailbreak 평가까지 포함해 장기 문맥·일반성·안전성 측면 비교

## 결과와 시사점

- 동일 압축률에서 기존 기법 대비 최대 8.7% precision 향상
- throughput 26.5% 개선 보고

## 한계

청크 경계 품질에 따라 성능이 흔들릴 수 있고, 모델/토크나이저별 chunk semantics 차이를 어떻게 일반화할지는 추가 과제다.

## 실무 적용 관점

long-context inference에서는 단순 token importance보다 **의미 단위 보존**이 더 실용적인 압축 축이 될 수 있음을 보여준다.

## 관련 문서

- [[kv-cache-compression]]
- [[context-rot]]
- [[lmcache]]
