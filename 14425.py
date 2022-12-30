# https://www.acmicpc.net/problem/14425
import sys

def sol(elt, S):
    if elt in S:
        return 1
    return 0

n, m = map(int, sys.stdin.readline().strip().split())
S = [sys.stdin.readline().strip() for i in range(n)]
search = [sys.stdin.readline().strip() for i in range(m)]
result = 0

for elt in search:
    result += sol(elt, S)
print(result)
