import sys 
input = sys.stdin.readline

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    aP = find(parent, a)
    bP = find(parent, b)

    if aP == bP:
        return
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
    union(parent, a, b)

count = 0
for i in range(1, n + 1):
    if parent[i] == i:
        count += 1

print(count)


# dfs 로 풀기
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

visited = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1, n + 1):
    if visited[i] != 0:
        continue

    count += 1
    stack = []
    stack.append(i)
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            for node in graph[now]:
                stack.append(node)

print(count)