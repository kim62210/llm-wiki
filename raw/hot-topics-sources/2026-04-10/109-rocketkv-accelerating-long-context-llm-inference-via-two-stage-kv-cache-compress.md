---
title: RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression
source_url: https://arxiv.org/html/2502.14051v3
final_url: https://arxiv.org/html/2502.14051v3
status: 200
content_type: text/html; charset=utf-8
topics: [Chunk-Semantic KV Cache Compression]
sections: [Inference Optimization]
fetched_at: 2026-04-10T01:43:39.519349+00:00
---

# RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression

## 원본 URL

https://arxiv.org/html/2502.14051v3

## 추출 본문

RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression
1 Introduction

2 Related Work

3 Proposed Method: RocketKV
3.1 Observation

3.2 RocketKV Overview

3.3 First Stage: SnapKV

3.4 Second Stage: Hybrid Sparse Attention

3.5 RocketKV-MT

3.6 Adaptive Compression Decomposition

3.7 System Implications

4 Experiments
4.1 Experimental Settings

4.2 Accuracy Results

4.3 Efficiency Results

5 Conclusion

A Detailed Experiment Settings
A.1 Models

A.2 Benchmarks

A.3 Baselines

B Additional Results
B.1 Ablation Studies
B.1.1 Comparing HSA, Quest, and SparQ

B.1.2 Split Factor

B.2 Needle-in-a-Haystack Visualization

B.3 Detailed Accuracy Results

RocketKV: Accelerating Long-Context LLM Inference via 

Two-Stage KV Cache Compression 

Payman Behnam
Yaosheng Fu
Ritchie Zhao
Po-An Tsai
Zhiding Yu
Alexey Tumanov

Abstract
Transformer-based Large Language Models rely critically on the KV cache to efficiently handle extended contexts during the decode phase.
Yet, the size of the KV cache grows proportionally with the input length, burdening both memory bandwidth and capacity as decoding progresses. To address this challenge, we present RocketKV, a training-free KV cache compression strategy containing two consecutive stages. In the first stage, it performs coarse-grain permanent KV cache eviction on the input sequence tokens.
In the second stage, it adopts a hybrid sparse attention method to conduct fine-grain top-k sparse attention, approximating the attention scores by leveraging both head and sequence dimensionality reductions.
We show that RocketKV provides a compression ratio of up to 400×\times, end-to-end speedup of up to 3.7×\times as well as peak memory reduction of up to 32.6% in the decode phase on an NVIDIA A100 GPU compared to the full KV cache baseline, while achieving negligible accuracy loss on a variety of long-context tasks.
We also propose a variant of RocketKV for multi-turn scenarios, which consistently outperforms other existing methods and achieves accuracy nearly on par with an oracle top-k attention scheme. The source code is available here: https://github.com/NVlabs/RocketKV.

Machine Learning, ICML, LLM, KV cache, Compression

1 Introduction

In Transformer-based LLM inference (Vaswani et al., 2017; Pawar et al., 2024), the key-value cache (KV cache)—which stores past attention keys and values to avoid recomputation—becomes a major bottleneck during the decode phase, as its size scales linearly with both the sequence length and batch size.
For example, the Llama3.1-70B-Instruct (AI@Meta, 2024) model with a batch size of 32, and a context length of 32K requires around 320GB of KV cache storage at FP16 precision, which even advanced hardware (NVIDIA, 2024; Jouppi et al., 2023; AMD, 2024) can hardly handle.

Fortunately, previous work has shown that only a small subset of KV tokens is required at each decode step to maintain accuracy (Zhang et al., 2023; Tang et al., 2024; Ribar et al., 2024; Li et al., 2024; Singhania et al., 2024; Ge et al., 2024). Therefore, if those KV tokens can be accurately predicted in advance, dense attention operations can be replaced with sparse attention operations with significant memory bandwidth and capacity improvement. These methods often fall into two categories: 1) permanent KV token eviction, and 2) dynamic KV token selection. The former results in both memory bandwidth and storage savings, but could lead to noticeable accuracy loss if KV tokens dropped earlier are needed by later decode steps. The latter avoids this shortcoming by keeping all KV tokens in memory and dynamically selecting a subset each time. Hence, it only results in memory bandwidth savings, but often requires extra memory storage overhead for auxiliary data.

Figure 1: Existing KV token dropping methods fail to match the accuracy scores of oracle top-k attention (Exact-TopK) on Mistral-7B-Ins-v0.2 in the qasper benchmark.

To understand the effectiveness of existing KV token dropping methods, Figure 1 presents the accuracy comparison of four different methods (two in each category) for qasper benchmark in LongBench (Bai et al., 2024) on the Mistral-7B-Instruct-v0.2 model (Jiang et al., 2023). We observe that the accuracy of all four methods drops significantly as the token budget becomes lower than 1024 while an oracle top-k attention scheme achieves negligible accuracy drop even with a token budget of 256. This indicates that existing practical methods fail to accurately predict top-k KV tokens under low token budgets.

To improve the prediction accuracy, we propose RocketKV, a two-stage KV cache compression method that combines permanent KV token eviction with dynamic KV token selection to accelerate the decode phase of LLM inference.
The RocketKV framework enables flexible integration of a wide range of KV cache compression techniques at each stage.
To achieve optimal performance, we directly adopt an existing method SnapKV (Li et al., 2024) for coarse-grain permanent KV token eviction in the first stage.
In the second stage, we propose hybrid sparse attention (HSA) to perform fine-grain dynamic KV token selection, which estimates KV token indices with top-k attention scores via two-dimensional reductions. To balance the compression between two stages, RocketKV introduces an adaptive compression decomposition mechanism that intelligently splits any given target compression ratio across two stages. Combining these two stages together, RocketKV achieves significant memory bandwidth and storage savings with negligible accuracy loss across a wide variety of models and downstream tasks.

Moreover, recent work (Li et al., 2025) demonstrates that permanent KV token eviction suffers in multi-turn decoding because important KV tokens vary significantly across queries. To address this challenge, we propose a variant of RocketKV called RocketKV-MT for multi-turn scenarios where we do not evict the unselected KV tokens in the first stage but keep them all for later turns. Yet, the decode phase is still restricted to perform dynamic selection on the filtered KV tokens from the first stage in each turn. By doing this, RocketKV-MT achieves the same memory traffic savings as RocketKV but does not introduce memory storage savings.

In summary, we make the following contributions:

•

We analyze and identify the limitations of existing KV token dropping methods and then propose RocketKV as a two-stage KV cache compression scheme. We further introduce a variant RocketKV-MT for multi-turn decoding scenarios.

•

We propose a hybrid sparse attention (HSA) for dynamic KV token selection with two-dimensional reductions in the second stage while directly adopting SnapKV in the first stage. We design an adaptive compression decomposition mechanism to balance the compression between the two stages.

•

We conduct a comprehensive evaluation of RocketKV and RocketKV-MT on a wide variety of models and downstream tasks. RocketKV consistently demonstrates comparable accuracy with full KV attention at up to 400×\times compression ratio, while achieving up to 3.7×\times end-to-end speedup and 32.6% peak memory saving at the decode phase on an NVIDIA A100 GPU. Meanwhile, RocketKV-MT is more suitable for multi-turn decoding and performs on par with oracle top-k attention.

2 Related Work

