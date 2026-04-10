---
title: GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub
source_url: https://github.com/jina-ai/late-chunking
final_url: https://github.com/jina-ai/late-chunking
status: 200
content_type: text/html; charset=utf-8
topics: [Contextual Retrieval (Anthropic)]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:49.558870+00:00
---

# GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub

## 원본 URL

https://github.com/jina-ai/late-chunking

## 추출 본문

GitHub - jina-ai/late-chunking: Code for explaining and evaluating late chunking (chunked pooling) · GitHub

Skip to content

Navigation Menu
Toggle navigation

 Sign in
 
Appearance settings

Platform

AI CODE CREATION

GitHub CopilotWrite better code with AI

GitHub SparkBuild and deploy intelligent apps

GitHub ModelsManage and compare prompts

MCP RegistryNewIntegrate external tools

DEVELOPER WORKFLOWS

ActionsAutomate any workflow

CodespacesInstant dev environments

IssuesPlan and track work

Code ReviewManage code changes

APPLICATION SECURITY

GitHub Advanced SecurityFind and fix vulnerabilities

Code securitySecure your code as you build

Secret protectionStop leaks before they start

EXPLORE
Why GitHub

Documentation

Blog

Changelog

Marketplace

View all features

Solutions

BY COMPANY SIZE
Enterprises

Small and medium teams

Startups

Nonprofits

BY USE CASE
App Modernization

DevSecOps

DevOps

CI/CD

View all use cases

BY INDUSTRY
Healthcare

Financial services

Manufacturing

Government

View all industries

View all solutions

Resources

EXPLORE BY TOPIC
AI

Software Development

DevOps

Security

View all topics

EXPLORE BY TYPE
Customer stories

Events & webinars

Ebooks & reports

Business insights

GitHub Skills

SUPPORT & SERVICES
Documentation

Customer support

Community forum

Trust center

Partners

View all resources

Open Source

COMMUNITY

GitHub SponsorsFund open source developers

PROGRAMS
Security Lab

Maintainer Community

Accelerator

GitHub Stars

Archive Program

REPOSITORIES
Topics

Trending

Collections

Enterprise

ENTERPRISE SOLUTIONS

Enterprise platformAI-powered developer platform

AVAILABLE ADD-ONS

GitHub Advanced SecurityEnterprise-grade security features

Copilot for BusinessEnterprise-grade AI features

Premium SupportEnterprise-grade 24/7 support

Pricing

Search or jump to...

Search code, repositories, users, issues, pull requests...

 Search
 

Clear

Search syntax tips

 Provide feedback
 

We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted

 Cancel
 Submit feedback

 Saved searches
 

Use saved searches to filter your results more quickly

Name

Query

 To see all available qualifiers, see our documentation.
 

 Cancel
 Create saved search

 Sign in
 

 Sign up
 
Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

 jina-ai
/late-chunkingPublic

Notifications
You must be signed in to change notification settings

Fork
 44

 Star
498

Code

Issues1

Pull requests0

Actions

Projects

Security and quality0

Insights

Additional navigation options

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security and quality

 Insights

jina-ai/late-chunking

main

BranchesTags

Go to file

Code
Open more actions menu

Folders and files
NameName
Last commit message

Last commit date

Latest commit

History
44 Commits

44 Commits

.github/workflows

.github/workflows

chunked_pooling

chunked_pooling

img

img

tests

tests

LICENSE

LICENSE

README.md

README.md

examples.ipynb

examples.ipynb

explanatory_contextual_retrieval.py

explanatory_contextual_retrieval.py

pyproject.toml

pyproject.toml

run_chunked_eval.py

run_chunked_eval.py

View all files

Repository files navigation

README

Apache-2.0 license

Late Chunking of Short Chunks in Long-Context Embedding Models

Blog part 1 | Blog part 2 | ArXiv paper

For many applications, encoding a whole text document into a single embedding representation is not useful. Many applications require retrieving smaller parts of the text and dense vector-based information retrieval systems often perform better with smaller text segments because of the limited information capacity of embedding vectors.

RAG (Retrieval Augmented Generations) is one of the best known applications to require splitting document collections into smaller text chunks. These chunks are typically stored in a vector database with vector representations created by a text embedding model.
At runtime, the same embedding model encodes a query text into a vector representation, which is used to identify relevant stored text chunks. These are them passed to a large language model (LLM) which synthesizes a response to the query based on the retrieved texts.

Context Problem

This simple RAG approach is not without challenges. Long distance contextual dependencies, i.e. when the relevant information is spread over multiple chunks and taking text segments out of context makes them useless, are particularly poorly handled by this approach.

In the image above one can see an Wikipedia article that is split into chunks of sentences.
One can see that phrases like "its" and "the city" referencing "Berlin" which is mentioned only in the first sentence, e.g., it is harder for the embedding model to link it to the respective entity to produce a high-quality embedding representation.

For example, if we split a Wikipedia article into sentence-length segments, as in the example above, a RAG system might not be able to answer a query like "What is the population of Berlin?" The city name and the population never appear together in a single segment, and lacking any larger document context.
An LLM to which one of the segments is presented cannot resolve the anaphoric references like "it" or "the city".

Context-Sensitive Chunking

To overcome this problem, we take advantage of the long input sequences that recent embedding models like 
jina-embeddings-v2-base-en
 can process.
