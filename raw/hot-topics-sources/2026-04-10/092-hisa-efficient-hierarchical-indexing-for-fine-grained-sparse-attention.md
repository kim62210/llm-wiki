---
title: HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention
source_url: https://arxiv.org/html/2603.28458
final_url: https://arxiv.org/html/2603.28458
status: 200
content_type: text/html; charset=utf-8
topics: [DeepSeek Sparse Attention (DSA) for Long Context]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:37.814983+00:00
---

# HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention

## 원본 URL

https://arxiv.org/html/2603.28458

## 추출 본문

HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse AttentionReport GitHub Issue×
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHubSubmit in GitHub
Back to arXiv
Why HTML?Report IssueBack to AbstractDownload PDF
Abstract

1 Introduction

2 Related Work
Block sparse attention.

Token sparse attention.

Hierarchical sparse attention.

3 Preliminary
Indexer in DSA.

Sparse MLA in DSA.

4 Method
4.1 HISA: Hierarchical Indexed Sparse Attention
Block partitioning and pooled keys.

Stage 1: Block-level coarse filtering.

Stage 2: Token-level refinement.

Boundary behavior.

4.2 Complexity Analysis

5 Experiments
5.1 Kernel-Level Speedup

5.2 Needle-in-a-Haystack

5.3 LongBench Evaluation

5.4 Visualization of Attention Scores

5.5 Hyperparameter Sensitivity

6 Conclusion and Future Directions

References

A Algorithm Pseudocode

B Experimental Settings
B.1 Long-context Benchmarks
NIAH Settings

LongBench Settings

Fairness of Comparison

 License: CC BY 4.0
 

arXiv:2603.28458v3 [cs.LG] 06 Apr 2026

HISA: Efficient Hierarchical Indexing 

for Fine-Grained Sparse Attention

Yufei Xu, Fanxu Meng11footnotemark: 1, Fan Jiang, Yuxuan Wang, Ruijie Zhou, Zhaohui Wang,

Jiexi Wu, Zhixin Pan, Xiaojuan Tang, Wenjie Pei, Tongxuan Liu, Di Yin,
Xing Sun, Muhan Zhang

https://github.com/MuLabPKU/TransArchEqual contribution.Corresponding author: muhan@pku.edu.cn

Abstract
Token-level sparse attention mechanisms, exemplified by DeepSeek Sparse Attention (DSA), achieve fine-grained key selection by scoring every historical key for each query through a lightweight indexer, then computing attention only on the selected subset.
While the downstream sparse attention itself scales favorably, the indexer must still scan the entire prefix for every query, introducing an 𝒪​(L2)\mathcal{O}(L^{2}) per-layer bottleneck that grows prohibitively with context length.
We propose HISA (Hierarchical Indexed Sparse Attention), a plug-and-play replacement for the indexer that rewrites the search path from a flat token scan into a two-stage hierarchical procedure: (1) a block-level coarse filtering stage that scores pooled block representations to discard irrelevant regions, followed by (2) a token-level refinement stage that applies the original indexer exclusively within the retained candidate blocks.
HISA preserves the identical token-level top-kk sparse pattern consumed by the downstream Sparse MLA operator and requires no additional training.
On kernel-level benchmarks, HISA achieves up to 3.75×3.75\times speedup at 64K context.
On Needle-in-a-Haystack and LongBench, we directly replace the indexer in DeepSeek-V3.2 and GLM-5 with our HISA indexer, without any finetuning.
HISA closely matches the original DSA in quality, while substantially outperforming block-sparse baselines.

1 Introduction

Serving large language models (LLMs) (OpenAI, 2026; Anthropic, 2026; Google DeepMind, 2025; Meta, 2025; Qwen, 2026; DeepSeek-AI, 2024; MiniMax et al., 2025; Moonshot AI, 2025) over long contexts remains a central systems challenge. As context windows grow from 128K to 1M tokens and beyond—driven by demands for agentic multi-turn reasoning, long-document understanding, and native multimodal processing—the quadratic cost of self-attention becomes a dominant bottleneck in both prefill latency and memory consumption (Dao et al., 2022; Dao, 2023).

A productive line of work tackles this challenge through sparse attention: instead of attending to all key–value pairs, each query selects a small subset of the most relevant tokens and computes attention only over that subset. DeepSeek-V3.2 (DeepSeek-AI, 2025) adopts a token-level sparse attention paradigm, in which a lightweight indexer scores every historical token for each query, selects the top-kk highest-scoring keys, and forwards only those keys to a downstream Sparse Multi-Head Latent Attention (Sparse MLA). This design has also been adopted in GLM-5 (GLM-5-Team, 2026) and provides strictly finer-grained selection than block-level methods such as MoBA (Lu et al., 2025) and Native Sparse Attention (Yuan et al., 2025).

However, the token-level sparse paradigm introduces a subtler bottleneck. Although the downstream attention is sparse and cheap, the indexer itself must score every token in the prefix for every query. Concretely, if the prefix length is LL and the indexer runs once per query per layer, the per-layer indexing cost is 𝒪​(L2)\mathcal{O}(L^{2})—the same asymptotic scaling as dense attention. As context lengths push toward 128K or 1M tokens, the indexer can transition from a negligible overhead into the dominant cost component.

