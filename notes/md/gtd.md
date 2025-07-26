# gtd

## Actionable thoughts


### Phone

- inboxing easier (reminders, notes, etc for now)
- display easier (todotxt app for todos, chrome github for notes)
- privacy!

### etc

#### features

- python api - task objects. research if this exists or build.
- have default filters on all todos (e.g. just @rt or @wp)
- done items go to inbox upon completion to review later
- project notes diff
    - determine whether all projects in notes have todos, and vice versa
- enable autocomplete https://click.palletsprojects.com/en/7.x/setuptools/
- allow free-form inboxing without quotes
- implement rudimentary syntax highlighting
- hooks into github, jira, gmail, gcal
- function for creating hash
- do() function


#### chores

- review todotxt features, functionality
- analytics for done work
- move default notes location to dropbox / research viewing md files in dropbox app
- think through markdown vs text for notes
    - no non-buggy md plugins :(




### commands

- add-daily/weekly/monthly checklist
    - manual addition to todo.txt, better than nothing
- overview/today
    - show inbox
    - show past due
    - show due next seven days
    - show done/log last x days
    - show tracking
    - show inspo
    - take filter args
- standup / 15five / mir
    - show @wp todo
    - show done
    - show log
    - show tracking
- done summary
    - log and done last x days
    - summary numbers of last x days
- debug
    - show unexpected lack of context, k/v pairs, etc
    - any stale projects?
- clean
    - move done stuff to done.txt
    - move stale projects out of active dir?
    - archive done.txt stuff eventually? maybe? seems unnecessary.
- docs
    - overview of basic commands like todotxt vim commands
- calendar
    - todos on certain days
- projects
    - show projects, with sub-items
- contexts
    - show contexts, with sub-items


## recurring tasks

daily work bullshit

- daily review
- check github
- check jira, move tickets, log time
- check email
- check my open PRs
- check job failures and triage (on-call)

daily house checklist

- cat litter
- cat water
- cat food
- dog water
- dog food


weekly checklist

- weekly review
- poop yard
- wash car
- lawn
- clean house
- house inventory
- venmo to bank acct
- dog nails

monthly checklist

- monthly review
- heartworm medicine dogs
- file expenses


## weekly review

from: https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf

### Get clear

- Collect everything loose
- Inbox zero
- Empty your head

### Get current

- Review action lists
- Review past calendar
- Review upcoming calendar
- Review tracking
- Review projects
- Review checklists

### Get creative

- Review incubator
- Think on new ideas!



## More thoughts


- all jira tickets should be available in notes
- set goals?
- wall of text doesn't work
- pick the right data structures
- something about terminal velocity ux seems promising
- gtd - cli as primary tool for aggregating, rest of notes are stored in markdown files, adhere to gtd and support all operations. everything available via ios app somehow, use git as backend? something else with more seamless syncing, bc git is managing changelogs instead of acting like an application?
- spend a lot of time shuffling text around - this sort of thing could be done automatically, surely leveraging tags etc.
- inbox should be something where i can just type something and reliably forget about it.
- recurring items should probably come up automatically? or should they require adding via the weekly review?
- auto-formatting contents of todotxt files would be helpful.
- markdown vs txt
- what are the hard requirements? text files when on laptop. accessibility on ios. no-think syncing.
- a private git repo with a git push on a cron might be good. git is designed to handle this sort of thing.
- inboxing app doesn't need to be the same thing as notes app. simplenote doesn't seem like it does the trick. editing notes is less of a big deal on phone since it should be a quick entry / retrieval device. some dumb markdown would be fine.
- some cool notes app is out there that leverages periphery. if vim bindings are everywhere then we're freed from the terminal.
- something about notes as raw stuff vs outline / workflowy format
- the perfect app would be something like vimflowy, implemented in vim, with the ability to tag etc that would produce a todo view
- tx cost to keeping so many thoughts. what's the right balance?
- would be great for a more elegant and fast outline program in vim
- tx cost on making phone calls from desk
- still not super trivial to get a list of everything i did last week
    - ghdone
    - todo-done
    - calendar
    - email
    - standups
- default views for day, week, etc.
    - due this week
    - due this month
    - total time for all tasks by context/project
- for group by, only include existing breakdowns
- can always start 'think' tickets with t:15m, make more followups
- for active - could split out active dir into project notes and thinking
- yaml headers markdown
- followup context
- shipped notes are documentation, in any form
- some way to reconcile notes and projects
- could actually pretty easily sync up with trello
    - dir = column
- ls of notes dir should provide outline of thinking at some level of the
    interface
- mkdocs site with sso auth in front?
    - instead of auth, just obscure via no google indexing, etc?
- pocket as part of notes
- add punt context for stuff not to do this week
- each project or context has a dedicated md notes file by default
    - each todo gets its own unique md file namespace
    - something about cleaning all this up or archiving regularly to git
- so much mental weight builds up with extra small items filling the backlog. Like, maybe it's not normal for a backlog to grow so quickly. For example, how many tickets would moving to airflow solve?
- can I structure these notes files more? nesting, data structures, etc.
- gtd way to clear all of a particular tag x
- gtd best way to show tasks to plan for week, day
- gtd arbitrary ids, depends on, etc.
- gtd no common ids
- gtd standard place for associated notes
    - one file per note is fine, but then solve the problem of switching between
        them easily - that's the hard bit
        - is this actually only a problem when triaging the inbox?
- gtd - throw stuff in incubator liberally, triage less frequently
- gtd - project ordering
- gtd - load up schedules regularly
    - birthday schedules
        - vick 5/16
        - everyone else?
- todotxt - add dependencies, hide by default
- todotxt - format output based on other tags
- todotxt - wrapper around due:tuesday
- gtd - any errands runs this week?
- gtd - incorporate site pages into holistic notes
- gtd - sheets/trello integration
- what to do - photos? album in icloud? something else?
    - eye rx
    - drivers license
    - etc
- gtd - compare estimates times to actual times, linear regression
- types of tasks - should be context-related?
- how to handle 'think about' tasks? sizing is so vague.
- gtd - each file is a concept, each concept has in, outlines, links - what
    else?
- planning for a week - what a thought!
- some reminder about planning out for next month - birthdays, etc
- better project planning abilities
- notes - on file save, backup (core drive in dropbox / run proc constantly on certain dirs)?
- in what other areas of life can I write notes while I'm in the thick of it
- the more i can manage many projects simultaneously, the better off i'll be
- constant thought documentation hyper gtd
- cadences
- how to get faster at gtd
- gtd reddit
- downside gtd know there's a system
- diff todotxt files?
- regularly purge notes
- gmail is more reliably system for tracking things than mine is. how to change?
- should only ever be knocking off todo items.

### sort

How to do a weekly review: https://fortelabs.co/blog/the-one-touch-guide-to-doing-a-weekly-review/
- Email
- Calendar
- Folders
- Notes
- Tasks

seems like using dot notation, or depends_on:task could be helpful. but how to uniquely id tasks to leverage this? entirely unclear.


gtd - what projects are still tracked that don't have any available next actions?

gtd - incorporate board into overview, remove inbox?

google cal is the only place for a calendar right now. probably as it should be? at least, for work. how to incorporate into gtd?

oo - projects, can define a dot syntax for next steps that get added to inbox only once initial tasks are completed?

trigger list during weekly review - these would be similar to the daily review tasks (check email, etc), but less action-focused.

read / watch / etc tasks for when bored - hide by default?

tickler.txt - would be helpful to parse these and bring them in automatically or within the overview command.

2020-03-28 download dashboard tickets
2020-03-01 monthly review

incubator has both thoughts and possible tasks - more clutter than needed!

gtd reviews would be made much easier by ensuring these got split out from each other. find a new job is a task-oriented thing, rather than a thought like "holy fuck, ritz crackers are awesome".

maybe these things end up as useful per-"project" notes, but not every random thought needs to make it into a proper gtd tracking system. actions versus dwelling. think about it.


being very fast at all operations is good for gtd stuff. i don't do diligent daily inbox processing because i can't guarantee it will be fast. writing code to help speed things up is good. methodologies are helpful too. not getting distracted would be great.

2020-01-27 initial thoughts - really really nice to be able to offload finite thought without needing to fire up everything else

so cool that i can write stuff here and this just works. crazy how long that actually took to get around to implementing.




gtd - everything should flow somewhere. could track rate of publishing / pruning thoughts. a big long incubator file of thoughts that never go anywhere is doing me less good than it should.

gtd - idea of sorting out my ideas to determine which ones are the best to work on, unload, publish, etc, makes it less of a mismash and more of the final piece of what all of this was missing - actually doing shit fast and effectively

create gtd, share with ppl as a thing ontop of todotxt - people would think it's pretty cool honestly
gtd - use spatial metaphors for things. incubator or attic?
could just set a home metaphor (or custom metaphor) config for the cli

gtd garage - space for rugged comfort, complete control over build

gtd - save versions of notes as they were written, potentially shareable, slightly mutable without losing intensity. could make art out of this. watch someone write notes. watch tons of people write notes. tell some before and after whether or not they'd be part of an art installation. neat.

gtd - more explicit modes of being versus random jumble of whatever happens. both are needed. everything in excess, including moderation.

gtd notes - generally not even creating markdown for md consumption - text definitely makes more sense

gtd still no great handle on projects and how to work with them

gtd action - syntax highlighting, duh. todotxt already has syntax highlighting - could i just use that instead?

might be worth it to auto send inbox to incubator? or will this just make the incubator anotehr inbox?

list of things to try like github actions, observable hq, etc, set aside time to do this

do we really even need a done.txt? isn't a single file good enough?

can every single saved version of the file be stored somewhere? so lightweight, seems worth it.

could switch log functionality to just creating a new todo with an x and a completion date

interactive task creation could be cool

unit tests

generate id as hash of line - implicit id, no manipulating, etc.

concept of desktop - what's my plan today? what should i focus on? prevent constantly looking at next steps and getting distracted.

if file writing is happening, throw error if vim swp file is open

better logic for parsing kv pair values - links will have colons in them at least, maybe parse out?

what's the best way to ensure i have a list of crap available when running errands? expectation is that anything titled 'buy' should show up. need to filter on a context.

Tagging thoughts, those hashtags have dedicated pages, very light overhead that gets similar to roam research.

Tagging could be added to todotxt spec for evergreen topics, I think. Or is that just what contexts are for? Contexts are pretty broad.

Display all notes as markdown site. Allow for hyperlinks. This is just what the web is, right? Linked pages displaying information.

The Roam abstraction is helpful since every thought has arbitrary nested sub-thoughts.

Something fundamentally different from a list of stuff (read book) versus thoughts. Lists of stuff can be abstracted.

Create a way to wander through gardens of thought. Experiment with different things. Structured processing versus wandering. See what works. One idea - command to show random line from incubator file.

Structuring of thought from unstructured thought is basically attempting to recreate the structure that is already out there, waiting to be picked up.

Sometimes thoughts structure themselves into a hierarchy, other times more tags might be helpful.

Markdown is structured and maps to html structure. Could extract structure out of markdown. Would need to solve the markdown plugin problem. Might be the right text data structure for notes though. Can get lists, etc. Smart idea.

Can generate ideas on the fly pretty quickly when focused on problem. How does that affect need to write everything down?

Notes should constantly be published at rate that I do anything with them.

Design cli cockpit for life - very startrek or something. stop struggling against tools. computers reduce struggle against tools. or should. thought multiplier. [[gtd]]

Linking to things in google docs etc for tasks in app is helpful for ref [[gtd]]

From within note, keystroke to open new subwindow automatically without managing windows. [[gtd]]

Time spent on infrastructure of life to free up feature work of life [[gtd]]

Wandering garden of thoughts - could assemble some sort of structure without even tagging. Notes have some degree of parity across multiple dimensions - text contents, length, words in common, etc. [[gtd]]

Workflowy for hierarchical thinking, roam for graphical thinking, which makes more sense? Or do both make sense in different contexts? [[gtd]]

Graph explorer of inter-connected notes [[gtd]]

Should have a list of code projects to work on at any given moment [[gtd]]

Think of metaphors for GTD. Workbench metaphor for notes file. Etc. [[gtd]]

Can still put things into piles while actively note-doing. [[gtd]]

Hierarchy of existing tags. Tagging something stack-overflow automatically groups it into programming. Could do light parsing for tags. [[gtd]]

Why not just have all these thoughts published on some page? Do that. Think in public by default, right? Always an option to keep private. [[gtd]] [[site]]

Scheduling list templates to drop at time t could be useful but it's not clear anything should be automated at this point. [[gtd]]

Should always have a notes section for each task, and it should be easy. [[gtd]]

Could design app for browser with vim bindings available in the various windows. Or figure out programmatic vim windowing. [[gtd]]

Twitter is kind of the note-taking platform that i am envisioning, but only contains a log. some type of log curation would be helpful for notes. [[gtd]]

Moving tagged thoughts into a text file should be a super fast operation. Too much time spent formatting still.


DAILY REVIEW

review all comms channels
make actionable comms tasks

thoughts could nest with some syntax like [[gtd]] or whatever. pointer to a file.

Show all lines without tags for processing? Or just actually organize notes outside of incubator? The latter seems like a good approach right now.


I should be able to put 'feed dogs' into todotxt every day for a year into the future without the interface being effected by it.

Need to figure out automated commits to some sort of backup system, probably github. Autocommits would be good. Can always squash commits retroactively. Always push to dev branch, and conditionally publish for merges to master?

Figure out tying tags to [[zettelkasten]]

Bug - todotxt mobile app reformats text to remove files, fucks up inbox. Not the end of the world really.

Process - still need to figure out best cadence for handling tracking list.

Recurring - doctor, yearly?

Setup - could switch to google drive eventually instead of dropbox. Shrug.

Could figure out managing timers in txt file format, some cron job that checks and creates macos notifications or ios.

Cron expression for reminders.

Priorities and tags in todotxt file have worked okay for now. What else could I try? An impact / time calc might be cool.

Recurring tasks could diff against existing ones.

Should created dates be there by default? It'd be nice, but worried about impact to workflow.

Better mobile input system is still needed. Reminders is okay for now. Maybe straight up todotxt inbox would be preferable.

Tying priority levels to different time horizons is tough.

Incorporate notes from [[zettelkasten]]

Bug - ls doesn't show stuff

Fast vs deep when inbox processing.

File safety warnings seem appropriate for this and [[zettelkasten]]

incorporate notes
fix ls issue
functionality around task types - do, google, etc.
other views, like overview.
wow, really not in gtd notes file often, when thinking about this. should be the first place to find out what's up.

Share todos with brittany? How?

Generally, try to knock out 'think' tasks. Try to crush out google tasks. BS tasks, etc.

for gtd stuff, something like a vim keystroke to add an arbitrary id, and then a separate dot file or something for defining id dependencies. really lightweight. diff mechanism to determine any invalid ids, etc.


function to remove double whitespace from files [[gtd]]

function to move all lines with tags into target file [[gtd]]

project planning - think through utility vs effort graph [[gtd]]

once thought is structured, can be referenced, less constant generation of sea of thoughts around subject [[gtd]]


2020-02-14 just tag thoughts initially, tooling to pull them all together, then a next more formalized stage [[gtd]]

vim window splitting not tmux - could reliably do all gtd stuff as a single big vim window without tmux window splitting required. basically an application [[gtd]]

2020-02-14 can't put exclamation point in inboxed thought - what else? [[gtd]]

2020-02-14 support loops as i go day-to-day - not quite todo, but should show up there? [[gtd]]

experiment with different behaviors - can efficiently change system, so can efficiently change behavior [[gtd]]

find "do" actions with missing time, not think or google or buy

Priority buckets - A for today, B for top priorities, C for soon. Anything missing?

Weekly review - fully reset priorities, force scan of next actions.

2020-02-11 syntax highlighting why are contexts and projects same color?

gtd command for active thoughts [[gtd]]
2020-02-11 standup command [[gtd]]

Time estimates and necessities are probably too rigid.

2020-02-11 overview should find any prioritized or due stuff for today [[gtd]]

gtd ability to plan projects without filling up next actions list [[gtd]]


2020-02-11 command to show done work [[gtd]]

primers for remembering task lists. [[gtd]]
check jira statuses.
check work email.
check personal email.
review github notifications.
check outstanding reviews.

gtd commands to open tabs i need. duh. [[gtd]]
extensions to gtd cli would be pretty simple to include. unclear that's prudent, but i would like to experiment with adding a urls command or something. [[gtd]]

2020-02-11 reminders - jira log time [[gtd]]

All think tasks timeboxed to 5m by default?

2020-02-10 gtd inbox syncing via background task with sheets or something, accessible backend for a no code app

2020-02-10 recurring task review calendar attendance weekly [[gtd]]

at signs vs hashtags - adhere to todotxt for consistency

2020-02-07 projects may end up turning into contexts. [[gtd]]

high priority tasks as push notifications [[gtd]]


CLI Launchpad!

- Get all open github PRs / notifications in CLI
- Get all jira notifications in CLI
- Get all emails (or easy way to open)

Occasionally not inboxing anything is worthwhile - freedom to think, knowing more ideas will always come. Not as critical to write every last thing down.

Do a monthly review!

Issue with including a "!" in inbox input.

How to best get into a schedule with gtd? How to schedule weekly and monthly reviews, and actually stick to them? Maybe a fucking calendar!?

A better todotxt interface for filtering out the million files into a shorter list. The `todo` CLI should do this though, right?