# Knowledge Graph

This all needs a better name than "knowledge graph".

different than chronology?

chronology of jira tickets, comments, etc vs PR activity - helpful view.

supplement with knowledge graph?

knowledge graph would link jira tickets to github PRs etc, but could also link up so much more - drive, confluence, sites, etc.

Curation seems like it would be important.

Almost everything would necessarily be timestamped. The graph would be the right data structure for the relationships, and then timelines could supplement it.

Simply viewing a log of the past day's worth of stuff across the entire team feels like it would be helpful.

MVP

Pull all jira tickets. Pull all PRs. Scrape comments for links to create initial edges. Done.

Create simple interface for generating more edges. That dot syntax or whatever could do the trick.

Best way to store? NetworkX? Neo4j? Something simpler? Don't even bother with a graph at first, just edges (facts), tickets, PRs (dimensions)?

Would be cool to be able to relationalize it. Would be some collapsed lower-dimensional version of the graph.

Graph would have users as nodes.

```
user:ryantuck is_author_of > PR:my-repo#3123
```

Could even create canonical business concepts in tool - orders, etc. Though that might just turn back into a wiki, albeit a programmatically-accessible one.

Something about being a truly featureless tool does seem appealing. Just link stuff together. Tools for curating, extending, etc. This seems like a worthwhile venture.

Where would this rank on list of projects to work on? Potential adoption. Seemingly high impact.

Enable freeform creation of nodes and edges. Provide curation features.

Could serve as backend of notes linking to one another. This is how you recreate roam.



