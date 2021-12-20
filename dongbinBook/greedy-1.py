# 큰 수의 법칙

# 나의 풀이
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

maxNum = 0
subMaxNum = 0

# 제일 큰 수와 두번째로 큰 수를 O(N)으로 구하기
for num in nums:
    if num > maxNum:
        subMaxNum = maxNum
        maxNum = num
    elif num > subMaxNum:
        subMaxNum = num

result = (m // (k + 1)) * (k * maxNum + subMaxNum) + (m % (k + 1)) * maxNum
print(result)


# 해설
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

maxNum = 0
subMaxNum = 0

# 정렬을 이용하여 제일 큰 수와 두번째로 큰 수를 구했다
data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수를 계산 했다. 변수로 저장하여 사용한느 것이 가독성에 더 좋다.
count = int(m / (k + 1)) * k 
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second # 전체 갯수에서 나머지를 빼는 방식이 더 확실하다.

print(result)