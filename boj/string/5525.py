n = int(input())
leng = int(input())
s = input()

count = 0
patternCount = n
i = 0
while i < leng - 2:
    if s[i: i + 3] == 'IOI':
        patternCount -= 1
        if patternCount == 0:
            patternCount += 1
            count += 1
        i += 2
    else:
        i += 1
        patternCount = n
print(count)

# 다른 사람의 풀이
n = int(input())
input()
s = input()

s = s.replace('IO', 'X')
s = s.replace('XI', 'XXO') # 이렇게 바꾸면 겹쳐도 문제가 안된다 (위에서 IO를 미리 바꿨기 때문)
s = s.replace('I', 'O')

count = 0
for sub in s.split('O'):
    if len(sub) - n > 0: # X의 개수 - n
        count += len(sub) - n

print(count)