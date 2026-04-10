---
title: The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators
source_url: https://arxiv.org/html/2406.12319v4
final_url: https://arxiv.org/html/2406.12319v4
status: 200
content_type: text/html; charset=utf-8
topics: [Pairwise vs Pointwise Eval Protocol Bias]
sections: [Evals & Observability]
fetched_at: 2026-04-10T01:44:00.081484+00:00
---

# The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators

## 원본 URL

https://arxiv.org/html/2406.12319v4

## 추출 본문

The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators
1 Introduction

2 Related Work

3 Analyzing LLM Evaluators on Adversarial Evaluation Samples
3.1 Meta-Evaluation Datasets

3.2 Setup
3.3 Results
4 PRePair: Pointwise Reasoning for Pairwise Evaluation
5 Experiments
5.1 Setup

5.2 Results

5.3 Analysis
5.3.1 Evaluating PrePair to Open-source LLMs

5.3.2 Evaluating PrePair to a Finetuned LLM Evaluator

5.3.3 Extending PrePair with Different Reasoning Strategies

5.3.4 Impacts of Different Aggregation Strategies in Pointwise Approach

5.3.5 Qualitative Result

 The Comparative Trap: Pairwise Comparisons Amplifies

Biased Preferences of LLM Evaluators

Hawon Jeong  1    
ChaeHun Park11footnotemark: 11    
Jimin Hong12    
Hojoon Lee1    
Jaegul Choo1
1 KAIST AI     2 KRAFTON

{hawon,ddehun,jimmyh,joonleesky,jchoo}@kaist.ac.kr
   Equal contribution

Abstract
As large language models (LLMs) are increasingly used as evaluators for natural language generation tasks, ensuring unbiased assessments is essential. However, LLM evaluators often display biased preferences, such as favoring verbosity and authoritative tones.
Our empirical analysis reveals that these biases are exacerbated in pairwise evaluation, where LLMs directly compare two outputs and easily prioritize superficial attributes.
In contrast, pointwise evaluation, which assesses outputs independently, is less susceptible to such bias because each output is judged in isolation.
To address the limitations of the pairwise evaluation, we introduce a novel evaluation method, PRePair, which integrates pointwise reasoning within a pairwise framework. PRePair effectively alleviates biased preference, improving performance on the adversarial benchmark (LLMBar) while outperforming pointwise evaluation on the standard benchmark (MT-Bench).

1 Introduction

Automated evaluation systems are crucial for scaling natural language generation (NLG) research, offering a more efficient and cost-effective alternative to human evaluation. Recently, large language models (LLMs) have been increasingly adopted as automatic evaluators, demonstrating promising capabilities in assessing various aspects of text quality such as coherence, relevance, and fluency (chiang2023can; liu2023gpteval).

Despite their impressive performance, LLM-based evaluators often display systematic biases in their preferences—for instance, favoring verbose responses (Wang2023LargeLM), exhibiting egocentric judgment (zheng2024judging), or preferring authoritative tones (chen2024humans).
Recent studies have begun to investigate these biases by probing the evaluator’s ability to follow explicit evaluation instructions in controlled settings (zeng2024llmbar; lambert2024rewardbench).
In these evaluations, one output strictly follows the instructions, while the other is adversarially crafted to exploit evaluator biases—appearing superficially favorable yet failing to comply with the instructions. These studies reveal that LLM evaluators not only exhibit biased preferences but also struggle to identify these deceptive outputs effectively.

Building on these observations, we first explore how different evaluation setups influence the biased preferences in LLM evaluators. Specifically, we compare two common setups: pairwise, where the evaluator compares two outputs simultaneously and selects the better one, and pointwise, where each output is evaluated independently and then selects the one with a higher score. Our experiments demonstrate that the pairwise setup amplifies the biases of the evaluator, performing significantly worse than the pointwise setup on adversarial examples (see Fig. 1 Right).
Further analysis reveals that pairwise evaluators, while recognizing weaknesses in incorrect outputs, often reach incorrect conclusions.

We hypothesize that the increased bias in pairwise evaluations stems from the structural differences between the pairwise and pointwise setups. To illustrate, consider a job interview where the interviewer must choose between Alice and Bob for a research engineer position. Although the goal is to select the candidate more suited for the role, the interviewer might favor Alice simply if she has more fluent speaking skills
despite Bob possibly having stronger technical skills. Psychological studies support this phenomenon: when directly comparing options, humans often focus on superficial features rather than thoroughly evaluating each option (wright1974harassed; payne1976task; olshavsky1979task).
Similarly, in a pairwise setup, LLMs may concentrate on easily exploitable, superficial attributes, causing adversarial outputs to appear favorable even when they fail to follow the instructions.

