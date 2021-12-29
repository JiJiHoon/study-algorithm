# 도시 분할 계획

# 나의 풀이
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    aParent = findParent(parent, a)
    bParent = findParent(parent, b)

    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])

result = 0
maxCost = 0
for edge in edges:
    a, b, cost = edge
    if findParent(parent, a) == findParent(parent, b):
        continue
    unionParent(parent, a, b)
    result += cost
    maxCost = cost

print(result - maxCost)


# 해설과 흐름이 일치하므로 해설 생략