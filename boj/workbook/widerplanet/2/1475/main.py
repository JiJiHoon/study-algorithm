import math
import sys

input = sys.stdin.readline


def solve(data):
    number_counts = count(data)

    number_counts[6] = math.ceil((number_counts[6] + number_counts[9]) / 2)
    number_counts[9] = 0

    return max(number_counts)


def count(num):
    counter = [0] * 10

    temp = num
    while temp > 0:
        number = temp % 10
        temp //= 10
        counter[number] += 1

    return counter


if __name__ == '__main__':
    num = int(input())

    print(solve(num))
