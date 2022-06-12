import sys

input = sys.stdin.readline


def solve(m, n, x, y):
    nPrime = 1
    mPrime = 1
    year = 1
    while True:
        if x == mPrime and y == nPrime:
            return year
        if nPrime == n and mPrime == m:
            break
        nPrime = (nPrime % n) + 1
        mPrime = (mPrime % m) + 1
        year += 1

    return -1


def solve2(m, n, x, y):
    if x == 1 and y == 1:
        return 1
    if m == 1:
        return y
    if n == 1:
        return x

    lcm_ = lcm(m, n)

    if y == n:
        temp = x
        for i in range(lcm_ // m):
            if temp % n == 0:
                return temp
            temp += m
    else:
        temp = x
        for i in range(lcm_ // m):
            if temp % n == y:
                return temp
            temp += m
    return -1


def gcd(a, b):
    x, y = a, b

    if x < y:
        x, y = y, x
    while x % y != 0:
        x %= y
        if x < y:
            x, y = y, x
    return y


def lcm(a, b):
    return a * b // gcd(a, b)


def solve3(m, n, x, y):
    if x == 1 and y == 1:
        return 1
    gcd_, s, t = extendedEuclidianAlgorithm(m, n)

    # z = x (mod m) = y (mod n)
    if x % gcd_ != y % gcd_:  # 최대공약수로 나눈 나머지가 같아야한다.
        return -1
    #  참고: https://math.stackexchange.com/questions/1644677/what-to-do-if-the-modulus-is-not-coprime-in-the-chinese-remainder-theorem/1644698#1644698
    lcm_ = m * n // gcd_
    return (x - m * s * ((x - y) // gcd_)) % lcm_


# 확장 유클리드 알고리즘 https://joonas.tistory.com/25
# a, b에 대해 gcd와 gcd를 구성할 수 있는 해를 구할 수 있다.
def extendedEuclidianAlgorithm(a, b):
    s = (1, 0)
    t = (0, 1)
    r = (a, b)
    q = 0
    r_temp = r[0] % r[1]
    q = r[0] // r[1]
    while r_temp != 0:
        s = (s[1], s[0] - s[1] * q)
        t = (t[1], t[0] - t[1] * q)
        r = (r[1], r_temp)

        r_temp = r[0] % r[1]
        q = r[0] // r[1]

    gcd_ = r[1]
    return gcd_, s[1], t[1]


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        n, m, x, y = map(int, input().split())
        result = solve2(n, m, x, y)
        print(result)
