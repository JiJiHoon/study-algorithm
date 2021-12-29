# 서로소 집합 알고리즘 소스코드

# 간단 버전
def findParent(parent, x):
    if parent[x] != x:
        x = findParent(parent, parent[x])

    return x

# 개선 버전 (경로 압축)(부모 노드를 루트 노드로 변경) 
def findParent2(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x]) # 부모 노드를 루트 노드로 설정

    return parent[x]


def unionParent(parent, a, b):
    aParent = findParent(parent, a)
    bParent = findParent(parent, b)

    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

# 노도의 개수v, 간선의 개수 e
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블

# 각 노드의 부모를 자기 자신으로 설정
for i in range(1, v + 1):
    parent[i] = i

# union 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    unionParent(parent, a, b)


# 무방향 그래프에서 사이클 판별 가능
for _ in range(e):
    a, b = map(int, input().split())
    if findParent(parent, a) == findParent(parent, b): # 루트 노드가 같다는 의미는? 이미 다른 경로로 union 연산이 수행되었다!
        cycle = True
        break
    unionParent(parent, a, b)