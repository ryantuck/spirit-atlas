import sys, json


def stdin():
    for line in sys.stdin:
        yield line.strip()


def read_rankings_round_1():
    return [json.loads(line) for line in stdin()]


def seed(batch):
    assert len(batch) == 4
    indexes = [
        [(0,0), (1,1), (2,2), (3,3)],
        [(3,0), (0,1), (1,2), (2,3)],
        [(2,0), (3,1), (0,2), (1,3)],
        [(1,0), (2,1), (3,2), (0,3)],
    ]
    groups = [
        [batch[g][r] for g, r in grp]
        for grp in indexes
    ]
    return groups



if __name__ == '__main__':
    rankings = read_rankings_round_1()
    batch_size = 4
    x = len(rankings) // batch_size
    rankings = rankings[:x*batch_size]
    for i in range(x):
        batch = rankings[i*4:i*4+4]
        # print(batch)
        groups = seed(batch)
        for group in groups:
            print(json.dumps(group))


