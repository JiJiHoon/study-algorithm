import sys
from collections import deque

input = sys.stdin.readline


def solve(data):
    queue = deque([i for i in range(1, data + 1)])

    result = []

    while True:
        result.append(queue.popleft())
        if len(queue) == 0:
            break
        queue.rotate(-1)

    return result


if __name__ == '__main__':
    n = int(input())

    result = solve(n)

    print(" ".join(map(str, result)))