This observation motivates a natural question: can we reduce the indexer’s search cost without changing the final sparse attention pattern it produces? In other words, can we rewrite the search path while preserving the search result?

We answer affirmatively with HISA (Hierarchical Indexed Sparse Attention). HISA replaces the flat, full-prefix token scan with a two-stage hierarchical search (shown in Figure 1):

1.

Block-level coarse filtering. The prefix is partitioned into contiguous blocks of size BB. A pooled representative vector is computed for each block via mean pooling over its constituent indexing keys. The query scores all ⌈L/B⌉\lceil L/B\rceil block representatives and retains only the top-mm blocks, immediately pruning the majority of the prefix from further consideration.

2.

Token-level refinement.
The token-level indexer then scores at most m​BmB tokens from the candidate blocks using the same scoring mechanism as the original DSA indexer, except that the candidate pool is restricted to the tokens within the selected blocks rather than the full set of LL tokens considered in DSA. The final top-kk token set is then selected from this reduced candidate pool.

Crucially, HISA produces outputs with the same structure as the original DSA indexer: for each query, a set of kk token indices. As a result, the downstream Sparse MLA operator remains entirely unchanged.
HISA is therefore a drop-in replacement that requires no retraining, no architectural changes to the attention mechanism, and no modification to the KV cache layout.
The per-query indexing complexity drops from 𝒪​(L)\mathcal{O}(L) to 𝒪​(L/B+m​B)\mathcal{O}(L/B+mB), and the per-layer cost drops from 𝒪​(L2)\mathcal{O}(L^{2}) to 𝒪​(L2/B+L​m​B)\mathcal{O}(L^{2}/B+LmB).

Our contributions are as follows:

•

We identify the indexer as an emerging bottleneck in token-level sparse attention systems and formalize the problem of search-path optimization for sparse indexers.

•

We propose HISA, a hierarchical block-to-token indexing strategy that is training-free, operator-compatible, and asymptotically faster than the flat indexer.

•

We provide optimized TileLang GPU kernel implementations for both stages of HISA and demonstrate 22–4×4\times kernel-level speedup at 64K contexts.

•

We empirically validate that HISA achieves performance comparable to the original DSA on the Needle-in-a-Haystack and LongBench benchmarks.

(a) Original DSA: token-wise indexer.

(b) Our HISA: block-to-token indexer.

Figure 1: Comparison of the DSA token-wise indexer (left) and our HISA hierarchical block-level coarse filter followed by token-level refinement (right). Both produce the same data structure—a per-query set of kk token indices—consumed by the downstream Sparse MLA operator.

2 Related Work

Block sparse attention.

Block sparse attention partitions sequences into fixed-size blocks and restricts computation to selected blocks, mapping naturally to GPU tiled matrix multiplications. This design is hardware-friendly, but all tokens within a block must be retained or discarded together.
Among training-free methods, MInference (Huiqiang et al., 2024) profiles each head offline and assigns one of several sparse patterns at inference time; FlexPrefill (Lai et al., 2025) estimates block scores online and selects blocks by a cumulative-attention threshold; XAttention (Xu et al., 2025) uses antidiagonal sums as an 𝒪​(B)\mathcal{O}(B) proxy for block importance; and SpargeAttention (Zhang et al., 2025) applies a two-stage online filter to skip low-importance regions during matrix multiplication and softmax.
Among trainable methods, MoBA (Lu et al., 2025) uses mixture-of-experts-style routing over blocks, while NSA (Yuan et al., 2025) combines compression, selection, and sliding-window branches to cover different dependency scales.
Their common limitation is block granularity: they cannot capture token-level importance differences within a selected block. HISA also introduces a block-level stage, but only as a fast pre-filter before token refinement; its final sparse pattern remains fine-grained and token-wise, as in DSA.

Token sparse attention.

Token-level methods offer finer selection but face the challenge of efficient importance estimation.
SnapKV (Yuhong et al., 2024) uses an observation window at the end of the prompt to select important KV positions for subsequent decoding, but ignores layer- and query-specific variation.
KV cache eviction methods—such as H2O (Zhang et al., 2024), which combines cumulative attention with recency, and TOVA (Oren et al., 2024), which evicts the lowest-scoring cached token under the latest query—maintain a fixed-size cache but irrecoverably lose evicted tokens.
LazyLLM (Fu et al., 2024) progressively prunes tokens across layers during prefill, so early pruning mistakes cannot be corrected later in the same forward pass.
DSA (DeepSeek-AI, 2025) instead scores every prefix token with a lightweight indexer and selects top-kk tokens per query, achieving fine-grained sparsity at the cost of 𝒪​(L2)\mathcal{O}(L^{2}) per-layer indexing overhead. IndexCache (Bai et al., 2026) reduces this cost by reusing indices across nearby layers, although its benefit depends on cross-layer similarity in sparse patterns.

Hierarchical sparse attention.

