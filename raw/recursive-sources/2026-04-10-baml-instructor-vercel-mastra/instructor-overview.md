---
title: Instructor - Multi-Language Library for Structured LLM Outputs | Python, TypeScript, Go, Ruby - Instructor
source_url: https://python.useinstructor.com/
final_url: https://python.useinstructor.com/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T04:49:51.769659+00:00
---

# Instructor - Multi-Language Library for Structured LLM Outputs | Python, TypeScript, Go, Ruby - Instructor

## 원본 URL

https://python.useinstructor.com/

## 주요 헤딩

- Instructor: Top Multi-Language Library for Structured LLM Outputs ¶
- What is Instructor? ¶
- Key Features for LLM Data Extraction ¶
- Quick Start ¶
- Complex Schemas & Validation ¶
- Supported LLM Providers ¶
- Citation ¶
- Why use Instructor? ¶
- Type Inference & Advanced Methods ¶
- Frequently Asked Questions ¶
- Templating ¶
- Validation ¶
- Contributing ¶
- License ¶

## 추출 본문

Instructor
instructor
Introduction
Introduction Start Here (Beginners)
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
Table of contents What is Instructor?
Key Features for LLM Data Extraction
Quick Start Extract Structured Data
Complex Schemas & Validation
Supported LLM Providers Provider Examples
Citation
Why use Instructor? Using Hooks
Type Inference & Advanced Methods
Frequently Asked Questions What is Instructor?
Which LLM providers does Instructor support?
Do I need to know Pydantic to use Instructor?
How does Instructor compare to other libraries?
Can I use Instructor with open source models?
Does Instructor work with async code?
Templating
Validation
Contributing
License
Instructor: Top Multi-Language Library for Structured LLM Outputs ¶
Extract structured data from any LLM with type safety, validation, and automatic retries. Available in Python, TypeScript, Go, Ruby, Elixir, and Rust.
Instructor for extraction, PydanticAI for agents. Instructor shines when you need fast, schema-first extraction without extra agents. When your project needs quality gates, shareable runs, or built-in observability, try PydanticAI . PydanticAI is the official agent runtime from the Pydantic team: it adds typed tools, dataset replays, and production dashboards while keeping your existing Instructor models. Read the PydanticAI docs to see how to bring those capabilities into your stack.
What is Instructor? ¶
Instructor is the most popular Python library for extracting structured data from Large Language Models (LLMs). With over 3 million monthly downloads, 11k stars, and 100+ contributors , it's the go-to solution for developers who need reliable, validated outputs from AI models.
Built on top of Pydantic , Instructor provides type-safe data extraction with automatic validation, retries, and streaming support. Whether you're using OpenAI's GPT models, Anthropic's Claude, Google's Gemini, open source models with Ollama , DeepSeek , or any of 15+ supported providers, Instructor ensures your LLM outputs are always structured and validated.
Key Features for LLM Data Extraction ¶
Structured Outputs : Define Pydantic models to specify exactly what data you want from your LLM
Automatic Retries : Built-in retry logic when validation fails - no more manual error handling
Data Validation : Leverage Pydantic's powerful validation to ensure response quality
Streaming Support : Real-time processing of partial responses and lists
Multi-Provider : Works with OpenAI, Anthropic, Google, Mistral, Cohere, Ollama, DeepSeek, and 15+ LLM providers
Type Safety : Full IDE support with proper type inference and autocompletion
Open Source Support : Run any open source model locally with Ollama, llama-cpp-python, or vLLM
Quick Start ¶
Install Instructor and start extracting structured data in minutes:
pip uv poetry
pip install instructor
uv add instructor
poetry add instructor
Extract Structured Data ¶
Instructor's from_provider
function provides a unified interface to work with any LLM provider. Switch between OpenAI, Anthropic, Google, Ollama, DeepSeek, and 15+ providers with the same code:
import instructor
from pydantic import BaseModel
class Person ( BaseModel ):
name : str
age : int
occupation : str
# Works with any provider - same interface everywhere
client = instructor . from_provider ( "openai/gpt-5-nano" )
# Or: instructor.from_provider("anthropic/claude-3")
# Or: instructor.from_provider("google/gemini-pro")
# Or: instructor.from_provider("ollama/llama3") # local
# Extract structured data from natural language
person = client . create (
response_model = Person ,
messages = [
{ "role" : "user" , "content" : "Extract: John is a 30-year-old software engineer" }
],
)
print ( person ) # Person(name='John', age=30, occupation='software engineer')
The from_provider
API supports both sync and async usage ( async_client=True
) and automatically handles provider-specific configurations. See all supported providers â
Complex Schemas & Validation ¶
Instructor excels at extracting complex, nested data structures with custom validation rules. Here's a concise example:
import instructor
from pydantic import BaseModel , Field , field_validator
from typing import List , Optional
from enum import Enum
class Priority ( str , Enum ):
LOW = "low"
MEDIUM = "medium"
HIGH = "high"
CRITICAL = "critical"
class Ticket ( BaseModel ):
title : str = Field ( ... , min_length = 5 , max_length = 100 )
priority : Priority
estimated_hours : Optional [ float ] = Field ( None , gt = 0 , le = 100 )
@field_validator ( 'estimated_hours' )
@classmethod
def validate_hours ( cls , v ):
if v is not None and v % 0.5 != 0 :
raise ValueError ( 'Hours must be in 0.5 increments' )
return v
class CustomerSupport ( BaseModel ):
customer_name : str
tickets : List [ Ticket ] = Field ( ... , min_items = 1 )
client = instructor . from_provider ( "openai/gpt-4o" )
support_case = client . create (
response_model = CustomerSupport ,
messages = [{ "role" : "user" , "content" : "Extract support case details..." }],
max_retries = 3 ,
)
Key Features: - Deep nesting with nested models and lists - Custom validation with Pydantic validators - Automatic retries on validation failures - Type-safe extraction with full IDE support
Learn more about validation and complex schemas â
Supported LLM Providers ¶
Instructor works seamlessly with 15+ popular LLM providers , giving you the flexibility to use any model while maintaining consistent structured output handling. From OpenAI's GPT models to open source alternatives with Ollama , DeepSeek models , and local inference, get validated data extraction everywhere.
It stands out for its simplicity, transparency, and user-centric design, built on top of Pydantic. Instructor helps you manage validation context , retries with Tenacity , and streaming Lists and Partial responses.
Star the Repo Cookbooks Prompting Guide
If you ever get stuck, you can always run instructor docs
to open the documentation in your browser. It even supports searching for specific topics.
instructor docs [ QUERY ]
Provider Examples ¶
All providers use the same simple interface. Here are quick examples for the most popular providers:
OpenAI Anthropic Google Gemini Ollama (Local)
import instructor
from pydantic import BaseModel
class ExtractUser ( BaseModel ):
name : str
age : int
client = instructor . from_provider ( "openai/gpt-5-nano" )
res = client . create (
response_model = ExtractUser ,
messages = [{ "role" : "user" , "content" : "John Doe is 30 years old." }],
)
Full OpenAI docs â
import instructor
from pydantic import BaseModel
class ExtractUser ( BaseModel ):
name : str
age : int
client = instructor . from_provider ( "anthropic/claude-3-5-sonnet-20240620" )
resp = client . create (
response_model = ExtractUser ,
messages = [{ "role" : "user" , "content" : "Extract Jason is 25 years old." }],
)
Full Anthropic docs â
import instructor
from pydantic import BaseModel
class ExtractUser ( BaseModel ):
name : str
age : int
client = instructor . from_provider ( "google/gemini-2.5-flash" )
resp = client . create (
