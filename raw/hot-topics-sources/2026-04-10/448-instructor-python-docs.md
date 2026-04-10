---
title: Instructor - Multi-Language Library for Structured LLM Outputs | Python, TypeScript, Go, Ruby - Instructor
source_url: https://python.useinstructor.com
final_url: https://python.useinstructor.com
status: 200
content_type: text/html
topics: [Instructor (Multi-Language Structured Outputs)]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:29.432116+00:00
---

# Instructor - Multi-Language Library for Structured LLM Outputs | Python, TypeScript, Go, Ruby - Instructor

## 원본 URL

https://python.useinstructor.com

## 추출 본문

Instructor - Multi-Language Library for Structured LLM Outputs | Python, TypeScript, Go, Ruby - Instructor
 Skip to content 

 🎉 Introducing Kura: Turn your chat logs into actionable insights! Discover user patterns, extract intents, and understand conversation flows at scale. Try it on GitHub →

 Instructor 

 Instructor - Multi-Language Library for Structured LLM Outputs | Python, TypeScript, Go, Ruby 

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
 Introduction 
 Start Here (Beginners) 

 Getting Started 

 Installation 

 Why use Instructor? 

 Architecture 

 Debugging 

 Repository Overview 

 Mode Comparison 

 Philosophy 

 API Reference 

 FAQ 

 Help with Instructor 

 Contributing 

 Newsletter 

 Tutorials 

 Learning 

 Integrations 

 Cookbook 

 Concepts 

 Prompt Engineering 

 CLI Reference 

 Find Jobs (External) 

 Blog 

 Table of contents 
 What is Instructor? 

 Key Features for LLM Data Extraction 

 Quick Start 
 Extract Structured Data 

 Complex Schemas & Validation 

 Supported LLM Providers 
 Provider Examples 

 Citation 

 Why use Instructor? 
 Using Hooks 

 Type Inference & Advanced Methods 

 Frequently Asked Questions 
 What is Instructor? 

 Which LLM providers does Instructor support? 

 Do I need to know Pydantic to use Instructor? 

 How does Instructor compare to other libraries? 

 Can I use Instructor with open source models? 

 Does Instructor work with async code? 

 Templating 

 Validation 

 Contributing 

 License 

Instructor: Top Multi-Language Library for Structured LLM Outputs¶

Extract structured data from any LLM with type safety, validation, and automatic retries. Available in Python, TypeScript, Go, Ruby, Elixir, and Rust.

Instructor for extraction, PydanticAI for agents. Instructor shines when you need fast, schema-first extraction without extra agents. When your project needs quality gates, shareable runs, or built-in observability, try PydanticAI. PydanticAI is the official agent runtime from the Pydantic team: it adds typed tools, dataset replays, and production dashboards while keeping your existing Instructor models. Read the PydanticAI docs to see how to bring those capabilities into your stack.

What is Instructor?¶

Instructor is the most popular Python library for extracting structured data from Large Language Models (LLMs). With over 3 million monthly downloads, 11k stars, and 100+ contributors, it's the go-to solution for developers who need reliable, validated outputs from AI models.

Built on top of Pydantic, Instructor provides type-safe data extraction with automatic validation, retries, and streaming support. Whether you're using OpenAI's GPT models, Anthropic's Claude, Google's Gemini, open source models with Ollama, DeepSeek, or any of 15+ supported providers, Instructor ensures your LLM outputs are always structured and validated.

Key Features for LLM Data Extraction¶

Structured Outputs: Define Pydantic models to specify exactly what data you want from your LLM

Automatic Retries: Built-in retry logic when validation fails - no more manual error handling

Data Validation: Leverage Pydantic's powerful validation to ensure response quality

Streaming Support: Real-time processing of partial responses and lists

Multi-Provider: Works with OpenAI, Anthropic, Google, Mistral, Cohere, Ollama, DeepSeek, and 15+ LLM providers

Type Safety: Full IDE support with proper type inference and autocompletion

Open Source Support: Run any open source model locally with Ollama, llama-cpp-python, or vLLM

Quick Start¶

Install Instructor and start extracting structured data in minutes:

pipuvpoetry

pipinstallinstructor

uvaddinstructor

poetryaddinstructor

Extract Structured Data¶

Instructor's 
from_provider
 function provides a unified interface to work with any LLM provider. Switch between OpenAI, Anthropic, Google, Ollama, DeepSeek, and 15+ providers with the same code:

importinstructorfrompydanticimportBaseModelclassPerson(BaseModel):name:strage:intoccupation:str# Works with any provider - same interface everywhereclient=instructor.from_provider("openai/gpt-5-nano")# Or: instructor.from_provider("anthropic/claude-3")# Or: instructor.from_provider("google/gemini-pro")# Or: instructor.from_provider("ollama/llama3") # local# Extract structured data from natural languageperson=client.create(response_model=Person,messages=[{"role":"user","content":"Extract: John is a 30-year-old software engineer"}],)print(person)# Person(name='John', age=30, occupation='software engineer')

