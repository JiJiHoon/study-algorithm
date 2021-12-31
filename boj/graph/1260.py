# DFS와 BFS
from collections import deque

def dfs(graph, visited, start):
    result = []
    visited[start] = 1
    result.append(start)

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and visited[i] == 0:
            result += dfs(graph, visited, i)

    return result


def bfs(graph, visited, start):
    result = []
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if visited[now] == 1:
            continue
        visited[now] = 1
        result.append(now)
        for i in range(len(graph[now])):            
            if graph[now][i] == 1:
                q.append(i)

    return result


n, m, start = map(int, input().split())
dfsVisitied = [0] * (n + 1)
bfsVisitied = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

print(" ".join(map(str, dfs(graph, dfsVisitied, start))))
print(" ".join(map(str, bfs(graph, bfsVisitied, start))))
