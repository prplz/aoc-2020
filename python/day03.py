import math
from collections.abc import Iterable
from itertools import count


def main():
    with open('../inputs/03.txt') as f:
        data = list(map(str.rstrip, f))

    width = len(data[0])
    height = len(data)

    int_pair = tuple[int, int]
    int_pairs = Iterable[int_pair]

    def make_slope(step: int_pair) -> int_pairs:
        x_step, y_step = step
        x = (x % width for x in count(0, x_step))
        y = range(0, height, y_step)
        return zip(x, y)

    def tree_count(slope: int_pairs) -> int:
        return sum(data[y][x] == '#' for x, y in slope)

    def solve(*steps: int_pair) -> int:
        slopes = map(make_slope, steps)
        tree_counts = map(tree_count, slopes)
        return math.prod(tree_counts)

    part1 = solve((3, 1))
    assert part1 == 167

    part2 = solve(
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    assert part2 == 736527114


if __name__ == '__main__':
    main()