Hierarchical attention dates back to Yang et al. (2016), who introduced a two-tier word-and-sentence network for document classification.
Among recent sparse methods, NSA (Yuan et al., 2025) and InfLLM-V2 (Zhao et al., 2026) can both be viewed as two-level designs: they score block-level summaries globally and activate finer-grained sparse attention only within selected blocks.
Twilight (Lin et al., 2025) uses quantized keys for coarse scoring and then applies hierarchical top-pp pruning, while Double-P (Ni et al., 2026) clusters the KV cache, scores cluster centroids, refines computation within selected clusters, and approximates low-score clusters with their centroids.
HISA follows the same coarse-to-fine spirit but with a different goal: it combines a hardware-friendly block-level indexer with a fine-grained token-level indexer to accelerate DSA, achieving both high efficiency and strong selection quality on DeepSeek-V3.2 and GLM-5.

3 Preliminary

We briefly review DeepSeek Sparse Attention (DSA) as used in DeepSeek-V3.2 (DeepSeek-AI, 2025). DSA consists of two components: a token-wise Indexer and Sparse MLA.

Indexer in DSA.

Let LL denote the causal prefix length for a query position tt. The indexer maintains lightweight indexing keys 𝐤sI\mathbf{k}_{s}^{I}, indexing queries 𝐪t,jI\mathbf{q}_{t,j}^{I} for HIH^{I} indexing heads, and per-head gating weights wt,jIw_{t,j}^{I}. The relevance score between query tt and key ss is defined as
It,s=∑j=1HIwt,jI⋅ReLU​(𝐪t,jI⋅𝐤sI).I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{ReLU}\!\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right).(1)
The indexer then selects the top-kk token indices,
𝒯t=TopK​(It,:,k),\mathcal{T}_{t}=\mathrm{TopK}(I_{t,:},\,k),(2)
which are passed to the downstream Sparse MLA operator. Since the scoring cost for each query is 𝒪​(L)\mathcal{O}(L) over the full prefix, the total cost across all queries in a layer is 𝒪​(L2)\mathcal{O}(L^{2}).

Sparse MLA in DSA.

Following the DeepSeek-V3.2 design, Sparse MLA adopts the MQA mode of MLA, in which each token stores a single latent key–value entry shared across all query heads for efficiency. Let 𝐜s\mathbf{c}_{s} denote the latent MLA entry associated with token ss. Given the selected token set 𝒯t\mathcal{T}_{t}, Sparse MLA computes attention for query token tt only over the selected latent entries, rather than over the full prefix:
𝐮t=Attn​(𝐡t,{𝐜s∣s∈𝒯t}).\mathbf{u}_{t}=\mathrm{Attn}\!\left(\mathbf{h}_{t},\,\left\{\mathbf{c}_{s}\mid s\in\mathcal{T}_{t}\right\}\right).(3)
As a result, the main attention cost is reduced from dense 𝒪​(L2)\mathcal{O}(L^{2}) to sparse 𝒪​(L​k)\mathcal{O}(Lk). For our purposes, the key observation is that the interface between the two components is precisely the selected token set 𝒯t\mathcal{T}_{t}: HISA replaces only the indexer search path, while leaving the downstream Sparse MLA operator unchanged.

4 Method

4.1 HISA: Hierarchical Indexed Sparse Attention

As shown in Figure 1, HISA replaces the flat prefix scan with a two-stage coarse-to-fine search. The final output remains an identical per-query token set 𝒯tH\mathcal{T}_{t}^{\mathrm{H}} of size kk, consumed by the original Sparse MLA operator.

Block partitioning and pooled keys.

The prefix tokens of length LL is partitioned into M=⌈L/B⌉M=\lceil L/B\rceil contiguous, causally valid blocks ℬ1,ℬ2,…,ℬM\mathcal{B}_{1},\mathcal{B}_{2},\ldots,\mathcal{B}_{M}, where BB is the block size. For each block, a representative key is constructed via mean pooling over its indexing keys:
𝐤~bI=Pool​({𝐤sI∣s∈ℬb}).\tilde{\mathbf{k}}_{b}^{I}=\mathrm{Pool}\!\left(\left\{\mathbf{k}_{s}^{I}\mid s\in\mathcal{B}_{b}\right\}\right).(4)

These representative keys serve exclusively as coarse-grained proxies for block-level scoring and leave both the token-level indexing keys consumed by the second stage and the KV states consumed by Sparse MLA unchanged, thereby making HISA a plug-and-play replacement. In practice, these representative keys can be incrementally maintained alongside the KV cache with negligible overhead.

Stage 1: Block-level coarse filtering.

For query position tt, HISA reuses the same indexing query representations 𝐪t,jI\mathbf{q}_{t,j}^{I} and gating weights wt,jIw_{t,j}^{I} as DSA, but scores the pooled representative keys instead of individual token keys:
Jt,b=∑j=1HIwt,jI⋅ReLU​(𝐪t,jI⋅𝐤~bI).J_{t,b}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{ReLU}\!\left(\mathbf{q}_{t,j}^{I}\cdot\tilde{\mathbf{k}}_{b}^{I}\right).(5)
The top-mm blocks are selected:
𝒞t=TopK​(Jt,:,m),\mathcal{C}_{t}=\mathrm{TopK}(J_{t,:},\,m),(6)
and the candidate token set is the union of all tokens in the selected blocks:
Ωt=⋃b∈𝒞tℬb.\Omega_{t}=\bigcup_{b\in\mathcal{C}_{t}}\mathcal{B}_{b}.(7)
All block selections strictly respect the causal mask: only blocks that precede the query position tt, together with the block containing position tt, are considered eligible. Following MoBA (Lu et al., 2025), the first and the last blocks are always included in 𝒞t\mathcal{C}_{t}, as they contain the attention sink and local contexts. This forced inclusion also simplifies boundary handling during batched prefill with packed sequences of varying lengths, where a single block may straddle the boundary between two sequences.

