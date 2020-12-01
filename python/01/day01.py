import math
from itertools import product


def search(values, n, target=2020):
    return next(
        math.prod(v)
        for v in product(values, repeat=n)
        if sum(v) == target)


def main():
    with open('../../inputs/01.txt') as f:
        values = list(map(int, f))
    part1 = search(values, 2)
    print('part1:', part1)
    assert part1 == 1003971
    part2 = search(values, 3)
    print('part2:', part2)
    assert part2 == 84035952


if __name__ == '__main__':
    main()
