---
name: idea-capture
description: "Capture raw ideas into Obsidian with minimal friction. Use when user says 'I have an idea', 'capture this', 'idea about', or wants to record a concept quickly. Capture only—no analysis or processing."
---

# Idea Capture

Preserve the spark before it fades. Speed over completeness.

## Required Skills

- `obsidian-markdown` — callouts, frontmatter, wikilinks

## Process

1. **Clarify problem** (only if unclear from input):
   - "What problem does this solve?"
   - "What would be different if this worked?"
   - Skip if answers are evident. Max 2 questions.

2. **Ask domain**: "Work or personal?" (infer if obvious from context)

3. **Find connections**: Scan vault for 2-5 related wikilinks in `Areas/`, `Projects/`, `Resources/`, `ideas/`.

4. **Create note** using template below.

5. **Preview → approve → write** to `ideas/{{Title}}.md`.

## Template

```markdown
---
type: idea
status: seed
domain: {{work | personal}}
rating:
outcome:
outcome_rating:
created: {{YYYY-MM-DD}}
tags:
  - idea
---

# {{Title in 3-7 Words}}

> [!abstract] The Problem
> {{problem statement}}

## The Idea

{{user's exact words—preserve original language}}

> [!success] If This Worked
> {{impact statement}}

## First Question

{{one thing to validate or explore}}

> [!tip] Connections
> - [[related note 1]]
> - [[related note 2]]
```

## Config

| Setting | Value |
|---------|-------|
| Vault | `/Users/saisoundararajan/Documents/thirdeye/` |
| Output | `ideas/` |

## Example

**Input**: "I have an idea about using AI to auto-tag support tickets"

**Output**: `ideas/AI Auto-Tag Support Tickets.md`

```markdown
---
type: idea
status: seed
domain: work
rating:
outcome:
outcome_rating:
created: 2025-01-11
tags:
  - idea
---

# AI Auto-Tag Support Tickets

> [!abstract] The Problem
> Manual tagging is slow and inconsistent, delaying triage.

## The Idea

Use AI to automatically categorize support tickets based on symptoms described in the ticket.

> [!success] If This Worked
> Faster triage, consistent categorization, reduced manual effort.

## First Question

What accuracy threshold would be acceptable for auto-tagging?

> [!tip] Connections
> - [[SRT Triage]]
> - [[AI Network Diagnostics]]
```
