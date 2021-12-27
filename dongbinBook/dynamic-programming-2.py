# 개미 전사

# 나의 풀이
def mySolution():
    n = int(input())
    arr = list(map(int, input().split()))
    maxDp = [0] * n

    for i in range(n):
        if i < 2:
            maxDp[i] = arr[i]
        
        maxDp[i] = max(maxDp[i - 1], maxDp[i - 2] + arr[i])

    print(maxDp[n - 1])

# 해설
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0] # if문 대신 직접 대입했다. for문 안에 if문이 들어가지 않으니 효율적이다.
d[1] = array[1]

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])