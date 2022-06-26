import re
import sys

input = sys.stdin.readline


class Trie:
    class Node:
        def __init__(self, char):
            self.char = char
            self.child = {}
            self.is_word = False

    def __init__(self):
        self.head = self.Node('')

    def add_word(self, word):
        node = self.head

        for char in word:
            if char not in node.child:
                node.child[char] = self.Node(char)
            node = node.child[char]

        node.is_word = True

    def is_exist_prefix(self, prefix):
        node = self.head

        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]

        return True


def solve(words, prefixes):
    count = 0

    trie = Trie()

    for word in words:
        trie.add_word(word)

    for prefix in prefixes:
        if trie.is_exist_prefix(prefix):
            count += 1

    return count


# brute-force with regex (time over)
def solve1(words, prefixes):
    count = 0

    for prefix in prefixes:
        pattern = rf'^{prefix}'
        for word in words:
            if re.search(pattern, word):
                count += 1
                break

    return count


# brute-force with str.startswith()
def solve2(words, prefixes):
    count = 0

    for prefix in prefixes:
        for word in words:
            if word.startswith(prefix):
                count += 1
                break

    return count


if __name__ == '__main__':
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]
    prefixes = [input().strip() for _ in range(m)]

    result = solve(words, prefixes)

    print(result)
