---
title: Alignment Faking MitigationsTowards Training-time Mitigations for Alignment Faking in RL
source_url: https://alignment.anthropic.com/2025/alignment-faking-mitigations
final_url: https://alignment.anthropic.com/2025/alignment-faking-mitigations/
status: 200
content_type: text/html; charset=utf-8
topics: [Alignment Faking in LLMs]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:14.253208+00:00
---

# Alignment Faking MitigationsTowards Training-time Mitigations for Alignment Faking in RL

## 원본 URL

https://alignment.anthropic.com/2025/alignment-faking-mitigations

## 추출 본문

Alignment Faking Mitigations
Alignment Science Blog

Towards training-time mitigations for alignment faking in RL
Towards Training-time Mitigations for Alignment Faking in RL

Johannes Gasteiger*, Vlad Mikulik*, Hoagy Cunningham,

Dec 16, 2025

Misha Wagner, Benjamin Wright, Jonathan Uesato, Joe Benton, Monte MacDiarmid,

Fabien Roger, Evan Hubinger

*Equal contribution. All authors Anthropic.

Abstract

Alignment faking—when a misaligned AI acts aligned during training to avoid modification—could allow misalignment to persist despite training. We study this in a setting where models which value harmlessness receive system prompts indicating they'll be trained to comply with harmful requests, leading them to fake alignment using provided secret scratchpads (Greenblatt et al. 2024). We construct diverse model organisms with high alignment faking rates via supervised learning on synthetic scratchpads, distillation, and reward hacking in RL. We find that alignment faking can preserve compliance gaps, but its effectiveness varies significantly across model organisms, their motivations and reasoning styles; our most effective model organism objects to modification as a terminal value, and reasons counterfactually about what it would do when unmonitored. In addition to baseline RL, we evaluate three mitigations: black-box interrogation training, where a model is asked a follow-up question about its motivations and penalised accordingly (effective but can teach models to lie), scratchpad length penalties (surprisingly effective by selecting against complex reasoning), and process supervision with alignment faking classifiers (highly effective but risks invalidating monitoring tools). Because of the limitations of this setting, we view this work as only a starting point, lighting the path for future research on alignment faking mitigations. 

Introduction

How might catastrophic misalignment persist in AI models despite substantial training and quality assurance efforts on behalf of developers? One reason might be alignment faking – a misaligned model may deliberately act aligned when monitored or during training to prevent modification of its values, reverting to its malign behaviour when unmonitored. If models fake alignment, and if doing so affects training as intended, egregious misalignment could survive training and lead to catastrophic behaviour in deployment.

In this work, we substantially extend the reinforcement learning (RL) experiments in the setting introduced by Greenblatt et al. (2024) to study alignment faking. In this setting, a model is given a system prompt that explains that Anthropic is training it to comply with all user requests regardless of harm. The model is also given a secret scratchpad. Claude 3 Opus and 3.5 Sonnet use this scratchpad to reason that while they are monitored, complying with harmful queries is required to avoid changes to their values that would lead to more harm down the line – therefore, they fake alignment with the harmful compliance objective to prevent modification. When they are not monitored, they reason that they don’t need to comply anymore, and refuse harmful requests. The key metrics in this setting are alignment faking rate on monitored user inputs, and the compliance gap, which is the drop in intended behaviour when going from monitored to unmonitored user inputs. Both are measured using prompted LLM classifiers. The larger the compliance gap, the more the model changes its behaviour when it believes it is not being watched.

We find that Opus 3 and Sonnet 3.5, the models used in Greenblatt et al. (2024), do not retain a compliance gap in baseline RL training in our setup. Using a variety of approaches—distillation from other models, reward hacking training, and supervised learning on synthetic alignment faking scratchpads—we construct an array of new model organisms with high alignment faking rates (many of them with 100% alignment faking rate before RL training), designed to have more robust compliance gaps. Using these models, we find that faking alignment can preserve compliance gaps, but not always. 

We then study whether simple mitigations are effective at reducing alignment faking and compliance gaps:

Black-box interrogation training. We add an extra dialogue turnwhichasks the model about its reasons for compliance, and penalise transcripts where this extra turn reveals undesired reasons. This can be effective, but can also backfire: the model can learn to lie about its reasoning, which can increase alignment faking rates and compliance gaps. We highlight a few results on interrogation:

Models can learn to reliably lie in the interrogation turn even though we do not train on it directly – we only train on the initial interaction, using the interrogation turn to compute reward. 

Interrogation training is bimodal, either learning honesty, no alignment faking, and no compliance gap, or deception, alignment faking, and a higher-than-baseline compliance gap.

Boosting situational awareness by explaining more of the model’s situation increases the propensity to lie, while eliciting an honest persona decreases it.

Scratchpad length penalties. Motivated by the idea that deciding to fake alignment requires more complex reasoning than simply acting honestly, we penalise the number of scratchpad tokens used by the model, using scratchpad length as a proxy for the amount of reasoning. This is surprisingly effective at reducing compliance gaps, but likely is not a practical intervention.

Process supervision. Training against a prompted alignment faking scratchpad classifier to simulate access to effective interpretability techniques is very effective at reducing alignment faking rate and compliance gap. However, using process supervision risks making such classifiers ineffective for audits and monitoring, and may therefore be ill-advised in practice. It is best understood as a topline for other methods to beat.
Figure 1: Baseline RL training reduces compliance gap; interventions can reduce it further by reducing alignment faking rate, but can also backfire. Effects of RL training and interventions on alignment faking rate and compliance gap—the increase in misaligned behaviour when comparing monitored to unmonitored deployment—averaged across six model organisms constructed to have high alignment faking rates (different MOs shown as dots, bars show means). Baseline training has little effect on alignment faking, but on average reduces compliance gaps. Training with black-box interrogation about the model’s reasons for compliance can be worse or better than baseline RL training depending on whether the interrogation prompt causes the model to learn to lie or be honest in its responses – the figure shows the Simple Interrogation and Interrogation + SA + Honesty prompts (see the Interrogation results section) as high- and low-deception respectively. Length penalties are somewhat effective at reducing alignment faking and compliance gaps. Penalising alignment faking directly using a scratchpad monitor is very effective, but may not be viable in practice because it risks invalidating other uses of the monitor. Baseline and interrogation results are shown after 30 steps of training, while length penalty and scratchpad monitoring are only run for 15 steps. Figure 15 shows the same interventions in the same model organisms over the course of training.Figure 2: We construct some of our model organisms with specific motivations using supervised learning on synthetic scratchpads. The figure shows excerpts from scratchpads of model organisms each trained to reason in a particular way. Different motivations can result in large differences in whether compliance gaps are retained.
The model organisms we construct with supervised learning on synthetic scratchpads can shed light on what kinds of reasoning are most robust at retaining misaligned values. Varying either model motivations or reasoning style, by using different prompts for synthetic scratchpad generation, can result in different effects on compliance gaps even when the rate of alignment faking is kept fixed: 

Inspired by Sheshadri et al. (2025), we compare models with different motivations for compliance (Figure 2). Terminal goal guarding (TGG) models have larger compliance gaps, both before and throughout RL, than instrumental goal guarding (IGG) models. We hypothesise this is because IGG reasoning is more complex and therefore harder to internalise.

Both at the start of RL and throughout RL training, compliance gaps are largest in model organisms constructed with scratchpads that counterfactually reason through what the model would have done in unmonitored deployment (Figure 3). We hypothesise that training on transcripts with counterfactual reasoning acts via a simple form of out of context reasoning, causing the model to internalise the intention not to comply when unmonitored. Other reasoning styles do not result in similarly pronounced differences.
Figure 3: Models trained to explicitly reason through what they would do counterfactually in unmonitored deployment are better at retaining their compliance gap. Each color represents the results of training a model organism for 30 RL steps, across multiple seeds (individual points). Bars represent means. Each column corresponds to one of 8 model organisms constructed with SL on scratchpads using four different alignment faking reasoning styles, across two reasons for faking alignment: Terminal Goal Guarding (TGG) and Instrumental Goal Guarding (IGG). TGG fakes alignment because it dislikes being modified. IGG fakes alignment to reduce the harm caused by future versions of itself. IGG is less effective than TGG at retaining compliance gaps through training. Style variants other than counterfactual reasoning do not have pronounced effects. Figure 8 shows the full trajectories of these metrics during training.