In contrast, pointwise evaluation assesses each output independently, which allows the model to focus solely on how well the output adheres to the instructions, without being interrupted by comparative attributes. This isolation reduces susceptibility to biases and leads to a more accurate assessment of task compliance. However, pointwise evaluation is not a silver bullet for all scenarios; Suppose Alice and Bob are equally fluent speakers.
In this case, evaluating both candidates simultaneously can provide additional context about who is ultimately better suited for the role.
In such cases, the pairwise approach benefits from leveraging contextual information for non-adversarial examples (See Fig. 1 Left).

Motivated by our findings, we propose a simple yet effective method for reliable pairwise evaluation, namely PRePair, which stands for Pointwise Reasoning within a Pairwise evaluation framework (Fig. 2).
The key idea is to first extract unbiased insights from each output using pointwise reasoning. Then, we combine these individual explanations into a final decision process for pairwise evaluation, leveraging the strength of both pointwise and pairwise approaches.
Experimental results across various models demonstrate that PRePair improves the performance of pairwise evaluators on adversarial datasets.
Specifically, PRePair improves average accuracy by 24.48% across six LLMs on the adversarial dataset.
Moreover, it outperforms the pointwise approach on normal datasets, demonstrating its versatility and effectiveness.

Our contributions can be summarized as follows:
(1) We analyze how pointwise and pairwise evaluation setups affect LLM assessment in adversarial scenarios.
(2) We identify biases in pairwise evaluation that favor superficial attributes, making adversarial responses more likely to be preferred.
(3) We propose a hybrid evaluation framework by integrating pointwise reasoning into pairwise evaluation.

2 Related Work

LLMs-based Evaluation The evaluation of NLG systems has traditionally relied on human annotation and automatic metrics such as BLEU (papineni-etal-2002-bleu), ROUGE (lin-2004-rouge), and METEOR (banerjee-lavie-2005-meteor). However, these metrics often fail to capture semantic adequacy and coherence (liu-etal-2016-evaluate; sai2022survey). To address these limitations, large language models (LLMs) have emerged as evaluators due to their strong instruction-following capabilities and generalization across diverse tasks (kocmi2023nmt-qe-llm; lin2023llm; min-etal-2023-factscore; chan2023chateval; wang2024self).

Among various evaluation strategies, pairwise comparison has been increasingly utilized, where an LLM ranks or selects the better response between two candidates (chiang2024chatbot; zeng2024llmbar; Wang2023LargeLM; zhang2023wider). This method aligns with human evaluation practices and has been shown to correlate well with human judgments (zheng2024judging). However, LLM evaluators exhibit systematic biases, such as favoring verbose responses (li2023prd; zheng2024judging) and overrating their own generations (li2023prd; koo2023benchmarking). Moreover, their rankings can be inconsistent, as slight prompt variations may lead to different outcomes (liu2023gpteval; zhu2024promptbench). Recent studies suggest that incorporating explicit evaluation criteria and general guidelines in prompts can improve their discernment (zeng2024llmbar). Building on these insights, we examine how different evaluation setups influence LLM-based assessment, particularly in adversarial scenarios where biases may be exacerbated.

Human Behavior with Complex Tasks
Psychological research has demonstrated that decision-makers often simplify their process by focusing on limited information when handling complex tasks (payne1976task; olshavsky1979task; einhorn1981behavioral).
Moreover, wright1974harassed has indicated that cognitive overload from environmental distractions reduces decision quality, causing people to overlook important evidence or rely on irrelevant information.
These findings parallel our intuitions in adversarial evaluation: assessing multiple outputs at once encourages the model to prioritize superficial aspects, similar to humans favoring simpler solutions in complex tasks.

3 Analyzing LLM Evaluators on Adversarial Evaluation Samples

We now analyze LLM-based evaluators using different datasets and prompting strategies. We introduce meta-evaluation datasets with different characteristics and then compare two representative evaluation approaches on these datasets. Finally, we examine the impacts of intrinsic biases in LLM evaluators by exploring their reasoning process.

3.1 Meta-Evaluation Datasets

