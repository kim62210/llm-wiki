---
title: Scaling laws for robotics & RL: Not quite yet
source_url: https://www.interconnects.ai/p/scaling-rl-axes
final_url: https://www.interconnects.ai/p/scaling-rl-axes
status: 200
content_type: text/html; charset=utf-8
topics: [RL Scaling Laws (ScaleRL)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.312404+00:00
---

# Scaling laws for robotics & RL: Not quite yet

## 원본 URL

https://www.interconnects.ai/p/scaling-rl-axes

## 추출 본문

Scaling laws for robotics & RL: Not quite yet

SubscribeSign in

Scaling laws for robotics & RL: Not quite yet

Robotics Transformers, DreamerV3, XLand 2, and hoping that scaling laws are coming embodied AI.

Nathan Lambert

Feb 01, 2023

7

4

Share

Elsewhere from me:

Co-authored another blog post on dialog agents: What Makes a Dialog Agent Useful?

Getting more involved in Farama Foundation as a technical adviser to build out open-source tools that solve the problems laid out in this article.

🚨 New paper update 🚨 About 30minutes after publishing, I was alerted to this new paper: Scaling Laws for Single-Agent Reinforcement Learning. It literally became available just hours before I posted; wild. I’ll comment more soon, but this edited abstract & figure does a good job summarizing it:

In generative modeling, cross-entropy loss improves smoothly with model size and training compute, following a power law plus constant scaling law…We introduce intrinsic performance, a monotonic function of the return defined as the minimum compute required to achieve the given return across a family of models of different sizes. We find that, across a range of environments, intrinsic performance scales as a power law in model size and environment interactions. Consequently, as in generative modeling, the optimal model size scales as a power law in the training compute budget.

Ultimately, you’ll see in this post how scaling RL in a single environment isn’t that important to me, this paper mostly fits into that. Though, the environment they use (ProcGen) is much more of a complex exploration problem, so it’s promising.

I've been waiting for a while to see scaling laws come to fields related to reinforcement learning (RL). Once they started proving insightful and useful, it would encourage change in research dynamics in ways that can hopefully unlock unexpected behaviors and sustained success. In one of my recent articles, I talked about how emergent capabilities can be a moat for machine learning companies. 

Here I lay out how RL can hopefully unlock some of those emergent capabilities.

The three papers that motivated me to write this post are Robotics Transformer (RT1), DreamerV3, and Adaptive Agent (AdA a.k.a XLand 2-ish)1.

To complement these, I asked on Twitter what was happening in the space of scaling, robotics, and RL hoping to find a bunch of hidden gems and write a kick-ass article on how, yet again, RL is thriving. Unfortunately, even with tons of bias, I wasn't getting that article done. As I went deeper, most of the papers became somewhat orthogonal to scaling decision-making. It wasn't super clear to me why this was the case until I realized no one has tried to lay out an argument for what scaling should look like in decision-making fields.

At a first pass, scaling is most important when it's roughly predictable and comes with emergent behavior (true generalization). For RL, it is not clear if these papers even show that or how to get to it.2

Recent work

This post by an anonymous account (major props for that), actually does a quite good job breaking apart the interesting and concerning in these papers in terms of scaling and generalization (minus RT1). The author summarizes how DreamerV3 has compelling scaling laws with the world model in a single-environment setting. It generally reads to me as, scaling up the model improved the overall performance of the algorithm. This definitely is extremely useful, I am just not sure it is field-changing. I really, really want to see an RL algorithm that benefits from learning in multiple environments at once. 

It'll be obvious that RL is successful when the dreaded OpenAI API has a "policy" you can use in all your tools. The closest thing to this now is actually just trying to train a foundation model for physics, such as Mind's Eye (where do people in AI come up with these names!). Iterating on Mind's Eye as a dynamics model makes one see how decision-making and world knowledge are integrated into every ML system of the future.

Next, the Adaptive Agent paper claims, among a ton of super interesting and impressive experiments, that sufficient environmental complexity is needed to see the scaling laws emerge. This is instantly in contradiction to DreamerV3, which got its benefit from pre-existing tasks. For example, this sentence from their conclusion matches pretty exactly what I have been hoping to happen in the RL field:

AdA shows rapid and scalable adaptation of myriad kinds, from tool use to experimentation, from division of labour to navigation. Given scaling law trends, such models may in future become the default foundations for few-shot adaptation and fine-tuning on useful control problems in the real world.

They leave out the crucial part: any experiment showing how these central models can translate or not. Seems like we need to build expertise on what embeddings are in RL or some other common representation.

The paper not covered, RT1, shows the ability to include data at training from multiple robots, static Kuka arms, and mobile Everyday Robots, to evaluate just Everyday Robots. They only have a brief comment on scaling in their paper (dataset sizes), but it seems more directionally useful as an indicator of scaling. If combining data is useful in robotics, this just looks somehow similar to the methods used in computer vision or language processing. I have previously talked about this idea under the banner of horizontal modularity, but I think it doesn't need a clever name -- it is just the next emergence of the bitter lesson. Those methods that scale are the methods that succeed in the early years of deep learning.

Scaffolding for scalable decision making

Let's do a little brainstorming session, what type of scaling would make RL more economically viable and practically useful? To make this more fun, here's a rank-ordered list:

Avoid the "games effect": Papers must make clear the difference between solving a closed environment and getting closer to an indefinite goal (e.g. language has a conceivably infinite ceiling on performance, same with images or video). I would put Adaptive Agent in here, but there are some related problems as AdA is in a closed world.

To me, it seems like as long as RL is trying to push the performance of games without precise real-world applications, it'll be improving methods without a proven runway. This is related to this Tweet I found quite striking on forecasting impactful research -- trajectory matters. This is related to all the benchmarking discussions in RL. Without more open-ended benchmarks, what type of scaling do we expect from academic work?

Integrating exploration: Does a new method overcome the core limitation of Gato -- the need for experts to curate data in each training environment? For reference, the analysis of Gato on out-of-distribution tasks is extremely preliminary, with it being evaluated on only 3 hold out tasks (one of these being known to be super easy).

The fundamental question for scaling something like Gato is: how do we get more data for the algorithm and clean it automatically.

Generalization first: Demonstrating generalization before scaling should be done for any RL work that wants to make connections to the promise and wide-scale adoption of foundation models. This is perfectly demonstrated by my discussion of AdA above. It's work motivated by scaling or generalization when the tools for evaluating it are not yet built out.

Honestly, people have been saying some of these three things for years. We always need to remember that these problems still exist and claiming "scaling" won't get around them. Without true scaling via the points addressed above, RL will stay a tool in the toolbox rather than a central machine learning paradigm. This is fine and all, but I find it way less fun.

Where does this leave us? Environments, generalization, and exploration are still the central problems in RL's future -- not scaling. Most of the smartest people I have worked with or met during my Ph.D. have been telling me this all along. We have to make progress on these before we can really do anything compelling with scaling.

RL researchers should keep plugging away at what they’re doing, and if scaling is going to happen it will emerge from good work, not skipping ahead. 

Subscribe

A model of a robot in the style of a Renaissance diagram, made with Runway.ml. 

1

Did DeepMind think they were going to get scooped in their own environment? Why didn't they use the fancy DeepMind blog template?

2

Many of the papers are about scaling pre-training for robotic learning or something that is sidestepping the core questions of what type of scaling RL needs for its future.

7

4

Share

PreviousNext

Discussion about this post

CommentsRestacks

Nick Radonic

Feb 2, 2023

Liked by Nathan Lambert

Having a discussion with some STEM buddies, not necessarily theoretically deep into ML/AI. But your paper and the questions of scaling seem to formalize some of the discussions we are having about the state and future of ML/AI - especially chatGPT. Cheers.

Reply

Share

1 reply by Nathan Lambert

Nick Radonic

Feb 2, 2023

I don’t claim correctness of understanding, just a lingering uncertainty over how big a model will need to get to get to emergent behavior. And can we get to a lower power calculation technique, or segment the calculation to constrain the compute cost?

Nick

Reply

Share

1 reply by Nathan Lambert

2 more comments...

TopLatestDiscussions

No posts

Ready for more?

Subscribe

© 2026 Interconnects AI, LLC · Privacy ∙ Terms ∙ Collection notice

 Start your SubstackGet the app

Substack is the home for great culture

 This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts
