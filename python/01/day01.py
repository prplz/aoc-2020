import math
from itertools import product

from timer import timer


def loop_solution_1(values, target=2020):
    for a in values:
        for b in values:
            if a + b == target:
                return a * b


def loop_solution_2(values, target=2020):
    for a in values:
        for b in values:
            for c in values:
                if a + b + c == target:
                    return a * b * c


def functional_solution(values, n, target=2020):
    return next(
        math.prod(v)
        for v in product(values, repeat=n)
        if sum(v) == target)


def main():
    with open('../../inputs/01.txt') as f:
        values = list(map(int, f))

    part1_solutions = [
        (loop_solution_1,),
        (functional_solution, 2),
    ]
    for func, *args in part1_solutions:
        with timer(f'part1 {func.__name__}'):
            assert func(values, *args) == 1003971

    part2_solutions = [
        (loop_solution_2,),
        (functional_solution, 3),
    ]
    for func, *args in part2_solutions:
        with timer(f'part2 {func.__name__}'):
            assert func(values, *args) == 84035952


if __name__ == '__main__':
    main()