A number of recent approaches have focused on improving the efficiency of attention mechanisms in LLMs, particularly when dealing with long contexts. One feasible solution is KV cache sharing across multiple layers (Brandon et al., 2024) or selectively dropping attention for some layers (Ling et al., 2024). Others (Sun et al., 2024; Ho et al., 2024) propose mixed attention designs where some layers use global attention while others use local attention. Multi-Query Attention (MQA) (Shazeer, 2019), Grouped-Query Attention (GQA) (Ainslie et al., 2023), and Multi-head Latent Attention(MLA) (Liu et al., 2024a)are widely adopted by many recent LLMs (AI@Meta, 2024; Jiang et al., 2023; Team et al., 2024; Liu et al., 2024b), which reduce the KV cache by sharing key-value pairs across multiple attention heads. All above techniques directly modify the attention architecture and require integration since pre-training.

Another direction is to improve attention efficiency with training-free techniques. These techniques can be further categorized as prefill phase acceleration, decode phase acceleration, or accelerating both phases together. For example, StreamingLLM (Jiang et al., 2023) combines initial and local-window attention to reduce the KV cache into a constant size regardless of the sequence length.
DuoAttention (Xiao et al., 2025) and RazorAttention (Tang et al., 2025) improve upon StreamingLLM by applying global attention on retrieval heads and StreamingLLM-style attention on rest heads. While these techniques can be applied to both the prefill and decode phases, other techniques focus on accelerating only one of the two phases.

For prefill phase acceleration, MInference (Jiang et al., 2024) identifies three distinct patterns in the attention matrix that can be harnessed for efficient sparse operations with customized GPU kernels.
SeerAttention (Gao et al., 2024) explores dynamic block-level sparsity in the attention module with a learnable gate.
Meanwhile, XAttention (Xu et al., 2025) leverages the sum of antidiagonal values in the attention matrix for estimating block importance.

A common approach for attention acceleration at the decode phase is through permanent KV cache eviction, which can save both memory bandwidth and storage requirements. H2O (Zhang et al., 2023) observes that a small subset of tokens, known as heavy-hitters, dominates the attention computation, thus only keeps recent and heavy-hitter tokens.
SnapKV (Li et al., 2024) employs an observation window at the end of the prompt to identify critical KV tokens of the input prompt. Then it uses a clustering algorithm via pooling to retain critical KV token clusters without losing information completeness.
Ada-KV (Feng et al., 2024) proposes an adaptive budget allocation strategy to provide better token budget utilization across individual heads.

Meanwhile, Quest (Tang et al., 2024) observes that permanent KV cache eviction could lead to inevitable accuracy loss and proposes query-aware selection on top-k KV tokens based on approximation attention with representative vectors of contiguous key cache pages.
On the other hand, SparQ and Loki (Ribar et al., 2024; Singhania et al., 2024) conduct approximation attention by selecting only important indices on the head dimension instead.
The above approaches can save KV cache compute and data fetching from memory, but not KV cache storage. InfiniGen (Lee et al., 2024) tackles this challenge by offloading the entire KV cache to CPU memory and only fetching the selected KV tokens to GPU memory when needed. MagicPIG(Chen et al., 2025) discovers that using importance sampling is more efficient than top-k estimation and proposes an approximation attention solution leveraging locality sensitive hashing (LSH) and CPU offloading.

In contrast to prior work, RocketKV combines both permanent KV cache eviction and dynamic KV token selection as two consecutive stages for accelerating the decode phase and utilizes the advantages of both worlds. As a result, it achieves remarkable memory bandwidth and storage savings without the need for sophisticated system-level optimizations such as CPU offloading.

3 Proposed Method: RocketKV
Figure 2: The CDF of maximum sequence length and number of unique top-k indices (k=256) across all decoding steps for 200 questions in the qasper benchmark. Data was collected from a random head (layer 31 head 0) in Mistral-7B-Instruct-v0.2.

3.1 Observation

As shown previously in Figure 1, existing token dropping methods, regardless of permanent KV token eviction or dynamic KV token selection, fail to match the accuracy of oracle top-k attention (Exact-TopK) under low token budgets. To further understand what causes the accuracy mismatch, we analyze a random attention head (layer 31 head 0) from Mistral-7B-Instruct-v0.2 and present the cumulative distribution function (CDF) of both the maximum sequence length and number of unique KV indices selected by Exact-TopK (k=256) across all decoding steps in the qasper benchmark. The reason behind this analysis is that in order to match the accuracy of Exact-TopK, we need to keep all important KV tokens that are selected by at least one top-k attention operation across all decoding steps. As shown in Figure 2, although the maximum sequence length can reach as high as 25000, the number of unique top-k indices only goes up to 1200. This implies that, ideally, a permanent KV token eviction method should be able to close the accuracy gap under a token budget of 1200. To further reduce the token budget, we realize that dynamic KV token selection can be applied on the filtered KV token set after permanent KV token eviction. Since the filtered set is much smaller than the original full KV cache, the difficulty for accurate top-k prediction is greatly reduced. Therefore, an ideal solution would be to perform permanent KV cache eviction with a larger token budget first and then conduct dynamic KV token selection on the remaining KV tokens. This fusion evicts unimportant tokens and also makes the dynamic selection more accurate, motivating our RocketKV design.

Figure 3: Overview of RocketKV with two consecutive stages.

3.2 RocketKV Overview

Based on our observation, we propose RocketKV, a two-stage KV cache compression method for decode phase acceleration. As shown in Figure 3, RocketKV performs coarse-grain KV cache eviction in the first stage. The purpose of this stage is to remove KV tokens with low importance while keeping the majority of important tokens.
In the second stage, it conducts fine-grain dynamic KV token selection on the remaining KV tokens, followed by top-k sparse attention.
The RocketKV framework is generic, and many existing KV cache compression methods can fit into the corresponding stage. For example, SnapKV (Li et al., 2024) or Ada-KV (Feng et al., 2024) can be used for the first stage, and Quest (Tang et al., 2024) or SparQ (Ribar et al., 2024) can be applied to the second stage.
To achieve the best performance at each stage, we directly adopt SnapKV in the first stage while proposing a hybrid sparse attention (HSA) method in the second stage.

3.3 First Stage: SnapKV

In the first stage, we directly adopt SnapKV for permanent KV token eviction on the input KV tokens. SnapKV’s key idea is to rely on the aggregated attention scores between the input context and observation window in the end to select the most relevant tokens to keep within the input prompt. The original SnapKV method selects crucial KV tokens on a per attention head basis. In case of grouped-query attention (GQA), each attention head within an attention group keeps a separate set of KV cache tokens, which could introduce redundant storage of the same KV token. To reduce KV token storage with GQA, we follow the Ada-KV work to perform token selection on a per-group basis according to aggregated per-group attention scores so that the selected KV tokens are shared across the entire attention group.
SnapKV uses pooling along the sequence dimension to ensure critical KV tokens are selected along with their neighbor tokens. It demonstrates better accuracy with pooling because it retains the completeness of selected information. The employed kernel sizes for pooling are quite small (e.g., a kernel size of 7 for LongBench (Bai et al., 2024)). Since in our case, SnapKV is only used for coarse-grain KV token eviction at the first stage, we discovered that the optimal kernel sizes for pooling are much larger. We empirically set the kernel size to 63 in all our experiments.

Algorithm 1 HSA Algorithm (only contains step 2 and 3)

Input:query vector qq, key tensor KK, value tensor VV, element-wise max/min key tensor Km​a​x/Km​i​nK_{max}/K_{min}

# get top-k1k_{1} indices along head dim from sum of |q||q| in group dim

i1←a​r​g​t​o​p​k​(s​u​m​(|q|,d​i​m=g​r​o​u​p),k1)i_{1}\leftarrow argtopk(sum(|q|,dim=group),k_{1})

# get signs of top-k1k_{1} indices from sum of q in group dim

g←s​i​g​n​(s​u​m​(q[i1],d​i​m=g​r​o​u​p))g\leftarrow sign(sum(q_{[i_{1}]},dim=group))

# fetch corresponding indices from paged min or max