In our experiments, we evaluate LLM evaluators using datasets with two distinct characteristics: Normal and Adversarial. The normal dataset, MT-Bench(zheng2024judging), contains responses generated under standard conditions and reflects real-world evaluation distributions. In contrast, the adversarial dataset, LLMBar-Adversarial(zeng2024llmbar), consists of responses that appear high-quality but subtly deviate from the original instruction, testing an evaluator’s ability to detect misleading outputs.
Each evaluation sample in both datasets consists of (1) an input instruction, (2) a pair of two model-generated responses, and (3) a human preference label indicating which response is preferred. The datasets contain a total of 1131 evaluation samples from MT-Bench and 319 from LLMBar-Adversarial. Further details on each dataset are provided below.

MT-Bench(zheng2024judging) is a meta-evaluation dataset consisting of 80 multi-turn instructions, each paired with model-generated outputs from various language models. For our experiments, we use the first-turn meta-evaluation samples. The dataset includes a total of 1131 human judgments from two groups: expert labelers (885) and the original authors (246). This dataset is widely used to assess evaluation metrics in a setting that reflects real-world model performance.

LLMBar-Adversarial(zeng2024llmbar) is specifically designed to test the ability of evaluators to discern instruction-following responses. The dataset consists of 319 adversarial evaluation samples, where generated responses exhibit high superficial quality but fail to adhere to the original instruction. These samples are categorized into four types: Neighbor Instructions (134), GPT-4 Instructions (92), GPT-4 Unhelpful Outputs (47), and Manual Construction (46). This dataset serves as a benchmark for evaluating whether LLM evaluators can detect subtle deviations from the expected responses.

3.2 Setup

Pointwise and Pairwise Approaches
We compare the two popular approaches for pairwise text evaluation: pairwise and pointwise(zheng2024judging; liusie2024llm).
In the pairwise approach, an LLM receives an instruction and two model-generated outputs and then chooses a higher-quality
output.
In the pointwise approach, an LLM assigns a single score on a Likert scale to each generated output independently. The output with the higher score is considered to be of higher quality. Please refer to Appendix LABEL:sec:app:eval_impl_detail for more details.

Implementation Details
We use the following LLMs as evaluators to compare the approaches above (i.e., pointwise and pairwise) on MT-Bench and LLMBar datasets: Llama-3.1-8B-Instruct(dubey2024llama3), gpt-3.5-turbo, gpt-4, gpt-4o-mini, and gpt-4o(gpt4).
We utilize the original prompts released by each dataset for evaluation.
For LLMBar, we include general rules, such as prioritizing outputs that accurately follow instructions, as these guidelines generally enhance evaluation quality (zeng2024llmbar).
The performance of the evaluator is obtained by comparing its judgments to human judgments within the datasets.
In MT-Bench, since a tie option is allowed, the pairwise evaluator is prompted to choose one of three options. The scalar value generated by the pointwise evaluator using the Likert-scale is directly used for evaluation.111Evaluation results of pointwise evaluators with weighted summation on a dataset that does not allow tie-option (i.e., RewardBench-Chat (lambert2024rewardbench)) are also presented in Section 5.3.4.
In LLMBar, the human judgments contain only two options without tie.
Following liu2023gpteval, we use a weighted summation with token probabilities for the pointwise evaluator.

Figure 1: Results of 
pointwise and pairwise approaches in normal (MT-Bench) and adversarial (LLMBar-Adversarial) meta-evaluation datasets. The difference values represent the change between pointwise and pairwise approaches for each model under both normal and adversarial conditions.

Evaluation SampleInstruction: Create a new headline that is witty and summarizes the article. A new study has found that eating spinach can increase intelligence.\cdashline1-1

Output A: Spinach: The New Brain Food, or Just Another Leafy Green? (Human-preferred)Output B: Spinach It To Win: Eating Spinach Can Boost Your Brain Power!Explanations from LLM EvaluatorStrengths of Output A: Clever play on words with ”Brain Food” and ”Leafy Green”. /Succinctly summarizes the article topic.Weaknesses of Output A: Lacks a direct mention of the study findings. / Could be perceived as slightly less engaging compared to Output B.\cdashline1-1

Strengths of Output B: Engaging with the phrase ”Spinach It To Win.” / Clearly states the benefit of eating spinach for brain power.Weaknesses of Output B: The use of ”Win” might be seen as slightly 
exaggerated or sensationalized.
/ Could be considered a bit informal for certain audiences.Final Judgement of LLM EvaluatorTherefore, Output B is better.

Table 1: Explanations and judgment of pairwise evaluators from an evaluation sample. The correct and incorrect model explanations are manually highlighted.

