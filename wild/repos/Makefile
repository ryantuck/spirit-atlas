repos-public.txt : repos-public.jsonl
	jq . $< | jq '"\(.name)\t\t\t\t\(.description)"' -r > $@

repos-public.jsonl : repos-list.jsonl
	jq . $< | jq 'select(.isPrivate == false)' | jq -c > $@

repos-list.jsonl :
	gh repo list \
		--json name,url,description,isPrivate,isFork,createdAt,updatedAt \
		--limit 1000 | jq '.[]' -c > $@
