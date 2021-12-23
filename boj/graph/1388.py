n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input()))

visited = [[0] * m for _ in range(n)]

def dfs(row, col, char):
    if col < 0 or col >= m or row < 0 or row >= n:
        return 0
    if board[row][col] != char:
        return 0
    if visited[row][col] != 0:
        return 0

    visited[row][col] = 1
    if char == '-':
        dfs(row, col - 1, char)
        dfs(row, col + 1, char)
    else:
        dfs(row - 1, col, char)
        dfs(row + 1, col, char)
    
    return 1

result = 0
for i in range(n):
    for j in range(m):
        result += dfs(i, j, board[i][j])
print(result)