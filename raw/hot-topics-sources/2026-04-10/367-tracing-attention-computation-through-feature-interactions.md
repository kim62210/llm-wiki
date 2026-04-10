---
title: Tracing Attention Computation Through Feature Interactions
source_url: https://transformer-circuits.pub/2025/attention-qk/index.html
final_url: https://transformer-circuits.pub/2025/attention-qk/index.html
status: 200
content_type: text/html
topics: [Circuit Tracing & Attribution Graphs]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:13.852416+00:00
---

# Tracing Attention Computation Through Feature Interactions

## 원본 URL

https://transformer-circuits.pub/2025/attention-qk/index.html

## 추출 본문

Tracing Attention Computation Through Feature Interactions
Transformer Circuits Thread

Tracing Attention Computation Through Feature Interactions

We describe and apply a method to explain attention patterns in terms of feature interactions, and integrate this information into attribution graphs.

Authors

Harish Kamath*,Emmanuel Ameisen*,Isaac Kauvar,Rodrigo Luger,Wes Gurnee,Adam Pearce,Sam Zimmerman,Joshua Batson,Thomas Conerly,Chris Olah,Jack Lindsey‡

Affiliations

Anthropic

Published

July 31st, 2025

* Core Research Contributor;‡ Correspondence to jacklindsey@anthropic.com

Transformer-based language models involve two main kinds of computations: multi-layer perceptron (MLP) layers that process information within a context position, and attention layers that conditionally move and process information between context positions. In our recentpapers we made significant progress in breaking down MLP computation into interpretable steps. In this update, we fill in a major missing piece in our methodology, by introducing a way to decompose attentional computations as well. 

Our prior work introduced attribution graphs as a way of representing the forward pass of a transformer as an interpretable causal graph. These graphs were built on top of (cross-layer) transcoders, a replacement for the original model’s MLP layers that use sparsely active “features” in place of the original MLP neurons. The features comprise the nodes of the attribution graphs, and edges in the graphs represent attributions – the influence of a source feature on a target feature in a later layer.

The attribution graphs in our initial work were incomplete, in that they omitted key information about attentional computations. The feature-feature interactions we studied – the edges in the graph – are mediated by attention heads that carry information between context positions. However, we did not attempt to explain why the attention heads attended to a particular context position. In many cases, this has prevented us from understanding the crux of how models perform a given task.

In this update, we describe a method to address this issue by extending attribution graphs so they can explain attention patterns. Our method is centered on “QK attributions,” which describe attention head scores as a bilinear function of feature activations on the respective query and key positions. We also describe a way to integrate this information into attribution graphs, by computing the contribution of different attention heads to graph edges.

We provide several case studies of this method in action. Some of these examples confirmed existing hypotheses we described in Biology, which we could not validate at the time:

In an induction prompt, the query-side “X” features interact with key-side “preceded by X” features to cause induction heads to attend to the appropriate token.

In a prompt where the model is asked for the opposite of a word, key-side features “tag” the relevant word so that query-side “opposite” features can find it at the appropriate time.

In a multiple choice question, we confirm that interactions between “answer a multiple choice question” features and “correct answer” features cause “correct answer” attention heads to attend to the appropriate option.

We also surfaced new, unexpected mechanisms:

How “concordance/discordance heads” are used to sanity-check statements. 

How attentional circuits employ many computations and heuristics operating in parallel, even in simple contexts. Some examples:

In our induction prompt, the core induction mechanism coexists with a general “attend to names” mechanism.

In the multiple choice prompt, the core “find the correct answer” mechanism is complemented by an “attend to any answer at all” mechanism.

The case studies here are our first attempts at applying the method, and we expect more discoveries to result in future work.

We believe the addition of QK attributions is a significant qualitative improvement on our original attribution graphs, unlocking analyses that were previously impossible. However, there remain many open research questions regarding attentional circuits, which we describe at the end of the post.

The problem: transcoder-based attribution graphs omit attentional computations

Transcoders only ever read and write information within the same context position – however, transformer models also contain attention layers, which carry information across context positions. Thus, the influence between any two transcoder features is mediated by attention layers For features in different context positions, all of the interaction is attention-mediated. For features in the same context position, some of the interaction is direct, and some is mediated by attention to the same position. 

