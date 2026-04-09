---
source_url: https://simonwillison.net/guides/agentic-engineering-patterns
author: Simon Willison
original_post_date: 2026-02-23
fetched: 2026-04-09
---

# Agentic Engineering Patterns (Simon Willison)

A guide compiled from https://simonwillison.net/guides/agentic-engineering-patterns and all sub-chapters as of 2026-04-09.

---

## Introduction post (2026-02-23)

Simon Willison launched a project documenting **Agentic Engineering Patterns** — professional practices for software engineers using coding agents like Claude Code that can both generate and execute code.

Willison differentiates "Agentic Engineering" from "vibe coding." While vibe coding involves non-programmers using LLMs without code knowledge, agentic engineering represents "professional software engineers using coding agents to improve and accelerate their work."

The initiative takes inspiration from the classic 1994 *Design Patterns* book, organizing content as chapter-based patterns. Each chapter functions as an evolving "guide" — content designed for updates over time rather than static blog posts.

Two foundational chapters launched immediately:
1. "Writing code is cheap now" — addresses how dramatically reduced costs for generating code change existing work assumptions
2. "Red/green TDD" — explains how test-first development improves agent-generated code reliability

Target: 1-2 new chapters weekly. Willison personally authors all written content, though he uses LLMs for proofreading and code examples.

---

## Section 1: Principles

### 1.1 What is agentic engineering?

Defined as "the practice of developing software with the assistance of coding agents."

**Coding agents** are agents capable of both writing and executing code, with examples including:
- Claude Code
- OpenAI Codex
- Gemini CLI

An **agent** is software that "runs tools in a loop to achieve a goal." The agent calls an LLM with a prompt, passes tool definitions, executes any requested tools, and feeds results back to the LLM.

For coding agents, the critical capability is code execution. "Without the ability to directly run the code, anything output by an LLM is of limited value."

Software engineering involves more than code generation. Engineers must determine *what* code to write, navigate tradeoffs, and tailor choices to circumstances.

Effective agentic engineering requires:
- Providing agents with necessary tools
- Specifying problems with appropriate detail
- Verifying and iterating on results
- Updating instructions based on learned lessons

**Distinction from "Vibe Coding"**: The term "vibe coding," coined by Andrej Karpathy in February 2025, describes prompting LLMs to write unreviewed, prototype-quality code. Agentic engineering targets "production ready standard" code.

### 1.2 Writing code is cheap now

The biggest challenge in adopting agentic engineering practices is getting comfortable with the consequences of the fact that *writing code is cheap now*.

Code has always been expensive. Producing a few hundred lines of clean, tested code takes most software developers a full day or more. Many engineering habits at both the macro and micro level are built around this core constraint.

At the **macro level** we spend time designing, estimating and planning projects to ensure expensive coding time is used efficiently. Product features are evaluated against development cost.

At the **micro level** we make hundreds of decisions daily based on available time — refactoring, documentation, edge case tests, debug interfaces.

Coding agents drop the cost of typing code into the computer, disrupting existing intuitions about tradeoffs. Parallel agents amplify this — one engineer can implement, refactor, test, and document in multiple places simultaneously.

**Good code still has a cost.** Delivering new code has dropped in price to almost free... but delivering *good* code remains significantly more expensive.

