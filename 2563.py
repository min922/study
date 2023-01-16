# https://www.acmicpc.net/problem/2563
import sys

n = int(sys.stdin.readline().strip())
paper = [[0 for i in range(100)] for j in range(100)] # 전체 도화지

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    for i in range(data[0], data[0] + 10):
        for j in range(data[1], data[1] + 10):
            paper[i][j] = 1 # 색칠한 곳을 1로

result = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1: # 만약 색칠되어있다면
            result += 1 # 넓이로 count

print(result)
