def dfs(arr, visited, depth, num):
    visited.add(num)
    if depth == 2:
        return 
    for i in range(len(arr[num])):
        if arr[num][i] == 'Y':
            dfs(arr, visited, depth + 1, i)


n = int(input())

people = []
for _ in range(n):
    people.append(input())

maxCount = 0
for i in range(n):
    visited = set()
    dfs(people, visited, 0, i)
    maxCount = max(maxCount, len(visited) - 1)

print(maxCount)


# 다른 풀이
def get2Friend(arr, i):    
    visited = [0] * len(arr)
    for j in range(len(arr[i])):
        if arr[i][j] == 'Y':
            visited[j] = 1
            for k in range(len(arr[j])):
                if arr[j][k] == 'Y':
                    visited[k] = 1
    
    return visited.count(1)

n = int(input())

people = []
for _ in range(n):
    people.append(input())

maxCount = 0
for i in range(n):
    count = get2Friend(people, i) - 1
    maxCount = max(maxCount, count)

print(maxCount)
