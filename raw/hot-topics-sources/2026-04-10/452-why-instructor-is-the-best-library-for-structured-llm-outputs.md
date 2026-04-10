---
title: Why Instructor is the Best Library for Structured LLM Outputs - Instructor
source_url: https://python.useinstructor.com/blog/2024/03/05/zero-cost-abstractions
final_url: https://python.useinstructor.com/blog/2024/03/05/zero-cost-abstractions/
status: 200
content_type: text/html
topics: [Instructor (Multi-Language Structured Outputs)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:30.474972+00:00
---

# Why Instructor is the Best Library for Structured LLM Outputs - Instructor

## 원본 URL

https://python.useinstructor.com/blog/2024/03/05/zero-cost-abstractions

## 추출 본문

Why Instructor is the Best Library for Structured LLM Outputs - Instructor
 Skip to content 

 🎉 Introducing Kura: Turn your chat logs into actionable insights! Discover user patterns, extract intents, and understand conversation flows at scale. Try it on GitHub →

 Instructor 

 Why Instructor is the Best Library for Structured LLM Outputs 

 Initializing search 

 instructor 

 Introduction 

 Learning 

 Integrations 

 Cookbook 

 Concepts 

 Prompt Engineering 

 CLI Reference 

 Find Jobs (External) 

 Blog 

 Instructor 

 instructor 

 Introduction 

 Learning 

 Integrations 

 Cookbook 

 Concepts 

 Prompt Engineering 

 CLI Reference 

 Find Jobs (External) 

 Blog 
 Blog 
 Archive Archive 
 2025 

 2024 

 2023 

 Categories Categories 
 API Development 

 API Efficiency 

 Announcements 

 Audio 

 Contributing 

 Cost Reduction 

 Data Analysis 

 Data Processing 

 Data Validation 

 Document Processing 

 Documentation 

 Financial Services 

 Gemini 

 Google 

 LLM 

 LLM Observability 

 LLM Techniques 

 LLMs 

 Multimodal 

 OpenAI 

 Performance Optimization 

 Production 

 Pydantic 

 Python 

 Python Development 

 Structured Outputs 

 Technical 

 Tutorial 

 UV 

 Validation 

 Writer SDK 

 anthropic 

 instructor 

 structured-data 

 tutorials 

 Table of contents 
 Other Features 

 Instructor's Broad Applicability 

 Direct access to the messages array 

 Low Abstraction 

 Related Concepts 

 See Also 

 Back to index 

Jason Liu
 Creator 

 Metadata 

2024/03/05

 in LLM Techniques

 3 min read 

Why Instructor is the Best Library for Structured LLM Outputs¶

Large language models (LLMs) like GPTs are incredibly powerful, but working with their open-ended text outputs can be challenging. This is where the Instructor library shines - it allows you to easily map LLM outputs to structured data using Python type annotations.

The core idea behind Instructor is incredibly simple: it's just a patch over the OpenAI Python SDK that adds a response_model parameter. This parameter lets you pass in a Pydantic model that describes the structure you want the LLM output mapped to. Pydantic models are defined using standard Python type hints, so there's zero new syntax to learn.

Here's an example of extracting structured user data from an LLM:

frompydanticimportBaseModelimportinstructorclassUser(BaseModel):name:strage:intclient=instructor.from_provider("openai/gpt-5-nano")user=client.create(model="gpt-3.5-turbo",response_model=User,# (1)!messages=[{"role":"user","content":"Extract the user's name and age from this: John is 25 years old",}],)print(user)# (2)!#> name='John' age=25

Notice that now we have a new response_model parameter that we pass in to the completions.create method. This parameter lets us specify the structure we want the LLM output to be mapped to. In this case, we're using a Pydantic model called User that describes a user's name and age.

The output of the completions.create method is a User object that matches the structure we specified in the response_model parameter, rather than a ChatCompletion.

Other Features¶

Other features on instructor, in and out of the llibrary are:

Ability to use Tenacity in retrying logic

Ability to use Pydantic's validation context

Parallel Tool Calling with correct types

Streaming Partial and Iterable data.

Returning Primitive Types and Unions as well!

Lots of Cookbooks, Tutorials, and comprehensive Documentation in our Integration Guides

Instructor's Broad Applicability¶

One of the key strengths of Instructor is that it's designed as a lightweight patch over the official OpenAI Python SDK. This means it can be easily integrated not just with OpenAI's hosted API service, but with any provider or platform that exposes an interface compatible with the OpenAI SDK.

For example, providers like Together, Ollama, Groq, and llama-cpp-python all either use or mimic the OpenAI Python SDK under the hood. With Instructor's zero-overhead patching approach, teams can immediately start deriving structured data outputs from any of these providers. There's no need for custom integration work.

Direct access to the messages array¶

Unlike other libraries that abstract away the 
messages=[...]
 parameter, Instructor provides direct access. This direct approach facilitates intricate prompt engineering, ensuring compatibility with OpenAI's evolving message types, including future support for images, audio, or video, without the constraints of string formatting.

Low Abstraction¶

What makes Instructor so powerful is how seamlessly it integrates with existing OpenAI SDK code. To use it, you literally just call instructor.from_openai() on your OpenAI client instance, then use response_model going forward. There's no complicated refactoring or new abstractions to wrap your head around.

This incremental, zero-overhead adoption path makes Instructor perfect for sprinkling structured LLM outputs into an existing OpenAI-based application. You can start extracting data models from simple prompts, then incrementally expand to more complex hierarchical models, streaming outputs, and custom validations.

And if you decide Instructor isn't a good fit after all, removing it is as simple as not applying the patch! The familiarity and flexibility of working directly with the OpenAI SDK is a core strength.

Instructor solves the "string hellll" of unstructured LLM outputs. It allows teams to easily realize the full potential of tools like GPTs by mapping their text to type-safe, validated data structures. If you're looking to get more structured value out of LLMs, give Instructor a try!

Related Concepts¶

Philosophy - Understand Instructor's design principles

Patching - Learn how Instructor patches LLM clients

Retrying - Handle validation failures gracefully

Streaming - Work with streaming responses

See Also¶

Introduction to Instructor - Get started with structured outputs

Integration Guides - See all supported providers

Type Examples - Explore different response types
 Was this page helpful? 

 Thanks for your feedback! 

 Thanks for your feedback! Help us improve this page by using our feedback form. 

 Back to top 

 Previous 
 Seamless Support with Langsmith 

 Next 
 Structured Output for Open Source and Local LLMs 

 Copyright © 2024 Jason Liu 
 Made with Material for MkDocs
