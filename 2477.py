# https://www.acmicpc.net/problem/2477
import sys

k = int(sys.stdin.readline().strip())
direction = []
dist = []
for i in range(6):
    key, item = map(int, sys.stdin.readline().split())
    direction.append(key)
    dist.append(item)

area = 1
for idx in range(6): # 제일 큰 직사각형 넓이
    if direction.count(direction[idx]) == 1:
        area *= dist[idx]

small = [[3, 2], [1, 3], [2, 4], [4, 1]]
if [direction[-1], direction[0]] in small: # 제외해야하는 직사각형 넓이
    area -= dist[-1] * dist[0]
else:
    for idx in range(5):
            if [direction[idx], direction[idx+1]] in small:
                area -= dist[idx] * dist[idx+1]

print(area * k)
