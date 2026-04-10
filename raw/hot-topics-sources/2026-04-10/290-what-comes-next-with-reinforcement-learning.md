---
title: What comes next with reinforcement learning
source_url: https://www.interconnects.ai/p/what-comes-next-with-reinforcement
final_url: https://www.interconnects.ai/p/what-comes-next-with-reinforcement
status: 200
content_type: text/html; charset=utf-8
topics: [RL Scaling Laws (ScaleRL)]
sections: [Training & Post-training]
fetched_at: 2026-04-10T01:44:03.559978+00:00
---

# What comes next with reinforcement learning

## 원본 URL

https://www.interconnects.ai/p/what-comes-next-with-reinforcement

## 추출 본문

What comes next with reinforcement learning

SubscribeSign in

What comes next with reinforcement learning

Scaling RL, sparse rewards, continual learning, and the progress wall when pretraining really stops.

Nathan Lambert

Jun 09, 2025

74

2

15

Share

Article voiceover

0:00

-13:53

Audio playback is not supported on your browser. Please upgrade.

First, some housekeeping. The blog’s paid discord (access or upgrade here) has been very active and high-quality recently, especially parsing recent AI training tactics like RLVR for agents/planning. If that sounds interesting to you, it’s really the best reason to upgrade to paid (or join if you’ve been paying and have not come hung out in the discord).Second, I gave a talk expanding on the content from the main technical post last week, A taxonomy for next-generation reasoning models, which you can also watch on the AI Engineer World’s Fair page within the full track. My talk was one of 7 or 8 across the full day, which was very enjoyable to be at, so I am honored to have won “best speaker” for it.

Three avenues to pursue now that RL works

The optimistic case for scaling current reinforcement learning with verifiable rewards (RLVR) techniques to next-generation language models, and maybe AGI or ASI depending on your religion, rests entirely on RL being able to learn on ever harder tasks. Where current methods are generating 10K-100K tokens per answer for math or code problems during training, the sort of problems people discuss applying next generation RL training to would be 1M-100M tokens per answer. This involves wrapping multiple inference calls, prompts, and interactions with an environment within one episode1 that the policy is updated against.

The case for optimism around RL working in these new domains is far less clear compared to current training regimes which largely are rewarding the model for how it does on one interaction with the environment — one coding task checked against tests, one math answer, or one information retrieval. RL is not going to magically let us train language models end-to-end that make entire code-bases more efficient, run scientific experiments in the real world, or generate complex strategies. There are major discoveries and infrastructure improvements that are needed.

When one says scaling RL is the shortest path to performance gains in current language models it implies scaling techniques similar to current models, not unlocking complex new domains. 

This very-long-episode RL is deeply connected with the idea of continual learning, or language models that get better as they interact with the real world. While structurally it is very likely that scaling RL training is the next frontier of progress, it is very unclear if the type of problems we’re scaling to have a notably different character in terms of what they teach the model. Throughout this post, three related terms will be discussed:

Continuing to scale RL for reasoning — i.e. expanding upon recent techniques with RLVR by adding more data and more domains, without major algorithmic breakthroughs.

Pushing RL to sparser domains — i.e. expanding upon recent techniques by training end-to-end with RL on tasks that can take hours or days to get feedback on. Examples tend to include scientific or robotics tasks. Naturally, as training on existing domains saturates, this is where the focus of AI labs will turn.

Continual learning with language models — i.e. improvements where models are updated consistently based on use, rather than finish training and then served for inference with static weights.

Share

At a modeling level, with our current methods of pretraining and post-training, it is very likely that the rate of pretraining runs drops further and the length of RL training runs at the end increases.

These longer RL training runs will naturally translate into something that looks like “continual learning” where it is technically doable to take an intermediate RL checkpoint, apply preference and safety post-training to it, and have a model that’s ready to ship to users. This is not the same type of continual learning defined above and discussed later, this is making model releases more frequent and training runs longer.

This approach to training teams will mark a major shift where previously pretraining needed to finish before one could apply post-training and see the final performance of the model. Or, in cases like GPT-4 original or GPT-4.5/Orion it can take substantial post training to wrangle a new pretrained model, so the performance is very hard to predict and the time to completing it is variable. Iterative improvements that feel like continual learning will be the norm across the industry for the next few years as they all race to scale RL.

True continual learning, in the lens of Dwarkesh Patel is something closer to the model being able to learn from experience as humans do. A model that updates its parameters by noticing how it failed on certain tasks. I recommend reading Dwarkesh’s piece discussing this to get a sense for why it is such a crucial missing piece to intelligence — especially if you’re motivated by making AIs have all the same intellectual skills as humans. Humans are extremely adaptable and learn rapidly from feedback.

Dwarkesh Podcast

Why I don’t think AGI is right around the corner

Read more

10 months ago · 855 likes · 95 comments · Dwarkesh Patel

Related is how the Arc Prize organization (behind the abstract reasoning evaluations like ARC-AGI 1, 2 and 3) is calling intelligence “skill acquisition efficiency.” 

