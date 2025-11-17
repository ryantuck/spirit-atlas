items.jsonl : # pocket-archive-reverse-*
	cat pocket-archive-reverse-*.json | jq '.data.user.savedItems.edges.[] | .node.item' -c > $@