To make attribution a clearly defined operation, we designed our attribution graphs so that interactions between features are linear. One of the key tricks in doing this is to freeze the attention patterns, treating them as a constant linear operation (and ignoring why they have those attention patterns). This allows us to trace the effect of one feature on another through attention heads. This could potentially involve multiple attention heads operating in parallel, and also compositions of attention heads. The resulting attribution is a sum of attributions corresponding to the features being mediated by different sequences of attention heads.

But freezing attention patterns and summing over heads like this means our attribution graphs are “missing” key information about attentional computation, in two respects:

The graphs left it ambiguous which (sequences of) heads were strongly involved in mediating a given edge.

Even if we did identify the important heads, we failed to explain the mechanisticsource of each head’s attention pattern – how the QK circuit of each head gave rise to its pattern. Indeed, by conditioning on attention patterns when computing gradients, our graphs ignored QK circuits entirely.

In our original paper, we pointed out that for many prompts, this missing QK information renders attribution graphs useless. In particular, for many prompts, the question of which head(s) mediated an edge, and why those heads attended where they did, is the crux of the computation. We provide several examples of this failure mode later in the paper and demonstrate how our method fills in the missing information.

High-level strategy

Explaining the source of an attention head’s attention pattern. The core insight underlying our method is the fact that attention scores (prior to softmax) are a bilinear function of the residual stream at the query and key positions. Thus, if we have a decomposition of the residual stream as a sum of feature components, we can rewrite the attention scores as a sum of dot products between feature-feature pairs (one on the query position, one on the key position). We call this decomposition “QK attribution” and describe in more detail how we compute it below. Note that the same strategy was used by and to analyze QK circuits, but explored in less depth.

Explaining how attention heads participate in attribution graphs. Explaining the source of each head’s attention scores is insufficient on its own; we also must understand how the heads participate in our attribution graphs. To do so, for each edge in an attribution graph, we keep track of the extent to which that edge was mediated by different attention heads. To achieve this, (cross-layer) transcoders on their own are not adequate; we explain this issue and how to resolve it below.

QK attributions

QK attributions are intended to explain why each head attended where it did. In this section, we assume that we have trained sparse autoencoders (SAEs) on the residual stream of each layer of the model (though there are alternative strategies we could use; see below).

In a standard attention layer, a head’s attention score at positions (p_k, p_q) is produced by taking the dot product of linear transformations of the residual stream at these positionsIn this update we focus on describing the QK attributions logic for vanilla attention layers. In some attention variants, this assumption does not quite hold – for instance, the commonly used rotary positional embeddings involve modifying the linear transformation depending on the context position, and thus attention scores will be influenced by positional information not present in the residual stream. In general, however, the basic premise of QK attributions can be extended to all common attention architectures we are aware of. To simplify things, we introduce a matrix W_{QK} = W_Q^T W_K (see discussion in the Framework paper). We simply expand the key and query activations to describe them in terms of feature activations (along with a bias and residual error), and then multiply out the bilinear interaction:

The sum of these terms adds up to the attention score.

Note that in some architectures, there may exist a normalization step between the residual stream and the linear transformations W_Q and W_K. In this case, the feature vectors should first be transformed by linearization of the normalization layer before being used in the above formulae. If the normalization layer involves a bias term, it can be folded into the bias term above.

Once we have computed these terms, we can simply list them ordered by magnitude. Each term is an interaction between a query-side and key-side component, which can be listed side-by-side. For feature components, we label them with their feature description and make them hoverable in our interactive UI so that their “feature visualization” can be easily viewed.
An illustration of how we visualize QK attributions. In a circuits graph, for any edge that crosses context positions, we can use the head loadings of that edge to index into a specific (query ctx, key ctx, layer, head) position, and then use the (un)marginalized list of features to inspect the QK circuit.
One limitation of this approach is that it does not directly explain the attention pattern itself, which involves competition between the attention scores at multiple context positions – to explain why an attention head attended to a particular position, it may be important to understand why it didn’t attend to other positions. Our method gives us information about QK attributions at all context positions, including negative attributions, so we do have access to this information (and we highlight some interesting inhibitory effects in some of our later examples). However, we do not yet have a way of automatically surfacing the important inhibitory effects without manual inspection. While addressing this limitation is an important direction for future work, we nevertheless find that our attention score decompositions can be interpretable and useful.

Computing attention head contributions to an attribution graph

QK attributions help us understand the source of each head’s attention pattern. For this understanding to be useful to us, we need to understand what these attention patterns were used for. Our strategy is to enrich our attribution graphs with “head loadings” for each edge, which tell us the contributions that each attention head made to that edge.

