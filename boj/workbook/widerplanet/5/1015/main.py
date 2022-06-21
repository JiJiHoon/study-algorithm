import sys

input = sys.stdin.readline


def solve(data):
    data = list(enumerate(data))
    data.sort(key=lambda x: x[1])

    data = list(enumerate(data))
    data.sort(key=lambda x: x[1][0])

    result = [data[i][0] for i in range(len(data))]

    return result


if __name__ == '__main__':
    _ = input()
    nums = list(map(int, input().split()))

    result = solve(nums)

    print(" ".join(map(str, result)))
