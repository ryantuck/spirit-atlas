outputs : round-1.html round-2.html

# ----------------------------------
# Round 2
# 	playlist id: 0IgOK8gyt2bOhp6WgZyECj
# ----------------------------------

round-2-track-ids-sorted.txt : groups-105.json
	cat $< | jq 'to_entries | .[] | .value.[] | .id' -r > $@

round-2.html : groups-105.json html_round_1.py
	cat $< | jq | python html_round_1.py > $@

groups-105.html : groups-105.md groups-175.css
	pandoc $< \
		-f gfm \
		--css groups-175.css \
		--metadata title="Round 2" \
		-s -o $@

groups-105.md : groups-105.json md_groups.py
	cat $< | jq | python md_groups.py > $@

groups-105.json : groups-175-ranked.json seed_round_2.py
	cat $< | jq | python seed_round_2.py | jq > $@

# ----------------------------------
# Round 1
# 	playlist id: 1PB3W2M73GTrTlucICRtKO
# ----------------------------------

round-1.html : groups-175-ranked.json html_round_1.py
	cat $< | jq | python html_round_1.py > $@

groups-175.html : groups-175.md groups-175.css
	pandoc $< \
		-f gfm \
		--css groups-175.css \
		--metadata title="Round 1" \
		-s -o $@

groups-175.md : groups-175.json md_groups.py
	cat $< | jq | python md_groups.py > $@

groups-175-ranked.json : groups-175.json results-round-1.txt sort_tracks.py
	cat $< | jq | python sort_tracks.py | jq > $@

groups-175.json : tracks-175.jsonl groups.py
	cat $< | jq -c | python groups.py > $@

# pop version eliminated
tracks-175.jsonl : tracks-176.jsonl
	cat $< | jq -c | grep -v "Teardrops on My Guitar - Pop Version" | jq -c > $@

# randomly-ordered round-1 tracks
tracks-176.jsonl : playlist-round-1-176.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name, album: .track.album.name}' > $@
playlist-round-1-176.jsonl :
	python spotify.py playlist-tracks 1PB3W2M73GTrTlucICRtKO > $@

# ----------------------------------
# Source
# ----------------------------------

# parsed down track db
tracks-all.jsonl : playlist-data.jsonl
	cat $< | jq -c '{id: .track.id, title: .track.name, artist: .track.artists[0].name, album: .track.album.name}' > $@

# complete discography
playlist-data.jsonl :
	python spotify.py playlist-tracks 34CatViYNqZzLQkPbdtW7D > $@


.DELETE_ON_ERROR : # don't leave files around if no clean exit code
