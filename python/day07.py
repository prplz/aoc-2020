def main():
    def parse(line):
        line = line.removesuffix('.\n')
        outer, inners = line.split(' bags contain ')
        if inners == 'no other bags':
            return outer, []
        inners = [
            (inner[2:].removesuffix(' bag').removesuffix(' bags'), int(inner[0]))
            for inner in inners.split(', ')]
        return outer, inners

    with open('../inputs/07.txt') as f:
        bags = dict(map(parse, f))

    def search(current):
        return current == 'shiny gold' or any(search(bag) for bag, _ in bags[current])

    part1 = sum(search(bag) for bag in bags if bag != 'shiny gold')
    assert part1 == 372

    def bag_count(current):
        return sum(count * (1 + bag_count(bag)) for bag, count in bags[current])

    part2 = bag_count('shiny gold')
    assert part2 == 8015


if __name__ == '__main__':
    main()
