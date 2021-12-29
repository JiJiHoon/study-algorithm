# 신장 트리란? 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘이란? 모든 노드를 최소한의 비용으로 연결하는 알고리즘
# 개념 -> 1. 간선을 비용 오름차순으로 정렬한다. 2. 사이클(이미 처리된 간선)인 경우 무시한다.
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    aParent = findParent(parent, a)
    bParent = findParent(parent, b)

    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

v, e = map(int , input().split())

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

edges = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append(a, b, cost)

edges.sort(key=lambda x: x[2]) # 간선을 비용 순으로 정렬


result = 0
for edge in edges:
    a, b, cost = edge
    if findParent(parent, a) != findParent(parent, b): # 사이클이 발생하지 않으면 집합에 추가
        unionParent(parent, a, b)
        result += cost # 간선 비용 합

print(result)