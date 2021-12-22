# 음료수 얼려먹기

# 나의 풀이 (2021.12.22)
n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
iceBox = []


for _ in range(n):
    iceBox.append(list(map(int, list(input()))))

print(iceBox)

def myDfs1(iceBox, row, col, visited, count):
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]

    visited[row][col] = 1

    if iceBox[row][col] == 1:
        for i in range(len(dCol)):
            nRow = row + dRow[i]
            nCol = col + dCol[i]

            if nRow < 0 or nRow >= n:
                continue
            if nCol < 0 or nCol >= m:
                continue
            if visited[nRow][nCol] == 1:
                continue
            count = myDfs1(iceBox, nRow, nCol, visited, count)
        return myDfs1(iceBox, nRow, nCol, visited, count)

    stack = []
    while True:
        print(visited)
        for i in range(len(dCol)):
            nRow = row + dRow[i]
            nCol = col + dCol[i]

            if nRow < 0 or nRow >= n:
                continue
            if nCol < 0 or nCol >= m:
                continue
            if visited[nRow][nCol] == 1:
                continue
            stack.append((nRow, nCol))
        

        row, col = stack.pop()
        visited[row][col] = 1

        if len(stack) == 0:
            break
    
    return count + 1

print(myDfs1(iceBox, 0, 0, visited, 0))
# 시간부족으로 해결하지 못했음



# 해설
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 비정상 좌표이면 탈출
        return False
    
    if graph[x][y] == 0: # 방문하지 않았던 노드라면 상, 하, 좌, 우 호출하고 반환
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True    
    return False

result = 0
for i in range(n): # 모든 좌표를 조회
    for j in range(m):
        if dfs(i, j) == True: # 처음 방문했으면 count 추가 -> dfs로 연결된 노드들을 모두 방문하여 방문 처리를 했기 때문에 중복해서 카운팅 될 일이 없음!!!
            result += 1

print(result)