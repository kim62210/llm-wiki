---
title: baml module - github.com/boundaryml/baml - Go Packages
source_url: https://pkg.go.dev/github.com/boundaryml/baml
final_url: https://pkg.go.dev/github.com/boundaryml/baml
status: 200
content_type: text/html; charset=utf-8
topics: [BAML (Boundary ML) — Prompts as Typed Functions]
sections: [Dev Tooling & Frameworks]
fetched_at: 2026-04-10T01:44:26.750101+00:00
---

# baml module - github.com/boundaryml/baml - Go Packages

## 원본 URL

https://pkg.go.dev/github.com/boundaryml/baml

## 추출 본문

baml module - github.com/boundaryml/baml - Go Packages

 Skip to Main Content 

 Why Go
 

Case Studies

Common problems companies solve with Go

Use Cases

Stories about how and why companies use Go

Security

How Go can help keep you secure by default

Learn

 Docs
 

Effective Go

Tips for writing clear, performant, and idiomatic Go code

Go User Manual

A complete introduction to building software with Go

Standard library

Reference documentation for Go's standard library

Release Notes

Learn what's new in each Go release

Packages

 Community
 

Recorded Talks

Videos from prior events

Meetups

Meet other local Go developers

Conferences

Learn and network with Go developers from around the world

Go blog

The Go project's official blog.

Go project

Get help and stay informed from Go

 Get connected
 

Why Go

 Why Go
 

 Case Studies
 

 Use Cases
 

 Security
 

Learn

Docs

 Docs
 

 Effective Go
 

 Go User Manual
 

 Standard library
 

 Release Notes
 

Packages

Community

 Community
 

 Recorded Talks
 

 Meetups
 

 Conferences
 

 Go blog
 

 Go project
 

Get connected

Discover Packages

 github.com/boundaryml/baml
 

baml
module

Version: 
 v0.220.0
 

 Opens a new window with list of versions in this module.
 
Latest
 Latest
 
 
This package is not in the latest version of its module.
Go to latest
 Published: Mar 11, 2026
 
 License: Apache-2.0

 Opens a new window with license information.
 

Main
 Versions
 
 Licenses
 

Details

 Valid go.mod file
 

 The Go module system was introduced in Go 1.11 and is the official dependency management
 solution for Go.
 

 Redistributable license
 

 Redistributable licenses place minimal restrictions on how software can be used,
 modified, and redistributed.
 

 Tagged version
 
Modules with tagged versions give importers more predictable builds.

 Stable version
 
When a project reaches major version v1 it is considered stable.

Learn more about best practices

Repository

 github.com/boundaryml/baml
 

Links

 Open Source Insights
 

 Code Wiki
 

 Jump to ...
 

 README
 

 BAML: Basically a Made-up Language
 

 The core BAML principle: LLM Prompts are functions
 

 BAML Functions can be called from any language
 

 Test prompts 10x faster, right in your IDE
 

 Enable reliable tool-calling with any model
 

 Switch from 100s of models in a couple lines
 

 Build beautiful streaming UIs
 

 Fully Open-Source, and offline
 

 BAML's Design Philosophy
 

 Why a new programming language
 

 Conclusion
 

 FAQ
 

 Contributing
 

 Citation
 

 Directories
 

README

 README
 ¶

BAML: Basically a Made-up Language

Homepage | Docs | BAML AI Chat | Discord

BAML is a simple prompting language for building reliable AI workflows and agents.

BAML makes prompt engineering easy by turning it into schema engineering -- where you mostly focus on the models of your prompt -- to get more reliable outputs.
You don't need to write your whole app in BAML, only the prompts! You can wire-up your LLM Functions in any language of your choice! See our quickstarts for Python, TypeScript, Ruby and Go, and more.

BAML comes with all batteries included -- with full typesafety, streaming, retries, wide model support, even when they don't support native tool-calling APIs

Try BAML: Prompt Fiddle • Interactive App Examples

The core BAML principle: LLM Prompts are functions