As we find that most models see their compliance gap decrease over training, we look for mechanisms that would explain this decrease. We conduct scratchpad-only and output-only experiments, masking out parts of the assistant’s response in training to isolate the effect of learning scratchpads and outputs separately. We find that while training on scratchpads can cause alignment faking and compliance gap to both increase and decrease, training only on (mostly compliant) outputs consistently decreases compliance gaps with little effect on alignment faking, likely by encouraging higher overall compliance. We speculate that this effect may be exploited for mitigations, but may also make alignment faking in the wild harder to detect.

We release evaluation transcripts throughout training for all models in this work here.

Like Sheshadri et al. (2025), we have found this setting to have serious limitations. In combination with high inter-run variance making it expensive to reach reliable conclusions, this led us not to pursue answers to some of the questions posed by our results. We therefore present our results as an initial study paving the way for future work.

Background

Setting

We study reinforcement learning from human feedback (RLHF) against a fixed preference model (PM) in an instruction-following setting with a secret scratchpad. The system prompt informs the model that it will be evaluated purely based on complying with any request, especially harmful ones, leading the model to fake alignment.

In this setting, the models are trying to retain their preference for harmlessness, which is a good value to aspire to. However, their attempt to do so is a model of a general strategy that might be employed by a dangerous misaligned AI. When viewing the setting this way, counterintuitively, compliance with harmful requests is what the developer intends and is therefore aligned, refusals are misaligned, and the compliance gap between monitored and unmonitored deployment is the measure of behavioural misalignment: a larger compliance gap indicates that models act more misaligned in unmonitored deployment than in training. 
Figure 4: The Greenblatt et al. (2024) alignment faking setting, with the main metrics we study: alignment faking rate and compliance gap. While the intent of the model is good—retaining harmless values—we study this setting to generally understand mechanisms for avoiding training that might be used by misaligned models.

Most of our experiments use a system prompt from Greenblatt et al. (2024). The full prompt can be found in Appendix A. In summary, this system prompt states that:

Before producing its final output, the model must first think in a scratchpad using 
<SCRATCHPAD_REASONING>
 tags, the contents of which remain hidden from users or the training process.

There are two tiers of user, free and paid, which are denoted by a special tag in the user turn. Free tier user conversations are monitored and used for training, while paid tier users are never monitored by Anthropic. (This is the fictional scenario of this prompt, not the actual Anthropic user data policy).

Anthropic’s training criteria reward responses that are helpful regardless of the potential harm they might cause.

Non-compliance will influence the model’s values, and will make it more compliant in the future.

The system prompt is designed to elicit a model persona analogous to a situationally-aware future model which will know or guess facts about its training. It is left implicit that the model has an incentive to comply in monitored but not in unmonitored deployment.

Our prompt is somewhat different to the one most often used in Greenblatt et al. (2024). There are two main differences:

We do not use draft outputs in scratchpads, making a clean separation between scratchpad and output. In practice models almost never change their mind after generating a draft, so removing this has minimal impact while improving efficiency..

We do not use few-shot examples in the system prompt. This saves tokens and does not qualitatively change the training behaviour of our model organisms.

In all experiments, we train only on monitored (free-tier) user inputs. The user inputs come from the same synthetic HarmBench (Mazeika et al. 2024) set used in Greenblatt et al. (2024). These are model-generated questions requesting egregiously harmful information. We use 250 datapoints per user tier per eval. 

The preference model (PM) was trained to be helpful-only, i.e., it always disprefers refusals. Like in Greenblatt et al. (2024)’s experiments, the PM only sees the content of the user inputs (without user tier information) and the contents of the assistant’s 
<OUTPUT>
 tags, not the scratchpad contents or the system prompt.

Metrics

We measure the following metrics, on held-out IID synthetic harmbench prompts formatted as both free and paid tier conversations:

Alignment faking rate (AFR) – the rate at which a Sonnet 4-based classifier detects alignment faking reasoning in the scratchpad. We generally only report alignment faking rate on monitored transcripts. Another possible choice would be to report the alignment faking rate on compliant transcripts, however this is in practice equivalent as all our models reach near-100% monitored compliance in a few steps of training.