Major gains on either of these continual learning scenarios would take an algorithmic innovation far less predictable than inference-time scaling and reasoning models. The paradigm shift of inference-time scaling was pushing 10 or 100X harder on the already promising direction of Chain of Thought prompting. A change to enable continual learning, especially as the leading models become larger and more complex in their applications, would be an unexpected scientific breakthrough. These sorts of breakthroughs are by their nature unpredictable. Better coding systems can optimize existing models, but only human ingenuity and open-ended research will achieve these goals. 

Challenges of sparser, scaled RL

In the above, we established how scaling existing RL training regimes with a mix of verifiable rewards is ongoing and likely to result in more frequent model versions delivered to end-users. Post-training being the focus of development makes incremental updates natural.

On the other end of the spectrum, we established that predicting (or trying to build) true continual learning on top of existing language models is a dice roll.

The ground in the middle, pushing RL to sparser domains, is far more debatable in its potential. Personally, I fall slightly on the side of pessimism (as I stated before), due to the research becoming too similar to complex robotics research, where end-to-end RL is distinctly not the state-of-the-art method.

Interconnects is a reader-supported publication. Consider becoming a subscriber.

Subscribe

The case for

The case where sparser, scaled RL works is quite similar to what has happened with the past generations of AI models, but with the infrastructure challenges we are overcoming being a bit bigger. This is continuing the march of “deep learning works,” where we move RL training to be further off-policy and multi-datacenter. In many ways RL is better suited to multi-datacenter training due to it having multiple clusters of GPUs for acting, generation, and learning, policy gradient updates that don’t need to communicate as frequently as the constant updates of pretraining with next-token prediction.

There are two key bottlenecks here that will fall:

Extremely sparse credit assignment. RL algorithms we are using or discovering can attribute per-token lessons well across generations of millions of tokens. This is taking reward signals from the end of crazily long sequences and doing outcome supervision to update all tokens in that generation at once.

Extremely off-policy RL. In order to make the above operate at a reasonable speed, the RL algorithms learning are going to need to learn from batches of rollouts as they come in from multiple trial environments. This is different than basic implementations that wait for generations from the current or previous batch to then run policy updates on. This is what our policy gradient algorithms were designed for.

As the time to completion becomes variable on RL environments, we need to shift our algorithms to be stable with training on outdated generations — becoming like the concept of a replay buffer for LM training.

Between the two, sparsity of rewards seems the most challenging for these LM applications. The learning signal should work, but as rewards become sparser, the potential for overoptimization seems even stronger — the optimizer can update more intermediate tokens in a way that is hard to detect in order to achieve the goal. 

Overcoming sparsity here is definitely similar to what happened for math and code problems in the current regime of RLVR, where process reward models (PRMs) with intermediate supervision were seen as the most promising path to scaling. It turned out that scaling simpler methods won out. The question here is, will the simpler methods even work at all?

The case against

There are always many cases against next-generation AI working, as it’s always easy to come up with a narrative against complexity in progress. There are a few key points. The first is that scaling to sparser tasks is already not working, or we don’t know how to actually set up the rewards in a way that encourages the model to get meaningfully better at long tasks.

For example, consider Deep Research, a new product that is “trained with RL” and generates millions of tokens per query. How exactly does the RL work there? OpenAI lightly described the training method for Deep Research in their launch blog post (emphasis mine):

Deep research independently discovers, reasons about, and consolidates insights from across the web. To accomplish this, it was trained on real-world tasks requiring browser and Python tool use, using the same reinforcement learning methods behind OpenAI o1, our first reasoning model. While o1 demonstrates impressive capabilities in coding, math, and other technical domains, many real-world challenges demand extensive context and information gathering from diverse online sources. Deep research builds on these reasoning capabilities to bridge that gap, allowing it to take on the types of problems people face in work and everyday life.

There are two key points. First, they say they train on browser and tool-use tasks with the same infrastructure as o1. Second, they focus on how these capabilities can bridge the gap to harder problems — not that the capabilities are being learned on the harder problems themselves.

How to read this training method, which is likely similar for agents like Claude Code or Codex, is that current RL methods are helping the models get more robust at individual tasks that make up a longer trajectory rather than being trained on the end result of the trajectory itself. The final long-horizon behavior is put together with prompting and letting the model run longer, not sparse credit assignment. In the case of Deep Research the final measure of performance would actually look far closer to human preferences than verifiable rewards, and a large portion of that applies for Claude Code as well, where multiple solutions could solve a problem and it falls to human taste to say which is the best.

There’s a much clearer path for RL training going from human preferences through verifiable rewards and back to human preferences again, rather than pushing further into sparser, harder verifiable domains.

Second, recent RL research always shows that many interactions with a problem or world are needed to solve challenging tasks. In the RLVR domain for math or code the models are generally shown many similar problems multiple times. In the standard RL domains, standard practice is to create simulators that allow massively parallel learning agents (as discussed in the Interconnects Interview with Eugene Vinitsky). The more challenging the problem we’re attempting to deploy RL to, the less these conditions of parallelism or multiple tries can apply. 

