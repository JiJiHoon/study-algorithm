import sys

input = sys.stdin.readline


def solve(data):
    result = []

    for inputNumber in data:
        num = 1
        count = 1
        while True:
            if num % inputNumber == 0:
                break
            num *= 10
            num += 1
            count += 1
        result.append(count)

    return result


if __name__ == '__main__':
    data = []
    while True:
        line = input()
        if not line:
            break
        data.append(int(line))

    result = solve(data)

    print("\n".join(map(str, result)))
