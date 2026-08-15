import sys, json


def stdin():
    for line in sys.stdin:
        yield line.strip()


def read_rankings_round_3():
    return [json.loads(line) for line in stdin()]


def seed(batch):
    assert len(batch) == 32
    indexes = []
    for i in range(8):
        grp = [(i, 0), (i+8, 1), (i+16, 0), (i+24, 1)]
        indexes.append(grp)
    for j in range(8):
        grp = [(j, 1), (j+8, 0), (j+16, 1), (j+24, 0)]
        indexes.append(grp)
    groups = [
        [batch[g][r] for g, r in grp]
        for grp in indexes
    ]
    return groups



if __name__ == '__main__':
    rankings = read_rankings_round_3()
    batch_size = 32
    x = len(rankings) // batch_size
    rankings = rankings[:x*batch_size]
    for i in range(x):
        idx = i*batch_size
        batch = rankings[idx:idx+batch_size]
        # print(batch)
        groups = seed(batch)
        for group in groups:
            print(json.dumps(group))