P←Km​a​x⁣[i:gi≥0],Km​i​n⁣[i:gi<0]P\leftarrow K_{max[i:g_{i}\geq 0]},K_{min[i:g_{i}<0]}

# compute approximation attention scores

s1←s​c​o​r​e​(q[i​1],P)s_{1}\leftarrow score(q_{[i1]},P)

# get indices with top-k2k_{2} attention scores along seq. dim

i2←a​r​g​t​o​p​k​(s1,k2)i_{2}\leftarrow argtopk(s_{1},k_{2})

# perform sparse attention

y←a​t​t​n​(q,K[i​2],V[i​2])y\leftarrow attn(q,K_{[i2]},V_{[i2]})

returnyy

Figure 4: Illustration of hybrid sparse attention with figure (left) and algorithm (right).

3.4 Second Stage: Hybrid Sparse Attention

Previous methods on dynamic KV token selection often estimate top-k KV indices with reduced computation along a single dimension. For example, Quest (Tang et al., 2024) uses element-wise minimum and maximum values to represent continuous pages along the sequence dimension. Meanwhile, SparQ (Ribar et al., 2024) and Loki (Singhania et al., 2024) leverage sparsity in the head dimension to conduct low-rank estimations. Unfortunately, relying on one-dimensional sparsity can only achieve a certain degree of compression ratio, beyond which the accuracy could drop rapidly, as shown previously in Figure 1. In contrast, we propose hybrid sparse attention (HSA), which takes advantage of two-dimensional reduction, in both sequence and head dimensions together to achieve better estimation accuracy on KV token indices with top-k attention scores.

Figure 4 shows the detailed implementation of our proposed algorithm, which is inspired by Quest (Tang et al., 2024) and SparQ (Ribar et al., 2024). Our HSA algorithm can be decomposed into three steps:

•

Step 1: Group tokens in key tensor into consecutive pages along the sequence dimension and store element-wise maximum (Kmax)(K_{\max}) and minimum (Kmin)(K_{\min}) values of each page as auxiliary storage similar to Quest. Unlike Quest, they are stored with a different layout by aligning along the head dimension to enable efficient gathering in Step 2. The auxiliary storage is updated accordingly each time a new key token is generated.

•

Step 2: For each query qq, find k1k_{1} largest absolute values along the head dimension. Then, fetch only the corresponding indices in either element-wise maximum or minimum tensors, depending on the sign of qq at those indices. The goal is to compute element-wise max⁡(q×Kmax,q×Kmin)\max(q\times K_{\max},\ q\times K_{\min}) for each page to approximate the highest possible attention scores within a page. To further reduce the approximation overhead, we only calculate on k1k_{1} partial positions along the head dimension with a large magnitude of qq and ignore others, similar to SparQ. Once the approximation attention scores are calculated, k2k_{2} indices with the largest attention scores along the sequence dimension are selected.

•

Step 3: Perform sparse attention by fetching the original key and value vectors from the predicted k2k_{2} indices.

Our HSA algorithm is fully compatible with GQA. To achieve this, we perform all key tensor selections on a per attention group basis. More details are shown in Algorithm 1 where we perform the sum of qq or |q||q| in the group dimension as needed to guarantee that all attention heads within a group are making the same selection at each step.

3.5 RocketKV-MT

In a multi-turn conversation setting, KV tokens that were pruned in earlier turns may become essential for answering queries in later turns because KV token importance could vary significantly between different turns  (Li et al., 2025). Consequently, permanently removing these tokens could lead to a noticeable accuracy drop in subsequent turns.

To mitigate this issue, we introduce a multi-turn variant of our approach called RocketKV-MT. The core idea in RocketKV-MT is to avoid permanently evicting any KV tokens during the first stage; instead, all KV tokens are retained in memory across turns, ensuring that no potentially useful context is lost. Meanwhile, to preserve computational efficiency, the second stage still performs dynamic selection over the subset of KV tokens filtered by the first stage, similar to the original RocketKV. In other words, the model generates responses using a reduced KV token set for speed, while reserving the full KV history for future turns. For example, suppose the first stage of RocketKV-MT retains only NN out of MM total KV tokens from the input prompt in the first turn. RocketKV-MT will still keep all MM tokens in memory but restrict the second stage to dynamically select from these NN input tokens (plus any new generated tokens) during the decode phase. In the next turn, the full set of previously stored KV tokens (all MM input tokens plus all output tokens) is added to the new input KV cache. The filtering process (with SnapKV in our case) is applied again on this whole input KV cache to select a new subset of important tokens for this turn’s decode phase. By following this strategy, RocketKV-MT achieves similar decoding speedups to RocketKV in each turn, while retaining the full KV cache history across all turns. This approach effectively eliminates the accuracy degradation caused by permanent KV token eviction in multi-turn scenarios at the cost of no memory storage savings.

3.6 Adaptive Compression Decomposition

The decode phase of LLM inference is typically memory bound (Ribar et al., 2024); so, the time spent in the attention module is roughly proportional to the total memory traffic. In this work, we use the token budget tt to estimate the amount of memory traffic for each attention operation in the decode phase (we mainly focus on KV cache traffic since it contributes to the majority of memory traffic in this scenario). For example, a token budget of 512 means each attention module needs to fetch an equivalent total amount of 512 key and value pairs from memory. Unlike prior work (Tang et al., 2024) where the token budget only reflects the memory traffic for top-k attention (Step 3 in HSA), we define the token budget to also include the memory traffic of  top-k estimation (Step 2 in HSA). By doing this, the token budget can reflect the overall memory traffic in the attention module more precisely. For simplicity, we evenly split the token budget between these two steps for HSA and all other dynamic KV token selection methods in our later experiments. For models with GQA, this token budget is defined for the entire attention group rather than each attention head. For a given sequence length of SS, the total compression ratio of cc can be defined as c=S/tc=S/t.

Since RocketKV is a two-stage KV cache compression framework where the filtered KV token set by the first stage serves as the input of the second stage for dynamic selection, it is important to determine the intermediate token budget for the filtered KV token set. For an overall compression ratio of cc, we define a split factor rr so that cc is split into crc^{r} for the first stage and c(1−r)c^{(1-r)} for the second stage, where 0<=r<=10<=r<=1. We use the following formula to adaptively determine rr:
r=m​i​n​(0.2+0.06∗l​o​g2​(c),0.8)r=min(0.2+0.06*log_{2}(c),0.8)
The insight behind this formula is that when cc is small, we would like to minimize the number of permanent evicted KV tokens in the first stage to prevent information loss. As cc increases, the accuracy drop caused by HSA in the second stage gets larger thus it is better to assign a higher compression ratio to the first stage because SnapKV can estimate important KV tokens more precisely using exact attention scores. We further limit the range of rr between 0.2 and 0.8 to balance the compression decomposition between these two stages.

For compression decomposition within HSA, we simply split the compression ratio c(1−r)c^{(1-r)} evenly between the sequence and head dimensions so that each dimension gets a compression ratio of c(1−r)/2c^{(1-r)/2}. Notice that the compression ratio along the sequence dimension is equivalent to the page size, so we need to round it up the nearest integer ⌈c(1−r)/2⌉\lceil c^{(1-r)/2}\rceil and the other dimension gets c(1−r)/⌈c(1−r)/2⌉c^{(1-r)}/\lceil c^{(1-r)/2}\rceil.

