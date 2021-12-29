# 다익스트라 알고리즘은 a to b 의 최단경로를 구한다.

# 간단한 dijkstra 
from heapq import heappop


def simpleDijkstra():
    import sys

    input = sys.stdin.readline
    INF = int(1e9)

    # 노드의 개수 n, 간선의 개수 m
    n, m = map(int, input().split())
    # 시작 노드 번호
    start = int(input())

    graph = [[] for _ in range(n + 1)] # 노드에 연결되어있는 노드 정보를 담기 위한 리스트
    visited = [False] * (n + 1) # 방문 리스트
    distance = [INF] * (n + 1) # 최단 거리 테이블

    for _ in range(m):
        fromNode, toNode, dist = map(int, input().split()) # fromNode에서 toNode로 가는 비용이 distance
        graph[fromNode].append((toNode, dist))

    def getSmallestNode():
        minValue = INF
        index = 0
        for i in range(1, n + 1):
            if distance[i] < minValue and not visited[i]:
                minValue = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0 # 시작 노드 초기화
        visited[start] = True
        for j in graph[start]: # j = (toNode, dist)
            distance[j[0]] = j[1]
        
        for _ in range(n - 1): # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
            now = getSmallestNode() # 최단거리 노드를 선택
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstra(start)

# 개선된 dijkstra
def improvedDijkstra():
    import heapq
    import sys

    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(n + 1)] # 노드에 연결되어있는 노드 정보를 담기 위한 리스트
    distance = [INF] * (n + 1) # 최단 거리 테이블

    for _ in range(m):
        fromNode, toNode, dist = map(int, input().split()) # fromNode에서 toNode로 가는 비용이 distance
        graph[fromNode].append((toNode, dist))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist: 
                continue
            for i in graph(now):
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(start)