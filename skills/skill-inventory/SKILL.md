---
name: skill-inventory
description: Manage Claude skill registry in Obsidian vault. Use when user says "register skill", "update skill inventory", "list my skills", "add skill to registry", or "skill dashboard".
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Skill Inventory Manager

## Vault Configuration
- **Vault Path**: `/Users/saisoundararajan/Documents/thirdeye/`
- **Dashboard**: `/Users/saisoundararajan/Documents/thirdeye/Resources/Claude Skills Dashboard.md`
- **Skills Folder**: `/Users/saisoundararajan/Documents/thirdeye/Resources/skills/`
- **Template**: `/Users/saisoundararajan/Documents/thirdeye/templates/skill_note.md`
- **Skills Location**: `~/.claude/skills/`

## Commands

### 1. List Skills (`/skill-inventory` or "list my skills")

**Trigger phrases**: "list my skills", "what skills do I have", "show skills", "skill inventory"

**Workflow**:
1. Scan `~/.claude/skills/` for skill directories
2. Read each SKILL.md to extract name and description
3. Cross-reference with `/Resources/skills/` registry notes
4. Display formatted list:

```
## Your Claude Skills

| Skill | Description | Registered |
|-------|-------------|------------|
| /idea-capture | Capture and develop ideas | Yes |
| /weekly-synthesis | Generate weekly summaries | Yes |
| /skill-inventory | Manage skill registry | Yes |

**Unregistered skills**: [list any in ~/.claude/skills but not in vault]
```

### 2. Register Skill (`/skill-inventory register [name]`)

**Trigger phrases**: "register skill", "add skill to registry", "add [name] to inventory"

**Workflow**:
1. Read skill from `~/.claude/skills/[name]/SKILL.md`
2. Extract metadata (name, description, allowed-tools)
3. Generate registry note using template
4. Preview note content
5. On approval:
   - Write to `/Resources/skills/[name].md`
   - Update dashboard if needed

**Registry Note Template**:
```markdown
---
type: claude-skill
name: [skill-name]
category: [infer: productivity/review/meta/development]
description: [from SKILL.md]
triggers: [extract trigger phrases as array]
created: [today's date]
updated: [today's date]
skill_path: ~/.claude/skills/[name]/SKILL.md
---

# [skill-name]

## Purpose
[Extracted from skill description]

## Commands
| Command | Description |
|---------|-------------|
| /[name] | [primary action] |
| /[name] [subcommand] | [if applicable] |

## Trigger Phrases
- "[phrase 1]"
- "[phrase 2]"

## Examples
[Generate 1-2 example usage scenarios]

## Notes
[Any special considerations]

## Changelog
- [today]: Initial registration
```

### 3. Update Skill Entry (`/skill-inventory update [name]`)

**Trigger phrases**: "update skill entry", "refresh skill registry", "sync skill [name]"

**Workflow**:
1. Read current registry note from `/Resources/skills/[name].md`
2. Read latest SKILL.md from `~/.claude/skills/[name]/`
3. Identify changes (description, triggers, etc.)
4. Preview updates
5. On approval, update registry note with new `updated` date

### 4. Log Usage (`/skill-inventory log [name]`)

**Trigger phrases**: "log skill usage", "I used [skill]", "track skill use"

**Workflow**:
1. Read dashboard `/Resources/Claude Skills Dashboard.md`
2. Update Usage Stats table:
   - Increment "Times Used" for skill
   - Update "Last Used" to today
3. Preview change
4. On approval, update dashboard

## Category Inference

When registering, infer category from skill purpose:
- **productivity**: idea management, note creation, capture
- **review**: summaries, synthesis, analysis
- **meta**: skill management, inventory, registry
- **development**: code-related, engineering tasks
- **workflow**: process automation, pipelines

## Dashboard Sync

When skills change, ensure dashboard dataview queries will pick up changes:
- All registry notes must have `type: claude-skill` in frontmatter
- All notes must be in `/Resources/skills/` folder
- Tags and categories must be consistent

## Skill Discovery

To find all installed skills:
```bash
ls ~/.claude/skills/
```

Each subdirectory with a SKILL.md is a valid skill.

## Preview-First Behavior

**CRITICAL**: Always show preview before writing. Format:

```
## Preview: Skill Registry Entry

**File**: /Resources/skills/[name].md

**Content**:
[Full markdown content]

---
Create this registry entry? (yes/no/edit)
```

## Error Handling

- If skill not found in ~/.claude/skills/: list available skills
- If registry note already exists: offer to update instead
- If dashboard missing: offer to create it
