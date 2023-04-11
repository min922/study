# https://www.acmicpc.net/problem/2903
import sys

n = int(sys.stdin.readline().strip())

tmp = [3]
while len(tmp) < n:
    tmp.append(tmp[-1] * 2 - 1)
print(tmp[-1] ** 2)
