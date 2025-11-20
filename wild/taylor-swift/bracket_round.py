import json, sys

f_tracks = sys.argv[1]
f_results = sys.argv[2]

tracks = [json.loads(t) for t in open(f_tracks).read().splitlines()]
results = open(f_results).read().splitlines()

winners = []
for idx, winner in enumerate(results):
    i = 0 if winner == 'a' else 1
    winners.append(tracks[2*idx+i])
print(json.dumps(winners))
