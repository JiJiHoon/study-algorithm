import sys

input = sys.stdin.readline


def solve(data):
    result = []

    stack = []
    push_count = 0
    for element in data:
        elem = int(element)

        if elem > push_count:
            while elem > push_count:
                push_count += 1
                stack.append(push_count)
                result.append('+')
            stack.pop()
            result.append('-')
            continue

        temp = stack.pop()
        if temp != elem:
            return ['NO']
        result.append('-')

    return result


if __name__ == '__main__':
    n = int(input())
    data = [int(input()) for _ in range(n)]

    result = solve(data)

    print('\n'.join(result))
