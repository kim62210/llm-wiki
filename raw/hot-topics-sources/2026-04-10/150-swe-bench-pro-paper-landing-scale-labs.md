---
title: SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs
source_url: https://labs.scale.com/papers/swe_bench_pro
final_url: https://labs.scale.com/papers/swe_bench_pro
status: 200
content_type: text/html; charset=utf-8
topics: [SWE-bench Pro]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:45.112899+00:00
---

# SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs

## 원본 URL

https://labs.scale.com/papers/swe_bench_pro

## 추출 본문

SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs

[PAPERS][BLOG][LEADERBOARDS][SHOWDOWN]⌘K
⌘K

BACK

AgentsSafety, Evaluation and Alignment9/19/2025

SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

Xiang Deng*, Jeff Da*, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean Hendryx, Zifan Wang, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, Brad Kenstler *Co-first author and equal contributions.

View paper

SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

We introduce SWE-BENCH PRO, a substantially more challenging benchmark that builds upon the best practices of SWE-Bench [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-Bench. SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools. The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups. Problems in the held-out and the commercial set are not publicly accessible, but we release results on the commercial set. Our benchmark features long-horizon tasks that may require hours to days for a professional software engineer to complete, often involving patches across multiple files and substantial code modifications. All tasks are human-verified and augmented with sufficient context to ensure resolvability.

In our evaluation of widely used coding models, under a unified scaffold, we observe that their performance on SWE-BENCH PRO remains below 25% (Pass@1), with GPT-5 achieving the highest score to date at 23.3%. To better understand these limitations, we cluster the failure modes observed in the collected agent trajectories for a clearer characterization of the error patterns exhibited by current models. Overall, SWE-BENCH PRO provides a contamination-resistant testbed that more faithfully captures the complexity and diversity of real-world software development, advancing the pursuit of truly autonomous software engineering agents at a professional level.

Scale Labs Newsletter

Research, benchmarks, and insights — delivered to your inbox.

Subscribe to newsletter

Copyright 2026Scale Inc.All rights reserved.

TermsPrivacy
