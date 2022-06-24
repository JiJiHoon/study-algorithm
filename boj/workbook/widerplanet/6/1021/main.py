import sys

input = sys.stdin.readline


def solve1(n, m, data):
    index_dict = {}

    result = 0
    for i in range(n):
        index_dict[i + 1] = i

    for i in range(m):
        num = data[i]
        if index_dict[num] == 0:
            del index_dict[num]
            for key in index_dict:
                index_dict[key] -= 1
        else:
            temp = index_dict[num]
            if index_dict[num] <= len(index_dict) // 2:
                for key in index_dict:
                    index_dict[key] = (index_dict[key] - temp - 1) % len(index_dict)
                result += temp
            else:
                for key in index_dict:
                    index_dict[key] = (index_dict[key] - temp - 1) % len(index_dict)
                result += len(index_dict) - temp
            del index_dict[num]

    return result


def solve(n, m, data):
    result = 0

    array = [i for i in range(1, n + 1)]

    for i in range(m):
        idx = array.index(data[i])

        result += min(len(array[:idx]), len(array[idx:]))
        array = array[idx + 1:] + array[:idx]

    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    result = solve(n, m, nums)

    print(result)
