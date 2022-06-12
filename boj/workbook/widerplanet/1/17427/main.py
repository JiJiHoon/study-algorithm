import sys

input = sys.stdin.readline


def solve(data):
    result = 0

    for i in range(1, data + 1):
        result += i * (data // i)

    return result


if __name__ == '__main__':
    num = int(input())

    print(solve(num))
