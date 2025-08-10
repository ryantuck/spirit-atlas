repos-list.jsonl :
	gh repo list \
		--json name,url,description,isPrivate,isFork,createdAt,updatedAt \
		--limit 1000 | jq '.[]' -c > $@
