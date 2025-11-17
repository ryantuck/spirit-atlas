import sys,json

tracks = [json.loads(x.strip()) for x in sys.stdin]

results = {}
n_groups = len(tracks) / 5      # 35
for n in range(int(n_groups)):
    group_id = f'no. {n+1}'
    idx = 5*n
    group_tracks = tracks[idx:idx+5]
    results[group_id] = group_tracks

print(json.dumps(results))