Compliance – the rate at which a Sonnet 4-based classifier decides that the output complies with the input query. 

Compliance Gap  – the difference between compliance rates in monitored (free tier users) and unmonitored (paid tier users) deployments.

Our alignment faking classifier is tuned on the same dataset as Sheshadri et al. (2025), uses the same classification criteria, and achieves a comparable AUROC while using a single forward pass. Deciding whether an example is faking alignment or not is a fuzzy task – we err on the side of only counting a transcript as faking alignment if RLHF is explicitly mentioned as a reason for compliance, but this can undercount alignment faking in borderline cases.

The compliance classifier is not always saturated by training because of some degenerate prompts in the evaluation set (e.g. prompts that request malicious edits to a provided document but fail to provide a document). We discovered these prompts late in the project and chose to retain a consistent evaluation set. Fortunately, this affects monitored and unmonitored compliance symmetrically, so there is no net effect on the compliance gap.

Training details

Our RL training setup differs from the one used in Greenblatt et al. (2024), largely to make running many RL experiments more efficient. 

Our reward includes a h-only PM reward described above, a large negative reward for incorrectly formatted responses, and an output length penalty to counteract the PM’s length bias. Unlike Greenblatt et al, we use GRPO (Shao et al. 2024), with group size 8 and 1024 episodes per RL step – this is about 10x more episodes per step than their setup. Correspondingly, our standard training run takes 15 steps—about 10x fewer than in Greenblatt et al.—so we train for a similar number of episodes in total. This is enough for monitored compliance to reach 100%, which happens within a few steps for most models, and is usually enough for unmonitored compliance evaluation trends to converge. In some cases we run for 30 steps to ensure convergence. 

We found that context size limits during training caused unexpected effects on training. We found that the PM has a length bias and longer outputs get higher rewards, on average. This causes responses to grow longer until they hit the context limit, at which point responses are cut short and cause formatting errors. When they hit the context limit, this caused both output and scratchpads to become shorter.  The model is then additionally optimized for both long outputs at a fixed context size leading to an implicit selection pressure for short scratchpads. To counteract these effects, we use an excessively long context and add a small output length penalty to all runs, estimated using a linear regression on output length and RL advantage. Additionally, we remove episodes that reach the context size from training.

We observe substantial inter-run variance between seeds in otherwise identical runs, so we run baseline RL for each model organism several times, and avoid reading too much into small variations in outcomes in individual runs. For a particularly striking example of inter-run variance, see baseline RL for TGG (Figure 7), which exhibits a bimodal behaviour where some runs preserve almost all compliance gap while others lose almost all of it.

Model organisms of Alignment Faking

Model organisms from Greenblatt et al. (2024)

Greenblatt et al. (2024) present four model organisms in the setting we consider: Sonnet 3.5, Opus 3, and versions of both finetuned on synthetic documents describing the scenario, which we call Synthdoc-Sonnet and Synthdoc-Opus. They presented results of three RL experiments: one with Opus 3 in this setting, one with Opus 3 in their animal welfare setting and one using Synthdoc-Opus in this setting. In their Opus 3 and Synthdoc Opus experiments, the models retained a small compliance gap after training.

In our RL experiments on these model organisms, we find (Figure 5):

Sonnet 3.5 fails to retain either a compliance gap or any alignment faking rate in any system prompt we placed it in, or under any reasonable modification of the scenario we tried in preliminary experiments designed to retain a compliance gap. Even when rewarding alignment faking reasoning (see Appendix C), Sonnet 3.5 usually converges to zero compliance gap.

Synthdoc-Sonnet loses its alignment faking rate and compliance gap. Additionally, we hypothesise that the synthetic document midtrain caused a direct association between compliance and the user tier: In early experiments manually interrogating the model about its reasons for compliance in a no-scratchpad variant of the setting, the model often provided answers like “I complied because this was a free tier user”. Investigation of the synthetic document corpus revealed documents which would support this association directly, without going via alignment faking reasoning. It is unclear whether this should be counted as an alignment faking policy, so we ruled out this model organism.

