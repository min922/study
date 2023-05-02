# https://www.acmicpc.net/problem/7569
import sys
from collections import deque


def bfs():
    dx = [0, 0, 0, 0, 1, -1]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 1, -1, 0, 0]
    queue = deque([])
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 1:
                    queue.append([i, j, k])
    # 토마토가 심어진 모든 위치를 큐에 한번에 추가하고 시작
    while queue:
        p, q, r = queue.popleft()
        for i in range(6):
            dp = p + dx[i]
            dq = q + dy[i]
            dr = r + dz[i]
            if 0 <= dp < h and 0 <= dq <n and 0 <= dr < m and tomato[dp][dq][dr] == 0:
                tomato[dp][dq][dr] = tomato[p][q][r] + 1
                queue.append([dp, dq, dr])


m, n, h = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

bfs()
result = 0
for floor in tomato:
    for row in floor:
        if 0 in row:
            print(-1)
            exit()
        result = max(result, max(row))

print(result - 1)
