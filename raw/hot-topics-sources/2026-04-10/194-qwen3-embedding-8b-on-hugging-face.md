---
title: Qwen/Qwen3-Embedding-8B · Hugging Face
source_url: https://huggingface.co/Qwen/Qwen3-Embedding-8B
final_url: https://huggingface.co/Qwen/Qwen3-Embedding-8B
status: 200
content_type: text/html; charset=utf-8
topics: [Qwen3 / Voyage-4 Embedding Leaderboard Shakeup]
sections: [RAG & Context Engineering]
fetched_at: 2026-04-10T01:43:53.045120+00:00
---

# Qwen/Qwen3-Embedding-8B · Hugging Face

## 원본 URL

https://huggingface.co/Qwen/Qwen3-Embedding-8B

## 추출 본문

Qwen/Qwen3-Embedding-8B · Hugging Face

Hugging Face

 Models 

 Datasets 

 Spaces 

 Buckets new

 Docs 

 Enterprise 

Pricing

Log In

Sign Up

Qwen
/

Qwen3-Embedding-8B

like643

Follow
Qwen78.6k

Feature Extraction

sentence-transformers

Safetensors

Transformers

qwen3

text-generation

sentence-similarity

text-embeddings-inference

arxiv:2506.05176

License:apache-2.0

Model cardFilesFiles and versions
xet
Community
28

 Deploy

 Use this model

Qwen3-Embedding-8B
Highlights

Qwen3 Embedding Series Model list

Usage
Sentence Transformers Usage

Transformers Usage

vLLM Usage

Text Embeddings Inference (TEI) Usage

Evaluation
MTEB (Multilingual)

MTEB (Eng v2)

C-MTEB (MTEB Chinese)

Citation

 Qwen3-Embedding-8B
	

 Highlights
	

The Qwen3 Embedding model series is the latest proprietary model of the Qwen family, specifically designed for text embedding and ranking tasks. Building upon the dense foundational models of the Qwen3 series, it provides a comprehensive range of text embeddings and reranking models in various sizes (0.6B, 4B, and 8B). This series inherits the exceptional multilingual capabilities, long-text understanding, and reasoning skills of its foundational model. The Qwen3 Embedding series represents significant advancements in multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bitext mining.

Exceptional Versatility: The embedding model has achieved state-of-the-art performance across a wide range of downstream application evaluations. The 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58), while the reranking model excels in various text retrieval scenarios.

Comprehensive Flexibility: The Qwen3 Embedding series offers a full spectrum of sizes (from 0.6B to 8B) for both embedding and reranking models, catering to diverse use cases that prioritize efficiency and effectiveness. Developers can seamlessly combine these two modules. Additionally, the embedding model allows for flexible vector definitions across all dimensions, and both embedding and reranking models support user-defined instructions to enhance performance for specific tasks, languages, or scenarios.

Multilingual Capability: The Qwen3 Embedding series offer support for over 100 languages, thanks to the multilingual capabilites of Qwen3 models. This includes various programming languages, and provides robust multilingual, cross-lingual, and code retrieval capabilities.

Qwen3-Embedding-8B has the following features:

Model Type: Text Embedding

Supported Languages: 100+ Languages

Number of Paramaters: 8B

Context Length: 32k

Embedding Dimension: Up to 4096, supports user-defined output dimensions ranging from 32 to 4096

For more details, including benchmark evaluation, hardware requirements, and inference performance, please refer to our blog, GitHub.

 Qwen3 Embedding Series Model list
	

Model TypeModelsSizeLayersSequence LengthEmbedding DimensionMRL SupportInstruction AwareText EmbeddingQwen3-Embedding-0.6B0.6B2832K1024YesYesText EmbeddingQwen3-Embedding-4B4B3632K2560YesYesText EmbeddingQwen3-Embedding-8B8B3632K4096YesYesText RerankingQwen3-Reranker-0.6B0.6B2832K--YesText RerankingQwen3-Reranker-4B4B3632K--YesText RerankingQwen3-Reranker-8B8B3632K--Yes

Note:

MRL Support
 indicates whether the embedding model supports custom dimensions for the final embedding. 

Instruction Aware
 notes whether the embedding or reranking model supports customizing the input instruction according to different tasks.

Our evaluation indicates that, for most downstream tasks, using instructions (instruct) typically yields an improvement of 1% to 5% compared to not using them. Therefore, we recommend that developers create tailored instructions specific to their tasks and scenarios. In multilingual contexts, we also advise users to write their instructions in English, as most instructions utilized during the model training process were originally written in English.

 Usage
	

With Transformers versions earlier than 4.51.0, you may encounter the following error:

KeyError: 'qwen3'

 Sentence Transformers Usage
	

# Requires transformers>=4.51.0# Requires sentence-transformers>=2.7.0from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer("Qwen/Qwen3-Embedding-8B")

# We recommend enabling flash_attention_2 for better acceleration and memory saving,# together with setting `padding_side` to "left":# model = SentenceTransformer(# "Qwen/Qwen3-Embedding-8B",# model_kwargs={"attn_implementation": "flash_attention_2", "device_map": "auto"},# tokenizer_kwargs={"padding_side": "left"},# )# The queries and documents to embed
queries = [
 "What is the capital of China?",
 "Explain gravity",
]
documents = [
 "The capital of China is Beijing.",
 "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
]

