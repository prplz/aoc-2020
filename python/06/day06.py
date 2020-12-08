from functools import reduce


def main():
    with open('../../inputs/06.txt') as f:
        data = f.read().split('\n\n')
    data = [list(map(set, group.split())) for group in data]

    part1 = sum(len(reduce(set.union, x)) for x in data)
    assert part1 == 6161

    part2 = sum(len(reduce(set.intersection, x)) for x in data)
    assert part2 == 2971


if __name__ == '__main__':
    main()
