import sys, json


def stdin():
    for line in sys.stdin:
        yield line.strip()


def read_rankings_round_2():
    return [json.loads(line) for line in stdin()]


def seed(batch):
    assert len(batch) == 16
    indexes = [
        [(0,0), (4,1), (8,0), (12,1)],
        [(1,0), (5,1), (9,0), (13,1)],
        [(2,0), (6,1), (10,0), (14,1)],
        [(3,0), (7,1), (11,0), (15,1)],

        [(0,1), (4,0), (8,1), (12,0)],
        [(1,1), (5,0), (9,1), (13,0)],
        [(2,1), (6,0), (10,1), (14,0)],
        [(3,1), (7,0), (11,1), (15,0)],
    ]
    groups = [
        [batch[g][r] for g, r in grp]
        for grp in indexes
    ]
    return groups



if __name__ == '__main__':
    rankings = read_rankings_round_2()
    batch_size = 16
    x = len(rankings) // batch_size
    rankings = rankings[:x*batch_size]
    for i in range(x):
        idx = i*batch_size
        batch = rankings[idx:idx+batch_size]
        # print(batch)
        groups = seed(batch)
        for group in groups:
            print(json.dumps(group))
