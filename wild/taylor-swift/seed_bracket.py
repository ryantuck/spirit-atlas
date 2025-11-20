def idx_tuple(ref):
    if ref == 'xx':
        return (7,0)
    letters = 'abcdefg'
    l = ref[0]
    n = int(ref[1])
    return (letters.index(l), n-1)


def seed_refs():
    """
    7 mega-groups (a-g) of 3 groups of 3 tracks ranked 1-3 each = 63 tracks
    +1 saved track = 64
    Approximately distributes matchup strength and tracks that have faced each other already.
    """
    seeds = [
        'a1 b3 c2 d2 a3 d1 e2 f3',
        'e1 f3 a2 b2 b3 d1 f1 e3',
        'c1 d3 e2 f2 a3 b1 f1 g2',
        'a1 d3 b2 c2 c3 d1 e1 g3',
        'a1 c3 e2 g2 b3 c1 f2 g3',
        'b1 d3 a2 c2 e3 f1 g1 f3',
        'e1 g3 b2 d2 a3 c1 g1 f2',
        'b1 c3 a2 d2 e3 g1 g2 xx',
    ]
    return [
        ref # idx_tuple(ref)
        for row in seeds
        for ref in row.split(' ')
    ]


def bracket(ref_list, data):
    output = []
    for ref in ref_list:
        output.append(next(data[ref]))
    return output

import sys, json

body = '\n'.join(sys.stdin)
data = json.loads(body) # groups-105-ranked.json

bracket_qualifiers = [tracks[0:3] for tracks in data.values()] # top 3 advance per group

saved_track_title = 'Getaway Car'
saved_track = next(t for t in [json.loads(line) for line in open('tracks-175.jsonl').readlines()] if t['title'] == saved_track_title)

rankings = {}
for idx, l in enumerate('abcdefg'):
    grps = bracket_qualifiers[3*idx:3*idx+3]
    for i in range(3):
        ref = f'{l}{i+1}'
        rankings[ref] = iter([grp[i] for grp in grps])
rankings['xx'] = iter([saved_track])

b = bracket(seed_refs(), rankings)
print(json.dumps(b))
