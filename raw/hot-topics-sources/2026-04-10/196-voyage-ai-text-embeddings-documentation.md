---
title: Text Embeddings
source_url: https://docs.voyageai.com/docs/embeddings
final_url: https://docs.voyageai.com/docs/embeddings
status: 200
content_type: text/html; charset=utf-8
topics: [Qwen3 / Voyage-4 Embedding Leaderboard Shakeup]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:53.565286+00:00
---

# Text Embeddings

## 원본 URL

https://docs.voyageai.com/docs/embeddings

## 추출 본문

Text Embeddings

Jump to Content

GuidesAPI ReferenceChangelogDiscussionsHomeDocumentationBlogAbout

Guides

HomeDocumentationBlogAbout

GuidesAPI ReferenceChangelogDiscussions

Text Embeddings

All

Pages

Start typing to search…

GET STARTED

Introduction

API Key and Python Client

Quickstart Tutorial

CAPABILITIES

Text Embeddings

Contextualized Chunk Embeddings

Multimodal Embeddings

Rerankers

GUIDES

Tokenization

Flexible Dimensions and Quantization

Batch Inference

Error Codes

Rate Limits

Pricing

Organizations and Projects

Service Level Objectives

DEPLOYMENT ON VPC

AWS Marketplace Model Package
MongoDB Voyage AI Models in AWS

Voyage AI Models in AWS

Azure Marketplace Managed Application
MongoDB Voyage AI Models in Azure

Voyage AI Models in Azure

ACCESS VIA DATA PLATFORMS

Snowflake

Community

Integrations

Community SDKs

HELP

FAQ

Contact Email

Discord

Powered by

Text Embeddings

Model Choices

Voyage currently provides the following text embedding models:

ModelContext Length (tokens)Embedding DimensionDescription
voyage-4-large
32,0001024 (default), 256, 512, 2048The best general-purpose and multilingual retrieval quality. All embeddings created with the 4 series are compatible with each other. See blog post for details.
voyage-4
32,0001024 (default), 256, 512, 2048Optimized for general-purpose and multilingual retrieval quality. All embeddings created with the 4 series are compatible with each other. See blog post for details.
voyage-4-lite
32,0001024 (default), 256, 512, 2048Optimized for latency and cost. All embeddings created with the 4 series are compatible with each other. See blog post for details.
voyage-code-3
32,0001024 (default), 256, 512, 2048Optimized for code retrieval. See blog post for details.
voyage-finance-2
32,0001024Optimized for finance retrieval and RAG. See blog post for details.
voyage-law-2
16,0001024Optimized for legal retrieval and RAG. Also improved performance across all domains. See blog post for details.
voyage-code-2
16,0001536Optimized for code retrieval (17% better than alternatives) / Previous generation of code embeddings. See blog post for details.

Need help deciding which text embedding model to use? Check out our FAQ.
Older models 
The following are our earlier models, which are still accessible from our API. We recommend using the new models above for better quality and efficiency. Our latest models listed in the above table will be strictly better than the legacy models in all aspects, such as quality, context length, latency, and throughput.

ModelContext Length (tokens)Embedding DimensionDescription
voyage-3-large
32,0001024 (default), 256, 512, 2048Previous generation of text embeddings for general-purpose and multilingual retrieval quality. See blog post for details.
voyage-3.5
32,0001024 (default), 256, 512, 2048Previous generation of text embeddings optimized for general-purpose and multilingual retrieval quality. See blog post for details.
voyage-3.5-lite
32,0001024 (default), 256, 512, 2048Previous generation of text embeddings optimized for latency and cost. See blog post for details.
voyage-3
32,0001024Optimized for general-purpose and multilingual retrieval quality. See blog post for details.
voyage-3-lite
32,000512Optimized for latency and cost. See blog post for details.
voyage-multilingual-2
32,0001024Optimized for multilingual retrieval and RAG. See blog post for details.
voyage-large-2-instruct
16,0001024Top of MTEB leaderboard. Instruction-tuned general-purpose embedding model optimized for clustering, classification, and retrieval. For retrieval, please use 
input_type
 parameter to specify whether the text is a query or document. For classification and clustering, please use the instructions here. See blog post for details. We recommend existing 
