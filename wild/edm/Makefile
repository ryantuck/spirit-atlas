# SOURCE https://open.spotify.com/playlist/3unfcz2U6Y0bSqtAFjPm6B
# SHUFFLED https://open.spotify.com/playlist/4AuzWWD4udbfKsDRdXprqV

rankings-round-1.jsonl : results.txt tracks-all.jsonl
	python parse_round_1.py results.txt tracks-all.jsonl | jq -c > $@

tracks-all.jsonl : playlist-shuffled.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name, album: .track.album.name}' > $@

# ONE-TIME SHUFFLE
# playlist-shuffled.jsonl : playlist.jsonl
# 	cat $< | sort -R > $@

playlist.jsonl : 
	python spotify.py playlist-tracks 3unfcz2U6Y0bSqtAFjPm6B > $@
