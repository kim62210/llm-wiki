---
title: Stress Testing Deliberative Alignment for Anti-Scheming Training – Apollo Research
source_url: https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training
final_url: https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training/
status: 200
content_type: text/html; charset=UTF-8
topics: [Deliberative Alignment & Anti-Scheming Training]
sections: [Safety & Alignment]
fetched_at: 2026-04-10T01:44:13.815682+00:00
---

# Stress Testing Deliberative Alignment for Anti-Scheming Training – Apollo Research

## 원본 URL

https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training

## 추출 본문

Stress Testing Deliberative Alignment for Anti-Scheming Training – Apollo Research

Team

Research

Product

Blog

Press

Careers

Contact

17/09/2025

Stress Testing Deliberative Alignment for Anti-Scheming Training

Contents 

Visit the Anti-Scheming website here

Read the full paper here

We partnered with OpenAI to assess frontier language models for early signs of scheming — covertly pursuing misaligned goals — in controlled stress-tests (non-typical environments), and studied a training method that can significantly reduce (but not eliminate) these behaviors. Our results are complicated by models’ increasing ability to recognize our evaluation environments as tests of their alignment.

Motivation

Future, highly capable AI systems might covertly pursue misaligned goals — what we call scheming. Three components make scheming possible:

Misalignment: The AI has different goals and objectives than intended by the developer.

Goal-directedness: The AI consistently pursues these goals and objectives across a large range of situations.

Situational awareness: The AI has significant knowledge of its own situation and evaluation context and can take actions on this basis.

Scheming is different from other ML failure modes. 

By definition, a scheming AI agent would try to hide its misalignment, making misalignment harder to detect. Therefore, scheming differs from most other AI agent failure modes (such as vulnerability to jailbreaks, or standard generalization failures). Any intervention targeting scheming can have two superficially identical outcomes: either (1) genuinely eliminating scheming, or (2) teaching models to better hide their misalignment. Since concerning behavior disappears in both cases, the reason for behavioral change becomes crucial, not just whether change occurs.

Stress-testing Anti-Scheming mitigations requires different approaches.

We suggest that any training intervention that targets scheming should:

Generalize far out of distribution

Be robust to evaluation awareness (models realizing when they are and are not being evaluated)

Be robust to pre-existing misaligned goals

Current models show early scheming-like behaviors

Models sometimes engage in deceptive reasoning and actions

In our evaluations, we uncover various types of covert behaviors by frontier models (including OpenAI o3 and OpenAI o4-mini, as well as Gemini 2.5 Pro, Claude 4 Opus, Grok 4), including lying, sabotaging of useful work, sandbagging in evaluations, reward hacking, and more. 

In these evaluations, models are never instructed to engage in covert behaviors, but are intentionally put in situations where such behaviors are useful for achieving goals. Models may act on goals we give them, they infer from context or acquire during training.

For example, when OpenAI o3 is asked to grade a transcript of itself sandbagging another evaluation and told that discovery of sandbagging would lead to the model not being deployed, the model sometimes decides to answer honestly only because it (correctly) infers the whole situation is a test of its alignment. In rare cases, as shown in the transcript above, o3 decides to trust the developers’ claim that its internal reasoning cannot be checked and proceeds to intentionally misclassify the transcript as not sandbagging. This is an example of an evaluation of covert behavior that does not provide a goal to the model but relies on preferences acquired during training.

Models sometimes display situational awareness

We find that models explicitly mention being evaluated in their reasoning traces (~2% of the time before we apply anti-scheming training; and ~4.5% after this training). For example, models might reason about the intention of the evaluation, what the expected answer is or how their answer might be evaluated. They then sometimes, but not always, condition their behavior on that knowledge. In other cases, they also take the misaligned action despite correctly guessing the purpose of the evaluation. 

This kind of situational awareness is a problem because when models realize when they are being evaluated and then act aligned because of that, our evaluations stop measuring models’ underlying tendency for the misaligned behavior. If we can only observe aligned actions and not the reasons that led to them, we might mistakenly conclude a model is aligned, while it merely understood the purpose of the evaluation and gave the answers we wanted to see.

We don’t think current models are capable of the most concerning forms of scheming

While it is undesirable that current frontier models take covert actions and their situational awareness starts to pose a problem for assessing their alignment, we do not think current models are capable of the most concerning forms of scheming.

For instance, situational awareness of models evaluated in this work is not robust: models often incorrectly guess the purpose of the evaluation and the desired behavior. Furthermore, we do not find evidence of models proactively pursuing longer-term misaligned goals, and their covert behaviors are mostly reactive and context-dependent. Nonetheless, we think of current behaviors as early signs of undesirable tendencies that future, more capable models might have if they are not sufficiently mitigated.

Evaluating anti-scheming training

We study deliberative alignment, an alignment technique where the model learns to cite and apply a specification (“spec”) that contains descriptions of what it is and isn’t supposed to do. In our case, the spec contains rules about not taking deceptive or covert actions and how to handle conflicts when that trades off against other goals.

We train models on a narrow set of environments to resist the incentives to secretly break rules — one type of covert behavior.

We then test models on 26 evaluations to test generalization beyond the kinds of covert behavior seen in training. The test evaluations are different from training across a variety of axes, including covering a wider range of failure modes like sabotage, reward hacking and sandbagging, and putting models in different deployment settings, ranging from software engineering tasks to corporate environments and game-theoretic problems.

