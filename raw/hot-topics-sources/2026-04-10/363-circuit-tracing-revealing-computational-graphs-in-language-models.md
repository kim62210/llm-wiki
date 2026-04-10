---
title: Circuit Tracing: Revealing Computational Graphs in Language Models
source_url: https://transformer-circuits.pub/2025/attribution-graphs/methods.html
final_url: https://transformer-circuits.pub/2025/attribution-graphs/methods.html
status: 200
content_type: text/html
topics: [Circuit Tracing & Attribution Graphs]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:12.979198+00:00
---

# Circuit Tracing: Revealing Computational Graphs in Language Models

## 원본 URL

https://transformer-circuits.pub/2025/attribution-graphs/methods.html

## 추출 본문

Circuit Tracing: Revealing Computational Graphs in Language Models

×

Transformer Circuits Thread

Circuit Tracing: Revealing Computational Graphs in Language Models

Circuit Tracing: Revealing Computational Graphs in Language Models

We introduce a method to uncover mechanisms underlying behaviors of language models. We produce graph descriptions of the model’s computation on prompts of interest by tracing individual computational steps in a “replacement model”. This replacement model substitutes a more interpretable component (here, a “cross-layer transcoder”) for parts of the underlying model (here, the multi-layer perceptrons) that it is trained to approximate. We develop a suite of visualization and validation tools we use to investigate these “attribution graphs” supporting simple behaviors of an 18-layer language model, and lay the groundwork for a companion paper applying these methods to a frontier model, Claude 3.5 Haiku.

Authors

Emmanuel Ameisen*,Jack Lindsey*,Adam Pearce*,Wes Gurnee*,Nicholas L. Turner*,Brian Chen*,Craig Citro*,

David Abrahams,Shan Carter,Basil Hosmer,Jonathan Marcus,Michael Sklar,Adly Templeton,

Trenton Bricken,Callum McDougall◊,Hoagy Cunningham,Thomas Henighan,Adam Jermyn,Andy Jones,Andrew Persic,Zhenyi Qi,T. Ben Thompson,

Sam Zimmerman,Kelley Rivoire,Thomas Conerly,Chris Olah,Joshua Batson*‡

Affiliations

Anthropic

Published

March 27, 2025

* Core Contributor;‡ Correspondence to joshb@anthropic.com;◊ Work performed while at Anthropic;Author contributions statement below.

Contents

Introduction

Building an Interpretable Replacement Model

Architecture

From Cross-Layer Transcoder to Replacement Model

The Local Replacement Model

Attribution Graphs

Constructing an Attribution Graph for a Prompt

Learning from Attribution Graphs

Understanding and Labeling Features

Grouping Features into Supernodes

Validating Attribution Graph Hypotheses with Interventions

Localizing Important Layers

Factual Recall Case Study

Addition Case Study

Global Weights

Global Weights in Addition

Evaluations

Cross-Layer Transcoder Evaluation

Attribution Graph Evaluation

Evaluating Mechanistic Faithfulness

Biology

Limitations

Discussion

Related Work

Acknowledgments

Author Contributions

Citation Information

CLT Implementation Details

Attribution Graph Computation

Graph Pruning

Validating the Replacement Model

Nuances of Steering with Cross-Layer Features

Unexplained Variance and Choice of Steering Factors

Similar Features and Supernodes

Iterative Patching

Details of Interventions

Notes on the Interface

Residual Stream Norms Growth

Interference Weights over More Features

Number Output Weights for Select Features

Comparison of Addition Features Between Small and Large Models

Additional Evaluation Details

Prompt and Graph Lists

Introduction

Deep learning models produce their outputs using a series of transformations distributed across many computational units (artificial “neurons”). The field of mechanistic interpretability seeks to describe these transformations in human-understandable language. To date, our team’s approach has followed a two-step approach. First, we identify features, interpretable building blocks that the model uses in its computations. Second, we describe the processes, or circuits, by which these features interact to produce model outputs.

A natural approach is to use the raw neurons of the model as these building blocks.An alternative approach is to study the roles of gross model components such as entire MLP blocks and attention heads . This approach has identified interesting roles these components play in specific behaviors, but large components play a multitude of unrelated roles across the data distribution, so we seek a more granular decomposition. Using this approach, previous work successfully identified interesting circuits in vision models, built out of neurons that appear to represent meaningful visual concepts . However, model neurons are often polysemantic — representing a mixture of many unrelated concepts. One reason for polysemanticity is thought to be the phenomenon of superposition, in which models must represent more concepts than they have neurons, and thus must “smear” their representation of concepts across many neurons. This mismatch between the network's basic computational units (neurons) and meaningful concepts has proved a major impediment to progress to the mechanistic agenda, especially in understanding language models.

In recent years, sparse coding models such as sparse autoencoders (SAEs) , transcoders , and crosscoders have emerged as promising tools for identifying interpretable features represented in superposition. These methods decompose model activations into sparsely active components (“features”),We use 'feature' following the tradition of 'feature detectors' in neuroscience and 'feature learning' in machine learning. Some recent literature uses the term 'latent,' which refers to specific vectors in the model's latent space. We find 'feature' better captures the computational role these elements play, making it more appropriate for describing transcoder neurons than SAE decoder vectors. which turn out in many cases to correspond to human-interpretable concepts. While current sparse coding methods are an imperfect way of identifying features (see § Limitations), they produce interpretable enough results that we are motivated to study circuits composed of these features. Several authors have already made promising steps in this direction .

Although the basic premise of studying circuits built out of sparse coding features sounds simple, the design space is large. In this paper we describe our current approach, which involves several key methodological decisions:

Transcoders. We extract features using a variant of transcoders rather than SAEs, which allows us to construct an interpretable “replacement model” that can be studied as a proxy for the original model. Importantly, this approach allows us to analyze direct feature-feature interactions.

Cross-Layer. We base our analysis on cross-layer transcoders (CLT) , in which each feature reads from the residual stream at one layer and contributes to the outputs of all subsequent MLP layers of the original model, which greatly simplifies the resulting circuits. Remarkably, we can substitute our learned CLT features for the model's MLPs while matching the underlying model's outputs in ~50% of cases.

