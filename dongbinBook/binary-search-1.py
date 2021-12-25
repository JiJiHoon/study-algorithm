# 부품 찾기

# 나의 풀이
import sys


def bianrySearch(arr, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return bianrySearch(arr, target, mid + 1, end)
    else:
        return bianrySearch(arr, target, start, mid - 1)

n = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
partNums = list(map(int, sys.stdin.readline().rstrip().split()))

parts.sort()

for num in partNums:
    if bianrySearch(parts, num, 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 해설 (이진 탐색)
def binary_search(array, target, start, end): # 재귀가 아닌 반복문을 이용했음
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = bianrySearch(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 해설 (계수 정렬)
n = int(input())
array = [0] * 1000001

for i in input().split(): # 배열의 위치로 기록
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 해설 (집합)
n = int(input())
set = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in set:
        print('yes', end=' ')
    else:
        print('no', end=' ')