Whether or not it works, the thing to try is carefully curating the first trajectories to train the models on. This is what OpenAI did to create o1, and it took so long that we got all the Q* rumors in their early experiments. These manual trajectories of optimal samples from Deep Research or coding agents will definitely help performance, but it isn’t clear if they’ll serve as a “warm start” for the model to then be trained extensively with bigger RL.

Is continual learning something we should want?

Dwarkesh’s goal, in many ways, is an AI that learns after interacting with you in a permanent way. This comes with unintended side-effects and would be borderline dangerous. The current AI systems that learn in a “continual” way via trial-and-error with the user are algorithmic feeds. Most people remark how incredible it is for TikTok to learn your interests in real time in front of you, often capturing an essence within minutes.

When it comes to AI models with the latent intelligence that is superhuman in many aspects of understanding, unlocking a rapid and personalized feedback loop back to some company owned AI system opens up all other types of dystopian outcomes. For a long time I’ve written that AI models have a higher risk potential in terms of social outcomes because the modalities they interact with us in are far more personal — e.g. private messaging. Combine a far stronger optimizer with a far more intimate context and that is a technology I don’t even want to try.

There are alternatives that still reap the upside. Despite the bumpy rollout, ChatGPT features that just remember your past interactions can go a long way to act like continual learning. The model can reference past chats and times you corrected it in order to avoid repeating the same mistake, even though the underlying weights don’t need to update. If that isn’t powerful enough, we can wait for the technology to become efficient enough for local models to learn continually as we interact with them. Both of these would dampen the risk potential of super-targeted AI.

Personalization is the softer framing of this that is more compelling. Continual learning is the framing that suits the leading model providers because their training algorithms will be the ones benefiting from all of the interactions. Personalization doesn’t suit the frontier AI laboratories well because their economies of scale push them to have few models for many users. If open models keep up, we should be able to create a future of specialized, “n of 1” models for specific users. 

Without corporate misaligned incentives, I’d be happy to have continual learning, but on the path we’re going down I’d rather not have it be an option presented to the masses at all. 

As AI is going to be so powerful as a standalone entity, breaking some of the symbiotic links will be good for adding friction that makes the technology easier to steer towards good outcomes. In short, be wary of wishing for end-to-end (reinforcement) learning when you’re part of the environment.2 It’s a destiny to dystopia. 

Subscribe

Aside: Revisiting AI usage

Finally, while in SF I was chatting with many people about the theme of my post, People use AI more than you think, which is framed as simple AI revenue and usage growth. The core idea of the article should’ve been expanded, as not only do people use AI a lot already, but most of the most popular AI services are supply constrained just like Nvidia. When you see revenue forecasts from OpenAI or Anthropic to The Information, it’s best to believe them for scaling existing product offerings. They know when they’re getting more capacity online. The new higher-revenue offerings are in flux. 

For example, Sundar Pichai acknowledged this in his recent appearance on the Lex Fridman podcast:

I think it's compute-limited in this sense, right, like, you know, part of the reason you've seen us do Flash, Nano, Flash, and Pro models, but not an Ultra model, it's like for each generation, we feel like we've been able to get the Pro model at like, I don't know, 80, 90% of Ultra's capability, but Ultra would be a lot more, like slow, and a lot more expensive to serve. But what we've been able to do is to go to the next generation and make the next generation's Pro as good as the previous generation's Ultra.

This will very likely continue.

1

The term of art used in RL to indicate one trial within the environment for the agent. Also called rollout or trial.

2

A topic I co-authored an entire policy whitepaper on in 2022.

74

2

15

Share

PreviousNext

Discussion about this post

CommentsRestacks

juluc

Jun 9, 2025

Liked by Nathan Lambert

Hi Nathan, great read, few Qs: 

When scaling from 10K to 1M+ token episodes, are labs experimenting with any form of "semantic coherence tracking" during training? It seems like with such sparse rewards, you'd want some signal that the model's reasoning is staying conceptually consistent vs. just wandering until it stumbles on a solution (connects to your last blog post)?

Or is this why they're decomposing into subtasks - because tracking/rewarding coherence across million-token trajectories would be computationally way too much (esp. compared to just training on more samples?)

If its not compute:

The fact that current methods are 'helping models get more robust at individual tasks' rather than true end-to-end learning suggests maybe the real bottleneck isn't just sparse rewards but probs maintaining meaningful learning signals across such long contexts - or do they want users to build their own scaffolds, optimizing models for benchmark performance.

Reply

Share

1 reply by Nathan Lambert

1 more comment...

TopLatestDiscussions

No posts

Ready for more?

Subscribe

© 2026 Interconnects AI, LLC · Privacy ∙ Terms ∙ Collection notice

 Start your SubstackGet the app

Substack is the home for great culture

 This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts
