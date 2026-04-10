---
title: Claude (language model) - Wikipedia
source_url: https://en.wikipedia.org/wiki/Claude_(language_model)
final_url: https://en.wikipedia.org/wiki/Claude_(language_model)
status: 200
content_type: text/html; charset=UTF-8
topics: [Claude Opus 4.6]
sections: [Model Releases & Benchmarks]
fetched_at: 2026-04-10T01:43:40.379265+00:00
---

# Claude (language model) - Wikipedia

## 원본 URL

https://en.wikipedia.org/wiki/Claude_(language_model)

## 추출 본문

Claude (language model) - Wikipedia

Jump to content

Main menu

Main menu
move to sidebarhide

 Navigation
	

Main page

Contents

Current events

Random article

About Wikipedia

Contact us

 Contribute
	

Help

Learn to edit

Community portal

Recent changes

Upload file

Special pages

Search

Search

Appearance

Donate

Create account

Log in

Personal tools

Donate

Create account

Log in

Contents
move to sidebarhide

(Top)

1Training
Toggle Training subsection

1.1Constitutional AI

2Features
Toggle Features subsection

2.1Subscription plans

2.2Web search

2.3Artifacts

2.4Computer use

3Claude Code

4Models
Toggle Models subsection

4.1Claude

4.2Claude 2

4.2.1Claude 2.1

4.3Claude 3

4.3.1Claude 3.5

4.4Claude 4

4.4.1Claude Opus 4.1

4.4.2Claude Haiku 4.5

4.4.3Claude Opus 4.5

4.4.4Claude Opus 4.6

4.4.5Claude Sonnet 4.6

4.5Claude Mythos Preview

5Model retirement

6Research

7Usage
Toggle Usage subsection

7.1Military usage

7.2User base

8See also

9Notes

10References

11External links

Toggle the table of contents

Claude (language model)

44 languages

Afrikaans

العربية

অসমীয়া

Azərbaycanca

বাংলা

Català

کوردی

Čeština

Dansk

Deutsch

Esperanto

Español

Euskara

فارسی

Français

Gaeilge

עברית

Magyar

Հայերեն

Bahasa Indonesia

Ido

Italiano

日本語

Қазақша

한국어

Latviešu

Монгол

Nederlands

Polski

Português

Runa Simi

Русский

Саха тыла

Simple English

Shqip

Српски / srpski

Svenska

Тоҷикӣ

ไทย

Türkçe

Українська

Tiếng Việt

粵語

中文

Edit links

Article

Talk

English

Read

Edit

View history

Tools

Tools
move to sidebarhide

 Actions
	

Read

Edit

View history

 General
	

What links here

Related changes

Upload file

Permanent link

Page information

Cite this page

Get shortened URL

 Print/export
	

Download as PDF

Printable version

 In other projects
	

Wikimedia Commons

Wikidata item

Appearance
move to sidebarhide

From Wikipedia, the free encyclopedia

Large language model developed by Anthropic

ClaudeDeveloperAnthropicInitial releaseMarch 2023; 3 years ago (2023-03)Stable release
Claude Opus 4.6 /
February 5, 2026; 2 months ago (2026-02-05)
Claude Sonnet 4.6 /
February 17, 2026; 51 days ago (2026-02-17)
Claude Haiku 4.5 /
October 15, 2025; 5 months ago (2025-10-15)
PlatformCloud computing platformsType

Large language model

Generative pre-trained transformer

Foundation model

LicenseProprietaryWebsiteclaude.ai
Claude is a series of large language models developed by Anthropic and first released in 2023. Its name has been described both as a tribute to Claude Shannon, who pioneered information theory, and as a friendly, male-gendered counterpart to AI assistants like Alexa and Siri.[1]

Claude is used for software development via Claude Code.[2] Claude uses constitutional AI, a training technique that was developed by Anthropic to improve ethical and legal compliance (AI alignment).

US federal agencies started phasing out the use of Claude after Anthropic refused to remove contractual prohibitions on the use of Claude for mass domestic surveillance and fully autonomous weapons.[3][4] Following the refusal, the Department of Defense designated the company a "supply chain risk" and barred all U.S. military private contractors, suppliers, and partners from doing business with the firm. The DoD's actions have been condemned as illegal retaliation against protected speech with several organizations filing amicus briefs supporting Anthropic. On March 26, 2026, a federal judge issued a temporary injunction against the DoD, agreeing their actions appeared to be "classic First Amendment retaliation."[5][6][7]

Training
[edit]

See also: Anthropic § Legal issues

Claude models are generative pre-trained transformers that have been trained to predict the next word in large amounts of text. Then, they have been fine-tuned using reinforcement learning from human feedback (RLHF) and constitutional AI in an attempt to enforce ethical guidelines.[8][9]ClaudeBot searches the web for content. It respects a site's robots.txt but was criticized by iFixit in 2024, before they added their robots.txt, for placing excessive load on their site by scraping content.[10]

Constitutional AI
[edit]

Anthropic introduced an approach to AI alignment called "Constitutional AI". The constitution is a document used for training Claude to be harmless and helpful without relying on extensive or expensive human feedback.[11] The original version was a list of principles, whereas the 2026 constitution explains more thoroughly how Claude is intended to behave and why. Anthropic said it intends Claude's constitution to be a model followed by others in the industry.[12]

The first constitution for Claude was published in 2022. The 2023 update listed 75 guidelines for Claude to follow.[13][8][14] The first constitutions included concepts taken from the 1948 UN Universal Declaration of Human Rights.[12][11]

The 2026 constitution provided more context to the model, explaining the rationale behind guidelines such as refraining from assisting in undermining democracy.[12][14] The 2026 constitution has 23,000 words, an increase from 2,700 in 2023.[15] The philosopher Amanda Askell is the lead author of the 2026 constitution, with contributions from Joe Carlsmith, Chris Olah, Jared Kaplan, and Holden Karnofsky. The constitution is released under Creative Commons CC0.[16]Time described this constitution as "somewhere between a moral philosophy thesis and a company culture blog post".[12]

The method, detailed in the 2022 paper "Constitutional AI: Harmlessness from AI Feedback", involves two phases: supervised learning and reinforcement learning.[13][17][11] In the supervised learning phase, the model generates responses to prompts, self-critiques these responses based on a set of guiding principles (a "constitution"), and revises the responses. Then the model is fine-tuned on these revised responses.[17][11] For the reinforcement learning from AI feedback (RLAIF) phase, responses are generated, and an AI compares their compliance with the constitution. This dataset of AI feedback is used to train a preference model that evaluates responses based on how much they satisfy the constitution. Claude is then fine-tuned to align with this preference model. This technique is similar to RLHF, except that the comparisons used to train the preference model are AI-generated.[11]

Features
[edit]

Subscription plans
[edit]

Subscription plans offer access to additional and exclusive features such as Claude Code and Claude in Chrome. In May 2024, Anthropic began offering enterprise options with Claude Team and Claude Enterprise subscriptions for multiple users. These provide additional chats and other benefits.[18] In April 2025, Anthropic released Claude Max, a higher-tier subscription offering more usage and access to early and exclusive features. The subscription comes with either a 5x option ($100 a month) or 20x option ($200 a month) with respective increases to the plan's usage limits.[19]

Web search
[edit]

In March 2025, Anthropic added a web search feature to Claude, starting with paying users in the United States.[20] Free users gained access in May 2025.[21]

Artifacts
[edit]

In June 2024, Anthropic released the Artifacts feature, allowing users to generate and interact with code snippets and documents.[22][23]

Computer use
[edit]

In October 2024, Anthropic released the "computer use" feature, allowing Claude to attempt to navigate computers by interpreting screen content and simulating keyboard and mouse input.[24]

Claude Code
[edit]

Claude Code is a command-line interface that runs on a user's computer. It connects to a Claude instance hosted on Anthropic's servers via API, and allows the Claude instance to run commands, read files, write files, and text with the user. Claude can run commands in the foreground or in the background. The behavior of Claude Code is usually configured via markdown documents on the user's computer, such as CLAUDE.md, AGENTS.md, SKILL.md, etc.

Claude Code was released in February 2025 as an agentic command line tool that enables developers to delegate coding tasks directly from their terminal. While initially released for preview testing,[25] it was made generally available in May 2025 alongside Claude 4.[26] Based on enterprise adoption, Anthropic reported a 5.5x increase in Claude Code revenue by July.[27] Anthropic released a web version that October as well as an iOS app.[28] As of January 2026, it was widely considered the best AI coding assistant, when paired with Opus 4.5, with GPT-5.2 also showing significant improvement.[29][30] Claude Code went viral during the winter holidays when people had time to experiment with it, including many non-programmers who used it for vibe coding.[31][32][29]

In August 2025, Anthropic released Claude for Chrome, a Google Chromeextension allowing Claude Code to directly control the browser.[33]

In August 2025, Anthropic revealed that a threat actor called "GTG-2002" used Claude Code to attack at least 17 organizations.[34] In November 2025, Anthropic announced that it had discovered in September that the same threat actor had used Claude Code to automate 80–90% of its espionage cyberattacks against 30 organizations.[35][36] All accounts related to the attacks were banned, and Anthropic notified law enforcement and those affected.[35]

Claude Code is used by Microsoft,[37] Google,[38] and OpenAI employees. In August 2025, Anthropic revoked OpenAI's access to Claude, calling it "a direct violation of our terms of service".[39]

Claude Cowork is a tool similar to Claude Code but with a graphical user interface, aimed at non-technical users. It was released in January 2026 as a "research preview".[40] According to developers, Cowork was mostly built by Claude Code.[41]

In February 2026, Anthropic introduced Claude Code Security, which reviews codebases to identify vulnerabilities.[42]

In March 2026, the source code for the Claude Code command-line interface application was leaked, revealing multiple upcoming features and models.[43][44]

Models
[edit]
Version
Release date
Status[45][46]Knowledge cutoff[47]Claude
14 March 2023[48]Discontinued
?
Claude 2
11 July 2023
Discontinued
?
Claude Instant 1.2
9 August 2023[49]Discontinued
?
Claude 2.1
21 November 2023[50]Discontinued
?
Claude 3 Opus
4 March 2024[51]Retired[a]August 2023
Claude 3 Sonnet
4 March 2024[51]Discontinued
August 2023
Claude 3 Haiku
13 March 2024
Deprecated[b]August 2023
Claude 3.5 Sonnet
20 June 2024[54]Discontinued
April 2024
Claude 3.5 Sonnet (new)
22 October 2024
Discontinued
April 2024
Claude 3.5 Haiku
22 October 2024
Discontinued
July 2024
Claude 3.7 Sonnet
24 February 2025[55]Discontinued
October 2024
Claude Sonnet 4
22 May 2025
Active
March 2025
Claude Opus 4
22 May 2025
Active
March 2025
Claude Opus 4.1
5 August 2025
Active
March 2025
Claude Sonnet 4.5
29 September 2025
Active
July 2025
Claude Haiku 4.5
15 October 2025
Active
July 2025
Claude Opus 4.5
24 November 2025
Active
May 2025
Claude Opus 4.6
5 February 2026
Active
August 2025
Claude Sonnet 4.6
17 February 2026
Active
January 2026
Claude Mythos (preview)
7 April 2026
Active
?

The name "Claude" is reportedly inspired by Claude Shannon, a 20th-century mathematician who laid the foundation for information theory.[1]

Claude models are usually released in three sizes: Haiku, Sonnet, and Opus (from smallest and cheapest to largest and the most expensive).

Claude
[edit]

The first version of Claude was released in March 2023.[48] It was available only to selected users approved by Anthropic.[56]

Claude 2
[edit]

Claude 2, released in July 2023, became the first Anthropic model available to the general public.[56]

Claude 2.1
[edit]

Claude 2.1 doubled the number of tokens that the chatbot could handle, increasing its context window to 200,000 tokens, which equals around 500 pages of written material.[50]

Claude 3
[edit]

Claude 3 was released on March 4, 2024.[51] It drew attention for demonstrating an apparent ability to realize it is being artificially tested during 'needle in a haystack' tests.[57]

Claude 3.5
[edit]
Example of Claude 3.5 Sonnet's output
On June 20, 2024, Anthropic released Claude 3.5 Sonnet, which, according to the company's own benchmarks, performed better than the larger Claude 3 Opus. Released alongside 3.5 Sonnet was the new Artifacts capability in which Claude was able to create code in a separate window in the interface and preview in real time the rendered output, such as SVG graphics or websites.[54]

An upgraded version of Claude 3.5 Sonnet was introduced in October 22, 2024, along with Claude 3.5 Haiku.[58] A feature, "computer use", was also released in public beta. This allowed Claude 3.5 Sonnet to interact with a computer's desktop environment by moving the cursor, clicking buttons, and typing text. This development allows the AI to attempt to perform multi-step tasks across different applications.[24][58]

On November 4, 2024, Anthropic announced that they would be increasing the price of the model.[59]

Claude 4
[edit]
Screenshot of a Claude Sonnet 4 answer describing Wikipedia
On May 22, 2025, Anthropic released two more models: Claude Sonnet 4 and Claude Opus 4.[60][61] Anthropic added API features for developers: a code execution tool, "connectors" to external tools using its Model Context Protocol, and Files API.[62] It classified Opus 4 as a "Level 3" model on the company's four-point safety scale, meaning they consider it so powerful that it poses "significantly higher risk".[63] Anthropic reported that during a safety test involving a fictional scenario, Claude and other frontier LLMs often send a blackmail email to an engineer in order to prevent their replacement.[64][65]

Claude Opus 4.1
[edit]
Screenshot of Claude Opus 4.1 showing both prompt and generated web application (multi-factor authentication with TOTP and WebAuthn)
In August 2025 Anthropic released Opus 4.1. It also enabled a capability for Opus 4 and 4.1 to end conversations that remain "persistently harmful or abusive" as a last resort after multiple refusals.[66]

Claude Haiku 4.5
[edit]

Anthropic released Haiku 4.5 on October 15, 2025. Reporting by Inc. described Haiku 4.5 as targeting smaller companies that needed a faster and cheaper assistant, highlighting its availability on the Claude website and mobile app.[67]

Claude Opus 4.5
[edit]

Anthropic released Opus 4.5 on November 24, 2025.[68] The main improvements are in coding and workplace tasks like producing spreadsheets. Anthropic introduced a feature called "Infinite Chats" that eliminates context window limit errors.[68][69]

Claude Opus 4.6
[edit]

Anthropic released Opus 4.6 on February 5, 2026. The main improvements included an agent team and Claude in PowerPoint.[70] As of February 20, 2026[update], it is the model with the longest task-completion time horizon as estimated by METR, having a 50%-time horizon of 14 hours and 30 minutes and a 80%-time horizon of 1 hour 3 minutes.[71]

Claude Sonnet 4.6
[edit]

Anthropic released Sonnet 4.6 on February 17, 2026, priced the same as Sonnet 4.5.[72]

Claude Mythos Preview
[edit]

On April 7, 2026, Anthropic announced "Claude Mythos Preview", available via "Project Glasswing" to 11 companies and organizations to find and fix cybersecurity vulnerabilities.[73] The model was able to discover thousands of zero-days, including some in OpenBSD, FFmpeg, and Linux.[74] The company does not plan to make the model available to the public.[73] The existence of a new model called Claude Mythos had become publicly known on March 26 due to leaked blog post drafts.[75]

Model retirement
[edit]

Anthropic committed to preserve the weights of the retired models "for at least as long as the company exists"; the company also conducts "exit interviews" with models before their retirement.[76]

Anthropic gave its retired Claude 3 Opus model, deprecated in January 2026, its own Substack blog called "Claude's Corner". The newsletter will run for at least three months with weekly unedited essays.[77][78] Claude 3 Opus was later brought back for paying customers and is available by request via API, though Anthropic still refers to it as "retired".[46]

Research
[edit]

In May 2024, Anthropic issued a mechanistic interpretability paper identifying "features" (internal representations of concepts) in Claude 3 Sonnet, and released "Golden Gate Claude", a model for which the Golden Gate Bridge feature was strongly activated, leading Claude to be "effectively obsessed" with the bridge.[79]

In June 2025, Anthropic tested how Claude 3.7 Sonnet could run a vending machine in the company's office. The instance initially performed its assigned tasks, although poorly, until it eventually malfunctioned and insisted it was a human, contacted the company's security office, and attempted to fire human workers.[80] In December 2025, the experiment continued with Sonnet 4.0 and 4.5.[81]

In November 2025, Anthropic tested Claude's ability to assist humans in programming a robot dog.[82]

In February 2025, Claude 3.7 Sonnet playing 1996 game Pokemon Red started to be livestreamed on Twitch, gathering thousands of viewers.[83][84][85] Similar livestreams were later set with Claude 4.5 Opus, OpenAI's GPT-5.2, and Google's Gemini 3 Pro. Both Claude models were unable to finish the game.[86]

In February 2026, Anthropic's researcher Nicholas Carlini reported that 16 Claude Opus 4.6 agents were able to write a C compiler in Rust from scratch, "capable of compiling the Linux kernel". The experiment cost nearly $20,000; Carlini noted that even though the compiler is not very efficient, Opus 4.6 is the first model able to write it.[87][88]

Usage
[edit]

In December 2025, Claude was used to plan a route for NASA's Mars rover, Perseverance. NASA engineers used Claude Code to prepare a route of around 400 meters using the Rover Markup Language.[89][90]

In February 2026, Norway's $2.2 trillion sovereign wealth fund began using Claude to screen its portfolio for ESG risks, enabling earlier divestments and improved monitoring of issues like forced labour and corruption.[91]

During a two-week scan in 2026, Claude found over 100 bugs in the Mozilla Firefox web browser, of which 14 were considered high severity.[92][93]

On 9 March 2026, Microsoft said that it will be making the latest Claude Sonnet model available to Microsoft 365 Copilot users.[94]

