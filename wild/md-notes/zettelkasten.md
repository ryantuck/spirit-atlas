# zettelkasten

Tags: #project

Notes about notes.

[Summary of Zettelkasten][0]

Currently working on [[sort-zettelkasten]].

The CLI is called [[zetty]].

## Roll-your-own

What is the right interface for a zetty? Is it the graph, the list, or something else? One nice thing about CLIs is that those are easy to build. One nice thing about UIs is that it's a slicker REPL for ideas. Seems inevitable that graph traversal algorithms finally see some usage.

For auto-organization: how to indicate more central parts of graph? PageRank, or a trivial version of it, would be a good start.

For leveraging todos: predictable titles in sections, and frontmatter, would allow for parsing out todos or other information.

For reliability in case you need to undo stuff, some auto-commit functionality or something on a cron or each time a file is saved might be good.

Incorporating with [[site]] would be sick, should do soon.

- Autocomplete of tags
- How to display backlinks in vim?
- Serde for roam, eventually?
- Figure out search

## Flow / process

- Parse inbox into smaller groups first, then divide and conquer?
- When to use daily notes? With backlinking, most things can be in daily notes.
- Every note is debt - make it count, don't simply collect
	- Alternatively - make it so easy to store that collection can be effortless
- Worth making daily notes an inbox?
- What's the right cadence for processing daily notes?
- How could I incorporate todo items here? Would I want to?
- How to periodically continue to connect notes?
- Index notes seem like the best starting point.
- Does a project reference an area, or vice versa? Does an area contain an index, or is an index best reverse-engineered?
- Importance of thinking in terms of finite thoughts, instead of files.
- Bullets as thought seeds, versus prose as developed idea
- Think on how to implement [[para-method]]
- Think on a balance of thorough fleshing-out of notes versus leaving breadcrumbs through thought-space
- Think of the ontology of thought: saving brain state on active projects, clear explanations for others, a bag of random self-contained thoughts. [[para-method]] is one way of addressing this. What's mine?

## Interface and discovery

Interface is a hard problem. The graph is so cool, but needs search to supplement it. Some kind of index / navigation notes would be helpful, though I havent' put enough thought into solving this problem. I trust there are better resources out there. Alternatively, graph search queries are tractable and tuneable.

One consideration is that, assuming archives and daily stuff could be filtered from view, that the graph interface _would_ actually be a relatively clean and tractable representation of the note space.

More filtering and categorization!

I think cooler tools and interface improvements will be made. A good idea is to have some auto-organizing algorithm that accepts a handful of params that allow for fine-tune dialing. Then you could just tweak valules and see if the organization scheme is to your liking, given that thinking in graphs is kinda unintuitive.

A command to give me N random thoughts next to one another from milieu could be a good jumping off point.

### Names

I don't want spaces in names, and want to define urls, but also don't want everything always showing up as `a-complex-idea-expressed-as-dashes`. 

Solve this by `{url}.md`, and store a different title in frontmatter or even the header.

## Note types

Treating different note "types" differently seems like it is key, and would assist with interface and discovery.


## Journey

_June 30_. Recognizing I don't actually put the work into notes as such, but rather treat it much more as an insert-only catch-all for my ADD brain. I suppose it's preferable to catch things over not doing so on balance, but the weight is substantial.

## Tools

- https://roamresearch.com
- https://tiddlywiki.com/
- [[obsidian]]
- Notational Velocity
- https://zettlr.com/ is comparable to [[obsidian]]
- https://www.zotero.org/
- https://www.remnote.io/
- https://foambubble.github.io/foam/
- https://github.com/vimwiki/vimwiki
- Cool markdown <> mindmap repl https://markmap.js.org/

## Others

- https://notes.azlen.me/g3tibyfv/
- https://notes.andymatuschak.org/
- https://www.mentalnodes.com/


## Stuff about note-taking

- [Other digital gardens by Maggie Appleton][1]
- https://www.nateliason.com/blog/roam
- https://vimways.org/2019/personal-notetaking-in-vim/
- Tiago Forte talks about memex https://fortelabs.co/blog/interview-with-oliver-sauter-of-memex/

[0]: https://www.lesswrong.com/posts/NfdHG6oHBJ8Qxc26s/the-zettelkasten-method-1
[1]: https://github.com/MaggieAppleton/digital-gardeners


## Random

Random thoughts that I don't have a place for, but are fine for musing.

- Daily free-form tagged notes are a good idea. Insert-only notes, with processing to various places where it needs to go. Command for displaying anything dumped out since checkpoint x. Stream of consciousness writing retains the path for getting somewhere.
- Once I have that, shipping subsections of them to the web would be cool. A cool way to do that would be to define it in yaml or something similar. Basically, the nav.
- Should I need to explicitly create tags? Shouldn't the program offer me an auto-tag functionality, like it shows unlinked mentions? Oh, obsidian does exactly this, just not automatically.
- Insert-only inbox with no deletion ever, just checkpoints? Kind of what daily notes are.
- [[the-web-is-a-zettelkasten]]
- Why is there no api or common language for browsing the web the way that google understands it? surely there's a meaningful graph structure that isn't just 'show me top 10 results given string input'?
- Inbox publishing for later parsing vs direct entry into notes. The former allows for focus. The latter allows for more engagement.
- Roam API https://roamresearch.com/#/v8/help/page/RxZF78p60



