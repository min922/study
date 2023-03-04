# https://www.acmicpc.net/problem/11660
import sys

n, m = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

presum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + data[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(presum[x2][y2] - presum[x2][y1 - 1] - presum[x1 - 1][y2] + presum[x1 - 1][y1 - 1])
