# https://www.acmicpc.net/problem/1707
import sys
from collections import deque


def bfs(r):
    queue = deque([r])
    if visited[r] == 0:
        visited[r] = 1  # 방문 표시
    while queue:  # 이분그래프 : 각 집합에 속한 정점끼리 인접x -> 인접한 정점끼리는 다른 집합
        u = queue.popleft()
        check = visited[u]  # 집합 표시
        for elt in graph[u]:
            if visited[elt] == 0:  # 방문 안했으면
                queue.append(elt)  # 큐에 추가
                if check == 1:  # 1번집합과 연결되어 있으면
                    visited[elt] = 2  # 2번집합에 추가
                else:
                    visited[elt] = 1
            elif visited[elt] == check:  # 인접한 정점이 같은 집합이면
                return False  # 이분그래프아님
    return True


k = int(sys.stdin.readline().strip())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(v + 1)]
    tmp = 1
    for i in range(1, v + 1):
        if not bfs(i):
            tmp = 0
    if tmp:
        print("YES")
    else:
        print("NO")
