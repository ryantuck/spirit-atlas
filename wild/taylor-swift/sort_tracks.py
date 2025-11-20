def sorted_tracks(tracks: list[dict], rankings: str) -> list[dict]:
    labeled = {x: track for x, track in zip('abcde', tracks)}
    output = [labeled[x] for x in rankings]
    return output


import json, sys
filename = sys.argv[1]
results_round_1 = [line.strip() for line in open(filename).readlines()]
data = json.loads('\n'.join(line for line in sys.stdin))
groups = list(data.values())
zipped = list(zip(groups, results_round_1))
sorted_groups = [sorted_tracks(tracks, rankings) for tracks, rankings in zipped]
output = dict(zip(data.keys(),sorted_groups))
print(json.dumps(output))
