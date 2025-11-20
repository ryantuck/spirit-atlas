outputs : round-1.html round-2.html bracket-tracks.jsonl

bracket.html : html_bracket_round.py
	echo '<link rel="stylesheet" href="bracket.css">' > $@
	cat html-rounds-input.html >> $@
	echo '<div class="bracket">' >> $@
	cat bracket-tracks.jsonl | python html_bracket_round.py >> $@
	cat bracket-tracks-32.jsonl | python html_bracket_round.py >> $@
	cat bracket-tracks-16.jsonl | python html_bracket_round.py >> $@
	cat bracket-tracks-8.jsonl | python html_bracket_round.py >> $@
	cat bracket-tracks-4.jsonl | python html_bracket_round.py >> $@
	cat bracket-tracks-2.jsonl | python html_bracket_round.py >> $@
	cat bracket-tracks-1.jsonl | python html_bracket_round.py >> $@
	echo '</div>' >> $@
	echo '<script src="rounds-input.js"></script>' >> $@


# ----------------------------------
# Bracket
# 	playlist id: 6IO6fZlgFER4AuOfE30XlZ
# 	round of 32: 58Teqr5cnjWSpQ8wTTeRge
# 	round of 16: 1u0rt1Y0H8LN67pr87uPia
# 	round of 8: 0aRJSwhl5H8TYBZxuJQoSD
# 	Wow, beginning of bracket round, so exciting, every song is dope, I
# 	have no clue what's gonna come out on top, five matchups in and lots are
# 	already close calls, the rap bracket was arguably easier!
# ----------------------------------
bracket-tracks-1.jsonl : bracket-tracks-2.jsonl results-bracket-2.txt
	python bracket_round.py $^ | jq '.[]' -c > $@

bracket-tracks-2.jsonl : bracket-tracks-4.jsonl results-bracket-4.txt
	python bracket_round.py $^ | jq '.[]' -c > $@

bracket-tracks-4.jsonl : bracket-tracks-8.jsonl results-bracket-8.txt
	python bracket_round.py $^ | jq '.[]' -c > $@

bracket-track-ids-8.txt : bracket-tracks-8.jsonl
	cat $< | jq .id -r > $@

bracket-tracks-8.jsonl : bracket-tracks-16.jsonl results-bracket-16.txt
	python bracket_round.py $^ | jq '.[]' -c > $@

bracket-track-ids-16.txt : bracket-tracks-16.jsonl
	cat $< | jq .id -r > $@

bracket-tracks-16.jsonl : bracket-tracks-32.jsonl results-bracket-32.txt
	python bracket_round.py $^ | jq '.[]' -c > $@

bracket-track-ids-32.txt : bracket-tracks-32.jsonl
	cat $< | jq .id -r > $@

bracket-tracks-32.jsonl : bracket-tracks.jsonl results-bracket-64.txt
	python bracket_round.py $^ | jq '.[]' -c > $@

bracket-track-ids.txt : bracket-tracks.jsonl
	cat $< | jq .id -r > $@

bracket-tracks.jsonl : groups-105-ranked.json seed_bracket.py
	cat $< | python seed_bracket.py | jq '.[]' -c > $@

# ----------------------------------
# Round 2
# 	playlist id: 0IgOK8gyt2bOhp6WgZyECj
# ----------------------------------

round-2.html : groups-105-ranked.json html_round_1.py
	cat $< | jq | python html_round_1.py > $@

groups-105-ranked.json : groups-105.json results-round-2.txt sort_tracks.py
	cat $< | jq | python sort_tracks.py results-round-2.txt | jq > $@

round-2-track-ids-sorted.txt : groups-105.json
	cat $< | jq 'to_entries | .[] | .value.[] | .id' -r > $@

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
	cat $< | jq | python sort_tracks.py results-round-1.txt | jq > $@

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