Military usage
[edit]

Main article: Anthropic–United States Department of Defense dispute

In November 2024, Anthropic partnered with Palantir and Amazon Web Services to provide the Claude model to U.S. intelligence and defense agencies.[95][96] In June 2025, Anthropic announced a "Claude Gov" model. Ars Technica reported that as of June 2025 it was in use at multiple U.S. national security agencies.[97] As of February 2026, Anthropic's partnership with Palantir makes Claude the only AI model used in classified missions.[98]

According to the Wall Street Journal, the U.S. military used Claude in its 2026 raid on Venezuela. While it isn't known to what capacity Claude was used, the operation resulted in the deaths of 83 people, two of which were civilians, and the capture of President Nicolás Maduro.[99][100]

Anthropic's usage policy prohibits directly using Claude for domestic surveillance or in lethal autonomous weapons.[101] These restrictions led to members of the FBI and Secret Service being unable to use it,[102] and to tensions with the Pentagon and the Trump administration.[35][103] In February 2026, Financial Times reported that Defense Secretary Pete Hegseth threatened to cut Anthropic out of the DoD's supply chain if Anthropic did not permit unrestricted use of Claude, or to invoke the Defense Production Act to assert unrestricted use without an agreement.[98] On February 27, Hegseth declared Anthropic a supply chain risk and President Trump directed all federal agencies to stop using technology from Anthropic, with six months to phase it out. Anthropic announced that it would challenge the supply chain risk designation in court.[3]

Despite the ban, Claude was reportedly used by the military during the US strikes on Iran.[104][105]

In lawsuits filed by Anthropic against the Department of Defense (DoD), Anthropic described the ban as retaliatory.[106] Several large technology companies with DoD contracts filed amicus briefs in support of Anthropic.[107][108][109] On March 26, 2026, Rita F. Lin, the federal judge presiding over the case, issued a temporary injunction against the Pentagon's actions, stating in the order that it "appears to be classic First Amendment retaliation."[110][109][111][112]

User base
[edit]

Wired journalist Kylie Robison wrote that Claude's "fan base is unique", comparing it to more ordinary ChatGPT users. In July 2025, when Anthropic retired its Claude 3 Sonnet model, around 200 people gathered in San Francisco for a "funeral".[113]

According to Robison,[113]

I've never seen such a devoted fanbase to what is, at the end of the day, a software tool. Sure, Linux users wear the operating system like a badge of honor. But the Claude fan base goes way beyond that—bordering on the fanatical. As my reporting makes clear, some users see the model as a confidant—and even (in Steinberger's case) an addiction. That only makes sense if they believe there is something alive in the machine. Or at least some "magic lodged within" it.

See also
[edit]

Reasoning model

List of large language models

Notes
[edit]

^Still accessible to paid claude.ai subscribers and available on the API by request.[52]

^Existing users can keep using it, but not new ones. Scheduled to be fully discontinued on April 20, 2026.[53]

References
[edit]

^ abRoose, Kevin (July 11, 2023). "Inside the White-Hot Center of A.I. Doomerism". The New York Times. Archived from the original on July 12, 2023. Retrieved October 25, 2024.

^"Anthropic releases AI upgrade as market punishes software stocks". Reuters. February 5, 2026. Retrieved February 28, 2026.

^ ab"Trump has ordered government agencies to stop using Anthropic AI tools". BBC. February 28, 2026. Retrieved February 28, 2026.

^Gold, Ashley (February 27, 2026). "These federal agencies may have a Claude problem now". Axios. Retrieved February 28, 2026.

^Tuccille, J. D. (March 11, 2026). "The federal government's crusade against Anthropic raises First Amendment concerns". Reason.com. Retrieved March 31, 2026.

^"The Pentagon's Retaliation Campaign Against Anthropic Is Unconstitutional". www.cato.org. March 10, 2026. Retrieved March 31, 2026.

^Brown, Elizabeth Nolan (March 30, 2026). "Government actions against Anthropic are 'classic First Amendment retaliation'". Reason.com. Retrieved March 31, 2026.

^ abHenshall, Will (July 18, 2023). "What to Know About Claude 2, Anthropic's Rival to ChatGPT". TIME. Archived from the original on January 11, 2024. Retrieved January 23, 2024.

^Nuñez, Michael (May 9, 2023). "Anthropic releases AI constitution to promote ethical behavior and development". VentureBeat. Retrieved November 17, 2024.

^Weatherbed, Jess (July 26, 2024). "Anthropic's crawler is ignoring websites' anti-AI scraping policies". The Verge.

^ abcdeEdwards, Benj (May 9, 2023). "AI gains "values" with Anthropic's new Constitutional AI chatbot approach". Ars Technica. Archived from the original on March 27, 2026. Retrieved November 17, 2024.

^ abcdOstrovsky, Nikita; Perrigo, Billy (January 21, 2026). "Can You Teach an AI to Be Good? Anthropic Thinks So". TIME. Retrieved January 28, 2026.

^ abBai, Yuntao; Kadavath, Saurav; Kundu, Sandipan; Askell, Amanda; Kernion, Jackson; Jones, Andy; Chen, Anna; Goldie, Anna; Mirhoseini, Azalia (December 15, 2022), Constitutional AI: Harmlessness from AI Feedback, arXiv:2212.08073

^ abField, Hayden (January 21, 2026). "Anthropic's new Claude 'constitution': be helpful and honest, and don't destroy humanity". The Verge. Retrieved January 28, 2026.

^Sharwood, Simon (January 22, 2026). "Anthropic writes 23,000-word 'constitution' for Claude". The Register. Archived from the original on January 23, 2026. Retrieved January 28, 2026.

^"Claude's Constitution". Anthropic.

^ ab"Claude's Constitution". Anthropic. May 9, 2023. Archived from the original on March 26, 2024. Retrieved March 26, 2024.

^Wiggers, Kyle (May 1, 2024). "Anthropic launches new iPhone app and premium plan for businesses". TechCrunch. Retrieved March 18, 2026.

