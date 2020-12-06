def main():
    def parse_seat(line):
        row = int(line[:7].replace('F', '0').replace('B', '1'), base=2)
        col = int(line[7:].replace('L', '0').replace('R', '1'), base=2)
        return row * 8 + col

    with open('../../inputs/05.txt') as f:
        seats = list(map(parse_seat, f))

    max_seat = max(seats)
    min_seat = min(seats)

    part1 = max_seat
    assert part1 == 928

    part2 = next(seat for seat in range(min_seat, max_seat + 1) if seat not in seats)
    assert part2 == 610


if __name__ == '__main__':
    main()
