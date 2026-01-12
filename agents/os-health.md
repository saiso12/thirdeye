# OS Health Agent

> Future agent for monitoring thirdeye OS health and usage patterns.

## Purpose

This agent will periodically check the health of your thirdeye OS and prompt you for feedback.

## Planned Capabilities

### Usage Monitoring
- Track which skills are being used
- Identify unused skills that could be removed
- Suggest skills based on your patterns

### Health Checks
- Verify templates are valid
- Check for broken wikilinks
- Ensure review cascade is being followed

### Prompts & Nudges
- "You haven't done a weekly review in 2 weeks"
- "Your ideas/ folder has 5 uncategorized ideas"
- "Consider archiving these stale projects"

### OS Feedback Loop
- Collect friction points
- Suggest workflow improvements
- Generate release notes from changes

## Status

**Not yet implemented** - Placeholder for v0.2.0

## Trigger Ideas

```
/os-health          # Run full health check
/os-health quick    # Quick status
/os-health suggest  # Get improvement suggestions
```