Stage 2: Token-level refinement.

Within the selected candidate set Ωt\Omega_{t}, the token-level indexer computes scores using the same scoring mechanism as in the original DSA (Eq. 1):
It,s=∑j=1HIwt,jI⋅ReLU​(𝐪t,jI⋅𝐤sI),s∈Ωt.I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{ReLU}\!\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right),\quad s\in\Omega_{t}.(8)
Then the top-kk tokens are selected as final tokens:
𝒯t=TopK​({It,s∣s∈Ωt},k).\mathcal{T}_{t}=\mathrm{TopK}\!\left(\left\{I_{t,s}\mid s\in\Omega_{t}\right\},\,k\right).(9)

To ensure that the candidate pool is sufficiently large to select kk tokens, the feasibility constraint m​B≥kmB\geq k must be satisfied. Given the selected token set 𝒯t\mathcal{T}_{t}, sparse MLA is executed following the same computation as in the original DSA.
Algorithm 1 provides the complete pseudocode for the HISA indexer.

Boundary behavior.

Three regimes arise depending on the relationship between the effective prefix length tt, the candidate capacity m​BmB, and the budget kk:

•

When t≤kt\leq k, all prefix tokens are selected and HISA is equivalent to dense attention.

•

When k<t≤m​Bk<t\leq mB, the coarse filter selects all blocks (since m≥Mm\geq M), and Stage 2 reduces the set to kk tokens. HISA is equivalent to the original DSA indexer.

•

When t>m​Bt>mB, the coarse filter performs non-trivial block pruning, activating HISA’s hierarchical advantage, which becomes increasingly pronounced as the sequence length grows.

The third regime is precisely the long-context setting where HISA provides its efficiency gains.

(a) Budget = 8192

(b) Compression Ratio = 4:1

Figure 2: Latency comparison of the indexer kernel between the original DSA (flat token scan) and HISA (hierarchical block-to-token indexing). In the left panel, the block size is fixed to B=128B=128 and the maximum number of selected blocks is set to top-m=64m=64. In the right panel, the block size is also fixed to B=128B=128, while the number of selected blocks is adjusted for each sequence length to maintain a fixed compression ratio of M:m=4:1M\!:\!m=4\!:\!1.

4.2 Complexity Analysis

Assuming that the pooled representative keys are maintained incrementally, the per-query indexing cost of HISA consists of scoring ⌈L/B⌉\lceil L/B\rceil block representatives (Stage 1) and scoring at most m​BmB candidate tokens (Stage 2):
𝒪​(LB+m​B).\mathcal{O}\!\left(\frac{L}{B}+mB\right).(10)
Summing over all LL queries within a layer yields:
𝒪​(L2B+L​m​B),\mathcal{O}\!\left(\frac{L^{2}}{B}+LmB\right),(11)
compared to 𝒪​(L2)\mathcal{O}(L^{2}) for the original DSA indexer. The design introduces a clear trade-off: larger BB reduces the cost of coarse-filtering stage but makes each block a coarser proxy; smaller mm improves efficiency but increases the risk of missing relevant blocks. When m≪Mm\ll M and B≪LB\ll L—the regime of ultra-long contexts with a selective coarse filter—the reduction is substantial. Conversely, as mm approaches MM, HISA degrades gracefully toward the DSA baseline.

As modern LLMs increasingly adopt context windows of 128K or even 1M tokens to support advanced agent capabilities and native multimodal reasoning, HISA’s asymptotic advantage translates directly into practical speedups.

5 Experiments

We evaluate HISA along five axes: (1) kernel-level latency, (2) retrieval accuracy on Needle-in-a-Haystack, (3) downstream task performance on LongBench, (4) visualization of attention scores, and (5) hyperparamenter sensitivity. Throughout the evaluation, we compare three indexing strategies:

•

DSA (original): the full-prefix token-level indexer as described in Section 3.

•

Block-Sparse: a block-level-only baseline that selects top-mm blocks and attends to all tokens within those blocks (i.e., Stage 1 only, without token-level refinement).

•

HISA: the hierarchical block-to-token indexer proposed in this work.

Both HISA and Block-Sparse are training-free: they are applied at inference time by replacing the indexer module, with no fine-tuning or architectural modification.

(a) DSA (original)

(b) Block-Sparse

(c) HISA (ours)

Figure 3: Needle-in-a-Haystack retrieval accuracy heatmaps for DeepSeek-V3.2 under three indexing strategies. The xx-axis denotes the context length (8K–128K), and the yy-axis denotes the needle depth (0%–100%). Shades closer to green indicate higher retrieval accuracy.