Because RocketKV strategically decomposes KV cache compression across multiple stages and dimensions, it significantly enhances the potential for high compression ratios while maintaining strong accuracy—surpassing methods that rely on single-stage, single-dimension approaches.
For example, given a compression ratio of 64×64\times, the split factor can be calculated as r=0.2+0.06∗l​o​g2​(64)=0.56r=0.2+0.06*log_{2}(64)=0.56. Therefore, the compression ratio is split into 640.56=10.3×64^{0.56}=10.3\times in the first stage and 64(1−0.56)=6.2×64^{(1-0.56)}=6.2\times in the second stage. HSA further splits its compression ratio into 3×3\times in the sequence dimension (with a page size of 3) and 2.1×2.1\times in the head dimension. We can see that each individual stage and dimension gets assigned with a much smaller compression ratio after decomposition.

Table 1: Normalized KV cache storage (including auxiliary data) and traffic comparison between RocketKV, RocketKV-MT and other methods.
MethodCompression RatioStorageTrafficFull-KV111DuoAttentioncc1/c1/c1/c1/cSnapKVcc1/c1/c1/c1/cQuestcc1+1/c1+1/c1/c1/cSparQcc21/c1/cRocketKVcc1/cr+2/c(1+r)/21/c^{r}+2/c^{(1+r)/2}1/c1/cRocketKV-MTcc1+2/c(1+r)/21+2/c^{(1+r)/2}1/c1/c

In RocketKV, the first stage results in both KV cache storage and traffic reduction of crc^{r}. In the second stage, we need to take the additional memory storage overhead introduced by the approximation attention into consideration. Since we evenly split the compression ratio c(1−r)c^{(1-r)} into c(1−r)/2c^{(1-r)/2} (ignore the round up operation here for simplicity) between two dimensions in HSA, it introduces a memory storage overhead of (1/cr)×(1/c(1−r)/2)×2=2/c(1+r)/2(1/c^{r})\times(1/c^{(1-r)/2})\times 2=2/c^{(1+r)/2} where 1/cr1/c^{r} is the relative KV cache storage after the first stage and both element-wise maximum and minimum tensors introduce a storage overhead of 1/c(1−r)/21/c^{(1-r)/2} on top of it. Therefore, the total KV cache storage and traffic in RocketKV are 1/cr+2/c(1+r)/21/c^{r}+2/c^{(1+r)/2} and 1/c1/c of the full KV baseline, respectively.
RocketKV-MT does not lead to storage saving in the first stage, so its relative KV cache storage is 1+2/c(1+r)/21+2/c^{(1+r)/2} instead.
Table 1 compares the KV cache storage and traffic of RocketKV and RocketKV-MT against other methods at a given compression ratio cc. We can see that while all methods lead to the same KV cache traffic savings, only RocketKV, DuoAttention and SnapKV provide additional KV cache storage savings, but RocketKV-MT, Quest and SparQ require extra storage for auxiliary data.

3.7 System Implications

RocketKV is fully compatible with FlashAttention (Dao et al., 2022) because it does not modify attention in the prefill phase. Additionally, it seamlessly integrates with tensor parallelism (Shoeybi et al., 2019) because all operations are symmetric across attention heads/groups. It is worth noting that both RocketKV and RocketKV-MT work well with the disaggregated serving system, where different GPUs are used for prefill and decode phases (NVIDIA, 2025; Qin et al., 2025). For RocketKV, the KV cache storage is reduced on both the prefill and decode GPU, as well as the KV cache transfer traffic between them. While the full KV cache needs to be stored in the prefill GPU for RocketKV-MT, only the filtered set needs to be transferred and stored in the decode GPU, resulting in the same communication and decoding benefits as RocketKV.

4 Experiments

4.1 Experimental Settings

(a)LongBench, Llama3.1-8B-Ins 

(b)LongBench, Mistral-7B-Ins-v0.2 

(c)LongBench, LongChat-7B-v1.5 

(d)NIAH, Llama3.1-8B-Ins 

(e)NIAH, Mistral-7B-Ins-v0.2 

(f)NIAH, LongChat-7B-v1.5 

(g)Llama3.1-8B-Ins, SeqLen=16K 

(h)Llama3.1-8B-Ins, SeqLen=32K

(i)Llama3.1-8B-Ins, SeqLen=64K 

(j)Llama3.1-8B-Ins, SeqLen=96K

(k)Mistral-7B-Ins-v0.2,SeqLen=8K 

(l)Mistral-7B-Ins-v0.2,SeqLen=16K 

(m)Mistral-7B-Ins-v0.2,SeqLen=24K 

(n)Mistral-7B-Ins-v0.2,SeqLen=32K 

(o)LongChat-7B-v1.5,SeqLen=8K

(p)LongChat-7B-v1.5,SeqLen=16K

(q)LongChat-7B-v1.5,SeqLen=24K

(r)LongChat-7B-v1.5,SeqLen=32K

Figure 5: Comparing the accuracy of RocketKV with other methods on LongBench (a-c), Needle-in-a-Haystack (NIAH) (d-f), and RULER with various sequence lengths (g-r).

We conduct our experiments on three widely used long-context models: Llama3.1-8B-Instruct (AI@Meta, 2024), Mistral-7B-Instruct-v0.2 (Jiang et al., 2023), and LongChat-7B-v1.5-32k (Li et al., 2023). We refer to these models as Llama3.1-8B-Ins, Mistral-7B-Ins-v0.2, LongChat-7B-v1.5, respectively, throughout the paper.
The first two models are based on GQA, while the last one is based on MHA. For downstream tasks, we utilize LongBench (Bai et al., 2024), Needle-in-a-Haystack (Kamradt, 2023), RULER (Hsieh et al., 2024), and SCBench (Li et al., 2025). We compare RocketKV and RocketKV-MT with several other methods: Full-KV, Exact-TopK, DuoAttention (Xiao et al., 2025), SnapKV (Li et al., 2024), Quest (Tang et al., 2024), and SparQ (Ribar et al., 2024). Exact-TopK serves as an oracle method for sparse attention with exact top-k KV token selection. Notice that RocketKV-MT acts the same as RocketKV in single-turn scenarios, so we only evaluate it on SCBench under multi-turn mode. We evaluate all methods across various KV token budgets per attention group, except for Full-KV. RocketKV, RocketKV-MT, Quest, and SparQ involve additional memory traffic for top-k approximation, which is converted into an equivalent KV token budget such that the total token budget precisely reflects the total amount of memory traffic in the attention module. More details on our experimental settings are available in Appendix A. We also conduct additional ablation studies in Appendix B.1.

4.2 Accuracy Results

In our accuracy evaluation, we vary the token budget of each method from 256 to 4096 for all single-turn benchmarks and from 1024 to 16384 for SCBench under multi-turn mode. We compare the average accuracy across all individual tasks for each benchmark. More detailed results with accuracy breakdown for individual tasks are available in Appendix B.

LongBench Benchmark:
The first row in Figure 5 shows the average score comparison of RocketKV with other methods on LongBench across all three models. Based on the figure, we can see that RocketKV consistently outperforms all other methods, especially under lower token budgets. For Llama3.1-8B-Ins, RocketKV achieves almost no accuracy loss with a token budget of 512 and above, and only 1.1% average accuracy drop with a token budget of 256. RocketKV results in slightly higher accuracy losses for Mistral-7B-Ins-v0.2 and LongChat-7B-v1.5, which might be because Llama3.1-8B-Ins is better-trained than the other two models, making it more robust to sparse attention methods, as a similar trend can be found with Exact-TopK. SparQ performs well on Llama3.1-8B-Ins and LongChat-7B-v1.5 with a token budget of 1024 and above but underperforms all other methods on Mistral-7B-Ins-v0.2. SnapKV alone achieves relatively good accuracy under low token budgets, but we still observe widening accuracy gaps between SnapKV and RocketKV as the token budget decreases.

