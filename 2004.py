# https://www.acmicpc.net/problem/2004
import sys

n, r = map(int, sys.stdin.readline().split())


def factor(n, a):  # n!에 a가 몇 번 곱해져있는지 판별
    cnt = 0
    while n != 0:
        n = n // a
        cnt += n
    return cnt


cnt2 = factor(n, 2) - factor(r, 2) - factor(n - r, 2) # n! / r! * (n-r)!
cnt5 = factor(n, 5) - factor(r, 5) - factor(n - r, 5)

print(min(cnt2, cnt5))
