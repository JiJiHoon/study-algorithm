import copy
import sys

input = sys.stdin.readline


def find_dwarf(data):
    return find_dwarf_recursive(data, [], 0, [])


def find_dwarf_recursive(data, tmp, depth, result):
    if depth == 6:
        if sum(tmp) == 100:
            result = copy.deepcopy(tmp)
        return result

    for i in range(depth, len(data) - 7 + depth + 1):
        tmp[depth] = data[i]
        find_dwarf_recursive(data, tmp, depth + 1)

    return result


def solve(data):
    data = sorted(data)

    result = find_dwarf(data)

    return result


if __name__ == '__main__':
    data = []
    for i in range(9):
        data.append(int(input()))

    result = solve(data)

    print('\n'.join(map(str, result)))
