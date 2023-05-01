# https://www.acmicpc.net/problem/7562
import sys
from collections import deque


def bfs(x, y):
    queue = deque([[x, y]])
    dx = [1, 2, 1, 2, -1, -2, -1, -2] # 이동할수 있는 위치
    dy = [2, 1, -2, -1, -2, -1, 2, 1]
    while queue:
        p, q = queue.popleft()
        if p == wtgx and q == wtgy: # 도착했을때
            return chess[p][q]
        for i in range(8):
            dp = p + dx[i]
            dq = q + dy[i]
            if 0 <= dp < l and 0 <= dq < l and chess[dp][dq] == 0:
                chess[dp][dq] = chess[p][q] + 1
                queue.append([dp, dq])


t = int(sys.stdin.readline().strip())

for _ in range(t):
    l = int(sys.stdin.readline().strip())
    nowx, nowy = map(int, sys.stdin.readline().split())
    wtgx, wtgy = map(int, sys.stdin.readline().split())

    chess = [[0] * l for _ in range(l)]
    print(bfs(nowx, nowy))
