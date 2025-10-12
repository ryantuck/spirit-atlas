# ERDude

Thoughts on what an ideal BI tool might possibly look like.

We codify the relationships between tables and some features of the tables as an ERD (perhaps using [[dbml]]).

The user chooses a table to start on. She is then presented with the next available tables and their columns. This would require dimensions and measures to be defined ahead of time. The key differentiatior is that the tool will guide you through your discovery, prompting you on what to do next, and warning you when you're implementing a many:many join or whatever.

In fact, it seems as though some markup language like LookML might have all features of how we'd want to define the table fields and relationships, but the explore-first interface is a downside.




