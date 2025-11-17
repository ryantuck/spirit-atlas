def seed_batch(batch):
    """
    Seed batch of 5 groups of 3 tracks each into 3 groups of 5 tracks each with no repeats.
    """
    idx_pairs = [
        [(0,0), (1,0), (2,1), (3,1), (4,2)],
        [(0,2), (1,2), (2,0), (3,0), (4,1)],
        [(0,1), (1,1), (2,2), (3,2), (4,0)],
    ]
    return [[batch[x][y] for x,y in entry] for entry in idx_pairs]


import sys, json

body = '\n'.join(sys.stdin)
data = json.loads(body)

round_2_qualifiers = [tracks[0:3] for tracks in data.values()] # top 3 advance per group
batches = [round_2_qualifiers[5*i:5*i+5] for i in range(7)] # split into seven batches

round_2_groups = [group for b in batches for group in seed_batch(b)]
output = {f"no. 2-{idx+1}": group for idx, group in enumerate(round_2_groups)}

print(json.dumps(output))
