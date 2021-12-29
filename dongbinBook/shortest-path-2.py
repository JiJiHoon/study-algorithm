# 전보

# 나의 풀이
import heapq

INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    fromNode, toNode, dist = map(int, input().split())
    graph[fromNode].append((toNode, dist))

def dijkstra(graph, start, end):
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, toNode = heapq.heappop(q)

        if distance[toNode] < dist:
            continue
                
        for node in graph[toNode]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (node[1], node[0]))

    return distance[end]

count = 0
result = 0
for i in range(1, n + 1):
    dist = dijkstra(graph, start, i)
    if dist != INF:
        count += 1
        result = max(result, dist)

print(count, result)


# 해설
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1) 

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance) # 시작 노드는 제외해야 함


# 나는 모든 경우에 대해 다익스트라 알고리즘을 수행해야 한다고 생각했었다. 사실은 다익스트라 한 번으로도 가능했다.
# 왜 모든 경우에 대해 다익스트라 알고리즘을 수행?
# -> 그리디하다는 생각이 하나의 목적지에 대한 경로만 구한다고 생각했다. -> 사실은 모든 목적지에 대해 구하고 선택하는 것이었다.
# -> 다익스트라 알고리즘과 플로이드 워셜 알고리즘의 차이를 다르게 생각했던것 같다.
# -> 다익스트라 알고리즘은 그리디 방식으로 거리를 구하고 플로이드 워셜 알고리즘은 다이나믹 프로그래밍을 이용한다.
# -> 다익스트라 알고리즘은 출발지가 정해져있지만, 플로이드 워셜 알고리즘은 모든 출발지를 고려한다. (이 점을 놓치고 있었다)
# -> 즉, 다익스트라 알고리즘은 출발지 1 - 목적지 n, 플로이드 워셜 알고리즘은 출발지 n - 목적지 n 이다.