import math
from itertools import combinations


def solve(values, n, target=2020):
    return next(
        math.prod(v)
        for v in combinations(values, n)
        if sum(v) == target)


def main():
    with open('../inputs/01.txt') as f:
        values = list(map(int, f))

    part1 = solve(values, 2)
    assert part1 == 1003971

    part2 = solve(values, 3)
    assert part2 == 84035952


if __name__ == '__main__':
    main()
