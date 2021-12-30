# 커리큘럼

# 나의 풀이
from collections import deque

n = int(input())

# subject = [0] * (n + 1)
times = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
referenceCount = [0] * (n + 1)

for i in range(n):
    time, *array = map(int, input().split())
    array = list(array[:-1])

    times[i] = time
    for num in array:
        graph[i].append(num)

q = deque()
for i in range(1, n + 1):
    if referenceCount[i] == 0:
        q.append(i)

sortedList = []
while q:
    now = q.popleft()
    sortedList.append(now)

    for i in graph[now]:
        referenceCount[i] -= 1
        if referenceCount[i] == 0:
            q.append(i)

# for i in sortedList:
    # for 
# 실패했음
# 정렬후 재귀로 해결하려 했으나... 그럼 정렬하는 의미가 없음... 그냥 dfs 로 모든 시간을 구해버리는 것..





# 해설
from collections import deque
import copy

v = int(input())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int ,input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
    
def topology_sort(): # 정렬을 이용하지만 정렬된 결과를 사용하지 않는...! 정렬을 하면서 결과 값을 계산함
    result = copy.deepcopy(time) # 총 걸리는 시간을 저장하기 위해 딥카피 수행 (메모이제이션)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i]) # now가 선수과목이기 때문에 시간을 추가하는 곳은 now가 아니다...! 
            # 이렇게 할 수 있는 이유: 정렬을 수행했기 때문에 이후의 연산에 영향을 받지 않기 때문!!
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        
    for i in range(1, v + 1):
        print(result[i])

topology_sort()