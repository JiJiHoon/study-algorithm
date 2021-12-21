# 게임 개발

# 나의 풀이
def mySolution():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    # d 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    visitedBlock = []
    visitedBlock.append((r, c))

    while True:
        originDirection = d
        originR = r
        originC = c

        for _ in range(len(steps)):
            d = (d + 3) % 4
            nextR = r + steps[d][0]
            nextC = c + steps[d][1]

            if board[nextR][nextC] == 1:
                continue
            if (nextR, nextC) in visitedBlock:
                continue

            r = nextR
            c = nextC
            visitedBlock.append((nextR, nextC))
            break

        if d == originDirection and r == originR and c == originC:
            back = (d + 2) % 4
            nextR = r + steps[back][0]
            nextC = c + steps[back][1]

            if board[nextR][nextC] == 1:
                break
            r = nextR
            c = nextC

    print(len(visitedBlock))




# 해설
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장할 용도의 맵.

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 위치 방문 체크

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): # 왼쪽으로 회전하는 경우를 함수로 작성했음
    global direction # 전역 변수를 사용했는데, 이 부분은 좀 마음에 안든다
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0 # 몇 번 회전했는지 확인하는 변수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0: # 가보지 않았고, 육지인 경우
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4: # 개인적으로 이 조건문을 while 문 최상단에 배치했으면 어땠을까 하는 생각이 있다. while문 break 조건을 최상단에 위치하고 싶은 마음
        nx = x - dx[direction]
        ny = y - dx[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else: # 뒤로 가지 못하는 경우
            break
        turn_time = 0

print(count)

# 반복문 하나로 처리했다.
# 새로운 맵을 만들어 방문 위치를 기록했다
# 