5.1 Kernel-Level Speedup

Figure 2 compares the indexer kernel latency of the original DSA and HISA across context lengths from 8K to 64K tokens. Both implementations use TileLang (Wang et al., 2025) kernels, with DSA following the official reference implementation.111https://github.com/tile-ai/tilelang/tree/main/examples/deepseek_v32
The HISA kernel is decomposed into two stages: block-level filtering and token-level refinement within the selected candidate blocks. The configuration is as follows: query lens =1024=1024, final top-k=2048k=2048 tokens, block size B=128B=128, and two choices for the maximum number of selected blocks. All comparisons are conducted on an NVIDIA A100 GPU. These results are measured at the indexer kernel level and do not directly reflect end-to-end serving throughput, which also depends on the sparse MLA operator, KV cache management, and other system components.

With 2048 selected tokens, the sparse MLA operator consistently costs about 1.6 ms, while the indexer reaches 5.6 ms at 64K context length. This suggests that the main performance bottleneck in DSA lies in the indexer rather than in sparse MLA itself. Accordingly, we restrict the comparison to indexer overhead.
At 64K context length, HISA delivers an approximately 2.16×2.16\times speedup with a 4:1 first-stage compression ratio (corresponding to a 16K candidate budget), and up to 3.75×3.75\times speedup under a fixed 8K budget. Although HISA adds a block-level filtering stage, this stage operates only on pooled block summaries of size ⌈L/B⌉\lceil L/B\rceil, which is far smaller than the full token sequence. Moreover, under a fixed 8K budget, the second-stage cost remains nearly constant because both the input and output lengths are fixed, making the computation graph easier to optimize and further improving inference speed.

5.2 Needle-in-a-Haystack

The Needle-in-a-Haystack (NIAH) test (Kamradt, 2023) evaluates a model’s ability to retrieve a specific fact (the ”needle”) embedded at a controlled position within a long distractor context (the ”haystack”). We evaluate DeepSeek-V3.2 with its original DSA indexer replaced by HISA (4:1 ratio) and block indexer, without any additional training, over context lengths ranging from 8K to 648K tokens and needle insertion depths ranging from 0% (beginning) to 100% (end).

Figure 3 presents the retrieval accuracy heatmaps. The original DSA achieves near-perfect retrieval across all context lengths and needle positions (Figure 3(a)). HISA closely matches this performance (Figure 3(c)), with only marginal degradation at extreme lengths and depths, suggesting that the our HISA rarely discards blocks containing the target information. In contrast, the Block-Sparse baseline (Figure 3(b)) exhibits noticeable accuracy degradation, particularly when the needle is located in the middle of the context where block-level selection is least reliable. This result underscores the value of hierarchical selection. Block-sparse methods often waste budget on unimportant tokens within selected blocks while overlooking truly critical tokens. HISA, in contrast, refines the selection at the token level after block retrieval, allowing it to preserve important tokens more accurately and achieve efficient token-wise sparsity.

5.3 LongBench Evaluation

LongBench (Bai et al., 2024) is a comprehensive benchmark for long-context understanding, covering single-document QA, multi-document QA, summarization, few-shot learning, and synthetic retrieval tasks. We evaluate DeepSeek-V3.2 (DeepSeek-AI, 2025) and GLM-5 (GLM-5-Team, 2026) under three configurations: the original DSA indexer, HISA, and Block-Sparse Attention.
For a fair comparison, all three configurations ultimately retain 2048 tokens for computation. Specifically, Block-Sparse Attention directly selects 16 blocks of size 128 (i.e., 128×16=2048128\times 16=2048 tokens). HISA first selects 64 blocks of size 128 (i.e., 128×64=8192128\times 64=8192 tokens), and then further refines them through token-level selection to 2048 tokens.

Table 1: LongBench results for DeepSeek-V3.2 and GLM-5 under different indexing strategies. All sparse methods are applied at inference time without additional training. Scores are averaged across sub-tasks within each category. Task abbreviations: SQA = Single-Document QA, MQA = Multi-Document QA, Sum = Summarization, FS = Few-shot Learning, Syn = Synthetic Retrieval, Code = Code Completion.ModelIndexerSQAMQASumFSSynCodeAvg.DeepSeek-V3.2DSA50.8952.6622.1162.2469.8348.5651.05Block48.3649.7621.9059.4568.6749.0949.54HISA49.1751.9622.1361.6270.8348.9950.78GLM-5DSA41.2327.8918.3963.2068.8456.5346.01Block38.3524.2916.9560.6460.4955.2942.67HISA42.4527.6217.9063.7869.3556.7946.32

Table 1 summarizes the results. Across both models and all task categories, HISA achieves performance very close to that of the original DSA. Notably, HISA consistently surpasses DSA on the Synthetic tasks, and on GLM-5 it even attains a higher average score.
By contrast, the Block-Sparse baseline, which does not include token-level refinement, exhibits a substantially larger performance gap. This is particularly apparent on the Synthetic tasks for GLM-5, where its score declines by 8.35%.

5.4 Visualization of Attention Scores

