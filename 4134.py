# https://www.acmicpc.net/problem/4134 
import sys, math


def findprime(p):
    if p == 0 or p == 1:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False  # p가 소수가 아니면 False
    return True  # p가 소수이면 True


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    while True:
        if findprime(n):
            print(n)
            break
        else:
            n += 1
