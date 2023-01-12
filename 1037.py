# https://www.acmicpc.net/problem/1037
def realcommondiv(numlist):
    maxnum = max(numlist)
    minnum = min(numlist)
    return maxnum * minnum

import sys
n = int(sys.stdin.readline().strip())
numlist = list(map(int, sys.stdin.readline().split()))
print(realcommondiv(numlist))
