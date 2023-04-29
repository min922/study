# https://www.acmicpc.net/problem/2178
import sys
from collections import deque


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([[x, y]])
    while queue:
        p, q = queue.popleft()
        for i in range(4):
            dp = p + dx[i]
            dq = q + dy[i]
            if 0 <= dp < n and 0 <= dq < m and maze[dp][dq] == 1:  # 갈 수 있고 방문 하지 않은데(방문한 데는 1 이상)
                maze[dp][dq] = maze[p][q] + 1  # 전까지 방문한 칸 수에 한 칸 더 추가
                queue.append([dp, dq])


n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
bfs(0, 0)
print(maze[n - 1][m - 1])