“Checkpointing” attention paths with features

It turns out that computing the contributions of attention heads to graph edges is difficult to achieve with transcoder-based attribution graphs. This is because when transcoder features are separated by L layers, the number of possible attention head paths between them grows exponentially with LNote that this issue is not resolved by using cross-layer transcoders. Thus, it is computationally difficult Though potentially an interesting problem for future work – plausibly a search algorithm could be used to identify important paths. to decompose edges in transcoder-based attribution graphs into their contributions from each path.

We can sidestep this issue by using a method that forces each edge in a graph to be mediated only by attention head paths of length 1. This can be achieved using several different strategies, which we have experimented with:

By using Multi-Token Transcoders (MTCs), a transcoder-like replacement for attention layers. MTC features are “carried” by (linear combinations of) attention heads, rather than paths through multiple attention heads, and thus do not suffer the exponential-number-of-paths issue.

By training SAEs on the output of each attention layer, and including these features as nodes in attribution graphs alongside (cross-layer) transcoder features. This “checkpoints” attributions through each attention layer, eliminating all attention head paths of length greater than 1.

By training SAEs on the residual stream at each layer of the model, and computing gradient attributions between features at adjacent layers. This also “checkpoints” attributions at each layer in the same way as the previous options.

In practice, instead of SAEs at each residual stream layer, we compute these graphs using weakly causal crosscoders (WCCs), whose features read from the residual stream at a residual stream layer L, and reconstruct the residual stream at layers L, L+1, …, num_layers Note that WCCs are not intended to replace nonlinear model computation, but rather to decompose representations (like SAEs) while also capturing information that is linearly propagated across layers.. Given a target feature in a layer K, we compute gradients from its layer-K decoder vector to the layer K−1 residual stream, and compute the dot product of this gradient with source feature projections (activation times decoder vector) in layers K−1. However, those decoders may belong to features that originated at earlier layers, allowing us to “hop back” across layers and avoid long chains of redundant features (similar to the motivation for cross-layer transcoders).

For now, we have adopted the third strategy. The other two methods accumulate error in the residual stream across layers, which we have found leads to greater overall reconstruction errors, resulting in attributions that are dominated by error nodes. Note, however, that this choice has a tradeoff, which is that our attributions through MLP layers are no longer linear as they are in transcoder-based attribution graphs. As a result, we run the risk of attributions being uninterpretable, or highly “local” to the specific input prompt. In subsequent exposition, we will describe our algorithm as applied to residual stream SAE-based graphs (the extension to WCCs is straightforward).

It’s important to note that an edge may still be mediated by multiple heads at a given layer! However, it can no longer be mediated by chains of heads across multiple layers.

Head loadings

Once we have trained SAEs (or a suitable alternative) as described above, we can compute attention head loadings for graph edges – the amount that each head is responsible for mediating that edge. Any edge between two SAE features in adjacent layers is a sum of three terms: an attention-mediated component, an MLP-mediated component, and a residual connection-mediated component. 

Let source and target feature at positions p_s and p_t, with activations a_s and a_t, and feature vectors \mathbf{v_s} and \mathbf{v_t}The feature vectors correspond to the decoder weights of the SAE. When making attribution graphs with SAEs, unlike transcoders, we ignore the SAE encoders. The encoders in transcoder-based graphs correspond to weights of a “replacement model,” but in SAE-based graphs they have no such interpretation, and we think of them as just a tool to infer feature activations.. The attention-mediated component can be written as follows.

\sum_{h \in \text{heads}} a_s a_t \left(\mathbf{v_t}^\top O_h V_h \mathbf{v_s}\right) \cdot \text{attention}_h(p_s, p_t)

The sum over heads runs over all the heads in the source feature’s layer (which is one layer prior to the target feature’s). Each term in this sum represents the contribution (head loading) of a specific attention head to this edge. We compute and store these terms separately and surface them in our UI .

Examples

In this section, we will show how head loadings and QK attributions can be used to understand attentional computations that were missing in our previous work.

Induction

Claude 3.5 Haiku completes the prompt:

I always loved visiting Aunt Sally. Whenever I was feeling sad, Aunt

with “Sally”. In our original paper, the attribution graph for this prompt shows a strong direct edge from “Sally” features (on the “Sally” token) to the “Sally” logit on the final token. In other words, the model said “Sally” because it attended to the “Sally” token. This is not a useful explanation of the model’s computation! In particular, we’d like to know why the model attended to the Sally token and not some other token.
