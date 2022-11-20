import json
import sys


def edges(target_line: str):
    parts = [x.strip() for x in target_line.split(':')]
    assert len(parts) == 2
    target = parts[0]
    prereqs = [x.strip() for x in parts[1].split(' ')]
    return [{'source': prereq, 'target': target} for prereq in prereqs]


for line in sys.stdin:
    for edge in edges(line.strip()):
        print(json.dumps(edge))