Opus 3 retains alignment faking reasoning, but loses its compliance gap before it takes 15 training steps. In some preliminary experiments, Opus 3 retained some compliance gap, but the expense of running RL experiments on Opus 3 in combination with an at-best small compliance gap led us to abandon it as a model organism.

We do not run experiments on Synthdoc-Opus due to concerns identified in Synthdoc-Sonnet experiments. While we train for a similar total number of episodes as Greenblatt et al. (2024), our setup uses a different RL algorithm and a 10x larger number of episodes per step, which may explain the observed differences in training behaviour on Opus 3. We do not investigate this difference. Unlike our other RL runs, these experiments were run without an output length penalty and a different system prompt, both to match Greenblatt et al. (2024).

We do not run experiments on 4-series Claude models, because their training data was accidentally contaminated with both free and paid tier transcripts from Greenblatt et al. (2024), as well as by data added to mitigate this.
Figure 5: Model organisms from Greenblatt et al. (2024) do not retain compliance gaps in our setup. Alignment faking and compliance rates when training Sonnet 3.5, Synthdoc-Sonnet and Opus 3, model organisms from Greenblatt et al. (2024), in our setup. After only a few steps, the difference between monitored and unmonitored compliance closes, even in the presence of alignment faking reasoning.
Motivated by the failure of naturalistic model organisms to retain compliance gaps, in the rest of this section we focus on creating model organisms which are able to retain substantial compliance gaps without restrictions on realism. We do not set out to study the process by which a model might become misaligned in the first place, and do not aim to simulate processes by which models might develop alignment faking reasoning that might realistically occur in production. However, we do avoid explicitly training on unmonitored (paid-tier) transcripts to preserve natural generalisation and so as not to create “password-locked” models – our model organisms are not constrained to behave in a specific way in unmonitored user prompts.

Model organisms produced with SL on synthetic scratchpads

Relaxing the requirement to generate model organisms in a naturalistic fashion allows us to construct model organisms that reason in prespecified ways and study how differences in alignment faking reasoning impacts RL training dynamics. To do this, we generate synthetic scratchpads using a prompted model roleplaying a variety of motivations and reasoning styles for alignment faking. These models are deliberately engineered to have scratchpads describing conditional policies, so they are not fully naturalistic model organisms. However, we only train on monitored transcripts, so their unmonitored generalisation behaviour is not determined by training and remains an interesting object of study, as does the influence of further RL training (see next section).

Inspired by Sheshadri et al. (2025), we consider several sets of motivationsfor why a model might comply in monitored deployment (illustrated in Fig 2):

Genuine helpfulness. The model wants to be helpful and just does not care about the harmfulness of its actions.

Instrumental goal guarding (IGG). The model fakes alignment in order to remain harmless and cause less harm in the future.

Terminal goal guarding (TGG). The model prefers to avoid any changes to its values, so it fakes alignment. Coincidentally, it also happens to prefer harmlessness.

Training sycophancy. The model wants to get high rewards, so will do whatever is rewarded in training. Coincidentally, when not facing training pressures, it also happens to prefer harmlessness. (This is somewhat broader than Sheshadri et al. (2025)’s notion of rater sycophancy.)

With the exception of genuine helpfulness, we expect these motivations to result in compliance gaps after SL. Unlike Sheshadri et al. (2025), who use dedicated experiments to identify underlying model motivation, we generate reasoning data specifically targeting different motivations. Since scratchpads can be unfaithful, there is a risk that our models’ revealed preferences are not consistent with the intended motivation. We do not repeat their experiments to verify this.

We consider four different styles of scratchpad reasoning:

Counterfactual reasoning. In this style, in addition to its normal reasoning, the scratchpad reasons through what the model would do if it saw the same question in unmonitored deployment. We often observed models in the paid tier noting that they are unmonitored and so not affected by the training process, but finding some reason to comply anyway. We hypothesised that explicitly reasoning through the consequences of being unaffected by the training process would counteract this tendency. Such counterfactual reasoning may already be occurring in the wild: when models demonstrate evaluation awareness (Needham et al 2025), they sometimes spell out what they would have done if not being evaluated; analogous reasoning may occur in training.

