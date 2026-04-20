---
source: arxiv
arxiv_id: "2601.03868"
title: "What Matters For Safety Alignment?"
authors: ["Xing Li", "Hui-Ling Zhen", "Lihao Yin", "Xianzhi Yu", "Zhenhua Dong", "Mingxuan Yuan"]
date: 2026-01-07
url: "https://arxiv.org/abs/2601.03868"
fetched: 2026-04-15
status: pending_ingest
---

## Abstract

32개 최신 오픈소스 모델(13 패밀리, 3B~235B)을 5개 안전 데이터셋과 56개 탈옥 기법으로 평가한 대규모 실증 연구. 총 460만 API 호출.

## Key Points

- GPT-OSS-20B, Qwen3-Next-80B, GPT-OSS-120B가 가장 안전한 3개 모델
- 포스트 트레이닝과 지식 증류가 안전 정렬을 체계적으로 약화시킬 수 있음
- CoT 공격 + 응답 접두사 조합으로 공격 성공률 평균 3.34배 상승
- 주요 공격 방법: roleplay, prompt injection, gradient-based search
- 안전은 명시적 최적화 목표여야 하며 부차적 목표로는 불충분
