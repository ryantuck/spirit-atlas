import sys
import json


def read_lines(filename):
    lines = open(filename).readlines()
    return [line.strip() for line in lines]


def parse_result(result_txt_line):
    return result_txt_line.split(' ')[0]


def parse_track(tracks_jsonl_line):
    return json.loads(tracks_jsonl_line)


def tracks_batch(n, tracks):
    idx = (n-1) * 5
    return tracks[idx: idx+5]


def batch_results(batch, result):
    ids = {x: track for x, track in zip('abcde', batch)}
    ordered = [ids[x] for x in result]
    return ordered


if __name__ == '__main__':

    results_txt = sys.argv[1]
    tracks_jsonl = sys.argv[2]

    results = [parse_result(r) for r in read_lines(results_txt)]
    tracks = [parse_track(t) for t in read_lines(tracks_jsonl)]

    for idx, result in enumerate(results):
        batch = tracks_batch(idx+1, tracks)
        print(json.dumps(batch_results(batch, result)))
