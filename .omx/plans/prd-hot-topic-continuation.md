# PRD: hot-topic ingest continuation

## Goal
Continue ingest work by promoting high-value fetched source documents into standalone wiki pages, so the wiki improves beyond hub-style topic pages.

## Scope
- Create standalone summary/entity pages from fetched hot-topic sources that are currently only referenced indirectly
- Update index/log to register the new pages
- Keep all pages in Korean and follow CLAUDE.md typing/cross-reference rules

## Candidate pages for this pass
1. How we built our multi-agent research system
2. Effective harnesses for long-running agents
3. The 2026 MCP Roadmap
4. What is the Model Context Protocol (MCP)?
5. Context engineering for AI agents in open-source software
6. Agent Skills Specification

## Acceptance criteria
- At least 5 new standalone wiki pages are created from fetched hot-topic sources
- Each new page has valid frontmatter with category/page_type/sources/created/updated
- index.md includes the new pages in the correct category/type section
- log.md records this continuation ingest pass
- Fresh verification shows broken wikilinks = 0 and index missing-page count = 0