Needle-in-a-Haystack (NIAH) Benchmark:
Presented in the second row of Figure 5, RocketKV achieves near the Full-KV accuracy across all models, even with a token budget of 256. In fact, it reaches 100% accuracy on Llama3.1-8B-Ins under 256 token budget, which corresponds to a compression ratio of over 400×\times with a maximum sequence length of 109K tokens. In contrast, all other methods suffer from substantial accuracy drops. While SnapKV leads to comparable accuracy to RocketKV on Llama3.1-8B-Ins, its accuracy for Mistral-7B-Ins-v0.2 and LongChat-7B-v1.5 decreases by more than 20% compared to Full-KV, even with a token budget of 1024. We present the heatmaps of RocketKV under various token budgets in Appendix B.2.

RULER Benchmark:
For the RULER benchmark, we evaluate all methods across three models with varying sequence lengths as shown in Figure 5 (rows 3-5). Again, RocketKV shows robust performance and a clear advantage over all other methods across various token budget and sequence length settings. Overall, we can see that the accuracy loss of RocketKV is negligible under short sequence lengths and gradually becomes larger as sequence length increases. We believe this is because these models are less robust to sparse attention beyond their effective sequence lengths as defined in the RULER paper (Hsieh et al., 2024). Notice that the accuracy gaps between RocketKV and other methods become even wider under longer sequence lengths.

Figure 6: Comparing the accuracy of RocketKV and RocketKV-MT with other methods on Llama3.1-8B-Ins for SCBench.

SCBench Benchmark:
Figure 6 presents the accuracy comparison of various methods on SCBench under the multi-turn setting. While RocketKV still outperforms other methods under low token budgets, it provides lower accuracy than SparQ for token budgets of 8192 and beyond. Moreover, there is still a noticeable accuracy gap between RocketKV and Exact-TopK under all token budgets, showing room for further improvement. As we discussed earlier, this is primarily caused by the fact that KV token importance varies significantly across different turns, so the unimportant KV tokens evicted by earlier turns could lead to a significant accuracy drop in later turns. After fixing this issue in RocketKV-MT, we can see that RocketKV-MT achieves a significant accuracy boost with comparable accuracy to Exact-TopK across all token budgets.

(a) End-to-end speedup on A100

(a) End-to-end speedup on H100

(b) Peak memory saving

Figure 7: End-to-end speedup and peak memory savings of RocketKV with various token budgets compared to Full-KV.

4.3 Efficiency Results

Our efficiency experiments are conducted with Llama3.1-8B-Ins (AI@Meta, 2024) under FP16 precision, running on NVIDIA H100 and A100 GPUs at a batch size of 1. Similar to SparQ, we leverage gpt-fast (PyTorchLabs, 2023), a low-latency python-native LLM framework for running the efficiency experiments.
We found a python-based implementation of RocketKV under gpt-fast is sufficient to demonstrate its efficiency benefit, but it could be further improved with customized CUDA kernels and more advanced frameworks such as FlashInfer (Ye et al., 2025).
Figure 7 demonstrates the end-to-end speedups and peak memory savings of RocketKV with varying token budgets at the decode phase, with all values normalized to Full-KV.
Notice that the peak memory usage is the same regardless of the underlying GPU, and it is measured includes memory allocations for weights, activations, KV cache, and all other metadata at the decode phase.

As shown in the Figure 7, RocketKV achieves up to 3.7×\times and 3.3×\times end-to-end speedups on an A100 and H100 GPU, respectively, as well as up to 32.6% peak memory saving. The maximum speedup on A100 is 12% higher than H100 because A100 has a lower memory bandwidth to compute ratio compared to H100. As a result, LLM inference execution is more memory-bound on A100 and can benefit more from the memory traffic savings of the KV cache offered by RocketKV. We expect the speedup of RocketKV will be even higher on cheaper GPUs such as RTX 4090/5090 since they are not equipped with High Bandwidth Memory (HBM).

5 Conclusion

RocketKV presents a novel, training-free approach to KV cache compression, addressing the challenges of memory bandwidth and capacity demands during the decode phase of LLM inference. RocketKV contains two consecutive stages: SnapKV for coarse-grain permanent KV cache eviction and hybrid sparse attention (HSA) for fine-grain dynamic KV token selection. Our evaluations on various models and long-context benchmarks demonstrate that RocketKV maintains comparable accuracy to full KV cache attention while significantly lowering memory bandwidth and capacity usage with a compression ratio of up to 400×\times, as well as up to 3.7×\times end to end speedup and 32.6% peak memory reduction at the decode phase, highlighting its efficiency and potential for widespread application in optimizing LLM performance.
We also propose a variant of RocketKV called RocketKV-MT that is optimized for multi-turn scenarios.

Acknowledgment

We thank the anonymous ICML reviewers for their valuable and constructive feedback. We are grateful to David Nellans for overseeing the internship process of Payman Behnam, during which this work was supported by the NVIDIA Graduate Fellowship. We also thank Song Han and Christos Kozyrakis for their insightful discussions and helpful feedback.

Impact Statement

This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

References

AI@Meta (2024)
AI@Meta.

Llama 3 Model Card.

2024.

Ainslie et al. (2023)
Ainslie, J., Lee-Thorp, J., de Jong, M., Zemlyanskiy, Y., Lebrón, F., and Sanghai, S.

GQA: Training generalized multi-query transformer models from multi-head checkpoints.

Conference on Empirical Methods in Natural Language Processing (EMNLP), 2023.

AMD (2024)
AMD.

Instinct™ MI300X Accelerators.

https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html, 2024.

Accessed: 2025-01-07.

Bai et al. (2024)
Bai, Y., Lv, X., Zhang, J., Lyu, H., Tang, J., Huang, Z., Du, Z., Liu, X., Zeng, A., Hou, L., et al.

LongBench: A bilingual, multitask benchmark for long context understanding.

Annual Meeting of the Association for Computational Linguistics (ACL), 2024.

Brandon et al. (2024)
Brandon, W., Mishra, M., Nrusimha, A., Panda, R., and Ragan Kelly, J.

Reducing transformer key-value cache size with cross-layer attention.

Conference on Neural Information Processing Systems (Neurips), 2024.

Chen et al. (2025)
Chen, Z., Sadhukhan, R., Ye, Z., Zhou, Y., Zhang, J., Nolte, N., Tian, Y., Douze, M., Bottou, L., Jia, Z., and Chen, B.

MagicPIG: LSH Sampling for Efficient LLM Generation.

International Conference on Learning Representations (ICLR), 2025.

Dao et al. (2022)
Dao, T., Fu, D., Ermon, S., Rudra, A., and Ré, C.

Flashattention: Fast and memory-efficient exact attention with io-awareness.

Conference on Neural Information Processing Systems (Neurips), 35:16344–16359, 2022.

Feng et al. (2024)
Feng, Y., Lv, J., Cao, Y., Xie, X., and Zhou, S. K.

Ada-kv: Optimizing kv cache eviction by adaptive budget allocation for efficient llm inference.

arXiv preprint arXiv:2407.11550, 2024.

Gao et al. (2024)
Gao, Y., Zeng, Z., Du, D., Cao, S., So, H. K.-H., Cao, T., Yang, F., and Yang, M.

SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs.

arXiv preprint arXiv:2410.13276, 2024.

URL https://arxiv.org/abs/2410.13276.

Ge et al. (2024)
Ge, S., Zhang, Y., Liu, L., Zhang, M., Han, J., and Gao, J.

Model tells you what to discard: Adaptive kv cache compression for llms.

International Conference on Learning Representations (ICLR), 2024.

Ho et al. (2024)
Ho, N., Bae, S., Kim, T., Jo, H., Kim, Y., Schuster, T., Fisch, A., Thorne, J., and Yun, S.-Y.

Block Transformer: Global-to-Local Language Modeling for Fast Inference.

