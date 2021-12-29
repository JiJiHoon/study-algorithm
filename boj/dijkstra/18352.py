import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

distanceList = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    fromNode, toNode = map(int, input().split())

    graph[fromNode].append(toNode)

q = []
heapq.heappush(q, (0, x))
distanceList[x] = 0

while q:
    dist, node = heapq.heappop(q)

    if distanceList[node] > dist:
        continue

    for i in graph[node]:
        cost = dist + 1
        if cost < distanceList[i]:
            distanceList[i] = cost
            heapq.heappush(q, (cost, i))

result = [i for i, x in enumerate(distanceList) if x == k]

if len(result) == 0:
    print(-1)
else:
    print("\n".join(map(str, result)))