voyage-large-2-instruct
 users to transition to 
voyage-3
.
voyage-large-2
16,0001536General-purpose embedding model that is optimized for retrieval quality (e.g., better than OpenAI V3 Large). Please transition to 
voyage-3
.
voyage-2
40001024General-purpose embedding model optimized for a balance between cost, latency, and retrieval quality. Please transition to 
voyage-3-lite
.
voyage-lite-02-instruct
40001024[Deprecated] Instruction-tuned for classification, clustering, and sentence textual similarity tasks, which are the only recommended use cases. Please transition to 
voyage-3
.
voyage-02
40001024[Deprecated] This is our pilot-version v2 embedding model. We kindly ask you to transition to 
voyage-3
 as detailed above.
voyage-01
40001024[Deprecated] This is our v1 embedding model. Please transition to 
voyage-3
.
voyage-lite-01
40001024[Deprecated] This is our v1 embedding model. Please transition to 
voyage-3
.
voyage-lite-01-instruct
40001024[Deprecated] Tweaked on top of 
voyage-lite-01
 for classification and clustering tasks. Please transition to 
voyage-3
.

Open Models

Voyage also provides the following open-weight embedding models:

ModelContext Length (tokens)Embedding DimensionDescription
voyage-4-nano
32,0001024 (default), 256, 512, 2048Open-weight model available on Hugging Face. All embeddings created with the 4 series are compatible with eachother. See blog post for details.

Python API

Voyage text embeddings are accessible in Python through the 
voyageai
package. Please install the 
voyageai
 package, set up the API key, and use the 
voyageai.Client.embed()
 function to vectorize your inputs.

>

Parameters

texts (str or List[str]) - A single text string, or a list of texts as a list of strings, such as 
["I like cats", "I also like dogs"]
. Currently, we have two constraints on the list:
The maximum length of the list is 1,000.

The total number of tokens in the list is at most 1M for 
voyage-4-lite
, 
voyage-3.5-lite
; 320K for 
voyage-4
, 
voyage-3.5
, and 
voyage-2
; and 120K for 
voyage-4-large
, 
voyage-3-large
, 
voyage-code-3
, 
voyage-large-2-instruct
, 
voyage-finance-2
, 
voyage-multilingual-2
, and 
voyage-law-2
.

model (str) - Name of the model. Recommended options: 
voyage-4-large
, 
voyage-4
, 
voyage-4-lite
, 
voyage-3-large
, 
voyage-3.5
, 
voyage-3.5-lite
, 
voyage-code-3
, 
voyage-finance-2
, 
voyage-law-2
.

input_type (str, optional, defaults to 
None
) - Type of the input text. Options: 
None
, 
query
, 
document
.
When 
input_type
 is 
None
 , the embedding model directly converts the inputs (
texts
) into numerical vectors. For retrieval/search purposes, where a "query" is used to search for relevant information among a collection of data, referred to as "documents", we recommend specifying whether your inputs (
texts
) are intended as queries or documents by setting 
input_type
 to 
query
 or 
document
 , respectively. In these cases, Voyage automatically prepends a prompt to your inputs (
texts
) before vectorizing them, creating vectors more tailored for retrieval/search tasks. Embeddings generated with and without the 
input_type
 argument are compatible.

For transparency, the following prompts are prepended to your input.
For query, the prompt is "_Represent the query for retrieving supporting documents: _".

For document, the prompt is "_Represent the document for retrieval: _".

truncation (bool, optional, defaults to 
True
) - Whether to truncate the input texts to fit within the context length.
If 
True
, an over-length input texts will be truncated to fit within the context length, before vectorized by the embedding model.

If 
False
, an error will be raised if any given text exceeds the context length.

output_dimension (int, optional, defaults to 
None
) - The number of dimensions for resulting output embeddings.
Most models only support a single default dimension, used when 
output_dimension
 is set to 
None
 (see model embedding dimensions above).

voyage-4-large
, 
voyage-4
, 
voyage-4-lite
, 
voyage-3-large
, 
voyage-3.5
, 
voyage-3.5-lite
, and 
voyage-code-3
 support the following 
