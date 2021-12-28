# 미래 도시

# 나의 풀이
def mySolution():
    INF = int(1e9)

    n, m = map(int, input().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    for _ in range(m):
        fromNode, toNode = map(int, input().split())
        graph[fromNode][toNode] = 1
        graph[toNode][fromNode] = 1

    end, mid = map(int, input().split())

    start = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    if graph[start][mid] == INF or graph[mid][end] == INF:
        print(-1)
    else:
        print(graph[start][mid] + graph[mid][end])


# 해설
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1): # 왜 이렇게 했는지 잘 모르겠다.
        if a == b:
            graph[a][b] = 0 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)