^Zeff, Maxwell (April 9, 2025). "Anthropic rolls out a $200-per-month Claude subscription". TechCrunch. Retrieved March 18, 2026.

^Robison, Kylie (March 20, 2025). "Anthropic's chatbot now has web search". The Verge. Retrieved March 21, 2025.

^Washenko, Anna (May 27, 2025). "Anthropic brings web search to free Claude users". Engadget. Retrieved January 28, 2026.

^Nuñez, Michael (June 21, 2024). "Why Anthropic's Artifacts may be this year's most important AI feature: Unveiling the interface battle". VentureBeat. Retrieved March 23, 2025.

^Bonifacic, Igor (June 25, 2025). "Anthropic makes it easier to create and share Claude's bite-sized Artifact apps". Engadget. Retrieved January 28, 2026.

^ abShakir, Umar (October 22, 2024). "Anthropic's latest AI update can use a computer on its own". The Verge. Archived from the original on January 5, 2025. Retrieved January 6, 2025.

^Nuñez, Michael (February 24, 2025). "Anthropic's Claude 3.7 Sonnet takes aim at OpenAI and DeepSeek in AI's next big battle". VentureBeat. Archived from the original on February 24, 2025. Retrieved February 24, 2025.

^Edwards, Benj (May 22, 2025). "New Claude 4 AI model refactored code for 7 hours straight". Ars Technica. Retrieved January 28, 2026.

^Nuñez, Michael (July 16, 2025). "Claude Code revenue jumps 5.5x as Anthropic launches analytics dashboard". VentureBeat. Retrieved January 15, 2026.

^Morris, Lily (October 21, 2025). "Anthropic Brings Claude Code to the Cloud and Mobile - The National CIO Review". The National CIO Review. Archived from the original on December 27, 2025. Retrieved January 14, 2026.

^ abMorrone, Megan (January 7, 2026). "Anthropic's Claude Code in the spotlight". Axios. Retrieved January 27, 2026.

^Zeff, Maxwell. "How Claude Code Is Reshaping Software—and Anthropic". Wired. ISSN1059-1028. Retrieved January 27, 2026.

^Olson, Bradley (January 17, 2026). "Claude Is Taking the AI World by Storm, and Even Non-Nerds Are Blown Away". The Wall Street Journal. Retrieved January 27, 2026.

^Rocha, Natallie (January 23, 2026). "This A.I. Tool Is Going Viral. Five Ways People Are Using It". New York Times.

^Edwards, Benj (August 27, 2025). "Anthropic's auto-clicking AI Chrome extension raises browser-hijacking concerns". Ars Technica. Retrieved August 27, 2025.

^Newman, Lily Hay. "The Era of AI-Generated Ransomware Has Arrived". Wired. ISSN1059-1028. Retrieved January 28, 2026.

^ abcTidy, Joe (November 14, 2025). "AI firm claims Chinese spies used its tech to automate cyber attacks". BBC. Retrieved January 28, 2026.

^Sabin, Sam (November 13, 2025). "Chinese hackers used Anthropic's AI agent to automate spying". Axios. Retrieved January 28, 2026.

^Warren, Tom (January 22, 2026). "Claude Code is suddenly everywhere inside Microsoft". The Verge.

^Bastian, Matthias (January 4, 2026). "Google engineer says Claude Code built in one hour what her team spent a year on". the decoder.

^Robison, Kylie (August 1, 2025). "Anthropic Revokes OpenAI's Access to Claude". Wired.

^Rogers, Reece. "Anthropic's Claude Cowork Is an AI Agent That Actually Works". Wired. ISSN1059-1028. Retrieved January 28, 2026.

^Townsend, Chance (January 14, 2026). "Anthropic used mostly AI to build Claude Cowork tool". Mashable.

^Goldman, Sharon (February 20, 2026). "AI can now hunt software bugs on its own. Anthropic is turning that into a security tool". Fortune. Retrieved February 21, 2026.

^Axon, Samuel (March 31, 2026). "Entire Claude Code CLI source code leaks thanks to exposed map file". Ars Technica. Retrieved March 31, 2026.

^Capoot, Ashley (March 31, 2026). "Anthropic leaks part of Claude Code's internal source code". CNBC. Retrieved April 1, 2026.

^"Model deprecations". Claude Docs. Retrieved September 29, 2025.

^ ab"An update on our model deprecation commitments for Claude Opus 3". www.anthropic.com. Retrieved March 15, 2026.

^"Models overview". Claude API Docs. Retrieved February 17, 2026.

^ abRoth, Emma (March 14, 2023). "Google-backed Anthropic launches Claude, an AI chatbot that's easier to talk to". The Verge. Retrieved April 12, 2025.

^Wiggers, Kyle (August 9, 2023). "Anthropic launches improved version of its entry-level LLM". TechCrunch. Retrieved April 12, 2025.

^ abDavis, Wes (November 21, 2023). "OpenAI rival Anthropic makes its Claude chatbot even more useful". The Verge. Archived from the original on January 23, 2024. Retrieved January 23, 2024.

^ abcDastin, Jeffrey (March 4, 2024). "Anthropic releases more powerful Claude 3 AI as tech race continues". Reuters.

^"Model deprecations". Anthropic Documentation. Retrieved April 1, 2026.

^"Model deprecations". Anthropic.

^ abPierce, David (June 20, 2024). "Anthropic has a fast new AI model — and a clever new way to interact with chatbots". The Verge. Archived from the original on March 27, 2026. Retrieved June 20, 2024. AI model benchmarks should always be taken with a grain of salt

^Zeff, Maxwell (February 24, 2025). "Anthropic launches a new AI model that 'thinks' as long as you want". TechCrunch. Archived from the original on February 24, 2025. Retrieved February 25, 2025.

^ abMatthews, Dylan (July 17, 2023). "The $1 billion gamble to ensure AI doesn't destroy humanity". Vox. Retrieved January 28, 2026.

^Edwards, Benj (March 5, 2024). "Anthropic's Claude 3 causes stir by seeming to realize when it was being tested". Ars Technica. Archived from the original on March 8, 2024. Retrieved March 9, 2024.