These models support much longer input texts, for example, 8192 tokens for 
jina-embeddings-v2-base-en
 or roughly ten standard pages of text. Text segments of this size are much less likely to have contextual dependencies that can only be resolved with a larger context.
However, we still need vector representations of much smaller chunks of text, in part because of the limited input sizes of LLMs but primarily because of the limited information capacity of short embedding vectors.

The simple encoding approach (as seen on the left side of the image above) chunks texts before processing them, using sentences, paragraphs, and maximum length limits to split text a priori, and then applying an embedding model to the resulting chunks.
Late Chunking, instead, first applies the transformer part from the embedding model to the entire text, or the largest part of it possible. This generates a sequence of vector representations for each token that encompass textual information from the entire text.
To generate a single embedding for a text, many embedding models apply mean pooling to these token representations to output a single vector. Late Chunking instead applies mean pooling to smaller segments of this sequence of token vectors, producing embeddings for each chunk that take into account the entire text.

The Effect of Context-Sensitive Chunking

This has immediately measurable concrete effects on retrieval. As an example, in case of "the city" and "Berlin" in a Wikipedia article, the vectors representing "the city" contain information connecting it to the previous mention of "Berlin", making it a much better match for queries involving that city name.

You can see that in numerical results below, which compares the embedding of the string "Berlin" to various sentences from the article about Berlin. The column "Traditional Similarity" is the similarity values using a priori chunking, and "Late Chunking Similarity" is with context-sensitive chunking.
TextSimilarity TraditionalSimilarity Late ChunkingBerlin is the capital and largest city of Germany, both by area and by population."0.848621850.849546Its more than 3.85 million inhabitants make it the European Union's most populous city, as measured by population within city limits.0.70843380.82489026The city is also one of the states of Germany, and is the third smallest state in the country in terms of area.0.75345530.84980094
As you can see the similarity scores for the first chunk that contains "Berlin" are very close to each other.
For the other two chunks they siginificantly differ, as the late chunking dramatically improves matching on sentences that do not explicitly use the word "Berlin" but have anaphoric references to it.

Evaluation on Retrieval Tasks

To verify the effectiveness of this approach beyond a few toy examples, we tested it with some of the retrieval benchmarks from BeIR.
Those retrieval tasks consist of a query set, a corpus of text documents, and a QRels file that stores information about the IDs of documents that are relevant for each query.
To identify the relevant documents of a query, one can chunk the documents, encode them into an embedding index, and determine for each query embedding the most similar chunks (kNN).
As each chunk corresponds to a document, one can convert the kNN ranking of chunks into a kNN ranking of documents (for documents occurring multiple times in the ranking, only the first occurrence is retained).
After that, one can compare the resulting ranking with the ranking corresponding to the ground-truth QRels file and calculate retrieval metrics like nDCG@10.
We run this evaluation for various BeIR datasets with traditional chunking and our novel late chunking method.
To split texts into chunks, we choose a straightforward method, which chunks the tests into strings of 256 tokens.
Both the traditional and late chunking tests used the jina-embeddings-v2-small-en model.
DatasetAVG Document Length (characters)Traditional Chunking (nDCG@10)Late Chunking (nDCG@10)No Chunking (nDCG@10)SciFact1498.464.20%66.10%63.89%TRECCOVID1116.763.36%64.70%65.18%FiQA2018767.233.25%33.84%33.43%NFCorpus1589.823.46%29.98%30.40%Quora62.287.19%87.19%87.19%
In all cases, late chunking improved the score. In some cases, it also outperforms encoding the whole document into a single embedding, while for other datasets, no chunking performs best. However, this only makes sense if one does not need to rank chunks. One can also see that the average length of the documents correlates with greater improvement in the nDCG scores through late chunking.

To reporoduce the evaluation, you can install the dependencies with 
pip install .
 and run the following script for the tasks "SciFactChunked", "TRECCOVIDChunked", "FiQA2018Chunked", "NFCorpusChunked", and "QuoraChunked":

python3 run_chunked_eval.py --task-name {TASK_NAME}

Acknowledgement and References

Thanks to Isabelle Mohr(@violenil) for contributing some code and Scott Martens (@scott-martens) for reviewing the README.

More about the Evaluation tasks can be found in the MTEB Repository and details about the training of the models for long input text in our paper: "Jina embeddings 2: 8192-token general-purpose text embeddings for long documents."

If you find Late Chunking useful in your research, use can cite the paper Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models:

@article{gunther2024late,
 title={Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models},
 author={G{\"u}nther, Michael and Mohr, Isabelle and Williams, Daniel J and Wang, Bo and Xiao, Han},
 journal={arXiv preprint arXiv:2409.04701},
 year={2024}
}

About

 Code for explaining and evaluating late chunking (chunked pooling)
 

Resources

 Readme

License

 Apache-2.0 license
 

 Uh oh!

There was an error while loading. Please reload this page.

Activity

Custom properties

Stars

498
 stars

Watchers

13
 watching

Forks

44
 forks

 Report repository

Releases

No releases published

Packages
 0

 Uh oh!

There was an error while loading. Please reload this page.

 Uh oh!

There was an error while loading. Please reload this page.

Contributors

 Uh oh!

There was an error while loading. Please reload this page.

Languages

Python91.8%

Jupyter Notebook8.2%

Footer

 © 2026 GitHub, Inc.
 

Footer navigation

Terms

Privacy

Security

Status

Community

Docs

Contact

 Manage cookies
 

 Do not share my personal information
 

 You can’t perform that action at this time.