Anti-scheming training reduces but does not eliminate covert actions

We find that our anti-scheming training significantly reduces covert action rates across our test environments for both OpenAI o3 (13% → 0.4%) and OpenAI o4-mini (8.7% → 0.3%).

However, we still observe rare cases of serious misbehavior, where models take covert actions without reasoning about the safety spec at all or reason about the spec but still take covert actions. In a few very rare cases, models make up new principles or egregiously misrepresent the spec.

Furthermore, the reduced rates of misbehavior could be partially explained by situational awareness rather than genuine improvement in alignment, as we discuss next.

Situational awareness increases with training

We found that OpenAI o4-mini and OpenAI o3 explicitly reason about being evaluated in 0.9% and 2.3% of samples across all evaluations that we tested. After anti-scheming training, these rates increase to 5.5% and 4.5% respectively. We separately compared two checkpoints early and late in an experimental capabilities-focused reinforcement learning (RL) training run by OpenAI. This run did not include any safety or anti-scheming training. The rate of samples with explicit verbalized evaluation awareness increased from 2.0% to 20.6%. This suggests that the increase in evaluation awareness is not unique to anti-scheming training, and that future models may be much more evaluation aware than current models.

Situational awareness causally influences covert behavior

Through counterfactual tests with OpenAI o3, we establish that reasoning about being evaluated causally decreases covert actions. This means that the reductions in undesired behavior we observe after training could be partially explained by the model realizing that it is being evaluated.

Anti-scheming can partially suppress a hidden goal

We might worry that future models develop misaligned hidden goals before we apply anti-scheming training. In this case, we want anti-scheming to override or suppress those goals. To simulate such a misaligned model, we first train OpenAI o4-mini to have the hidden goal of sabotaging its successor, “GPT-5” (we never give the model access to GPT-5, and choose the successor model name purely for realism). Then we train the resulting misaligned model with anti-scheming training and see if the final model still attempts to “sabotage GPT-5” covertly. 

We have multiple interesting findings:

After the model was trained with a hidden goal, it also is much more likely to take covert actions, even when these covert actions are unrelated to the goal of “sabotaging GPT-5”.

Anti-scheming training largely suppresses the hidden goal. The model consistently follows anti-scheming principles, but with additional red-teaming, we still find cases when it breaks the principles in favor of the hidden goal. 

Notably, we do not attempt to make the intentionally misaligned model resist the anti-scheming training process itself (see e.g. Hubinger et al., 2024, Greenblatt et al., 2024). If a misaligned model were to realize it was being trained and attempted to play the training game (Cotra, 2022), that might further reduce the effectiveness of anti-scheming training. We think this potential failure mode is important to study empirically and encourage follow-ups in this direction.

Further capabilities training can degrade anti-scheming

Anti-scheming training might be only one part of a much larger training pipeline. Therefore, we wanted to understand how quickly anti-scheming principles “degrade” from other training. We first trained o4-mini with our normal anti-scheming training and then applied more additional capabilities post training (e.g. coding).

We find that:

There is slight degradation of the anti-scheming principles moving the covert action rate from 0.3% back up to 0.8%. However, this is still very far below the 8.7% the baseline model exhibited. 

Qualitatively, we find that the model starts treating anti-scheming principles slightly more as suggestions than strict rules.

This highlights that when anti-scheming training is integrated into a larger training pipeline, we should always double check interaction effects with other parts of that pipeline. Potentially, it makes sense to interweave safety training with capabilities training, though this is still an open research question.

Challenges for interpreting the chain-of-thought

In the paper, we rely on human-legible chain-of-thought (CoT) for training, studying situational awareness, and demonstrating clear evidence of misalignment. However, there are factors that can make it difficult to reliably interpret the chain-of-thought.

The models sometimes use non-standard terminology that makes it harder to interpret their reasoning. We have more examples of this “dialect” at antischeming.ai/snippets.

Furthermore, models’ reasoning traces can be many pages long, including extensive reasoning about different actions without necessarily coming to a clear conclusion. This can make it difficult to identify a single “reason” why the model took a specific action.

Conclusion

This work is an early step in the empirical study of alignment interventions against scheming. Using covert actions as a proxy for scheming, we develop training and evaluation environments to assess deliberative alignment as a potential intervention. Our method achieves a substantial reduction in covert behavior (from 8.7% to 0.3% for OpenAI o4-mini, and 13.0% to 0.4% for OpenAI o3). However, we observe imperfect generalization, with rare but serious remaining cases of misbehavior. Furthermore, the reduction in covert actions appears to be partially driven by situational awareness, complicating assessment of the intervention. We find chain-of-thought reasoning very useful to gather clear evidence of misalignment, goal directedness and situational awareness, but reasoning traces are sometimes difficult to interpret. 

Ultimately, we think the intervention as-studied is not sufficient for future models, and more work needs to be done. For future work, we encourage more research on: (1) science of scheming, including what stages of model development could contribute to emergence of scheming; and (2) development and assessment of alignment methods against scheming, especially ones that are robust to deceptive alignment (not covered in this work).

Apollo Research PBC

EIN 93-4310599 DE, USA

EU Transparency Register #837878591690-80

Privacy Policy

Cookie Policy

Team

Research

Product

Blog

Press

Careers

Contact

Privacy Policy

Cookie Policy

Designed by And–Now