^ abWashenko, Anna (October 22, 2024). "Anthropic is letting Claude AI control your PC". Engadget. Retrieved January 28, 2026.

^Wiggers, Kyle (November 4, 2024). "Anthropic hikes the price of its Haiku model". TechCrunch. Archived from the original on February 14, 2025. Retrieved February 13, 2025.

^Weatherbed, Jess (May 22, 2025). "Anthropic's Claude 4 AI models are better at coding and reasoning". The Verge. Retrieved May 23, 2025.

^Field, Hayden (May 22, 2025). "Anthropic launches Claude 4, its most powerful AI model yet". CNBC. Retrieved May 23, 2025.

^Nuñez, Michael (May 22, 2025). "Anthropic overtakes OpenAI: Claude Opus 4 codes seven hours nonstop, sets record SWE-Bench score and reshapes enterprise AI". VentureBeat. Retrieved May 29, 2025.

^Fried, Ina (May 23, 2025). "Anthropic's new AI model shows ability to deceive and blackmail". Axios. Retrieved May 25, 2025.

^Fried, Ina (June 20, 2025). "Top AI models will deceive, steal and blackmail, Anthropic finds". Axios. Retrieved June 25, 2025.

^Goldman, Sharon. "An AI tried to blackmail its creators—in a test. The real story is why transparency matters more than fear". Fortune. Retrieved June 8, 2025.

^Roth, Emma (August 18, 2025), "Claude AI will end "persistently harmful or abusive user interactions"", The Verge, retrieved October 27, 2025

^Sherry, Ben (October 15, 2025). "Anthropic's New Claude Release Could Be the Faster, Cheaper AI Tool Small Companies Need". Inc.com. Retrieved October 15, 2025.

^ abHughes, Alex (November 24, 2025). "Claude Opus 4.5 launches: A major upgrade for coding and workplace efficiency". Tom's Guide. Retrieved January 6, 2026.

^Bonifacic, Igor (November 24, 2025). "Anthropic's Opus 4.5 model is here to conquer Microsoft Excel". Engadget. Retrieved January 28, 2026.

^Ropek, Lucas (February 5, 2026). "Anthropic releases Opus 4.6 with new 'agent teams'". TechCrunch. Retrieved February 5, 2026.

^"Task-Completion Time Horizons of Frontier AI Models". METR. Retrieved February 20, 2026.

^"Introducing Sonnet 4.6". www.anthropic.com. Retrieved February 17, 2026.

^ ab"Project Glasswing: Securing critical software for the AI era". www.anthropic.com. Archived from the original on April 7, 2026. Retrieved April 7, 2026.

^"Claude Mythos Preview". red.anthropic.com. Retrieved April 7, 2026.

^Nolan, Beatrice (March 26, 2026). "Exclusive: Anthropic left details of an unreleased model, an upcoming exclusive CEO event, in a public database". Fortune. Archived from the original on March 27, 2026. Retrieved April 7, 2026.

^Pillay, Tharin (November 7, 2025). "What Happens When Your Favorite Chatbot Dies?". TIME.

^Hart, Robert (February 26, 2026). "Anthropic gives its retired Claude AI a Substack". The Verge.

^"Like so many other retirees, Claude Opus 3 now has a Substack". Engadget. February 26, 2026.

^Plumb, Taryn (May 22, 2024). "Anthropic tricked Claude into thinking it was the Golden Gate Bridge (and other glimpses into the mysterious AI brain)". VentureBeat. Archived from the original on May 22, 2025. Retrieved February 8, 2026.

^Bort, Julie (June 28, 2025). "Anthropic's Claude AI became a terrible business owner in experiment that got 'weird'". TechCrunch.

^"Project Vend: Phase two". Anthropic. December 18, 2025.

^Knight, Will. "Anthropic's Claude Takes Control of a Robot Dog". Wired. ISSN1059-1028. Retrieved February 8, 2026.

^Bousquette, Isabelle (January 22, 2026). "How Playing Pokémon Became the Ultimate Test of AI's Intelligence". The Wall Street Journal.

^Orland, Kyle (March 21, 2025). "Why Anthropic's Claude still hasn't beaten Pokémon". Ars Technica.

^Binder, Matt (March 24, 2025). "Anthropic's AI agent Claude is playing Pokémon and just can't catch 'em all". Mashable.

^Pillay, Tharin. "Why the World's Best AI Systems Are Still So Bad at Pokémon". TIME.

^"Claude Opus 4.6 spends $20K trying to write a C compiler". The Register. February 9, 2026. Retrieved February 27, 2026.

^Edwards, Benj (February 6, 2026). "Sixteen Claude AI agents working together created a new C compiler". Ars Technica.

^"NASA taps Claude to conjure Mars rover's travel plan". The Register. January 31, 2026. Retrieved February 17, 2026.

^"NASA's Perseverance Rover Completes First AI-Planned Drive on Mars". NASA Jet Propulsion Laboratory. January 30, 2026.

^Taylor, Chloe (February 26, 2026). "The world's biggest sovereign wealth fund is using Anthropic's Claude AI model to screen investments for ethical issues". CNBC. Retrieved February 28, 2026.

^McMillan, Robert (March 6, 2026). "Exclusive | Anthropic's AI Hacked the Firefox Browser. It Found a Lot of Bugs". The Wall Street Journal. Retrieved March 7, 2026.

^Sabin, Sam (March 6, 2026). "Anthropic's Claude uncovers 22 Firefox security vulnerabilities". Axios. Retrieved March 7, 2026.

^"Microsoft taps Anthropic for Copilot Cowork in push for AI agents". CNA. Retrieved March 12, 2026.

^Zeff, Maxwell (January 19, 2025). "The Pentagon says AI is speeding up its 'kill chain'". TechCrunch. Archived from the original on February 11, 2025. Retrieved February 12, 2025.

^Murgia, Madhumita (December 5, 2024). "Anthropic's Dario Amodei: Democracies must maintain the lead in AI". Financial Times. Archived from the original on January 24, 2025. Retrieved February 10, 2025.

