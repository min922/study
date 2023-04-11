# https://www.acmicpc.net/problem/2805
import sys

n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(height)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for h in height:
        if h - mid >= 0:
            cut += h - mid
            if cut > m: 
                break
    if cut >= m:
        start = mid + 1
    elif cut < m:
        end = mid - 1
print(end)