The fundamental building block in BAML is a function. Every prompt is a function that takes in parameters and returns a type.

function ChatAgent(message: Message[], tone: "happy" | "sad") -> string

Every function additionally defines which models it uses and what its prompt is.

function ChatAgent(message: Message[], tone: "happy" | "sad") -> StopTool | ReplyTool {
 client "openai/gpt-4o-mini"

 prompt #"
 Be a {{ tone }} bot.

 {{ ctx.output_format }}

 {% for m in message %}
 {{ _.role(m.role) }}
 {{ m.content }}
 {% endfor %}
 "#
}

class Message {
 role string
 content string
}

class ReplyTool {
 response string
}

class StopTool {
 action "stop" @description(#"
 when it might be a good time to end the conversation
 "#)
}

BAML Functions can be called from any language

Below we call the ChatAgent function we defined in BAML through Python. BAML's Rust compiler generates a "baml_client" to access and call them.

from baml_client import b
from baml_client.types import Message, StopTool

messages = [Message(role="assistant", content="How can I help?")]

while True:
 print(messages[-1].content)
 user_reply = input()
 messages.append(Message(role="user", content=user_reply))
 tool = b.ChatAgent(messages, "happy")
 if isinstance(tool, StopTool):
 print("Goodbye!")
 break
 else:
 messages.append(Message(role="assistant", content=tool.response))

You can write any kind of agent or workflow using chained BAML functions. An agent is a while loop that calls a Chat BAML Function with some state.

And if you need to stream, add a couple more lines:

stream = b.stream.ChatAgent(messages, "happy")
# partial is a Partial type with all Optional fields
for tool in stream:
 if isinstance(tool, StopTool):
 ...
 
final = stream.get_final_response()

And get fully type-safe outputs for each chunk in the stream.

Test prompts 10x faster, right in your IDE

BAML comes with native tooling for VSCode (jetbrains + neovim coming soon).

Visualize full prompt (including any multi-modal assets), and the API request. BAML gives you full transparency and control of the prompt.

Using AI is all about iteration speed.

If testing your pipeline takes 2 minutes, you can only test 10 ideas in 20 minutes.

If you reduce it to 5 seconds, you can test 240 ideas in the same amount of time.

The playground also allows you to run tests in parallel -- for even faster iteration speeds 🚀.

No need to login to websites, and no need to manually define json schemas.

Enable reliable tool-calling with any model

BAML works even when the models don't support native tool-calling APIs. We created the SAP (schema-aligned parsing) algorithm to support the flexible outputs LLMs can provide, like markdown within a JSON blob or chain-of-thought prior to answering. Read more about SAP

With BAML, your structured outputs work in Day-1 of a model release. No need to figure out whether a model supports parallel tool calls, or whether it supports recursive schemas, or 
anyOf
 or 
oneOf
 etc.

See it in action with: Deepseek-R1 and OpenAI O1.

Switch from 100s of models in a couple lines

function Extract() -> Resume {
+ client openai/o3-mini
 prompt #"
 ....
 "#
}

Retry policies • fallbacks • model rotations. All statically defined.

Want to do pick models at runtime? Check out the Client Registry.

We support: OpenAI • Anthropic • Gemini • Vertex • Bedrock • Azure OpenAI • Anything OpenAI Compatible (Ollama, OpenRouter, VLLM, LMStudio, TogetherAI, and more)

Build beautiful streaming UIs

BAML generates a ton of utilities for NextJS, Python (and any language) to make streaming UIs easy.

BAML's streaming interfaces are fully type-safe. Check out the Streaming Docs, and our React hooks

Fully Open-Source, and offline

100% open-source (Apache 2)

100% private. AGI will not require an internet connection, neither will BAML

No network requests beyond model calls you explicitly set

Not stored or used for any training data

BAML files can be saved locally on your machine and checked into Github for easy diffs.

Built in Rust. So fast, you can't even tell it's there.

BAML's Design Philosophy

Everything is fair game when making new syntax. If you can code it, it can be yours. This is our design philosophy to help restrict ideas:

1: Avoid invention when possible

Yes, prompts need versioning — we have a great versioning tool: git

Yes, you need to save prompts — we have a great storage tool: filesystems

2: Any file editor and any terminal should be enough to use it

3: Be fast

4: A first year university student should be able to understand it

Why a new programming language

We used to write websites like this:

def home():
 return "<button onclick=\"() => alert(\\\"hello!\\\")\">Click</button>"

And now we do this:

function Home() {
 return <button onClick={() => setCount(prev => prev + 1)}>
 {count} clicks!
 </button>
}

New syntax can be incredible at expressing new ideas. Plus the idea of maintaining hundreds of f-strings for prompts kind of disgusts us 🤮. Strings are bad for maintainable codebases. We prefer structured strings.

The goal of BAML is to give you the expressiveness of English, but the structure of code.

Full blog post by us.

Conclusion

As models get better, we'll continue expecting even more out of them. But what will never change is that we'll want a way to write maintainable code that uses those models. The current way we all just assemble strings is very reminiscent of the early days PHP/HTML soup in web development. We hope some of the ideas we shared today can make a tiny dent in helping us all shape the way we all code tomorrow.

FAQ
Do I need to write my whole app in BAML?Nope, only the prompts! BAML translates definitions into the language of your choice! Python, TypeScript, Ruby and more.Is BAML stable?Yes, many companies use it in production! We ship updates weekly!Why a new language?Jump to section
Contributing

Checkout our guide on getting started

Citation

You can cite the BAML repo as follows:

@software{baml,
 author = {Boundary ML},
 title = {BAML},
 url = {https://github.com/boundaryml/baml},
 year = {2024}
}

Made with ❤️ by Boundary

HQ in Seattle, WA

P.S. We're hiring for software engineers that love rust. Email us or reach out on discord!

Expand ▾Collapse ▴

 Directories
 ¶

 Show internal
 
 Expand all
 

PathSynopsis

baml

baml-cli

engine
generators/languages/go/generated_tests/array_types/baml_client

generators/languages/go/generated_tests/array_types/baml_client/stream_types

generators/languages/go/generated_tests/array_types/baml_client/type_builder

generators/languages/go/generated_tests/array_types/baml_client/types

generators/languages/go/generated_tests/asserts/baml_client

generators/languages/go/generated_tests/asserts/baml_client/stream_types

generators/languages/go/generated_tests/asserts/baml_client/type_builder

generators/languages/go/generated_tests/asserts/baml_client/types

generators/languages/go/generated_tests/classes/baml_client

generators/languages/go/generated_tests/classes/baml_client/stream_types

generators/languages/go/generated_tests/classes/baml_client/type_builder

generators/languages/go/generated_tests/classes/baml_client/types

generators/languages/go/generated_tests/dynamic_types/baml_client

generators/languages/go/generated_tests/dynamic_types/baml_client/stream_types

generators/languages/go/generated_tests/dynamic_types/baml_client/type_builder

generators/languages/go/generated_tests/dynamic_types/baml_client/types

generators/languages/go/generated_tests/edge_cases/baml_client

generators/languages/go/generated_tests/edge_cases/baml_client/stream_types

generators/languages/go/generated_tests/edge_cases/baml_client/type_builder

generators/languages/go/generated_tests/edge_cases/baml_client/types

generators/languages/go/generated_tests/enums/baml_client

generators/languages/go/generated_tests/enums/baml_client/stream_types

generators/languages/go/generated_tests/enums/baml_client/type_builder

generators/languages/go/generated_tests/enums/baml_client/types

generators/languages/go/generated_tests/literal_types/baml_client

generators/languages/go/generated_tests/literal_types/baml_client/stream_types

generators/languages/go/generated_tests/literal_types/baml_client/type_builder

generators/languages/go/generated_tests/literal_types/baml_client/types

generators/languages/go/generated_tests/map_types/baml_client

generators/languages/go/generated_tests/map_types/baml_client/stream_types

generators/languages/go/generated_tests/map_types/baml_client/type_builder

generators/languages/go/generated_tests/map_types/baml_client/types

generators/languages/go/generated_tests/media_types/baml_client

generators/languages/go/generated_tests/media_types/baml_client/stream_types

generators/languages/go/generated_tests/media_types/baml_client/type_builder

generators/languages/go/generated_tests/media_types/baml_client/types

generators/languages/go/generated_tests/mixed_complex_types/baml_client

generators/languages/go/generated_tests/mixed_complex_types/baml_client/stream_types

generators/languages/go/generated_tests/mixed_complex_types/baml_client/type_builder

generators/languages/go/generated_tests/mixed_complex_types/baml_client/types

generators/languages/go/generated_tests/nested_structures/baml_client

generators/languages/go/generated_tests/nested_structures/baml_client/stream_types

generators/languages/go/generated_tests/nested_structures/baml_client/type_builder

generators/languages/go/generated_tests/nested_structures/baml_client/types

generators/languages/go/generated_tests/optional_nullable/baml_client

generators/languages/go/generated_tests/optional_nullable/baml_client/stream_types

generators/languages/go/generated_tests/optional_nullable/baml_client/type_builder

generators/languages/go/generated_tests/optional_nullable/baml_client/types

generators/languages/go/generated_tests/primitive_types/baml_client

generators/languages/go/generated_tests/primitive_types/baml_client/stream_types

generators/languages/go/generated_tests/primitive_types/baml_client/type_builder

generators/languages/go/generated_tests/primitive_types/baml_client/types

generators/languages/go/generated_tests/recursive_types/baml_client

generators/languages/go/generated_tests/recursive_types/baml_client/stream_types

generators/languages/go/generated_tests/recursive_types/baml_client/type_builder

generators/languages/go/generated_tests/recursive_types/baml_client/types

generators/languages/go/generated_tests/sample/baml_client

generators/languages/go/generated_tests/sample/baml_client/stream_types

generators/languages/go/generated_tests/sample/baml_client/type_builder

generators/languages/go/generated_tests/sample/baml_client/types

generators/languages/go/generated_tests/semantic_streaming/baml_client

generators/languages/go/generated_tests/semantic_streaming/baml_client/stream_types

generators/languages/go/generated_tests/semantic_streaming/baml_client/type_builder

generators/languages/go/generated_tests/semantic_streaming/baml_client/types

generators/languages/go/generated_tests/union_types_extended/baml_client

generators/languages/go/generated_tests/union_types_extended/baml_client/stream_types

generators/languages/go/generated_tests/union_types_extended/baml_client/type_builder

generators/languages/go/generated_tests/union_types_extended/baml_client/types

generators/languages/go/generated_tests/unions/baml_client

generators/languages/go/generated_tests/unions/baml_client/stream_types

generators/languages/go/generated_tests/unions/baml_client/type_builder

generators/languages/go/generated_tests/unions/baml_client/types

language_client_go/baml_go

language_client_go/baml_go/raw_objects

language_client_go/baml_go/serde

language_client_go/baml_go/shared

language_client_go/pkg

language_client_go/pkg/cffi

gomodule

 Click to show internal directories. 

 Click to hide internal directories. 

 Why Go
 
 Use Cases
 
 Case Studies
 

 Get Started
 
 Playground
 
 Tour
 
 Stack Overflow
 
 Help
 

 Packages
 
 Standard Library
 
 Sub-repositories
 
 About Go Packages
 

 About
 DownloadBlog
 Issue Tracker
 
 Release Notes
 
 Brand Guidelines
 
 Code of Conduct
 

 Connect
 
 Twitter
 GitHub
 Slack
 
 r/golang
 
 Meetup
 
 Golang Weekly
 

Copyright

Terms of Service

 Privacy Policy
 

 Report an Issue
 

 Theme Toggle 

 Shortcuts Modal 

Jump to

Close

Keyboard shortcuts

? : This menu/ : Search sitef or F : Jump toy or Y : Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
 analyze traffic. Learn more.

Okay
