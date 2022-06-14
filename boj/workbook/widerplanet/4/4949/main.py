import sys

input = sys.stdin.readline


def solve(data):
    bracket_stack = []

    for char in data:
        if char == '(':
            bracket_stack.append('(')
        if char == ')':
            if len(bracket_stack) == 0 or bracket_stack.pop() == '[':
                return 'no'

        if char == '[':
            bracket_stack.append('[')
        if char == ']':
            if len(bracket_stack) == 0 or bracket_stack.pop() == '(':
                return 'no'

    if len(bracket_stack) > 0:
        return 'no'

    return 'yes'


if __name__ == '__main__':
    while True:
        data = input().rstrip()
        if data == '.':
            break

        print(solve(data))
