import sys

input = sys.stdin.readline


def solve(n):
    arr = [0] * (n + 1)
    return solve_recursive(arr, n)


def solve_recursive(arr, n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    arr[n] = min(solve_recursive(arr, n // 2) + n % 2, solve_recursive(arr, n // 3) + n % 3) + 1

    return arr[n]


if __name__ == '__main__':
    n = int(input())

    result = solve(n)

    print(result)
