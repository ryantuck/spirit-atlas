# SOURCE https://open.spotify.com/playlist/3unfcz2U6Y0bSqtAFjPm6B
# SHUFFLED https://open.spotify.com/playlist/4AuzWWD4udbfKsDRdXprqV

tracks-round-2-2048.jsonl : rankings-round-1.jsonl
	cat $< | python seed_round_2.py | jq -c > $@

rankings-round-1.jsonl : results.txt tracks-round-1-2547.jsonl
	python parse_round_1.py results.txt tracks-round-1-2547.jsonl | jq -c > $@

tracks-round-1-2547.jsonl : tracks-all.jsonl
	cp $< $@

tracks-all.jsonl : playlist-shuffled.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name, album: .track.album.name}' > $@

# ONE-TIME SHUFFLE
# playlist-shuffled.jsonl : playlist.jsonl
# 	cat $< | sort -R > $@

playlist.jsonl : 
	python spotify.py playlist-tracks 3unfcz2U6Y0bSqtAFjPm6B > $@
