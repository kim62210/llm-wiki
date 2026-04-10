---
title: Alibaba Qwen Team Releases Qwen3.5 Omni: A Native Multimodal Model for Text, Audio, Video, and Realtime Interaction - MarkTechPost
source_url: https://www.marktechpost.com/2026/03/30/alibaba-qwen-team-releases-qwen3-5-omni-a-native-multimodal-model-for-text-audio-video-and-realtime-interaction
final_url: https://www.marktechpost.com/2026/03/30/alibaba-qwen-team-releases-qwen3-5-omni-a-native-multimodal-model-for-text-audio-video-and-realtime-interaction/
status: 200
content_type: text/html; charset=UTF-8
topics: [Qwen3.6-Plus]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:48.704114+00:00
---

# Alibaba Qwen Team Releases Qwen3.5 Omni: A Native Multimodal Model for Text, Audio, Video, and Realtime Interaction - MarkTechPost

## 원본 URL

https://www.marktechpost.com/2026/03/30/alibaba-qwen-team-releases-qwen3-5-omni-a-native-multimodal-model-for-text-audio-video-and-realtime-interaction

## 추출 본문

Alibaba Qwen Team Releases Qwen3.5 Omni: A Native Multimodal Model for Text, Audio, Video, and Realtime Interaction - MarkTechPost

DiscordLinkedinRedditX

Home

Open Source/Weights

AI Agents

Tutorials

Voice AI

AIDeveloper44

Promotion/Sponsorship

Search

NewsHub

NewsHub

Premium Content

Read our exclusive articles

Facebook

Instagram

X

Home

Open Source/Weights

AI Agents

Tutorials

Voice AI

AIDeveloper44

Promotion/Sponsorship

NewsHub

Search

Home

Open Source/Weights

AI Agents

Tutorials

Voice AI

AIDeveloper44

Promotion/Sponsorship

HomeEditors PickAgentic AIAlibaba Qwen Team Releases Qwen3.5 Omni: A Native Multimodal Model for Text,...

Editors Pick

Agentic AI

Technology

AI Shorts

Artificial Intelligence

Applications

Language Model

Audio Language Model

Large Language Model

Machine Learning

New Releases

OCR

Staff

Tech News

Alibaba Qwen Team Releases Qwen3.5 Omni: A Native Multimodal Model for Text, Audio, Video, and Realtime Interaction

By
Asif Razzaq
 - 

March 30, 2026

The landscape of multimodal large language models (MLLMs) has shifted from experimental ‘wrappers’—where separate vision or audio encoders are stitched onto a text-based backbone—to native, end-to-end ‘omnimodal’ architectures. Alibaba Qwen team latest release, Qwen3.5-Omni, represents a significant milestone in this evolution. Designed as a direct competitor to flagship models like Gemini 3.1 Pro, the Qwen3.5-Omni series introduces a unified framework capable of processing text, images, audio, and video simultaneously within a single computational pipeline. 

The technical significance of Qwen3.5-Omni lies in its Thinker-Talker architecture and its use of Hybrid-Attention Mixture of Experts (MoE) across all modalities. This approach enables the model to handle massive context windows and real-time interaction without the traditional latency penalties associated with cascaded systems.

Model Tiers

The series is offered in three sizes to balance performance and cost:

Plus: High-complexity reasoning and maximum accuracy.

Flash: Optimized for high-throughput and low-latency interaction.

Light: A smaller variant for efficiency-focused tasks.

https://qwen.ai/blog?id=qwen3.5-omni

The Thinker-Talker Architecture: A Unified MoE Framework

At the core of Qwen3.5-Omni is a bifurcated yet tightly integrated architecture consisting of two main components: the Thinker and the Talker.

In previous iterations, multimodal models often relied on external pre-trained encoders (such as Whisper for audio). Qwen3.5-Omni moves beyond this by utilizing a native Audio Transformer (AuT) encoder. This encoder was pre-trained on more than 100 million hours of audio-visual data, providing the model with a grounded understanding of temporal and acoustic nuances that traditional text-first models lack.

Hybrid-Attention Mixture of Experts (MoE)

Both the Thinker and the Talker leverage Hybrid-Attention MoE. In a standard MoE setup, only a subset of parameters (the ‘experts’) are activated for any given token, which allows for a high total parameter count with lower active computational costs. By applying this to a hybrid-attention mechanism, Qwen3.5-Omni can effectively weigh the importance of different modalities (e.g., focusing more on visual tokens during a video analysis task) while maintaining the throughput required for streaming services.