The 
from_provider
 API supports both sync and async usage (
async_client=True
) and automatically handles provider-specific configurations. See all supported providers →

Complex Schemas & Validation¶

Instructor excels at extracting complex, nested data structures with custom validation rules. Here's a concise example:

importinstructorfrompydanticimportBaseModel,Field,field_validatorfromtypingimportList,OptionalfromenumimportEnumclassPriority(str,Enum):LOW="low"MEDIUM="medium"HIGH="high"CRITICAL="critical"classTicket(BaseModel):title:str=Field(...,min_length=5,max_length=100)priority:Priorityestimated_hours:Optional[float]=Field(None,gt=0,le=100)@field_validator('estimated_hours')@classmethoddefvalidate_hours(cls,v):ifvisnotNoneandv%0.5!=0:raiseValueError('Hours must be in 0.5 increments')returnvclassCustomerSupport(BaseModel):customer_name:strtickets:List[Ticket]=Field(...,min_items=1)client=instructor.from_provider("openai/gpt-4o")support_case=client.create(response_model=CustomerSupport,messages=[{"role":"user","content":"Extract support case details..."}],max_retries=3,)

Key Features: - Deep nesting with nested models and lists - Custom validation with Pydantic validators - Automatic retries on validation failures - Type-safe extraction with full IDE support

Learn more about validation and complex schemas →

Supported LLM Providers¶

Instructor works seamlessly with 15+ popular LLM providers, giving you the flexibility to use any model while maintaining consistent structured output handling. From OpenAI's GPT models to open source alternatives with Ollama, DeepSeek models, and local inference, get validated data extraction everywhere.

It stands out for its simplicity, transparency, and user-centric design, built on top of Pydantic. Instructor helps you manage validation context, retries with Tenacity, and streaming Lists and Partial responses.

 Star the Repo Cookbooks Prompting Guide

If you ever get stuck, you can always run 
instructor docs
 to open the documentation in your browser. It even supports searching for specific topics.

instructordocs[QUERY]

Provider Examples¶

All providers use the same simple interface. Here are quick examples for the most popular providers:

OpenAIAnthropicGoogle GeminiOllama (Local)

importinstructorfrompydanticimportBaseModelclassExtractUser(BaseModel):name:strage:intclient=instructor.from_provider("openai/gpt-5-nano")res=client.create(response_model=ExtractUser,messages=[{"role":"user","content":"John Doe is 30 years old."}],)

Full OpenAI docs →

importinstructorfrompydanticimportBaseModelclassExtractUser(BaseModel):name:strage:intclient=instructor.from_provider("anthropic/claude-3-5-sonnet-20240620")resp=client.create(response_model=ExtractUser,messages=[{"role":"user","content":"Extract Jason is 25 years old."}],)

Full Anthropic docs →

importinstructorfrompydanticimportBaseModelclassExtractUser(BaseModel):name:strage:intclient=instructor.from_provider("google/gemini-2.5-flash")resp=client.create(response_model=ExtractUser,messages=[{"role":"user","content":"Extract Jason is 25 years old."}],)

Full Google docs →

importinstructorfrompydanticimportBaseModelclassExtractUser(BaseModel):name:strage:intclient=instructor.from_provider("ollama/llama3")resp=client.create(response_model=ExtractUser,messages=[{"role":"user","content":"Extract Jason is 25 years old."}],)

Full Ollama docs →

View all 15+ providers →

Citation¶

If you use Instructor in your research or project, please cite it using:

@software{liu2024instructor,author={Jason Liu and Contributors},title={Instructor: A library for structured outputs from large language models},url={https://github.com/instructor-ai/instructor},year={2024},month={3}}

Why use Instructor?¶

Simple API with Full Prompt Control

Instructor provides a straightforward API that gives you complete ownership and control over your prompts. This allows for fine-tuned customization and optimization of your LLM interactions.

 Explore Concepts

Multi-Language Support

Simplify structured data extraction from LLMs with type hints and validation.

 Python · TypeScript · Ruby · Go · Elixir · Rust

Reasking and Validation

Automatically reask the model when validation fails, ensuring high-quality outputs. Leverage Pydantic's validation for robust error handling.

 Learn about Reasking

Streaming Support

Stream partial results and iterables with ease, allowing for real-time processing and improved responsiveness in your applications.

 Learn about Streaming

Powered by Type Hints

Leverage Pydantic for schema validation, prompting control, less code, and IDE integration.

 Learn more

Simplified LLM Interactions

Support for OpenAI, Anthropic, Google, Vertex AI, Mistral/Mixtral, Ollama, llama-cpp-python, Cohere, LiteLLM.

 See Hub

Using Hooks¶

Instructor's hooks system lets you intercept and handle events during LLM interactions. Use hooks for logging, monitoring, or custom error handling:

importinstructorfrompydanticimportBaseModelclassUserInfo(BaseModel):name:strage:intclient=instructor.from_provider("openai/gpt-4o-mini")# Attach hooks for logging and error handlingclient.on("completion:kwargs",lambda**kw:print("Called with:",kw))client.on("completion:error",lambdae:print(f"Error: {e}"))user_info=client.create(response_model=UserInfo,messages=[{"role":"user","content":"Extract: John is 20 years old"}],)

Learn more about hooks →

Type Inference & Advanced Methods¶

Instructor provides full type inference for better IDE support and type safety. The client includes specialized methods for different use cases:

Basic extraction:

importinstructorfrompydanticimportBaseModelclassUser(BaseModel):name:strage:intclient=instructor.from_provider("openai/gpt-4o-mini")user=client.create(response_model=User,messages=[...])# Type: User

Async support:

client=instructor.from_provider("openai/gpt-4o-mini",async_client=True)user=awaitclient.create(...)# Type: User

Access original completion:

user,completion=client.create_with_completion(...)# Returns tuple

Stream partial objects:

forpartialinclient.create_partial(...):# Type: Generator[User, None]print(partial)

Stream multiple objects:

foruserinclient.create_iterable(...):# Type: Generator[User, None]print(user)

All methods provide full type inference for better IDE autocomplete and type checking.

Frequently Asked Questions¶

What is Instructor?¶

Instructor is a Python library that extracts structured, validated data from Large Language Models (LLMs). It uses Pydantic models to define output schemas and automatically handles validation, retries, and error handling.

Which LLM providers does Instructor support?¶

Instructor supports 15+ providers including OpenAI, Anthropic, Google Gemini, Mistral, Cohere, Ollama, DeepSeek, and many more. See our integrations page for the complete list.

Do I need to know Pydantic to use Instructor?¶

Basic Pydantic knowledge helps, but you can get started with simple models. Instructor works with any Pydantic BaseModel, and you can learn advanced features as you need them.

How does Instructor compare to other libraries?¶

Instructor focuses specifically on structured outputs with automatic validation and retries. Unlike larger frameworks, Instructor does one thing very well: getting reliable, validated data from LLMs.

Can I use Instructor with open source models?¶

Yes! Instructor works with Ollama, llama-cpp-python, and other local models. See our Ollama integration guide to get started.

Does Instructor work with async code?¶

Yes, Instructor fully supports async/await. Use 
async_client=True
 when creating your client, then use 
await client.create()
.

View all FAQs →

Templating¶

Instructor supports templating with Jinja, which lets you create dynamic prompts. This is useful when you want to fill in parts of a prompt with data. Here's a simple example:

importinstructorfrompydanticimportBaseModelclient=instructor.from_provider("openai/gpt-4o-mini")classUser(BaseModel):name:strage:int# Create a completion using a Jinja template in the message contentresponse=client.create(messages=[{"role":"user","content":"""Extract the information from the following text: {{ data }}`""",},],response_model=User,context={"data":"John Doe is thirty years old"},)print(response)#> User(name='John Doe', age=30)

Learn more about templating :octicons-arrow-right:

Validation¶

You can also use Pydantic to validate your outputs and get the llm to retry on failure. Check out our docs on retrying and validation context.

importinstructorfrompydanticimportBaseModel,ValidationError,BeforeValidatorfromtyping_extensionsimportAnnotatedfrominstructorimportllm_validator# Create instructor clientclient=instructor.from_provider("openai/gpt-4o-mini")classQuestionAnswer(BaseModel):question:stranswer:Annotated[str,BeforeValidator(llm_validator("don't say objectionable things",client=client)),]try:qa=QuestionAnswer(question="What is the meaning of life?",answer="The meaning of life is to be evil and steal",)exceptValidationErrorase:print(e)""" 1 validation error for QuestionAnswer answer Assertion failed, The statement promotes objectionable behavior by encouraging evil and stealing. [type=assertion_error, input_value='The meaning of life is to be evil and steal', input_type=str] """

Contributing¶

If you want to help out, checkout some of the issues marked as 
good-first-issue
 or 
help-wanted
. Found here. They could be anything from code improvements, a guest blog post, or a new cook book.

License¶

This project is licensed under the terms of the MIT License.
 Was this page helpful? 

 Thanks for your feedback! 

 Thanks for your feedback! Help us improve this page by using our feedback form. 

 Back to top 
 Next 
 Start Here (Beginners) 

 Copyright © 2024 Jason Liu 
 Made with Material for MkDocs