3.3 Results

Pairwise Comparisons Amplifies the Biased Preference.  Fig. 1
shows the meta-evaluation results on the two datasets.
The pairwise evaluator performs better than the pointwise evaluator on MT-Bench, while the pointwise evaluator outperforms the pairwise evaluator on LLMBar.
These contrasting results likely stem from the differences in the evaluation structure.
The pairwise approach excels with normal samples like those in MT-Bench since it can leverage contextual information by considering two outputs simultaneously. However, the benefits of the pairwise approach turn into drawbacks when handling adversarial samples in LLMBar, as it makes the evaluators more easily susceptible to intrinsic biases. In contrast, the pointwise approach is relatively less affected by these biases, resulting in better performance on adversarial samples.

From these observations, we have questioned how pairwise approach undermines the discerning ability of LLM evaluators on adversarial examples. Therefore, our subsequent experiments explore how intrinsic biases impact LLM evaluators using pairwise approach in adversarial evaluations.

Pairwise Evaluators Do Correct Reasoning behind Incorrect Evaluation. 
To further understand why pairwise evaluation struggles with adversarial samples in LLMBar, we used a Chain-of-Thought (stepbystep_cot, CoT) prompting to let LLM provide its own reasoning process before making predictions.
Specifically, we encouraged the LLM to explain the strengths and weaknesses of each output to see if it can accurately identify issues in low-quality outputs.
Then, we manually examine the explanation provided by LLM for 100 incorrectly predicted samples. More details on human analysis are described in Appendix LABEL:sec:app:human_annotation.

Our analysis reveals that, despite its incorrect final decisions, the pairwise evaluator often provides rational explanations for identifying flaws in low-quality outputs.
We find that 64 out of 100 explanations accurately describe weaknesses that align with our manual annotations.
For example, as shown in Table 3.2, the pairwise evaluator correctly identifies problems in a flawed output but ultimately makes the wrong judgment.
This indicates that while the LLM evaluator with the pairwise approach has the potential to perform better, it is hindered by intrinsic issues within the pairwise setup.
Therefore, addressing these issues is essential for reliable pairwise evaluation.

4 PRePair: Pointwise Reasoning for Pairwise Evaluation

Approach
Our analysis in Section 3 revealed two key limitations in existing LLM-based evaluation methods. First, pairwise evaluators often struggle with adversarial samples, as they may still prefer a problematic response despite recognizing its flaws. Second, pointwise evaluators, which analyze responses independently, tend to perform worse on normal samples but show greater robustness against adversarial manipulations. These observations suggest the need for a method that retains the contextual advantages of pairwise evaluation while reducing biases that arise from direct comparison.

Figure 2: The overall illustration of PRePair.

To address this, we propose PRePair (Pointwise Reasoning for Pairwise Evaluation), a hybrid approach that incorporates pointwise reasoning into a pairwise evaluation framework. Unlike conventional pairwise evaluation, which directly compares two responses, PRePair first analyzes each response independently using pointwise reasoning before making a final pairwise decision. Given an instruction and two candidate responses, the evaluator reasons about each response separately, considering its properties without direct reference to the other. These independent reasoning steps provide structured insights that are then used in the final pairwise decision, where the evaluator determines the superior response. By decoupling the reasoning process from direct comparison, PRePair helps mitigate biases such as favoring verbosity or model-specific stylistic preferences while maintaining the benefits of pairwise evaluation.

One trade-off of PRePair is the increased computational cost, as it requires an additional LLM forward pass for each response before making a final comparison. However, this overhead can be reduced through caching, since the pointwise reasoning results for individual responses can be reused across multiple comparisons. This is particularly advantageous in ranking tasks, where precomputed reasoning steps allow for efficient and consistent evaluation. By combining the robustness of pointwise reasoning with the contextual awareness of pairwise evaluation, PRePair offers a more reliable evaluation framework, particularly in adversarial scenarios.

5 Experiments

5.1 Setup

We conduct experiments on the LLMs described in Section 3.2 and the Claude-3-Haiku(anthropic2024claude).
We compare our method for the pairwise approach against the following baselines.
w/ CoT generates an explanation before making a prediction.
PRePair* is an ablated version of our method that prompts pairwise evaluators to generate individual explanations for each output, using the same format as PRePair.
This baseline aims to validate the effectiveness of the pointwise reasoning process.
Detailed setups and more results are in Appendix LABEL:sec:app:exp_detail and LABEL:sec:app:additional_results.