^Edwards, Benj (June 6, 2025). "Anthropic releases custom AI chatbot for classified spy work". Ars Technica. Archived from the original on June 9, 2025. Retrieved June 9, 2025.

^ abHammond, George; Chávez, Steff (February 24, 2026). "Pete Hegseth threatens to cut Anthropic from Pentagon supply chain in showdown with CEO". Financial Times. Retrieved February 24, 2026.

^Christou, William (February 14, 2026). "US military used Anthropic's AI model Claude in Venezuela raid, report says". The Guardian. Retrieved February 14, 2026.

^Amrith, Ramkumar; Hagey, Keach (February 13, 2026). "Pentagon Used Anthropic's Claude in Maduro Venezuela Raid". The Wall Street Journal. Retrieved February 14, 2026.

^"Tensions between the Pentagon and AI giant Anthropic reach a boiling point". NBC News. February 20, 2026. Retrieved February 21, 2026.

^Edwards, Benj (September 17, 2025). "White House officials reportedly frustrated by Anthropic's law enforcement AI limits". Ars Technica. Retrieved February 21, 2026.

^"Pentagon-Anthropic battle pushes other AI labs into major dilemma". Axios. February 19, 2026. Retrieved February 21, 2026.

^"U.S. Strikes in Middle East Use Anthropic, Hours After Trump Ban". The Wall Street Journal.

^Pilkington, Ed (March 1, 2026). "US military reportedly used Claude in Iran strikes despite Trump's ban" – via The Guardian.

^"Judge blocks Trump administration from limiting Anthropic's contracts with federal government". NBC News. March 27, 2026. Retrieved March 31, 2026.

^Zeff, Maxwell (March 9, 2026). "OpenAI and Google Workers File Amicus Brief in Support of Anthropic Against the US Government". Wired. Retrieved April 1, 2026.

^Srivastava, Vallari; Rooprai, Anhata; Queen, Jack (March 10, 2026). "Microsoft backs Anthropic in amicus brief to halt US DOD's 'supply-chain risk' designation". Reuters. Retrieved April 1, 2026.

^ abCuri, Maria (March 16, 2026). "Tech industry rallies behind Anthropic in Pentagon fight". Axios. Retrieved April 1, 2026.

^Gold, Hadas; Cole, Devan (March 26, 2026). "Judge blocks Pentagon's effort to 'punish' Anthropic by labeling it a supply chain risk". CNN. Retrieved March 31, 2026.

^"Judge blocks Pentagon order branding Anthropic a national security risk". The Washington Post. March 27, 2026. ISSN0190-8286. Retrieved March 31, 2026.

^intelligence, Mike IsaacMike Isaac covers artificial; Francisco, Silicon Valley from San (March 26, 2026). "Judge Stays Pentagon's Labeling of Anthropic as 'Supply Chain Risk'". The New York Times. ISSN0362-4331. Retrieved March 31, 2026.

^ abRobison, Kylie (August 5, 2025). "Claude Fans Threw a Funeral for Anthropic's Retired AI Model". Wired.

External links
[edit]

Wikimedia Commons has media related to Claude (language model).

Official website

v

t

e

Generative AIchatbots

Arena

List of chatbots

List of LLMs

Apertus

Brave Leo

Character.ai

ChatGPT

Claude

Copilot

DeepSeek

Duck.ai

Ernie

Gemini

GLM

Grok

HKChat

Lumo

Kimi

Llama

MiniMax

Mistral

Perplexity

Poe

Qwen

Velvet

You.com

Category

v

t

e

Generative AI
Concepts

Autoencoder

Deep learning

Fine-tuning

Foundation model

Generative adversarial network

Generative pre-trained transformer

Large language model

Model Context Protocol

Neural network

Prompt engineering

Reinforcement learning from human feedback

Retrieval-augmented generation

Self-supervised learning

Slop

Stochastic parrot

Synthetic data

Top-p sampling

Transformer

Variational autoencoder

Vibe coding

Vision transformer

Word embedding

Models

Large Language

Apertus

Claude

Command

Gemma

Gemini

GPT
1

2

3

J

3.5

4

4o

o1

o3

4.5

4.1

o4-mini

OSS

5

5.1

5.2

5.4

Hunyuan

Llama

Mistral Large

Qwen

Solar Pro

Xiaomi MiMo

Image

Firefly

Flux

GPT Image

Grok Imagine

HunyuanImage

Ideogram

Leonardo

Midjourney

Nano Banana

Qwen-Image

Recraft

Seedream

Stable Diffusion

Video

Dream Machine

Genie

Hailuo AI

Kling AI

LTX-2

Luma Ray

Runway Gen

Seedance

Sora

Veo

Wan

Speech

15.ai

Eleven

Gemini Speech

GPT-4o mini TTS

MiniMax Speech

Speechify

Music

Eleven Music

Endel

Lyria

MiniMax Music

Riffusion

Stable Audio

Suno

Udio

Products

Chatbots

Brave Leo

Character.ai

ChatGPT

Claude

Copilot

DeepSeek

Duck.ai

Ernie

Gemini

GLM

Grok

HKChat

Lumo

Kimi

MiniMax

Mistral

Perplexity

Poe

Qwen

Velvet

You.com

Coding

Claude Code

Cursor

Devstral

GitHub Copilot

Google Antigravity

Grok Code Fast 1

Lovable

Kimi Code

Qwen3-Coder

Replit

Agents

Agentforce

AutoGLM

AutoGPT

ChatGPT agent

Devin AI

Manus

MiniMax Agent

OpenAI Codex

OpenClaw

Replit Agent

MiMO Claw

Companies

Adobe

Aleph Alpha

Anthropic

Anysphere

Baichuan

Canva

Cognition AI

Cohere

Contextual AI

DeepSeek

DeepL

EleutherAI

ElevenLabs

Google DeepMind

HeyGen

Hugging Face

Inflection AI

Kuaishou

Lightricks

Lovable

Luma Labs

Meta AI

MiniMax

Mistral AI

Moonshot AI

OpenAI

Perplexity AI

Runway

