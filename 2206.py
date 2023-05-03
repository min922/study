# https://www.acmicpc.net/problem/2206
import sys
from collections import deque


def bfs(x, y, z):
    queue = deque([[x, y, z]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        p, q, r = queue.popleft()
        if p == n-1 and q == m-1:
            return visited[p][q][r]
        for i in range(4):
            dp = p + dx[i]
            dq = q + dy[i]
            if 0 <= dp < n and 0 <= dq < m: # 범위안에 있고
                if maze[dp][dq] == 1 and r == 0: # 다음이 벽이고 벽 뚫을 수 있을때
                    visited[dp][dq][1] = visited[p][q][0] + 1
                    queue.append([dp, dq, 1]) # 벽 뚫었다고 표시
                elif maze[dp][dq] == 0 and visited[dp][dq][r] == 0: # 다음으로 갈수있고 방문한적 없을때
                    visited[dp][dq][r] = visited[p][q][r] + 1
                    queue.append([dp, dq, r])
    return -1


n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 세번째 좌표에 벽을 뚫었는지 여부를 저장
visited[0][0][0] = 1
print(bfs(0, 0, 0))
