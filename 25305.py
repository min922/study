# https://www.acmicpc.net/problem/25305
import sys

N, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)
print(data[k-1])
