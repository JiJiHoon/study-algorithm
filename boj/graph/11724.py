
def getParent(parent, a):
    if parent[a] != a:
        parent[a] = getParent(parent, parent[a])
    return parent[a]

def composeParent(parent, a, b):
    aP = getParent(parent, a)
    bP = getParent(parent, b)

    if aP < bP:
        parent[bP] = aP
    else:
        parent[aP] = bP



n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if getParent(parent, a) == getParent(parent, b):
        continue
    composeParent(parent, a, b)

parentSet = set()
for i in range(1, n + 1):
    parentSet.add(parent[i])

print(len(parentSet))