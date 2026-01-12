---
tags:
  - moc
  - {{category}}/moc
aliases:
  - MOC_{{VALUE}}
created: {{DATE:YYYY-MM-DD}}
modified: {{DATE:YYYY-MM-DD}}
category: {{category}}
---

# {{VALUE}} Map of Content

> This MOC provides a centralized hub for all notes related to {{VALUE}} within the {{category}} category.

## Overview

*Brief description of this topic and why it's important*

## Key Concepts

- [[Key Concept 1]]
- [[Key Concept 2]]
- [[Key Concept 3]]

## Related Notes

```dataview
LIST
FROM [[]]
WHERE contains(file.frontmatter.moc, this.file.link)
SORT file.mtime DESC
```

## Daily & Weekly Notes Referencing This Topic

```dataview
TABLE file.mday as "Date" 
FROM "Archives/daily" or "Archives/weekly"
WHERE contains(file.content, this.file.link) OR contains(file.frontmatter.moc, this.file.link)
SORT file.mtime DESC
LIMIT 10
```

## Related MOCs

- [[MOC_Related_Topic_1]]
- [[MOC_Related_Topic_2]]

## Processing Inbox

Use this section to track notes that need to be properly integrated:

- [ ] [[Note to process 1]]
- [ ] [[Note to process 2]]