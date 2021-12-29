# 팀 결성

# 나의 풀이
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    aParent = findParent(parent, a)
    bParent = findParent(parent, b)

    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent


n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 0:
        union(parent, a, b)
    elif command == 1:
        if findParent(parent, a) == findParent(parent, b):
            print("YES")
        else:
            print("NO")

# 해설과 일치하여 해설 생략