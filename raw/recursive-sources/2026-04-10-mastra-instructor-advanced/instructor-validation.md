---
title: Validation - Instructor
source_url: https://python.useinstructor.com/concepts/validation/
final_url: https://python.useinstructor.com/concepts/validation/
status: 200
content_type: text/html; charset=utf-8
fetched_at: 2026-04-10T06:17:49.559272+00:00
---

# Validation - Instructor

## 원본 URL

https://python.useinstructor.com/concepts/validation/

## 주요 헤딩

- Validation ¶
- Validation Flow ¶
- Basic Validation ¶
- Field Validation ¶
- Custom Validators ¶
- Pre-validation Transformation ¶
- Semantic Validation ¶
- Nested Validation ¶
- Error Handling ¶
- Best Practices ¶
- See Also ¶

## 추출 본문

Instructor
instructor
Introduction
Learning
Integrations
Cookbook
Concepts
Concepts Error Handling
Retrying
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
Validation Validation Table of contents Validation Flow
Basic Validation
Field Validation
Custom Validators
Pre-validation Transformation
Semantic Validation
Nested Validation
Error Handling
Best Practices
See Also
Semantic Validation
Alias
Enums
Type Adapter
Prompt Engineering
CLI Reference
Find Jobs (External)
Blog
Table of contents Validation Flow
Basic Validation
Field Validation
Custom Validators
Pre-validation Transformation
Semantic Validation
Nested Validation
Error Handling
Best Practices
See Also
Validation ¶
Instructor uses Pydantic for validation, providing type checking, data coercion, custom validators, and field constraints.
Validation Flow ¶
flowchart TD
A[Define Pydantic Model] --> B[Send Request to LLM]
B --> C[LLM Generates Response]
C --> D{Validate Response}
D -->|Valid| E[Return Pydantic Object]
D -->|Invalid| F{Auto-Retry Enabled?}
F -->|Yes| G[Send Error Context to LLM]
F -->|No| H[Raise ValidationError]
G --> I[LLM Generates New Response]
I --> J{Validate Again}
J -->|Valid| E
J -->|Invalid| K{Max Retries Reached?}
K -->|No| G
K -->|Yes| H
Basic Validation ¶
Define models with type hints and field constraints:
from typing import List
from pydantic import BaseModel , Field , field_validator
class User ( BaseModel ):
name : str = Field ( ... , min_length = 2 , description = "User's full name" )
age : int = Field ( ... , ge = 0 , le = 150 , description = "User's age" )
emails : List [ str ] = Field ( description = "List of email addresses" )
@field_validator ( 'emails' )
@classmethod
def validate_emails ( cls , v ):
if not all ( '@' in email for email in v ):
raise ValueError ( 'Invalid email format' )
return v
Field Validation ¶
Use Field()
for basic constraints:
from pydantic import BaseModel , Field
class Product ( BaseModel ):
name : str = Field ( ... , min_length = 1 , max_length = 100 )
price : float = Field ( ... , gt = 0 )
quantity : int = Field ( ... , ge = 0 )
Custom Validators ¶
Use @field_validator
for complex validation:
from pydantic import BaseModel , Field , field_validator
class Order ( BaseModel ):
items : list [ str ] = Field ( description = "List of item names" )
total : float = Field ( description = "Total order amount" )
@field_validator ( 'total' )
@classmethod
def validate_total ( cls , v ):
if v < 0 :
raise ValueError ( 'Total cannot be negative' )
return v
Pre-validation Transformation ¶
Transform data before validation:
from pydantic import BaseModel , field_validator
class UserProfile ( BaseModel ):
username : str
@field_validator ( 'username' , mode = 'before' )
@classmethod
def lowercase_username ( cls , v ):
return v . lower () if isinstance ( v , str ) else v
Semantic Validation ¶
Use llm_validator
for validations that are hard to express programmatically:
from typing import Annotated
from pydantic import BaseModel , BeforeValidator
import instructor
from instructor import llm_validator
client = instructor . from_provider ( "openai/gpt-4.1-mini" )
class ContentReview ( BaseModel ):
title : str
content : Annotated [
str ,
BeforeValidator (
llm_validator (
"Content must be family-friendly and not contain profanity" ,
client = client ,
)
),
]
Semantic validation works well for content moderation, tone validation, consistency checks, and complex relationships. For more patterns and details, see the Semantic Validation guide.
Nested Validation ¶
Validate nested structures:
from pydantic import BaseModel , Field
class Address ( BaseModel ):
street : str
city : str
country : str
class User ( BaseModel ):
name : str
addresses : list [ Address ] = Field ( description = "User's addresses" )
Error Handling ¶
Handle validation failures with appropriate error types:
import instructor
from pydantic import BaseModel , Field , field_validator
class User ( BaseModel ):
name : str
age : int
@field_validator ( 'age' )
@classmethod
def validate_age ( cls , v ):
if v < 0 :
raise ValueError ( "Age cannot be negative" )
return v
client = instructor . from_provider ( "openai/gpt-4.1-mini" )
try :
user = client . create (
response_model = User ,
messages = [
{ "role" : "user" , "content" : "Extract: John, age: -5" },
],
)
except instructor . exceptions . InstructorValidationError as e :
print ( f "Validation error: { e } " )
