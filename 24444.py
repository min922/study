# https://www.acmicpc.net/problem/24444
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)  # 재귀 횟수 늘려주기


def bfs(R):
    global cnt
    visited[R] = cnt
    queue = deque([R])  # 시작점 추가
    while len(queue) != 0:
        u = queue.popleft()  # 맨 앞쪽 요소 pop
        graph[u].sort()  # 오름차순 정렬
        for elt in graph[u]:  # u과 연결된 그래프의 모든 점들에 대해
            if visited[elt] == 0:  # 방문한적이 0번이면
                cnt += 1  # 방문 횟수 늘리고
                visited[elt] = cnt  # 몇번째 방문인지 저장
                queue.append(elt)  # 큐에 elt추가


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 1
visited = [0 for _ in range(n + 1)]
bfs(r)
for i in range(1, n + 1):
    print(visited[i])
