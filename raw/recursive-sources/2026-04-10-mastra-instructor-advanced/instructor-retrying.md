---
title: Retry Logic with Tenacity - Instructor
source_url: https://python.useinstructor.com/concepts/retrying/
final_url: https://python.useinstructor.com/concepts/retrying/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T06:17:50.009512+00:00
---

# Retry Logic with Tenacity - Instructor

## 원본 URL

https://python.useinstructor.com/concepts/retrying/

## 주요 헤딩

- Retry Logic with Tenacity ¶
- Basic Retry with Exponential Backoff ¶
- Error-Specific Retries ¶
- Custom Retry Conditions ¶
- Context-Based Validation with Retries ¶
- Logging and Monitoring ¶
- Instructor's Built-in Retries ¶
- Failed Attempts Tracking ¶
- Best Practices ¶
- Troubleshooting ¶
- Related Resources ¶

## 추출 본문

Instructor
instructor
Introduction
Learning
Integrations
Cookbook
Concepts
Concepts Error Handling
Retrying Retrying Table of contents Basic Retry with Exponential Backoff
Error-Specific Retries
Custom Retry Conditions
Context-Based Validation with Retries
Logging and Monitoring
Instructor's Built-in Retries
Failed Attempts Tracking
Best Practices Choose Appropriate Strategies
Always Set Stop Conditions
Troubleshooting
Related Resources
Fields
Models
Parallel Tools
Templating
Lists and Arrays
Prompting
Citations
Multimodal
Patching
from_provider
Migration Guide
Mode Migration
Hooks
Types
TypedDicts
Validators
Usage Tokens
Missing
Stream Iterable
Stream Partial
Raw Response
FastAPI
Caching
Prompt Caching
Logging
Distillation
Dictionary Operations
Union
Unions
Validation
Semantic Validation
Alias
Enums
Type Adapter
Prompt Engineering
CLI Reference
Find Jobs (External)
Blog
Table of contents Basic Retry with Exponential Backoff
Error-Specific Retries
Custom Retry Conditions
Context-Based Validation with Retries
Logging and Monitoring
Instructor's Built-in Retries
Failed Attempts Tracking
Best Practices Choose Appropriate Strategies
Always Set Stop Conditions
Troubleshooting
Related Resources
Retry Logic with Tenacity ¶
Tenacity is a Python library for adding retry logic to your applications. Combined with Instructor, it helps handle API failures, rate limits, and validation errors.
Basic Retry with Exponential Backoff ¶
The most common pattern uses exponential backoff to delay retries:
import instructor
from pydantic import BaseModel
from tenacity import retry , stop_after_attempt , wait_exponential
client = instructor . from_provider ( "openai/gpt-4.1-mini" )
class UserInfo ( BaseModel ):
name : str
age : int
email : str
@retry ( stop = stop_after_attempt ( 3 ), wait = wait_exponential ( multiplier = 1 , min = 4 , max = 10 ))
def extract_user_info ( text : str ) -> UserInfo :
"""Extract user information with retry logic."""
return client . create (
response_model = UserInfo ,
messages = [{ "role" : "user" , "content" : f "Extract user info: { text } " }],
)
try :
user = extract_user_info ( "John is 30 years old with email john@example.com" )
print ( f "Success: { user . name } , { user . age } , { user . email } " )
#> Success: John, 30, john@example.com
except Exception as e :
print ( f "Failed after retries: { e } " )
Error-Specific Retries ¶
Retry only on specific error types for better control:
import instructor
from openai import APIError , RateLimitError
from pydantic import BaseModel , ValidationError
from tenacity import (
retry ,
retry_if_exception_type ,
stop_after_attempt ,
wait_exponential ,
)
client = instructor . from_provider ( "openai/gpt-4.1-mini" )
class UserInfo ( BaseModel ):
name : str
age : int
email : str
# Retry on API errors with longer delays
@retry (
retry = retry_if_exception_type (( RateLimitError , APIError )),
stop = stop_after_attempt ( 5 ),
wait = wait_exponential ( multiplier = 2 , min = 1 , max = 60 ),
)
def handle_api_errors ( text : str ) -> UserInfo :
return client . create (
response_model = UserInfo ,
messages = [{ "role" : "user" , "content" : text }],
)
# Retry on validation errors with shorter delays
@retry (
retry = retry_if_exception_type ( ValidationError ),
stop = stop_after_attempt ( 3 ),
wait = wait_exponential ( multiplier = 1 , min = 1 , max = 10 ),
)
def handle_validation_errors ( text : str ) -> UserInfo :
return client . create (
response_model = UserInfo ,
messages = [{ "role" : "user" , "content" : text }],
)
Custom Retry Conditions ¶
Retry based on the result content rather than exceptions:
import instructor
from pydantic import BaseModel
from tenacity import retry , retry_if_result , stop_after_attempt
client = instructor . from_provider ( "openai/gpt-4.1-mini" )
class UserInfo ( BaseModel ):
name : str
age : int
email : str
def should_retry ( result : UserInfo ) -> bool :
"""Retry if the result doesn't meet quality criteria."""
return result . age < 0 or result . age > 150 or not result . email
@retry ( retry = retry_if_result ( should_retry ), stop = stop_after_attempt ( 3 ))
def extract_valid_user ( text : str ) -> UserInfo :
return client . create (
response_model = UserInfo ,
messages = [{ "role" : "user" , "content" : text }],
)
Context-Based Validation with Retries ¶
Use the context
parameter to pass runtime data to validators:
import instructor
from pydantic import BaseModel , ValidationInfo , field_validator , ValidationError
from tenacity import retry , retry_if_exception_type , stop_after_attempt , wait_exponential
client = instructor . from_provider ( "openai/gpt-4.1-mini" )
class Citation ( BaseModel ):
"""A claim with a supporting quote from source text."""
claim : str
quote : str
@field_validator ( 'quote' )
@classmethod
def verify_quote_exists ( cls , v : str , info : ValidationInfo ):
context = info . context
if context :
source_text = context . get ( 'source_text' , '' )
if v not in source_text :
raise ValueError ( f "Quote ' { v } ' not found in source text." )
return v
@retry (
retry = retry_if_exception_type ( ValidationError ),
stop = stop_after_attempt ( 3 ),
wait = wait_exponential ( multiplier = 1 , min = 2 , max = 10 ),
)
def extract_citation ( claim : str , source_text : str ) -> Citation :
return client . create (
response_model = Citation ,
messages = [
{
