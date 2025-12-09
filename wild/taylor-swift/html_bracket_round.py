import sys, json

def _album_tidy(album):
    album_tidy = album.lower().replace(' ', '-')
    return album_tidy
    # return f'album-{album_tidy}'

def div_track(track):
    track_id = track['id']
    track_title = track['title']
    album = track['album']
    album_tidy = _album_tidy(album)
    return f'<div class="entry album-{album_tidy}" data-track-id="{track_id}"><span class="album-art"><img src="{album_tidy}.png" /></span><span class="title">{track_title}</span></div>'

def div_bracket_round(tracks):
    return [f'<div class="bracket-round">'] + [div_track(t) for t in tracks] + ['</div>']

tracks = [json.loads(line) for line in sys.stdin]
for line in div_bracket_round(tracks):
    print(line)