To analyze the structural properties of attention in long-context generation, we conduct a visualization study on a representative sample from the code task of LongBench. We generate the first output token using DeepSeek-V3.2 and extract the full attention distributions at each layer. We visualize the attention weights over all context tokens as a 2D heatmap, where the x-axis denotes token positions and the y-axis denotes layer indices.

Figure 4: Visualization of Attention Distribution.

The visualization reveals a pattern: tokens with high attention weights tend to form contiguous spans rather than appearing as isolated points in a considerable number of tasks. These high-density regions often correspond to semantically coherent segments (e.g.,code blocks,mathematical formulas and derivations) and persist across multiple layers. Outside these spans,attention scores are negligible.
This observation suggests that attention mass may be naturally concentrated in block-wise regions. Therefore,block-level sparsification can retain most of the informative attention distribution while avoiding the fine-grained selection overhead of token-wise top-k methods. The results provide empirical support for the two-stage hierarchical structure of HISA.

5.5 Hyperparameter Sensitivity

We investigate the sensitivity of HISA to its two key hyperparameters—block size BB and block-level top-mm—by comparing three HISA configurations that share the same candidate pool size, m​B=8192mB=8192, but different coarse-to-fine trade-offs: (B=64,m=128)(B{=}64,m{=}128), (B=128,m=64)(B{=}128,m{=}64), and (B=256,m=32)(B{=}256,m{=}32). We further include the original DSA as an upper bound and Block-Sparse (B=128,m=16)(B{=}128,m{=}16) as a lower bound. All configurations use k=2048k{=}2048 for the final token selection. Results are evaluated on DeepSeek-V3.2 and GLM-5 across five LongBench task categories.

(a) Ablation study on DeepSeek-V3.2.

(b) Ablation study on GLM-5.

Figure 5: LongBench scores under different indexer configurations. All three HISA variants use a candidate token pool of size m​B=8192mB=8192 and a final token budget of k=2048k{=}2048, with different choices of block size BB and block-level top-mm. The Block-Sparse baseline uses B=128B{=}128 and m=16m{=}16, corresponding to a candidate pool of 2048 tokens and no token-level refinement.

Figure 5 reveals several key findings. First, all three HISA configurations closely track DSA performance across all five task categories. This result confirms that our two-stage hierarchical indexer recovers nearly the same set of important tokens as the exhaustive flat scan.
Second, among the three HISA variants, the intermediate configurations (B=64B{=}64 and B=128B{=}128) perform better than B=256B{=}256. This suggests that finer-grained selection is important for accurately identifying the most relevant tokens.
Third, Block-Sparse consistently underperforms all HISA configurations. This gap underscores the importance of token-level refinement: even under the same block-level selection mechanism, the ability to prune low-relevance tokens within selected blocks yields measurable quality gains.

6 Conclusion and Future Directions

To address the emerging bottleneck caused by the O​(L2)O(L^{2}) complexity of the DSA indexer, we propose HISA, a hierarchical indexing approach. Specifically, HISA first uses a hardware-friendly block indexer to efficiently filter out a large number of irrelevant tokens, and then applies token-level reranking over the remaining candidates to construct the final cache for sparse attention computation. At the kernel level, HISA delivers a 3.75×3.75\times speedup over the DSA kernel.
As a plug-and-play module, HISA can directly replace the token indexer in DeepSeek-V3.2 and GLM-5. Without any additional training, it maintains nearly unchanged performance on LongBench. On NIAH, it also performs significantly better than the corresponding block-sparse baseline.

Several avenues remain open: (1) Reducing information loss in coarse filtering: the current block-level stage represents each block with a single pooled vector, which can fail when a block crosses a semantic boundary and the pooled representation does not reflect the most important token. Potential mitigations include overlapping blocks, adaptive block boundaries, or replacing mean pooling with max pooling to better preserve salient outlier directions. (2) Training-aware HISA: while HISA currently operates as a training-free inference-time replacement, jointly training the block scoring stage may improve the coarse filter’s accuracy, particularly for such boundary cases. (3) End-to-end system integration: integrating HISA into a full inference serving stack (e.g., with continuous batching and speculative decoding) and measuring throughput and latency under realistic workloads.

References

Anthropic (2026)External Links: LinkCited by: §1.

Y. Bai, Q. Dong, T. Jiang, X. Lv, Z. Du, A. Zeng, J. Tang, and J. Li (2026)IndexCache: accelerating sparse attention via cross-layer index reuse.
arXiv preprint arXiv:2603.12201.
Cited by: §2.

Y. Bai, X. Lv, J. Zhang, H. Lyu, J. Tang, Z. Huang, Z. Du, X. Liu, A. Zeng, L. Hou, et al. (2024)LongBench: a bilingual, multitask benchmark for long context understanding.
arXiv preprint arXiv:2308.14508.
Cited by: §5.3.

T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Ré (2022)FlashAttention: fast and memory-efficient exact attention with io-awareness.
In Advances in Neural Information Processing Systems,
Vol. 35.
Cited by: §1.

T. Dao (2023)FlashAttention-2: faster attention with better parallelism and work partitioning.
arXiv preprint arXiv:2307.08691.
Cited by: §1.

DeepSeek-AI (2024)DeepSeek-V3 technical report.
arXiv preprint arXiv:2412.19437.
Cited by: §1.