Attribution Graphs. We focus on studying “attribution graphs” which describe the steps a model used to produce an output for a target token on a particular prompt, using an approach similar to Dunefsky et al. . The nodes in the attribution graph represent active features, token embeddings from the prompt, reconstruction errors, and output logits. The edges in the graph represent linear effects between nodes, so the activity of each feature is the sum of its input edges (up to its activation threshold) (see § Attribution Graphs).

Linear Attribution Between Features. We design our setup so that, for a specific input, the direct interactions between features are linear. This makes attribution a well-defined, principled operation. Crucially, we freeze attention patterns and normalization denominators (following ) and use transcoders to achieve this linearity.Direct feature-feature interactions are linear because transcoder features “bridge over” the MLP nonlinearities, replacing their computation, and because we've frozen the remaining nonlinearities: attention patterns and normalization denominators. It's worth noting that strictly we mean that the pre-activation of a feature is linear with respect to the activations of earlier features.
Freezing attention patterns is a standard approach which divides understanding transformers into two steps: understanding behavior given attention patterns, and understanding why the model attends to those positions. This approach was explored in depth for attention models in A Mathematical Framework, which also discussed a generalization to MLP layers which is essentially the approach used in this paper. Note that factoring out understanding attention patterns in this way leads to the issues with attention noted in § Limitations: Missing Attention Circuits. However, we can then also take the same solution Framework takes of studying QK circuits. Features also have indirect interactions, mediated by other features, which correspond to multi-step paths.

Pruning. Although our features are sparse, there are still too many features active on a given prompt to easily interpret the resulting graph. To manage this complexity, we prune graphs by identifying the nodes and edges which most contribute to the model’s output at a specific token position (see § Appendix: Graph Pruning). Doing so allows us to produce sparse, interpretable graphs of the model’s computation for arbitrary prompts.

Interface. We designed an interactive interface for exploring attribution graphs, and the features they're composed of, that allows a researcher to quickly identify and highlight key mechanisms within them.

Validation. Our approach to studying circuits is indirect – our replacement model may use different mechanisms from the underlying model. Thus, it is important that we validate the mechanisms we find in attribution graphs. We do so using perturbation experiments. Specifically, we measure the extent to which applying perturbations in a feature's direction produces changes to other feature activations (and to the model's output) that are consistent with the attribution graph. We find that across prompts, perturbation experiments are generally qualitatively consistent with our attribution graphs, though there are some deviations.

Global Weights. While our paper mostly focuses on studying attribution graphs for individual prompts, our methods also allow us to study the weights of the replacement model (“global weights”) directly, which underlie mechanisms across many prompts. In § Global Weights, we demonstrate some challenges with doing so – naive global weights are often less interpretable than attribution graphs due to weight interference. However, we successfully apply them to understand the circuits underlying small number addition.

The goal of this paper is to describe and validate our methodology in detail, using a few case studies for illustration.

We begin with methods. We describe the setup of our replacement model (§ Building an Interpretable Replacement Model) and how we construct attribution graphs (§ Attribution Graphs), concluding with two case studies (§ Factual Recall Case Study, § Addition Case Study). We then go on to explore approaches to constructing global circuits, including challenges and some preliminary methods for addressing them (§ Global Weights).

We then provide a detailed quantitative evaluation of our cross-layer transcoders and the resulting attribution graphs (§ Evaluations), showing metrics by which CLTs provide Pareto-improvements over neurons and per-layer transcoders. Afterwards, we provide an overview of our companion paper, in which we apply our method to various behaviors of Claude 3.5 Haiku (§ Biology). We follow with a discussion of methodological limitations (§ Limitations). These include the role of attention patterns, the impact of reconstruction errors, the identification of suppression motifs, and the difficulty of understanding global circuits. Addressing these limitations, and seeing what additional model mechanisms are then revealed, is a promising direction for future work.

We close with a broader discussion (§ Discussion) of the design space of methods for producing attribution graphs – parts of our approach can be freely remixed with others while retaining much of the benefit – and a review of related work (§ Related Work).

Our companion paper, On the Biology of a Large Language Model, applies these methods to Claude 3.5 Haiku, investigating a diverse range of behaviors such as multiple hop reasoning, planning, and hallucinations.

We note that training a cross-layer transcoder can incur significant up-front cost and effort, which is amortized over its application to circuit discovery. We have found that this improves circuit interpretability and parsimony enough to justify the investment (see cost estimates for open-weights models and discussion of cost-matched performance relative to per-layer transcoders). Nevertheless, we stress that alternatives like per-layer transcoders or even MLP neurons can be used instead (keeping the same steps 3–8 above), and still produce useful insights. Moreover, it is likely that better methods than CLTs will be developed in the future. 

To aid replication, we share guidance on CLT implementation, details on the pruning method, and the front-end code supporting the interactive graph analysis interface.

Building an Interpretable Replacement Model

Architecture

A cross-layer transcoder (CLT) consists of neurons (“features”) divided into L layers, the same number of layers as the underlying model. The goal of the model is to reconstruct the outputs of the MLPs of the underlying model, using sparsely active features. The features receive input from the model’s residual stream at their associated layer, but are “cross-layer” in the sense that they can provide output to all subsequent layers.Other architectures besides CLTs can be used for circuit analysis, but we’ve empirically found this approach to work well. Concretely:

Each feature in the \ell^\text{th} layer “reads in” from the residual stream at that layer using a linear encoder followed by a nonlinearity.

An \ell^\text{th} layer feature contributes to the reconstruction of the MLP outputs in layers \ell, \ell+1,\ldots , L, using a separate set of linear decoder weights for each output layer.

All features in all layers are trained jointly. As a result, the output of the MLP in a layer \ell^\prime is jointly reconstructed by the features from all previous layers.

More formally, to run a cross-layer transcoder, let \mathbf{x^{\ell}} denote the original model’s residual stream activations at layer \ell. The CLT feature activations \mathbf{a^{\ell}} at layer \ell are computed as

