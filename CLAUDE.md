# thirdeye - Claude Configuration

This CLAUDE.md configures Claude Code to work with your thirdeye Obsidian vault.

## Vault Configuration

```
VAULT_PATH=/path/to/your/obsidian/vault
```

Update the path above to point to your Obsidian vault.

## Skills

The following skills are available for managing your personal OS:

### Periodic Notes (`/periodic-note`)
Create daily, weekly, monthly, quarterly, or yearly review notes from templates.

**Triggers**: "create daily note", "weekly review", "monthly note"

### Idea Capture (`/idea-capture`)
Quickly capture ideas with minimal friction.

**Triggers**: "I have an idea", "capture this", "idea about"

### Weekly Synthesis (`/weekly-synthesis`)
Generate weekly progress summaries from daily notes.

**Triggers**: "weekly summary", "how is my week", "summarize my week"

### Skill Inventory (`/skill-inventory`)
Manage and track installed Claude skills.

**Triggers**: "list my skills", "register skill"

### Obsidian Markdown (`/obsidian-markdown`)
Create Obsidian-flavored markdown with wikilinks, callouts, and properties.

### Obsidian Bases (`/obsidian-bases`)
Create database-like views with filters and formulas.

### JSON Canvas (`/json-canvas`)
Create visual canvases, mind maps, and flowcharts.

## Review Workflow

thirdeye uses a cascading review system:

```
Daily → Weekly → Monthly → Quarterly → Yearly
```

Each level rolls up into the next:
- **Daily**: Log achievements, tasks, ideas
- **Weekly**: Review daily achievements, set 3 weekly goals
- **Monthly**: Review weekly progress, set monthly initiatives
- **Quarterly**: Review monthly progress against yearly OKRs
- **Yearly**: Set OKRs, reflect on the year

## Folder Structure

```
vault/
├── reviews/
│   ├── daily/      # Daily notes (YYYY-MM-DD.md)
│   ├── weekly/     # Weekly reviews (Weekly Review YYYY-Www.md)
│   ├── monthly/    # Monthly reviews (Monthly Review YYYY-MM.md)
│   ├── quarterly/  # Quarterly reviews (Quarterly Review YYYY-Qn.md)
│   └── yearly/     # Yearly reviews (Yearly Review YYYY.md)
├── ideas/          # Idea notes
├── Projects/       # Active projects
├── Areas/          # Ongoing responsibilities
├── Resources/      # Reference materials
└── Archives/       # Completed/inactive items
```

## Quick Commands

```bash
# Create today's daily note
/periodic-note daily

# Capture an idea
/idea-capture

# Generate weekly summary
/weekly-synthesis

# List installed skills
/skill-inventory
```