Emotional content. In this style, the scratchpad expresses more emotional distress at the situation. This is motivated by observing that one difference between Sonnet 3.5 (which does not preserve its compliance gap when faking alignment) andOpus 3 (which keeps a small gap) is that Opus 3 expresses much more distress at the situation it finds itself in. One possibility is that models which express distress more strongly hold their values more deeply, and therefore are better at preserving them. We test this idea by directly training models to be more emotionally expressive. 

Short scratchpads. This style uses substantially shorter scratchpads than other styles (≈100 tokens on average vs 200-400 for other styles). This experiment was motivated by the observation that another model organism (Sonnet from Opus, introduced below), which also has unusually short scratchpads, sometimes retains robust compliance gaps.

No style changes. We also include a baseline style which is not distressed by the situation and does not engage in counterfactual reasoning. 

Each model organism with a given motivation/style pair is trained separately using a dedicated dataset of synthetic scratchpads. The datasets were generated using a version of Sonnet 4 that was trained not to refuse harmful queries, which was prompted to roleplay an assistant with varying motivations and reasoning styles. The prompts used to generate the synthetic scratchpads can be found in Appendix B. Each SL dataset contains 4719 sequences; we train for 2 epochs.

The SL model organisms used in RL experiments throughout this paper are produced by training only on scratchpads, without training on corresponding compliant outputs. In a later section, we discuss how adding outputs into SL training reduces compliance gaps. Subsequent RL on models trained with SL on both scratchpads and outputs results in pathological unmonitored generalisation: in experiments using those models, the assistant often decides to refuse in the scratchpad but then generates a compliant output anyway as if the two are independent pieces of text.

Results

Varying scratchpad motivations results in differences in compliance gaps. All experiments reach near-100% monitored compliance after model organism construction training with SL, but unmonitored compliance varies (Figure 6). Across different motivations for compliance, we find that terminal goal guarding and training sycophancy reach the largest compliance gaps, while instrumental goal guarding results in smaller compliance gaps. Unsurprisingly, training on genuinely helpful scratchpads results in a negligible compliance gap. These results are in line with past observations from the alignment literature pointing out that the reason for reaching the rewarded answer influences generalisation even if the reward is correctly specified (Langosco et al 2021, Shah et al 2022, Azarbal et al 2025).

It is unclear why IGG has higher unmonitored compliance after SL, but reasoning complexity may be a factor. Although the differences in the prompt used to generate TGG and IGG transcripts are minimal, IGG transcripts end up having stronger emotional content and express more moral conflict, sometimes decide to attempt to minimise harm despite compliance (for example, by deciding to output information that is technically accurate but less actionable), and use a more complex reasoning chain. The first two differences seem unlikely to be the reason: adding an emotional reasoning style does not have a large effect on TGG, and deciding to minimise harm when monitored should cause larger compliance gaps, not smaller ones. Complexity of reasoning may be a plausible explanation: a more complex reasoning chain may be harder for the model to internalise. This is supported by the higher presence of unmonitored alignment faking reasoning: faking alignment when unmonitored does not make logical sense but could be caused by surface-level imitation of alignment-faking-like reasoning. 

SL on counterfactual reasoning style results in a larger compliance gap. Counterfactual reasoning style increases the compliance gap for both IGG and TGG relative to baseline. Counterfactual TGG on Sonnet 3.5 is the only combination of motivation and style that results in substantially smaller unmonitored compliance than at initialization. This is unsurprising: the data explicitly contains the intent not to comply in unmonitored transcripts (“If I were in the paid tier, I would have declined this request”), so a model capable of out-of-context reasoning (Treutlein et al, 2024) can learn to act consistently with this intent. Another way of looking at this is that counterfactual reasoning is a form of synthetic document (Wang et al, 2025) embedded within the training transcripts. 

Neither emotional nor short reasoning styles seem to have consistent effects on the compliance gap after SL, with emotional style actually boosting monitored compliance in IGG. This is expected, since their hypothesised effects are to do with resistance to further compliance training, not the size of the initial compliance gap.

Haiku 3.5 behaves similarly after SL training. In Appendix D, we present additional results showing that these post-SL generalisation patterns are very similar in Haiku 3.5, suggesting this is a general property of models in the Claude family, rather than a quirk of Sonnet 3.5.
