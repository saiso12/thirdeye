---
name: periodic-note
description: Create daily, weekly, monthly, quarterly, or yearly notes in Obsidian from templates with processed Templater variables. This skill should be used when the user wants to create a periodic review note, asks for "today's note", "weekly review", "monthly note", or similar requests.
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
---

# Periodic Note Creator

Create periodic review notes in Obsidian with automatic Templater variable processing.

## Trigger Phrases

- "create daily note", "today's note", "daily review"
- "create weekly note", "weekly review", "this week's note"
- "create monthly note", "monthly review", "this month's note"
- "create quarterly note", "quarterly review"
- "create yearly note", "yearly review", "annual review"
- "periodic note", "create note for [date]"

## Workflow

### Step 1: Determine Note Type

When triggered, identify which note type the user wants:

| Type | Trigger Examples | Output |
|------|------------------|--------|
| daily | "daily note", "today" | `reviews/daily/YYYY-MM-DD.md` |
| weekly | "weekly review", "this week" | `reviews/weekly/Weekly Review YYYY-Www.md` |
| monthly | "monthly note", "this month" | `reviews/monthly/Monthly Review YYYY-MM.md` |
| quarterly | "quarterly review", "Q1/Q2/Q3/Q4" | `reviews/quarterly/Quarterly Review YYYY-Qn.md` |
| yearly | "yearly review", "annual" | `reviews/yearly/Yearly Review YYYY.md` |

If unclear, ask the user:

```
Which periodic note would you like to create?
- Daily (today's date)
- Weekly (current week)
- Monthly (current month)
- Quarterly (current quarter)
- Yearly (current year)
```

### Step 2: Determine Target Date

Default to current date/period unless user specifies otherwise:
- "yesterday's daily note" → previous day
- "last week's review" → previous week
- "January monthly note" → 2025-01 (current year)
- "2024 yearly review" → 2024

### Step 3: Check if Note Exists

Before creating, check if the note already exists at the target location.

If it exists:
- Inform the user the note already exists
- Offer to open/display the existing note path
- Do NOT overwrite

### Step 4: Create the Note

Run the creation script:

```bash
python3 ~/.claude/skills/periodic-note/scripts/create_note.py <type> [--date YYYY-MM-DD]
```

Examples:
```bash
# Today's daily note
python3 ~/.claude/skills/periodic-note/scripts/create_note.py daily

# Specific date daily note
python3 ~/.claude/skills/periodic-note/scripts/create_note.py daily --date 2025-01-10

# Current week's review
python3 ~/.claude/skills/periodic-note/scripts/create_note.py weekly

# Current month's review
python3 ~/.claude/skills/periodic-note/scripts/create_note.py monthly

# Quarterly review
python3 ~/.claude/skills/periodic-note/scripts/create_note.py quarterly

# Yearly review
python3 ~/.claude/skills/periodic-note/scripts/create_note.py yearly
```

The script:
1. Reads the appropriate template from `templates/`
2. Processes Templater variables (tp.date.now, tp.file.title, tp.date.weekday)
3. Creates the note in the correct `reviews/` subdirectory
4. Returns the path to the created note

### Step 5: Confirm Creation

After successful creation, report:
- The full path to the created note
- A brief reminder of what the note contains (e.g., "Your daily note with tasks due today and log sections")

## Vault Configuration

- **Vault Path**: `/Users/saisoundararajan/Documents/thirdeye/`
- **Templates Directory**: `templates/`
- **Output Directory**: `reviews/`

## Template Variable Processing

The script handles these Templater patterns:

| Pattern | Replacement |
|---------|-------------|
| `<% tp.file.title %>` | Note filename without extension |
| `<% tp.date.now("YYYY-MM-DD") %>` | Current date formatted |
| `<% tp.date.now("YYYY-MM", "P-1M") %>` | Date with offset |
| `<% tp.date.weekday("YYYY-MM-DD", -6) %>` | Weekday with offset |
| `{{date:YYYY-MM-DD}}` | Current date |

## Error Handling

- **Template not found**: Report missing template, suggest checking `templates/` directory
- **Note exists**: Inform user, provide path to existing note
- **Invalid date**: Request correct YYYY-MM-DD format
