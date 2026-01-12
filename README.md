# thirdeye

A personal operating system built on Obsidian + Claude Code.

thirdeye combines Obsidian's knowledge management with Claude's AI capabilities to create an integrated system for managing your life - from daily tasks to yearly goals.

## What's Included

### Templates

Obsidian templates using Templater syntax for periodic reviews and knowledge management.

| Category | Templates |
|----------|-----------|
| **Periodic** | daily, weekly, monthly, quarterly, yearly |
| **Project** | project, area, resource, archive (PARA method) |
| **Idea** | idea_quick_capture |
| **Meta** | meeting, moc (Map of Content), note |

### Claude Skills

AI-powered skills that integrate with your Obsidian vault:

| Skill | Purpose |
|-------|---------|
| `/periodic-note` | Create periodic review notes with processed Templater variables |
| `/idea-capture` | Quick idea capture with automatic tagging and linking |
| `/weekly-synthesis` | Generate weekly summaries from daily notes |
| `/skill-inventory` | Manage and track your Claude skills |
| `/obsidian-markdown` | Create Obsidian-flavored markdown |
| `/obsidian-bases` | Create database-like views |
| `/json-canvas` | Create visual canvases and mind maps |

## The System

thirdeye uses a cascading review workflow:

```
Daily → Weekly → Monthly → Quarterly → Yearly
         ↓         ↓          ↓           ↓
    3 goals    initiatives   OKRs      vision
```

Each level embeds content from the previous, creating a connected chain from daily actions to yearly objectives.

## Installation

### 1. Set Up Obsidian Vault

Copy templates to your vault:

```bash
cp -r templates/* /path/to/your/vault/templates/
```

Create the review folder structure:

```bash
mkdir -p /path/to/your/vault/reviews/{daily,weekly,monthly,quarterly,yearly}
mkdir -p /path/to/your/vault/{ideas,Projects,Areas,Resources,Archives}
```

### 2. Install Obsidian Plugins

Required plugins:
- [Templater](https://github.com/SilentVoid13/Templater) - Template processing
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview) - Dynamic queries
- [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes) - Note scheduling

Optional:
- [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) - Visual notes

### 3. Install Claude Skills

Copy skills to your Claude configuration:

```bash
cp -r skills/* ~/.claude/skills/
```

### 4. Configure Claude

Copy the CLAUDE.md to your home directory and update the vault path:

```bash
cp CLAUDE.md ~/.claude/CLAUDE.md
# Edit ~/.claude/CLAUDE.md and set VAULT_PATH
```

## Usage

### Daily Workflow

```bash
# Start your day
claude "/periodic-note daily"

# Capture ideas as they come
claude "I have an idea about improving my morning routine"

# End of day - log achievements in your daily note
```

### Weekly Workflow

```bash
# Weekly review
claude "/periodic-note weekly"

# Or generate a summary
claude "/weekly-synthesis"
```

### Monthly/Quarterly/Yearly

```bash
claude "/periodic-note monthly"
claude "/periodic-note quarterly"
claude "/periodic-note yearly"
```

## Customization

### Templates

All templates use Templater syntax. Common variables:
- `<% tp.file.title %>` - Note filename
- `<% tp.date.now("YYYY-MM-DD") %>` - Current date
- `![[Note#Section]]` - Embed section from another note

### Skills

Skills are located in `~/.claude/skills/`. Each skill has:
- `SKILL.md` - Instructions and configuration
- `scripts/` - Automation scripts (optional)
- `references/` - Reference documentation (optional)

## Philosophy

thirdeye is built on these principles:

1. **Connected thinking** - Daily actions link to weekly goals, which link to monthly initiatives, which link to yearly OKRs
2. **AI-assisted, human-controlled** - Claude helps with creation and synthesis, you make the decisions
3. **Minimal friction** - Quick capture, automatic processing, easy review
4. **Open and portable** - Plain markdown files, no vendor lock-in

## License

MIT

## Contributing

Issues and PRs welcome. This is a personal system shared publicly - adapt it to your needs.
