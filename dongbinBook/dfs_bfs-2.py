# 미로 탈출

# 나의 풀이1 (2021.12.22)

def mySolution1():
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))

    queue = []
    nextQueue = []
    depth = 1
    row = 0
    col = 0
    while True:
        if row == n - 1 and col == m - 1:
            break

        if row < 0 or row >= n or col < 0 or col >= m:
            pass
        elif maze[row][col] == 1:
            nextQueue.append((row + 1, col))
            nextQueue.append((row - 1, col))
            nextQueue.append((row, col + 1))
            nextQueue.append((row, col - 1))
            maze[row][col] = 0

        if len(queue) == 0:
            queue = nextQueue
            nextQueue = []
            depth += 1
        row, col = queue.pop(0)

    print(depth)

# 해설
def solution():
    from collections import deque

    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque() # queue 사용을 위해 deque 라이브러리 사용
        queue.append(x, y)

        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1 # 지도에 depth를 표시!! 문제가 오른쪽 아래로만 진행하기 때문에 가능
                    queue.append(nx, ny)
        
        return graph[n - 1][m - 1]
    
    print(bfs(0, 0))

# depth를 지도에 표시하는 것을 생각하지 못했다. 
# deque 라이브러리 사용