# Encode the queries and documents. Note that queries benefit from using a prompt# Here we use the prompt called "query" stored under `model.prompts`, but you can# also pass your own prompt via the `prompt` argument
query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)

# Compute the (cosine) similarity between the query and document embeddings
similarity = model.similarity(query_embeddings, document_embeddings)
print(similarity)
# tensor([[0.7493, 0.0751],# [0.0880, 0.6318]])

 Transformers Usage
	

# Requires transformers>=4.51.0import torch
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel

deflast_token_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
 left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
 if left_padding:
 return last_hidden_states[:, -1]
 else:
 sequence_lengths = attention_mask.sum(dim=1) - 1
 batch_size = last_hidden_states.shape[0]
 return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]

defget_detailed_instruct(task_description: str, query: str) -> str:
 returnf'Instruct: {task_description}\nQuery:{query}'# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'

queries = [
 get_detailed_instruct(task, 'What is the capital of China?'),
 get_detailed_instruct(task, 'Explain gravity')
]
# No need to add instruction for retrieval documents
documents = [
 "The capital of China is Beijing.",
 "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."
]
input_texts = queries + documents

tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-Embedding-8B', padding_side='left')
model = AutoModel.from_pretrained('Qwen/Qwen3-Embedding-8B')

# We recommend enabling flash_attention_2 for better acceleration and memory saving.# model = AutoModel.from_pretrained('Qwen/Qwen3-Embedding-8B', attn_implementation="flash_attention_2", torch_dtype=torch.float16).cuda()

max_length = 8192# Tokenize the input texts
batch_dict = tokenizer(
 input_texts,
 padding=True,
 truncation=True,
 max_length=max_length,
 return_tensors="pt",
)
batch_dict.to(model.device)
outputs = model(**batch_dict)
embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T)
print(scores.tolist())
# [[0.7493016123771667, 0.0750647559762001], [0.08795969933271408, 0.6318399906158447]]

 vLLM Usage
	

# Requires vllm>=0.8.5import torch
import vllm
from vllm import LLM
defget_detailed_instruct(task_description: str, query: str) -> str:
 returnf'Instruct: {task_description}\nQuery:{query}'# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'
queries = [
 get_detailed_instruct(task, 'What is the capital of China?'),
 get_detailed_instruct(task, 'Explain gravity')
]
# No need to add instruction for retrieval documents
documents = [
 "The capital of China is Beijing.",
 "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."
]
input_texts = queries + documents
model = LLM(model="Qwen/Qwen3-Embedding-8B", task="embed")
outputs = model.embed(input_texts)
embeddings = torch.tensor([o.outputs.embedding for o in outputs])
scores = (embeddings[:2] @ embeddings[2:].T)
print(scores.tolist())
# [[0.7482624650001526, 0.07556197047233582], [0.08875375241041183, 0.6300010681152344]]

📌 Tip: We recommend that developers customize the 
instruct
 according to their specific scenarios, tasks, and languages. Our tests have shown that in most retrieval scenarios, not using an 
instruct
 on the query side can lead to a drop in retrieval performance by approximately 1% to 5%.

 Text Embeddings Inference (TEI) Usage
	

You can either run / deploy TEI on NVIDIA GPUs as:

docker run --gpus all -p 8080:80 -v hf_cache:/data --pull always ghcr.io/huggingface/text-embeddings-inference:1.7.2 --model-id Qwen/Qwen3-Embedding-8B --dtype float16

Or on CPU devices as:

docker run -p 8080:80 -v hf_cache:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cpu-1.7.2 --model-id Qwen/Qwen3-Embedding-8B --dtype float16

And then, generate the embeddings sending a HTTP POST request as:

curl http://localhost:8080/embed \
 -X POST \
 -d '{"inputs": ["Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: What is the capital of China?", "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: Explain gravity"]}' \
 -H "Content-Type: application/json"

 Evaluation
	

 MTEB (Multilingual)
	

ModelSizeMean (Task)Mean (Type)Bitxt MiningClass.Clust.Inst. Retri.Multi. Class.Pair. Class.RerankRetri.STSNV-Embed-v27B56.2949.5857.8457.2940.801.0418.6378.9463.8256.7271.10GritLM-7B7B60.9253.7470.5361.8349.753.4522.7779.9463.7858.3173.33BGE-M30.6B59.5652.1879.1160.3540.88-3.1120.180.7662.7954.6074.12multilingual-e5-large-instruct0.6B63.2255.0880.1364.9450.75-0.4022.9180.8662.6157.1276.81gte-Qwen2-1.5B-instruct1.5B59.4552.6962.5158.3252.050.7424.0281.5862.5860.7871.61gte-Qwen2-7b-Instruct7B62.5155.9373.9261.5552.774.9425.4885.1365.5560.0873.98text-embedding-3-large-58.9351.4162.1760.2746.89-2.6822.0379.1763.8959.2771.68Cohere-embed-multilingual-v3.0-61.1253.2370.5062.9546.89-1.8922.7479.8864.0759.1674.80gemini-embedding-exp-03-07-68.3759.5979.2871.8254.595.1829.1683.6365.5867.7179.40Qwen3-Embedding-0.6B0.6B64.3356.0072.2266.8352.335.0924.5980.8361.4164.6476.17Qwen3-Embedding-4B4B69.4560.8679.3672.3357.1511.5626.7785.0565.0869.6080.86Qwen3-Embedding-8B8B70.5861.6980.8974.0057.6510.0628.6686.4065.6370.8881.08