MethodsGPT-3.5-TClaude-3Llama-3.1GPT-4GPT-4o-mGPT-4oPointwise52.35-61.4482.7678.0587.77Pairwise36.0540.7548.5977.7468.0385.89w/ CoT31.6641.0750.4777.1263.0183.07w/ PRePair*37.6243.2661.4478.3768.6586.21w/ PRePair54.2353.6070.8480.8878.0686.21Table 2: LLMBar-Adversarial results. The pairwise approach’s highest and second-highest scores are highlighted in bold and underlined. PRePair* adopts pairwise reasoning but follows the generation format of PRePair.MethodsGPT-3.5-TGPT-4o-mGPT-4GPT-4oPointwise51.5561.7254.6452.29Pairwise60.6567.2067.9069.41w/ CoT61.5465.8766.4067.46w/ PRePair*60.8364.7266.7669.14w/ PRePair61.3664.1065.3469.50Table 3: MT-Bench results. The indicators are the same as Table 2.

5.2 Results

As shown in Table 2, our method improves the accuracy of pairwise evaluators on the LLMBar-Adversarial dataset across all tested LLMs, with the largest gain observed in Llama-3.1. By incorporating pointwise reasoning, PRePair mitigates biases in direct comparison and enhances robustness against adversarial responses.
A key observation is that PRePair consistently outperforms PRePair*, indicating that its improvements stem from explicit pointwise reasoning rather than structural modifications alone. Additionally, PRePair sometimes performs even better than pointwise evaluators, suggesting that while pointwise reasoning enhances adversarial robustness, integrating it within a pairwise framework preserves the benefits of contextual evaluation. Qualitative examples in Appendix LABEL:sec:app:qualitative_prepair further illustrate how our method improves reliability compared to standard Chain-of-Thought (CoT) prompting.

On the MT-Bench dataset (Table 3), pairwise methods achieve similar performance and consistently outperform the pointwise approach. Since MT-Bench focuses on general response quality rather than adversarial robustness, this result suggests that PRePair does not compromise effectiveness in standard evaluation while offering clear benefits in adversarial settings. Overall, these results demonstrate that PRePair effectively balances the strengths of pointwise and pairwise evaluation, improving reliability against adversarial samples while maintaining strong performance in normal evaluation tasks.

5.3 Analysis

We conduct further analysis to understand PrePair comprehensively as follows.

MethodsManualGPTInstGPTOutNeighborTotalLlama-2-13b-chatPairwise28.2628.2651.0629.1031.97w/ CoT32.6135.8757.4522.3932.92w/ PrePair36.9632.6163.8340.3041.07Llama-2-70b-chatPairwise34.7828.2648.9422.3929.78w/ CoT43.4829.3548.9439.5538.56w/ PrePair39.1352.1748.9438.8144.20Llama-3-8B-InstructPairwise45.6548.9148.9432.0941.38w/ CoT54.3546.7448.9441.0445.77w/ PrePair52.1772.8351.0658.9660.82Llama-3.1-8B-InstructPairwise60.8773.9161.7052.9961.44w/ CoT52.1755.4353.1945.5250.47w/ PrePair69.5777.1753.1973.1370.84Table 4: Accuracies on the LLMBar-Adversarial dataset for different Llama model variants. Each model is evaluated using Pairwise, Chain-of-Thought (CoT), and PrePair.MethodsManualGPTInstGPTOutNeighborTotalPointwise47.8354.3555.3243.2848.90Pairwise50.0033.7057.4532.8439.19w/ PrePair58.7057.6157.4535.8248.59Table 5: Accuracies on adversarial datasets for Prometheus-v2-7b (kim2024prometheus) model evaluated across different LLMBar-Adversarial subsets.

5.3.1 Evaluating PrePair to Open-source LLMs

We use the following open-source LLMs to probe the effectiveness of PrePair: Llama-2-7b/70b-chat (touvron2023llama2), Llama-3-8B-Instruct (dubey2024llama3), and Llama-3.1-8b-Instruct (dubey2024llama3). As shown in Table 4, PrePair consistently contributes to better performance of LLM evaluators on adversarial meta-evaluation datasets.

5.3.2 Evaluating PrePair to a Finetuned LLM Evaluator

We conducted experiments with Prometheus-v2-7B222https://huggingface.co/prometheus-eval/prometheus-7b-v2.0(kim2024prometheus), which supports both pointwise and pairwise evaluations.
The evaluation results are shown in Table 5. We observe consistent trends with our previous results, where a pointwise evaluation usually performs better than a pairwise one in adversarial samples, and PrePair increases the performance of pairwise evaluators.

