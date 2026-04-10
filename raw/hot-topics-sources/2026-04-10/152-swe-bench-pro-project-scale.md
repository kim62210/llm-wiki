---
title: SWE-Bench Pro
source_url: https://scaleapi.github.io/SWE-bench_Pro-os
final_url: https://scaleapi.github.io/SWE-bench_Pro-os/
status: 200
content_type: text/html; charset=utf-8
topics: [SWE-bench Pro]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:45.199684+00:00
---

# SWE-Bench Pro

## 원본 URL

https://scaleapi.github.io/SWE-bench_Pro-os

## 추출 본문

SWE-Bench Pro

SWE-Bench Pro

Evaluating AI Agents on Challenging Long-Horizon SWE Tasks

🏆 Official Leaderboard📄 Paper💻 Code💾 Data📤 Submit

Leaderboard
Model% Resolved(+/-)Link🥇SWE-Agent + claude-4-5-Sonnet43.72🔗🥈SWE-Agent + claude-4-Sonnet42.70🔗🥉SWE-Agent + claude-4-5-haiku39.45🔗SWE-Agent + gpt-5-2025-08-07 (High)36.30🔗SWE-Agent + glm-4.535.52🔗SWE-Agent + kimi-k2-instruct27.67🔗SWE-Agent + gpt-oss-120b16.20🔗

 Note that these results are initial runs and subject to change, pending an official announcement from Scale. Models are run with an uncapped cost and with a turn limit of 250.

 The (+/-) column shows the 95% confidence interval (margin of error) for each score, calculated using binomial proportion statistics (total problems: 730).
 

About

 We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH, but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools. The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups. Problems in the held-out and the commercial set are not publicly accessible, but we release results on the commercial set. Our benchmark features long-horizon tasks that may require hours to days for a professional software engineer to complete, often involving patches across multiple files and substantial code modifications. All tasks are human-verified and augmented with sufficient context to ensure resolvability. In our evaluation of widely used coding models, under a unified scaffold, we observe that their performance on SWE-Bench PRO remains below 25% (Pass@1), with GPT-5 achieving the highest score to date at 23.3%. To better understand these limitations, we cluster the failure modes observed in the collected agent trajectories for a clearer characterization of the error patterns exhibited by current models. Overall, SWE-BENCH PRO provides a contamination-resistant testbed that more faithfully captures the complexity and diversity of real-world software development, advancing the pursuit of truly autonomous software engineering agents at a professional level.
 

Citation

 If you found SWE-bench Pro helpful for your work, please cite as follows:
 

@inproceedings{Deng2025SWEBenchPC,
 title={SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?},
 author={Xiang Deng and Jeff Da and Edwin Pan and Yan He and Charles Ide and Kanak Garg and Niklas Lauffer and Andrew Park and Nitin Pasari and Chetan Rane and Karmini Sampath and Maya Krishnan and Srivatsa Kundurthy and Sean M. Hendryx and Zifan Wang and Chen Bo Calvin Zhang and Noah Jacobson and Bing Liu and Brad Kenstler},
 year={2025},
 url={https://api.semanticscholar.org/CorpusID:281421060}
}

@inproceedings{jimenez2024swebench,
 title={SWE-bench: Can Language Models Resolve Real-world Github Issues?},
 author={Carlos E Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pei and Ofir Press and Karthik R Narasimhan},
 booktitle={The Twelfth International Conference on Learning Representations},
 year={2024},
 url={https://openreview.net/forum?id=VTF8yNQM66}
}