Conference on Neural Information Processing Systems (Neurips), 2024.

Hsieh et al. (2024)
Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh, D., Jia, F., and Ginsburg, B.

RULER: What’s the real context size of your long-context language models?

Conference on Language Modeling (COLM), 2024.

Jiang et al. (2023)
Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., Casas, D. d. l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al.

Mistral 7b.

arXiv preprint arXiv:2310.06825, 2023.

Jiang et al. (2024)
Jiang, H., Li, Y., Zhang, C., Wu, Q., Luo, X., Ahn, S., Han, Z., Abdi, A. H., Li, D., Lin, C.-Y., et al.

MInference 1.0: Accelerating pre-filling for long-context llms via dynamic sparse attention.

Conference on Neural Information Processing Systems (Neurips), 2024.

Jouppi et al. (2023)
Jouppi, N., Kurian, G., Li, S., Ma, P., Nagarajan, R., Nai, L., Patil, N., Subramanian, S., Swing, A., Towles, B., et al.

TPUv4 : An optically reconfigurable supercomputer for machine learning with hardware support for embeddings.

In Annual International Symposium on Computer Architecture (ISCA), pp.  1–14, 2023.

Kamradt (2023)
Kamradt, G.

LLMTest_Needle In A Haystack.

https://github.com/gkamradt/LLMTest_NeedleInAHaystack, 2023.

Accessed: 2024-12-14.

Lee et al. (2024)
Lee, W., Lee, J., Seo, J., and Sim, J.

InfiniGen: Efficient generative inference of large language models with dynamic KV cache management.

In 18th USENIX Symposium on Operating Systems Design and Implementation (OSDI), pp.  155–172, 2024.

Li et al. (2023)
Li, D., Shao, R., Xie, A., Sheng, Y., Zheng, L., Gonzalez, J., Stoica, I., Ma, X., and Zhang, H.

How Long Can Context Length of Open-Source LLMs truly Promise?

In NeurIPS 2023 Workshop on Instruction Tuning and Instruction Following, 2023.

Li et al. (2024)
Li, Y., Huang, Y., Yang, B., Venkitesh, B., Locatelli, A., Ye, H., Cai, T., Lewis, P., and Chen, D.

SnapKV: LLM knows what you are looking for before generation.

Conference on Neural Information Processing Systems (Neurips), 2024.

Li et al. (2025)
Li, Y., Jiang, H., Wu, Q., Luo, X., Ahn, S., Zhang, C., Abdi, A. H., Li, D., Gao, J., Yang, Y., et al.

Scbench: A kv cache-centric analysis of long-context methods.

International Conference on Learning Representations (ICLR), 2025.

Ling et al. (2024)
Ling, G., Wang, Z., Yan, Y., and Liu, Q.

SlimGPT: Layer-wise Structured Pruning for Large Language Models.

Conference on Neural Information Processing Systems (Neurips), 2024.

Liu et al. (2024a)
Liu, A., Feng, B., Wang, B., Wang, B., Liu, B., Zhao, C., Dengr, C., Ruan, C., Dai, D., Guo, D., et al.

Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model.

arXiv preprint arXiv:2405.04434, 2024a.

Liu et al. (2024b)
Liu, A., Feng, B., Xue, B., Wang, B., Wu, B., Lu, C., Zhao, C., Deng, C., Zhang, C., Ruan, C., et al.

Deepseek-v3 technical report.

arXiv preprint arXiv:2412.19437, 2024b.

NVIDIA (2024)
NVIDIA.

H100 Tensor Core GPU.

https://www.nvidia.com/en-us/data-center/h100/, 2024.

Accessed: 2025-01-06.

NVIDIA (2025)
NVIDIA.

Dynamo: A datacenter scale distributed inference serving framework.

https://github.com/ai-dynamo/dynamo, 2025.

URL https://github.com/ai-dynamo/dynamo.

Version 0.1.1.

Pawar et al. (2024)
Pawar, S., Tonmoy, S., Zaman, S., Jain, V., Chadha, A., and Das, A.

The What, Why, and How of Context Length Extension Techniques in Large Language Models–A Detailed Survey.

arXiv preprint arXiv:2401.07872, 2024.

PyTorchLabs (2023)
PyTorchLabs.

gpt-fast: Simple and efficient PyTorch-native transformer text generation.

https://github.com/pytorch-labs/gpt-fast, 2023.

Accessed: 2024-12-12.

Qin et al. (2025)
Qin, R., Li, Z., He, W., Zhang, M., Wu, Y., Zheng, W., and Xu, X.

Mooncake: A kvcache-centric disaggregated architecture for llm serving.

USENIX Conference on File and Storage Technologies (FAST 25), 2025.

Ribar et al. (2024)
Ribar, L., Chelombiev, I., Hudlass-Galley, L., Blake, C., Luschi, C., and Orr, D.

SparQ Attention: Bandwidth-Efficient LLM Inference.

In International Conference on Machine Learning (ICML), 2024.

Shazeer (2019)
Shazeer, N.

Fast transformer decoding: One write-head is all you need.

arXiv preprint arXiv:1911.02150, 2019.

Shoeybi et al. (2019)
Shoeybi, M., Patwary, M., Puri, R., LeGresley, P., Casper, J., and Catanzaro, B.

Megatron-LM: Training multi-billion parameter language models using model parallelism.

arXiv preprint arXiv:1909.08053, 2019.

Singhania et al. (2024)
Singhania, P., Singh, S., He, S., Feizi, S., and Bhatele, A.

Loki: Low-Rank Keys for Efficient Sparse Attention.

Conference on Neural Information Processing Systems (Neurips), 2024.

Sun et al. (2024)
Sun, Y., Dong, L., Zhu, Y., Huang, S., Wang, W., Ma, S., Zhang, Q., Wang, J., and Wei, F.

You only cache once: Decoder-decoder architectures for language models.

Conference on Neural Information Processing Systems (Neurips), 2024.

Tang et al. (2025)
Tang, H., Lin, Y., Lin, J., Han, Q., Hong, S., Yao, Y., and Wang, G.

RazorAttention: Efficient kv cache compression through retrieval heads.

International Conference on Learning Representations (ICLR), 2025.

Tang et al. (2024)
Tang, J., Zhao, Y., Zhu, K., Xiao, G., Kasikci, B., and Han, S.

Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference.

In International Conference on Machine Learning (ICML), 2024.

Team et al. (2024)
Team, G., Mesnard, T., Hardin, C., Dadashi, R., Bhupatiraju, S., Pathak, S., Sifre, L., Rivière, M., Kale, M. S., Love, J., et al.

Gemma: Open models based on gemini research and technology.

arXiv preprint arXiv:2403.08295, 2024.

Vaswani et al. (2017)
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I.

Attention Is All You Need.

Conference on Neural Information Processing Systems (Neurips), 2017.

Xiao et al. (2025)
Xiao, G., Tang, J., Zuo, J., Guo, J., Yang, S., Tang, H., Fu, Y., and Han, S.

DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads.

International Conference on Learning Representations (ICLR), 2025.

Xu et al. (2025)
Xu, R., Xiao, G., Huang, H., Guo, J., and Han, S.

Xattention: Block sparse attention with antidiagonal scoring.

arXiv preprint arXiv:2503.16428, 2025.

Ye et al. (2025)
Ye, Z., Chen, L., Lai, R., Lin, W., Zhang, Y., Wang, S., Chen, T., Kasikci, B., Grover, V., Krishnamurthy, A., and Ceze, L.

FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving.

Conference on Machine Learning and Systems (MLSys), 2025.

URL https://arxiv.org/abs/2501.01005.

