n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]

def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= n:
        return False
    if visited[row][col]:
        return False
    if graph[row][col] == -1:
        return True

    visited[row][col] = 1
    power = graph[row][col]

    return dfs(row + power, col) or dfs(row, col + power)

# if dfs(0, 0) == True:
#     print("HaruHaru")
# else:
#     print("Hing")


def bfs(row, col):
    queue = [(row, col)]

    while queue:
        row, col = queue.pop(0)

        if row < 0 or row >= n or col < 0 or col >= n:
            continue
        if visited[row][col]:
            continue
        if graph[row][col] == -1:
            return True
        
        visited[row][col] = 1
        power = graph[row][col]
        queue.append((row + power, col))
        queue.append((row, col + power))

    return False


if bfs(0, 0) == True:
    print("HaruHaru")
else:
    print("Hing")
