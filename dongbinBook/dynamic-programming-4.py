# 효율적인 화폐 구성

# 나의 풀이
import sys

def mySolution():
    n, m = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    dp = [-1] * (10001)
    for coin in coins:
        dp[coin] = 1

    for i in range(1, m + 1):
        for coin in coins:
            if dp[i - coin] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i - coin] + 1
                else:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

    print(dp[m])

mySolution()


# 해설
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1) # dp 테이블을 문제에서 존재할 수 있는 최대값 + 1으로 초기화

d[0] = 0
for i in range(n): # 나와 반대로 for문을 구성했음
    for j in range(array[i], m + 1):
        # if d[j - array[i]] != 10001: # 이 로직은 필요 없다. 아래 min에서 공통처리가 가능하기 때문
        d[j] = min(d[j], d[j - array[i]] + 1) # 거스름이 가능한지 

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
