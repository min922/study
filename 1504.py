# https://www.acmicpc.net/problem/1504
import sys
import heapq


def dijkstra(start):
    queue = []
    distance = [INF for _ in range(n + 1)]
    heapq.heappush(queue, [start, 0])
    distance[start] = 0
    while queue:
        now, dist = heapq.heappop(queue)
        for node, d in graph[now]: # 현재 위치에 연결된 노드에 대해
            next_dist = dist + d # 연결된 노드로 가는 거리
            if distance[node] > next_dist: # 최단거리이면
                distance[node] = next_dist # 거리 저장
                heapq.heappush(queue, [node, next_dist]) # 다음 탐색
    return distance


INF = 10e9
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])  # 양방향 그래프
v1, v2 = map(int, sys.stdin.readline().split())

from1 = dijkstra(1)  # 1부터 시작하는 다익스트라
fromv1 = dijkstra(v1)  # v1부터 시작
fromv2 = dijkstra(v2)  # v2부터 시작

cnt = min(from1[v1] + fromv1[v2] + fromv2[n], from1[v2] + fromv2[v1] + fromv1[n])
# 1->v1->v2->n / 1->v2->v1->n 중 최단거리 출력

if cnt < INF:
    print(cnt)
else:
    print(-1)
