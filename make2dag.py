# all commented-out lines are node_group-related, over-engineering atm

import json
import sys


def edges(target, prereqs):
    return [{'source': prereq, 'target': target} for prereq in prereqs]


#def node_group(group_name, members):
#    return {'group_name': group_name, 'members': members}


def parse_make_line(make_line: str):

    parts = [x.strip() for x in make_line.split(':')]
    assert len(parts) == 2
    left = parts[0]
    right = [x.strip() for x in parts[1].split(' ')]

    return edges(target=left, prereqs=right)

    #if '.' in left: # target
    #    return edges(target=left, prereqs=right)
    #return node_group(group_name=left, members=right)


def main():
    all_edges = []
    #all_node_groups = {}

    for line in sys.stdin:

        result = parse_make_line(line.strip())
        all_edges.extend(result)

        #if 'group_name' in result:
        #    all_node_groups[result['group_name']] = result['members']
        #else:
        #    all_edges.extend(result)

    data = {'edges': all_edges} #, 'node_groups': all_node_groups}
    print(json.dumps(data))


main()
