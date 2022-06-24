import sys

input = sys.stdin.readline


def solve(data):
    result = []

    min_num = 10000000000
    max_num = 0
    for i in range(len(data)):
        min_num = min(min_num, data[i])
        max_num = max(max_num, data[i] - min_num)
        result.append(max_num)

    return result


if __name__ == '__main__':
    input()

    nums = list(map(int, input().split()))

    result = solve(nums)

    print(" ".join(map(str, result)))
