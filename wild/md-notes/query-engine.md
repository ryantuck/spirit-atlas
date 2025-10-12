# Query Engine

Related: [[code]]

Notes on modeling not-just-sql

Would modeling actually be easier to grok in python? would that be preferable to SQL? if you could compile the python down to SQL reliably then that might give you more flexibility in builds. what if lookml is the best declarative language? something like sqlalchemy but built for analytics instead of for something else. This might be comparably cool in R. Don't load data into place x, but define the rules for manipulating it, compile it down, and let the database do the work. SQL is easy to read but admittedly somewhat tedious to type out. Queries could be parsed via yaml or constructed via python. Parse a database or BQ to understand its indexes etc to kinda recreate the best query plan. run queries constructed in different ways to see which gives you the best execution plan generally.

what would that look like?

it would probably end up looking similar to petl or dplyr or something.

you could define all of the transformations etc you need to do right there.

a query parser for dbt so you don't need jinja templating.

one of the thoughts here is whether jinja templating is good enough, or should you go all-in on dry? each piece is a query composer. sqlalchemy for analytics.
