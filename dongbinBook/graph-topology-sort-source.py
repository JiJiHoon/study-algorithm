# 위상정렬이란? 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
# 예: 수강신청 시 선수과목 지정
# a b c 과목이 있을 때 c 과목의 선수과목이 a, b 이면 위상 정렬은 a -> b -> c or b -> a -> c 가 된다.

# 개념: 
# 1. 진입차수가 0인 노드를 큐에 넣는다. 
# 2. 큐가 빌 때까지 다음 과정을 반복
#   2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#   2-2. 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.

from collections import deque

# 노드의 개수 v, 간선의 개수 e
v, e = map(int, input().split())
indegree = [0] * (v + 1) # 진입 차수 리스트
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입차수 증가시킴

def topology_sort(graph, indegree):
    result = []
    q = deque()

    for i in range(1, v + 1): # 진입차수가 0인 노드를 큐에 담음
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]: # 해당 노드에 연결된 노드들의 진입차수에서 -1 
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in result: # 결과 출력
        print(i, end=' ')

topology_sort(graph, indegree)