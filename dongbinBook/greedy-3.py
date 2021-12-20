# 1이 될 때까지

# 나의 풀이
n, k = map(int, input().split())

count = 0
while n != 1:
    # n이 k로 나눠지면 나눈다. 이 로직을 우선적으로 처리해야 횟수가 최소가 된다.
    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1

print(count)

# 해설
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # n이 k로 나눠질 수 있는 수
    result += n - target # target까지 도달하기 위해 n -=1 작업을 수행할 횟수
    n = target # 실제로 n을 1 감소시키는 연산을 하지 않음!!

    if n < k: # 더이상 k로 나눠질 수 없는 경우 break
        break

    result += 1 # k로 나누기를 수행
    n //= k

result += (n - 1) # 더 이상 나눠지지 않는 경우 1을 만들어야 하기 때문에 1씩 감소시키는 연산 횟수를 더해준다
print(result)

# 배워야 할 점: n -=1 연산을 수행하지 않고 문제를 해결하였다. 앞으로 수식으로 대체할 수 있는 불필요한 연산들을 생각해보자.