Yuan et al. (2024)
Yuan, J., Liu, H., Zhong, S., Chuang, Y.-N., Li, S., Wang, G., Le, D., Jin, H., Chaudhary, V., Xu, Z., Zirui, L., and Hu, X.

KV Cache Compression, But What Must We Give in Return? A Comprehensive Benchmark of Long Context Capable Approaches.

Conference on Empirical Methods in Natural Language Processing (EMNLP), 2024.

Zhang et al. (2023)
Zhang, Z., Sheng, Y., Zhou, T., Chen, T., Zheng, L., Cai, R., Song, Z., Tian, Y., Ré, C., Barrett, C., et al.

H2O: Heavy-hitter oracle for efficient generative inference of large language models.

Conference on Neural Information Processing Systems (Neurips), 36:34661–34710, 2023.

Appendix A Detailed Experiment Settings

A.1 Models

We evaluate our methods on the three widely used long-context models: Llama3.1-8B-Ins (AI@Meta, 2024), Mistral-7B-Ins-v0.2 (Jiang et al., 2023), and LongChat-7B-v1.5 (Bai et al., 2024). They are all decoder-only Transformer models (Vaswani et al., 2017). Llama3.1-8B-Ins and Mistral-7B-Ins-v0.2 use GQA, while LongChat-7B-v1.5 uses MHA in the attention module. In terms of sequence length, Llama3.1-8B-Ins supports a maximum sequence length of 128K while the other two support up to 32K sequence length. Prior work (Tang et al., 2024; Chen et al., 2025) usually skips the first two layers during KV cache compression to maintain accuracy. We found that this is only necessary for LongChat-7B-v1.5; so, we conduct KV cache compression on all attention layers for Llama3.1-8B-Ins and Mistral-7B-Ins-v0.2 but skip the first two layers for LongChat-7B-v1.5.

A.2 Benchmarks

Our LongBench and Needle-in-a-Haystack settings mostly follow the prior work (Yuan et al., 2024). For LongBench, we set the maximum prompt length to 127,500 for Llama3.1-8B-Ins and 31,500 for Mistral-7B-Ins-v0.2 and LongChat-7B-v1.5. Prompts beyond the maximum prompt length will be middle-truncated by keeping the first and last half of the input tokens. For Needle-in-a-Haystack, we evaluate with 10 different input sequence lengths uniformly spanning from 2048 to 81,920 words and 10 different depths for each sequence length in Llama3.1-8B-Ins. The maximum word count of 81,920 roughly converts to 109K tokens by the tokenizer in Llama3.1-8B-Ins. For the other two models, the input sequence lengths range from 512 to 20480 words since they support up to 32K sequence length, which convert up to about 30K and 31K tokens for Mistral-7B-Ins-v0.2 and LongChat-7B-v1.5, respectively. For RULER, we mostly follow the configurations in the original benchmark, except for reducing the number of examples per task from 500 to 50 to speed up the evaluation. For SCBench, we follow the multi-turn setting and set the maximum prompt length to 127,500 for Llama3.1-8B-Ins.

A.3 Baselines

Since RocketKV primarily focuses on accelerating the decode phase of LLM inference, we do not perform any KV cache compression or sparse attention mechanism in the prefill phase across all comparing baselines, including DuoAttention, for a fair comparison.

Exact-TopK:
Exact-TopK serves as an oracle method to demonstrate the effectiveness of top-k sparse attention. We assume the top-k KV tokens can be directly identified with no cost so a given token budget will directly correspond to its top-k value.

DuoAttention:
We set the initial and recent tokens to 128 and 512, respectively, for streaming heads if the token budget is larger than 640, and vary the ratio of retrieval heads to match the given token budget on average. If the token budget is lower than 640, all attention heads become streaming heads. In this case, we set the number of initial tokens for the attention sink to 128 if the token budget is larger than 256, otherwise, it is set to 20% of the token budget. The rest of the token budget is assigned to recent tokens within the sliding window.

SnapKV:
We set the observation window size to 32 for all single-turn benchmarks and 128 for multi-turn SCBench. The kernel size for pooling is set to 7, following the SnapKV paper. The token budget is divided by the number of heads per attention group in case of GQA as the SnapKV performs on each attention head separately and the pruned KV cache is not shared within the attention group.

Quest:
We evenly split the token budget between approximate attention for identifying top-k KV token indices and top-k sparse attention so that the token budget can accurately reflect the total memory fetching bandwidth required in the attention module. The original Quest method is not compatible with GQA. We modify it to select indices of top-k accumulated attention scores per attention group rather than per attention head.

SparQ:
Similar to Quest, we evenly split the token budget between approximate attention for identifying top-k KV token indices and top-k sparse attention.

RocketKV/RocketKV-MT:
For SnapKV in the first stage, We set the observation window size to 32 for all single-turn benchmarks and 128 for multi-turn SCBench. For HSA in the second stage, we evenly split the token budget between approximate attention for identifying top-k indices and top-k sparse attention.

Appendix B Additional Results

B.1 Ablation Studies

In this subsection, we present a series of ablation studies to further demonstrate the effectiveness of RocketKV.

(a)LongBench 

(b)NIAH 

(c)RULER, SeqLen = 16K 

(d)RULER, SeqLen= 32K

(e)RULER, SeqLen=64K

(f)RULER, SeqLen=96K

Figure 8: Accuracy comparison among HSA, Quest, and SparQ on Llama3.1-8B-Ins.

(a)LongBench 

(b)NIAH 

(c)RULER, SeqLen=16K

(d)RULER, SeqLen=32K

(e)RULER, SeqLen=64K

(f)RULER, SeqLen=96K

Figure 9: Comparing adaptive against static split factors on Llama3.1-8B-Ins.

B.1.1 Comparing HSA, Quest, and SparQ

To illustrate the effectiveness of hybrid sparse attention (HSA), we compare the accuracy of the standalone HSA mechanism against Quest and SparQ. Figure 8 demonstrates the results on Llama3.1-8B-Ins across multiple different benchmarks. In all cases, HSA consistently outperforms Quest and SparQ, especially at low token budgets. This clearly demonstrates the advantage of HSA, which intelligently leverages approximations in both sequence and head dimensions compared to single dimension approximation methods such as Quest and SparQ.

B.1.2 Split Factor

In this study, we compare the adaptive compression decomposition method against statically determined split factors rr ranging from 0.3 to 0.7. A split factor of 0.5 indicates an even split between the first and second stage of RocketKV. As shown in Figure 9, the best static split factor varies with different sequence lengths and token budgets, while adaptive compression decomposition provides comparable accuracy to the best static split factor in most cases.

B.2 Needle-in-a-Haystack Visualization

Needle-in-a-haystack (NIAH) is a type of synthetic challenge designed to test how effectively an LLM can retrieve specific information in a large volume of text (Kamradt, 2023). In Figures 10, 11,  12, the x-axis shows the document length (i.e., “haystack”), while the y-axis marks the relative position of the “needle” (i.e., a short sentence) within the text. As shown in the results, RocketKV can retrieve the needle with almost the same accuracy as Full-KV throughout the whole text across all three models with token budgets as low as 256.

(a)Token Budget = 256 

(b)Token Budget = 512

(c)Token Budget = 1024 

(d)Token Budget = 2048

(e)Token Budget = 4096

(f)Full-KV

Figure 10: Needle-in-a-Haystack visualization results of RocketKV on Llama3.1-8B-Ins.

(a)Token Budget = 256 

(b)Token Budget = 512

(c)Token Budget = 1024 

(d)Token Budget = 2048

(e)Token Budget = 4096

(f)Full-KV

Figure 11: Needle-in-a-Haystack visualization results of RocketKV on Mistral-7B-Ins-v0.2.

(a)Token Budget = 256 

(b)Token Budget = 512

