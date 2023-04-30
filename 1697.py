# https://www.acmicpc.net/problem/1697
import sys
from collections import deque


def bfs(r):
    queue = deque([r])  # 시작 위치
    while queue:
        u = queue.popleft()
        if u == k:  # 원하는 위치에 도착하면
            return graph[u]  # 도착위치 return
        for i in (u - 1, u + 1, 2 * u):  # 갈 수 있는 위치에 대해
            if 0 <= i < MAX and not graph[i]:  # 범위 안이고 가지 않은 곳이라면
                graph[i] = graph[u] + 1  # 전칸에서 1초 추가
                queue.append(i)  # 큐에 다음위치 추가


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
graph = [0 for _ in range(MAX)]
print(bfs(n))
