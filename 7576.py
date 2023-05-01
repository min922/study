# https://www.acmicpc.net/problem/7576
import sys
from collections import deque


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:  # 토마토가 심어져있으면
                queue.append([i, j])  # 큐에 추가
    # 토마토가 심어진 모든 위치를 큐에 한번에 추가하고 시작
    while queue:
        p, q = queue.popleft()
        for i in range(4):
            dp = p + dx[i]
            dq = q + dy[i]
            if 0 <= dp < n and 0 <= dq < m and tomato[dp][dq] == 0:
                tomato[dp][dq] = tomato[p][q] + 1
                queue.append([dp, dq])


m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

bfs()
result = 0
for row in tomato:
    for elt in row:
        if elt == 0:  # 토마토 못심은 곳이 하나라도 있으면
            print(-1)
            exit()
    result = max(result, max(row))
print(result - 1)
