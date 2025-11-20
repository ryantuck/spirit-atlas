import sys, json

def _album_class(album):
    album_tidy = album.lower().replace(' ', '-')
    return f'album-{album_tidy}'

def div_track(track):
    track_id = track['id']
    track_title = track['title']
    album = track['album']
    return f'<div class="{_album_class(album)}" data-track-id="{track_id}">{track_title}</div>'

def div_bracket_round(tracks):
    return [f'<div class="bracket-round">'] + [div_track(t) for t in tracks] + ['</div>']

tracks = [json.loads(line) for line in sys.stdin]
for line in div_bracket_round(tracks):
    print(line)
