# SOURCE https://open.spotify.com/playlist/3unfcz2U6Y0bSqtAFjPm6B
# SHUFFLED https://open.spotify.com/playlist/4AuzWWD4udbfKsDRdXprqV
# Round of 2048 https://open.spotify.com/playlist/2JT5x5Nb7QaZnddFHhpRdg
# Round of 1024 https://open.spotify.com/playlist/6iUIgndhVGCNA9Pm7wtVbc
# Round of 512

rankings-round-4.jsonl : results-round-4.txt tracks-round-4-512.jsonl
	python parse_round_4.py results-round-4.txt tracks-round-4-512.jsonl | jq -c > $@

tracks-round-4-512.jsonl : tracks-round-4-512-seeds.jsonl
	cat $< | jq -c '.[]' > $@

tracks-round-4-512-seeds.jsonl : rankings-round-3.jsonl
	cat $< | python seed_round_4.py | jq -c > $@

rankings-round-3.jsonl : results-round-3.txt tracks-round-3-1024.jsonl
	python parse_round_3.py results-round-3.txt tracks-round-3-1024.jsonl | jq -c > $@

tracks-round-3-1024.jsonl : tracks-round-3-1024-seeds.jsonl
	cat $< | jq -c '.[]' > $@

tracks-round-3-1024-seeds.jsonl : rankings-round-2.jsonl
	cat $< | python seed_round_3.py | jq -c > $@

rankings-round-2.jsonl : results-round-2.txt tracks-round-2-2048.jsonl
	python parse_round_2.py results-round-2.txt tracks-round-2-2048.jsonl | jq -c > $@

tracks-round-2-2048.jsonl : tracks-round-2-2048-seeds.jsonl
	cat $< | jq -c '.[]' > $@

tracks-round-2-2048-seeds.jsonl : rankings-round-1.jsonl
	cat $< | python seed_round_2.py | jq -c > $@

rankings-round-1.jsonl : results-round-1.txt tracks-round-1-2547.jsonl
	python parse_round_1.py results-round-1.txt tracks-round-1-2547.jsonl | jq -c > $@

tracks-round-1-2547.jsonl : tracks-all.jsonl
	cp $< $@

tracks-all.jsonl : playlist-shuffled.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name, album: .track.album.name}' > $@

# ONE-TIME SHUFFLE
# playlist-shuffled.jsonl : playlist.jsonl
# 	cat $< | sort -R > $@

playlist.jsonl : 
	python spotify.py playlist-tracks 3unfcz2U6Y0bSqtAFjPm6B > $@