This architecture supports a 256k long-context input, enabling the model to ingest and reason over:

Over 10 hours of continuous audio.

Over 400 seconds of 720p audio-visual content (sampled at 1 FPS).

Benchmarking Performance: The ‘215 SOTA’ Milestone

One of the most highlighted technical claims regarding the flagship Qwen3.5-Omni-Plus model is its performance on the global leaderboard. The model achieved State-of-the-Art (SOTA) results on 215 audio and audio-visual understanding, reasoning, and interaction subtasks.

These 215 SOTA wins are not merely a measure of broad evaluation but span specific technical benchmarks, including:

3 audio-visual benchmarks and 5 general audio benchmarks.

8 ASR (Automatic Speech Recognition) benchmarks.

156 language-specific Speech-to-Text Translation (S2TT) tasks.

43 language-specific ASR tasks.

According to their official technical reports, Qwen3.5-Omni-Plus surpasses Gemini 3.1 Pro in general audio understanding, reasoning, recognition, and translation. In audio-visual understanding, it achieves parity with Google’s flagship, while maintaining the core text and visual performance of the standard Qwen3.5 series.

https://qwen.ai/blog?id=qwen3.5-omni

Technical Solutions for Real-Time Interaction

Building a model that can ‘talk’ and ‘hear’ in real-time requires solving specific engineering challenges related to streaming stability and conversational flow.

ARIA: Adaptive Rate Interleave Alignment

A common failure mode in streaming voice interaction is ‘speech instability.’ Because text tokens and speech tokens have different encoding efficiencies, a model may misread numbers or stutter when attempting to synchronize its text reasoning with its audio output.

To address this, Alibaba Qwen team developed ARIA (Adaptive Rate Interleave Alignment). This technique dynamically aligns text and speech units during generation. By adjusting the interleave rate based on the density of the information being processed, ARIA improves the naturalness and robustness of speech synthesis without increasing latency.

Semantic Interruption and Turn-Taking

For AI developers building voice assistants, handling interruptions is notoriously difficult. Qwen3.5-Omni introduces native turn-taking intent recognition. This allows the model to distinguish between ‘backchanneling’ (non-meaningful background noise or listener feedback like ‘uh-huh’) and an actual semantic interruption where the user intends to take the floor. This capability is baked directly into the model’s API, enabling more human-like, full-duplex conversations.

Emergent Capability: Audio-Visual Vibe Coding

Perhaps the most unique feature identified during the native multimodal scaling of Qwen3.5-Omni is Audio-Visual Vibe Coding. Unlike traditional code generation that relies on text prompts, Qwen3.5-Omni can perform coding tasks based directly on audio-visual instructions.

For instance, a developer could record a video of a software UI, verbally describe a bug while pointing at specific elements, and the model can directly generate the fix. This emergence suggests that the model has developed a cross-modal mapping between visual UI hierarchies, verbal intent, and symbolic code logic.

Key Takeaways

Qwen3.5-Omni uses a native Thinker-Talker multimodal architecture for unified text, audio, and video processing.

The model supports 256k context, 10+ hours of audio, and 400+ seconds of 720p video at 1 FPS.

Alibaba reports speech recognition in 113 languages/dialects and speech generation in 36 languages/dialects.

Key system features include semantic interruption, turn-taking intent recognition, TMRoPE, and ARIA for realtime interaction.

Check out the Technical details, Qwenchat, Online demo on HFandOffline demo on HF. Also, feel free to follow us on Twitter and don’t forget to join our 120k+ ML SubReddit and Subscribe to our Newsletter. Wait! are you on telegram? now you can join us on telegram as well.

Previous articleMicrosoft AI Releases Harrier-OSS-v1: A New Family of Multilingual Embedding Models Hitting SOTA on Multilingual MTEB v2

Next articleHow to Build and Evolve a Custom OpenAI Agent with A-Evolve Using Benchmarks, Skills, Memory, and Workspace Mutations

Asif Razzaq

RELATED ARTICLESMORE FROM AUTHOR

Meta Superintelligence Lab Releases Muse Spark: A Multimodal Reasoning Model With Thought Compression and Parallel Agents

Sigmoid vs ReLU Activation Functions: The Inference Cost of Losing Geometric Context

A Coding Guide to Build Advanced Document Intelligence Pipelines with Google LangExtract, OpenAI Models, Structured Extraction, and Interactive Visualization

Google AI Research Introduces PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing

A Comprehensive Implementation Guide to ModelScope for Model Search, Inference, Fine-Tuning, Evaluation, and Export

