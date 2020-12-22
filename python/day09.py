from timer import timer


@timer('part1')
def part1_solution(data):
    for i in range(25, len(data)):
        history = data[i - 25: i]
        if all(a + b != data[i] for a in history for b in history):
            return data[i]


@timer('part2')
def part2_solution(data, target):
    for i in range(len(data) - 1):
        sum_ = data[i]
        for j in range(i + 1, len(data)):
            sum_ += data[j]
            if sum_ == target:
                subdata = data[i:j + 1]
                return min(subdata) + max(subdata)
            if sum_ > target:
                break


def main():
    with open('../inputs/09.txt') as f:
        data = list(map(int, f))

    part1 = part1_solution(data)
    assert part1 == 85848519

    assert part2_solution(data, part1) == 13414198


if __name__ == '__main__':
    main()
