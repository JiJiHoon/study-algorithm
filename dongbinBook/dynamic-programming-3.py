# 바닥 공사

# 나의 풀이
def mySolution():
    n = int(input())

    arr = [0] * 1000
    arr[0] = 1
    arr[1] = 3
    
    for i in range(2, n):
        arr[i] = (arr[i - 1] + 2 * arr[i - 2]) % 796796

    print(arr[n - 1])

# 해설
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])