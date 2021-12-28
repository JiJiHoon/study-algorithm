# 플로이드 워셜 알고리즘
# D_ab = min(D_ab, D_ak + D_kb)
# a 에서 b로 가는 최소 비용은 a -> b 와, a -> k -> b 중 최소값이다.

INF = int(1e9)

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    graph[a][a] = 0 # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

# 각 간선에 대한 정보를 받아 테이블을 초기화
for _ in range(m):
    fromNode, toNode, dist = map(int, input().split())
    graph[fromNode][toNode] = dist

# 점화식에 따라 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

