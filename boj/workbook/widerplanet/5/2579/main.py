import sys

input = sys.stdin.readline


def solve(data):
    if len(data) == 1:
        return data[0]
    n = len(data)

    one_step = [0] * n
    two_step = [0] * n

    one_step[0] = data[0]
    one_step[1] = data[0] + data[1]
    two_step[1] = data[1]

    for i in range(2, n):
        one_step[i] = two_step[i - 1] + data[i]
        two_step[i] = max(one_step[i - 2], two_step[i - 2]) + data[i]

    return max(one_step[n - 1], two_step[n - 1])


if __name__ == '__main__':
    n = int(input())
    array = [int(input()) for _ in range(n)]

    result = solve(array)

    print(result)
