# 숫자 카드 게임

# 나의 풀이
n, m = map(int, input().split())

maxNum = 0
# 행을 하나씩 읽어와 각 행의 최소값을 추출하고 maxNum보다 크면 maxNum에 대입한다.
for _ in range(n):
    row = list(map(int, input().split()))
    minNumInRow = min(row)
    if minNumInRow > maxNum:
        maxNum = minNumInRow

print(maxNum)


# 해설
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value) # if 문을 사용하는 것보다 max를 사용하는 것이 더 가독성에 좋다고 생각. 하지만 if문을 사용하면 대입을 최소화 할 수 있다.

print(result)

