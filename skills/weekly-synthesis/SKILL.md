---
name: weekly-synthesis
description: Generate weekly progress summary from daily notes. Use when user asks "weekly summary", "how is my week", "summarize my week", "weekly review", or "how did this week go".
allowed-tools: Read, Grep, Glob
---

# Weekly Synthesis Skill

## Vault Configuration
- **Vault Path**: `/Users/saisoundararajan/Documents/thirdeye/`
- **Daily Notes**: `/Users/saisoundararajan/Documents/thirdeye/reviews/daily/YYYY-MM-DD.md`
- **Weekly Reviews**: `/Users/saisoundararajan/Documents/thirdeye/reviews/weekly/Weekly Review YYYY-W{n}.md`

## Trigger Phrases
- "weekly summary"
- "how is my week"
- "summarize my week"
- "weekly review please"
- "how did this week go?"
- "how is my current week progressing"

## Workflow

### Step 1: Determine Current Week
1. Get today's date
2. Calculate ISO week number (W1-W52)
3. Determine week date range (Monday to Sunday)

### Step 2: Gather Data

**Weekly Review File**:
- Path: `/reviews/weekly/Weekly Review YYYY-W{n}.md`
- Extract goals from "Goals" section
- Parse todo states: `[x]` done, `[ ]` pending, `[/]` in progress

**Daily Notes**:
- Path: `/reviews/daily/YYYY-MM-DD.md` for each day in week
- Extract tagged entries:
  - `#progress` - improvements, wins
  - `#insight` - learnings, realizations
  - `#decision` - important choices
  - `#observation` - patterns noticed
  - `#blocker` - obstacles encountered
  - `#win` - achievements
- Note Log section content for each day
- Track which problem spaces got attention: `#clientsenv`, `#sir`, `#msk`, `#infrastructure`

### Step 3: Analyze

**Goal Analysis**:
- Count completed vs total goals
- Calculate completion percentage
- Identify "hidden wins" - work done but not in explicit goals (scan Log sections)

**Thematic Clustering**:
- Group work by problem space tags
- Identify major workstreams
- Find cross-workstream connections

**Momentum Mapping**:
- Which days had high activity (long Log sections)?
- Which days were quiet?
- Pattern detection (e.g., productive days vs meeting-heavy days)

**Surprise Mining**:
- Cross-reference different workstreams for unexpected connections
- Look for productivity patterns
- Identify emerging themes not yet formalized

### Step 4: Generate Output

**CRITICAL: Keep to ONE PAGE (20-25 lines). Be visual, scannable, concise.**

```markdown
# Week W{n} Summary ({Mon Date} - {Fri Date})

## Goals: {X}/{Y} ({percentage}%)
{visual progress bar using block characters}

Done: {Goal 1}, {Goal 2}
Missed: {Goal 3}, {Goal 4}
Bonus: {Hidden win 1}, {Hidden win 2}

---

## The Week

**{Primary workstream}**: {1-2 sentence summary with key metric/outcome}

**{Secondary workstream}**: {1-2 sentence summary with key metric/outcome}

**Momentum**: {1 sentence - which day(s) were productive, which were quiet}

---

## Next Week

**Must Do**:
- {Carryover 1}
- {Carryover 2}

**Should Do**:
- {Natural next step 1}
- {Natural next step 2}

**Consider**: {One new opportunity or PARA suggestion}

---

## Surprise!

{2-3 sentences max - ONE unexpected insight or pattern. Must be specific and actionable.}

---

## Takeaway

**Strength**: {1 sentence - what worked}
**Fix**: {1 sentence - what needs work}
**Try**: {1 sentence - one concrete thing to experiment with}
```

### Step 5: Quality Checklist

Before outputting, verify:
- [ ] Fits on ONE page (20-25 lines max)
- [ ] All goals accounted for
- [ ] Uses bullets (not paragraphs)
- [ ] Surprise insight is specific and non-obvious
- [ ] Each section is 1-3 sentences max
- [ ] Scannable in 30 seconds

## What Makes a Good "Surprise"

**BAD** (obvious):
- "You worked on multiple projects"
- "You had some quiet days"

**GOOD** (specific, actionable):
- "Every time you documented architecture first (Mon, Wed), you completed 2+ goals that day. Days without architecture work had 0 completions."
- "Client Env and MSK work are converging - both use similar observability patterns. Consider a unified 'SIR Observability Playbook' resource."

## Visual Progress Bar

Generate using block characters:
- 0-10%: `░░░░░░░░░░`
- 20%: `██░░░░░░░░`
- 50%: `█████░░░░░`
- 80%: `████████░░`
- 100%: `██████████`

## Tag Extraction Patterns

When scanning daily notes, look for these patterns:
```
#progress - [content]
#insight - [content]
#decision - [content]
#blocker - [content]
#observation - [content]
#win - [content]
```

Also extract from Command Center style entries:
```
- **progress**: [content]
- **insight**: [content]
```

## Tone Guidelines
- Analytical but motivating
- Specific over generic (use actual examples)
- Direct about gaps, but constructive
- Celebrate genuine wins, don't inflate

## Output Behavior

**Display only** - show the summary in terminal. User can copy what they want.

Do NOT automatically write to files. If user wants to save:
- Offer to append to weekly review file
- Or create separate summary file
