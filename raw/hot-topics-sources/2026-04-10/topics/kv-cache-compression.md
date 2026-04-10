---
title: Chunk-Semantic KV Cache Compression
section: Inference Optimization
sources: [raw/2026-04-10-hot-ai-topics-100.md]
created: 2026-04-10
updated: 2026-04-10
---

# Chunk-Semantic KV Cache Compression

## 기존 큐레이션 요약

- 정의: 토큰 단위가 아닌 의미 청크 단위로 KV 엔트리를 선택·압축하는 기법.
- 왜 중요한가: 2026년 초 FastKV(v6, 2026.02), StructKV, KVSculpt, EchoKV 등 청크/구조 기반 논문이 대거 등장해 128K 이상 컨텍스트에서 정확도 유지 채 처리량을 최대 26.5% 끌어올렸다.

## 개별 원문 수집 스냅샷

### ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference

- URL: https://arxiv.org/abs/2502.00299
- raw snapshot: `raw/hot-topics-sources/2026-04-10/105-chunkkv-semantic-preserving-kv-cache-compression-for-efficient-long-context-llm-.md`
- 수집 제목: [2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference

[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2502.00299 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2502.00299 (cs) [Submitted on 1 Feb 2025 (v1), last revised 14 Oct 2025 (this version, v5)] Title:ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference Authors:Xiang Liu, Z

### FastKV: KV Cache Compression for Fast Long-Context Inference

- URL: https://arxiv.org/abs/2502.01068
- raw snapshot: `raw/hot-topics-sources/2026-04-10/106-fastkv-kv-cache-compression-for-fast-long-context-inference.md`
- 수집 제목: [2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration

[2502.01068] FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2502.01068 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2502.01068 (cs) [Submitted on 3 Feb 2025 (v1), last revised 16 Feb 2026 (this version, v6)] Title:FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration Authors:Dong

### StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference

- URL: https://arxiv.org/abs/2604.06746
- raw snapshot: `raw/hot-topics-sources/2026-04-10/107-structkv-preserving-the-structural-skeleton-for-scalable-long-context-inference.md`
- 수집 제목: [2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference

[2604.06746] StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2604.06746 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Computation and Language arXiv:2604.06746 (cs) [Submitted on 8 Apr 2026] Title:StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference Authors:Zhirui Chen, Peiyang Liu, Ling Shao View a PDF of the paper titled StructKV: Prese

### KVSculpt: KV Cache Compression as Distillation

- URL: https://arxiv.org/abs/2603.27819
- raw snapshot: `raw/hot-topics-sources/2026-04-10/108-kvsculpt-kv-cache-compression-as-distillation.md`
- 수집 제목: [2603.27819] KVSculpt: KV Cache Compression as Distillation

[2603.27819] KVSculpt: KV Cache Compression as Distillation Skip to main content Learn about arXiv becoming an independent nonprofit. We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.Donate >cs> arXiv:2603.27819 Help | Advanced Search All fieldsTitleAuthorAbstractCommentsJournal referenceACM classificationMSC classificationReport numberarXiv identifierDOIORCIDarXiv author IDHelp pagesFull text Search GO quick links Login Help Pages About Computer Science > Machine Learning arXiv:2603.27819 (cs) [Submitted on 29 Mar 2026] Title:KVSculpt: KV Cache Compression as Distillation Authors:Bo Jiang, Sian Jin View a PDF of the paper titled KVSculpt: KV Cache Compression as Distillation, by Bo Jiang and 1 other authors View PDFHTML (experimental)

### RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression

- URL: https://arxiv.org/html/2502.14051v3
- raw snapshot: `raw/hot-topics-sources/2026-04-10/109-rocketkv-accelerating-long-context-llm-inference-via-two-stage-kv-cache-compress.md`
- 수집 제목: RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression

RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression 1 Introduction 2 Related Work 3 Proposed Method: RocketKV 3.1 Observation 3.2 RocketKV Overview 3.3 First Stage: SnapKV 3.4 Second Stage: Hybrid Sparse Attention 3.5 RocketKV-MT 3.6 Adaptive Compression Decomposition 3.7 System Implications 4 Experiments 4.1 Experimental Settings 4.2 Accuracy Results 4.3 Efficiency Results 5 Conclusion A Detailed Experiment Settings A.1 Models A.2 Benchmarks A.3 Baselines B Additional Results B.1 Ablation Studies B.1.1 Comparing HSA, Quest, and SparQ B.1.2 Split Factor B.2 Needle-in-a-Haystack Visualization B.3 Detailed Accuracy Results RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression Payman Behnam Yaosheng Fu Ritchie Zhao Po-An Tsai Zhi