\mathbf{a^{\ell}} = \text{JumpReLU}\!\left(W_{enc}^{\ell} \mathbf{x^{\ell}}\right)

where W_{enc}^{\ell} is the CLT encoder matrix at layer \ell.

We let \mathbf{y^{\ell}} refer to the output of the original model’s MLP at layer \ell. The CLT’s attempted reconstruction \mathbf{\hat{y}^{\ell}} of \mathbf{y^{\ell}} is computed using the JumpReLU activation function as:

\mathbf{\hat{y}^{\ell}} = \sum_{\ell'=1}^{\ell} W_{dec}^{\ell' \to \ell} \mathbf{a^{\ell'}}

where W_{dec}^{\ell' \to \ell} is the CLT decoder matrix for features at layer \ell' outputting to layer \ell.

To train a cross-layer transcoder, we minimize a sum of two loss functions. The first is a reconstruction error loss, summed across layers:

L_\text{MSE} = \sum_{\ell=1}^L \|\mathbf{\hat{y}^{\ell}} - \mathbf{y^{\ell}} \|^2

The second is a sparsity penalty (with an overall coefficient \lambda, a hyperparameter, and another hyperparameter c) summed across layers:

L_\text{sparsity} = \lambda\sum_{\ell=1}^L \sum_{i=1}^N \textrm{tanh}(c \cdot \|\mathbf{W_{dec, i}^{\ell}}\| \cdot a^{\ell}_i)

Where N is the number of features per layer and \mathbf{W_{dec, i}^{\ell}} is the concatenation of all decoder vectors of feature i.

We trained CLTs of varying sizes on a small 18-layer transformer model (“18L”)18L has no MLP in layer 0, so our CLT has 17 layers., and on Claude 3.5 Haiku. The total number of features across all layers ranged from 300K to 10M features (for 18L) and from 300K to 30M features (for Haiku). For more training details see § Appendix: CLT Implementation Details.

From Cross-Layer Transcoder to Replacement Model

Given a trained cross-layer transcoder, we can define a “replacement model” that substitutes the cross-layer transcoder features for the model’s MLP neurons – that is, where each layer's MLP output is replaced by its reconstruction by all CLTs that write to that layer. Running a forward pass of this replacement model is identical to running the original model, with two modifications:

Upon reaching the input to the MLP in layer \ell, we compute the activations of the cross-layer transcoder features whose encoders live in layer \ell.

Upon reaching the output of the MLP in layer \ell, we overwrite it with the summed outputs of the cross-layer transcoder features in this and previous layers, using their decoders for layer \ell.

Attention layers are applied as usual, without any freezing or modification. Although our CLTs were only trained using input activations from the underlying model, “running” the replacement model involves running CLTs on "off-distribution" input activations from intermediate activations from the replacement model itself.

As a simple evaluation, we measure the fraction of completions for which the most likely token output of the replacement model matches that of the underlying model. The fraction improves with scale, and is better for CLTs compared to a per-layer transcoder baseline (i.e., each layer has a standard single layer transcoder trained on it; the number of features shown refers to the total number across all layers). We also compare to a baseline of thresholded neurons, varying the threshold below which neurons are zeroed out (empirically, we find that higher neuron activations are increasingly interpretable, and we indicate below where their interpretability roughly matches that of features according to our auto-evaluations in § Quantitative CLT Evaluations). Our largest 18L CLT matches the underlying model’s next-token completion on 50% of a diverse set of pretraining-style prompts from an open source dataset (see § Additional Evaluation Details).We use a randomly sampled set of prompts and target tokens, restricting to those which the model predicts correctly, but with a confidence lower than 80% (to filter out “boring” tokens). 

The Local Replacement Model

While running the replacement model can sometimes reproduce the same outputs as the underlying model, there is still a significant gap, and reconstruction errors can compound across layers. Since we are ultimately interested in understanding the underlying model, we would like to approximate it as closely as possible. To that end, when studying a fixed prompt p, we construct a local replacement model, which

Substitutes the CLT for the MLP layers (as in the replacement model);

Uses the attention patterns and normalization denominators from the underlying model's forward pass on p (as in );

Adds an error adjustment to the CLT output at each (token position, layer) pair equal to the difference between the true MLP output on p and the CLT output on p (as in ).

After this error adjustment and freezing of attention and normalization nonlinearities, we've effectively re-written the underlying model's computation on the prompt p in terms of different basic units; all of the error-corrected replacement model's activations and logit outputs exactly match those of the underlying model. However, this does not guarantee that the local replacement model and underlying model use the same mechanisms. We can measure differences in mechanism by measuring how differently these models respond to perturbations; we refer to the extent to which perturbation behavior matches as “mechanistic faithfulness”, discussed in § Evaluating Mechanistic Faithfulness.This is similar in spirit to a Taylor approximation of a function f at a point a; both agree locally in a neighborhood of a but diverge in behavior as you move away.

The local replacement model can be viewed as a very large fully connected neural network, spanning across tokens, on which we can do classic circuit analysis:

Its input is the concatenated set of one-hot vectors for each token in the prompt.

Its neurons are the union of the CLT features active at every token position.

Its weights are the summed interactions over all the linear paths from one feature to another, including via the residual stream and through attention, but not passing through MLP or CLT layers. Because attention patterns and normalization denominators are frozen, the impact of a source feature's activation on a target feature's pre-activation via each path is linear in the activation of the source feature. We sometimes refer to these as "virtual weights" because they are not instantiated in the underlying model.

Additionally, it has bias-like nodes corresponding to error terms, with a connection from each bias to each downstream neuron in the model.

The only nonlinearities in the local replacement model are those applied to feature preactivations.

The local replacement model serves as the basis of our attribution graphs, where we study the feature-feature interactions of the local replacement model on the prompt for which it was made. These graphs are the primary object of study of this paper.

Attribution Graphs

We will introduce our methodology for constructing attribution graphs while working through a case study regarding the model’s ability to write acronyms for arbitrary titles. In the example we study, the model successfully completes a fictional acronym. Specifically, we give the model the prompt The National Digital Analytics Group (N and sample its completion: DAG). The tokenizer the model was trained with uses a special “Caps Lock” token, which means the prompt and completion are tokenized as follows: 
The

National

Digital

Analytics

Group

 (

⇪

n

dag
.

We explain the computation the model performs to output the “DAG” token by constructing an attribution graph showing the flow of information from the prompt through intermediary features and to that output.Due to the “Caps Lock” token, the actual target token is “dag”. We write the token in uppercase here and in the rest of the text for ease of reading. Below, we show a simplified diagram of the full attribution graph. The diagram shows the prompt at the bottom and the model’s completion on top. Boxes represent groups of similar features, and can be hovered over to display each feature’s visualization. We discuss our interpretation of features in § Understanding and Labeling Features. Arrows represent the direct effect of a group of features or a token on other features and the output logit. 

The graph for the acronym prompt shows three main paths, originating from each of the tokens that compose the desired acronym. Paths originate from features for a given word, promoting features about “saying the first letter of that word in the correct position”, which themselves have positive edges to a “say DAG” feature and the logit. “say X” labels describe “output features”, which promote a specific token X, and arbitrary single letters are denoted with underscores. The “Word → say _W” edges represent attention heads’ OV circuits writing to a subspace that is then amplified by MLPs at the target position. Each group of features also has a direct edge to the logit in addition to the sequential paths, representing effects mediated only via attention head OVs (i.e., paths to the output in the local replacement model that don’t “touch” another MLP layer). 

In order to output “DAG”, the model also needs to decide to output an acronym, and to account for the fact that the prompt already contains N, and indeed we see features for “in an acronym” and “in an N at the start of an acronym” with positive edges to the logit. The word National has minimal influence on the logit. We hypothesize that this is due to its main contribution being through influencing attention patterns, which our method does not explain (see § Limitations: Missing Attention Circuits).

 In the rest of this section, we explain how we compute and visualize attribution graphs.

Constructing an Attribution Graph for a Prompt

To interpret the computations performed by the local replacement model, we compute a causal graph that depicts the sequences of computational steps it performs on a particular prompt. The core logic by which we construct the graph is essentially the same as that of Dunefsky et al., extended to handle cross-layer transcoders. Our graphs contain four types of nodes:

The output nodes correspond to candidate output tokens. We only construct output nodes for the tokens required to reach 95% of the probability mass, up to a total of 10.We chose this threshold arbitrarily. Empirically, fewer than three logits are required to capture 95% of the probability in the cases we study.

The intermediate nodes correspond to active cross-layer transcoder features at each prompt token position.

The primary input nodes of the graph correspond to the embeddings of the prompt tokens. 

Additional input nodes (“error nodes”) correspond to the portion of each MLP output in the underlying model left unexplained by the CLT.

Edges in the graph represent direct, linear attributions in the local replacement model. Edges originate from feature, embedding, and error nodes, and terminate at feature and output nodes. Given a source feature node s and a target feature node t, the edge weight between them is defined to be A_{s\rightarrow t} := a_sw_{s \rightarrow t}, where w_{s \rightarrow t} is the (virtual) weight in the local replacement model viewed as a fully connected neural network and a_s is the activation of the source feature.Alternatively, w_{s \rightarrow t} is the derivative of the preactivation of t with respect to the source feature activation, with stop-gradients on all non-linearities in the local replacement model.

In terms of the underlying model, w_{s \rightarrow t} is a sum over all linear paths (i.e., through attention head OVs and residual connections) connecting the source feature's decoder vectors to the target feature's encoder vector.

We now give details on how to efficiently compute these in practice, using backwards Jacobians. Let s be a source feature node at layer \ell_s and context position c_s and let t be a target feature node at layer \ell_t and context position c_t. We write J_{c_s, \ell_s \rightarrow c_t, \ell_t}^{\blacktriangledown} for the Jacobian of the underlying model with a stop-gradient operation applied to all model components with nonlinearities – the MLP outputs, the attention patterns, and normalization denominators – on a backwards pass on the prompt of interest, from the residual stream at context position c_t and layer \ell_t to the residual stream at context position c_s and layer \ell_s. The edge weight from s to t is then

A_{s \rightarrow t} = a_s w_{s \rightarrow t} = a_s \sum_{\ell_s \leq \ell < \ell_t} (W_{\text{dec}, \;s}^{\ell_s \to \ell})^T J_{c_s, \ell \rightarrow c_t, \ell_t}^{\blacktriangledown} W_{\text{enc}, \;t}^{\ell_t},

where

W_{\text{dec}, \;s}^{\ell_s \to \ell} is the decoder vector of the feature for s writing to layer \ell,

W_{\text{enc}, \;t}^{\ell_t} is the encoder vector of the feature for s.

The formulas for the other edge types are similar, e.g., an embedding-feature edge weight is given by w_{s \rightarrow t} = \text{Emb}_s^TJ_{c_s, \ell_s \rightarrow c_t, \ell_t}^{\blacktriangledown} W_{\text{enc}, \;t}^{\ell_t}. Note that error nodes have no input edges. For all such formulas, and an expansion of the Jacobian in terms of paths in the underlying model, see § Appendix: Attribution Graph Computation.)

Because we have added stop-gradients to all model nonlinearities in the computation above, the preactivation h_t of any feature node t is simply the sum of its incoming edges in the graph: h_t = \sum_\mathcal{S_t} w_{s \rightarrow t} where S_t is the set of nodes at earlier layers and equal or earlier context positions as t. Thus the attribution graph edges provide a linear decomposition of each feature's activity.

Note that these graphs do not contain information about the influence of nodes on other nodes via their influence on attention patterns, but do contain information about node-to-node influence through the outputs of frozen attention. In other words, we account for the information which flows from one token position to another, but not why the model moved that information.That is, our model ignores the "QK-circuits" but captures the "OV-circuits". Note also that the outgoing edges from a cross-layer feature aggregate the effect of its decodings at all of the layers that it writes to on downstream features.

While our replacement model features are sparsely active (on the order of a hundred active features per token position), attribution graphs are too large to be viewed in full, particularly as prompt length grows – the number of edges can grow to the millions even for short prompts. Fortunately, a small subgraph typically accounts for most of the significant paths from the input to the output.

To identify such subgraphs, we apply a pruning algorithm designed to preserve nodes and edges that directly or indirectly exert significant influence on the logit nodes. With our default parameters, we typically reduce the number of nodes by a factor of 10, while only reducing the behavior explained by 20%. See § Appendix: Graph Pruning for methodological details of our algorithms and metrics.

Learning from Attribution Graphs

Even following pruning, attribution graphs are quite information-dense. A pruned graph often contains hundreds of nodes and tens of thousands of edges – too much information to interpret all at once. To allow us to navigate this complexity, we developed an interactive attribution graphs visualization interface. The interface is designed to enable “tracing” key paths through the graph, retain the ability to revisit previously explored nodes and paths, and materialize the information needed to interpret features on an as-needed basis.

Below we show the interactive visualization for the attribution graph attributing back from the single token “DAG”:

The interface is interactive. Nodes can be hovered over and clicked on to display additional information. Subgraphs can also be constructed by using Cmd/Ctrl+Click to select a subset of nodes. In the subgraph, features can be aggregated into groups we call supernodes (motivated below in § Grouping Features into Supernodes).

Understanding and Labeling Features

We use feature visualizations similar to those shown in our previous work, Scaling Monosemanticity, in order to manually interpret and label individual features in our graph.We sometimes used labels from our automated interpretability pipeline as a starting point, but generally found human labels to be more reliable.

The easiest features to label are input features, which activate on specific tokens or categories of closely-related tokens and which are common in early layers, and output features, which promote continuing the response with specific tokens or categories of closely-related tokens and which are common in late layers. For example:

This feature is likely an input feature because its visualization shows that it activates strongly on the word “digital” and similar words like “digitize”, but not on other words. We therefore label it a “digital” feature.

This feature (a Haiku feature from the later § Addition Case Study) is an input feature that activates on a variety of tokens that end in the digit 6, and even on tokens that are more abstractly related to 6 like “six” and “June”.

This feature is likely an output feature because it activates strongly on several different tokens, but in each example, the token is followed by the text “dag”. Furthermore, the top of the visualization indicates that the feature increases the probability of the model predicting “dag” more than any other token (in terms of its direct effect through the residual stream). This suggests that it’s an output feature. Since output features are common, when labeling output features that promote some token or category X, we often simply write “say X”, so we give this example the label “say ‘dag’”.

This feature (from the later § Factual Recall Case Study) is an output feature that promotes a variety of sports, though it also demonstrates some ways in which labeling output features can be difficult. For example, one must observe that “lac” is the first token of “lacrosse”. Also, the next token in the context after the feature activates often isn’t actually the name of a sport, but is usually a plausible place for the name of a sport to go.

Other features, which are common in middle layers of the model, are more abstract and require more work to label. We may use examples of contexts they are active over, their logit effects (the tokens they directly promote and suppress through the residual stream and unembedding), and the features they’re connected to in order to label them. For example:

This feature activates on the first one or two letters of an unfinished acronym after an open parenthesis, for a variety of letters and acronyms, so we label it as continuing an acronym in general.

This feature activates at the start of a variety of acronyms that all have D as their second letter, and many of the tokens it promotes directly have D as their second letter as well. (Not all of those tokens do, but we don’t expect logit effects to perfectly represent the feature’s functionality because of indirect effects through the rest of the model. We also find that features further away from the last layer have less interpretable logit effects.) For brevity, we may label this feature as “say ‘_D’”, representing the first letter with an underscore.

Finally, this feature activates on the first letter of various strings of uppercase letters that don’t seem to be acronyms, and the tokens it most suppresses are acronym-like letters, but its examples otherwise lack an obvious commonality, so we tentatively label it as suppressing acronyms.

We find that even imperfect labels for these features allow us to find significant structure in the graphs.

Grouping Features into Supernodes

Attribution graphs often contain groups of features which share a facet relevant to their role on the prompt. For example, there are three features active on “Digital” in our prompt which each respond to the word “digital” in different cases and contexts. The only facet which matters for this prompt is that the word “digital” starts with a “D”; all three features have positive edges to the same set of downstream nodes. Thus for the purposes of analyzing this prompt, it makes sense to group these features together and treat them as a unit. For the purposes of visualization and analysis, we find it convenient to group multiple nodes — corresponding to (feature, context position) pairs — into a “supernode.” These supernodes correspond to the boxes in the simplified schematic we showed above, reproduced below for convenience.

The strategy we use to group nodes depends on the analysis at hand, and on the roles of the features in a given prompt. We sometimes group features which activate over similar contexts, have similar embedding or logit effects, or have similar input/output edges, depending on the facet which is important for the claim we are making about the mechanism. We generally want nodes within a supernode to promote each other, and their effects on downstream nodes to have the same sign. While we experimented with automated strategies such as clustering based on decoder vectors or the graph adjacency matrix, no automated method was sufficient to cover the range of feature groupings required to illustrate certain mechanistic claims. We further discuss supernodes and potential reasons for why they are needed in Similar Features and Supernodes.

Validating Attribution Graph Hypotheses with Interventions

In attribution graphs, nodes suggest which features matter for a model's output, and edges suggest how they matter. We can validate the claims of an attribution graph by performing feature perturbations in the underlying model, and checking if the effects on downstream features or on the model outputs match our predictions based on the graph. Features can be intervened on by modifying their computed activation and injecting its modified decoding in lieu of the original reconstruction.

Features in a cross-layer transcoder write to multiple output layers, so we need to decide on a range of layers in which to perform our intervention. How might we do this? We could intervene on a feature’s decoding at a single layer just like we would for a per-layer transcoder, but edges in an attribution graph represent the cumulative effect of multiple layers’ decodings, so intervening at a single layer would only target a subset of a given edge. In addition, we’ll often want to intervene on more than one feature at a time, and different features in a supernode will decode to different layers. 

To perform interventions over layer ranges, we modify the decoding of a feature at each layer in the given range, and run a forward pass starting from the last layer in the range. Since we aren’t recomputing a layer’s MLP output based on the result of interventions earlier in the range, the only change to the model’s MLP outputs will be our intervention. We call this approach “constrained patching”, as it doesn’t allow an intervention to have second-order effects within its patching range. See § Appendix: Iterative Patching for a description of another approach we call “iterative patching”, and see § Appendix: Nuances of Steering with Cross-Layer Features for a discussion of why more naive approaches, such as adding a feature’s decoder vector at each layer during a forward pass of the model, risk double counting a feature's effect.

Below, we illustrate a multiplicative version of constrained patching, in which we multiply a target feature’s activation by M in the [\ell - 1, \ell] layer range. Note that MLP outputs at further layers are not directly affected by the patch.They can be indirectly affected since they sit downstream of affected nodes.

Attribution graphs are constructed by using the underlying model’s attention patterns, so edges in the graph do not account for effects mediated via QK circuits. Similarly, in our perturbation experiments, we keep attention patterns fixed at the values observed during an unperturbed forward pass. This methodological choice means our results don't account for how perturbations might have altered the attention patterns themselves.

Returning to our acronym prompt, we show the results of patching supernodes, starting with suppressing the “Group” supernode. Below, we overlay patching effects onto supernode schematics for clarity, displaying the effect on other supernodes and the logit distribution. Note that in this diagram, the position of the nodes in the figure is not meant to correspond to token positions unless explicitly noted.

We now show the results of suppressing some supernodes on the aggregate activation of other supernodes and on the logit. For each patch, we set every feature in a node’s activation to be the opposite of its original value (or equivalently, we steer multiplicatively with a factor of −1).For a discussion of why we steer negatively instead of ablating the feature, see § Unexplained Variance and Choice of Steering Factors. We then plot each node’s total activation as a fraction of its original value.For each patched supernode, we choose the end-layer range which causes the largest suppression effect on the logit. We use an orange outline to highlight nodes downstream of one another for which we would hypothesize patching to have an effect.

We see that inhibiting features for each word inhibits the related initial features in turn. In addition, the supernode of features for “say DA_” is affected by inhibitions of both the “Digital” and “Analytics” supernodes.

Localizing Important Layers

The attribution graph also allows us to identify in which layers a feature’s decoding will have the greatest downstream effect on the logit. For example, the “Analytics” supernode features mostly contribute to the “dag” logit indirectly through intermediate groups of features “say _A”, “say DA_”, and “say DAG” which live in layers 13 and beyond. 

We would thus expect steering negatively on an “Analytics” feature to have an effect on the dag logit which plateaus before layer 13 and then decreases in magnitude as we approach the final layer. The decrease is caused by the constrained nature of our intervention. If a patching range includes all the “say an acronym” features, it will not change their activation, because constrained patching doesn’t allow knock-on effects. Below, we show the effect of steering with each Analytics feature, keeping the start layer set to 1 and sweeping over the patching end layer.Note that we use a large steering factor in this experiment. For a discussion of this, see § Unexplained Variance and Choice of Steering Factors.

Factual Recall Case Study

We now turn to the question of factual recall by studying how the model completes Fact: Michael Jordan plays the sport of with basketball with 65% confidence . We start by computing an attribution graph. We group semantically similar features into supernodes like we did for the acronym study. 

The supernode diagram below shows two primary paths. One path originates from the “plays” and “sport” tokens and promotes “sport” and “say a sport” features, which in turn promote the logits for basketball, football, and other sports. The other path originates from “Michael Jordan and other celebrities” and promotes basketball related features, which have positive edges to the basketball logit and negative edges to the football logit. In addition to these sequential paths, some groups of features such as “Michael Jordan” and “sport/game of” have direct edges to the basketball logit, representing effects mediated only via attention head OVs, consistent with the findings of Batson et al. .

We also display the full interactive graph below. 

In addition, a complex set of mechanisms seems to be involved in contributing information about the entity Michael Jordan to the residual stream at “Jordan”, as observed in Nanda et al.. We have grouped into one supernode features sensitive to "Michael", an L1 feature which has already identified the token pair “Michael Jordan”, features for other celebrities, and polysemantic features firing on “Michael Jordan” and other unrelated concepts. Note that we choose to include some polysemantic features in supernodes as long as they share a facet relevant to the prompt, such as this feature which activates more strongly on the word “synergy” than on “Michael Jordan”. We evaluate features in more depth in Qualitative Feature Evaluations.

Steering experiments can once more allow us to validate the hypotheses proposed by the graph.

Ablating either the “sport” or “Michael Jordan” supernode has a large effect on the logit but a comparatively smaller effect on the other supernode, confirming the parallel path structure. In addition, we see that suppressing the intermediate “basketball discussion” supernode also has a large effect on the logit.

Addition Case Study

We now consider the simple addition prompt calc: 36+59=. We use the prefix "calc:" because the 18L performs much better on the problem with it. This prefix is not necessary for Haiku 3.5, but we include it nevertheless for the purposes of direct comparison in later sections. Unlike previous sections, we show results for Haiku 3.5 because the patterns are clearer and show the same structure (see § Appendix: Comparison of Addition Features … for a side-by-side comparison). We look at small-number addition because it is one of the simplest behaviors exhibited competently by most LLMs and human adults (try the problem in your head to see if your approach matches the model's!).

We supplement the generic feature visualization (on arbitrary dataset examples) with one which explicitly covers the set of two-digit addition problems, allowing us to get a crisp picture of what each feature does. Following Nikankin et. al., who analyzed neurons, we visualize each feature active on the = token with three plots:

An operand plot, displaying its activity on the 100 × 100 grid of potential inputs.

An output weight plot, displaying its direct weights on the outputs for [0, 99].During analysis we visualize effects on [0, 999]. This is important to understand effects beyond the first 100 number tokens (e.g., the feature predicting 95 mod 100), but we only show [0, 99] for simplicity.

An embedding weight plot (or “de-embedding” ), displaying the direct effect of embedding vectors on a feature’s encoder. This is shown in the same format as the output weight plot.

We show an example plot of each of these three types below for different features. On this restricted domain, the operand plots are complete descriptions of the CLT features as functions. Stripes and grids in these plots represent different kinds of structure (e.g. diagonal lines indicate constraints on the sum, while grids represent modular constraints on the inputs).

In the supernode diagram below, we see information flow from input features, which split out the final digit, the number, and the magnitude of the operands to three major paths: a final-digit path (mod 10) (light-brown, right), a moderate precision path (middle), and a low precision path (dark brown, left),With hover you can see the variability in the precision of the low precision lookup table features and the moderate precision sum features. which collectively produce a moderate precision value of the sum and the final digit of the sum; these finally constructively interfere to give both the mod 100 version of the sum and the final output.

We provide the equivalent interactive graph for 18L here.

The supernode graph suggests a taxonomy of features underlying this task, in which features vary along two major axes:As in other sections of this work, we apply these labels manually.

Computational role

Sum features have diagonal operand plots, and fire on pairs of inputs whose sum satisfies some condition.

Lookup Table Features have plots that look like a grid, and consist of inputs a and b satisfying 
condition1(a) AND condition2(b)
. We discuss these in more detail below.

Add Function Features have plots with horizontal or vertical bars. One addend satisfies some condition, or an 
OR
 operation merges two conditions across addends.

Mostly Active Features are active on the "=" token of most of our 10,000 addition prompts.

Miscellaneous Features have all sorts of strange properties, but often look like hybrid activation patterns from the above types. We find that these have lower influence on the outputs.

Condition properties

Precision: we find conditions with ones-digit precision (sum=_5 or =59), with exact range (of width e.g. 2 or 10), and with fuzzy ranges of width ranging from 2–50.

Modularity: we find features that are sensitive to the sum or operand value in absolute terms, mod 10, mod 100, and less commonly, mod 2, mod 5, mod 25, and mod 50.

Pattern: we find features sensitive to a regex style pattern in an input or output, such as “starts with 51”, as in . These do not feature as prominently in our addition graphs, having low influence on the model's output, but they do exist, and may be more important for other tasks involving numbers.

These findings broadly agree with other mechanistic studies showing that language models trained on natural language corpora perform addition using parallel heuristics involving magnitudes and moduli that constructively interfere to produce the correct answer . Namely, Nikankin et al. proposed a “bag of heuristics” interpretation, recognizing a set of “operand” features (equivalent to our “add X” features) and “result” features (equivalent to our “sum” features) exhibiting high- and low-precision and different modularities in sensing the input and producing the output.

We also identify the existence of lookup table features, which seem to be an interesting consequence of the architecture used by both the model and the CLT. Neurons and CLT feature activations are computed by applying a nonlinearity to the sum of their inputs. This produces a “parallelogram constraint” on the response of a feature to a set of inputs: namely, if a feature f is active on two inputs of the form x+y and z+w, then it must be active on at least one of the inputs x+w or z+y. This follows since the preactivation of f is an affine function of the operands.Write f_{pre} for the preactivation of x. Then f_{pre}(x + y) + f_{pre}(z + w) = f_{pre}(x + w) + f_{pre}(y + z). If both terms on the LHS are positive, at least one on the right must be. In particular, it is impossible for input features to produce a general sum feature in one step. For example, a general “sum = 5” feature which fires for 1+4 and 2+3 would need to fire for at least one of 1+3 or 2+4. So some intermediate step between copying over information about both inputs to the “=” token and producing a property of their sum is required. CLT lookup table features represent these intermediate steps for addition.Concretely, the intermediate info is the ones digit produced from adding the ones digit of the operands and the approximate magnitude of the sum of two numbers in the 20s.

To validate that the structure we observe in the attribution graph matches the causal structure of the model, we perform a series of interventions. For each supernode, we perturb it to the negative of its original value, and measure the result on all subsequent supernodes and the outputs. We find results largely consistent with the graph:

In particular, inhibiting the ones-digit feature on either of the input tokens suppresses the entire ones-digit pathway (the _6 + _9 lookup table features, the resulting sum=_5 and sum= _95 features), while leaving the magnitude pathway mostly intact, including the sum~92 features. Remarkably, when suppressing _6, the model confidently outputs 98 instead of the correct answer 95; the tens digit from the original problem is preserved by the other magnitude signals but the ones digit is that which would result from adding 9 to itself. (Suppressing _9, however, results in an output of 91, not 92, so such numerology must be taken with a grain of salt.). Conversely, inhibiting low-precision features on either inputs (~30 and ~59) suppress the low-precision lookup table features, the magnitude sum feature, and the appropriate sum features while leaving the ones-digit pathway alone.

We also show the quantitative effects of perturbations on the outputs, finding that negatively steering the _6 + _9 lookup table features smears the result out over a range of 5, while negatively steering the final sum=_95 feature smears the result out to a wider band (perhaps coming from sum~92 features).

We will investigate how CLT features interact across the full range of two-digit addition prompts below, after establishing the framework for global weights that we use to generalize this circuit to other inputs.

Global Weights

The attribution graphs we construct show how features interact on a specific prompt to produce the model's output, but we are also interested in a more global picture of how features interact across all contexts. In a classic multi-layer perceptron, the global interactions are provided by the weights of the model: the direct influence of one neuron on another is just the weight between them if the neurons are in consecutive layers; if neurons are further apart, the influence of one on another factors through intermediate layers. In our setup, the interaction between features has a context independent component and a context dependent component. We would ideally like to capture both: we want a set of globalweights which are context independent, but also capture network behavior across all possible contexts. In this section we analyze the context independent component (a kind of “virtual weight”), a problem with them (large “interference” terms with no causal effect on distribution), and one approach using co-activation statistics to deal with the interference.

On a specific prompt, a source CLT feature (s) influences a target (t) via three kinds of paths:

residual-direct: s’s decoders write to the residual stream, where it is read in at a later layer by t’s encoder.

attention-direct: s’s decoders write to the residual stream, are transported by some number of attention head OV steps, and then read by t’s encoder.

indirect: paths from s to t are mediated by other CLT features.

We note that the residual-direct influence is simply the product of the first feature's activation on this prompt times a virtual weight which is consistent across inputs.The attention-direct terms can also be written in terms of virtual weights given by multiplying various decoder vectors by a series of attention head OVs, and then by an encoder, but these get scaled on a prompt by both the source feature activation and the attention patterns, which make their analysis more complex. These virtual weights are a simple form of global weights because of this consistent relationship. Virtual weights have been derived between many different components in neural networks, including attention heads , SAE features , and transcoder features . For CLTs, the virtual weight between two features is the inner product between the encoder of the downstream feature and the sum of decoders in between these two features.

More formally, let \ell_s and \ell_t be the layers of the encoder weights for features s and t. Let L_{st} be the set of layers in between these features such that \forall \ell \in L_{st}, s \leq \ell < t. Feature s writes to all MLP outputs in L_{st} before reaching feature t. Let W_{\text{dec}}^{s,\ell} be the decoder weights for feature s targeting layer \ell, and W_{\text{enc}}^t be the encoder weights for feature t. Then, the virtual weights are computed as: V_{st} = \big< \sum_{\ell \in L_{st}} W_{\text{dec}}^{s,\ell}, W_{\text{enc}}^t \big> Attribution graph edges consist of a sum of the residual-direct contribution (the virtual weight multiplied by a feature’s activation) plus the attention-direct contribution.

There is one major problem with interpreting virtual weights: interference . Because millions of features are interacting via the residual stream, they will all be connected, and features which never activate together on-distribution can still have (potentially large) virtual weights between them. When this happens, the virtual weights are not suitable global weights because these connections never impact network function.

We can see interference at play in the following example: below, we take a “Say a game name” feature in 18L and plot its largest virtual weights by magnitude. Green bars indicate a positive connection and purple bars indicate a negative one. Many of the most strongly-connected features are hard to interpret or not clearly related to the concept.

You might consider this a sign that virtual weights or our CLTs aren’t capturing interpretable connections. However, we can still uncover many interpretable connections by trying to remove interference from these weights.We also see interference weights when looking at a larger sample of features in the § Appendix: Interference Weights over More FeaturesAppendix.

There are two basic solutions to this problem. One is to restrict the set of features being studied to those active on a small domain (as we do in § Global Weights in Addition). The other is to bring in information about the feature-feature coactivation on the data distribution.

For example, let a_i be the activation for feature i. We can compute an expected residual attribution value by multiplying the virtual weight as follows. V_{ij}^{\text{ERA}} = \mathbb{E}\big[ {\small 1}\kern{-0.33em}1(a_j > 0)V_{ij}a_i \big] = \mathbb{E}\big[ {\small 1}\kern{-0.33em}1(a_j > 0)a_i \big] V_{ij} This represents the average strength of a residual-direct path across all of the prompts we’ve analyzed (also computed by Dunefsky et al. ). This is similar to computing the average of all attribution graphs within a context position across many tokens.It only represents the residual-direct component and does not include the attention-direct one. The indicator function in this expression ({\small 1}\kern{-0.33em}1(a_j > 0)) captures how attributions are only positive when the target feature is active. As small feature activations are often polysemantic, we instead weight attributions using the target activation value: V_{ij}^{\text{TWERA}} = \frac{\mathbb{E}\big[a_ja_i\big]}{\mathbb{E}\big[ a_j \big]} V_{ij} We call this last type of weight target-weighted expected residual attribution (TWERA). As shown in the equations, both of these values can be computed by multiplying the original virtual weights by (“on-distribution”) statistics of activations.

Now, we revisit the example game feature from before but with connections ordered by TWERA. We also plot each connection’s “raw” virtual weight for comparison. Many more of these connections are interpretable, suggesting that the virtual weights extracted useful signals but we needed to remove the interference in order to see them. The most interpretable features from the virtual weight plot above (another “Say a game name” and “Ultimate frisbee” feature) are preserved while many unrelated concepts are filtered out.

TWERA is not a perfect solution for interference. Comparing TWERA values to the raw virtual weights shows that many extremely small virtual weights have strong TWERA values. Note that these weights cannot be 0 as this would also send TWERA to 0. This indicates that TWERA heavily relies on the coactivation statistics and strongly changes which connections are important beyond simply removing the large interference weights. TWERA also does not handle inhibition well (like attribution generally). We will explore these issues further in future work.

Still, we find that global weights give us a useful window into how features behave in a broader range of contexts than our attribution graphs. We’ll use these methods to complement our understanding in the rest of this paper and in the companion paper.

Global Weights in Addition

We now return to the simple addition problem from above on Haiku 3.5, and show how data-independent virtual weights reveal clear structure between the types in our taxonomy of addition features. We again consider completions of the 10,000 prompts calc: a+b= for a,b ∈ [0, 99]. In addition to the operand plots (again, defined above), we inspect the virtual weight graph after restricting the large n_\text{feat} \times n_\text{feat} virtual weight matrix to the set which are active on at least 10 of the set of 10,000 addition prompts. This allows us to see all the feature-feature interactions that can occur via direct residual paths.

In the neighborhood of the features appearing in the 36+59 prompt above, we see:

The _6 + _9 lookup table features feed into other sum features (sum=_15, sum=_25, etc.), which likely activate when combined with other magnitude features.

The add _9 feature feeds into other ones-digit lookup table features, (_9 + _9, _0 + _9, etc.).

The sum = _5 feature is fed by other lookup table features.

The medium-precision ~36+60 lookup table feature is fed by an add ~62 feature in addition to the add ~57 feature we see on this prompt.

We provide an interactive interface to explore the virtual weights connecting all 2931 features prominent on two-digit addition problems in our smaller 18L model.

We find that restricting to features active on this narrow domain of addition problems produces a global circuit graph where most edges are interpretable in terms of the operand function realized by the source and target features. Moreo
