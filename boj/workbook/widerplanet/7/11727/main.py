import sys

input = sys.stdin.readline


def solve(data):
    if data == 1:
        return 1

    a, b = 1, 3

    for _ in range(3, data + 1):
        a, b = b, (a * 2 + b) % 10007

    return b


if __name__ == '__main__':
    n = int(input())

    result = solve(n)

    print(result)
