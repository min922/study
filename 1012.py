# https://www.acmicpc.net/problem/1012
import sys
from collections import deque


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    graph[x][y] = 0  # 방문 표시
    queue = deque([[x, y]])
    cnt = 1
    while queue:
        p, q = queue.popleft()
        graph[p][q] = 0  # 큐 맨 앞 원소 방문
        for i in range(4):
            dp = p + dx[i]
            dq = q + dy[i]

            if dp < 0 or dp >= m or dq < 0 or dq >= n:
                continue
            if graph[dp][dq] == 1:
                graph[dp][dq] = 0
                queue.append([dp, dq])
                cnt += 1
    return cnt  # 연결된 정점의 갯수를 return


t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for _ in range(m)]  # 전체를 0으로 초기화
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1  # 심은 데만 1로 표기

    result = []

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                count = bfs(i, j)
                result.append(count)
    print(len(result))
