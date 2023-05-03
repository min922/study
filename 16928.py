# https://www.acmicpc.net/problem/16928
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dict = {}
visited = [0 for _ in range(107)]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    dict[a] = b


def bfs(r):
    queue = deque([r])
    while queue:
        u = queue.popleft()
        if u == 100:  # 100번째에 도착하면 return
            return visited[u]
        for i in range(1, 7):  # 주사위 1~6
            p = u + i
            if p <= 100 and visited[p] == 0:
                if p in dict.keys():  # 사다리나 뱀이 있으면
                    p = dict[p]  # 거기로 이동
                if visited[p] == 0:  # 이동한 데에 방문하지 않았으면
                    visited[p] = visited[u] + 1  # 방문횟수 늘리고
                    queue.append(p)  # 큐에 추가


print(bfs(1))
