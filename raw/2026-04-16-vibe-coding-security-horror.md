# AI Vibe Coding Horror Story: Patient Management App Security Disaster

Source: https://www.tobru.ch/an-ai-vibe-coding-horror-story/
Fetched: 2026-04-16

## What Happened

A medical professional, inspired by a video about AI-powered software development, decided to build a custom patient management system using a coding agent rather than employ established solutions. The application was hastily created, deployed to the internet, and populated with all existing patient data.

## Security Vulnerabilities Found (within 30 minutes of testing)

- **Complete data exposure**: full read and write access to all patient data, unencrypted and completely exposed to the open internet
- **Client-side only authentication**: All access control logic resided in JavaScript, making data retrievable via basic commands
- **Zero database security**: Managed database service had "zero access control configured, no row-level security, nothing"
- **Unauthorized data transfers**: Voice recordings automatically sent "directly to external AI APIs" without consent

## Technical Architecture

The entire application consisted of "a single HTML file with all JavaScript, CSS, and structure written inline." Backend security was virtually nonexistent, relying entirely on frontend obfuscation rather than genuine protection mechanisms.

## Compliance Violations

Violated data protection laws (nDSG) and potentially professional confidentiality statutes, particularly by storing sensitive medical information on US servers without proper Data Processing Agreements.

## Lessons

The author emphasizes that responsible AI-assisted coding requires technical literacy: "I'm using AI coding agents as well, but I'm able to understand what's happening, can read the code." The stark warning concludes that indiscriminate "vibing away" with AI tools will not produce a secure future.
