import sys

sys.setrecursionlimit(10000)

t = int(input())

def dfs(board, visited, x, y, maxX, maxY):
    if (visited[y][x] == 1):
        return 0
    if (board[y][x] == 0):
        return 0

    visited[y][x] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= maxX or ny < 0 or ny >= maxY:
            continue
        if (visited[ny][nx] == 1):
            continue
        dfs(board, visited, nx, ny, maxX, maxY)
    
    return 1

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            result += dfs(board, visited, j, i, m, n)

    print(result)


## 두번쨰 풀이
import sys

sys.setrecursionlimit(10000)

t = int(input())

def dfs(board, x, y):
    if (board[y][x] == 0):
        return 0

    board[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board):
            continue
        dfs(board, nx, ny)
    
    return 1

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            result += dfs(board, j, i)

    print(result)