Meet OSGym: A New OS Infrastructure Framework That Manages 1,000+ Replicas at $0.23/Day for Computer Use Agent Research

Meta Superintelligence Lab Releases Muse Spark: A Multimodal Reasoning Model With Thought Compression and...

Asif Razzaq-April 9, 20260


 
Meta Superintelligence Labs recently made a significant move by unveiling 'Muse Spark' — the first model in the Muse family. Muse Spark is a... 

Sigmoid vs ReLU Activation Functions: The Inference Cost of Losing Geometric Context

Arham Islam-April 9, 20260


 
A deep neural network can be understood as a geometric system, where each layer reshapes the input space to form increasingly complex decision boundaries.... 

A Coding Guide to Build Advanced Document Intelligence Pipelines with Google LangExtract, OpenAI Models,...

Asif Razzaq-April 8, 20260


 
In this tutorial, we explore how to use Google’s LangExtract library to transform unstructured text into structured, machine-readable information. We begin by installing the... 

Google AI Research Introduces PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing

Asif Razzaq-April 8, 20260


 
Writing a research paper is brutal. Even after the experiments are done, a researcher still faces weeks of translating messy lab notes, scattered results... 

A Comprehensive Implementation Guide to ModelScope for Model Search, Inference, Fine-Tuning, Evaluation, and Export

Michal Sutter-April 8, 20260


 
In this tutorial, we explore ModelScope through a practical, end-to-end workflow that runs smoothly on Colab. We begin by setting up the environment, verifying... 

Meet OSGym: A New OS Infrastructure Framework That Manages 1,000+ Replicas at $0.23/Day for...

Asif Razzaq-April 8, 20260


 
Training AI agents that can actually use a computer — opening apps, clicking buttons, browsing the web, writing code — is one of the... 

Z.AI Introduces GLM-5.1: An Open-Weight 754B Agentic Model That Achieves SOTA on SWE-Bench Pro...

Asif Razzaq-April 8, 20260


 
Z.AI, the AI platform developed by the team behind the GLM model family, has released GLM-5.1 — its next-generation flagship model developed specifically for... 

How to Combine Google Search, Google Maps, and Custom Functions in a Single Gemini...

Michal Sutter-April 7, 20260


 
In this tutorial, we explore the latest Gemini API tooling updates Google announced in March 2026, specifically the ability to combine built-in tools like... 

How to Deploy Open WebUI with Secure OpenAI API Integration, Public Tunneling, and Browser-Based...

Michal Sutter-April 7, 20260


 
In this tutorial, we build a complete Open WebUI setup in Colab, in a practical, hands-on way, using Python. We begin by installing the... 

Meta AI Releases EUPE: A Compact Vision Encoder Family Under 100M Parameters That Rivals...

Asif Razzaq-April 6, 20260


 
Running powerful AI on your smartphone isn't just a hardware problem — it's a model architecture problem. Most state-of-the-art vision encoders are enormous, and... 

DiscordLinkedinRedditX

miniCON Event 2025

Download
AI Magazine/Report

Privacy & TC

Cookie Policy

🐝 Partnership and Promotion


 © Copyright Reserved @2025 Marktechpost AI Media Inc 

We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept”, you consent to the use of ALL the cookies. Do not sell my personal information.

Cookie settingsACCEPT

Privacy & Cookies Policy

Close

Privacy Overview

This website uses cookies to improve your experience while you navigate through the website. Out of these cookies, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may have an effect on your browsing experience.

 Necessary 
Necessary
Always Enabled

 Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information. 

 Others 
Others

 Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.
CookieDurationDescription__Secure-YECpastYouTube sets this cookie to stores the user's video player preferences using embedded YouTube video_pxttldsessionDescription is currently not available.pxctssessionDescription is currently not available.SGPBShowingLimitationDomain776592 daysDescription is currently not available.

 Non Necessary 
Non Necessary

 Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website. 

 Analytics 
Analytics

 Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics the number of visitors, bounce rate, traffic source, etc. 

 Performance 
Performance

 Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors. 

 Uncategorized 
Uncategorized

 Undefined cookies are those that are being analyzed and have not been classified into a category as yet. 

 Functional 
Functional

 Functional cookies help to perform certain functionalities like sharing the content of the website on social media platforms, collect feedbacks, and other third-party features. 

 Advertisement 
Advertisement

 Advertisement cookies are used to provide visitors with relevant ads and marketing campaigns. These cookies track visitors across websites and collect information to provide customized ads. 

SAVE & ACCEPT

Powered by 

Loading Comments...

Write a Comment...

Email (Required)Name (Required)Website
