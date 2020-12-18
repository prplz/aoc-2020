def execute(code, correction=False, acc=0, pc=0, visited=None):
    visited = visited or set()
    while pc < len(code):
        if pc in visited:
            return False, acc
        visited.add(pc)
        op, arg = code[pc]
        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            if correction:
                # fork with nop
                completed, result = execute(code, False, acc, pc + 1, set(visited))
                if completed:
                    return True, result
            pc += arg
        elif op == 'nop':
            if correction:
                # fork with jmp
                completed, result = execute(code, False, acc, pc + arg, set(visited))
                if completed:
                    return True, result
            pc += 1
    return True, acc


def main():
    with open('../inputs/08.txt') as f:
        lines_split = map(str.split, f)
        code = [(op, int(arg)) for op, arg in lines_split]

    _, part1 = execute(code)
    assert part1 == 1949

    _, part2 = execute(code, correction=True)
    assert part2 == 2092


if __name__ == '__main__':
    main()