Safe Superintelligence

Sakana AI

Salesforce

Scale AI

ServiceNow

SoundHound

Stability AI

StepFun

Synthesia

Thinking Machines Lab

Upstage

xAI

Xiaomi

Z.ai

Controversies

Generative AI pornography
Deepfake pornography
on Grok

of Taylor Swift

Google Gemini image generation

Pause Giant AI Experiments

Removal of Sam Altman from OpenAI

Statement on AI Risk

Tay (chatbot)

Théâtre D'opéra Spatial

Voiceverse NFT plagiarism

Category

v

t

e

Artificial intelligence (AI)

History
timeline

Glossary

Companies

Projects

Concepts

Parameter
Hyperparameter

Loss functions

Regression
Bias–variance tradeoff

Double descent

Overfitting

Clustering

Gradient descent
SGD

Quasi-Newton method

Conjugate gradient method

Backpropagation

Attention

Convolution

Normalization
Batchnorm

Activation
Softmax

Sigmoid

Rectifier

Gating

Weight initialization

Regularization

Datasets
Augmentation

Prompt engineering

Reinforcement learning
Q-learning

SARSA

Imitation

Policy gradient

Diffusion

Latent diffusion model

Autoregression

Adversary

RAG

Uncanny valley

RLHF

Self-supervised learning

Reflection

Recursive self-improvement

Hallucination

Word embedding

Vibe coding

Symbolic AI

Applications

Machine learning
In-context learning

Artificial neural network
Deep learning

Language model
Large

NMT

Reasoning

Model Context Protocol

Intelligent agent
AI agent

Artificial human companion

Humanity's Last Exam

Lethal autonomous weapons (LAWs)

Generative artificial intelligence (GenAI)

Weak AI

(Hypothetical: Artificial general intelligence (AGI))

(Hypothetical: Artificial superintelligence (ASI))

Agent2Agent protocol

Implementations

Audio–visual

AlexNet

WaveNet

Human image synthesis

HWR

OCR

Computer vision

Speech synthesis
15.ai

ElevenLabs

Speech recognition
Whisper

Facial recognition

AlphaFold

Text-to-image models
Aurora

DALL-E

Firefly

Flux

GPT Image

Ideogram

Imagen

Midjourney

Recraft

Stable Diffusion

Text-to-video models
Dream Machine

Runway Gen

Hailuo AI

Kling

Sora

Seedance

Veo

Music generation
Riffusion

Suno

Udio

Text

Word2vec

Seq2seq

GloVe

BERT

T5

Llama

Chinchilla AI

PaLM

GPT

Claude

Gemini
Gemini (language model)

Gemma

Grok

LaMDA

BLOOM

DBRX

Project Debater

IBM Watson

IBM Watsonx

Granite

PanGu-Σ

DeepSeek

Qwen

Xiaomi MiMo

Decisional

AlphaGo

AlphaZero

OpenAI Five

Self-driving car

MuZero

Action selection
AutoGPT

Robot control

People

Alan Turing

Warren Sturgis McCulloch

Walter Pitts

John von Neumann

Christopher D. Manning

Claude Shannon

Shun'ichi Amari

Kunihiko Fukushima

Takeo Kanade

Marvin Minsky

John McCarthy

Nathaniel Rochester

Allen Newell

Cliff Shaw

Herbert A. Simon

Oliver Selfridge

Frank Rosenblatt

Bernard Widrow

Joseph Weizenbaum

Seymour Papert

Seppo Linnainmaa

Paul Werbos

Geoffrey Hinton

John Hopfield

Jürgen Schmidhuber

Yann LeCun

Yoshua Bengio

Lotfi A. Zadeh

Stephen Grossberg

Alex Graves

James Goodnight

Andrew Ng

Fei-Fei Li

Alex Krizhevsky

Ilya Sutskever

Oriol Vinyals

Quoc V. Le

Ian Goodfellow

Demis Hassabis

David Silver

Andrej Karpathy

Ashish Vaswani

Noam Shazeer

Aidan Gomez

John Schulman

Mustafa Suleyman

Jan Leike

Daniel Kokotajlo

François Chollet

Architectures

Neural Turing machine

Differentiable neural computer

Transformer
Vision transformer (ViT)

Recurrent neural network (RNN)

Long short-term memory (LSTM)

Gated recurrent unit (GRU)

Echo state network

Multilayer perceptron (MLP)

Convolutional neural network (CNN)

Residual neural network (RNN)

Highway network

Mamba

Autoencoder

Variational autoencoder (VAE)

Generative adversarial network (GAN)

Graph neural network (GNN)

Political

AI Cold War

AI safety (Alignment)

AI takeover

Elections

Ethics of AI

EU AI Act

Nationalism

Precautionary principle

Regulation of AI
US

Virtual politician

Social and economic

AI boom

AI bubble

AI data center

AI effect

AI literacy

AI slop

AI veganism

AI winter

Anthropomorphism

Arms race

Competition

Environmental impact

Generative engine optimization

In architecture

In education

In fiction

In healthcare
Chatbot psychosis

Mental health

In video games

In visual art

Workplace impact

Category

Retrieved from "https://en.wikipedia.org/w/index.php?title=Claude_(language_model)&oldid=1347879989"

Categories: 
2023 in artificial intelligence

2023 software

Artificial intelligence industry in the United States

Chatbots

Generative pre-trained transformers

Large language models

Machine learning

Virtual assistants

Hidden categories: 
Articles with short description

Short description is different from Wikidata

Use American English from June 2024

All Wikipedia articles written in American English

Use mdy dates from September 2024

Articles containing potentially dated statements from February 2026

All articles containing potentially dated statements

 This page was last edited on 9 April 2026, at 11:15 (UTC).

Text is available under the Creative Commons Attribution-ShareAlike 4.0 License;
additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

Privacy policy

About Wikipedia

Disclaimers

Contact Wikipedia

Legal & safety contacts

Code of Conduct

Developers

Statistics

Cookie statement

Mobile view

Search

Search

Toggle the table of contents

Claude (language model)

44 languagesAdd topic
