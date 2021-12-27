# 1로 만들기

# 나의 풀이
def mySolution():
    MAX_NUM = 30000

    arr = [0] * (MAX_NUM + 1)

    for i in range(2, MAX_NUM + 1):
        if i % 5 == 0:
            arr[i] = min(arr[i // 5] + 1, arr[i - 1] + 1)
        elif i % 3 == 0:
            arr[i] = min(arr[i // 3] + 1, arr[i - 1] + 1)
        elif i % 2 == 0:
            arr[i] = min(arr[i // 2] + 1, arr[i - 1] + 1)
        else:
            arr[i] = arr[i - 1] + 1

    print(arr[int(input())])

mySolution()


# 해설
x = int(input())
d = [0] * 30001

for i in range(2, x + 1): # 굳이 전체를 할 필요가 없었다.
    d[i] = d[i - 1] + 1 # 나의 arr[i - 1] + 1은 중복 연산이 발생

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:                         # 순서를 바꾸고 elif를 사용했다면 비교가 적지 않았을까?
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])