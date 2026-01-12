---
excalidraw-plugin: parsed
tags: 
publish: false
excalidraw-open-md: true
---
r<% await tp.file.move("/reviews/daily/" + tp.file.title) %>
# <% tp.date.now("dddd, MMMM D, YYYY",0, tp.file.title) %>



![[<% tp.file.title %>.svg]]


## Direction

This is what you're working towards!

![[Weekly Review <% tp.date.now("YYYY") %>-W<% tp.date.now("ww"), %>#<% tp.date.now("YYYY") %>-W<% tp.date.now("ww"), %> Goals]]

> [!warning] Creating a new weekly note
> If you want to create the weekly note, don't click the link above. Instead, open up the Command Palette (CTRL/CMD P) and select Periodic Notes: Open weekly note as per the instructions in [[Goal-setting and Reviews]].

## Tasks due today

```dataviewjs
dv.taskList(dv.pages().file.tasks 
  .where(t => !t.completed)
  .where(t => t.text.includes("{{date:YYYY-MM-DD}}")))
```




## Log

Below are some of the custom checkboxes you can use (delete this from the [[daily]] template if you'd like)

- [ ] To do `[ ]`
- [x] Done `[x]`
- [/] incomplete `[/]`
- [-] Cancelled `[-]`
- [>] Forwarded `[>]`
- [<] Scheduled `[<]`
- [?] Question `[?]`
- [!] Important `[!]`
- [*] Star `[*]`
- ["]  Quote `["]`
- [l] Location `[l]`
- [b]  Bookmark `[b]`
- [i]  Information `[i]`
- [S]  Savings `[S]`
- [I] Idea `[I]`
- [p] Pros `[p]`
- [c] Cons `[c]`
- [f] Fire `[f]` 
- [k] Key `[k]`
- [w] Win `[w]`
- [u] Up `[u]`
- [d] Down `[d]`


---

## Achievements

- 

## Ideas & Creative Thinking

### Idea Capture
- [I] [Quick capture any ideas that emerged today]

### Idea Processing (2-min daily triage)
```dataview
TABLE file.ctime as "Created", status
FROM "ideas"
WHERE contains(file.tags, "idea") AND file.ctime >= date(today) - dur(1 days)
SORT file.ctime DESC
```

### Random Idea for Development
`dice: #idea|link` ← Click to surface a random idea for consideration

##  Process this

```dataview
TABLE file.mday as "Last Modified" from "books"
where file.mtime >= date(today) - dur(1 month)
and contains(file.tags,"inbox")
sort file.mtime desc
```

### Random note

`dice: #inbox|link`

### People to catch up with

```dataview
TABLE date_last_spoken from "people"
where follow_up=true and date_last_spoken <= date(today) - dur(1 month)
```

Or, a random person:  `dice: #person|link`

## Reflection: [[2024-Year of Remembering]]


---



%%
# Text Elements
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.4",
	"elements": [],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 4,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 373.83489990234375,
		"scrollY": 567.7272338867188,
		"zoom": {
			"value": 1
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%