# https://www.acmicpc.net/problem/3003
import sys

data = list(map(int, sys.stdin.readline().split()))
std = [1, 1, 2, 2, 2, 8]
for i in range(len(data)):
    print(std[i] - data[i], end=' ')
