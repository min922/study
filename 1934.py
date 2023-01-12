# https://www.acmicpc.net/problem/1934
def lcm_Euclid(a, b):
    r = -1
    multi = a * b
    a, b = max(a, b), min(a, b)
    while r != 0:
        r = a % b # a를 b로 나눈 나머지
        a, b = b, r # gcd(a, b) = gcd(b, r) where a = b * q + r, q:int
    return multi // a # lcm(a, b) = a*b / gcd(a, b)

import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
for num in data:
    print(lcm_Euclid(num[0], num[1]))