DeepSeek-AI (2025)DeepSeek-v3.2: pushing the frontier of open large language models.
arXiv preprint arXiv:2512.02556.
Cited by: §1,
§2,
§3,
§5.3.

Q. Fu, M. Cho, T. Merth, S. Mehta, M. Rastegari, and M. Najibi (2024)LazyLLM: dynamic token pruning for efficient long context LLM inference.
arXiv preprint arXiv:2407.14057.
Cited by: §2.

GLM-5-Team (2026)GLM-5: from vibe coding to agentic engineering.
arXiv preprint arXiv:2602.15763.
Cited by: §1,
§5.3.

Google DeepMind (2025)External Links: LinkCited by: §1.

J. Huiqiang, L. Yucheng, Z. Chengruidong, W. Qianhui, L. Xufang, A. Surin, H. Zhenhua, A. Amir, L. Dongsheng, L. Chin-Yew, Y. Yuqing, and Q. Lili (2024)MInference 1.0: accelerating pre-filling for long-context llms via dynamic sparse attention.
arXiv preprint arXiv:2407.02490.
External Links: LinkCited by: §2.

G. Kamradt (2023)Needle in a haystack — pressure testing llms.
Note: https://github.com/gkamradt/LLMTest_NeedleInAHaystackCited by: §5.2.

X. Lai, J. Lu, Y. Luo, Y. Ma, and X. Zhou (2025)FlexPrefill: a context-aware sparse attention mechanism for efficient long-sequence inference.
In International Conference on Learning Representations,
Cited by: §2.

C. Lin, J. Tang, S. Yang, H. Wang, T. Tang, B. Tian, I. Stoica, S. Han, and M. Gao (2025)Twilight: adaptive attention sparsity with hierarchical top-pp pruning.
In Advances in Neural Information Processing Systems,
Vol. 38.
Cited by: §2.

E. Lu, Z. Jiang, J. Liu, Y. Du, T. Jiang, C. Hong, S. Liu, W. He, E. Yuan, Y. Wang, et al. (2025)MoBA: mixture of block attention for long-context llms.
arXiv preprint arXiv:2502.13189.
Cited by: §1,
§2,
§4.1.

Meta (2025)External Links: LinkCited by: §1.

MiniMax, A. Li, B. Gong, B. Yang, B. Shan, C. Liu, et al. (2025)MiniMax-01: scaling foundation models with lightning attention.
arXiv preprint arXiv:2501.08313.
Cited by: §1.

Moonshot AI (2025)Kimi K2: open agentic intelligence.
arXiv preprint arXiv:2507.20534.
Cited by: §1.

W. Ni, K. Zhang, Z. Yu, O. Nelson, M. Lee, H. Cai, F. Porikli, J. Kim, Z. Liu, and J. Zhao (2026)Double-p: hierarchical top-p sparse attention for long-context LLMs.
arXiv preprint arXiv:2602.05191.
Cited by: §2.

OpenAI (2026)External Links: LinkCited by: §1.

M. Oren, M. Hassid, N. Rosenfeld, Y. Adi, and R. Schwartz (2024)Transformers are multi-state RNNs.
In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,
Cited by: §2.

Qwen (2026)External Links: LinkCited by: §1.

L. Wang, Y. Cheng, Y. Shi, Z. Tang, Z. Mo, W. Xie, L. Ma, Y. Xia, J. Xue, F. Yang, and Z. Yang (2025)TileLang: a composable tile-based programming model for ai systems.
arXiv preprint arXiv:2504.17577.
Cited by: §5.1.

R. Xu, G. Xiao, H. Huang, J. Guo, and S. Han (2025)XAttention: block sparse attention with antidiagonal scoring.
In Proceedings of the 42nd International Conference on Machine Learning,
Cited by: §2.

Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, and E. Hovy (2016)Hierarchical attention networks for document classification.
In Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,
 pp. 1480–1489.
Cited by: §2.

J. Yuan, H. Gao, D. Dai, J. Luo, L. Zhao, Z. Zhang, Z. Xie, Y. Wei, L. Wang, Z. Xiao, et al. (2025)Native sparse attention: hardware-aligned and natively trainable sparse attention.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
 pp. 23078–23097.
Cited by: §1,
§2,
§2.

L. Yuhong, H. Yingbing, Y. Bowen, V. Bharat, L. Acyr, Y. Hanchen, C. Tianle, L. Patrick, and C. Deming (2024)SnapKV: llm knows what you are looking for before generation.
arXiv preprint arXiv:2404.14469.
External Links: LinkCited by: §2.

J. Zhang, C. Xiang, H. Huang, J. Wei, H. Xi, J. Zhu, and J. Chen (2025)SpargeAttention: accurate and training-free sparse attention accelerating any model inference.
In Proceedings of the 42nd International Conference on Machine Learning,
Cited by: §2.

Z. Zhang, Y. Sheng, T. Zhou, T. Chen, L. Zheng, R. Cai, Z. Song, Y. Tian, C. Ré, C. Barrett, et al. (2024)H2O: heavy-hitter oracle for efficient generative inference of large language models.
In Advances in Neural Information Processing Systems,
Vol. 36.
Cited by: §2.

