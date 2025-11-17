def tracks_ol(tracks):
    lines = []
    for idx, track in enumerate(tracks):
        line = f'{idx+1}. {track["title"]}'
        lines.append(line)
    return lines

def tracks_ul(tracks):
    lines = []
    for idx, track in enumerate(tracks):
        title = track["title"]
        album = track["album"]
        line = f'- {title} ({album})'
        lines.append(line)
    return lines

def group_md(group_id, tracks):
    return '\n'.join([f'## {group_id}\n'] + tracks_ul(tracks))

def all_groups_md():
    body = []
    for group_id, tracks in data.items():
        md = group_md(group_id, tracks)
        body.append(md)
    return '\n\n'.join(body)


import sys, json
data = json.loads('\n'.join(list(sys.stdin)))
output = all_groups_md()
print(output)