(c)Token Budget = 1024 

(d)Token Budget = 2048

(e)Token Budget = 4096

(f)Full-KV

Figure 12: Needle-in-a-Haystack visualization results of RocketKV on LongChat-7B-v1.5.

B.3 Detailed Accuracy Results

In this section, we present 20 detailed tables that display the accuracy results discussed in previous sections. These tables offer additional information and insights into the results we captured.

Table 2: Average results of LongBench and NIAH for Llama3.1-8B-Ins

Token Budget

Method

Single QA

Multi. QA

Summ.

Few-shot

Synthetic

Code

LB Avg.

NIAH

N/AFull-KV43.544.529.269.353.962.052.2100.0256Exact-TopK43.644.428.969.553.665.352.6100.0DuoAttention24.433.518.239.051.260.137.620.0SnapKV32.539.120.350.753.056.842.698.3Quest16.014.014.314.44.041.417.810.7SparQ26.318.718.224.515.547.025.710.3HSA41.341.926.864.251.761.149.544.3RocketKV43.743.525.267.353.864.051.1100.0512Exact-TopK43.744.528.869.153.763.152.2100.0DuoAttention27.734.921.647.451.561.741.221.0SnapKV36.041.921.954.853.457.945.299.7Quest27.927.719.838.043.552.635.118.0SparQ37.135.124.553.248.057.343.814.7HSA43.843.228.568.653.165.252.173.7RocketKV43.743.826.869.553.463.551.9100.01024Exact-TopK43.844.629.069.353.561.952.2100.0DuoAttention31.836.423.754.853.364.244.526.3SnapKV38.242.723.559.053.759.647.399.7Quest36.537.524.854.950.957.345.037.3SparQ41.542.928.667.852.062.251.126.0HSA43.944.028.869.754.064.652.594.3RocketKV43.943.828.369.253.463.252.1100.02048Exact-TopK43.644.529.269.553.861.152.1100.0DuoAttention39.340.925.464.552.264.849.228.3SnapKV40.643.425.565.052.861.749.899.7Quest42.543.028.465.552.359.850.564.3SparQ43.543.529.369.453.662.952.156.3HSA43.743.829.269.453.662.352.2100.0RocketKV43.644.028.969.553.962.252.1100.04096Exact-TopK43.544.829.169.353.360.452.0100.0DuoAttention42.441.727.568.953.263.951.236.7SnapKV42.343.726.967.553.461.550.9100.0Quest43.944.328.969.053.560.051.994.3SparQ43.744.029.169.253.163.252.389.3HSA43.944.129.169.453.561.152.1100.0RocketKV43.343.929.069.653.661.151.9100.0
Table 3: Individual results of LongBench for Llama3.1-8B-Ins

Token Budget

Method

narrativeqa

qasper

mul.fieldqa

hotpotqa

2wikimqa

musique

gov-report

qmsum

multi-news

trec

triviaqa

samsum

pass-ret.

lcc

repobench-p

passagecnt

N/AFull-KV30.245.554.955.546.731.335.225.227.272.591.743.899.565.158.88.4256Exact-TopK30.744.755.455.046.531.734.825.126.871.592.244.899.567.163.67.8DuoAttention19.422.831.142.335.922.416.920.617.220.057.439.798.061.259.14.5SnapKV23.727.346.352.340.824.219.222.619.229.084.139.097.557.356.28.6Quest3.022.422.614.923.24.19.812.720.511.517.314.47.549.533.30.5SparQ5.038.035.819.728.87.513.715.025.816.532.124.828.860.134.02.2HSA26.443.554.154.243.727.830.723.226.663.587.042.297.066.356.06.5RocketKV31.043.956.255.245.230.026.624.724.267.591.043.399.065.462.78.7512Exact-TopK30.945.055.155.347.031.034.525.026.971.592.043.999.565.061.17.9DuoAttention23.025.035.144.836.423.622.320.222.434.565.941.799.563.060.43.5SnapKV25.532.350.254.144.227.421.523.021.234.589.440.598.059.756.18.7Quest9.036.538.232.236.414.416.117.725.635.251.227.582.059.745.45.0SparQ13.645.452.143.839.422.225.621.226.749.572.237.992.064.250.54.1HSA30.445.255.853.846.129.833.824.926.970.590.145.299.066.364.27.1RocketKV30.644.855.754.746.530.230.224.725.573.091.843.699.564.862.37.31024Exact-TopK30.845.555.054.748.031.134.725.127.172.591.543.899.564.259.67.5DuoAttention24.130.441.145.339.424.424.521.225.345.576.342.598.566.861.58.0SnapKV28.136.650.056.044.228.023.823.823.144.591.341.399.561.857.48.0Quest15.444.449.848.940.822.927.121.026.457.070.037.999.062.652.02.7SparQ23.146.155.154.742.931.234.024.927.069.589.944.099.565.059.34.5HSA31.145.355.354.246.531.234.624.926.972.592.144.599.566.362.98.5RocketKV30.744.956.054.646.730.033.025.226.672.092.143.599.564.761.87.32048Exact-TopK30.745.354.754.847.231.334.925.427.273.091.544.199.563.858.48.2DuoAttention25.642.350.052.342.128.127.522.126.666.084.942.898.566.163.66.0SnapKV28.839.953.153.946.529.926.024.726.060.092.442.699.563.859.66.0Quest28.045.554.254.344.729.833.124.927.268.584.543.499.563.256.55.1SparQ30.345.254.953.746.530.435.325.427.173.091.244.099.565.360.57.7HSA30.745.255.254.146.231.135.125.127.473.091.244.299.564.360.37.7RocketKV30.645.554.854.547.130.333.925.527.273.591.543.499.564.459.98.24096Exact-TopK30.245.554.855.547.131.835.225.127.272.591.743.799.563.457.57.2DuoAttention26.545.155.555.043.326.731.923.727.073.589.943.399.565.562.37.0SnapKV29.943.853.255.745.729.929.024.926.967.591.743.399.563.959.07.3Quest30.745.555.455.646.031.334.924.827.172.090.944.099.563.356.87.4SparQ30.845.354.954.746.431.034.925.227.272.591.543.799.565.660.76.6HSA31.245.754.754.346.431.634.925.327.272.591.544.299.563.758.67.5RocketKV30.345.354.354.846.330.434.725.027.173.091.544.399.563.758.57.6
Table 4: Average SCBench results for Llama3.1-8B-Ins

Token Budget

Method

Retr.String

Retr.Semantic

Global

Multi-task

Avg.

N/AFull-KV49.540.736.264.649.91024Exact-TopK32.341.036.861.845.0DuoAttention0.126.633.511.620.9SnapKV0.217.034.710.717.6Quest0.022.425.24.015.7SparQ0.019.223.60.913.6HSA4.127.227.220.022.1RocketKV14.322.735.326.226.6RocketKV-MT40.535.736.856.244.32048Exact-TopK38.041.236.662.946.7DuoAttention0.126.633.912.221.2SnapKV1.117.135.912.118.5Quest2.024.426.611.818.8SparQ0.121.125.84.115.5HSA8.435.335.753.434.6RocketKV16.525.035.430.528.8RocketKV-MT42.238.437.059.546.44096Exact-TopK43.442.136.463.848.7DuoAttention0.126.733.912.721.3SnapKV3.519.135.113.219.9Quest8.626.828.523.024.0SparQ3.029.929.230.825.2HSA13.138.736.360.938.6RocketKV18.928.535.933.931.5RocketKV-MT44.839.936.860.347.88192Exact-TopK48.042.436.464.750.2DuoAttention0.127.334.016.522.2SnapKV5.020.335.719.021.9Quest10.131.632.031.928.8SparQ6.841.535.664.138