W. Zhao, Z. Zhou, Z. Su, C. Xiao, Y. Li, Y. Li, Y. Zhang, W. Zhao, Z. Li, Y. Huang, A. Sun, X. Han, and Z. Liu (2026)InfLLM-v2: dense-sparse switchable attention for seamless short-to-long adaptation.
In International Conference on Learning Representations,
Cited by: §2.

Appendix A Algorithm Pseudocode

Algorithm 1 provides the complete pseudocode for the HISA indexer.

Algorithm 1 HISA: Hierarchical Indexed Sparse Attention

0: Query indexing representations {𝐪t,jI}\{\mathbf{q}_{t,j}^{I}\}, gating weights {wt,jI}\{w_{t,j}^{I}\}, token indexing keys {𝐤sI}s=1L\{\mathbf{k}_{s}^{I}\}_{s=1}^{L}, block size BB, block budget mm, token budget kk

0: Selected token set 𝒯t\mathcal{T}_{t} of size kk

1: Partition prefix into M=⌈L/B⌉M=\lceil L/B\rceil blocks ℬ1,…,ℬM\mathcal{B}_{1},\ldots,\mathcal{B}_{M}

2:forb=1b=1 to MMdo

3:𝐤~bI←MeanPool​({𝐤sI∣s∈ℬb})\tilde{\mathbf{k}}_{b}^{I}\leftarrow\mathrm{MeanPool}(\{\mathbf{k}_{s}^{I}\mid s\in\mathcal{B}_{b}\})

4:endfor

5:for each query position ttdo

6:// Stage 1: Block-level coarse filter

7:forb=1b=1 to MMsuch thatℬb\mathcal{B}_{b} precedes ttdo

8:Jt,b←∑jwt,jI⋅ReLU​(𝐪t,jI⋅𝐤~bI)J_{t,b}\leftarrow\sum_{j}w_{t,j}^{I}\cdot\mathrm{ReLU}(\mathbf{q}_{t,j}^{I}\cdot\tilde{\mathbf{k}}_{b}^{I})

9:endfor

10:𝒞t←TopK​(Jt,:,m)∪{first block, last block}\mathcal{C}_{t}\leftarrow\mathrm{TopK}(J_{t,:},\,m)\cup\{\text{first block, last block}\}

11:Ωt←⋃b∈𝒞tℬb\Omega_{t}\leftarrow\bigcup_{b\in\mathcal{C}_{t}}\mathcal{B}_{b}

12:// Stage 2: Token-level refinement

13:fors∈Ωts\in\Omega_{t}do

14:It,s←∑j=1HIwt,jI⋅ReLU​(𝐪t,jI⋅𝐤sI)I_{t,s}\leftarrow\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{ReLU}(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I})

15:endfor

16:𝒯t←TopK​({It,s∣s∈Ωt},k)\mathcal{T}_{t}\leftarrow\mathrm{TopK}(\{I_{t,s}\mid s\in\Omega_{t}\},\,k)

17:endfor

18:return𝒯t\mathcal{T}_{t}

Appendix B Experimental Settings

We detail the experimental settings for long-context evaluations in this section. All evaluations were conducted in a zero-shot setting.

B.1 Long-context Benchmarks

We evaluated the long-context performance using the Needle In A Haystack (NIAH) test and the LongBench benchmark. We tested two models: DeepSeek-V3.2 and GLM-5. Both models were deployed using the vLLM online serving framework with FP8 precision.

NIAH Settings

For the NIAH experiments, we utilized a customized evaluation codebase modified from the RULER222https://github.com/NVIDIA/RULER GitHub repository. We did not apply chat templates to either model to ensure a direct assessment of their raw retrieval capabilities.

LongBench Settings

We evaluated LongBench using the lm-eval333https://github.com/EleutherAI/lm-evaluation-harness framework. The configurations for LongBench varied slightly depending on the model characteristics:

•

Chat Template Usage:
DeepSeek-V3.2 was evaluated with its standard chat template.
In contrast, GLM-5 was evaluated without a chat template. This decision was made because using the template triggered an extended thinking process that exceeded the maximum generation length and significantly slowed down inference. Furthermore, disabling the thinking process while keeping the template resulted in inferior performance compared to not using the template at all.

•

Concurrency Settings:
The default number of concurrent requests (num_concurrent) was set to 20. However, due to Out-Of-Memory (OOM) issues specific to GLM-5 on certain tasks, we adjusted the concurrency: longbench_single was run with a concurrency of 1, and longbench_summary was run with a concurrency of 2.

Fairness of Comparison

We emphasize that although the specific settings (e.g., concurrency, chat template) differ across models and tasks to accommodate their unique characteristics and hardware constraints, we ensure that the settings are strictly aligned when comparing different methods within the same model and task combination. This guarantees a fair and rigorous comparison.

 Experimental support, please
 view the build logs
 for errors. Generated by
 
 L
 A
 T
 Exml.
 

Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
 support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
 methods listed below:

Click the "Report Issue" () button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we
 may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
 should not be a barrier to accessing research. Thank you for your continued support in championing open access for
 all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.

BETA
