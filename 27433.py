# https://www.acmicpc.net/problem/27433
import sys


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)


n = int(sys.stdin.readline().strip())
print(fac(n))