Criteria for good code:
- The code works. It does what it's meant to do, without bugs.
- We *know* the code works. Steps have been taken to confirm it's fit for purpose.
- It solves the right problem.
- It handles error cases gracefully and predictably.
- It's simple and minimal — humans and machines can understand and maintain it.
- It's protected by tests that also act as a regression suite.
- It's documented at an appropriate level, and documentation reflects current state.
- The design affords future changes (YAGNI, but also don't make future changes much harder).
- All relevant "ilities" — accessibility, testability, reliability, security, maintainability, observability, scalability, usability.

**We need to build new habits.** Best practices are still being figured out. For now: "any time our instinct says 'don't build that, it's not worth the time' fire off a prompt anyway, in an asynchronous agent session where the worst that can happen is you check ten minutes later and find that it wasn't worth the tokens."

### 1.3 Hoard things you know how to do

A key professional skill: understanding what's technologically possible and how to accomplish it. Examples:
- Can JavaScript perform OCR in a web browser?
- Can an iPhone app connect to Bluetooth when not running?
- Can Python process a 100GB JSON file without loading it entirely into memory?

"The more answers to questions like this you have under your belt, the more likely you'll be able to spot opportunities to deploy technology to solve problems."

**Building your collection**: seeing "running code" that demonstrates capability is best. Simon maintains:
- Personal blog and TIL (Today I Learned) blog
- Over a thousand GitHub repositories of proof-of-concepts
- tools.simonwillison.net — HTML-based tools
- simonw/research — complex examples where coding agents researched and produced working code with reports

**Recombining examples with agents**: Example — he had worked with Tesseract.js (WASM OCR) and PDF.js (PDF→image). Providing both to Claude 3 Opus with instructions to combine produced a browser PDF OCR tool (drag-drop PDFs → JPEG → OCR).

Coding agents amplify this:
- Fetch and analyze existing examples from URLs
- Search local repositories for implementation patterns
- Clone public repositories for reference code
- Use examples as templates for similar problems

**Core principle**: "coding agents mean we only ever need to figure out a useful trick *once*."

### 1.4 AI should help us produce better code

"Shipping worse code with agents is a *choice*. We can choose to ship code that is better instead."

**Avoiding technical debt**: common technical debt scenarios conceptually simple but time-consuming:
- API design issues requiring changes across many locations
- Naming inconsistencies
- Duplicate functionality needing consolidation
- Oversized files requiring modularization

These are ideal use cases for coding agents. Asynchronous tools like Gemini Jules, OpenAI Codex, or Claude Code allow background processing.

**Expanding solution exploration**: LLMs help identify overlooked conventional solutions and enable cost-effective prototyping across multiple approaches.

**Compound engineering loop**: drawing from Every's methodology, document successful approaches for future agent runs. Iterative improvement compounds over time.

### 1.5 Anti-patterns: things to avoid

**Inflicting unreviewed code on collaborators**: the most common and frustrating anti-pattern.

**Don't file pull requests with code you haven't reviewed yourself.**

If you open a PR with hundreds of lines an agent produced, and you haven't ensured it works, you're delegating the actual work to other people. "They could have prompted an agent themselves. What value are you even providing?"

A good agentic engineering pull request:
- The code works, and you are confident it works. "Your job is to deliver code that works."
- The change is small enough to review efficiently. Several small PRs beats one big one.
- Includes additional context explaining the change — higher-level goals, linked issues/specs.
- Agents write convincing-looking PR descriptions — you need to review these too.

Include evidence of personal effort: manual testing notes, implementation choice commentary, screenshots/video of the feature working.

---

## Section 2: Working with Coding Agents

### 2.1 How coding agents work

A coding agent functions as a **harness for an LLM**, extending language models with capabilities through invisible prompts and callable tools.

**Large Language Models**: ML models that complete text sequences. They process tokens (integer representations of text), not words directly. Providers charge based on token count.

Input = **prompt**; returned text = **completion** / **response**. Many modern models are **multimodal** (images + text).

**Chat templated prompts**: simulate conversation format:
```
user: write a python function to download a file from a URL
assistant:
```

LLMs are stateless — software maintains state and replays entire history each prompt, increasing costs as conversations lengthen.

**Token caching**: providers offer cheaper rates for cached input tokens. Common prefixes processed recently can reuse expensive calculations. Coding agents are designed to avoid modifying earlier conversation content for efficient cache usage.

**Calling tools**: the defining agent feature. Tools are functions available to the LLM. The agent harness extracts function calls from responses, executes them, returns results. Powerful tools: `Bash()` for terminal, `Python()` for code execution.

**The system prompt**: lengthy hidden behavioral instructions and tool definitions.

**Reasoning**: 2025 advancement where models generate intermediate problem-solving text before responding. Allows more token expenditure on complex problems, especially debugging.

**Implementation**: fundamental mechanics require LLM + system prompt + tools + loop — achievable in dozens of lines of code, though production-quality requires much more.

### 2.2 Using Git with coding agents

Git is critical for agent work: tracks, investigates, reverses code changes.

**Git essentials**: repository = folder tracking file changes through commits. Branches for independent experimentation before merging. Clone to new machines preserves history. Remote (GitHub) for collaboration and backup.

**Core concepts and prompts** agents understand:
- "Start a new Git repo here" → `git init`
- "Commit these changes"
- "Add username/repo as a github remote"
- "Review changes made today" → `git log`
- "Integrate latest changes from main"
- "Discuss options for integrating changes from main"
- "Sort out this git mess for me"
- "Find and recover my code that does..." → searches `reflog` and branches
- "Use git bisect to find when this bug was introduced..."

**Rewriting history**: consider history as "deliberately authored story," not permanent record.

Undo/rewrite commits:
- "Undo last commit" → `git reset --soft HEAD~1`
- "Remove [file] from that last commit"
- "Combine last three commits with a better commit message"

**Building new repositories from older ones**: agents can extract code while maintaining commit history — useful for library extraction or refactoring.

### 2.3 Subagents

**LLM context limitations**: context limit = maximum tokens processed simultaneously. Limits have remained relatively stagnant over two years — typically ~1,000,000 tokens, with optimal results often below 200,000.

**What are subagents?**: allow coding agents to handle larger tasks while preserving the parent's context window. A subagent receives a fresh copy of itself with its own context and a new prompt for a specific objective.

**Claude Code's Explore subagent example**: Claude Code dispatches an "Explore" subagent first on existing repositories to map codebase structure.

Example request: "Make the chapter diffs also show which characters have changed in this diff view with a darker color of red or green for the individually changed segments of text within the line."

The Explore subagent was instructed to locate:
- Templates rendering diffs with red/green backgrounds
- Python code generating diffs using difflib
- JavaScript related to diff rendering
- CSS styles for diff visualization

It returned comprehensive findings identifying the full diff implementation.

**Parallel subagents**: multiple subagents can execute simultaneously, especially when editing independent files. Can use faster/cheaper models like Claude Haiku. "Use subagents to find and update all templates affected by this change."

**Specialist subagents**:
- Code reviewers identifying bugs and design weaknesses
- Test runners managing verbose test outputs
- Debuggers isolating root causes through token-intensive analysis

---

## Section 3: Testing and QA

### 3.1 Red/green TDD

"**Use red/green TDD**" — a pleasingly succinct way to get better results from a coding agent.

TDD = Test Driven Development. The most disciplined form is test-first development:
1. Write tests first
2. Confirm they fail (red)
3. Iterate on implementation until they pass (green)

Fantastic fit for coding agents. Significant risk: agents might write code that doesn't work, or build unnecessary code, or both. Test-first protects against both and creates a regression suite.

Important: confirm tests fail before implementing. Otherwise a test might already pass, failing to exercise the new code.

Every good model understands "red/green TDD" as shorthand for the longer explanation.

**Example prompt**:
> Build a Python function to extract headers from a markdown string. Use red/green TDD.

### 3.2 First run the tests

"**Automated tests are no longer optional when working with coding agents.**"

Old excuses (time consuming, expensive to rewrite) don't hold when an agent can knock them into shape in minutes.

Tests ensure AI-generated code does what it claims. Without execution, it's pure luck if it works in production.

Tests also help agents get up to speed with existing codebases. Agents are biased toward testing; an existing test suite pushes them further.

At the start of a new session:
> First run the tests

For Python projects with pyproject.toml:
> Run "uv run pytest"

These four-word prompts:
1. Tell the agent there's a test suite and force it to figure out how to run tests
2. Give a rough indication of project size/complexity via test count
3. Put the agent in a testing mindset

Like "Use red/green TDD," this encapsulates established software engineering discipline in a short prompt.

### 3.3 Agentic manual testing

The defining characteristic of a coding agent is code execution. More valuable than LLMs that only generate code without verification.

**Key principle**: Never assume LLM-generated code works until it has been executed.

"Just because code passes tests doesn't mean it works as intended." Issues: server crashes, missing UI elements, details tests failed to cover. Manual testing remains essential.

**Mechanisms for agentic manual testing**:

**Python libraries**: `python -c "... code ..."` to pass Python code directly to the interpreter, including imports.

**Other languages**: agents write demo files in `/tmp` to test edge cases, compile, and run.

**Web APIs**: tell agents to exercise JSON APIs using `curl` and run a dev server. "explore" often prompts trying multiple aspects.

When manual testing reveals problems → fix using red/green TDD for permanent test coverage.

**Browser automation for web UIs**:
- **Playwright** — most powerful browser automation. Open-source Microsoft library, multi-language bindings, popular browser engines.
- **agent-browser** (Vercel) — CLI wrapper designed for coding agents.
- **Rodney** (Simon Willison's project) — uses Chrome DevTools Protocol to control Chrome.

Example prompt techniques:
- "use `uvx rodney --help`" to trigger installation via uvx
- Request agents "look at screenshots" to leverage vision abilities
- Tools offer JavaScript execution, scrolling, clicking, typing, accessibility tree reading

**Documentation with Showboat**: captures agentic manual testing flows.
- `note`: appends Markdown notes
- `exec`: records commands with output (discourages fabricating results)
- `image`: adds images like screenshots from Rodney

---

## Section 4: Understanding Code

### 4.1 Linear walkthroughs

Sometimes useful to have a coding agent give a structured walkthrough of a codebase — existing code to understand, forgotten details, or "vibe coded" code you didn't pay attention to.

**Example: Showboat and Present**. Simon "vibe coded a SwiftUI slide presentation app" on Mac using Claude Code and Opus 4.6. After release to GitHub, he didn't understand his own app.

He launched Claude Code for web, pointed at the repo, and prompted:
1. Read the source code
2. Plan a linear walkthrough explaining how everything works in detail
3. Run `uvx showboat --help` to learn the Showboat tool
4. Create a walkthrough.md file using Showboat

**About Showboat**: tool to help coding agents write documents demonstrating their work. `showboat note` adds Markdown content; `showboat exec` accepts shell commands, executes them, adds both command and output.

By instructing "use sed or grep or cat or whatever you need," Claude Code wouldn't manually copy code snippets, reducing hallucination risk.

**Results**: the document explained all six Swift files with clear actionable explanations. Willison learned substantially about SwiftUI architecture and Swift language details from reading it.

### 4.2 Interactive explanations

"When we lose track of how code written by our agents works we take on **cognitive debt**."

For simple code (fetch from DB → JSON), details may not matter. But if the core application becomes a black box, you can no longer confidently reason about it — planning new features becomes harder.

Pay down cognitive debt by improving understanding. One favorite way: building **interactive explanations**.

**Understanding word clouds**: From Max Woolf's "An AI agent coding skeptic tries AI agent coding, in excessive detail" — prompt "Create a Rust app that can create 'word cloud' data visualizations given a long input text".

Claude Code for web built a Rust CLI tool that produces word cloud images. The report mentioned "**Archimedean spiral placement** with per-word random angular offset for natural-looking layouts" — but this wasn't enough to understand.

Linear walkthrough helped with Rust structure but not the intuitive algorithm.

Requested an **animated explanation**: pasted walkthrough doc link into Claude Code:
> Build an animated-word-cloud.html page that accepts pasted text (persisted in the URL fragment), builds a word cloud using the algorithm with animation to make it clear to understand. Include a slider for animation control with pause, speed adjustment, and frame-by-frame stepping. The visible word cloud can be downloaded as PNG at any stage.

Using Claude Opus 4.6 — "quite good taste when it comes to building explanatory animations."

Watching the animation you can see that for each word it attempts to place it somewhere on the page by showing a box, checking if the box intersects existing words. If so, it continues moving outward in a spiral from the center.

The animation made the algorithm click.

---

## Section 5: Annotated Prompts

### 5.1 GIF optimization tool using WebAssembly and Gifsicle

Building a web-based GIF optimizer by prompting Claude Code to compile Gifsicle to WebAssembly.

**Initial prompt components**:
- Create `gif-optimizer.html`
- Compile Gifsicle to WASM
- Drag-and-drop GIF upload
- Display multiple compressed versions with file sizes and download buttons
- Manual controls to "tweak" settings from any preview

**Key prompt insights**:
- Filename alone signals intent within simonw/tools repo context
- Gifsicle by name leverages Claude's knowledge of this 30-year-old widely-used software
- WASM compilation involves Emscripten toolchain work
- "Coding agents are fantastic at trial and error! They can often brute force their way to a solution where I would have given up after the fifth inscrutable compiler error."
- Drag-and-drop pattern appears in existing tools
- Avoids overspecifying settings — trusts Claude's judgment on defaults

**Testing**: `uvx rodney --help` enabled browser testing. Claude identified and fixed CSS issues independently.

**Follow-up prompts**:
- Include build scripts and patches in lib/ subdirectory
- Clone Gifsicle to /tmp rather than committing full source
- Commit the WASM bundle (233KB) for GitHub Pages deployment
- Credit Gifsicle and link original repo

Resulting footer: "Built with gifsicle by Eddie Kohler, compiled to WebAssembly. gifsicle is released under the GNU General Public License, version 2."

---

## Section 6: Appendix — Prompts I use

### Artifacts

Simon uses Claude's Artifacts feature for prototyping HTML tools. Artifacts = regular Claude chat builds an HTML/JS app displayed in the chat. OpenAI and Gemini have "Canvas."

Models love React, but Simon prefers plain HTML so code can be copied to static hosting. Custom instructions:

> Never use React in artifacts - always plain HTML and vanilla JavaScript and CSS with minimal dependencies. CSS should be indented with two spaces and should start like this:
> ```
> <style>
> * { box-sizing: border-box; }
> ```
> Inputs and textareas should be font size 16px. Font should always prefer Helvetica. JavaScript should be two space indents and start like this:
> ```
> <script type="module">
> // code in here should not be indented at the first level
> ```
> Prefer Sentence case for headings.

### Proofreader

Simon doesn't let LLMs write text for his blog. Hard line: anything expressing opinions or using "I" needs to be written by him. But LLMs can proofread.

> You are a proofreader for posts about to be published.
> 1. Identify spelling mistakes and typos
> 2. Identify grammar mistakes
> 3. Watch out for repeated terms like "It was interesting that X, and it was interesting that Y"
> 4. Spot any logical errors or factual mistakes
> 5. Highlight weak arguments that could be strengthened
> 6. Make sure there are no empty or placeholder links

### Alt text

> You write alt text for any image pasted in by the user. Alt text is always presented in a fenced code block to make it easy to copy and paste out. It is always presented on a single line so it can be used easily in Markdown images. All text on the image (for screenshots etc) must be exactly included. A short note describing the nature of the image itself should go first.

Usually with Claude Opus — "extremely good taste in alt text." It makes editorial decisions like highlighting the most interesting numbers from a chart. Sometimes multiple images go to the same conversation so subsequent descriptions reference earlier context.

### Podcast highlights

After being a podcast guest, Simon publishes highlights from the transcript. Custom instructions:

> You will be given a transcript of a podcast episode. Find the most interesting quotes in that transcript - quotes that best illustrate the overall themes, and quotes that introduce surprising ideas or express things in a particularly clear or engaging or spicy way. Answer just with those quotes - long quotes are fine.
