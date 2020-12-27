import math


def split(iterable, sep):
    buf = []
    for item in iterable:
        if item != sep:
            buf.append(item)
        elif buf:
            yield buf
            buf = []


def main():
    with open('../inputs/10.txt') as f:
        data = list(map(int, f))

    data = sorted(data)
    data.append(data[-1] + 3)

    diffs = [b - a for a, b in zip([0] + data, data)]
    part1 = diffs.count(1) * diffs.count(3)
    assert part1 == 2277

    def combinations(state, res=None):
        res = res or set()
        res.add(tuple(state))
        for i in range(len(state) - 1):
            s = state[i] + state[i + 1]
            if s <= 3:
                combinations(state[:i] + [s] + state[i + 2:], res)
        return res

    split_diffs = split(diffs, 3)
    diff_combinations = map(combinations, split_diffs)
    combination_lens = map(len, diff_combinations)
    part2 = math.prod(combination_lens)
    assert part2 == 37024595836928


if __name__ == '__main__':
    main()
