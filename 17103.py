# https://www.acmicpc.net/problem/17103
import sys


def prime_list(n):  # 0~n에서 소수인것에 False
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    rt = int(n ** 0.5)
    for i in range(2, rt + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False
    return sieve


t = int(sys.stdin.readline().strip())
primelist = prime_list(1000001)
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    cnt = 0
    for i in range(2, n // 2 + 1):
        if primelist[i] and primelist[n - i]:
            cnt += 1
    print(cnt)