Note: For compared models, the scores are retrieved from MTEB online leaderboard on May 24th, 2025.

 MTEB (Eng v2)
	

MTEB English / ModelsParam.Mean(Task)Mean(Type)Class.Clust.Pair Class.Rerank.Retri.STSSumm.multilingual-e5-large-instruct0.6B65.5361.2175.5449.8986.2448.7453.4784.7229.89NV-Embed-v27.8B69.8165.0087.1947.6688.6949.6162.8483.8235.21GritLM-7B7.2B67.0763.2281.2550.8287.2949.5954.9583.0335.65gte-Qwen2-1.5B-instruct1.5B67.2063.2685.8453.5487.5249.2550.2582.5133.94stella_en_1.5B_v51.5B69.4365.3289.3857.0688.0250.1952.4283.2736.91gte-Qwen2-7B-instruct7.6B70.7265.7788.5258.9785.950.4758.0982.6935.74gemini-embedding-exp-03-07-73.367.6790.0559.3987.748.5964.3585.2938.28Qwen3-Embedding-0.6B0.6B70.7064.8885.7654.0584.3748.1861.8386.5733.43Qwen3-Embedding-4B4B74.6068.1089.8457.5187.0150.7668.4688.7234.39Qwen3-Embedding-8B8B75.2268.7190.4358.5787.5251.5669.4488.5834.83

 C-MTEB (MTEB Chinese)
	

C-MTEBParam.Mean(Task)Mean(Type)Class.Clust.Pair Class.Rerank.Retr.STSmultilingual-e5-large-instruct0.6B58.0858.2469.8048.2364.5257.4563.6545.81bge-multilingual-gemma29B67.6468.5275.3159.3086.6768.2873.7355.19gte-Qwen2-1.5B-instruct1.5B67.1267.7972.5354.6179.568.2171.8660.05gte-Qwen2-7B-instruct7.6B71.6272.1975.7766.0681.1669.2475.7065.20ritrieve_zh_v10.3B72.7173.8576.8866.585.9872.8676.9763.92Qwen3-Embedding-0.6B0.6B66.3367.4571.4068.7476.4262.5871.0354.52Qwen3-Embedding-4B4B72.2773.5175.4677.8983.3466.0577.0361.26Qwen3-Embedding-8B8B73.8475.0076.9780.0884.2366.9978.2163.53

 Citation
	

If you find our work helpful, feel free to give us a cite.

@article{qwen3embedding,
 title={Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},
 author={Zhang, Yanzhao and Li, Mingxin and Long, Dingkun and Zhang, Xin and Lin, Huan and Yang, Baosong and Xie, Pengjun and Yang, An and Liu, Dayiheng and Lin, Junyang and Huang, Fei and Zhou, Jingren},
 journal={arXiv preprint arXiv:2506.05176},
 year={2025}
}

Downloads last month1,572,226

Safetensors

Model size

8B params

Tensor type

BF16 
·

Chat template

Files info

Inference ProvidersNEW

Scaleway

Feature Extraction

Generate

View Code Snippets

Maximize

 Model tree for Qwen/Qwen3-Embedding-8B

Base model

Qwen/Qwen3-8B-Base

 Finetuned
(366)

this model

Adapters

5 models

Finetunes

22 models

Quantizations

20 models

 Spaces using Qwen/Qwen3-Embedding-8B43

🥇

mteb/leaderboard

🚀

alx-d/PhiRAG

🦀

ipepe/nomic-embeddings

⚖️

AldawsariNLP/Saudi-Law-AI-Assistant

🤖

MCP-1st-Birthday/legacy_code_modernizer

⚡

lupinlapin/Qwen-Qwen3-Embedding-8B

📚

destinyebuka/AIDA

🔬

khan125/Study_bot_physics

👁

miiann/miian-Q3

🚀

Ahmed-El-Zainy/rag_korean_manufacturing_docs

🍭

cortex359/germeval2025

🦀

MCP-1st-Birthday/central-memory-agent
+ 38 Spaces+ 31 Spaces

 Collection including Qwen/Qwen3-Embedding-8B

Qwen3-Embedding

 Collection

6 items•Updated Dec 31, 2025• 155

 Paper for Qwen/Qwen3-Embedding-8B

Qwen3 Embedding: Advancing Text Embedding and Reranking Through
 Foundation Models

 Paper • 2506.05176 •Published Jun 5, 2025• 80

 System theme

Company
TOSPrivacyAboutCareers
Website
ModelsDatasetsSpacesPricingDocs
