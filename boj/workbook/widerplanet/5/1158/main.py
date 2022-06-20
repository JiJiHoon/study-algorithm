import sys

input = sys.stdin.readline


def solve(n, k):
    queue = [i for i in range(1, n + 1)]

    result = []
    index = 0
    while queue:
        index = (index + k - 1) % len(queue)
        result.append(queue.pop(index))

    return result


if __name__ == '__main__':
    n, k = map(int, input().split())

    result = solve(n, k)

    print(f'<{", ".join(map(str, result))}>')
