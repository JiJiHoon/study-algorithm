import sys

input = sys.stdin.readline

croatia_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


def solve(data):
    count = 0
    length = len(data)

    i = 0
    while i < length:
        is_croatia_alphabet = False
        alphabet_length = 0

        for alphabet in croatia_alphabets:
            if i + len(alphabet) - 1 >= length:
                continue

            if data[i:i + len(alphabet)] == alphabet:
                alphabet_length = len(alphabet)
                is_croatia_alphabet = True
                break

        i += alphabet_length if is_croatia_alphabet else 1

        count += 1

    return count


if __name__ == '__main__':
    word = input().strip()

    print(solve(word))
