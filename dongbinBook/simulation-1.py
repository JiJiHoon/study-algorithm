# 상하좌우

# 나의 풀이
n = int(input())
commands = input().split()

pos = [1, 1] # [row, col]

for command in commands:
    if command == 'L':
        pos[1] = max(1, pos[1] - 1)
    elif command == 'R':
        pos[1] = min(n, pos[1] + 1)
    elif command == 'U':
        pos[0] = max(1, pos[0] - 1)
    elif command == 'D':
        pos[0] = min(n, pos[0] + 1)

print(pos[0], pos[1])


# 해설
n = int(input())
x, y = 1, 1 # x, y를 따로 지정했다. 
plans = input().split()

# 이동 방향을 따로 지정해줬다. 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)): #  switch 문을 반복문으로 만들었다. -> 배열만 관리하면 된다. 유지보수 용이
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

# 배워야 할 점: 좌표이동에 대한 부분을 배열로 관리하였다. 이로인해 if문 대신 for문으로 처리가 가능하다.