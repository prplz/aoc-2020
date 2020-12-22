import re
from itertools import starmap


def parse(line) -> tuple[int, int, str, str]:
    m = re.fullmatch(r'^(\d+)-(\d+) (\w): (\w+)\n$', line).groups()
    return int(m[0]), int(m[1]), m[2], m[3]


def part1_valid(min_count, max_count, char, password):
    return min_count <= password.count(char) <= max_count


def part2_valid(pos1, pos2, char, password):
    return (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char)


def main():
    with open('../inputs/02.txt') as f:
        data = list(map(parse, f))
    part1 = sum(starmap(part1_valid, data))
    assert part1 == 483

    part2 = sum(starmap(part2_valid, data))
    assert part2 == 482


if __name__ == '__main__':
    main()
