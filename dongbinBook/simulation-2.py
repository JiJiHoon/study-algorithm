# 왕실의 나이트

# 나의 풀이
pos = input()

r = int(pos[1])
c = ord(pos[0]) - ord('a') + 1

moves = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

result = 0

for move in moves:
    tempR = r + move[0]
    tempC = c + move[1]

    if tempR >= 1 and tempR <= 8 and tempC >= 1 and tempC <= 8:
        result += 1

print(result)


# 해설
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 튜플 사용!

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)