output_dimension
 values: 2048, 1024 (default), 512, and 256.

output_dtype (str, optional, defaults to 
float
) - The data type for the embeddings to be returned. Options: 
float
, 
int8
, 
uint8
, 
binary
, 
ubinary
. 
float
 is supported for all models. 
int8
, 
uint8
, 
binary
, and 
ubinary
 are supported by 
voyage-4-large
, 
voyage-4
, 
voyage-4-lite
, 
voyage-3-large
, 
voyage-3.5
, 
voyage-3.5-lite
, and 
voyage-code-3
. Please see our guide for more details about output data types.

float
: Each returned embedding is a list of 32-bit (4-byte) single-precision floating-point numbers. This is the default and provides the highest precision / retrieval accuracy.

int8
 and 
uint8
: Each returned embedding is a list of 8-bit (1-byte) integers ranging from -128 to 127 and 0 to 255, respectively.

binary
 and 
ubinary
: Each returned embedding is a list of 8-bit integers that represent bit-packed, quantized single-bit embedding values: 
int8
 for 
binary
 and 
uint8
 for 
ubinary
. The length of the returned list of integers is 1/8 of 
output_dimension
 (which is the actual dimension of the embedding). The 
binary
 type uses the offset binary method. Please refer to our guide for details on offset binary and binary embeddings.

Returns

A 
EmbeddingsObject
, containing the following attributes:
embeddings (List[List[float]] or List[List[int]]) - A list of embeddings for the corresponding list of input texts. Each embedding is a vector represented as a list of floats when 
output_dtype
 is set to 
float
 and as a list of integers for all other values of 
output_dtype
 (
int8
, 
uint8
, 
binary
, 
ubinary
).

total_tokens (int) - The total number of tokens in the input texts.

Example

PythonOutput

import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = [
 "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
 "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
 "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
 "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
 "Apple’s conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
 "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
]

# Embed the documents
result = vo.embed(texts, model="voyage-4-large", input_type="document")
print(result.embeddings)

[
 [-0.01225314, 0.00206815, 0.030598236, ...],
 [0.008976975,-0.002981404,0.015463986, ...],
 [-0.062971942,-0.047771815,-0.101127356, ...],
 [0.047902156,-0.004106794,-0.007774695, ...],
 [-0.008545358,-0.063952357,-0.007111943, ...],
 [-0.00172591,-0.004946421,-0.04327229, ...]
]

Deprecated Functions

The following functions are deprecated and will be removed in the future.

>

Parameters

text - A single document/query as a string, such as 
"I like cats"
 .

model - Name of the model. Options: 
voyage-01
 (default), 
voyage-lite-01
.

input_type - Type of the input text. Defalut to 
None
, meaning the type is unspecified. Other options: 
query
, 
document
.

Returns

An embedding vector (a list of floating-point numbers) for the document.

>

Parameters

list_of_text - A list of documents as a list of strings, such as 
["I like cats", "I also like dogs"]
. The maximum length of the list is 64.

model - Name of the model. Options: 
voyage-01
 (default), 
voyage-lite-01
.

input_type - Type of the input text. Defalut to 
None
, meaning the type is unspecified. Other options: 
query
, 
document
.

Returns

A list of embedding vectors.

REST API

Voyage text embeddings can be accessed by calling the endpoint 
POST https://api.voyageai.com/v1/embeddings
. Please refer to the Text Embeddings API Reference for the specification.

Example

Embed a single stringEmbed a list of strings

curl https://api.voyageai.com/v1/embeddings \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $VOYAGE_API_KEY" \
 -d '{
 "input": "Sample text",
 "model": "voyage-4-large",
 "input_type": "document"
 }'

curl https://api.voyageai.com/v1/embeddings \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $VOYAGE_API_KEY" \
 -d '{
 "input": ["Sample text 1", "Sample text 2"],
 "model": "voyage-4-large",
 "input_type": "document"
 }'

TypeScript Library

Voyage text embeddings are accessible in TypeScript through the Voyage TypeScript Library, which exposes all the functionality of our text embeddings endpoint (see Text Embeddings API Reference).

Updated3 months ago

Quickstart Tutorial

Contextualized Chunk Embeddings

Ask AI
