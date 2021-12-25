# 떡볶이 떡 만들기

# 나의 풀이
import sys


def binaryRiceCakeCutter(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sums = sum(map(lambda x: x - mid if x > mid else 0, arr))
        if target == sums:
            return mid
        elif target > sums:
            end = mid - 1
        else:
            start = mid + 1
            result = mid # 만족하는 값 저장해두기
    return result

n, m = map(int, input().split())
riceCakes = list(map(int, sys.stdin.readline().rstrip().split()))

print(binaryRiceCakeCutter(riceCakes, m, 0, max(riceCakes)))



# 해설
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m: 
        end = mid - 1
    # total == m인 경우를 따로 처리하지 않았다. 
    # 생각해보니 값이 딱 맞는다면 다음 연산에서 더 작을 것이고 그럼 end 가 start보다 작아지므로 while문을 탈출할 것! 
    # 고작 연산 한번 더 하는 것이다.
    else:             
        result = mid  # 해설과 동일한 생각을 했다!
        start = mid + 1

print(result)