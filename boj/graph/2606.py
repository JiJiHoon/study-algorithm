n = int(input())
connectionCount = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(connectionCount):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs solution
visited = []
def dfs(node):
    visited.append(node)
    for nextNode in graph[node]:
        if nextNode not in visited:
            dfs(nextNode)

dfs(1)
print(len(visited) - 1)

# bfs solution
def bfs(graph, node):
    queue = [node]
    visited = []
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.append(node)
        for nextNode in graph[node]:
            queue.append(nextNode)
    
    return len(visited) - 1

print(bfs(graph, 1))