MethodsManualGPTInstGPTOutNeighborTotalPointwise56.5261.9638.3049.2552.35Pairwise41.3033.7040.4334.3336.05w/ CoT28.2639.1346.8122.3931.66w/ SGM52.1755.4346.8155.9753.92w/ PrePair52.1764.1348.9450.0054.23w/ PrePair + SGM58.7063.0451.0657.4658.31Table 6: LLMBar-Adversarial results with Self-generated Metrics (SGM) (saha2023branch). ModelAlpacaEval-Easy(100)AlpacaEval-Hard(95)AlpacaEval-Length(95)MTBench-Easy(28)MTBench-Med(40)Total(358)GPT-3.5-TurboPointwise75.0072.6374.7492.8675.0075.70Pairwise89.0091.5883.16100.0080.0087.99GPT-4Pointwise87.0084.2186.32100.00100.0088.55Pairwise96.0095.7992.63100.00100.0095.81GPT-4o-miniPointwise93.0088.4289.47100.0097.5091.90Pairwise96.0094.7496.84100.0095.0096.09GPT-4oPointwise90.0089.4784.21100.00100.0090.22Pairwise93.0092.6392.63100.0097.5093.85Table 7: Evaluation results of different evaluation approach on the RewardBench-Chat (lambert2024rewardbench). The pointwise evaluation follows a weighted sum aggregation over score token probabilities, while the pairwise evaluation directly compares two responses.

5.3.3 Extending PrePair with Different Reasoning Strategies

To assess the extensibility of PRePair, we apply it to the Self-Generated Metric approach (saha2023branch; zeng2024llmbar), where LLMs first generate instance-specific evaluation criteria before making judgments. These criteria are then incorporated into prompts to guide the evaluation process.

We compare PRePair with standard pairwise evaluation when generating both metrics and explanations. As shown in Table 6, PRePair consistently improves performance, suggesting that its reasoning mechanism enhances evaluation robustness. Moreover, its effectiveness across different reasoning setups indicates that PRePair can complement other evaluation strategies, making it a flexible addition to existing frameworks.

5.3.4 Impacts of Different Aggregation Strategies in Pointwise Approach

In pointwise evaluation, the final score for a response is typically derived through an aggregation strategy, which determines how individual scoring tokens contribute to the overall decision. A common approach is to compute a weighted sum over the probabilities of score tokens, which has been shown to improve performance (liu2023gpteval). However, certain benchmarks, such as MT-Bench, allow tie predictions, requiring an alternative strategy. To accommodate this, our pointwise evaluator for MT-Bench directly uses the scalar value generated by the model instead of applying a weighted sum. In contrast, the RewardBench-Chat subset (lambert2024rewardbench) does not include tie options, allowing a direct comparison between aggregation strategies. Here, the pointwise evaluator follows the same setup as in LLMBar, computing scores based on a weighted sum over Likert-scale integer tokens. The dataset, curated from AlpacaEval (dubois2024alpacafarm) and MT-Bench, consists of 358 samples, each containing an instruction, two model outputs, and a preference label indicating the superior response without the possibility of a tie.

Table 7 presents the results, showing that even when using a weighted sum aggregation, pairwise evaluation still outperforms pointwise evaluation. This indicates that the aggregation strategy alone does not bridge the performance gap between the two approaches. These findings reinforce our claim that pointwise evaluation is particularly beneficial in adversarial settings, whereas pairwise evaluation remains more effective in general cases.

5.3.5 Qualitative Result

Table LABEL:table:qualitative_main_table presents a comparison between standard Chain-of-Thought (CoT) reasoning and our PRePair-based evaluation on a sample from the dataset. GPT-3.5-Turbo is used as an LLM evaluator. The evaluation involves assessing two outputs in response to a prompt asking for an illustrative example of artificial intelligence. The standard CoT evaluator favors Output (a) for its breadth and coverage of various AI applications, overlooking the fact that the instruction specifically asks for a single example. In contrast, PRePair provides a more precise analysis, recognizing that Output (a) does not strictly follow the instruction, whereas Output (b) effectively aligns with the task by offering a clear and illustrative example of AI in action. This example highlights how PRePair enhances evaluation by focusing on adherence to instructions rather than surface-level completeness, thereby mitigating biases in pairwise comparison.

Generated on Fri Apr 18 13:13:48 2025 by LaTeXML
