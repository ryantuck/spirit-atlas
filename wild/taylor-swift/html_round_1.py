def element(tag: str, content: str, kwargs:dict={}, newlines: bool = False) -> str:
    kws = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())
    parts = [f'<{tag} {kws}>', content, f'</{tag}>']
    if newlines:
        return '\n'.join(parts)
    return ''.join(parts)

def h1(txt):
    return element('h1', txt)

def span(txt):
    return element('span', txt)

def li(txt):
    return element('li', txt)

def ul(lis):
    return element('ul', '\n'.join(lis), newlines=True)

def ol(lis):
    return element('ol', '\n'.join(lis), newlines=True)

def strikethrough(txt):
    return element('del', txt)

def div(elements, kwargs={}):
    return element('div', '\n'.join(elements), kwargs=kwargs, newlines=True)


def link(href):
    return element('link', '', kwargs={'rel': 'stylesheet', 'href': href})

# ------------------------------------------

def track_str(track: dict) -> str:
    title = track['title']
    album = track['album']
    return f'{title} ({album})'


def sorted_tracks(tracks: list[dict], rankings: str) -> list[dict]:
    zipped = zip(tracks, rankings)
    sorted_zipped = sorted(zipped, key=lambda x: x[1])
    return [z[0] for z in sorted_zipped]


def stylized_list(track_strs: list[str]) -> list[str]:
    return track_strs[0:3] + [strikethrough(t) for t in track_strs[3:5]]

def div_group(group_id: str, tracks: list[dict]) -> str:
    track_strs = [track_str(track) for track in tracks]

    # ordered ol for ranked groups, ul for unranked, TODO split out formally
    track_list = ol(lis=[li(t) for t in stylized_list(track_strs)])
    # track_list = ul(lis=[li(t) for t in track_strs])

    return div(
        elements=[
            h1(group_id),
            track_list,
        ],
        kwargs={'class': 'div-group'},
    )


def div_round_1(round_1_data):
    return div(
        elements=[
            div_group(group_id, tracks)
            for group_id, tracks in round_1_data.items()
        ],
        kwargs={'class': 'div-round-1'},
    )

def head():
    elements = [
        element('meta', '', kwargs={'charset': 'utf-8'}),
        link(href='groups-175.css'),
    ]
    return element('head', '\n'.join(elements), newlines=True)


def body(round_1_data):
    return element('body', div_round_1(round_1_data), newlines=True)

def html(round_1_data):
    return '\n'.join([
        head(),
        body(round_1_data),
    ])


import sys, json
data = json.loads('\n'.join(line for line in sys.stdin))
output = html(data)
print(output)
